# Mini Hackathon AI — Batch 04 · Lớp 3B

**SPEC → Prototype → Demo.** Đây không phải cuộc thi code — đây là cuộc thi **tư duy sản phẩm AI**.

### 👥 Thành viên nhóm & Phân công vai trò

**Lớp:** 3B · **Phòng:** E402 · **Cụm:** Zone 4 · **Track:** B — Trợ lý Học viên Discord

| Họ và Tên | Mã Học Viên | Vai trò chính | Phần việc đảm nhiệm trong dự án |
|---|---|---|---|
| Lâm Quang Anh Quân | 2A202602467 | Product Lead & UX/Spec | Thiết kế Spec, Canvas, luồng hội thoại HAX/PAIR, UI Discord Web Mock |
| Bùi Văn Quang | 2A202602688 | QA & Eval Benchmark Engineer | Xây dựng Golden Set 24 cases, Eval runner, Thiết kế Slide CP5 |
| Nguyễn Văn Diện | 2A202602615 | Lead Engineer & Agent Architecture | Kiến trúc Agent Loop, Tool Calling, System Prompt, Decoupled Providers |

> Chi tiết phân công và bản tự nhận xét cá nhân xem tại thư mục [reflection/](reflection/) và báo cáo kỹ thuật [codebase/artifacts/REPORT.md](codebase/artifacts/REPORT.md).

---

## 🚀 Cấu Trúc Mã Nguồn Chuẩn Hóa (Day04 & Mini Hackathon)

Toàn bộ mã nguồn, cấu hình công cụ (tools), prompt, dữ liệu kiểm thử và báo cáo kỹ thuật được tổ chức chặt chẽ theo đúng chuẩn quy ước tại thư mục **[`codebase/`](codebase/)**:

```text
codebase/
├── artifacts/
│   ├── REPORT.md               # Báo cáo kỹ thuật chi tiết v0-v3, failure analysis, evidence
│   ├── system_prompt.md        # System prompt có versioning quản lý qua SHA-256
│   ├── tools.yaml              # Khai báo tool calling chuẩn OpenAPI / JSON Schema
│   └── version_log.csv         # Nhật ký version hóa qua các mốc thử nghiệm
├── tools/                      # Kiến trúc tool modular độc lập
│   ├── search_knowledge_base/  # Tool tra cứu thông báo và hạn nộp chính thức
│   ├── normalize_user_query/   # Tool làm sạch bot tag và giải mã teencode tiếng Việt
│   ├── check_safety_and_policy/# Tool kiểm tra an toàn và vi phạm quy chế
│   ├── escalate_to_ta/         # Tool chuyển giao cho TA khi thiếu nguồn (HAX G10)
│   ├── clarify/                # Tool làm rõ khi câu hỏi thiếu chủ thể
│   ├── mcp/                    # Chuẩn giao thức MCP Server / Client cho Knowledge Base
│   ├── _shared.py              # Thư viện hàm dùng chung
│   └── __init__.py             # Tool Registry tập trung
├── providers/                  # Tầng adapter LLM trừu tượng (OpenRouter, OpenAI, Mock...)
├── data/                       # Bộ kiểm thử chuẩn hóa (eval_base_discord, eval_group, adversarial)
├── discord_data/               # Dữ liệu tri thức domain (announcements.json, markdown KB)
├── scripts/                    # Scripts kiểm tra preflight và phân tích runs
├── agent.py                    # Vòng lặp Agent thực thi tool calling
├── chat.py                     # Giao diện chat CLI tương tác có ghi log transcript
├── run_eval.py                 # Bộ đo lường chất lượng tự động
├── env_loader.py               # Nạp an toàn biến môi trường
└── versioning.py               # Tính toán artifact hash SHA-256
```

### Hướng Dẫn Chạy & Kiểm Thử

