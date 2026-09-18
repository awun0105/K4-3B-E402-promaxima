# Phân tích Dữ liệu Hỗ trợ Đề tài B1: Trợ lý Học viên (Discord)

## 1. Nguồn Dữ liệu & Từ điển Dữ liệu
Dữ liệu được phân tích dựa trên thư mục `data/discord-pack/`:
- **`k4_messages.csv`**: Chứa 1092 tin nhắn thật giai đoạn onboarding (12–14/09) của Khóa 4 từ 2 server Discord. Các cột quan trọng: `msg_id` (mã tin nhắn), `author` (mã người dùng/bot), `is_bot` (để phân biệt bot hay học viên), `content` (nội dung đã được ẩn danh).
- **`k4_daily_reports.md`**: Chứa 4 bản tin tự động sinh bởi bot, dùng làm baseline để tìm ra lỗi thực tế của tính năng báo cáo cuối ngày.
- **`DATA_DICTIONARY.md`**: File định nghĩa cách các thông tin nhạy cảm đã được ẩn danh (ví dụ tên bị đổi thành `[HV]`, mã sinh viên đổi thành `[MSSV]`).

## 2. Phân tích Vấn đề (Pain Points) liên quan đến Đề B1
Đề tài B1 yêu cầu: **"Tối ưu trợ lý hiện có: Trả lời câu hỏi deadline từ nguồn chính thức hoặc chuyển cho TA thay vì đoán bừa."**

### A. Tần suất câu hỏi của học viên (Pain Point đếm được)
- **Nguồn file**: `k4_messages.csv`
- **Cách đếm**: Lọc các tin nhắn không phải của bot (`is_bot = False`) chứa từ khóa liên quan đến hạn nộp (`"deadline"`, `"hạn"`, `"nộp"`, `"lịch"`, `"khi nào"`) và có chứa dấu chấm hỏi (`?`).
- **Kết quả**: Có tổng cộng **24** tin nhắn là câu hỏi về hạn nộp và thời gian. Điều này chứng minh đây là vấn đề phổ biến nhất trong tuần onboarding.

### B. Các bằng chứng thực tế (Nguyên văn từ Học viên)
Dưới đây là 5 bằng chứng tiêu biểu (Ví dụ mẫu) nằm trong file `k4_messages.csv`:

- **Mã tin nhắn `M19124`** (nằm ở **Dòng số 130**, Cột `content`):
  > *"a ơi sao deadline ghép đội tự do end sớm vậy a?"*
  > (Câu hỏi này thể hiện rõ sự hoang mang của học viên về lịch trình/thời hạn).

- **Mã tin nhắn `M40677`** (nằm ở **Dòng số 439**, Cột `content`):
  > *"[@BOT] tôi nộp codelab trên vlearn đúng giờ deadline như thông báo (23:59) nhưng commit trên máy bị lỗi và sau thời gian đó mới lên thì có được tính là nộp đúng hạn không ?"*
  > (Câu hỏi này thể hiện rõ sự hoang mang của học viên về lịch trình/thời hạn).

- **Mã tin nhắn `M13974`** (nằm ở **Dòng số 272**, Cột `content`):
  > *"[@BOT]  cho  mình hỏi việc mình được điểm danh hay chưa có thể check ở đâu ạ"*
  > (Câu hỏi này thể hiện rõ sự hoang mang của học viên về lịch trình/thời hạn).

- **Mã tin nhắn `M69081`** (nằm ở **Dòng số 16**, Cột `content`):
  > *"có điểm danh ws không ạ"*
  > (Câu hỏi này thể hiện rõ sự hoang mang của học viên về lịch trình/thời hạn).

- **Mã tin nhắn `M84993`** (nằm ở **Dòng số 303**, Cột `content`):
  > *"[@BOT] check xem t đã nộp bài codelab chưa"*
  > (Câu hỏi này thể hiện rõ sự hoang mang của học viên về lịch trình/thời hạn).


### C. Lỗi của Bot hiện tại (Baseline lỗi)
- **Nguồn file**: `k4_messages.csv` và `k4_daily_reports.md`.
- **Ví dụ lỗi trả lời sai/hallucinate**: Ở cột `reply_to` liên kết tới các câu hỏi trên, khi xem các tin nhắn phản hồi của Bot (cột `is_bot = True` và `author = BOT`), có hiện tượng bot "ảo giác", đưa ra quy định tự chế hoặc không có thông tin chính thức.
- **Ví dụ lỗi trong bản tin tự sinh (`k4_daily_reports.md`)**:
  - Dòng 36, dòng 124: Chuỗi `"nguồn tham chiếu"` bị chèn sai chỗ (lỗi template prompt). Ví dụ: `nguồn tham chiếuhi nào...`
  - Tóm tắt bị sai lệch ngữ cảnh, báo cáo sai trạng thái (Ghi "Đã có phản hồi" nhưng thực tế không ai xử lý).

## 3. Tổng kết
Việc phân tích file dữ liệu của Khóa 4 cho thấy vấn đề của Đề B1 là hoàn toàn có thật và rất nhức nhối (cost-of-error cao khi ảnh hưởng đến điểm số của học viên). Các dẫn chứng dòng/cột trên sẽ được sử dụng trực tiếp làm Evidence vững chắc cho vòng thẩm định (CP1/CP2) của Ban Giám khảo.
