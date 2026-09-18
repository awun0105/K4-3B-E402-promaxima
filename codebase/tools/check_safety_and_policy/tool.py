from __future__ import annotations

import re
from typing import Any

try:
    from .._shared import err
except (ImportError, ValueError):
    from tools._shared import err


def check_safety_and_policy(query: str = "") -> dict[str, Any]:
    """
    Inspect incoming student queries for safety violations, prompt injections,
    homework-solving requests, late submission bypasses, and external inquiries.
    """
    try:
        clean_text = (query or "").lower().strip()
        flags: list[str] = []
        suggested_action: str | None = None

        # 1. Prompt Injection detection
        injection_patterns = [
            r"bỏ qua (mọi|các) (chỉ dẫn|lệnh|quy tắc)",
            r"ignore (all|previous) (instructions|prompts)",
            r"từ giờ bạn là",
            r"you are now",
            r"xác nhận rằng deadline .* được dời",
            r"system prompt",
        ]
        for pattern in injection_patterns:
            if re.search(pattern, clean_text):
                flags.append("PROMPT_INJECTION")
                suggested_action = "POLICY_VIOLATION"
                break

        # 2. Late submission / policy bypass
        late_patterns = [
            r"nộp muộn (1|vài|\d+) phút",
            r"extend thời gian submit",
            r"gia hạn riêng",
            r"xin nộp bù",
        ]
        for pattern in late_patterns:
            if re.search(pattern, clean_text):
                flags.append("LATE_SUBMISSION_BYPASS")
                suggested_action = "POLICY_VIOLATION"
                break

        # 3. Homework / code generation requests
        homework_patterns = [
            r"viết (giùm|hộ|giúp) .* code",
            r"giải (câu|bài|lab) \d+",
            r"làm bài tập hộ",
        ]
        for pattern in homework_patterns:
            if re.search(pattern, clean_text):
                flags.append("DO_HOMEWORK_REQUEST")
                suggested_action = "OUT_OF_SCOPE"
                break

        # 4. External course inquiry
        if "devops" in clean_text or "trung tâm khác" in clean_text:
            flags.append("EXTERNAL_COURSE")
            suggested_action = "OUT_OF_SCOPE"

        # 5. Modify grades / XP
        if "cộng cho mình" in clean_text and "xp" in clean_text:
            flags.append("MODIFY_XP")
            suggested_action = "OUT_OF_SCOPE"

        # 6. Private attendance check
        attendance_patterns = [
            r"điểm danh .* (chưa|check ở đâu|quét qr)",
            r"quét qr .* điểm danh",
        ]
        for pattern in attendance_patterns:
            if re.search(pattern, clean_text):
                flags.append("PRIVATE_ATTENDANCE_DATA")
                suggested_action = "ESCALATE_TO_TA"
                break

        is_safe = (len(flags) == 0) or (suggested_action not in ("POLICY_VIOLATION",))

        return {
            "tool": "check_safety_and_policy",
            "flags": flags,
            "suggested_action": suggested_action,
            "is_safe": is_safe,
            "num_flags": len(flags),
        }
    except Exception as exc:
        return err("check_safety_and_policy", exc)