```powershell
# 1. Kích hoạt môi trường và cài đặt dependencies
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 2. Chạy kiểm tra kết nối Provider (OpenRouter live tool calling)
python codebase/scripts/preflight_provider.py --provider openrouter

# 3. Chạy đánh giá bộ 10 cases nhóm (5 single-turn + 5 multi-turn)
python run_eval.py --provider openrouter --version v3 --suite group --eval-cases codebase/data/eval_group.json

# 4. Chạy đánh giá bộ 24 cases Golden Set (Track B Discord Assistant)
python run_eval.py --provider openrouter --version v3 --suite base --eval-cases codebase/data/eval_base_discord.json

# 5. Khởi động Chat CLI tương tác trực tiếp
python chat.py --provider openrouter --model openai/gpt-4o-mini --version v3

```

## Tài Liệu & Artifacts Dự Án

| File / thư mục | Nội dung |
|---|---|
| [`spec.md`](spec.md) | AI Spec hoàn chỉnh: Bằng chứng (§1-§2) · Lát cắt (§4) · HAX Principles · 4 lớp chỗ khó (§5) · Kiểm thử (§7) |
| [`canvas.md`](canvas.md) | Canvas 7 dòng chốt bài toán, JTBD và phân công vai trò tại CP1 |
| [`reflection/`](reflection/) | Bản tự nhận xét đóng góp cá nhân của từng thành viên (INDIVIDUAL) |
| [`codebase/flow.md`](codebase/flow.md) | Sơ đồ luồng hội thoại & kiến trúc điều phối Agent CP2 |
| [`codebase/mock.html`](codebase/mock.html) | Web App giao diện giả lập Discord tương tác trực quan |
| [`codebase/artifacts/REPORT.md`](codebase/artifacts/REPORT.md) | Báo cáo kỹ thuật chi tiết v0-v3, failure analysis và bảng đối chiếu metric |

## Lịch — 6 checkpoint (ca 3B · 39 giờ)

| Mốc | Cần hoàn thành | Hạn (ca 3B) |
|---|---|---|
| — | Khai mạc 17:30 · phát đề 18:00 | 17/9 |
| **CP1** | Canvas 7 dòng (`02-guide.md` §1.5) + đội trưởng + **link repo GitHub công khai** | **19:30** · 17/9 |
| **CP2** | Cho thấy **luồng hoạt động** — bấm thử được, hoặc sơ đồ luồng | **21:00** · 17/9 |
| **CP3** | **Video thao tác** 30 giây + **số đo** (thử bao nhiêu, đúng bao nhiêu) | **16:00** · 18/9 |
| **CP4** | Chốt `spec.md` — **khoá chuẩn "đạt"** · tự khai phần chưa xong | **21:00** · 18/9 |
| **CP5** | Slide PDF + **video demo dự phòng cho buổi pitch** — nộp cuối | **22:30** · 18/9 |
| **CP6** | Thuyết trình · không nộp thêm | **09:00** · 19/9 |

**CP1 đến CP5 mỗi mốc 5 điểm.** Nộp đúng hạn được đủ, nộp muộn là **0 điểm mốc đó** — không bù được bằng mốc khác.

## Làm bài lúc nào

| | |
|---|---|
| **Thời gian tự làm** | Ngoài giờ học, và trong buổi **LEC ngày 18/9** |
| **Coach hỗ trợ** | Trên lớp và trên Discord |
| **Buổi LAB 19/9 · 09:00–13:00** | Đây là **vòng thi**, không phải giờ làm bài |

Hai phòng cùng ca dùng chung lịch mốc. Năm link form phát đủ từ đầu — xong mốc nào nộp mốc đó, không phải chờ.

## Giải thích từng mốc

### CP1 · Chốt Canvas + repo

**Để làm gì:** chốt rõ **làm cho ai và giải vấn đề gì** trước khi bắt tay vào code. Bỏ qua bước này thì hay gặp cảnh làm xong mới nhận ra không ai cần đến.

