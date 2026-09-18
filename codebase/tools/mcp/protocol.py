from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class MCPToolDefinition:
    name: str
    description: str
    inputSchema: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "inputSchema": self.inputSchema,
        }


@dataclass
class MCPResourceDefinition:
    uri: str
    name: str
    mimeType: str = "application/json"
    description: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "uri": self.uri,
            "name": self.name,
            "mimeType": self.mimeType,
            "description": self.description,
        }


@dataclass
class JSONRPCRequest:
    jsonrpc: str = "2.0"
    id: Optional[str | int] = 1
    method: str = ""
    params: Optional[Dict[str, Any]] = field(default_factory=dict)


@dataclass
class JSONRPCResponse:
    jsonrpc: str = "2.0"
    id: Optional[str | int] = 1
    result: Optional[Any] = None
    error: Optional[Dict[str, Any]] = None
