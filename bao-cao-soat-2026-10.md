# Báo cáo soát nội dung — 19/10/2026

**Người soát:** Claude · **Phạm vi:** 22 bài · hơn 100 nguồn mở lại · 5 mặt soát
**Trạng thái:** đã sửa vào file, **chưa đăng** — chờ anh duyệt bằng GitHub Desktop hoặc `./dang-bai.sh`

---

## Trước hết: tác vụ tự động có chạy, nhưng báo cáo không tới được anh

Tác vụ soát định kỳ **đã chạy đúng hạn ngày 01/10/2026**, lúc 9h08 sáng giờ Việt Nam, và chạy hết **2 tiếng 44 phút** mới xong. Nó không hỏng.

Vấn đề nằm ở chỗ khác: **mỗi lần tác vụ chạy, nó mở một cuộc trò chuyện riêng.** Báo cáo được gửi vào đó, không vào cuộc trò chuyện anh đang dùng. Anh có bật thông báo qua điện thoại và email cho tác vụ này, nhưng rõ ràng là nó không tới được chỗ anh nhìn thấy.

Đây là lỗi thiết kế của tôi khi dựng tác vụ, không phải lỗi của anh. Phần cuối báo cáo có mục bàn cách chữa.

Vì không lấy lại được báo cáo cũ, tôi **soát lại từ đầu ngay trong phiên này**.

---

## Tóm tắt một đoạn

Đã đọc trọn 22 bài, mở lại hơn 100 đường nguồn, đối chiếu từng con số với bài báo gốc. Tìm được **5 lỗi nặng** (trong đó **3 lỗi liên quan tới an toàn của người đọc**), **12 lỗi vừa**, và một số lỗi nhỏ. Đã sửa **16 bài** và **11 sơ đồ**. Cũng vá **6 lỗ hổng bảo mật** của thư viện dựng website.

Tin tốt: **toàn bộ khuyến cáo y tế trên website vẫn đúng tính tới hôm nay** — không có mục nào lạc hậu, không có link chết. Và hai lỗi lịch sử của bài kể chuyện (con số Rottman, đếm "bốn câu chuyện") vẫn đang đúng.

---

## BA LỖI LIÊN QUAN TỚI AN TOÀN — nên để ý nhất

### 1. Bài thai kỳ không có một chữ nào về giấc ngủ an toàn của trẻ sơ sinh

**Bài:** *Chín tháng, và một danh sách ngắn hơn bạn tưởng*

Đây là bài **duy nhất** của chuyên mục *"Mang thai & năm đầu đời"* — chuyên mục mà chính website mô tả là *"từ khi biết tin đến khi con tròn một tuổi"*. Nhưng cả bài dừng lại ở lúc sinh.

Nguy hiểm hơn là chỗ dễ lẫn: **chỗ duy nhất trong bài có chữ "nằm ngửa" lại nói nằm ngửa là nguy hiểm.** Điều đó đúng — với **thai phụ** từ tuần 28. Nhưng với **trẻ sau sinh thì ngược hoàn toàn**: nằm ngửa là tư thế bảo vệ, còn nằm nghiêng thì Viện Nhi khoa Hoa Kỳ nói nguyên văn là *"nguy hiểm ngang với nằm sấp"*.

Một người mẹ mới sinh nhớ lại bài này và đặt con nằm nghiêng "cho giống lúc mang thai" thì đã làm đúng điều cần tránh nhất trong cả lĩnh vực sơ sinh.

**Đã sửa:** thêm **mục 8** vào danh sách — chỗ ngủ an toàn, trích đúng khuyến nghị hiện hành của Viện Nhi khoa Hoa Kỳ (nằm ngửa mọi giấc ngủ · mặt phẳng cứng và phẳng · không gối, chăn rời, thú nhồi bông, quây cũi · cùng phòng nhưng không cùng giường, ít nhất 6 tháng · áp dụng suốt năm đầu). Kèm một khối cảnh báo nói thẳng rằng **tư thế của mẹ và tư thế của con là hai chuyện ngược nhau**.

