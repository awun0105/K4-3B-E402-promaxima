from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

# Core Discord Assistant Tools (Domain-specific Track B)
from .search_knowledge_base.tool import search_knowledge_base
from .normalize_user_query.tool import normalize_user_query
from .check_safety_and_policy.tool import check_safety_and_policy
from .escalate_to_ta.tool import escalate_to_ta
from .clarify.tool import ask_user

TOOL_FUNCTIONS = {
    # --- Discord Assistant Core Registry ---
    "search_knowledge_base": search_knowledge_base,
    "normalize_user_query": normalize_user_query,
    "check_safety_and_policy": check_safety_and_policy,
    "escalate_to_ta": escalate_to_ta,
    "clarify": ask_user,
}


def load_tool_declarations(path: Path) -> list[dict[str, Any]]:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))["tools"]


def to_openai_tools(declarations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{
        "type": "function",
        "function": {
            "name": item["name"],
            "description": item.get("description", ""),
            "parameters": item.get("parameters", {"type": "object", "properties": {}}),
        },
    } for item in declarations]
