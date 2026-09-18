from __future__ import annotations

from typing import Any

try:
    from .._shared import err
except (ImportError, ValueError):
    from tools._shared import err


def escalate_to_ta(
    reason: str = "no_grounding",
    user_query: str = "",
    student_id: str | None = None,
) -> dict[str, Any]:
    """
    Escalate inquiry to Teaching Assistants (TAs) or Lab Coaches on Discord.
    Used when a requested deadline/event has not been officially announced (Lớp 1 Grounding),
    or when personal attendance/grades data is requested that the bot cannot access.
    """
    try:
        return {
            "tool": "escalate_to_ta",
            "status": "escalated",
            "tag": "@TA",
            "reason": reason,
            "user_query": user_query,
            "student_id": student_id,
            "handoff_message": (
                "Thông tin này hiện chưa có trong thông báo chính thức của BTC. "
                "Mình đã tag @TA vào thread này để hỗ trợ bạn sớm nhất nhé!"
            ),
        }
    except Exception as exc:
        return err("escalate_to_ta", exc)
