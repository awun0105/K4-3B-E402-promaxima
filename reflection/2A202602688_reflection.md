# Thu Hoạch Cá Nhân - Bùi Văn Quang (2A202602688)

## 1. Vai trò cá nhân
**QA & Eval Benchmark Engineer**

## 2. Phần việc trực tiếp phụ trách
- Khai thác Evidence, đối soát dữ liệu từ 1.092 tin nhắn thực tế để đảm bảo chất lượng bài toán.
- Xây dựng bộ dữ liệu kiểm thử (Golden Set) với 46 test cases.
- Lập trình Script chạy đánh giá tự động (Eval runner - `run_eval.py`).
- Thu thập metrics, so sánh pass rate qua các bản Run 1, Run 2, Run 3.
- Chịu trách nhiệm **tạo thiết kế Slide & biên soạn nội dung** thuyết trình báo cáo CP5.

## 3. Cách ứng dụng AI trong quá trình xây dựng
- Dùng LLM để tự động sinh ra các biến thể (Adversarial variants) từ câu hỏi chuẩn, tạo data bẩn test giới hạn bot.
- Dùng AI để lên dàn ý nội dung cho Slide thuyết trình, đảm bảo bám sát mạch chấm điểm.
- Nhờ AI hỗ trợ format kết quả eval từ file CSV sang báo cáo `.md` tự động.

## 4. Bài học thực tế từ thất bại của nhóm
- **Thất bại với việc test thủ công:** Ban đầu định test tay trên giao diện khiến tiến độ tắc nghẽn nghiêm trọng. Bài học: Nhờ tự động hóa bằng Headless Evaluation (script `run_eval.py`), nhóm mới có thể an tâm sửa code mà không sợ làm hỏng các case cũ.
- **Thảm họa quản lý phiên bản Git:** Sát deadline, cả team cuống cuồng push đè code lên `main`, gây ra conflict vỡ nát toàn bộ hệ thống code và script test. Bài học chung của cả team: Phải tuân thủ kỷ luật Git, phân chia Branch và review bằng Pull Request cẩn thận.
- **Prompt mập mờ khiến Agent coding sai:** Khi dùng AI để sinh script test và logic code, cả nhóm gửi prompt quá sơ sài. AI sinh ra code rác, chạy vòng lặp vô tận. Bài học: Việc ra lệnh cho AI phải chi tiết, rõ ràng và có điều kiện đầu ra (output constraint) chặt chẽ.
