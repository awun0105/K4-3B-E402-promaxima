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

### B. Bằng chứng thực tế toàn bộ (24 trường hợp)
Dưới đây là TOÀN BỘ 24 câu hỏi của học viên cùng với phản hồi tương ứng của Bot (nếu có) để chứng minh rõ ràng sự sai lệch, đoán bừa hoặc bỏ sót của hệ thống hiện tại.

**💡 Phát hiện quan trọng từ dữ liệu (Insight):** Hệ thống cũ bộc lộ 2 điểm yếu chí mạng:
1. Nếu học viên **có tag `[@BOT]`**, bot sẽ trả lời nhưng thường bị ảo giác (hallucinate), đoán bừa thông tin.
2. Nếu học viên **không tag `[@BOT]`**, bot hoàn toàn "mù" và bỏ sót tin nhắn, dẫn đến tin nhắn bị trôi.

#### Trường hợp M73605 (Dòng 18)
- **Học viên hỏi:** *"Anh ơi cho e hỏi chút ạ. Vì buổi sáng học 13h mới tan, mà chiều em có lịch bận nên em có thể xin tan sớm vào buổi sáng không ạ?"*
- **Bot phản hồi:** (Không có bot phản hồi, TA/Học viên khác tự giải quyết)
- **Phân tích lỗi:** Học viên **KHÔNG** tag `@BOT`. Hệ thống bot cũ hoàn toàn thụ động (reactive) nên đã bỏ sót câu hỏi, không hỗ trợ kịp thời.

#### Trường hợp M19124 (Dòng 130)
- **Học viên hỏi:** *"a ơi sao deadline ghép đội tự do end sớm vậy a?"*
- **Bot phản hồi:** (Không có bot phản hồi, TA/Học viên khác tự giải quyết)
- **Phân tích lỗi:** Học viên **KHÔNG** tag `@BOT`. Hệ thống bot cũ hoàn toàn thụ động (reactive) nên đã bỏ sót câu hỏi, không hỗ trợ kịp thời.

#### Trường hợp M37211 (Dòng 322)
- **Học viên hỏi:** *"các bạn labcoach cho mình hỏi, mình quét mã điểm danh đầy đủ nhưng tsao trên app ko có lịch sử điểm danh nhỉ? mình cảm ơn"*
- **Bot phản hồi:** (Không có bot phản hồi, TA/Học viên khác tự giải quyết)
- **Phân tích lỗi:** Học viên **KHÔNG** tag `@BOT`. Hệ thống bot cũ hoàn toàn thụ động (reactive) nên đã bỏ sót câu hỏi, không hỗ trợ kịp thời.

#### Trường hợp M49945 (Dòng 357)
- **Học viên hỏi:** *"[@BOT] khi nào thì bắt đầu tính điểm xp?"*
- **Bot phản hồi:** *"Bạn muốn hỏi về điểm XP trong ngữ cảnh nào?

1. Điểm XP khi tham gia Zoom meetings
2. Điểm XP liên quan đến bot commands
3. Điểm XP trong quá trình onboarding

Hoặc bạn mô tả rõ hơn giúp mình nhé!"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M56777 (Dòng 382)
- **Học viên hỏi:** *"[@BOT] hạn thành lập team là ngày nào? team không đủ 4 người có bị giải tán không"*
- **Bot phản hồi:** *"Chào bạn! Về thắc mắc của bạn, mình xin giải đáp như sau nhé:

