# Thu Hoạch Cá Nhân - Lâm Quang Anh Quân (2A202602467)

## 1. Vai trò cá nhân
**Nhóm trưởng (Team Leader), Product Lead & UX/Spec, Quản lý Repo**

## 2. Phần việc trực tiếp phụ trách
- Đảm nhiệm vai trò **Nhóm trưởng**, lên kế hoạch phân công, theo dõi và đôn đốc tiến độ dự án.
- **Quản lý kho mã nguồn (Repo Management)**, điều phối việc đẩy code lên GitHub và kiểm soát các nhánh.
- Thiết kế **UI/UX** cho Web App giả lập Discord, đảm bảo trải nghiệm thân thiện, quen thuộc cho học viên.
- Khai thác insight từ dữ liệu Discord (`data-analysis.md`), chốt Spec định hướng sản phẩm (§1-§2) và thiết kế luồng hội thoại HAX.

## 3. Cách ứng dụng AI trong quá trình xây dựng
- Dùng AI (Gemini/Claude) để sinh nhanh các block TailwindCSS, hỗ trợ tinh chỉnh bố cục UI.
- Dùng AI để hỗ trợ parse và gom cụm các tin nhắn thô từ file CSV, tìm ra con số 43/1.092 tin nhắn về deadline.
- AI làm rất tốt việc hỗ trợ thiết kế UI, nhưng tôi phải dùng Human-in-the-loop để rà soát số liệu thực tế tránh ảo giác.

## 4. Bài học thực tế từ thất bại của nhóm
- **Thảm họa quản lý phiên bản Git:** Dù là nhóm trưởng và quản lý repo, tôi đã thiếu kỷ luật lúc sát deadline, để cả nhóm cùng cuống cuồng push đè code trực tiếp lên nhánh `main`. Kết quả là conflict nát bét cả UI lẫn backend. Bài học chung của cả team: Làm việc nhóm bắt buộc phải dùng Git Branch, chia feature riêng và thực hiện Pull Request đàng hoàng.
- **Thiếu đồng bộ công việc:** Do tôi chỉ nêu ý tưởng mà không chốt rõ API Spec giữa frontend và backend, dẫn đến UI của tôi và code của Dev bị lệch pha, mất nhiều thời gian sửa chữa. Bài học: Cần có bản "hợp đồng giao tiếp" trước khi bắt tay làm.
- **Prompt mập mờ khiến Agent coding sai:** Khi cả team dùng AI Agent (Copilot) để viết code, do cung cấp prompt quá chung chung, AI đã sinh ra code rác làm hỏng vòng lặp tool calling và rò rỉ dữ liệu. Bài học: Giao việc cho AI Agent cũng phải chi tiết, chia nhỏ vấn đề và định nghĩa đầu ra cực kỳ rõ ràng y như giao cho con người.
