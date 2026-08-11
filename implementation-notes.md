---
title: "Sổ tay vận hành dự án"
subtitle: "Đọc file này là biết dự án đang ở đâu, vừa thay đổi gì, và bạn tự làm được những gì"
version: "1.0.0"
date: "2026-08-11"
---

# Sổ tay vận hành dự án

> **File này dành cho bạn — người chủ dự án, không phải người viết code.**
>
> Không cần đọc một lượt từ đầu đến cuối. Cần gì tra nấy:
>
> | Bạn muốn | Đọc phần |
> | --- | --- |
> | Biết dự án đang có gì | **A** |
> | Nhờ Claude làm việc gì đó | **B** |
> | Tự làm mà không cần Claude | **C** |
> | Không hiểu một từ nào đó | **D** |
> | Đang gặp một tình huống cụ thể | **E** |
> | Xem đã thay đổi những gì | **F** |
> | Kiểm tra Claude có làm đúng không | **G** |

**Nguyên tắc của sổ tay này:** mỗi lần Claude chạm vào dự án, Claude **bắt buộc** ghi vào Phần F — đã làm gì, vì sao, ảnh hưởng gì tới bạn, và *nếu tự làm thì làm thế nào*. Bạn không phải nhớ. Bạn chỉ cần đọc.

---

## PHẦN A — Dự án đang ở đâu

*Cập nhật lần cuối: 11/08/2026*

### Tình trạng chung

| Hạng mục | Hiện tại |
| --- | --- |
| Tên website | Đồng hành cùng con |
| Đã lên mạng chưa? | ⏳ **Sắp** — còn 2 việc ở dưới |
| **Địa chỉ website sẽ là** | **https://lucero6886.github.io/dong-hanh-cung-con/** |
| Tài khoản GitHub | `Lucero6886` |
| Mã nguồn trên mạng | <https://github.com/Lucero6886/dong-hanh-cung-con> (công khai ✓) |
| Nhánh đang dùng | `master` |
| Nơi lưu mã nguồn | Máy bạn: `Downloads\Note giáo dục trẻ\dong-hanh-cung-con\` |
| Số bài viết | **3** bài, đã xuất bản cả 3, không có bài nháp |
| Số chủ đề đang dùng | **3** / 10 chủ đề đã chuẩn bị sẵn |
| Số thẻ | **9** |
| Số trang website tự sinh ra | **28** |
| Tình trạng kỹ thuật | ✅ Chạy tốt, 0 lỗi, 0 cảnh báo |

### Ba bài viết hiện có

| Bài | Chủ đề | Nguồn gốc |
| --- | --- | --- |
| Từ phần thưởng đến động lực bên trong | Động lực & thói quen | Biên tập từ file Word của bạn |
| Hỏi con học được gì, thay vì hỏi con được mấy điểm | Giao tiếp cha mẹ – con | Mở rộng từ bài trên |
| Cấu trúc thay vì nhắc nhở | Tự lập & trách nhiệm | Mở rộng từ bài trên |

### Chín thẻ đang dùng

`cha mẹ` · `giao tiếp` · `giáo dục` · `phần thưởng` · `thói quen` · `trách nhiệm` · `tự giác` · `tự học` · `động lực`

### ✅ Đã xong

- [x] **1. Có tài khoản GitHub** — `Lucero6886`
- [x] **2. Claude đã biết tên tài khoản** — đã điền vào cấu hình, mọi địa chỉ trong website giờ trỏ đúng
- [x] **3. Cài GitHub Desktop và đẩy dự án lên** — mã nguồn đã nằm trên GitHub, công khai

### ⏳ Còn hai việc — làm đúng thứ tự này

**Việc 1 — Bật công tắc GitHub Pages** *(2 phút, chỉ bạn làm được)*

Đây là việc bật cho website được phép hiện ra. Chưa bật thì vào link sẽ hiện "404".

1. Mở <https://github.com/Lucero6886/dong-hanh-cung-con/settings/pages>
2. Phần **`Build and deployment`**, ô **`Source`** đang là *"Deploy from a branch"*
3. Bấm vào và **chọn `GitHub Actions`**
4. Xong — nó tự lưu, không có nút Save

**Việc 2 — Đẩy bản sửa của Claude lên** *(1 phút)*

Claude vừa sửa 2 file (xem lý do ở **Phần F**, mục ngày 11/08). Chưa đẩy lên thì website vẫn không chạy.

1. Mở **GitHub Desktop**
2. Cột trái hiện 2 file đã đổi: `.github/workflows/deploy.yml` và `src/config/site.ts`. Bấm xem thử nếu muốn.
3. Ô dưới bên trái gõ: *"sửa địa chỉ website và nhánh"*
4. Bấm **`Commit to master`** → rồi bấm **`Push origin`**

**Sau đó:** chờ khoảng 2 phút, rồi mở <https://lucero6886.github.io/dong-hanh-cung-con/>

Muốn xem nó đang chạy tới đâu: <https://github.com/Lucero6886/dong-hanh-cung-con/actions> — chờ dấu tích xanh.

> Xong hai việc này là website chính thức lên mạng. Từ đó về sau chỉ còn việc viết bài.

### Quy trình sau khi xong 4 việc trên

```
Bạn đưa ghi chép cho Claude
        ↓
