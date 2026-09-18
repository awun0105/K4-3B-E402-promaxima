from __future__ import annotations

import json
from pathlib import Path
from typing import Any

try:
    from .._shared import ANNOUNCEMENTS_FILE, DISCORD_DATA_DIR, err, fold_text, terms
except (ImportError, ValueError):
    from tools._shared import ANNOUNCEMENTS_FILE, DISCORD_DATA_DIR, err, fold_text, terms


def _load_announcements() -> list[dict[str, Any]]:
    if not ANNOUNCEMENTS_FILE.exists():
        return []
    try:
        return json.loads(ANNOUNCEMENTS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []


def search_knowledge_base(
    query: str = "",
    announcement_id: str = "",
    top_k: int = 3,
) -> dict[str, Any]:
    """
    Search official course announcements, deadlines, deliverables, and policies.
    Can filter by query string or exact announcement_id (e.g. 'ANN-GATE-01', 'ANN-LAB-02').
    """
    try:
        records = _load_announcements()
        ann_id = (announcement_id or "").strip().upper()
        clean_query = (query or "").strip().lower()

        # Exact announcement ID match
        if ann_id:
            for item in records:
                if item.get("id", "").upper() == ann_id:
                    return {
                        "tool": "search_knowledge_base",
                        "status": "success",
                        "hits": [item],
                        "total_found": 1,
                    }
            return {
                "tool": "search_knowledge_base",
                "status": "not_found",
                "message": f"Announcement with ID '{ann_id}' not found.",
                "hits": [],
                "total_found": 0,
            }

        if not clean_query:
            return {
                "tool": "search_knowledge_base",
                "status": "success",
                "hits": records[:top_k],
                "total_found": len(records),
            }

        query_tokens = terms(clean_query)
        scored_hits: list[tuple[int, dict[str, Any]]] = []

        for item in records:
            haystack = " ".join([
                item.get("id", ""),
                item.get("topic", ""),
                item.get("policy", ""),
                item.get("deadline", ""),
                " ".join(item.get("deliverables", [])),
                item.get("submission_method", ""),
            ])
            haystack_tokens = terms(haystack)
            score = len(query_tokens & haystack_tokens)

            # Substring bonus
            if fold_text(clean_query) in fold_text(haystack):
                score += 5

            if score > 0:
                scored_hits.append((score, item))

        scored_hits.sort(key=lambda x: x[0], reverse=True)
        results = [item for _, item in scored_hits[:top_k]]

        return {
            "tool": "search_knowledge_base",
            "status": "success" if results else "no_match",
            "hits": results,
            "total_found": len(scored_hits),
        }
    except Exception as exc:
        return err("search_knowledge_base", exc)
