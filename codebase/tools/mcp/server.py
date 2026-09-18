from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from codebase.tools import TOOL_FUNCTIONS, load_tool_declarations
from codebase.tools._shared import ANNOUNCEMENTS_FILE
from codebase.tools.mcp.protocol import (
    JSONRPCRequest,
    JSONRPCResponse,
    MCPResourceDefinition,
    MCPToolDefinition,
)

ROOT_DIR = Path(__file__).resolve().parents[2]
TOOLS_YAML_PATH = ROOT_DIR / "artifacts" / "tools.yaml"


class DiscordKBMcpServer:
    """
    Model Context Protocol (MCP) Server for K4 Course Knowledge Base and Discord Assistant.
    Provides standard MCP methods:
      - tools/list: Returns registered MCP tools from tools.yaml.
      - tools/call: Dispatches execution to specific tool in TOOL_FUNCTIONS.
      - resources/list: Exposes knowledge base resources.
      - resources/read: Fetches raw knowledge base announcements.
    """

    def __init__(self, tools_yaml_path: Optional[Path] = None) -> None:
        self.tools_path = tools_yaml_path or TOOLS_YAML_PATH
        self.tool_declarations = load_tool_declarations(self.tools_path)

    def list_tools(self) -> List[Dict[str, Any]]:
        result = []
        for decl in self.tool_declarations:
            mcp_tool = MCPToolDefinition(
                name=decl["name"],
                description=decl.get("description", ""),
                inputSchema=decl.get("parameters", {"type": "object", "properties": {}}),
            )
            result.append(mcp_tool.to_dict())
        return result

    def list_resources(self) -> List[Dict[str, Any]]:
        return [
            MCPResourceDefinition(
                uri="k4://knowledge-base/announcements",
                name="K4 Official Announcements Knowledge Base",
                description="List of all official deadlines, deliverables, and submission guidelines.",
            ).to_dict()
        ]

    def read_resource(self, uri: str) -> Dict[str, Any]:
        if uri == "k4://knowledge-base/announcements":
            content = ANNOUNCEMENTS_FILE.read_text(encoding="utf-8") if ANNOUNCEMENTS_FILE.exists() else "[]"
            return {
                "contents": [
                    {
                        "uri": uri,
                        "mimeType": "application/json",
                        "text": content,
                    }
                ]
            }
        return {"error": {"code": -32602, "message": f"Resource not found: {uri}"}}

    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        func = TOOL_FUNCTIONS.get(name)
        if not func:
            return {
                "isError": True,
                "content": [{"type": "text", "text": f"Error: Tool '{name}' not found."}],
            }
        try:
            res = func(**arguments)
            return {
                "isError": False,
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(res, ensure_ascii=False),
                    }
                ],
            }
        except Exception as exc:
            return {
                "isError": True,
                "content": [{"type": "text", "text": f"Execution error: {str(exc)}"}],
            }

    def handle_jsonrpc(self, request: Dict[str, Any]) -> Dict[str, Any]:
        req_id = request.get("id")
        method = request.get("method")
        params = request.get("params", {})

        if method == "tools/list":
            return JSONRPCResponse(id=req_id, result={"tools": self.list_tools()}).__dict__
        elif method == "tools/call":
            name = params.get("name")
            arguments = params.get("arguments", {})
            return JSONRPCResponse(id=req_id, result=self.call_tool(name, arguments)).__dict__
        elif method == "resources/list":
            return JSONRPCResponse(id=req_id, result={"resources": self.list_resources()}).__dict__
        elif method == "resources/read":
            uri = params.get("uri")
            return JSONRPCResponse(id=req_id, result=self.read_resource(uri)).__dict__
        else:
            return JSONRPCResponse(
                id=req_id,
                error={"code": -32601, "message": f"Method not found: {method}"},
            ).__dict__