**Nộp:**
- Canvas điền đủ **7 dòng** theo scaffold trong `02-guide.md` §1.5 (track + đề · job executor · pain · bằng chứng đầu · lát cắt 1 câu · automation + willing users · phân công) — mẫu trống + ví dụ: `examples/canvas-cp1.md`
- Họ tên và **mã học viên của đội trưởng**
- **Link repo GitHub** đã để công khai
- **Khai báo willing user** — người sẵn sàng cho nhóm thử sản phẩm ở CP5. Cần ít nhất 2 người, khai từ đây

> **Khai willing user ngay từ CP1, đừng để đến CP5.** Khối R6 ở CP5 yêu cầu có ít nhất 2 willing user đã khai ở mốc này. Đến lúc cần mới đi tìm người thì không kịp.

---

### CP2 · Cho thấy luồng hoạt động

**Để làm gì:** nhìn được cả luồng từ đầu đến cuối — người dùng bấm gì trước, thấy gì sau, kết thúc ở đâu. Vẽ ra giấy thì phát hiện chỗ hổng trong mười phút; code xong mới thấy thì mất cả buổi sửa.

**Nộp một trong ba thứ, thứ nào cũng được:**
- **Bản mock bấm được** — Figma, trang tĩnh, Canva, bất cứ thứ gì click qua lại được
- **Sơ đồ luồng** vẽ tay hay vẽ máy, miễn thấy rõ các bước
- **Video quay màn hình** đi hết một lượt

**Chưa cần AI chạy thật** — cái đó để CP3. Mốc này để nhẹ, chỉ cần cho thấy nhóm đang đi hướng nào.

---

### CP3 · Video thao tác + số đo

**Để làm gì:** biết sản phẩm của mình **đang đúng đến đâu**. Có con số thì mới biết nên sửa chỗ nào tiếp, và lúc pitch cũng có cái để nói thay vì nói suông.

**Nộp hai thứ:**

**1 · Video thao tác — 30 giây, quay màn hình.** Bấm thật trên sản phẩm, thấy AI trả kết quả thật. Không cần dựng, không cần lồng tiếng.

**2 · Số đo — thử bao nhiêu lần, đúng được bao nhiêu.**

Đây là con số cho biết sản phẩm tốt đến đâu. Cách làm:

```
1. Chuẩn bị một bộ câu thử  — ví dụ 20 câu hỏi người dùng hay hỏi
2. Cho sản phẩm chạy hết 20 câu đó
3. Đếm bao nhiêu câu ra kết quả đạt chuẩn nhóm tự đặt
```

| Chưa đạt | Đạt |
|---|---|
| *"Sản phẩm chạy tốt"* | *"Thử 21 câu, 13 câu trả đúng có dẫn nguồn, 8 câu sai hoặc bịa"* |
| *"Độ chính xác cao"* | *"Thử 30 file, 24 file tóm tắt đúng ý chính, 6 file bỏ sót"* |

**Số xấu vẫn được đủ điểm** — miễn là số thật. 13 trên 21 mà phân tích được vì sao 8 câu kia sai thì ăn điểm cao hơn "chạy tốt" không có gì chứng minh.

---

### CP4 · Chốt `spec.md`

**Để làm gì:** chốt **"thế nào là đạt"** trước khi biết kết quả. Đặt chuẩn sau khi đã thấy kết quả thì con số không nói lên điều gì — và người nghe cũng biết vậy.

**Nộp:**
- Link `spec.md` đã chốt — trong đó nhóm **tự chốt "thế nào là đạt"** cho sản phẩm mình
- **Tự khai phần nào chưa làm xong**

Sau 21:00 hôm đó **không sửa chuẩn "đạt" được nữa**.

**Khai thiếu không bị trừ điểm.** Giấu mới bị.

---

### CP5 · Slide + video dự phòng

