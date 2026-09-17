# Template AI Spec *(spec.md — commit trước hạn chốt spec: 21:00 18/9, tại CP4 · quality bar chốt từ thời điểm nộp)*

> Cấu trúc phủ đúng "SPEC 8 phần" của chương trình: Bằng chứng (§1-§2) · Lát cắt (§4) · Canvas (đính kèm CP1) · Augment/Automate (§4) · 4 đường đi của trải nghiệm (§6) · Kiểu lỗi (§5) · Kiểm thử (§7) · Phân công (§8). Hướng dẫn viết từng mục: `02-guide.md`.

# AI SPEC — [Tên lát cắt] · Nhóm [] · Zone [4]
Hướng: [ ] A — VLearn  [x] B — Trợ lý Học viên  [ ] C — Làn mở
Loại: [ ] Tối ưu tính năng có sẵn  [ ] Tính năng mới

## §1. User & Job
- Job executor + workflow: Học viên khóa AI Thực Chiến trên Discord muốn xác nhận thời hạn (deadline) nộp bài chính xác cho Lab/bài tập sắp tới.
- Core JTBD: Xác nhận chính xác thời hạn nộp bài để đảm bảo tiến độ và không bị trừ điểm.
- Problem statement: Học viên muốn tra cứu/xác nhận deadline nhưng bị bot hiện tại tự suy đoán từ thảo luận cũ đưa ra ngày sai, hoặc bị trôi tin nhắn quá lâu không được phản hồi, dẫn đến nộp bài muộn, mất điểm và hoang mang.
- Evidence:
  - Số liệu mining: Dựa trên phân tích `discord-pack/k4_messages.csv`, lọc với từ khóa `("deadline" OR "hạn" OR "nộp" OR "lịch" OR "khi nào")` kết hợp với dấu `?`. Kết quả: **43/1.092** tin nhắn là câu hỏi về deadline. Trong đó, **15/43** tin nhắn nhận câu trả lời tự đoán sai hoặc không được phản hồi sau 4 tiếng.
  - 5 ví dụ nguyên văn: `D0145`, `D0278`, `D0412`, `D0652`, `D0891` (Log chi tiết trong thư mục `eval/evidence/`).

## §2. Impact & quyết định chọn
- Bảng impact:

| Ứng viên | Người gặp/tần suất | Mỗi lần tốn gì | Khả thi (Build) | Chọn? |
|---|---|---|---|---|
| Phan Danh Đạt (2A202602627) | Cao (nhiều học viên hỏi deadline) | Mất điểm, hoang mang | Cao | Có |
| Võ Trường An (2A20262656) | Thấp (chỉ vài người cần) | Mất thời gian tìm thông tin | Trung bình | Loại |
| Phạm Đình Duy (2A202602913) | Trung bình (cần tài liệu) | Mất thời gian chờ phản hồi | Trung bình | Loại |

- Ứng viên ĐÃ LOẠI:
  - Võ Trường An: Vấn đề ít phổ biến, không gây ảnh hưởng lớn đến tiến độ chung của khoá học.
  - Phạm Đình Duy: Vấn đề mang tính chất cá nhân, không phải nỗi đau chung của nhiều học viên.
- Ứng viên CHỌN (Phan Danh Đạt):
  - Vì bằng chứng mining data cho thấy đây là nỗi đau rất rõ rệt (43/1092 tin nhắn, 15/43 tin nhắn bị lỗi), ảnh hưởng trực tiếp đến kết quả học tập (nộp muộn) của nhiều học viên, và giải pháp có thể kiểm chứng được bằng cơ sở dữ liệu thông báo chính thức.

## §3. Giải pháp tương tự đã nghiên cứu
- [Sản phẩm 1]: flow / đáng học / đáng né / mình khác gì
- [Sản phẩm 2]: ...

## §4. Thiết kế
- Lát cắt MỘT CÂU (1 user · 1 việc · 1 quyết định AI · 1 kết quả):
- Non-goals (≥3 thứ KHÔNG build):
- Mức prototype nhắm tới: [ ] Sketch [ ] Mock [ ] Working — phần nào mock, phần nào thật:
- Automation: [ ] augment [ ] conditional [ ] automate — lý do theo cost-of-error:
- §4b. Nguyên tắc đã áp dụng (≥4 — HAX/PAIR, xem guide):
  | Nguyên tắc | Áp cụ thể vào đâu trong prototype |
  |---|---|

## §5. Kiểu lỗi — 4 lớp chỗ khó + kịch bản (≥8) [bảng theo guide §2.5]

## §6. Bốn đường đi của trải nghiệm
- Happy path: · Low-confidence (②): · Failure/không căn cứ (①): · Correction (user sửa):
- Khi bị đòi ngoài phạm vi (③): · Case đặc thù domain (④):

## §7. Kiểm thử
- Chiều chất lượng + định nghĩa kiểm chứng được:
- Golden set (≥20 case theo cơ cấu trong guide §2.6, file trong eval/):
- Quality bar (chốt từ hạn chốt spec của khoá, giữ nguyên sau đó): "Đạt khi ≥ ___% qua bộ, và ___"
- Kết quả các lượt chạy (bảng % — cập nhật đến trước CP6):

## §8. Phân công & kế hoạch
- Phân công có tên: spec / evidence / prompt / code / demo
- Willing users (≥2 tên) + kế hoạch vòng validation *(bonus, nếu làm)*:
- Multi-prototype (nếu làm): trục khác biệt của ≥2 phương án + lý do chọn:

## §9. Changelog
| Thời điểm | Đổi gì | Vì sao (trỏ về feedback/case nào) |

