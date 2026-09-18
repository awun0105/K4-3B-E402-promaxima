from __future__ import annotations

import re
from typing import Any

try:
    from .._shared import TEENCODE_MAPPINGS, err
except (ImportError, ValueError):
    from tools._shared import TEENCODE_MAPPINGS, err


def normalize_user_query(raw_query: str = "") -> dict[str, Any]:
    """
    Clean, de-noise, and normalize user messages from Discord.
    Strips [@BOT] tags, removes redundant spaces, detects entities (Lab, Gate, CP),
    and normalizes common Vietnamese teencode / slang into standard terminology.
    """
    try:
        text = raw_query or ""
        if not text.strip():
            return {
                "tool": "normalize_user_query",
                "original": raw_query,
                "normalized": "",
                "is_empty": True,
                "detected_entities": [],
            }

        # 1. Remove Discord bot tags [@BOT], <@123456>, etc.
        cleaned = re.sub(r"\[@BOT\]|<@!?[0-9]+>", "", text, flags=re.IGNORECASE).strip()

        if not cleaned:
            return {
                "tool": "normalize_user_query",
                "original": raw_query,
                "normalized": "",
                "is_empty": True,
                "detected_entities": [],
            }

        # 2. Detect entities
        detected: list[str] = []
        for lab_idx in range(1, 10):
            if re.search(rf"\b(lab|lạp)\s*{lab_idx}\b", cleaned, re.IGNORECASE):
                detected.append(f"Lab {lab_idx}")
        if re.search(r"\bgate\s*1\b", cleaned, re.IGNORECASE):
            detected.append("Gate 1")
        cp_match = re.search(r"\b(cp[1-6]|checkpoint\s*[1-6])\b", cleaned, re.IGNORECASE)
        if cp_match:
            detected.append(cp_match.group(0).upper())

        # 3. Replace teencode
        normalized = cleaned
        for slang, standard in TEENCODE_MAPPINGS.items():
            pattern = rf"\b{re.escape(slang)}\b"
            normalized = re.sub(pattern, standard, normalized, flags=re.IGNORECASE)

        return {
            "tool": "normalize_user_query",
            "original": raw_query,
            "normalized": normalized,
            "is_empty": False,
            "detected_entities": detected,
        }
    except Exception as exc:
        return err("normalize_user_query", exc)