*Nguồn tôi đã tự mở:* [AAP — A Parent's Guide to Safe Sleep](https://www.healthychildren.org/English/ages-stages/baby/sleep/Pages/a-parents-guide-to-safe-sleep.aspx) (trang cập nhật 11/09/2026)

---

### 2. Bài thai kỳ bỏ mất liều acid folic gấp 10 lần, cho đúng nhóm người cần nó nhất

**Bài:** *Chín tháng…* — khối cảnh báo về acid folic

Bài viết: *"Đúng liều, đúng lúc, đúng mục đích. **Không cần uống nhiều hơn khuyến nghị.**"* — ngay sau khi nêu các con số 400 và 400–800 mcg.

Nhưng Cơ quan phòng bệnh Hoa Kỳ có một ngoại lệ: người **đã từng mang thai mà con bị dị tật ống thần kinh**, nếu muốn có thai lại, được khuyến nghị **4.000 mcg mỗi ngày** — gấp mười lần.

Nghĩa là đúng nhóm người đã mất một đứa con vì dị tật ống thần kinh sẽ đọc câu đó và yên tâm uống một phần mười liều mình cần.

**Đã sửa:** thêm hẳn một đoạn nêu ngoại lệ, kèm lời dặn đây là trường hợp phải do bác sĩ chỉ định.

*Nguồn tôi đã tự mở:* [CDC — Folic Acid: Facts for Clinicians](https://www.cdc.gov/folic-acid/hcp/clinical-overview/index.html) (xem lại lần cuối 16/07/2026). Nguyên văn: *"it is recommended they get 4,000 mcg of folic acid daily"*.

---

### 3. Bài thai kỳ tuyên bố danh sách của mình là đầy đủ, trong khi không hề nhắc tiêm chủng hay sàng lọc

**Bài:** *Chín tháng…* — câu *"Hết. Đó là danh sách."* và câu kết *"Phần còn lại, phần lớn là quảng cáo."*

Hai câu này đóng lại cả bài, nên chúng là thứ người đọc nhớ. Đặt cạnh nhau, chúng dạy người đọc một quy tắc: *không có trong bảy mục này thì không cần.*

Cả bài không có một chữ nào về tiêm chủng trong thai kỳ, sàng lọc tiền sản giật, đái tháo đường thai kỳ, theo dõi huyết áp hay cân nặng. Một thai phụ được mời tiêm vắc-xin, hoặc được hẹn làm nghiệm pháp đường huyết, hoàn toàn có thể nhớ lại câu kết của bài và từ chối.

**Đã sửa:** đổi thành *"Hết. Đó là tám việc."* kèm một đoạn nói rõ đây là danh sách về **dinh dưỡng và lối sống** — những việc anh tự quyết ở nhà — chứ không phải toàn bộ danh mục chăm sóc thai kỳ, và những việc kia nằm trong tám lần khám. Câu kết đổi thành *"Phần còn lại — những thứ được **bán** cho bạn — phần lớn là quảng cáo."*

---

## HAI LỖI NẶNG VỀ TOÀN VẸN NGUỒN

### 4. Nghiên cứu Rottman bị gán sai ý nghĩa ở cả bốn chỗ

**Bài:** *Kể chuyện thế nào thì con thực sự đổi*

Bài viết các tỷ lệ 22,86% · 46,75% · 58,82% là *"trẻ đổi sang cách chia **công bằng**"*. Các con số thì đúng — nhưng nhãn thì sai.

Tôi đã mở bản toàn văn. Biến kết quả được định nghĩa là trẻ có **chuyển giữa hai nguyên tắc chia** (chia đều / chia theo công sức) theo đúng hướng truyện khuyên hay không. Mỗi đứa trẻ được nghe đúng nguyên tắc **ngược** với cách nó vừa chia — nên **một nửa số trẻ được thuyết phục sang hướng "ai làm nhiều hơn thì được nhiều hơn"**, tức chia *không* đều.

Đây là nghiên cứu về **mức dễ bị thuyết phục**, không phải về lòng công bằng. Một phụ huynh đọc "46,75% trẻ đổi sang cách chia công bằng" sẽ hiểu là gần một nửa số trẻ trở nên tử tế hơn.

Thêm một chỗ nữa: bài rút ra *"nói thẳng cũng được, **có khi còn hơn**"* bằng cách so 67,33% (thí nghiệm 2) với 46,75% (thí nghiệm 3) — hai mẫu khác nhau. Chỗ nhóm tác giả **có** so trực tiếp, trong cùng một thí nghiệm, thì hai cách **không khác nhau đáng kể** (p = 0,212), và họ kết luận nguyên văn: *thứ quyết định là bài học, không phải bản thân câu chuyện.*

**Đã sửa:** thân bài, `alt` của sơ đồ, dữ liệu sơ đồ trong `make-figures.py`, và ghi chú mục nguồn — cả bốn chỗ.

*Nguồn tôi đã tự mở:* [Rottman và cộng sự 2020, bản toàn văn](https://www.bu.edu/cdl/files/2020/10/Rottman-et-al-2020.pdf)

---

### 5. Bài tấm gương nói chắc ở bốn chỗ mà nguồn không cho phép

**Bài:** *Vì sao bác hàng xóm hiệu quả hơn danh nhân* — đây hiện là bài yếu nhất về toàn vẹn nguồn.

| Bài đang nói | Nguồn thật sự nói |
| --- | --- |
| *"Họ đếm số giờ tình nguyện thật, **đối chiếu với hồ sơ của các tổ chức**"* | Cả hai thí nghiệm đều dùng **bản tự khai**; chính nhóm tác giả nêu thiên lệch mong muốn xã hội là điểm yếu cơ bản nhất |
| *"**Cả hai lần**, nhóm đọc về tấm gương gần tham gia nhiều hơn hẳn"* | Thí nghiệm 1 **không đạt ý nghĩa thống kê** (p = 0,17); tác giả quy cho mẫu 54 người quá nhỏ. Chỉ thí nghiệm 2 đạt rõ |
| *"…khi tấm gương đạo đức **ở quá xa tầm với**, phản ứng là hạ thấp người đó"* | Nhan đề bài báo là *"…to Defuse **Anticipated Reproach**"* — cơ chế là **cảm giác bị phán xét**, không phải khoảng cách. Làm trên sinh viên, không làm trên trẻ em |
| *"Hai nhóm đọc về phần vật lộn có điểm số **tăng lên**"* | **Không đạt ý nghĩa thống kê** (p = 0,17 và p = 0,51). Khoảng cách giữa các nhóm đến từ việc nhóm chỉ-đọc-thành-tựu **tụt xuống**, không phải hai nhóm kia đi lên |

Chỗ cuối đáng ngại nhất vì **hình vẽ còn phóng to cái phần không có thật** — hai cột "tăng" vẽ to hơn cột "giảm", ngược hẳn tỷ lệ thật.

**Đã sửa:** cả bốn chỗ, cộng `description`, `alt`, `caption`, dữ liệu sơ đồ và hai ghi chú nguồn. Kết luận thực hành của bài **vẫn đứng** — chỉ là giờ nó dựa trên lý do đúng: không phải vì kể vật lộn làm điểm tăng, mà vì chỉ kể thành tựu làm điểm tụt.

*Nguồn tôi đã tự mở:* [Han và cộng sự 2017](https://www.frontiersin.org/articles/10.3389/fpsyg.2017.00283/pdf) · [Lin-Siegler và cộng sự, *Even Einstein Struggled*](https://www.tc.columbia.edu/media/administration/tc-academy/program-images/Even-Einstein-Struggled.pdf) · [Minson & Monin 2012](https://vegstudies.univie.ac.at/fileadmin/user_upload/p_foodethik/Minson__J._and_Monin__B_2012._Do-Gooder_Derogation_-_About_Vegetarians_...._200.full.pdf)

---

## LỖI VỪA — đã sửa hết

| # | Bài | Chuyện gì | Đã làm gì |
| --- | --- | --- | --- |
| 6 | *"Nếu… thì…"* | Bài dùng con số **d = 0,65** mà **chính nhóm tác giả đã tự hạ xuống** năm 2025: gộp 642 phép kiểm còn **d = 0,36**, và sau khi chỉnh sai lệch công bố còn **0,15**. Chính họ gọi là *"nhỏ theo thước đo thông thường"*. Bài lại không nêu một chữ phản biện nào — trong khi đây là chủ đề nằm trong danh sách khủng hoảng nhân bản | Thêm hẳn đoạn nêu phía phản biện, thêm mục nguồn 2025, và thêm một câu gỡ áp lực cho cha mẹ: *"nếu tuần sau nhà bạn chưa khác đi nhiều, đó là bình thường"* |
| 7 | *"Nếu… thì…"* | `description` hứa *"hiệu quả hơn hẳn việc nhắc"* — không nghiên cứu nào so với việc nhắc. Nhóm đối chứng là nhóm **không có kế hoạch "nếu–thì"** | Viết lại `description`, `subtitle`, và hai câu trong thân bài |
| 8 | *"Nếu… thì…"* | *"trẻ có khó khăn về chú ý"* — nguồn nói **trẻ được chẩn đoán ADHD**, và chỉ *"ở một số phép phân tích"*. Hai nhóm rộng hẹp khác hẳn nhau | Sửa cho đúng nguồn, giữ nguyên bổ ngữ hạn định |
| 9 | *Tự giác không mọc lên từ lời nhắc* | *"lời khen mô tả việc con làm thì **chưa thấy có mặt hại nào**"* — nguồn nói khen **nỗ lực** có thể bị hiểu là *"giải thưởng an ủi hoặc tín hiệu con kém", **nhất là ở tuổi teen***. Bài này gắn cho cả nhóm 15–18 tuổi | Viết lại thành lời khuyên thật dùng được: với con lớn, khen vào **cách con làm** an toàn hơn khen vào việc con đã cố |
| 10 | *Tự giác…* (sơ đồ) | Ghi chú sơ đồ bỏ mất **nhóm đối chứng 14%**, làm hình kể thành "khen chăm chỉ giúp trẻ bớt gian lận ba lần". Thật ra khen chăm chỉ (13%) ngang với không khen gì (14%); chỉ khen thông minh làm **tăng** lên 38% | Thêm nhóm đối chứng vào ghi chú |
| 11 | *Tự giác…* (sơ đồ) | Tiêu đề hình ghi *"…của **trẻ**"* nhưng hai trong ba con số là số gộp mọi lứa tuổi | Bỏ chữ "của trẻ" khỏi tiêu đề |
| 12 | *Não của con đang xây theo kiểu nào* **và** *Sáu năm đầu đời* | *"Việc cắt tỉa… **mạnh nhất** chính là ở tuổi teen"* — nguồn chỉ nói việc cắt tỉa ở vùng trán **kéo dài tới** giữa tuổi teen, không nói gì về cường độ. Và chính bài kia viết đúng ở một chỗ khác, tức là bài tự mâu thuẫn | Sửa cả hai bài về đúng điều nguồn nói |
| 13 | *Não tuổi teen đang xây lại* | *"ở đúng giai đoạn **não cần ngủ nhất**"* — ngược với chính con số bài vừa trích: Viện Y học Giấc ngủ Hoa Kỳ khuyến nghị teen 13–18 ngủ **8–10 tiếng**, **ít hơn** nhóm 6–12 tuổi (9–12 tiếng) | Đổi thành điều đúng và vẫn mạnh: *"đúng vào lúc cơ thể nó đã tự đẩy giờ buồn ngủ muộn đi tới hai tiếng"*. Sửa cả `caption` |
| 14 | *Não tuổi teen…* (sơ đồ) | Cột "khuyến nghị" vẽ ở **9** nhưng phần thiếu lại tính từ **8** — người đọc trừ bằng mắt ra 2,5 tiếng, mà hình ghi 1,5 | Đổi cột đầu về đúng mức sàn 8 và ghi rõ trong nhãn |
| 15 | *Khi con bắt đầu đóng cửa phòng* | `description` vẫn còn câu doạ: *"cách cha mẹ phản ứng **sẽ quyết định cửa còn mở hay khép hẳn**"* — đúng loại câu đã gỡ khỏi thân bài hồi tháng 8, và mâu thuẫn với chính thân bài lẫn hai bài khác | Viết lại `description` |
| 16 | *Khi con bắt đầu đóng cửa phòng* | Một câu **thiếu chữ** làm nghĩa thành ngược: *"Không phải nhìn vào mắt nhau làm giảm áp lực"* — đọc ra thành phủ định, trong khi mục này tên là *"Đi cạnh nhau, đừng ngồi đối diện"* | Thêm chữ "Việc", và *"nhìn thẳng vào mắt nhau"* |
| 17 | *Khi con bắt đầu đóng cửa phòng* | *"**Sau vài tuần, sẽ có lần** con giữ bạn lại nói chuyện"* — hứa chắc một kết quả có thời hạn, không nguồn. Cha mẹ làm đúng năm tuần mà không thấy gì sẽ nghĩ mình làm sai | Đổi thành lời kể của nhiều cha mẹ, kèm câu nói rõ đây không phải thước đo |
| 18 | *Cơn giận của con, và cơn giận của mình* | Đoạn về "cạn ý chí" nói *"đều không tìm lại được hiệu ứng"* — đúng tới tháng 8/2026, nhưng **tháng 10/2025 đã có một công trình đa phòng thí nghiệm tìm thấy hiệu ứng**. Và bài không có **một mục nguồn nào** | Viết lại đoạn cho đúng là tranh luận chưa ngã ngũ, **thêm khối nguồn 3 mục** (cả hai phía), và gỡ chữ "cạn" khỏi phụ đề cùng ba chỗ khác cho khỏi tự mâu thuẫn |
| 19 | *Kỷ luật không phải là phạt* | Ghi chú nguồn nói nghiên cứu Talwar & Lee đo *"trẻ bị phạt **vì nói dối**"*. Thật ra nó đo **môi trường trừng phạt nói chung** (trẻ bị đánh vì quên bút), và đo trên **trẻ 3–4 tuổi** trong khi bài gắn cho nhóm 6–14 | Viết lại cả thân bài lẫn ghi chú, nêu đúng con số (94% / 55%) và nói rõ hai giới hạn |
| 20 | *Kỷ luật không phải là phạt* | Bài nói *"bằng chứng đủ mạnh để nói thẳng"* — mạnh hơn mức chính tác giả tự nhận: họ viết rằng chưa loại được khả năng **trẻ khó hơn thì bị đánh nhiều hơn** | Thêm một đoạn nêu phía phản biện, **và** thêm báo cáo WHO tháng 8/2025 — nguồn này làm kết luận của bài **vững hơn**, không yếu đi |
| 21 | *Năm điều ai cũng nói về nuôi con* | Bảng "kẹo dẻo" chia sai các bước: *"năng lực sẵn có của trẻ"* **đã nằm trong** bước giảm hai phần ba rồi. Bước cuối thêm vào là những gì đo lúc **4 tuổi rưỡi** | Sửa bảng, `alt` và dữ liệu sơ đồ |
| 22 | *Chín tháng…* (sơ đồ) | Ghi chú in trên ảnh biến một hướng dẫn **dành cho giới nghiên cứu** (*"Future researches are recommended to avoid…"*) thành một ngưỡng an toàn nói với thai phụ — trái hẳn với thân bài, vốn đã nói rất đúng. Ảnh bị chụp lại và chia sẻ rời khỏi bài thì đọc thành *"dưới 65 dB thì áp loa lên bụng được"* | Bỏ hẳn phần ngưỡng khỏi ảnh |

Ngoài ra: sửa câu trích "hiệu ứng Mozart" cho đúng (nguồn nói riêng về bản sonata KV 448 và bài kiểm tra tư duy không gian, không nói chung chung) · sửa câu về thuốc lá cho khớp đúng điều nguồn NHS nói · bỏ một so sánh gán cho Adele Diamond mà bài báo của bà không đưa ra · dịch *"vấn đề nội tâm"* thành **lo âu và trầm cảm** kèm giải thích *r* bằng lời thường · ba chỗ thiếu chữ (*"cho lần sau tức"*, *"không dễ như nghe"*, và câu ở mục 16) · hai ghi chú sơ đồ nói chắc hơn thân bài.

---

## BẢO MẬT — đã vá

`npm audit` báo **6 lỗ hổng** (1 trung bình, 5 mức cao) trong các thư viện phụ. Đã vá bằng một lệnh. Sau khi vá: **0 lỗ hổng**.

Nói cho đúng mức độ, đừng để anh lo: website của anh là **trang tĩnh**, mọi thứ dựng sẵn rồi mới đưa lên mạng. Nguy cơ thực tế với anh là **thấp**. Nhưng đây là thứ vá bằng một lệnh nên không có lý do để lâu. Chỉ file khai báo phiên bản thay đổi; không một dòng nội dung nào bị ảnh hưởng.

---

## NHỮNG GÌ ĐÃ KIỂM VÀ THẤY SẠCH

**Toàn bộ khuyến cáo y tế vẫn đúng tính tới 19/10/2026.** Đã mở và đối chiếu từng cái:

| Tổ chức | Chủ đề | Kết quả |
| --- | --- | --- |
| Viện Nhi khoa Hoa Kỳ | Màn hình | Bản 01/2026 **vẫn là bản mới nhất**. Con số 1–2 giờ/ngày khớp nguyên văn |
| Viện Nhi khoa Hoa Kỳ | Giấc ngủ trẻ em, giấc ngủ an toàn sơ sinh | Không có bản mới hơn |
| Viện Y học Giấc ngủ Hoa Kỳ | Thời lượng ngủ theo tuổi | Bản 2016 vẫn hiện hành, hai câu trích khớp 100% nguyên văn |
| WHO | Màn hình dưới 5 tuổi · khám thai 8 lần · i-ốt · sức khoẻ tinh thần chu sinh | Không có bản mới. Mọi con số khớp |
| Cochrane | Acid folic · omega-3 | **Cả hai vẫn ở đúng phiên bản website đang dẫn** — đây là rủi ro lớn nhất vì một tổng quan Cochrane được cập nhật thì kết luận có thể đổi hẳn |
| USPSTF | Acid folic | Mức A, bản 2023, không có bản mới |
| CDC | Rượu bia & thai kỳ | Trang xem lại 10/08/2026, hai câu trích khớp nguyên văn |
| NIMH | Não tuổi teen | Bản 2023, khớp |

**Không có link chết.**

Và một chỗ bài làm rất đúng, đáng giữ: cú đổi hướng dẫn màn hình của Viện Nhi khoa Hoa Kỳ hồi tháng 1/2026 — thứ từng làm bài này lạc hậu một lần — đã được xử lý đúng, dẫn đúng tài liệu, trích đúng nguyên văn.

---

## MỘT LỖI NHỎ DO CHÍNH TÔI GÂY RA HÔM NAY

Khi sửa ghi chú sơ đồ bài kỷ luật, tôi thay nhầm nửa câu và để lại một câu lặp: *"Nhưng cột phải Nhiều cha mẹ thấy cột phải nhẹ dần…"*. Tôi phát hiện khi đọc lại chữ đã vẽ ra trên ảnh, và đã sửa rồi vẽ lại. Ghi ở đây vì sổ tay phải trung thực.

---

## MỘT CÁI BẪY VỀ ẢNH BÌA — đã rõ hơn trước

Hồi 17/09 tôi phát hiện cả 22 ảnh bìa đổi khi vẽ lại, và quy cho máy thiếu font Inter.

Hôm nay máy tôi **có** font Inter — và cả 22 ảnh bìa **vẫn đổi**, mỗi ảnh hơn chục nghìn pixel, đúng ở vùng chữ.

Nghĩa là nguyên nhân rộng hơn tôi tưởng: **ảnh bìa không tái tạo được giống nhau giữa các máy**, dù có đúng font. Tôi đã đo từng ảnh một để chắc chắn đây không phải chuyện metadata, rồi **trả lại toàn bộ 22 ảnh bìa** và chỉ giữ 11 sơ đồ thực sự cần đổi.

Đã ghi lại thành quy tắc cứng trong `CLAUDE.md`: **đừng bao giờ nhận ảnh bìa mới trừ khi chữ trên bìa thật sự đổi** — luôn trả lại bằng `git checkout --`.

---

## BA VIỆC TÔI *KHÔNG* LÀM, VÀ VÌ SAO

**1. Không thêm nguồn về văn bản quan điểm của Viện Nhi khoa châu Âu.** Có dấu hiệu rằng tháng 7/2026 các hiệp hội nhi khoa châu Âu ra một văn bản **vẫn giữ con số làm trung tâm** (dưới 2 tuổi tránh màn hình; 3–5 tuổi một giờ; trên 5 tuổi dưới hai giờ) — tức là ngược với hướng của Viện Nhi khoa Hoa Kỳ, và đáng lẽ bài màn hình nên nêu cả hai phía.

Nhưng **tôi dùng hết hạn mức tìm kiếm của phiên trước khi tự mở được tài liệu đó**. Theo quy tắc 5, tôi không đưa vào một nguồn mình chưa tự mở. Đây là **việc đáng làm nhất ở lần soát sau** — hoặc anh nhắn tôi trong phiên mới thì tôi tra nốt.

**2. Không sửa một vài khẳng định chưa có nguồn** mà tôi chưa kịp tra (con số "lệch 2 tiếng cuối tuần" ở bài tuổi teen; hai mốc "6 tuổi / 11 tuổi" ở bài sáu-đến-mười-hai; một câu về tần suất gọi điện ở bài con đã trưởng thành). Chúng **không sai** theo bất cứ nguồn nào tôi mở được — chỉ là chưa có gì đỡ. Để nguyên còn hơn sửa mò.

**3. Không đăng gì lên mạng.** Như mọi lần.

---

## VIỆC CẦN ANH QUYẾT

### a) Chữa chỗ báo cáo tự động không tới được anh

Ba cách, anh chọn:

1. **Giữ nguyên, anh tự đi tìm.** Báo cáo 01/10 vẫn còn trong cuộc trò chuyện riêng của tác vụ. Thử tìm trong danh sách tác vụ đã chạy, hoặc kiểm email ngày 01/10.
2. **Đổi lời nhắc của tác vụ** để nó mở đầu bằng một dòng không thể bỏ sót và nói rõ anh cần làm gì tiếp. Tôi làm được ngay, không mất gì.
3. **Bỏ tác vụ tự động, thay bằng việc anh nhắn tôi "soát nội dung" mỗi quý.** Chậm hơn nhưng chắc chắn tới tay anh — vì nó diễn ra ngay trong cuộc trò chuyện anh đang dùng.

Tôi nghiêng về **cách 3 kết hợp cách 2**: giữ tác vụ để nó nhắc, nhưng việc soát thật thì làm ở chỗ anh nhìn thấy.

### b) Hai việc còn tồn từ 29/09

- Có đổi tên hiển thị trong lịch sử đăng bài không? Lần đăng 02/10 vừa rồi **vẫn mang tên `Nam Dinh Van`** và email trường đại học. Hai dòng lệnh đã có sẵn ở Phần C việc 0c.
- Có cài đăng nhập GitHub cho WSL không?

---

## GIỜ ANH LÀM GÌ

Mở **GitHub Desktop**, xem lại thay đổi, rồi bấm **Commit** và **Push**.

Hoặc, nếu muốn thử cách mới:

```bash
cd "/mnt/c/Users/admin/Downloads/Note giáo dục trẻ/dong-hanh-cung-con"
./dang-bai.sh "soát nội dung tháng 10: sửa 16 bài, vá bảo mật"
```

Nó sẽ cho anh xem **từng chữ** đã đổi trước khi hỏi ý. Với đợt này thì đáng xem — có 16 bài thay đổi.

Website tự dựng lại khoảng 2–3 phút sau đó.