Claude biên tập và ghi file vào thư mục trên máy bạn
        ↓
Claude ghi vào Phần F của sổ tay: đã làm gì, vì sao
        ↓
Bạn mở GitHub Desktop → NHÌN THẤY chính xác Claude đã đổi những gì
        ↓
Ưng thì bấm 2 nút. Không ưng thì bấm "Discard" để huỷ.
        ↓
2 phút sau website tự cập nhật
```

> Bước "nhìn thấy chính xác Claude đã đổi gì" chính là câu trả lời cho lo ngại của bạn. **Không có gì lên mạng mà bạn chưa nhìn qua và chưa bấm đồng ý.**

---

## PHẦN B — Làm việc với Claude thế nào

### Ai làm gì

| Việc | Ai làm | Vì sao |
| --- | --- | --- |
| Nghĩ ra ý tưởng bài viết | **Bạn** | Đây là giá trị của dự án. Không ai thay được. |
| Ghi chép thô, kể trải nghiệm | **Bạn** | Chất liệu gốc phải là của bạn. |
| Biên tập thành bài hoàn chỉnh | Claude | Việc kỹ thuật về câu chữ và định dạng. |
| Kiểm chứng nguồn khoa học | Claude, **bạn duyệt** | Claude tra, nhưng bạn là người chịu trách nhiệm cuối. |
| Tạo file, đặt tên, điền thông tin kỹ thuật | Claude | Đây là chỗ dễ sai và không thú vị. |
| Kiểm tra website không lỗi | Claude | Chạy máy móc. |
| Đẩy bài lên mạng | Claude | Một câu lệnh. |
| **Quyết định đăng hay không** | **Bạn** | Luôn luôn là bạn. |
| Ghi lại vào sổ tay này | Claude | Bắt buộc, sau mỗi thay đổi. |

### Câu mẫu để nhắn cho Claude

Copy nguyên câu, thay phần trong ngoặc:

**Đăng bài mới từ ghi chép**

```
Đây là ghi chép của tôi về (chủ đề).
Biên tập thành bài viết cho website rồi đăng lên giúp tôi.
Nhớ cập nhật sổ tay vận hành.