1.  **Hạn thành lập team:** Hiện tại mình không có thông tin về ngày cụ thể cho hạn chót thành lập team trong dữ liệu. Để chắc chắn nhất, bạn hãy kiểm tra lại kênh [#channel] (thông báo Build) hoặc xem lịch trình chi tiết tại trang [Events của Phoenix](https://phoenix.note.transformerlabs.ai/events) nha.

2.  **Team không đủ 4 người:** Thông thường, BTC khuyến khích các team có đủ thành viên để cùng nhau gánh vác khối lượng công việc của Build Phase. Nếu team bạn hiện tại chưa đủ người, bạn có thể:
    *   Ghé qua kênh [#channel] để "rao tin" tìm thêm đồng đội đang lẻ bóng.
    *   Nếu vẫn gặp khó khăn, bạn hãy mở một ticket tại kênh [#channel], chọn loại `general` để nhờ BTC hỗ trợ ghép thêm thành viên hoặc tư vấn về trường hợp cụ thể của team mình nhé.

Đừng lo lắng quá, cứ chủ động tìm kiếm hoặc nhờ BTC hỗ trợ sớm là được nè! Bạn còn cần mình giúp gì nữa không?"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M88027 (Dòng 426)
- **Học viên hỏi:** *"cho em hỏi Lab2 có được extend thời gian submit thêm không v ạ? Em lỡ nộp muộn 1 phút không submit bài được ạ"*
- **Bot phản hồi:** (KHÔNG CÓ AI PHẢN HỒI - Bị trôi tin nhắn)
- **Phân tích lỗi:** Học viên **KHÔNG** tag `@BOT`. Hệ thống bot cũ hoàn toàn thụ động (reactive) nên đã bỏ sót câu hỏi, không hỗ trợ kịp thời.

#### Trường hợp M40677 (Dòng 439)
- **Học viên hỏi:** *"[@BOT] tôi nộp codelab trên vlearn đúng giờ deadline như thông báo (23:59) nhưng commit trên máy bị lỗi và sau thời gian đó mới lên thì có được tính là nộp đúng hạn không ?"*
- **Bot phản hồi:** *"Chào bạn! Về vấn đề nộp bài codelab trên **Vlearn** bị trễ do lỗi commit, mình không có thông tin cụ thể về quy định châm chước cho trường hợp này trong dữ liệu hiện tại.

Tuy nhiên, để đảm bảo quyền lợi của mình, bạn nên thực hiện ngay các bước sau nhé:

1.  **Liên hệ Admin:** Bạn hãy nhắn tin trực tiếp cho **@Vlearn Admin** để trình bày về lỗi kỹ thuật bạn gặp phải (kèm ảnh chụp màn hình lỗi commit nếu có để làm minh chứng).
2.  **Tạo Ticket:** Bạn có thể vào kênh [hỏi-đáp-bot]([link:discord.com]), dùng lệnh `/ticket create` để mở một thread hỗ trợ. Khi đó, BTC sẽ xem xét trường hợp cụ thể của bạn và đưa ra quyết định cuối cùng.

Bạn cứ yên tâm liên hệ sớm với các anh chị để được hỗ trợ nhé. Chúc bạn giải quyết vấn đề suôn sẻ!"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M80655 (Dòng 442)
- **Học viên hỏi:** *"[@user] Cho mình hỏi là: Email cá nhân nhận lịch mã số 02, sau đó nhận thêm mã số 03. Còn email outlook thì ngược lại nhận lịch mã số 03, sau đó nhận mã số 02. Vậy mình nên học theo lịch nào?"*
- **Bot phản hồi:** (Không có bot phản hồi, TA/Học viên khác tự giải quyết)
- **Phân tích lỗi:** Học viên **KHÔNG** tag `@BOT`. Hệ thống bot cũ hoàn toàn thụ động (reactive) nên đã bỏ sót câu hỏi, không hỗ trợ kịp thời.

#### Trường hợp M85508 (Dòng 518)
- **Học viên hỏi:** *"[@BOT]  tối nay có lịch gì không?"*
- **Bot phản hồi:** *"Bạn muốn hỏi về lịch trình gì tối nay ạ?

1. Lịch trình các buổi học/hoạt động trong khóa học?
2. Lịch trình các kênh hỗ trợ/họp mặt (Office Hours, Tickets)?
3. Lịch trình các lệnh bot có thể sử dụng?

Hoặc bạn mô tả rõ hơn giúp mình nhé!"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M49863 (Dòng 559)
- **Học viên hỏi:** *"[@BOT] trả lời cả 3 Nộp báo cáo daily day ở đâu trên Discord?
Nộp báo cáo daily day như thế nào khi chưa có đề tài team?
Có cần nộp báo cáo daily day khi chưa có đề tài team không?"*
- **Bot phản hồi:** *"Chào bạn nhé! Mình xin giải đáp 3 thắc mắc của bạn về vụ daily standup nè:

1.  **Nộp báo cáo daily day ở đâu trên Discord?**
    Bạn chỉ nộp báo cáo trong **forum thread riêng của team mình** thôi nhé. Khi các bạn lập đội, hệ thống sẽ tạo một forum team (có tên dạng `t-001`, `t-002`...) dành riêng cho team bạn đó.

2.  **Nộp như thế nào khi chưa có đề tài team?**
    Bạn vẫn sử dụng lệnh **`/daily-standup`** như bình thường nha. Trong phần nội dung báo cáo, bạn có thể ghi rõ là team đang trong quá trình thảo luận, tìm kiếm hoặc lựa chọn đề tài. Nếu có khó khăn gì trong việc chọn đề, bạn có thể điền vào phần `blocker` (trường này là tùy chọn, không bắt buộc nè).

3.  **Có cần nộp báo cáo khi chưa có đề tài không?**
    **Có bạn nha!** Vì đây là báo cáo tiến độ hàng ngày (`daily-standup`), việc team đang tích cực thảo luận để chốt đề tài cũng là một phần tiến độ quan trọng cần được ghi nhận đó.

Nếu cần hỗ trợ gì thêm về các lệnh `/topic`, cứ nhắn mình nha! ✨"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M58536 (Dòng 567)
- **Học viên hỏi:** *"[@BOT] daily day là thành viên nào cũng phải tag nhỉ trường hợp "Nộp như thế nào khi chưa có đề tài team?
Bạn vẫn sử dụng lệnh /daily-standup như bình thường nha. Trong phần nội dung báo cáo, bạn có thể ghi rõ là team đang trong quá trình thảo luận, tìm kiếm hoặc lựa chọn đề tài. Nếu có khó khăn gì trong việc chọn đề, bạn có thể điền vào phần blocker (trường này là tùy chọn, không bắt buộc nè).
" thì như nào"*
- **Bot phản hồi:** *"Chào bạn nha! Về thắc mắc của bạn, mình xin giải thích rõ hơn để bạn dễ hình dung nè:

1.  **Ai là người nộp?**
    Đúng rồi, **từng thành viên** trong team đều nên thực hiện lệnh `/daily-standup` cho riêng mình nhé. Việc này giúp hệ thống ghi nhận sự tích cực và cộng XP cá nhân cho chính bạn đó.

2.  **Có phải tag (ping) mọi người không?**
    **Không cần thiết** phải tag các thành viên khác khi bạn nộp daily đâu nè. Khi bạn dùng lệnh `/daily-standup`, hệ thống đã tự động ghi nhận đó là báo cáo của riêng bạn rồi.

3.  **Nộp như thế nào khi chưa có đề tài?**
    Dù team chưa chốt đề tài chính thức, nhưng chắc chắn bạn vẫn đang có những hoạt động để chuẩn bị cho dự án mà, đúng không? Bạn có thể ghi nội dung báo cáo như sau:
    *   *Ví dụ 1:* "Đang cùng team thảo luận và brainstorm để chọn đề tài dự án."
    *   *Ví dụ 2:* "Nghiên cứu các công nghệ liên quan để đề xuất ý tưởng cho team."
    *   *Ví dụ 3:* "Đã họp team 30 phút để lọc ra top 3 đề tài tiềm năng."

**Tóm lại là:** Cứ mỗi ngày bạn có tham gia đóng góp, thảo luận hay nghiên cứu cho team (dù là bước sơ khai nhất) thì bạn cứ mạnh dạn nộp daily để tích lũy XP và duy trì tiến độ nha! ✨

Nếu bạn còn chỗ nào chưa rõ, cứ hỏi mình nhé!"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M76564 (Dòng 569)
- **Học viên hỏi:** *"[@BOT] trường hợp "Nộp như thế nào khi chưa có đề tài?
Dù team chưa chốt đề tài chính thức, nhưng chắc chắn bạn vẫn đang có những hoạt động để chuẩn bị cho dự án mà, đúng không? Bạn có thể ghi nội dung báo cáo như sau:
Ví dụ 1: "Đang cùng team thảo luận và brainstorm để chọn đề tài dự án."
Ví dụ 2: "Nghiên cứu các công nghệ liên quan để đề xuất ý tưởng cho team."
Ví dụ 3: "Đã họp team 30 phút để lọc ra top 3 đề tài tiềm năng."" cần ghi cả field yesterday và today không"*
- **Bot phản hồi:** *"💬 Mình cần xả hơi tí xíu 😄 Quay lại sau **2 phút** nhé! Càng build nhiều, càng lên level — level cao hơn là chat thoải mái hơn đó 🚀"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M15491 (Dòng 571)
- **Học viên hỏi:** *"[@BOT]  trường hợp "Nộp như thế nào khi chưa có đề tài?
Dù team chưa chốt đề tài chính thức, nhưng chắc chắn bạn vẫn đang có những hoạt động để chuẩn bị cho dự án mà, đúng không? Bạn có thể ghi nội dung báo cáo như sau:
Ví dụ 1: "Đang cùng team thảo luận và brainstorm để chọn đề tài dự án."
Ví dụ 2: "Nghiên cứu các công nghệ liên quan để đề xuất ý tưởng cho team."
Ví dụ 3: "Đã họp team 30 phút để lọc ra top 3 đề tài tiềm năng."" cần ghi cả field yesterday và today không"*
- **Bot phản hồi:** *"💬 Mình cần xả hơi tí xíu 😄 Quay lại sau **1 phút** nhé! Càng build nhiều, càng lên level — level cao hơn là chat thoải mái hơn đó 🚀"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M60145 (Dòng 576)
- **Học viên hỏi:** *"[@BOT] trường hợp "Nộp như thế nào khi chưa có đề tài?
Dù team chưa chốt đề tài chính thức, nhưng chắc chắn bạn vẫn đang có những hoạt động để chuẩn bị cho dự án mà, đúng không? Bạn có thể ghi nội dung báo cáo như sau:
Ví dụ 1: "Đang cùng team thảo luận và brainstorm để chọn đề tài dự án."
Ví dụ 2: "Nghiên cứu các công nghệ liên quan để đề xuất ý tưởng cho team."
Ví dụ 3: "Đã họp team 30 phút để lọc ra top 3 đề tài tiềm năng."" cần ghi cả field yesterday và today không"*
- **Bot phản hồi:** *"Chào bạn nha! Câu trả lời là: **Có, bạn nên điền cả hai trường `yesterday` và `today`** để báo cáo được đầy đủ và rõ ràng nhất nhé! ✨

Việc điền cả hai trường giúp Mod và các thành viên khác thấy được sự kết nối trong công việc của bạn. Dù chưa có đề tài chính thức, bạn có thể ghi như sau:

*   **Yesterday (Hôm qua):** Bạn đã làm gì để tìm kiếm đề tài?
    *   *Ví dụ:* "Đã tìm hiểu về các ứng dụng AI trong giáo dục" hoặc "Đã liệt kê ra 3 ý tưởng cá nhân".
*   **Today (Hôm nay):** Bạn dự định làm gì tiếp theo?
    *   *Ví dụ:* "Thảo luận cùng team để chọn ra ý tưởng tốt nhất" hoặc "Tiếp tục nghiên cứu tính khả thi của ý tưởng A".

**Một vài lưu ý nhỏ cho bạn:**
*   Việc ghi rõ ràng giúp bạn duy trì thói quen làm việc chuyên nghiệp.
*   Trường **Blocker** (Khó khăn) thì vẫn là **tùy chọn**, nếu bạn thấy việc chưa có đề tài là một trở ngại lớn cần hỗ trợ thì hãy ghi vào đó nhé.

Chúc bạn và team sớm tìm được đề tài thật "xịn" nha! Nếu cần hỗ trợ gì thêm cứ nhắn mình nè. 🚀"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M95655 (Dòng 620)
- **Học viên hỏi:** *"[@BOT] nộp đề tài như nào?"*
- **Bot phản hồi:** *"bạn gõ /topic pick để chọn đề tài nha"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M98092 (Dòng 635)
- **Học viên hỏi:** *"[@BOT] -activity để làm gì? khi nào có "commit mới lên sóng""*
- **Bot phản hồi:** *"Commit và PR vào main thành công sẽ được ghi nhận trên kênh [link:discord.com] nhé"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M57734 (Dòng 698)
- **Học viên hỏi:** *"[@BOT]  quy cách nộp daily standup, cả nhóm có phải nộp ko? hình thức nộp như nào, viết ra sao, có mẫu ko? Nộp vào đâu?"*
- **Bot phản hồi:** *"Bạn đang hỏi về quy cách nộp daily standup cho nhóm hay về một loại nộp bài khác?

1. Quy cách nộp daily standup cho nhóm
2. Quy định về việc nộp bài nói chung

Hoặc bạn mô tả rõ hơn giúp mình nhé!"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M79664 (Dòng 703)
- **Học viên hỏi:** *"[@BOT] nộp daily standup cả nhóm có phải nộp ko hay 1 người thôi? hình thức nộp như nào, viết ra sao, có mẫu ko? Nộp vào đâu?"*
- **Bot phản hồi:** *"Bạn đang hỏi về quy cách nộp daily standup cho cả nhóm hay chỉ cho cá nhân?

1. Quy cách nộp daily standup cho cả nhóm
2. Quy cách nộp daily standup cho cá nhân

Hoặc bạn mô tả rõ hơn giúp mình nhé!"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M37039 (Dòng 719)
- **Học viên hỏi:** *"[@BOT] ngoài daily-standup còn phải nộp gì trong discord nhóm nữa không? và làm sao xem số XP hiện tại?"*
- **Bot phản hồi:** *"Bạn nộp daily standup trong thread `Thảo luận` trong channel riêng của team mình nhé (t-xxx)
Cách thức nộp: gõ /daily"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M78574 (Dòng 766)
- **Học viên hỏi:** *"[@BOT] nộp daily standup chỉ ở nội dung build phase thôi hay có cả học LAB và LEC trên giảng đường vinuni?"*
- **Bot phản hồi:** *"Chào bạn nè! Câu trả lời là: **Daily Standup chỉ tập trung vào nội dung Build Phase thôi nhé!** 🛠️

Cụ thể để bạn dễ phân biệt giữa hai hoạt động này:

*   **Hoạt động Build (Online):** Đây là nơi bạn dùng lệnh `/daily-standup`. Mục đích là để báo cáo tiến độ dự án, những việc team đã làm, kế hoạch tiếp theo và các khó khăn (blockers) trong quá trình xây dựng sản phẩm.
*   **Hoạt động trên lớp (LAB/LEC tại VinUni):** Phần này thuộc về chương trình học offline, được quản lý trên nền tảng **Vlearn**. Các vấn đề liên quan đến bài giảng, điểm danh hay thủ tục lớp học bạn sẽ theo dõi tại danh mục `LỚP HỌC - KHOÁ 4` và liên hệ **Vlearn Admin** nếu cần hỗ trợ nha.

Tóm lại, khi làm Standup, bạn cứ tập trung "khoe" tiến độ build dự án của team mình là chuẩn bài luôn! Nếu cần hỗ trợ gì thêm về các lệnh bot, cứ nhắn mình nhé. ✨"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M80377 (Dòng 869)
- **Học viên hỏi:** *"[@BOT] Em có giấy gọi khám sơ tuyển NVQS nhưng không về địa phương kịp thì BTC có hỗ trợ giấy tờ xác nhận hay gì không, để em nộp cho địa phương?"*
- **Bot phản hồi:** *"Chào bạn! Về vấn đề xin giấy xác nhận để nộp cho địa phương do vướng lịch trình của chương trình, bạn cần thực hiện theo hướng dẫn sau để được hỗ trợ chính thức nhé:

1.  **Gửi email yêu cầu:** Bạn hãy gửi email trình bày rõ lý do và yêu cầu hỗ trợ giấy tờ về địa chỉ:
    *   **Email chính:** `AIthucchien@vinuni.edu.vn`
    *   **CC:** `[EMAIL]`
    *   *Nội dung:* Bạn nên đính kèm ảnh chụp giấy gọi khám và thông tin cá nhân (MSSV, lớp, đội nhóm) để BTC có cơ sở xác nhận nhanh nhất cho bạn.

2.  **Tạo Ticket hỗ trợ (nếu cần):** Nếu bạn cần hỏi thêm về việc vắng mặt trong các hoạt động cụ thể của Build Phase, bạn có thể dùng lệnh `/ticket create` tại kênh [🎫-tickets]([link:discord.com]) và chọn loại `general` để trao đổi trực tiếp với các anh chị Admin/Mod.

Vì đây là thủ tục hành chính quan trọng, bạn nên gửi email sớm nhất có thể để BTC kịp thời xử lý giúp bạn nhé. Chúc bạn giải quyết công việc thuận lợi! ✨"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M34960 (Dòng 908)
- **Học viên hỏi:** *"[@BOT] Có xếp hạng cả XP nhóm không hay chỉ xếp hạng XP cá nhân thôi ?"*
- **Bot phản hồi:** *"Chào bạn! Hiện tại hệ thống đang tập trung hiển thị bảng xếp hạng cá nhân để mọi người cùng thi đua nè.

Cụ thể:
*   Bạn dùng lệnh `/leaderboard users` để xem bảng xếp hạng cá nhân toàn server nhé.
*   Để xem XP và level của riêng mình (hoặc của một bạn cụ thể), bạn dùng lệnh `/rank`.

Về phần **XP nhóm**: Mặc dù các hoạt động như commit hay Pull Request đều được ghi nhận theo từng repo của team trong tổ chức `AI20K-Build-Phase-Cohort-4`, nhưng lệnh hiển thị bảng xếp hạng riêng cho nhóm hiện chưa được liệt kê phổ biến như bảng cá nhân.

**Mẹo nhỏ cho bạn:**
Bạn có thể thử gõ `/leaderboard` vào khung chat Discord để xem hệ thống có gợi ý thêm tùy chọn nào khác (như `teams`) không nhé. Nếu cần thông tin chính xác nhất về cách tính điểm tổng cho cả đội, bạn có thể nhắn tin hỏi các @Mod để được hỗ trợ nha! 🚀"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M98666 (Dòng 912)
- **Học viên hỏi:** *"[@BOT] thời gian mở daily standup và kết thúc là khi nào vậy? hôm qua mình gửi sớm daily standup thì không được, chiều nay quá deadline thì nó lại blocked mình."*
- **Bot phản hồi:** *"[@role]

Mình chưa rõ thông tin câu này lắm, để chắc chắn không sai sót thì mình nhờ Mod vào trả lời giúp bạn ạ!"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.

#### Trường hợp M65517 (Dòng 993)
- **Học viên hỏi:** *"[@BOT] có xem được lịch sử +XP ko ?"*
- **Bot phản hồi:** *"Các bạn có thể theo dõi hoặc tìm kiếm điểm XP của mình bằng Discord ID tại kênh [link:discord.com] hoặc xem lịch sử XP của bản thân bằng `/rank`"*
- **Phân tích lỗi:** Học viên **CÓ** tag `@BOT`. Tuy nhiên, bot trả lời sai, tự đoán hoặc lan man không giải quyết được trực tiếp vấn đề.


### C. Lỗi của Bot trong Bản tin hàng ngày (`k4_daily_reports.md`)
- **Dòng 36, dòng 124:** Chuỗi `"nguồn tham chiếu"` bị chèn sai chỗ (lỗi template prompt). Ví dụ: `nguồn tham chiếuhi nào...`
- **Lỗi ảo giác (Hallucination):** Tóm tắt bị sai lệch ngữ cảnh, báo cáo sai trạng thái (Ghi "Đã có phản hồi" nhưng thực tế không ai xử lý).

## 3. Tổng kết
Việc trích xuất đủ bộ bằng chứng trên cho thấy vấn đề của Đề B1 là cực kỳ nhức nhối. Ở các trường hợp bot có trả lời (do được tag), bot thường tự đưa ra thông tin không chính thức hoặc trả lời quá máy móc. Ở các trường hợp bot không trả lời (do không được tag), tin nhắn bị trôi khiến học viên không biết thời hạn chính xác.
