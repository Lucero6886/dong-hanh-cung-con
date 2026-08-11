# Hướng dẫn viết bài

Tài liệu này viết cho **người không làm về web**. Bạn không cần biết lập trình để dùng nó.

---

## Mục lục

1. [Ba việc bạn cần nhớ](#1-ba-việc-bạn-cần-nhớ)
2. [Tạo một bài viết](#2-tạo-một-bài-viết)
3. [Frontmatter — bảng tra từng trường](#3-frontmatter--bảng-tra-từng-trường)
4. [Chủ đề hoạt động thế nào](#4-chủ-đề-hoạt-động-thế-nào)
5. [Thẻ hoạt động thế nào](#5-thẻ-hoạt-động-thế-nào)
6. [Viết nội dung bằng Markdown](#6-viết-nội-dung-bằng-markdown)
7. [Chèn ảnh](#7-chèn-ảnh)
8. [Hộp biên tập (Callout)](#8-hộp-biên-tập-callout)
9. [Trích dẫn nguồn](#9-trích-dẫn-nguồn)
10. [Xem thử trên máy](#10-xem-thử-trên-máy)
11. [Bài nháp](#11-bài-nháp)
12. [Bài nổi bật](#12-bài-nổi-bật)
13. [Đăng bài](#13-đăng-bài)
14. [Nguyên tắc biên tập](#14-nguyên-tắc-biên-tập)
15. [Danh sách kiểm tra trước khi đăng](#15-danh-sách-kiểm-tra-trước-khi-đăng)

---

## 1. Ba việc bạn cần nhớ

1. **Mỗi bài viết là một file** trong `src/content/articles/`.
2. **Tên file chính là địa chỉ bài viết trên website.**
3. **Đầu file có một khối cấu hình** gọi là *frontmatter*, nằm giữa hai dòng `---`.

Không có gì khác. Không có trang quản trị, không có mật khẩu, không có nút "Đăng bài".

---

## 2. Tạo một bài viết

```bash
cp templates/article-template.md src/content/articles/ten-bai-viet.md
```

Hoặc tạo tay một file mới trong `src/content/articles/`.

### Đặt tên file

Tên file trở thành địa chỉ:

| Tên file | Địa chỉ trên website |
| --- | --- |
| `cau-truc-thay-vi-nhac-nho.md` | `/articles/cau-truc-thay-vi-nhac-nho/` |
| `khi-con-vao-tuoi-teen.md` | `/articles/khi-con-vao-tuoi-teen/` |

**Quy tắc:**

- Viết **không dấu** (`tu-giac` chứ không phải `tự-giác`)
- Dùng **gạch ngang**, không dùng khoảng trắng hay gạch dưới
- Chỉ chữ thường
- Ngắn gọn nhưng đủ nghĩa

> ⚠️ **Đổi tên file sau khi đã đăng sẽ làm hỏng đường link cũ** mà người khác đã chia sẻ. Hãy cân nhắc kỹ tên file ngay từ đầu.

### Chọn `.md` hay `.mdx`?

| | `.md` | `.mdx` |
| --- | --- | --- |
| Viết chữ, tiêu đề, danh sách, bảng | ✅ | ✅ |
| Dùng hộp `<Callout>` | ❌ | ✅ |

Không cần callout thì dùng `.md` cho đơn giản. Cần callout thì đổi đuôi thành `.mdx` — nội dung không phải sửa gì.

---

## 3. Frontmatter — bảng tra từng trường

Frontmatter là khối nằm **giữa hai dòng `---` ở đầu file**:

```yaml
---
title: "Từ phần thưởng đến động lực bên trong"
description: "Thưởng cho con không sai. Điều đáng quan tâm hơn là thông điệp trẻ hình thành."
date: 2026-08-10
category: "Động lực & thói quen"
tags:
  - động lực
  - trách nhiệm
draft: false
---
```

### Bắt buộc

| Trường | Kiểu | Ghi chú |
| --- | --- | --- |
| `title` | chữ | Tiêu đề bài. Cũng là thẻ `<h1>` và tiêu đề trên Google. Đặt trong dấu ngoặc kép. |
| `description` | chữ | 1–2 câu. Hiện trên thẻ bài viết, trên Google, và khi chia sẻ lên Facebook/Zalo. Nên 120–160 ký tự. |
| `date` | ngày | Định dạng `2026-08-11` (năm-tháng-ngày). **Không** viết `11/08/2026`. |
| `category` | chữ | Tên chủ đề. Xem mục 4. |

### Tuỳ chọn

| Trường | Kiểu | Ghi chú |
| --- | --- | --- |
| `subtitle` | chữ | Tiêu đề phụ, hiện ngay dưới tiêu đề chính. |
| `updated` | ngày | Ngày sửa lần cuối. Có giá trị thì bài hiện thêm "Cập nhật …". |
| `author` | chữ | Bỏ trống thì lấy tác giả mặc định trong `src/config/site.ts`. |
| `tags` | danh sách | Xem mục 5. |
| `ageGroups` | danh sách | Ví dụ `["6–10", "11–14"]`. Hiện trên thẻ bài và đầu bài. |
| `featured` | true/false | `true` → hiện ở khối "Bài viết nổi bật" trang chủ. |
| `draft` | true/false | `true` → bài bị ẩn hoàn toàn. Xem mục 11. |
| `coverImage` | chữ | Ví dụ `"/images/articles/abc.webp"`. Xem mục 7. |
| `coverAlt` | chữ | Mô tả ảnh cho người khiếm thị. Có `coverImage` thì nên có trường này. |
| `readingTime` | số | Ghi đè thời gian đọc. **Bỏ trống thì hệ thống tự tính** — nên bỏ trống. |
| `sourceType` | chữ | `ghi-chep-goc` / `bien-tap-mo-rong` / `tong-hop`. Xem mục 9. |
| `editorNote` | chữ | Ghi chú biên tập, hiện in nhỏ ở cuối bài. |
| `references` | danh sách | Nguồn tham khảo. Xem mục 9. |

> 💡 **Sai frontmatter thì `npm run build` báo lỗi ngay**, kèm tên file và tên trường. Đây là chủ ý — thà lỗi lúc build còn hơn đăng lên rồi mới phát hiện.

---

## 4. Chủ đề hoạt động thế nào

Chủ đề đến **từ chính bài viết**, không phải từ một danh sách cố định.

Bạn viết `category: "Động lực & thói quen"` → website tự tạo trang `/categories/dong-luc-thoi-quen/` và đưa bài vào đó.

**Viết một chủ đề hoàn toàn mới cũng được** — trang chủ đề mới sẽ tự xuất hiện, với đường dẫn tự sinh từ tên (bỏ dấu tiếng Việt).

### Mười chủ đề đã có sẵn mô tả

`Đồng hành cùng con` · `Động lực & thói quen` · `Học tập & tự học` · `Giao tiếp cha mẹ – con` · `Cảm xúc & tâm lý` · `Kỷ luật tích cực` · `Tự lập & trách nhiệm` · `Công nghệ & trẻ em` · `Tuổi teen` · `Góc suy ngẫm của cha mẹ`

Muốn thêm mô tả cho một chủ đề mới, mở `src/config/taxonomy.ts` và thêm vào danh sách `CATEGORIES`. Không thêm cũng không sao — chỉ là trang chủ đề đó chưa có đoạn giới thiệu.

> ⚠️ **Tên chủ đề phải viết giống hệt nhau giữa các bài**, kể cả dấu và khoảng trắng. `"Tuổi teen"` và `"Tuổi Teen"` sẽ bị tính là hai chủ đề khác nhau.

---

## 5. Thẻ hoạt động thế nào

Thẻ là cách tìm ngang qua các chủ đề. Một bài chỉ có **một** chủ đề, nhưng có thể có **nhiều** thẻ.

```yaml
tags:
  - động lực
  - phần thưởng
  - tự giác
```

Website tự tạo `/tags/dong-luc/`, `/tags/phan-thuong/`, `/tags/tu-giac/`.

**Thẻ dùng nhiều trong dự án:**
`động lực` · `phần thưởng` · `tự giác` · `trách nhiệm` · `thói quen` · `học tiếng Anh` · `tuổi teen` · `giao tiếp` · `tự học` · `cảm xúc` · `kỷ luật` · `cha mẹ` · `giáo dục`

**Lời khuyên:** mỗi bài 3–5 thẻ. Ít quá thì khó tìm, nhiều quá thì thẻ mất ý nghĩa. Ưu tiên dùng lại thẻ đã có thay vì đặt thẻ mới gần giống.

---

## 6. Viết nội dung bằng Markdown

Phần dưới dòng `---` thứ hai là nội dung bài.

```markdown
Đoạn mở đầu viết bình thường, không cần ký hiệu gì.

## Tiêu đề mục lớn

Chữ **in đậm** và chữ *in nghiêng*.

### Tiêu đề mục nhỏ

- Gạch đầu dòng
- Gạch đầu dòng nữa

1. Danh sách đánh số
2. Mục thứ hai

> Đoạn trích dẫn, hiện với vạch màu bên trái.

[Chữ hiển thị](https://dia-chi-lien-ket.com)

| Cột A | Cột B |
| --- | --- |
| Ô 1 | Ô 2 |

---
```

**Ba điều cần nhớ:**

1. **Không viết `# Tiêu đề` trong nội dung.** Tiêu đề bài đã lấy từ `title` ở frontmatter rồi. Trong bài chỉ dùng `##` trở xuống.
2. **Mục lục tự sinh từ các `##` và `###`.** Bài có từ 2 mục trở lên thì mục lục tự hiện ở cột bên phải.
3. **Cần một dòng trống** giữa các đoạn văn, trước và sau danh sách, trước và sau bảng.

---

## 7. Chèn ảnh

### Bước 1 — Bỏ ảnh vào đúng chỗ

Đặt file ảnh trong `public/images/articles/`.

Nên dùng định dạng `.webp` (nhẹ hơn `.jpg` khoảng 30%), bề ngang khoảng 1200px, dung lượng dưới 300KB.

### Bước 2 — Ảnh bìa

```yaml
coverImage: "/images/articles/dong-luc-ben-trong.webp"
coverAlt: "Hai mẹ con ngồi cùng bàn học, mẹ đang lắng nghe con nói"
```

Đường dẫn viết **từ gốc `public`**, tức là bỏ chữ `public` đi và bắt đầu bằng `/`.

### Bước 3 — Ảnh trong bài

```markdown
![Mô tả ảnh cho người khiếm thị](/images/articles/ten-anh.webp)
```

> ⚠️ **Luôn viết mô tả ảnh.** Đó là phần trong `[...]`. Người dùng trình đọc màn hình phụ thuộc vào nó. Ảnh chỉ để trang trí thì để trống: `![](...)`.

### Ảnh xem trước khi chia sẻ

Bài có `coverImage` thì ảnh đó được dùng khi chia sẻ lên Facebook, Messenger, Zalo, LinkedIn. Không có thì dùng ảnh mặc định `public/social/og-default.png`.

Muốn tạo ảnh chia sẻ riêng cho một bài:

```bash
npm run og -- --title "Tiêu đề bài viết" --out public/images/articles/ten-bai.png
```

---

## 8. Hộp biên tập (Callout)

**Chỉ dùng được trong file `.mdx`.** Đổi đuôi file từ `.md` sang `.mdx` là dùng được ngay, không cần import gì.

```mdx
<Callout type="tip">

Nội dung gợi ý cho cha mẹ.

</Callout>
```

> ⚠️ **Phải có dòng trống** sau `<Callout ...>` và trước `</Callout>`. Thiếu dòng trống thì chữ in đậm, danh sách… bên trong sẽ không hiển thị đúng.

### Sáu kiểu có sẵn

| `type` | Nhãn hiện ra | Dùng khi nào |
| --- | --- | --- |
| `tip` | Gợi ý cho cha mẹ | Một việc cụ thể có thể làm |
| `warning` | Điều cần lưu ý | Cảnh báo, giới hạn, ngoại lệ |
| `say` | Thử nói với con | Câu nói mẫu cha mẹ dùng được luôn |
| `reflect` | Câu hỏi để suy ngẫm | Danh sách câu hỏi tự vấn |
| `key` | Ý chính | Tóm tắt điều quan trọng nhất |
| `avoid` | Nên hạn chế | Cách làm dễ phản tác dụng |

### Đổi nhãn

```mdx
<Callout type="reflect" title="Tự hỏi mình cuối tuần này">

- Câu hỏi thứ nhất?
- Câu hỏi thứ hai?

</Callout>
```

---

## 9. Trích dẫn nguồn

Đây là phần quan trọng nhất của dự án về mặt uy tín.

### Quy tắc tuyệt đối

> **Không bao giờ bịa nguồn.**
> Không bịa tên nghiên cứu, tên tác giả, con số thống kê, tên sách hay đường link.
> Không kiểm chứng được thì viết rõ là không kiểm chứng được — hoặc bỏ hẳn ý đó ra khỏi bài.

### Ghi nguồn

```yaml
references:
  - label: "Lepper, M. R., Greene, D., & Nisbett, R. E. (1973). Undermining children's intrinsic interest with extrinsic reward. Journal of Personality and Social Psychology, 28(1), 129–137."
    url: "https://doi.org/10.1037/h0035519"
    note: "Nghiên cứu kinh điển về hiệu ứng biện minh thừa."
```

`url` và `note` là tuỳ chọn. Nguồn có DOI thì nên dùng link `https://doi.org/...` vì nó bền hơn link tạp chí.

### Ghi rõ bài này từ đâu ra

```yaml
sourceType: "ghi-chep-goc"
```

| Giá trị | Nghĩa là |
| --- | --- |
| `ghi-chep-goc` | Biên tập từ ghi chép, trao đổi, bài nói của chính bạn |
| `bien-tap-mo-rong` | Bạn viết mới, mở rộng từ nguyên tắc giáo dục |
| `tong-hop` | Tổng hợp có dẫn nguồn bên ngoài |

Website tự hiện một dòng ghi chú tương ứng ở cuối bài. Muốn viết ghi chú riêng thì dùng `editorNote`.

### Bốn loại nội dung cần phân biệt trong bài

Khi viết, hãy tự hỏi mỗi đoạn thuộc loại nào — và viết sao cho người đọc cũng phân biệt được:

1. **Nguyên tắc giáo dục** — cách hiểu tương đối ổn định.
2. **Quan sát cá nhân** — trải nghiệm của bạn. Hãy nói rõ đây là quan sát cá nhân.
3. **Kết quả nghiên cứu** — chỉ nêu khi có nguồn ở `references`, và nêu cả mức độ chắc chắn.
4. **Gợi ý thực hành** — điều có thể thử, kèm lưu ý mỗi đứa trẻ một khác.

---

## 10. Xem thử trên máy

```bash
npm run dev
```

Mở địa chỉ hiện trong terminal. Sửa file rồi lưu → trình duyệt tự tải lại.

Ở chế độ này, bài `draft: true` **vẫn hiện** để bạn xem thử.

Muốn xem đúng như bản thật (bài nháp bị ẩn):

```bash
npm run build
npm run preview
```

---

## 11. Bài nháp

```yaml
draft: true
```

Bài nháp:

- **Hiện** khi chạy `npm run dev` trên máy bạn
- **Bị ẩn hoàn toàn** khi build thật: không có trang riêng, không lên trang chủ, không vào RSS, không vào sitemap, không vào tìm kiếm

Nghĩa là bạn có thể yên tâm commit và push bài nháp lên GitHub — không ai thấy cho tới khi bạn đổi thành `draft: false`.

---

## 12. Bài nổi bật

```yaml
featured: true
```

Bài hiện ở khối "Bài viết nổi bật" trên trang chủ. Mặc định trang chủ lấy 3 bài; đổi số này trong `src/config/site.ts` (`SITE.featuredLimit`).

Nếu số bài đánh dấu nổi bật ít hơn 3, hệ thống tự lấy thêm bài mới nhất cho đủ — nên khối này không bao giờ bị trống.

---

## 13. Đăng bài

```bash
git add .
git commit -m "Bài mới: Tên bài viết"
git push
```

Xong. GitHub tự build và đăng trong khoảng 1–2 phút.

**Bạn KHÔNG cần** sửa trang chủ, sửa trang chủ đề, sửa RSS, sửa sitemap hay sửa danh sách bài. Tất cả tự cập nhật.

Muốn kiểm tra: vào repo trên GitHub → tab **Actions** → chờ dấu ✓ xanh.

---

## 14. Nguyên tắc biên tập

Giọng văn của dự án: **điềm đạm, ấm áp, tôn trọng, thực tế, trung thực về mức độ chắc chắn.**

### Nên

- "Cha mẹ **có thể cân nhắc**…"
- "Một cách tiếp cận **có thể hữu ích** là…"
- "**Trong nhiều trường hợp**…"
- "**Điều quan trọng cần phân biệt** là…"
- "Điều này **còn tuỳ vào** từng đứa trẻ."

### Tránh

- "Cha mẹ **phải**…" (trừ khi thật sự có cơ sở)
- Tiêu đề giật gân, gây sợ hãi
- Làm người đọc thấy có lỗi
- Khẳng định như thể có một công thức đúng duy nhất
- Nhiều emoji
- Câu khẩu hiệu sáo rỗng
- **Chẩn đoán trẻ** — website này không làm việc đó, trong bất kỳ trường hợp nào

### Người đọc nên cảm thấy gì sau khi đọc

> "Mình hiểu vấn đề rõ hơn."
> "Mình có một điều cụ thể để thử."
> "Mình không bị phán xét."
> "Mình muốn nghĩ sâu hơn về cách mình đang đồng hành với con."

---

## 15. Danh sách kiểm tra trước khi đăng

- [ ] Tên file không dấu, dùng gạch ngang
- [ ] `title` và `description` đã viết xong (mô tả 120–160 ký tự)
- [ ] `date` đúng định dạng `2026-08-11`
- [ ] `category` viết giống hệt các bài cùng chủ đề
- [ ] Có 3–5 `tags`
- [ ] `draft` đã đổi thành `false`
- [ ] Trong bài không có `#` (chỉ dùng `##` trở xuống)
- [ ] Ảnh nằm trong `public/images/articles/` và có mô tả ảnh
- [ ] Mọi con số, nghiên cứu, trích dẫn đều **kiểm chứng được** và có trong `references`
- [ ] Không có câu nào mang tính chẩn đoán trẻ
- [ ] Đã chạy `npm run build` và không có lỗi
- [ ] Đã xem thử bài trên màn hình hẹp (thu nhỏ cửa sổ trình duyệt)
