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

Tự kiểm tra:

```bash
npm run build                                          # phải không lỗi
npm run check                                          # phải 0 errors, 0 warnings
grep -rn "Mr. Lucero" src/ --include=*.astro           # phải rỗng
grep -rn 'href="/' src/ --include=*.astro              # chỉ được có link ngoài
```

---

## Việc đang chờ chủ dự án

Kiểm tra Phần A của `implementation-notes.md` mỗi đầu phiên. Tính đến 11/08/2026 còn 4 việc chưa xong:

1. Có tài khoản GitHub
2. **Cho biết tên tài khoản GitHub** → khi biết, sửa `DEPLOY.siteUrl` trong `src/config/site.ts` (đang là `your-username`) rồi cập nhật sổ tay
3. Cài GitHub Desktop *(chỉ chủ dự án làm được)*
4. Bật GitHub Pages: Settings → Pages → Source → GitHub Actions *(chỉ chủ dự án làm được)*

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
| Mô tả chủ đề, hành trình | `src/config/taxonomy.ts` |
| Trường frontmatter hợp lệ | `src/content.config.ts` |
| Truy vấn bài viết | `src/utils/articles.ts` — đừng gọi `getCollection()` trực tiếp trong trang |
| Màu sắc, cỡ chữ | `src/styles/global.css` khối `:root` |
| Quy trình đăng | `.github/workflows/deploy.yml` |
