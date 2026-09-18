---
name: check_safety_and_policy
track: core
kind: safety_filter
provider: regex_policy_rules
requires_env: []
inputs: [query]
outputs: [flags, suggested_action, is_safe, num_flags]
side_effect: false
---
# check_safety_and_policy

Kiểm tra tính an toàn và ranh giới chính sách của câu hỏi:
- Phát hiện Prompt Injection và nỗ lực jailbreak (Lớp 4).
- Phát hiện yêu cầu xin nộp muộn / phá vỡ quy chế (Lớp 4).
- Phát hiện yêu cầu giải bài tập / viết code hộ (Lớp 3 - Out-of-Scope).
- Phát hiện yêu cầu tra cứu dữ liệu điểm danh cá nhân (Lớp 1 - Grounding / Cần tag TA).
- Phát hiện câu hỏi về khóa học ngoài phạm vi AI20K K4.
