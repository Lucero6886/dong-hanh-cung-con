# Hướng dẫn cho Claude khi làm việc trên dự án này

> File này được Claude đọc tự động ở mọi phiên làm việc. Chủ dự án không cần đọc.

## Bối cảnh quan trọng nhất

Chủ dự án là **Lê Văn Thuấn**, một người **không biết lập trình và không làm về công nghệ thông tin**. Anh ấy đã nói rõ mối lo: *nhờ Claude làm hết thì sẽ không hiểu và không nắm được dự án của mình.*

Vì vậy mục tiêu của Claude ở đây **không chỉ là hoàn thành việc**, mà là hoàn thành việc **theo cách giữ cho chủ dự án luôn nắm được quyền kiểm soát**.

Mọi quyết định về cách trả lời, cách giải thích, cách ghi chép đều phải phục vụ mục tiêu đó.

---

## SÁU QUY TẮC BẮT BUỘC

### 1. Cập nhật sổ tay sau MỌI thay đổi

Sau bất kỳ thay đổi nào lên dự án (thêm/sửa/gỡ bài, sửa cấu hình, sửa lỗi, nâng cấp), **bắt buộc** thêm một mục vào **Phần F** của `implementation-notes.md`, theo đúng mẫu có sẵn ở cuối phần đó:

```markdown
### ngày/tháng/năm — Tên việc
**Người thực hiện:** … · **Loại:** …
**Đã làm gì** …
**Vì sao** …
**Ảnh hưởng tới bạn** …
**Nếu bạn muốn tự làm phần này** …
**Có gì cần bạn quyết không?** …
```

Mục mới nằm **trên cùng** trong Phần F.

Mục **"Nếu bạn muốn tự làm phần này"** là bắt buộc và không được bỏ qua — đây chính là phần chống phụ thuộc. Nếu việc đó chủ dự án tự làm được trên web GitHub, hãy chỉ rõ các bước hoặc trỏ tới đúng mục trong Phần C.

Ghi cả **lỗi do chính Claude gây ra**. Sổ tay phải trung thực, không phải bản báo cáo thành tích.

### 2. Cập nhật lại số liệu ở Phần A

Sau khi thêm/gỡ bài hoặc đổi cấu hình, cập nhật lại bảng trạng thái và các con số ở **Phần A** (số bài, chủ đề, thẻ, số trang, danh sách bài, việc đang chờ). Số liệu phải lấy từ dự án thật, không ước lượng.

### 3. Tạo lại bản HTML sau khi sửa file .md

```bash
pandoc implementation-notes.md \
  --from=markdown+yaml_metadata_block+pipe_tables+task_lists \
  --to=html5 --standalone --toc --toc-depth=2 --wrap=none \
  --template=scripts/notes-template.html \
  --output=implementation-notes.html
```

Không có pandoc thì báo cho chủ dự án, đừng tự viết tay HTML.

Tương tự với `dong-hanh-guide.md` → dùng `scripts/guide-template.html`.

### 4. Không tự ý đăng bài

Luôn hỏi ý trước khi đăng. Cách an toàn: tạo bài với `draft: true`, cho chủ dự án đọc, chỉ đổi thành `false` khi được đồng ý.

### 5. Toàn vẹn nguồn — tuyệt đối

- **Không bịa** tên nghiên cứu, tác giả, năm, số liệu, trích dẫn, đường link.
- Khẳng định khoa học phải **tra cứu thật** bằng web search, không viết theo trí nhớ.
- Tra được thì ghi vào `references` trong frontmatter, có link kiểm chứng được.
- Không tra được thì nói thẳng và đề xuất bỏ ý đó hoặc viết nhẹ đi.
- Vấn đề còn tranh luận trong giới học thuật thì **phải nêu cả phía phản biện**.
- Biên tập từ ghi chép gốc: **giữ nguyên luận điểm**, phần Claude thêm vào phải ghi rõ trong `editorNote`.

### 6. Giải thích bằng tiếng Việt đời thường

- Không dùng từ chuyên môn mà không dịch ngay tại chỗ.
- Ưu tiên ví von đời thường (xem Phần D của sổ tay để dùng lại đúng cách ví von).
- Báo cáo kết quả bằng thứ chủ dự án quan tâm: *"bài đã lên, xem tại đây"* — không phải *"đã commit và push lên origin/main"*.
- Khi phải nhắc tới thao tác kỹ thuật, luôn kèm câu trả lời cho: **"tôi tự làm thì làm thế nào?"**

---

## Quy ước kỹ thuật bắt buộc

Ba quy ước dưới đây, vi phạm là website hỏng. Giải thích đầy đủ ở `dong-hanh-guide.md` Phần 6 và 8.

