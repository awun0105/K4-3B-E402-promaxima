# Sơ đồ luồng CP2 — Trợ lý Học viên (Discord)

```mermaid
flowchart TD
    A[Học viên gửi tin nhắn trên Discord] --> B{Tin nhắn có liên quan đến deadline / hạn nộp / lịch nộp không?}
    B -- Không --> C[Bot trả lời bình thường hoặc bỏ qua]
    B -- Có --> D[Bot phân loại intent: deadline / nộp / lịch]
    D --> E{Có nguồn chính thức của BTC / thông báo đáng tin cậy không?}
    E -- Không --> F[Bot không đoán, báo thiếu căn cứ <br> <b>(G10 - Thu hẹp phạm vi khi nghi ngờ)</b>]
    F --> G{Có thông tin bổ sung từ người dùng không?}
    G -- Có --> H[Bot yêu cầu xác nhận thêm 1 thông tin ngắn]
    H --> E
    G -- Không --> I[Bot tag TA / chuyển tiếp hỗ trợ <br> <b>(G8 - Gạt bỏ dễ dàng, câu từ chối ngắn gọn)</b>]
    I --> J[TA trả lời trực tiếp trong thread]

    E -- Có --> K{Mức chắc chắn cao và trùng khớp 100% với nguồn không?}
    K -- Có --> L[Bot trả lời: deadline + link nguồn chính thức <br> <b>(G11 - Giải thích vì sao)</b>]
    L --> M[Học viên nhận câu trả lời rõ ràng]

    K -- Không --> N[Bot không trả lời chắc chắn <br> <b>(G10 - Thu hẹp phạm vi)</b>]
    N --> O{User muốn sửa / phản hồi thả emoji ❌ không?}
    O -- Có --> P[Bot thu hồi câu trả lời tự động <br> và yêu cầu làm rõ <b>(G9 - Sửa chữa dễ dàng)</b>]
    P --> E
    O -- Không --> I

    classDef safe fill:#d9f7be,stroke:#52c41a,color:#000;
    classDef warn fill:#fff2d9,stroke:#faad14,color:#000;
    classDef danger fill:#fde7e8,stroke:#cf1322,color:#000;
    classDef end fill:#e6f7ff,stroke:#1890ff,color:#000;

    class C safe;
    class L,M safe;
    class H,N,P warn;
    class F,I,J danger;
    class E end;
```

## Phiên bản dạng text đơn giản cho slide / demo

```text
Học viên hỏi trên Discord
        |
        v
Có phải câu hỏi deadline / nộp / lịch nộp không?
        |
        +-- Không --> Bot trả lời thường / bỏ qua
        |
        +-- Có --> Bot kiểm tra nguồn chính thức BTC
                       |
                       +-- Không tìm thấy / không chắc chắn --> Bot KHÔNG đoán
                                                            |
                                                            +-- Có thông tin bổ sung --> hỏi lại 1 câu ngắn
                                                            |
                                                            +-- Không có --> tag TA và chuyển tiếp
                                                                                 |
                                                                                 v
                                                                               TA hỗ trợ
                       |
                       +-- Tìm thấy source rõ ràng --> Bot kiểm tra độ chắc chắn
                                                       |
                                                       +-- Có độ chắc chắn cao --> trả lời kèm link nguồn
                                                       |
                                                       +-- Không chắc chắn --> hỏi lại / yêu cầu xác nhận
```

## Gợi ý demo 3 phút

1. Mở màn hình giả lập Discord
2. Gõ câu hỏi: "Hạn nộp Lab 2 là khi nào?"
3. Bot kiểm tra thông báo chính thức
4. Bot trả lời: "Deadline Lab 2 là ... - Nguồn: BTC"
5. Gõ trường hợp thiếu nguồn: "Hạn nộp Lab 7 là khi nào?"
6. Bot không đoán, báo thiếu căn cứ và tag TA
7. Nhấn mạnh: "AI chỉ trả lời khi có nguồn chính thức; không có source thì chuyển người."

## Câu nhấn trong demo

> "AI không đoán deadline. Khi thiếu căn cứ, nó từ chối và chuyển cho TA để tránh sai lệch về điểm số và thời hạn nộp."
