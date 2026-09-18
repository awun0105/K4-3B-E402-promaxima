---
name: normalize_user_query
track: core
kind: text_processing
provider: python_regex
requires_env: []
inputs: [raw_query]
outputs: [normalized, is_empty, detected_entities]
side_effect: false
---
# normalize_user_query

Chuẩn hóa câu hỏi đầu vào từ học viên trên Discord:
- Loại bỏ các tag bot dạng `[@BOT]`, `<@123456>`.
- Phát hiện tin nhắn rỗng / spam.
- Giải mã và chuẩn hóa các từ lóng (teencode), ví dụ: `đét lai` -> `deadline`, `lạp 2` -> `Lab 2`, `ở mô zậy` -> `ở đâu vậy`.
- Tự động trích xuất các thực thể học tập: `Lab 1`, `Lab 2`, `Gate 1`, `CP1` - `CP6`.