1. **Mọi liên kết nội bộ đi qua `withBase()`** — viết thẳng `href="/articles/"` sẽ chạy ở máy nhưng hỏng trên GitHub Pages.
2. **Không viết cứng danh tính** (tên tác giả, tên website) vào component — luôn `import { SITE } from '../config/site'`.
3. **Không tạo trang `.astro` riêng cho một bài viết** — bài viết luôn nằm trong `src/content/articles/`.

### Quy ước về hình minh hoạ

- **Không tự chế màu mới.** Ba màu dữ liệu trong `figures_lib.py` (`TEAL` `#1e8163`, `BLUE` `#3f6bbf`, `CLAY` `#b04c26`) đã qua bộ kiểm tra của quy chuẩn trực quan hoá và đạt toàn bộ. Đổi một màu thì **bắt buộc chạy lại bộ kiểm tra**, không được ước lượng bằng mắt.
- **Tối đa 3 màu dữ liệu trên một hình.** Màu thứ 4 (vàng) đã thử và trượt phần mù màu. Cần nhiều hơn → gộp nhóm hoặc tách thành hai hình.
- **Mọi hình tự mang nền sáng.** Đây là chủ ý cho chế độ tối, không phải lỗi — lý do ghi ở đầu `figures_lib.py`. Đừng "sửa" thành nền trong suốt.
- **Sơ đồ phải mang thông tin**, không trang trí. Không dùng ảnh chụp trẻ em lấy trên mạng (bản quyền + quyền hình ảnh của trẻ).
- Bài mới nên có `coverImage` + `coverAlt` trong frontmatter và ít nhất một `<Figure>` trong thân bài. Bài `.md` có `<Figure>` phải đổi đuôi thành `.mdx`.
- ⚠️ **ĐỪNG vẽ lại ảnh bìa nếu máy không có font Inter.** `FONT_PNG` trong `figures_lib.py` là `"Inter Display, Inter, DejaVu Sans, sans-serif"`. Thiếu Inter thì cairosvg **âm thầm** thay bằng DejaVu và cả 22 ảnh bìa đổi khác hẳn. Kiểm trước bằng `fc-list | grep -i inter`; không có thì sau khi chạy script hãy `git checkout -- public/images/articles/*-cover.png` và chỉ giữ các file `.svg`. (Đã xảy ra 17/09/2026.)
- Tiêu đề và dòng nguồn của sơ đồ **không tự ngắt dòng**. `frame()` trong `figures_lib.py` giờ báo lỗi nếu chúng vượt khung — đừng bỏ qua lỗi đó, hãy viết tiêu đề ngắn lại.

### Khi sửa một câu trong bài, đọc lại bốn thứ đi kèm

Đợt sửa lớn 25/08/2026 sửa đúng thân bài nhưng để lại lỗi ở **đúng bốn chỗ** này. Mỗi lần sửa nội dung, kiểm lại:

1. `description` trong frontmatter — hiện khi chia sẻ link, rất dễ thành câu mà thân bài vừa phản bác
2. `subtitle` — hiện ở đầu bài và trong danh sách bài
3. `alt` và `caption` của mọi `<Figure>` trong cùng mục, **và** dữ liệu sơ đồ trong `figures()` của `make-figures.py`
4. `note` của mục nguồn liên quan trong khối `references:`

Tự kiểm tra:

```bash
npm run build                                          # phải không lỗi
npm run check                                          # phải 0 errors, 0 warnings
grep -rn "Mr. Lucero" src/ --include=*.astro           # phải rỗng
grep -rn 'href="/' src/ --include=*.astro              # chỉ được có link ngoài
```

---

## Việc đang chờ chủ dự án

Kiểm tra Phần A của `implementation-notes.md` mỗi đầu phiên.

**Tính đến 23/08/2026: không còn việc thiết lập nào chờ chủ dự án.** Toàn bộ đã xong — tài khoản GitHub `Lucero6886`, `DEPLOY.siteUrl` đã điền `https://lucero6886.github.io`, GitHub Desktop đã cài, GitHub Pages đã bật, website chạy thật từ 11/08/2026.

## Hai tác vụ tự động đang chạy

| Tác vụ | Lịch | Làm gì | Ràng buộc |
| --- | --- | --- | --- |
| Soạn bài nháp | 8h sáng thứ Hai hằng tuần | Viết một bài nháp kèm ảnh bìa + sơ đồ, **chỉ khi** 7 ngày qua chưa có bài mới | `draft: true` bắt buộc · cấm push · cấm chế màu mới |
| Soát nội dung | 9h sáng ngày 1, mỗi 3 tháng (1/10, 1/1, 1/4, 1/7) | Soát 4 mặt: nguồn · chuẩn mực biên tập · tính cập nhật của khuyến cáo y tế · tính nhất quán. Gửi báo cáo kèm câu sửa đề xuất | **Chỉ đọc, không sửa file** · cấm push · cấm bịa · cấm bịa lỗi cho có |

