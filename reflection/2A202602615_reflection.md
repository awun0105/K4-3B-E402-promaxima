# Thu Hoạch Cá Nhân - Nguyễn Văn Diện (2A202602615)

## 1. Vai trò cá nhân
**Lead Engineer & Agent Architecture**

## 2. Phần việc trực tiếp phụ trách
- Xây dựng kiến trúc hệ thống Agent Loop và cơ chế Tool Calling cho Bot.
- Lập trình backend xử lý Python (`server.py`, `chat.py`) kết nối với API của LLM.
- Tối ưu hóa System Prompt để điều phối hành vi của Bot theo đúng luồng thiết kế.
- Tái cấu trúc codebase theo hướng Decoupled, dễ dàng thay đổi Model.

## 3. Cách ứng dụng AI trong quá trình xây dựng
- Dùng AI Coding Agent (GitHub Copilot / Cursor) để sinh boilerplate cho Server và xử lý parse JSON.
- Dùng AI như một "hacker" tấn công thử (Prompt Injection) xem Bot có vượt rào không, từ đó vá lỗ hổng System Prompt.

## 4. Bài học thực tế từ thất bại của nhóm
- **Kiểm soát Ảo giác (Hallucination):** Ban đầu bot tự bịa ra ngày nộp của "Lab 7" không tồn tại. Bài học: Tuyệt đối không dùng Prompt suông để ngăn ảo giác, mà phải dùng **Tool Constraint** (ép logic code gọi `escalate_to_ta` khi không tìm thấy kết quả).
- **Thảm họa quản lý phiên bản Git:** Sát deadline, do team lỏng lẻo kỷ luật, tôi và các bạn cuống cuồng push đè code lên `main` gây conflict vỡ nát toàn bộ hệ thống backend. Bài học chung của cả team: Kỷ luật Git Branch và Pull Request là yếu tố sống còn của làm việc nhóm, nếu không code sẽ tự dẫm chân lên nhau.
- **Prompt mập mờ khiến Agent coding sai:** Khi dùng AI Copilot để viết cấu trúc vòng lặp Tool Calling, do tôi viết prompt đầu vào mập mờ, AI đã hiểu sai luồng logic, sinh code rác gây hỏng toàn bộ pipeline. Bài học: Giao task cho AI code đòi hỏi kỹ năng Prompt sắc bén, cung cấp đủ ngữ cảnh kiến trúc thì hệ thống mới không bị AI "phá".