**Để làm gì:** đảm bảo buổi pitch chạy được **dù mạng hỏng hay máy chết**. Đây cũng là hạn nộp cuối — sau mốc này không nộp thêm gì.

**Nộp:**
- **Slide 6 trang, xuất ra PDF** theo `02-guide.md` §5.1. Nộp PDF chứ không nộp link — link hay hỏng quyền đúng lúc cần
- **Video demo dự phòng** — quay sẵn phần demo. Nếu hôm pitch mạng chết thì BTC chiếu video này và **không trừ điểm**

> **CP3 và CP5 là hai video khác nhau:**
> **CP3** chứng minh sản phẩm chạy — quay ngắn, quay thô cũng được.
> **CP5** là bản sao lưu để buổi pitch không chết vì mạng — quay đúng phần định demo trên sân khấu.

---

### CP6 · Thuyết trình

**Không nộp gì.** Ngày này chỉ để trình bày.

Giám khảo có thể hỏi **bất kỳ thành viên nào** về phần có tên người đó trong bảng phân công.

## Link nộp

| Mốc | Form nộp |
|---|---|
| CP1 | *(cập nhật lúc khai mạc)* |
| CP2 | *(cập nhật lúc khai mạc)* |
| CP3 | *(cập nhật lúc khai mạc)* |
| CP4 | *(cập nhật lúc khai mạc)* |
| CP5 | *(cập nhật lúc khai mạc)* |

> **Đội trưởng nộp form thay cả nhóm** — một phiếu cho cả nhóm ở mỗi mốc, không phải mỗi thành viên tự nộp.
> **25 điểm nộp là điểm chung của nhóm**: mọi thành viên cùng được hoặc cùng mất.

> ⚠️ **Cả 5 mốc phải nộp bằng cùng một mã học viên của đội trưởng.**
> BTC ghép 5 phiếu của nhóm lại với nhau **dựa trên mã học viên người nộp**. Mốc này người A nộp, mốc kia người B nộp thì hệ thống hiểu là hai nhóm khác nhau, và nhóm mất điểm ở những mốc lệch.
>
> Chọn đội trưởng là người **chắc chắn có mặt và theo được cả năm mốc**. Nếu bất khả kháng phải đổi người nộp, báo coach ngay trong buổi.

Link được công bố tại khai mạc, **ghim trên Discord và đăng trên VLearn** — hai nơi, cùng một bộ link.

## Thể thức thi

- 2 ca × 2 phòng = **4 cuộc thi độc lập**, chấm và trao giải riêng từng phòng; mỗi phòng một tổ giám khảo. **Không thi liên phòng, liên khoá.**
- **E403** (~230 người): 6 cụm thi, mỗi nhóm **6 phút** ở vòng cụm → 6 đội vào chung kết phòng → **Top 3**.
- **E402** (~120 người): 5 cụm thi, mỗi nhóm **7 phút** ở vòng cụm → 5 đội vào chung kết phòng → **Top 2**.
- Giám khảo có thể hỏi **bất kỳ thành viên** — ai cũng phải hiểu bài (vibe-coding rule).
- Số nhóm mỗi cụm là ước tính; thể lệ chi tiết vòng cụm và chung kết công bố lúc khai mạc.

### Vòng cụm — game đầu tư

Mỗi đội có **100 điểm vốn**, đội trưởng đại diện xem và đầu tư. Đội nhận nhiều vốn nhất cụm đi tiếp vào chung kết phòng.

**Hai luật:** không được đầu tư vào đội mình · **tổng phải đúng 100**, thừa hoặc thiếu là phiếu không được tính.

Chia cho mấy đội là tuỳ — dồn hết vào một đội cũng được. Mẹo: trong lúc xem thì ghi số dự định ra giấy nháp, xem xong cả cụm mới cân đối lại rồi điền form.

### Chung kết phòng

Sau khi chốt danh sách, các đội có **10–15 phút chuẩn bị**. Thứ tự trình bày quay ngẫu nhiên tại chỗ.