(dán ghi chép của bạn vào đây)
```

**Đăng bài từ file Word**

```
Tôi vừa để file (tên file).docx vào thư mục dự án.
Đọc và biên tập thành bài viết cho website giúp tôi.
Giữ nguyên luận điểm của tôi, phần nào bạn thêm vào thì nói rõ.
```

**Sửa một bài đã đăng**

```
Bài "(tên bài)" cần sửa: (nói rõ muốn sửa gì).
Sửa xong nhớ ghi vào sổ tay.
```

**Gỡ một bài xuống ngay**

```
Gỡ bài "(tên bài)" xuống khỏi website, giữ lại nội dung để sau đăng lại.
```

**Đổi thông tin website**

```
Đổi (tên website / tên tác giả / dòng bản quyền / menu) thành: (nội dung mới).
```

**Không hiểu chuyện gì đang xảy ra**

```
Giải thích cho tôi bằng tiếng Việt đời thường: (điều bạn không hiểu).
Tôi không biết code, đừng dùng từ chuyên môn.
```

**Kiểm tra sức khoẻ dự án**

```
Kiểm tra toàn bộ dự án xem có gì hỏng không, rồi báo cáo cho tôi
bằng ngôn ngữ dễ hiểu. Cập nhật phần A của sổ tay vận hành.
```

### Quy tắc Claude phải tuân theo

Các quy tắc này đã được ghi vào file `CLAUDE.md` trong dự án, nên **mọi phiên làm việc với Claude về sau đều tự động đọc được**, kể cả khi bạn mở một cuộc trò chuyện hoàn toàn mới:

1. Sau mỗi thay đổi, ghi một mục vào **Phần F** của sổ tay này.
2. Cập nhật lại số liệu ở **Phần A**.
3. Không đăng bài nào khi chưa hỏi ý bạn.
4. Không bịa nguồn, không bịa số liệu, không bịa nghiên cứu.
5. Giữ nguyên luận điểm gốc của bạn; phần nào Claude thêm vào phải nói rõ.
6. Giải thích bằng tiếng Việt đời thường, không dùng từ chuyên môn mà không dịch.

> Nếu có lúc nào Claude làm mà không ghi sổ, bạn cứ nhắc: *"Cập nhật sổ tay vận hành đi."*

---

## PHẦN C — Những việc bạn tự làm được, không cần Claude

Đây là phần quan trọng nhất của sổ tay. **Tất cả đều làm trên trình duyệt web, không cài phần mềm, không gõ lệnh.**

Mục đích: để bạn không bao giờ bị kẹt khi không có Claude bên cạnh.

> **Chuẩn bị chung:** mở <https://github.com>, đăng nhập, vào repo `dong-hanh-cung-con` của bạn.
> "Repo" chỉ là cái tên gọi thư mục dự án đặt trên mạng. Xem Phần D.

---

### Việc 0 — Cài GitHub Desktop (một lần duy nhất, quan trọng nhất)

GitHub Desktop là một ứng dụng miễn phí do chính GitHub làm. Nó là **cây cầu** giữa thư mục trên máy bạn và website trên mạng — và quan trọng hơn, nó **cho bạn xem trước mọi thay đổi** trước khi chúng lên mạng.

**Cài đặt**

1. Vào <https://desktop.github.com>, tải bản cho Windows, cài như mọi phần mềm khác
2. Mở lên, bấm **`Sign in to GitHub.com`** → trình duyệt mở ra → đăng nhập → xong
3. Bấm **`File`** → **`Add local repository`**
4. Bấm **`Choose…`**, trỏ tới thư mục:
   `C:\Users\admin\Downloads\Note giáo dục trẻ\dong-hanh-cung-con`
5. Bấm **`Add repository`**

**Đưa dự án lên mạng lần đầu**

6. Bấm nút **`Publish repository`** ở thanh trên
7. Tên để nguyên `dong-hanh-cung-con`
8. **Bỏ tích ô `Keep this code private`** — website công khai thì mã nguồn phải công khai (GitHub Pages miễn phí yêu cầu vậy)
9. Bấm **`Publish repository`**

Xong. Mã nguồn đã lên GitHub. Giờ quay lại làm **việc số 6** để bật website.

---

### Việc 0b — Đưa thay đổi của Claude lên mạng (làm thường xuyên)

Mỗi lần Claude sửa gì đó trong thư mục dự án, bạn làm ba bước này:

1. Mở **GitHub Desktop**
2. Cột trái hiện danh sách file đã đổi. **Bấm vào từng file để xem.**
   - Chữ **nền xanh lá** = phần được thêm vào
   - Chữ **nền đỏ** = phần bị bỏ đi
   - Đây là lúc bạn kiểm tra. Không ưng chỗ nào thì chưa bấm gì cả — nhắn Claude sửa lại.
3. Ưng rồi thì:
   - Ô dưới bên trái, gõ vài chữ mô tả (ví dụ: *"bài mới về tuổi teen"*)
   - Bấm nút xanh **`Commit to main`**
   - Bấm tiếp nút **`Push origin`** ở thanh trên

⏱ Khoảng 2 phút sau website tự cập nhật.

> **Muốn huỷ hết thay đổi của Claude?** Bấm chuột phải vào file → **`Discard changes`**. File quay về như cũ. Không mất gì.

---

### Việc 1 — Xem website đang có những bài gì

1. Trong repo, bấm vào thư mục **`src`**
2. Bấm tiếp **`content`** → **`articles`**
3. Mỗi file trong đó là một bài viết

**Xong.** Không sửa gì thì không hỏng gì — cứ yên tâm bấm vào xem.

---

### Việc 2 — Sửa chữ trong một bài đã đăng

1. Vào `src` → `content` → `articles`, bấm vào bài cần sửa
2. Bấm biểu tượng **cây bút chì ✏️** ở góc trên bên phải
3. Sửa chữ như gõ trong Notepad
4. Kéo xuống cuối, bấm nút xanh **`Commit changes`**
5. Hộp thoại hiện ra → bấm tiếp nút xanh **`Commit changes`**

⏱ Khoảng 2 phút sau website tự cập nhật.

> ⚠️ **Đừng đụng vào phần nằm giữa hai dòng `---` ở đầu file** trừ khi bạn biết mình đang làm gì. Đó là phần khai báo kỹ thuật (xem Phần D: *frontmatter*). Sửa phần chữ bên dưới thì luôn an toàn.

---

### Việc 3 — Gỡ một bài xuống ngay lập tức

Dùng khi bạn nhận ra bài có chỗ sai và muốn ẩn đi trong lúc chưa kịp sửa.

1. Mở bài đó, bấm **cây bút chì ✏️**
2. Tìm dòng: `draft: false`
3. Sửa thành: `draft: true`
4. Bấm **`Commit changes`** hai lần

⏱ 2 phút sau bài biến mất khỏi website. **Nội dung vẫn còn nguyên** — đổi lại thành `false` là bài quay về.

> **Đừng xoá file.** Đổi `draft` là đủ, và giữ được toàn bộ nội dung.

---

### Việc 4 — Đưa một bài lên khối "Bài viết nổi bật" ở trang chủ

1. Mở bài đó, bấm **cây bút chì ✏️**
2. Tìm dòng `featured: false` → sửa thành `featured: true`
3. Bấm **`Commit changes`** hai lần

---

### Việc 5 — Xem website có đang bị lỗi không

1. Trong repo, bấm tab **`Actions`** ở thanh trên cùng
2. Nhìn dòng trên cùng của danh sách:

| Dấu hiệu | Nghĩa là |
| --- | --- |
| ✅ **Dấu tích xanh** | Mọi thứ bình thường, website đã cập nhật |
| 🟡 **Chấm vàng đang quay** | Đang xử lý, chờ 1–2 phút |
| ❌ **Dấu X đỏ** | Có lỗi — website **vẫn giữ bản cũ**, không bị hỏng |

> Gặp dấu X đỏ đừng lo. Website cũ vẫn chạy bình thường. Chỉ cần nhắn Claude: *"Actions đang báo đỏ, xem giúp tôi."*

---

### Việc 6 — Bật GitHub Pages (làm một lần duy nhất)

Đây là việc số 3 trong danh sách chờ ở Phần A.

1. Trong repo, bấm **`Settings`** (bánh răng, ở thanh trên cùng bên phải)
2. Cột bên trái, kéo xuống tìm mục **`Pages`**, bấm vào
3. Nhìn phần **`Build and deployment`**
4. Ở ô **`Source`**, đang là "Deploy from a branch" → bấm vào và **chọn `GitHub Actions`**
5. Xong, không cần bấm Save — nó tự lưu

⏱ Vài phút sau, ngay tại trang đó sẽ hiện địa chỉ website của bạn.

> Đây là bước hay bị quên nhất. Không làm bước này thì Actions vẫn báo xanh nhưng vào link sẽ hiện "404 — không tìm thấy trang".

---

### Việc 7 — Xem website và lấy link gửi phụ huynh

#### Link trang chủ — dùng để giới thiệu chung

```
https://lucero6886.github.io/dong-hanh-cung-con/
```

Đây là link chính. Gửi link này khi muốn giới thiệu cả thư viện.

> 💡 **Lưu vào Bookmark.** Mở link, bấm dấu ⭐ trên thanh địa chỉ trình duyệt. Lần sau không phải nhớ.

#### Link một bài cụ thể — dùng khi muốn gửi đúng một bài

Cách chắc chắn nhất, không cần nhớ gì:

1. Mở trang chủ
2. Bấm vào bài muốn gửi
3. **Copy nguyên dòng địa chỉ trên đầu trình duyệt** (bôi đen → Ctrl+C)

Ví dụ ba bài hiện có:

| Bài | Link |
| --- | --- |
| Từ phần thưởng đến động lực bên trong | `.../articles/tu-phan-thuong-den-dong-luc-ben-trong/` |
| Hỏi con học được gì, thay vì hỏi con được mấy điểm | `.../articles/hoi-con-hoc-duoc-gi-thay-vi-hoi-may-diem/` |
| Cấu trúc thay vì nhắc nhở | `.../articles/cau-truc-thay-vi-nhac-nho/` |

*(`...` là phần `https://lucero6886.github.io/dong-hanh-cung-con`)*

