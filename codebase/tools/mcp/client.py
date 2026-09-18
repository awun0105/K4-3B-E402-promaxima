from __future__ import annotations

try:
    from codebase.tools.mcp.server import DiscordKBMcpServer
except (ImportError, ValueError):
    from .server import DiscordKBMcpServer


class DiscordKBMcpClient:
    """
    Model Context Protocol (MCP) Client for interacting with the course MCP Server.
    Provides decoupled, standardized tool execution and resource retrieval.
    """

    def __init__(self, server: Optional[DiscordKBMcpServer] = None) -> None:
        self.server = server or DiscordKBMcpServer()
        self._request_counter = 0

    def _next_id(self) -> int:
        self._request_counter += 1
        return self._request_counter

    def list_tools(self) -> List[Dict[str, Any]]:
        req = {"jsonrpc": "2.0", "id": self._next_id(), "method": "tools/list", "params": {}}
        resp = self.server.handle_jsonrpc(req)
        return resp.get("result", {}).get("tools", [])

    def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        req = {
            "jsonrpc": "2.0",
            "id": self._next_id(),
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments},
        }
        resp = self.server.handle_jsonrpc(req)
        return resp.get("result", {})

    def read_resource(self, uri: str) -> Dict[str, Any]:
        req = {
            "jsonrpc": "2.0",
            "id": self._next_id(),
            "method": "resources/read",
            "params": {"uri": uri},
        }
        resp = self.server.handle_jsonrpc(req)
        return resp.get("result", {})