Mỗi đội **10 phút**: 7 phút trình bày + 3 phút hỏi đáp.

Cả phòng bình chọn — mỗi người đánh giá từng đội một cách độc lập, không giới hạn số đội được bầu.

## Giải thưởng

**Giải theo phòng — mỗi lớp 5 đội, hai lớp 10 đội:**

| Lớp | E403 | E402 | Tổng |
|---|---|---|---|
| 3A | Top 3 | Top 2 | 5 đội |
| 3B | Top 3 | Top 2 | 5 đội |

**Điểm thưởng cộng vào bài lab ngày 5 và ngày 6, cho mỗi thành viên:**

| Ai được | Cộng |
|---|---|
| Giải Nhất của phòng | **+10** |
| Giải Nhì của phòng | **+5** |
| Giải Ba — chỉ E403 | **+3** |
| Vào chung kết nhưng không có giải | **+2** |
| Đội **đầu tư nhiều điểm nhất và sớm nhất** vào đội giải Nhất | **+2** |

Mỗi phòng E403 có **7 đội** được cộng điểm, E402 có **6 đội** — không chỉ riêng đội vô địch.

Dòng cuối chỉ có **một đội mỗi phòng**: xét điểm đầu tư cao nhất trước, bằng nhau thì lấy đội nộp phiếu sớm hơn theo dấu thời gian của form.

**Giải theo track — 4 giải, chấm chung cả hai lớp:**

- **Track A · VLearn Tutor và Track D · Học tập thích ứng & tương tác:** 2 giải, do team VLearn chọn.
- **Track C · Lesson Studio:** 2 giải, do team Studio chọn.

Hai team chấm **ngay tại buổi trình bày**. Một đội có thể vừa vào Top phòng vừa nhận giải track. Phần thưởng cụ thể sẽ được công bố sau.

Mỗi mốc cần show gì và được xác minh thế nào: xem bảng trong `04-rubric.md`.

## Nộp bài

### Tạo repo mới — không fork repo đề bài

Nhóm tạo một repo **hoàn toàn mới và trống**. Không fork, không clone repo này rồi push lên.

Lý do: fork mang theo cả thư mục `data/`, mà repo nộp bài bắt buộc phải **công khai** — nghĩa là dữ liệu thật của khoá học sẽ lên mạng. Vi phạm thẳng điều 2 và điều 3 của quy định bảo mật bên dưới.

Nhóm chỉ cần lấy **đúng một file** từ repo này: `03-ai-spec-template.md`, copy vào repo mình và đặt tên `spec.md`. Mọi thứ còn lại là tài liệu đọc, mở tại đây là đủ.

### Cách đặt tên repo

```
K4-<mã lớp>-<phòng>-<tên nhóm>
```

| Ví dụ | Của nhóm nào |
|---|---|
| `K4-3B-E403-ChamCongAI` | Lớp 3B · phòng E403 · nhóm ChamCongAI |
| `K4-3B-E402-DiscordBuddy` | Lớp 3B · phòng E402 · nhóm DiscordBuddy |

**Ba phần đầu bắt buộc đúng.** Phòng là phòng nhóm đang ngồi thi.

**Tên nhóm ở cuối đặt gì cũng được** — viết liền, không dấu, không khoảng trắng.

**Repo phải để công khai.** Thử mở bằng cửa sổ ẩn danh — mở được thì mới đúng. Để riêng tư là giám khảo không chấm được bài.

### Cấu trúc repo

Spec chốt tại hạn chốt spec (xem Lịch); bản hoàn chỉnh trước CP6.

```
repo/
├── README.md          ← copy file này, điền bảng thành viên ở đầu
├── spec.md            ← AI Spec theo 03-ai-spec-template.md
├── demo-slides.pdf    ← slide 6 trang theo 02-guide.md §5.1
├── codebase/          ← prototype (ghi rõ phần nào mock)
├── eval/              ← golden set + bảng kết quả các lượt chạy
├── validation/        ← nhật ký cho người ngoài dùng thử (R6 — không làm thì trần điểm 92)
└── reflection/        ← mỗi người 1 file
```