Trong mỗi bài còn có sẵn mục **"Chia sẻ"** ở cuối, kèm nút **`Sao chép liên kết`** — bấm một cái là link nằm sẵn trong bộ nhớ tạm, dán thẳng vào Zalo được.

#### Khi dán vào Zalo / Facebook / Messenger

Link sẽ **tự nở ra thành một thẻ xem trước** có tiêu đề, mô tả và ảnh — thay vì một dòng chữ dài loằng ngoằng. Website đã được chuẩn bị sẵn cho việc này.

> ⏳ **Zalo và Facebook lưu đệm rất lâu.** Nếu bạn dán thử link *trước khi* website chạy xong, chúng sẽ nhớ luôn cái lỗi 404 đó và hiện sai trong nhiều giờ. **Chỉ dán thử sau khi mở link thấy website hiện ra bình thường.** Lỡ rồi thì nhắn Claude, có cách xoá bộ nhớ đệm.

#### Nên kiểm tra trước khi gửi cho phụ huynh

- [ ] Mở link trên **điện thoại** — phần lớn phụ huynh đọc bằng điện thoại
- [ ] Bấm thử 2–3 liên kết trong bài xem có mở được không
- [ ] Dán link vào Zalo của chính mình trước, xem thẻ xem trước hiện đúng chưa
- [ ] Đọc lướt lại bài một lần cuối bằng con mắt phụ huynh

#### Muốn có mã QR để in ra?

Nhắn Claude: *"Tạo mã QR cho link website để tôi in ra."* Tiện khi họp phụ huynh hoặc dán ở bảng tin lớp.

---

## PHẦN D — Từ điển: 15 từ bạn sẽ gặp

Giải thích bằng ví dụ đời thường, không dùng từ chuyên môn để giải thích từ chuyên môn.

