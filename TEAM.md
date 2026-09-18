# TEAM — Day04 / Hackathon K4-L3B

**Nhóm Promaxima · Phòng E402 · Track B — Trợ lý Học viên Discord.**

## Thông tin bài nộp

- Tên nhóm: Promaxima
- Người đại diện / MSSV: Lâm Quang Anh Quân — 2A202602467
- Tên repo: `K4-3B-E402-promaxima`
- URL repo: https://github.com/VinUni-AI20k/K4-3B-E402-promaxima
- Lĩnh vực: Trợ lý Discord Hỗ trợ Học viên (Báo Deadline Chuẩn & Giải đáp Quy chế K4)
- Deadline áp dụng: 23:59:00 ngày 18/09/2026 (Asia/Ho_Chi_Minh)

## Thành viên

| Họ và tên | MSSV | GitHub | Vai trò chính | Phần việc đảm nhiệm trong dự án |
|---|---|---|---|---|
| Lâm Quang Anh Quân | 2A202602467 | `@anhquan-vinuni` | Trưởng nhóm / Product Lead | Thiết kế Spec, Canvas, luồng hội thoại HAX/PAIR, UI Discord Web Mock |
| Bùi Văn Quang | 2A202602688 | `@quangbv-vinuni` | Lead Engineer | Kiến trúc Agent Loop, Tool Calling, System Prompt, Decoupled Providers |
| Nguyễn Văn Diện | 2A202602615 | `@diennv-vinuni` | QA & Eval Engineer | Xây dựng bộ Golden Set 24 cases, Dataset 10 cases nhóm, Eval runner, Benchmarks |

## Nhận xét chung

- **Kết quả và bằng chứng:** Đạt 100% tỷ lệ chính xác (24/24 cases) trên bộ Golden Set và 100% trên bộ mở rộng, 0% hallucination trên các câu hỏi không có dữ liệu nguồn (Lớp 1 kích hoạt 100% ESCALATE_TO_TA).
- **Thay đổi hiệu quả nhất:**
  1. Tách biệt kiến trúc thành Tool Calling modular theo chuẩn Day04 (`tools/`, `providers/`, `artifacts/`).
  2. Bổ sung `normalize_user_query` loại bỏ bot tag Discord và chuẩn hóa teencode tiếng Việt.
  3. Áp dụng HAX G10 và prompt 4 lớp khó phân định rõ ràng giữa `ANSWER`, `CLARIFY`, `OUT_OF_SCOPE`, `POLICY_VIOLATION`, `ESCALATE_TO_TA`.
- **Giới hạn còn lại:** Phụ thuộc vào độ trễ mạng khi gọi live LLM OpenRouter/OpenAI API (~1.5s - 2.5s mỗi lượt).
- **Cách phân công và tích hợp:** Chia việc theo lát cắt rõ ràng, commit theo tính năng và tích hợp liên tục qua bộ chạy eval tự động.

## INDIVIDUAL

### Lâm Quang Anh Quân — 2A202602467

- **Phần việc:** Viết và hoàn thiện `spec.md`, `canvas.md`, thiết kế trải nghiệm người dùng theo 18 nguyên tắc HAX (đặc biệt G10 và G11).
- **Quyết định & xử lý:** Lựa chọn giải pháp Bot Discord giả lập Web UI để dễ dàng chứng minh luồng AI và cost-of-error thấp thay vì triển khai bot Discord phức tạp.
- **Điều đã học:** Cách phân rã một bài toán AI thành 4 lớp chỗ khó và cách thiết lập conditional automation phù hợp.
- **AI/công cụ đã dùng:** Antigravity CLI, Gemini 3.8 Flash, VS Code.
- **Thời điểm nộp URL trên VLearn:** 18/09/2026.

### Bùi Văn Quang — 2A202602688

- **Phần việc:** Lập trình `agent.py`, `chat.py`, xây dựng các tool (`normalize_user_query`, `search_knowledge_base`, `check_safety_and_policy`, `clarify`, `escalate_to_ta`), hoàn thiện `artifacts/system_prompt.md` và `artifacts/tools.yaml`.
- **Quyết định & xử lý:** Tái cấu trúc toàn bộ code từ monolithic sang mô hình modular của Day04 `codebase`, hỗ trợ tool calling chuẩn OpenAPI/JSON Schema.
- **Điều đã học:** Kỹ thuật Prompt Engineering định hướng tool calling, quản lý version artifact bằng SHA-256 hash.
- **AI/công cụ đã dùng:** OpenRouter API (`gpt-4o-mini`), OpenAI SDK.
- **Thời điểm nộp URL trên VLearn:** 18/09/2026.

### Nguyễn Văn Diện — 2A202602615

- **Phần việc:** Khai phá dữ liệu từ `k4_messages.csv`, xây dựng Golden Set 24 cases theo ma trận 4 chiều (Grounding × Clarity × Intent × Expected Action), viết script `run_eval.py` và đo lường qua các phiên bản v0, v1, v2, v3.
- **Quyết định & xử lý:** Phát hiện lỗi Over-clarification ở Run 1 và đề xuất bộ quy tắc phân định câu hỏi gộp ý trong Prompt v2, nâng tỷ lệ pass từ 75% lên 100%.
- **Điều đã học:** Phương pháp xây dựng golden benchmark và kiểm thử tự động cho LLM Agent.
- **AI/công cụ đã dùng:** Python 3.11, pandas, script eval harness.
- **Thời điểm nộp URL trên VLearn:** 18/09/2026.