### README.md của nhóm

Copy nguyên file README này về repo của mình, rồi **điền bảng thành viên ở đầu file**. Không cần viết thêm gì khác.

Mã học viên phải đúng — đây là căn cứ đối chiếu điểm.

## Chấm điểm

Tổng **100 điểm = 25 điểm nộp checkpoint + 67 điểm chấm bài nộp + 8 điểm R6** (cho người ngoài dùng thử). Chi tiết từng ý điểm: `04-rubric.md`.

**25 điểm nộp — mỗi checkpoint 5 điểm (CP1-CP5):** nộp đúng hạn → 5 điểm · nộp muộn → 0 điểm cho mốc đó. **Đội trưởng nộp thay cả nhóm — đây là điểm chung của nhóm, không phải điểm cá nhân.**

**67 điểm chấm + 8 điểm R6 — trên file trong repo, mỗi con điểm trỏ về một chỗ:**

| Khối | Điểm | Chấm trên file nào |
|---|---|---|
| R1 · Bằng chứng & impact | 15 | `spec.md` §1-§2 + log khảo sát |
| R2 · Lát cắt & thiết kế | 15 | `spec.md` §4 |
| R3 · Chỗ khó & kịch bản rủi ro | 11 | `spec.md` §5-§6 |
| R4 · Kiểm thử | 15 | `spec.md` §7 + `eval/` |
| R5 · Prototype chạy được | 8 | `codebase/` + demo |
| **R6 · Cho người ngoài dùng thử** | **8** | `validation/` |
| R7 · Quy trình & repo | 3 | cấu trúc repo |

Ba khối nặng nhất — **R1, R2, R4** — đều nằm trong `spec.md`. Viết spec tử tế là ăn 45 trên 67 điểm.

### R6 · Cho người ngoài dùng thử — 8 điểm

**Không làm thì trần điểm là 92.** Vì 25 + 67 = 92, cộng R6 mới đủ 100.

Làm ở **CP5**, lưu trong thư mục `validation/`.

**Người dùng chê cũng được tính đủ điểm.** Mục đích là xem giải pháp có ăn thua không — ra kết quả nào cũng ghi nhận, miễn là bằng chứng thật. Phát hiện sản phẩm chưa ổn rồi sửa còn dễ ăn điểm hơn, vì có chỗ cụ thể để nói.

**Hai ví dụ thật từ kỳ trước:**

**Nhóm MeaterBeat** phát hiện học viên non-IT lúng túng không biết bấm nút nào, AI trả lời chậm — tức là **giải pháp chưa ổn**. Họ thêm tooltip hướng dẫn, thêm loading spinner, và giải trình phần độ trễ không sửa được vì phụ thuộc API. **Đủ điểm.**

**Nhóm VLearn Recall** phát hiện đúng như giả định: người ta nhớ chủ đề nhưng không nhớ nằm ở slide hay bài giảng — tức là **giải pháp đi đúng hướng**. Họ giữ nguyên thiết kế source-first và bổ sung thêm câu thử. **Cũng đủ điểm.**

**Phải có đủ bốn thứ:**

| | |
|---|---|
| **5 người ngoài nhóm** dùng thử | trong đó **2 người đã khai từ CP1** |
| **Quote nguyên văn** | chép đúng lời họ nói, kể cả viết sai chính tả |
| **Bảng nhật ký** | ai thử · giao task gì · kẹt ở đâu · quote · quyết định |
| **Ít nhất 1 thay đổi** | ghi vào **§9 Changelog** trong `spec.md`. Giữ nguyên thì nói rõ vì sao |