| Từ | Hiểu nôm na là | Ví von |
| --- | --- | --- |
| **Repo** *(repository)* | Thư mục dự án đặt trên mạng | Như một thư mục Google Drive, nhưng nhớ được mọi phiên bản cũ |
| **GitHub** | Nơi lưu repo, miễn phí | Cái "Google Drive" dành cho dự án như thế này |
| **Commit** | Lưu lại kèm ghi chú lý do | Bấm Ctrl+S, nhưng có ghi "vì sao tôi sửa" và lưu vĩnh viễn |
| **Push** | Đẩy bản trên máy lên mạng | Bấm "đồng bộ" để mọi người thấy bản mới |
| **Build** | Máy dựng file bạn viết thành trang web | Nhà in nhận bản thảo rồi in thành tờ báo |
| **Deploy** | Đưa bản vừa dựng ra cho mọi người xem | Xe chở báo ra sạp |
| **Actions** | Cái máy tự động chạy build + deploy | Người thợ in tự động, làm việc mỗi khi có bản thảo mới |
| **Frontmatter** | Phần khai báo ở đầu file, giữa hai dòng `---` | Tờ khai dán ngoài bì thư: gửi ai, ngày nào, thuộc loại gì |
| **Markdown** *(.md)* | Cách viết chữ có định dạng bằng ký hiệu đơn giản | `**đậm**` cho ra **đậm**. Như gõ tin nhắn Zalo có `*chữ*` |
| **Draft** | Bản nháp | `draft: true` = để trong ngăn kéo. `draft: false` = dán lên bảng tin |
| **Slug** | Phần đuôi trong địa chỉ bài viết | Tên file `tu-giac.md` → địa chỉ `.../articles/tu-giac/` |
| **Category** | Chủ đề của bài | Như kệ sách trong thư viện. Một bài nằm trên **một** kệ |
| **Tag** | Thẻ dán thêm để dễ tìm | Giấy nhớ dán lên gáy sách. Một bài dán được **nhiều** thẻ |
| **RSS** | Kênh để người đọc theo dõi bài mới | Như "đăng ký nhận báo", tự động có bài mới |
| **Sitemap** | Bản đồ website gửi cho Google | Mục lục đưa cho thủ thư để họ xếp sách đúng chỗ |

### Ba từ dễ nhầm nhất

**Build vs Deploy.** Build là *in báo*, deploy là *chở ra sạp*. Build hỏng thì không có gì ra sạp — nên báo cũ vẫn nằm đó, không ai đọc phải bản hỏng.

**Draft vs Xoá.** Draft là *cất vào ngăn kéo* — lấy ra lúc nào cũng được. Xoá là *đốt đi*. Luôn dùng draft.

**Category vs Tag.** Một bài chỉ nằm trên **một** kệ (category), nhưng dán được **nhiều** giấy nhớ (tag).

---

## PHẦN E — Mười tình huống thường gặp

### 1. "Tôi muốn đăng một bài mới"

Nhắn Claude câu mẫu ở **Phần B**. Hoặc tự làm trên GitHub — nhưng lần đầu nên để Claude làm và đọc lại phần Claude ghi trong sổ, sẽ nhanh hiểu hơn.

### 2. "Tôi phát hiện bài có chỗ sai chính tả"

→ **Phần C, việc 2.** Tự sửa mất 1 phút, không cần Claude.

### 3. "Tôi lỡ đăng nhầm, muốn gỡ ngay"

→ **Phần C, việc 3.** Đổi `draft: false` thành `draft: true`.

### 4. "Website hiện chữ trơ trọi, mất hết màu và bố cục"

Đây là lỗi cấu hình địa chỉ, gần như luôn là do bước 2 trong danh sách chờ chưa làm.
→ Nhắn Claude: *"Website mất hết định dạng, tài khoản GitHub của tôi là ABC, sửa giúp tôi."*

### 5. "Actions báo dấu X đỏ"

Website cũ **vẫn đang chạy bình thường**, không ai thấy lỗi.
→ Nhắn Claude: *"Actions đang báo đỏ, xem giúp tôi."*

### 6. "Vào link website thì hiện 404"

→ Chưa bật GitHub Pages. **Phần C, việc 6.**

### 7. "Bài tôi vừa đăng không thấy đâu cả"

Kiểm tra theo thứ tự:
1. Chờ đủ 2 phút chưa?
2. Tab **Actions** đã hiện dấu tích xanh chưa?
3. Trong bài, dòng `draft:` đang là `false` chứ?
4. Vẫn không thấy → nhắn Claude.

### 8. "Tôi muốn đổi tên website / tên tác giả"

→ Nhắn Claude câu mẫu ở **Phần B**. Toàn bộ website đổi theo, vì mọi thứ đều lấy từ **một** file cấu hình duy nhất.

### 9. "Tôi lỡ sửa hỏng gì đó và không biết cách quay lại"

**Không có gì mất được.** GitHub lưu mọi phiên bản.
→ Nhắn Claude: *"Tôi lỡ sửa hỏng, quay lại bản trước giúp tôi."*

### 10. "Tôi quên hết rồi, phải bắt đầu từ đâu?"