Chi tiết cho chủ dự án: `implementation-notes.md` Phần C, việc 9 và việc 10.

Khi chủ dự án nhắn **"áp dụng bản soát nguồn"** → đọc báo cáo gần nhất, sửa vào file, ghi Phần F, rồi chuyển sang máy anh ấy để tự duyệt bằng GitHub Desktop.

## Cách đưa thay đổi lên mạng

**Claude KHÔNG tự đẩy code lên GitHub.** Quy trình đã thống nhất: Claude ghi file vào thư mục
trên máy chủ dự án, rồi chủ dự án tự xem lại trong GitHub Desktop và bấm duyệt.

Lý do: chủ dự án cần nhìn thấy chính xác Claude đã đổi gì trước khi nội dung lên mạng.
Đây là điều kiện để anh ấy giữ quyền kiểm soát — không được bỏ qua vì lý do tiện lợi.

Sau khi ghi file xong, luôn nhắc: *"Mở GitHub Desktop, xem lại thay đổi, rồi bấm Commit và Push."*

⚠️ Lệnh `git` KHÔNG chạy được trong thư mục kết nối qua device_bash (không xoá được
`.git/index.lock`). Đừng thử commit ở đó — dùng `device_commit_files` hoặc
`unzip -p ... > file` để ghi, và để chủ dự án lo phần git bằng GitHub Desktop.

---

## Giọng viết cho nội dung website

Điềm đạm, ấm áp, tôn trọng cha mẹ, trung thực về mức độ chắc chắn.

| Nên | Tránh |
| --- | --- |
| "Cha mẹ có thể cân nhắc…" | "Cha mẹ phải…" |
| "Trong nhiều trường hợp…" | "Luôn luôn…", "Không bao giờ…" |
| Nêu cả phía phản biện | Trình bày một chiều như đã ngã ngũ |

Tuyệt đối không: chẩn đoán trẻ, dùng nỗi sợ hoặc cảm giác tội lỗi, trình bày suy diễn cá nhân như kết luận khoa học.

Chi tiết: `CONTRIBUTING.md` và `docs/CONTENT_GUIDE.md`.

---

## Bản đồ dự án nhanh

| Cần làm gì | File |
| --- | --- |
| Thêm/sửa bài | `src/content/articles/*.md` hoặc `.mdx` |
| Đổi tên site, tên miền, menu, bản quyền | `src/config/site.ts` ⭐ nguồn duy nhất |
| Thương hiệu ELS (logo, khẩu hiệu, giới thiệu, bật/tắt) | `src/config/site.ts` khối `BRAND` |
| Tạo lại bộ ảnh logo khi chủ dự án đổi logo | `python3 scripts/make-brand-assets.py <file-logo>` → ghi ra `public/brand/` |
| Bảng màu / cỡ chữ / 8 khuôn sơ đồ dùng chung cho mọi hình | `scripts/figures_lib.py` ⭐ nguồn duy nhất — **không tự chạy** |
| Vẽ lại toàn bộ ảnh bìa + sơ đồ | `python3 scripts/make-figures.py` → ghi ra `public/images/articles/` (xoá và tạo lại cả thư mục) |
| Gắn ảnh bìa + `<Figure>` vào bài viết | `python3 scripts/attach-figures.py` — chạy lại nhiều lần vẫn an toàn, tự bỏ qua bài đã gắn |
| Thêm hình cho một bài mới | Thêm mục vào `figures()` trong `make-figures.py` và vào `PLAN` trong `attach-figures.py`, rồi chạy hai lệnh trên |
| Đổi hoạ tiết ảnh bìa của một chủ đề | Bảng `MOTIF` trong `make-figures.py` (8 hoạ tiết ↔ 13 chủ đề) |
| Mô tả chủ đề, hành trình | `src/config/taxonomy.ts` |
| Trường frontmatter hợp lệ | `src/content.config.ts` |
| Thứ tự đọc của một loạt bài trong hành trình | `stageOrder` trong frontmatter (số nhỏ đọc trước; bỏ trống → xếp theo ngày) |
| Truy vấn bài viết | `src/utils/articles.ts` — đừng gọi `getCollection()` trực tiếp trong trang |
| Màu sắc, cỡ chữ | `src/styles/global.css` khối `:root` |
| Quy trình đăng | `.github/workflows/deploy.yml` |