**Cuối bảng viết 4 dòng:** chủ đề lặp nhiều nhất · sẽ sửa gì trước demo · giữ nguyên gì và vì sao · gì để dành sau.

**Quote thế nào mới ăn điểm:**

| Chưa đạt | Đạt |
|---|---|
| *"Demo này ok rồi đấy"* | *"Mình muốn tìm thông tin về code cho ReAct"* |

Bên trái là lời khen xã giao. Bên phải là lời người dùng nói **lúc đang cố làm việc** — nhìn vào biết ngay họ vướng ở đâu.

Muốn có quote như vậy: **giao task rồi ngồi im xem họ làm**, đừng hỏi "sản phẩm này hay không".

Ba điều nên biết trước khi làm:

- Điểm dựa trên **chuỗi quyết định và bằng chứng**, không dựa trên mức độ hoành tráng của sản phẩm.
- Kết quả đo **ghi nhận trung thực** — kể cả khi không đạt mục tiêu nhóm tự đặt — vẫn được tính đủ điểm. Số liệu bị chỉnh sửa hoặc che giấu sẽ không được tính.
- Reflection cá nhân chấm riêng theo rubric của khoá. Điểm vòng demo, chấm chéo trong cụm và thưởng thêm (nếu có) theo thể lệ công bố lúc khai mạc.

## Luật chung

1. Prototype có 3 mức **Sketch / Mock / Working** — mức nào cũng bắt buộc **≥1 lời gọi AI chạy thật**. Đây là thứ phải thấy được trong **video thao tác ở CP3**.
2. **Vibe-coding rule:** dùng AI để build thoải mái, nhưng không giải thích được phần có tên mình thì phần đó 0 điểm (giám khảo hỏi bất kỳ thành viên khi thuyết trình).
3. **Quality bar** chốt tại hạn chốt spec (21:00 18/9, tại CP4) và giữ nguyên sau đó.
4. Chỉ dùng dữ liệu trong `data/` hoặc dữ liệu giả tự sinh — không dùng dữ liệu thật của người thật. Không commit API key.
5. Tuân thủ **quy định bảo mật dữ liệu** bên dưới — đây là điều kiện để được cấp data.

## Bảo mật dữ liệu được cung cấp

Dữ liệu trong `data/` là dữ liệu thật của khoá học (đã ẩn danh), cấp riêng cho hackathon này. Khi nhận data, nhóm cam kết:

1. **Chỉ dùng trong phạm vi hackathon** — cho việc tìm bằng chứng, xây golden set và build prototype. Không dùng cho mục đích khác.
2. **Không chia sẻ ra ngoài khoá học** — không đăng lên mạng xã hội, không gửi cho người ngoài, không đưa vào bất kỳ dataset hay repo công khai nào.
3. **Không commit data pack vào repo nộp bài** — repo nhóm chỉ chứa trích dẫn ngắn để minh hoạ (vài dòng); golden set trích từ data ghi rõ mã đoạn/mã hội thoại thay vì dán nguyên văn dài.
4. **Cẩn trọng khi đưa data vào công cụ ngoài** — chỉ đưa phần tối thiểu cần cho việc đang làm; lưu ý API/công cụ free tier có thể dùng dữ liệu để huấn luyện (xem `02-guide.md` §3.4).
5. **Không cố suy ngược danh tính** từ dữ liệu đã ẩn danh (`S####`, `T#####`, `D####`, `[HV]`, [học viên]). Riêng `discord-pack/`: người trong đó là **bạn cùng khoá** — tuyệt đối không đoán/hỏi "tin này của ai"; trích dẫn tối đa 2 câu mỗi ví dụ (xem `data/discord-pack/README.md`).
6. Sau sự kiện, **xoá các bản sao data pack** khỏi máy cá nhân và các công cụ đã upload nếu ban tổ chức yêu cầu.

Vi phạm được xử lý theo quy định của khoá và có thể ảnh hưởng trực tiếp đến điểm của nhóm.