→ Mở đúng file này, đọc **Phần A**. Nó luôn cho biết dự án đang ở đâu và việc gì đang chờ bạn.

---

## PHẦN F — Nhật ký thay đổi

> Claude ghi vào đây sau **mỗi** lần chạm vào dự án. Bạn chỉ đọc.
> Mục mới nhất nằm trên cùng.

---

### 11/08/2026 — Sửa lỗi khiến website không tự cập nhật + điền địa chỉ thật

**Người thực hiện:** Claude · **Loại:** Sửa lỗi *(lỗi do Claude gây ra)*

**Bối cảnh**

Bạn đã đẩy dự án lên GitHub thành công, nhưng website vào link vẫn báo 404. Claude kiểm tra và tìm ra hai nguyên nhân — **một trong hai là lỗi của Claude.**

**Nguyên nhân 1 — Lỗi của Claude: đặt sai tên nhánh cần theo dõi**

Cái máy tự động của GitHub được cài để "hễ có thay đổi ở nhánh tên **`main`** thì dựng lại website". Nhưng GitHub Desktop tạo nhánh tên **`master`**.

Kết quả: bạn đẩy code lên, nhưng máy đứng chờ ở một nhánh khác. **Nó chưa hề chạy lần nào.**

Claude đã ghi trong tài liệu là phải đổi tên nhánh thành `main`, nhưng đó là một câu lệnh gõ tay — mà bạn thì dùng GitHub Desktop, hoàn toàn hợp lý. **Đáng ra Claude phải lường trước điều này ngay từ đầu.**

Cách sửa: cài cho máy nghe **cả hai** tên nhánh, `main` lẫn `master`. Từ giờ dùng cách nào cũng chạy.

**Nguyên nhân 2 — Chưa có địa chỉ thật**

Cấu hình vẫn ghi `your-username` vì trước đó Claude chưa biết tài khoản GitHub của bạn. Claude đã tự tìm ra (`Lucero6886`) từ chính thư mục dự án trên máy bạn, thay vì bắt bạn đi tìm.

Đã điền vào. Toàn bộ địa chỉ trong website — thẻ xem trước khi chia sẻ Zalo/Facebook, bản đồ gửi Google, kênh RSS — giờ trỏ đúng.

**Ảnh hưởng tới bạn**

Cần bạn làm 2 việc ở **Phần A** (bật GitHub Pages, rồi đẩy bản sửa này lên). Sau đó website chạy.

Địa chỉ website của bạn: **https://lucero6886.github.io/dong-hanh-cung-con/**

**Nếu bạn muốn tự làm phần này**

Xem hai file đã sửa trong GitHub Desktop trước khi bấm duyệt — đây đúng là lúc bước xem trước phát huy tác dụng.

Cách tự kiểm tra máy tự động có chạy không, không cần Claude:
<https://github.com/Lucero6886/dong-hanh-cung-con/actions> — xem **Phần C, việc 5**.

**Có gì cần bạn quyết không?**

Không. Chỉ cần làm 2 việc ở Phần A.

**Vì sao ghi rõ lỗi của Claude vào đây**

Vì sổ tay này chỉ có giá trị nếu nó trung thực. Bạn cần biết chỗ nào Claude làm hụt, để lần sau gặp hiện tượng tương tự — *"đẩy code lên rồi mà website không đổi gì"* — bạn nhận ra ngay và biết đường hỏi.

---

### 11/08/2026 — Chọn GitHub Desktop làm "nút bấm" đưa bài lên mạng

**Người thực hiện:** Claude · **Loại:** Quyết định về quy trình

**Đã làm gì**

Bổ sung **việc 0** và **việc 0b** vào Phần C: cài và dùng GitHub Desktop.

**Vì sao**

Khi Claude ghi file vào thư mục trên máy bạn, các file đó mới chỉ nằm trên máy — chưa lên mạng. Cần một cách đưa chúng lên, mà không bắt bạn gõ lệnh.

Đã cân nhắc hai cách:

| Cách | Vì sao chọn / không chọn |
| --- | --- |
| Claude tự đẩy lên mạng | ❌ Cần bạn tạo một "chìa khoá" (mật khẩu kỹ thuật) rồi dán cho Claude mỗi phiên. Rườm rà, và dán mật khẩu vào khung chat là thói quen không nên có. |
| **GitHub Desktop** | ✅ Miễn phí, chính chủ GitHub, không gõ lệnh, đăng nhập một lần. **Và quan trọng nhất: nó cho bạn xem trước từng chữ Claude đã đổi, trước khi bấm đồng ý.** |

**Ảnh hưởng tới bạn**

Điều này biến mối lo của bạn thành một tính năng. Thay vì Claude âm thầm làm rồi bạn phải tin, quy trình giờ là: **Claude đề xuất → bạn xem → bạn duyệt.** Không có gì lên mạng mà bạn chưa nhìn qua.

Thêm một việc phải cài (mất 5 phút, một lần), đổi lại bạn giữ được quyền phủ quyết ở mọi thay đổi.

