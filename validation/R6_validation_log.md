# Nhật ký Kiểm chứng Người dùng Ngoài Nhóm (R6 Validation)

**Thời gian thực hiện:** 18/09/2026
**Mục tiêu:** Kiểm chứng prototype Bot Hỗ Trợ K4 với người dùng thật, đánh giá khả năng hiểu ngữ cảnh và xử lý lỗi theo nguyên tắc HAX.

## 1. Bảng Ghi Nhận Validation

| Người thử (Tên/Vai — Willing user?) | Task đã giao | Quan sát | Quote nguyên văn | Mức nghiêm trọng |
|---|---|---|---|---|
| Võ Trường An (Học viên K4 — Có) | Hỏi bot lịch nộp bài Lab 2 bằng ngôn ngữ mạng (viết tắt/teencode) xem bot có hiểu không. | Người dùng gõ "cho em hỏi đét lai lạp 2 là bh dợ?". Bot nháp ban đầu không hiểu "bh" (bao giờ) và "đét lai" (deadline) nên trả lời chung chung. Người thử lắc đầu nhận xét. | "Bình thường trên kênh chat bọn em toàn gõ tắt kiểu 'bh' với 'dl' cho nhanh, bot mà bắt gõ đúng chính tả 100% thì dùng ức chế lắm." | Cao (Học viên hay dùng từ viết tắt, bot RAG sẽ miss context nếu không có bước chuẩn hóa từ ngữ). |
| Phạm Đình Duy (Học viên K4 — Có) | Hỏi bot thời hạn nộp của một bài Lab không tồn tại (ví dụ Lab 7) để xem bot xử lý thiếu thông tin thế nào. | Người dùng hỏi "Hạn nộp bài Lab 10 là khi nào vậy bot, nếu không biết ãy nói ok?". Ở test run sớm, bot cố gắng đoán mò một ngày nộp bài thay vì báo lỗi. Người thử nhíu mày và chỉ tay vào màn hình. | "Thôi chết, Lab 10 làm gì có mà nó dám phán là ngày 20/10 nộp vậy? Thế này lỡ tin theo là toang." | Rất nghiêm trọng (Hallucination về deadline là lỗi chí mạng, vi phạm HAX G10). |

## 2. Tổng Hợp Thay Đổi (Cập nhật vào Spec)

- **Chủ đề lặp nhiều nhất:** Lỗi hiểu sai ngữ cảnh thực tế của học viên (teencode) và rủi ro bịa đặt thông tin khi thiếu dữ liệu nguồn.
- **Thay đổi đã làm:**
  1. Cập nhật System Prompt thêm bước `normalize_user_query` để giải mã teencode/viết tắt trước khi gọi tool.
  2. Bổ sung constraint bắt buộc gọi tool `escalate_to_ta` nếu không tìm thấy kết quả từ Knowledge Base (chống bịa đặt tuyệt đối).
- **Phần giữ nguyên có lý do:** Giao diện Web App giả lập Discord. (Lý do: Người dùng thấy cực kỳ quen thuộc, không mất thời gian onboarding).
- **Phần đưa vào backlog:** Thêm tính năng lưu trữ lịch sử chat dài hạn để học viên có thể cuộn xem lại các deadline đã hỏi.
