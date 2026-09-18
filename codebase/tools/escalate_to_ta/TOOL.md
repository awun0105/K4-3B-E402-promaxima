---
name: escalate_to_ta
track: core
kind: human_handoff
provider: discord_notification
requires_env: []
inputs: [reason, user_query, student_id]
outputs: [status, tag, handoff_message]
side_effect: true
---
# escalate_to_ta

Chuyển tiếp câu hỏi cho Giảng viên / Trợ giảng (TA) hoặc Lab Coach trên Discord:
- Áp dụng nguyên tắc HAX G10: Thu hẹp phạm vi / nhường quyền khi nghi ngờ hoặc thiếu dữ liệu.
- Kích hoạt khi học viên hỏi về các mốc sự kiện/Lab tương lai chưa từng được BTC công bố (Lớp 1).
- Kích hoạt khi học viên hỏi về dữ liệu cá nhân (điểm danh, điểm số cá nhân) mà bot không có thẩm quyền truy cập.
- Tự động tag `@TA` và tạo tin nhắn bàn giao lịch sự.