**Nếu bạn muốn tự làm phần này**

Đây vốn dĩ là phần của bạn — **Phần C, việc 0 và 0b**. Claude không làm hộ được, và cũng không nên làm hộ.

**Có gì cần bạn quyết không?**

Có: cài GitHub Desktop (việc số 3 trong danh sách chờ ở Phần A).

Nếu bạn thấy cách này vẫn phiền, có một lựa chọn khác: tải file lên thẳng trên web GitHub bằng cách kéo thả. Nhắn Claude *"hướng dẫn tôi cách kéo thả file lên GitHub"* là được — nhưng cách đó bạn sẽ không xem trước được thay đổi.

---

### 11/08/2026 — Dựng toàn bộ website (v1.0.0)

**Người thực hiện:** Claude · **Loại:** Khởi tạo dự án

**Đã làm gì**

Dựng hoàn chỉnh website từ con số không: bộ khung, giao diện, hệ thống chủ đề và thẻ, tìm kiếm, và 3 bài viết đầu tiên. Website chạy được, kiểm tra không có lỗi.

**Vì sao làm như vậy**

Chọn kiểu website "tĩnh" — tức là mọi trang được dựng sẵn thành file, không có máy chủ chạy phía sau. Lý do: không tốn tiền duy trì, không thể bị sập vì quá tải, không cần bảo mật phức tạp, và quan trọng nhất — bài viết của bạn nằm trong các file văn bản đơn giản, mở bằng Notepad cũng đọc được sau 10 năm nữa.

**Ảnh hưởng tới bạn**

- Bạn có 3 bài viết thật, trong đó bài chính giữ nguyên luận điểm từ file Word của bạn.
- Website chưa lên mạng — cần bạn làm 3 việc ở **Phần A**.
- Từ giờ, thêm một bài là 22 thứ khác tự cập nhật theo (trang chủ, chủ đề, thẻ, tìm kiếm, RSS...). Bạn không phải sửa gì thêm.

**Nếu bạn muốn tự làm phần này**

Bạn không cần tự dựng lại. Nhưng phần bạn *nên* tự làm được là **thêm và sửa bài** — xem **Phần C, việc 1–4**.

**Có gì cần bạn quyết không?**

Có — 3 việc ở **Phần A**. Website chưa lên mạng được nếu thiếu.

---

### 11/08/2026 — Kiểm chứng lại nguồn khoa học trong bài chính

**Người thực hiện:** Claude · **Loại:** Kiểm chứng nội dung

**Đã làm gì**

Bài *"Từ phần thưởng đến động lực bên trong"* có nhắc tới nghiên cứu tâm lý học. Thay vì viết theo trí nhớ, Claude đã tra cứu thật trên mạng để xác minh.

**Kết quả**

Hai nghiên cứu được nhắc tới là **có thật** và đã ghi nguồn đầy đủ ở cuối bài. Nhưng tra kỹ thì phát hiện thêm một điều quan trọng: **vấn đề này vẫn đang còn tranh luận** trong giới nghiên cứu — có nhóm tác giả khác đưa ra kết luận gần như ngược lại.

**Ảnh hưởng tới bạn**

Bài viết đã được viết lại phần đó để nêu **cả hai phía**, thay vì trình bày như thể đã có kết luận cuối cùng. Điều này bảo vệ uy tín của bạn: một bài thừa nhận "chỗ này chưa ngã ngũ" đáng tin hơn một bài nói chắc như đinh đóng cột.

Ngoài ra, chi tiết tìm được còn **củng cố chính luận điểm gốc của bạn**: nghiên cứu cho thấy phần thưởng *bất ngờ, không gắn với nhiệm vụ* thì hầu như không gây tác động tiêu cực — đúng bằng sự khác biệt giữa *"học xong thì mẹ mua đồ chơi"* và *"cuối tuần cả nhà đi chơi"* mà bạn đã viết trong ghi chép.

**Nếu bạn muốn tự làm phần này**

Bạn tự kiểm tra được: mở bài viết, kéo xuống cuối phần **"Nguồn tham khảo"**, bấm vào từng đường link. Link nào không mở được thì báo Claude. **Đây là việc bạn nên tự làm với mọi bài có trích nghiên cứu** — xem thêm **Phần G**.

---

### 11/08/2026 — Sửa một lỗi phát hiện khi kiểm thử

**Người thực hiện:** Claude · **Loại:** Sửa lỗi

**Đã làm gì**

Khi thử tắt JavaScript trong trình duyệt (một số người đọc dùng máy cũ hoặc mạng yếu), phát hiện hai nút bấm — nút chuyển nền sáng/tối và nút sao chép liên kết — **vẫn hiện ra nhưng bấm không có tác dụng gì**.

**Vì sao**

Một quy tắc định dạng của Claude đã vô tình đè lên lệnh "ẩn nút này đi". Đã sửa và kiểm tra lại cả hai trường hợp: bật và tắt JavaScript.

**Ảnh hưởng tới bạn**

Người đọc không gặp cảnh bấm một cái nút chết. Bạn không phải làm gì.

**Vì sao ghi lại chuyện nhỏ này vào sổ**

Để bạn thấy rõ: **cái gì cũng được kiểm tra bằng thử nghiệm thật, không phải nói suông.** Khi Claude nói "website chạy tốt", đó là kết quả chạy thử — nếu có lỗi thì lỗi được ghi lại ở đây, kể cả lỗi do chính Claude gây ra.

---

### Mẫu cho các mục sau

```markdown
### ngày/tháng/năm — Tên việc

**Người thực hiện:** Claude / Bạn · **Loại:** Bài mới / Sửa bài / Sửa lỗi / Đổi cấu hình

**Đã làm gì**
…

**Vì sao**
…

**Ảnh hưởng tới bạn**
…

**Nếu bạn muốn tự làm phần này**
…

**Có gì cần bạn quyết không?**
…
```

---

## PHẦN G — Bốn cách tự kiểm tra Claude làm đúng

Bạn không cần biết code để kiểm chứng. Bốn cách dưới đây ai cũng làm được.

### 1. Mở từng đường link nguồn

Bài nào có mục **"Nguồn tham khảo"** ở cuối, hãy bấm thử từng link.

- Link mở ra đúng bài nghiên cứu → tốt
- Link chết, hoặc mở ra thứ chẳng liên quan → **báo Claude ngay**

> Đây là cách kiểm tra quan trọng nhất, và cũng là chỗ dễ mất uy tín nhất nếu sai.

### 2. Đọc mục "Ghi chú biên tập" ở cuối bài

Mỗi bài đều có một dòng in nhỏ ở cuối, nói rõ bài này từ đâu ra: biên tập từ ghi chép gốc của bạn, hay do Claude viết mở rộng.

Đọc dòng đó và tự hỏi: **có đúng như vậy không?** Nếu Claude ghi "biên tập từ ghi chép gốc" mà bạn đọc thấy toàn ý lạ, thì có vấn đề.

### 3. Đọc bài như một người đọc bình thường

Không cần soi kỹ thuật. Chỉ cần tự hỏi:

- Đây có còn là điều **tôi** muốn nói không?
- Có câu nào làm cha mẹ khác cảm thấy bị phán xét không?
- Có chỗ nào nói chắc quá so với những gì thực sự biết không?
- Có chỗ nào nghe như đang chẩn đoán bệnh cho một đứa trẻ không?

Thấy gợn ở đâu thì nói, kể cả khi không giải thích được vì sao. Trực giác của bạn về giọng văn đáng tin hơn Claude.

### 4. Nhìn tab Actions

→ **Phần C, việc 5.** Dấu tích xanh = mọi thứ đã lên mạng thật, không chỉ là lời nói.

---

## Một điều cuối

Bạn không cần hiểu website được dựng thế nào, cũng như không cần biết máy in hoạt động ra sao để làm một tờ báo hay.

Thứ **bắt buộc** phải nắm chỉ có ba:

1. **Dự án đang ở đâu** → Phần A
2. **Tự thêm, sửa, gỡ bài được** → Phần C
3. **Tự kiểm tra được Claude làm đúng** → Phần G

Ba thứ đó là quyền kiểm soát. Còn lại là chi tiết kỹ thuật — cần thì tra sổ, không cần nhớ.

Và nếu có lúc nào đọc một mục trong Phần F mà không hiểu, cứ nhắn:

> *"Mục ngày (…) trong sổ tay, giải thích lại cho tôi bằng lời dễ hiểu hơn."*

Sổ tay này viết chưa đủ rõ thì đó là lỗi của sổ tay, không phải của bạn.

---

<small>

**Các tài liệu khác trong dự án** — bạn *không cần* đọc để vận hành, chỉ tra khi tò mò:

| File | Nội dung | Dành cho |
| --- | --- | --- |
| `implementation-notes.md` | **Chính là file này** | ⭐ Bạn — dùng hằng ngày |
| `dong-hanh-guide.md` | Giải thích sâu về kiến trúc hệ thống | Bạn khi muốn hiểu sâu, hoặc thợ web sau này |
| `docs/CONTENT_GUIDE.md` | Hướng dẫn viết bài đầy đủ | Khi bạn muốn tự viết bài không cần Claude |
| `docs/DEPLOYMENT.md` | Đăng website, tên miền riêng | Khi mua tên miền riêng |
| `docs/AI_CONTENT_WORKFLOW.md` | Quy trình biến ghi chép thành bài | Khi muốn nhờ một trợ lý AI khác |
| `README.md` | Tổng quan kỹ thuật | Thợ web, nếu sau này bạn thuê người |
| `CLAUDE.md` | Quy tắc Claude phải theo | Máy đọc, bạn không cần đọc |

Bản `.md` là bản gốc để sửa. Bản `.html` là để đọc cho dễ.

</small>
