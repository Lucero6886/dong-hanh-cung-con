---
title: "Đồng hành cùng hệ thống"
subtitle: "Tài liệu giúp bạn hiểu bản chất, nắm được thay đổi, và luôn làm chủ dự án này"
version: "1.0.0"
date: "2026-08-11"
---

# Đồng hành cùng hệ thống

> **Tài liệu này khác với README.**
> README trả lời câu hỏi *"làm thế nào"*. Tài liệu này trả lời câu hỏi *"vì sao"* và *"cái gì đang thực sự diễn ra"*.
>
> Đọc hết mất khoảng 15–20 phút. Sau đó bạn sẽ hiểu hệ thống đủ để tự sửa, tự mở rộng, và tự chẩn đoán khi có gì đó không như ý — mà không cần hỏi ai.

---

## Mục lục

- [Phần 1 — Bản chất hệ thống trong một câu](#phần-1--bản-chất-hệ-thống-trong-một-câu)
- [Phần 2 — Chuyện gì xảy ra khi bạn bấm "push"](#phần-2--chuyện-gì-xảy-ra-khi-bạn-bấm-push)
- [Phần 3 — Bốn tầng của hệ thống](#phần-3--bốn-tầng-của-hệ-thống)
- [Phần 4 — Bản đồ: muốn đổi X thì sửa ở đâu](#phần-4--bản-đồ-muốn-đổi-x-thì-sửa-ở-đâu)
- [Phần 5 — Danh sách những gì TỰ ĐỘNG](#phần-5--danh-sách-những-gì-tự-động)
- [Phần 6 — Vì sao lại làm như vậy: các quyết định kiến trúc](#phần-6--vì-sao-lại-làm-như-vậy-các-quyết-định-kiến-trúc)
- [Phần 7 — Vòng đời một bài viết](#phần-7--vòng-đời-một-bài-viết)
- [Phần 8 — Ba điều dễ làm hỏng hệ thống](#phần-8--ba-điều-dễ-làm-hỏng-hệ-thống)
- [Phần 9 — Tự chẩn đoán khi có sự cố](#phần-9--tự-chẩn-đoán-khi-có-sự-cố)
- [Phần 10 — Kiểm tra sức khoẻ định kỳ](#phần-10--kiểm-tra-sức-khoẻ-định-kỳ)
- [Phần 11 — Nhật ký thay đổi](#phần-11--nhật-ký-thay-đổi)
- [Phần 12 — Những hướng mở rộng đã được tính sẵn](#phần-12--những-hướng-mở-rộng-đã-được-tính-sẵn)

---

## Phần 1 — Bản chất hệ thống trong một câu

> **Website này là một cái máy biến thư mục văn bản thành website, chạy lại mỗi lần bạn đẩy code lên GitHub.**

Đọc lại câu trên một lần nữa, vì mọi thứ còn lại chỉ là chi tiết của nó.

Cụ thể hơn:

- **Đầu vào**: một thư mục chứa các file `.md` / `.mdx` (`src/content/articles/`)
- **Cái máy**: Astro — chạy trên máy GitHub, không chạy trên máy người đọc
- **Đầu ra**: một đống file HTML tĩnh, nằm im trên máy chủ của GitHub
- **Người đọc**: tải file HTML về, đọc. Không có gì "chạy" phía sau cả.

### Vì sao điều này quan trọng

Vì nó quyết định **những gì hệ thống làm được và những gì không**:

| Làm được | Không làm được (theo thiết kế) |
| --- | --- |
| Rất nhanh, không sập, không tốn tiền | Bình luận của người đọc |
| Không cần bảo trì máy chủ | Đăng nhập / tài khoản |
| Nội dung sống lâu hơn giao diện | Nội dung thay đổi theo từng người đọc |
| Sao lưu = copy thư mục | Sửa bài trực tiếp trên web |

Những thứ ở cột phải **không phải là thiếu sót**. Chúng là cái giá phải trả — và đã được trả một cách có chủ ý — để đổi lấy cột trái.

---

## Phần 2 — Chuyện gì xảy ra khi bạn bấm "push"

Đây là chuỗi sự kiện đầy đủ. Hiểu được nó thì mọi lỗi đều tự chẩn đoán được.

```
   MÁY CỦA BẠN
   ┌────────────────────────────────────────────┐
   │ 1. Bạn thêm file bai-viet-moi.md           │
   │ 2. git add . && git commit && git push     │
   └───────────────────┬────────────────────────┘
                       │ (mã nguồn được gửi lên)
                       ▼
   GITHUB
   ┌────────────────────────────────────────────┐
   │ 3. Nhận push vào nhánh main                │
   │ 4. Kích hoạt .github/workflows/deploy.yml  │
   └───────────────────┬────────────────────────┘
                       ▼
   MÁY ẢO CỦA GITHUB (mượn 2 phút, xong là trả)
   ┌────────────────────────────────────────────┐
   │ 5. Tải mã nguồn về                         │
   │ 6. Cài Node.js 22                          │
   │ 7. npm ci        ← cài thư viện            │
   │ 8. npm run build ← ⭐ CÁI MÁY CHẠY Ở ĐÂY   │
   │                                            │
   │    Bên trong bước 8:                       │
   │    · Quét src/content/articles/            │
   │    · Kiểm tra frontmatter từng file        │
   │      → sai là DỪNG, báo lỗi, không đăng    │
   │    · Tính thời gian đọc từng bài           │
   │    · Gom chủ đề, gom thẻ, gom hành trình   │
   │    · Tính bài liên quan cho từng bài       │
   │    · Sinh HTML cho mọi trang               │
   │    · Sinh rss.xml, sitemap, robots.txt     │
   │    · Sinh search-index.json                │
   │    · Nén CSS, băm tên file để cache tốt    │
   │                                            │
   │ 9. Gói thư mục dist/ lại                   │
   └───────────────────┬────────────────────────┘
                       ▼
   GITHUB PAGES
   ┌────────────────────────────────────────────┐
   │ 10. Nhận gói, trải ra máy chủ toàn cầu     │
   │ 11. Website mới hoạt động (~1–2 phút)      │
   └────────────────────────────────────────────┘
```

### Ba điều rút ra từ sơ đồ này

**1. Bước 8 chạy y hệt trên máy bạn và trên GitHub.**
Nên `npm run build` chạy được ở nhà thì trên GitHub cũng chạy được. Nếu Actions đỏ mà máy bạn xanh, gần như chắc chắn là bạn **quên đẩy một file lên** (hay gặp nhất: `package-lock.json`).

**2. Frontmatter sai thì website KHÔNG bị đăng đè.**
Bước 8 dừng lại, bước 10 không xảy ra, bản cũ vẫn nguyên. Đây là một tính năng, không phải lỗi — bạn không bao giờ vô tình đăng một website hỏng.

**3. Không có gì "chạy" sau khi website đã lên.**
Người đọc chỉ tải file tĩnh. Nên website không thể sập vì quá tải, và không có gì để bị tấn công.

---

## Phần 3 — Bốn tầng của hệ thống

Toàn bộ dự án chia làm bốn tầng. Xếp theo mức độ bạn sẽ đụng tới, từ nhiều nhất đến ít nhất.

```
┌─────────────────────────────────────────────────────────┐
│  TẦNG 1 — NỘI DUNG          Đụng tới: hằng tuần         │
│  src/content/articles/*.md                              │
│  public/images/articles/                                │
│  → Đây là tài sản thật của dự án                        │
├─────────────────────────────────────────────────────────┤
│  TẦNG 2 — CẤU HÌNH          Đụng tới: vài tháng một lần │
│  src/config/site.ts        tên site, tên miền, menu     │
│  src/config/taxonomy.ts    mô tả chủ đề, hành trình     │
│  → Sửa dữ liệu, không sửa logic                         │
├─────────────────────────────────────────────────────────┤
│  TẦNG 3 — GIAO DIỆN         Đụng tới: khi muốn đổi form │
│  src/styles/    src/components/    src/layouts/         │
│  src/pages/                                             │
│  → Đổi cả tầng này, Tầng 1 vẫn nguyên vẹn               │
├─────────────────────────────────────────────────────────┤
│  TẦNG 4 — HẠ TẦNG           Đụng tới: gần như không bao │
│  astro.config.mjs    package.json                       │
│  .github/workflows/deploy.yml    src/utils/             │
│  → Dựng một lần, chạy mãi                               │
└─────────────────────────────────────────────────────────┘
```

### Quy tắc vàng

> **Tầng trên không được biết gì về tầng dưới.**

Một file bài viết không hề biết website trông như thế nào. Nó chỉ khai báo mình có tiêu đề gì, thuộc chủ đề nào. Nhờ vậy:

- Bạn **đổi toàn bộ giao diện** (Tầng 3) mà không phải sửa một chữ nào trong bài viết.
- Bạn **đổi tên miền** (Tầng 2) mà không phải sửa một dòng nào ở Tầng 3.
- Sau này muốn bỏ Astro dùng công cụ khác, các file `.md` vẫn dùng lại được nguyên vẹn.

Đây chính là điều được nhắc tới khi nói *"nội dung tách rời khỏi hình thức"*.

---

## Phần 4 — Bản đồ: muốn đổi X thì sửa ở đâu

Tra bảng này thay vì đi tìm trong code.

### Nội dung

| Muốn làm | Sửa ở |
| --- | --- |
| Thêm bài viết | Tạo file mới trong `src/content/articles/` |
| Sửa bài đã đăng | Sửa file `.md` tương ứng, thêm `updated:` |
| Gỡ bài xuống | Đặt `draft: true` (đừng xoá file — mất lịch sử) |
| Đổi bài nổi bật trang chủ | `featured: true` / `false` trong frontmatter |
| Thêm ảnh | Bỏ vào `public/images/articles/`, khai `coverImage` |

### Danh tính website

| Muốn làm | Sửa ở |
| --- | --- |
| Đổi tên website, khẩu hiệu | `src/config/site.ts` → `SITE` |
| Đổi tác giả mặc định | `src/config/site.ts` → `SITE.author` |
| Đổi tên miền / thư mục con | `src/config/site.ts` → `DEPLOY` |
| Đổi dòng bản quyền | `src/config/site.ts` → `COPYRIGHT` |
| Thêm/bớt mục menu | `src/config/site.ts` → `NAV` |
| Thêm link mạng xã hội | `src/config/site.ts` → `SOCIAL_LINKS` |
| Đổi số bài trên trang chủ | `src/config/site.ts` → `featuredLimit`, `latestLimit` |

### Phân loại nội dung

| Muốn làm | Sửa ở |
| --- | --- |
| Thêm chủ đề mới | **Không cần sửa gì** — cứ viết `category:` mới trong bài |
| Thêm mô tả cho chủ đề | `src/config/taxonomy.ts` → `CATEGORIES` |
| Đổi đường dẫn một chủ đề | `src/config/taxonomy.ts` → thêm `slug:` cho chủ đề đó |
| Thêm thẻ mới | **Không cần sửa gì** — cứ viết trong `tags:` |
| Thêm "hành trình" mới | `src/config/taxonomy.ts` → `JOURNEYS` |

### Giao diện

| Muốn làm | Sửa ở |
| --- | --- |
| Đổi màu chủ đạo | `src/styles/global.css` → khối `:root` (và khối `[data-theme='dark']`) |
| Đổi cỡ chữ | `src/styles/global.css` → các biến `--step-*` |
| Đổi độ rộng cột chữ khi đọc | `src/styles/global.css` → `--measure` |
| Sửa cách hiển thị bài viết | `src/layouts/ArticleLayout.astro` |
| Sửa thẻ bài viết | `src/components/ArticleCard.astro` |
| Sửa trang chủ | `src/pages/index.astro` |
| Thêm kiểu hộp Callout mới | `src/components/Callout.astro` + `src/styles/article.css` |
| Thêm một trang mới (vd `/lien-he/`) | Tạo `src/pages/lien-he.astro` |

### Kỹ thuật

| Muốn làm | Sửa ở |
| --- | --- |
| Thêm trường frontmatter mới | `src/content.config.ts` → `schema` |
| Đổi cách tính thời gian đọc | `src/config/site.ts` → `SITE.wordsPerMinute` |
| Đổi cách chọn bài liên quan | `src/utils/articles.ts` → `getRelatedArticles` |
| Sửa quy trình đăng | `.github/workflows/deploy.yml` |

---

## Phần 5 — Danh sách những gì TỰ ĐỘNG

Đây là lời hứa cốt lõi của hệ thống. Khi bạn thêm **một** file Markdown, tất cả những thứ dưới đây cập nhật mà bạn **không phải làm gì**:

| # | Tự động cập nhật | Ở đâu |
| --- | --- | --- |
| 1 | Trang riêng của bài viết | `/articles/ten-bai/` |
| 2 | Danh sách tất cả bài viết | `/articles/` |
| 3 | Khối "Bài viết mới nhất" trang chủ | `/` |
| 4 | Khối "Bài viết nổi bật" (nếu `featured: true`) | `/` |
| 5 | Trang chủ đề tương ứng | `/categories/xxx/` |
| 6 | **Tạo mới** trang chủ đề nếu chủ đề chưa từng có | `/categories/moi/` |
| 7 | Danh sách chủ đề + số bài mỗi chủ đề | `/categories/` |
| 8 | Trang từng thẻ | `/tags/xxx/` |
| 9 | **Tạo mới** trang thẻ nếu thẻ chưa từng có | `/tags/moi/` |
| 10 | Danh sách thẻ + số bài mỗi thẻ | `/tags/` |
| 11 | Các trang hành trình khớp tag/chủ đề | `/journeys/xxx/` |
| 12 | Mục "Bài viết liên quan" ở **các bài khác** | mọi bài |
| 13 | Điều hướng bài trước / bài sau | mọi bài |
| 14 | Nguồn cấp RSS | `/rss.xml` |
| 15 | Sitemap cho Google | `/sitemap-index.xml` |
| 16 | Chỉ mục tìm kiếm | `/search-index.json` |
| 17 | Thời gian đọc ước lượng | tính từ số từ |
| 18 | Mục lục trong bài | tính từ các `##` |
| 19 | Thẻ Open Graph để chia sẻ Facebook/Zalo | `<head>` của bài |
| 20 | Dữ liệu có cấu trúc Schema.org | `<head>` của bài |
| 21 | Danh sách chủ đề ở chân trang | mọi trang |
| 22 | `robots.txt` trỏ đúng sitemap | `/robots.txt` |

> **Nếu có ngày nào bạn thấy mình phải sửa tay một trong 22 mục trên khi đăng bài — hệ thống đã bị hỏng ở đâu đó.** Hãy quay lại đọc Phần 8.

---

## Phần 6 — Vì sao lại làm như vậy: các quyết định kiến trúc

Phần này giải thích các lựa chọn quan trọng, để sau này bạn (hoặc người khác) không vô tình phá bỏ chúng vì tưởng là tuỳ tiện.

### 6.1 — Vì sao là website tĩnh, không có cơ sở dữ liệu

**Lựa chọn:** sinh HTML sẵn khi build, không có máy chủ động, không có CSDL.

**Vì sao:** dự án này nhắm tới việc tồn tại **nhiều năm**, do **một người** duy trì. Cơ sở dữ liệu cần sao lưu, cần nâng cấp, cần bảo mật, cần trả tiền. Một thư mục file `.md` trong Git thì không cần gì cả — và có thể mở bằng Notepad sau 10 năm.

**Đánh đổi:** không có bình luận, không có tài khoản. Chấp nhận được với một thư viện bài đọc.

### 6.2 — Vì sao chủ đề do nội dung quyết định, không do danh sách cứng

**Lựa chọn:** chủ đề được gom lại **từ frontmatter các bài viết**. File `taxonomy.ts` chỉ bổ sung mô tả.

**Vì sao:** nếu danh sách chủ đề nằm cứng trong code, thì mỗi lần muốn thêm chủ đề bạn phải sửa code — và đó chính là lúc người ta bỏ cuộc. Với cách hiện tại, viết `category: "Chủ đề chưa từng có"` là trang chủ đề mới tự xuất hiện.

**Cách kiểm chứng:** mở `src/utils/articles.ts`, hàm `getCategoriesWithArticles()` — nó duyệt bài viết rồi mới dựng danh sách, chứ không đọc từ một mảng cố định.

**Cái giá:** viết sai chính tả tên chủ đề sẽ tạo ra một chủ đề mới thay vì báo lỗi. Hãy copy-paste tên chủ đề giữa các bài.

### 6.3 — Vì sao chỉ có MỘT nơi khai báo tên miền

**Lựa chọn:** `src/config/site.ts` là nguồn duy nhất. `astro.config.mjs` **import** từ đó.

**Vì sao:** lỗi phổ biến nhất khi deploy Astro lên GitHub Pages là `base` bị khai hai nơi và lệch nhau, khiến website mất sạch CSS. Bằng cách để `astro.config.mjs` đọc từ `site.ts`, tình huống đó **không thể xảy ra**.

**Hệ quả:** đổi tên miền = sửa đúng 2 dòng, ở đúng 1 file.

### 6.4 — Vì sao mọi liên kết đều đi qua hàm `withBase()`

**Lựa chọn:** không viết `href="/articles/"` trực tiếp ở bất kỳ đâu. Luôn viết `href={withBase('/articles/')}`.

**Vì sao:** khi website nằm trong thư mục con (`/dong-hanh-cung-con/`), đường dẫn `/articles/` trỏ ra ngoài gốc tên miền và bị 404. Hàm `withBase()` trong `src/utils/url.ts` tự gắn tiền tố.

> ⚠️ **Đây là quy tắc dễ vi phạm nhất khi thêm trang mới.** Nếu bạn thêm một liên kết mà quên `withBase()`, trên máy bạn (`npm run dev`) nó vẫn chạy, nhưng lên GitHub Pages sẽ hỏng. Hãy kiểm tra bằng `npm run preview` chứ không chỉ `npm run dev`.

### 6.5 — Vì sao JavaScript chỉ là "gia vị", không phải "nguyên liệu"

**Lựa chọn:** tắt JavaScript thì website vẫn đọc được gần như đầy đủ.

Cụ thể:

| Tính năng | Không có JavaScript thì sao |
| --- | --- |
| Đọc bài viết | Bình thường |
| Menu di động | Vẫn mở được (dùng thẻ `<details>` của HTML) |
| Mục lục | Bình thường |
| Thanh tiến độ đọc | Đứng yên (làm bằng CSS thuần) |
| Chế độ tối | Vẫn theo cài đặt hệ điều hành, chỉ mất nút bấm tay |
| Trang tìm kiếm | Hiện toàn bộ danh sách bài để tự duyệt |
| Nút chia sẻ | Facebook/X/LinkedIn vẫn chạy; mất nút "sao chép" |

**Vì sao:** người đọc chủ yếu dùng điện thoại, mạng có lúc chập chờn. Nội dung không nên phụ thuộc vào việc một file `.js` tải xong.

### 6.6 — Vì sao thanh tiến độ đọc làm bằng CSS

**Lựa chọn:** dùng `animation-timeline: scroll()` thay vì bắt sự kiện cuộn bằng JavaScript.

**Vì sao:** bắt sự kiện cuộn bằng JavaScript làm giật trang trên điện thoại yếu. CSS chạy trên luồng đồ hoạ, không giật. Trình duyệt chưa hỗ trợ thì thanh đứng yên — không ai mất gì.

### 6.7 — Vì sao tìm kiếm không dùng dịch vụ ngoài

**Lựa chọn:** sinh sẵn `search-index.json` khi build, trình duyệt tải một lần rồi lọc tại chỗ.

**Vì sao:** các dịch vụ tìm kiếm bên ngoài cần đăng ký, cần khoá API, có giới hạn miễn phí, và có thể ngừng hoạt động. Với quy mô vài trăm bài viết, tệp JSON chỉ vài trăm KB — lọc trong trình duyệt là quá đủ và nhanh hơn.

**Điểm cộng:** từ khoá bạn gõ không được gửi đi đâu cả.

**Khi nào cần đổi:** nếu thư viện vượt khoảng **500 bài**, tệp chỉ mục sẽ nặng. Lúc đó hãy giảm độ dài đoạn trích trong `buildSearchIndex()` (`src/utils/articles.ts`) từ 1500 xuống 400 ký tự trước khi nghĩ tới dịch vụ ngoài.

### 6.8 — Vì sao gõ không dấu vẫn tìm ra

Cả phía build và phía trình duyệt đều chuẩn hoá chữ bằng cách tách dấu (`normalize('NFD')`) rồi xoá dấu, và xử lý riêng chữ `đ`. Nhờ vậy `dong luc` khớp với `động lực`. Cùng một thuật toán được dùng để sinh đường dẫn — nên `/tags/dong-luc/` luôn khớp với thẻ `động lực`.

### 6.9 — Vì sao frontmatter được kiểm tra nghiêm ngặt

**Lựa chọn:** `src/content.config.ts` mô tả chính xác các trường hợp lệ. Sai là build dừng.

**Vì sao:** một bài viết thiếu `description` sẽ hiển thị xấu trên Google và khi chia sẻ — nhưng bạn sẽ không nhận ra cho tới khi ai đó nói. Dừng ngay lúc build là cách rẻ nhất để phát hiện.

### 6.10 — Vì sao chỉ có 3 thư viện phụ thuộc

Chỉ dùng `@astrojs/mdx`, `@astrojs/rss`, `@astrojs/sitemap`. Không React, không Tailwind, không thư viện icon, không thư viện animation.

**Vì sao:** mỗi thư viện thêm vào là một thứ có thể hỏng khi nâng cấp, và một thứ phải học lại sau hai năm không đụng tới. Với một website đọc chữ là chính, CSS thuần là đủ.

---

## Phần 7 — Vòng đời một bài viết

Từ lúc là ghi chép vụn cho tới lúc có người đọc trên điện thoại.

```
① GHI CHÉP THÔ
   File Word, tin nhắn, ghi vội, một cuộc trao đổi
                │
                ▼
② BIÊN TẬP (có thể nhờ trợ lý AI)
   Xem docs/AI_CONTENT_WORKFLOW.md
   ⚠️ Giữ nguyên luận điểm gốc. Đánh dấu phần mở rộng.
                │
                ▼
③ KIỂM CHỨNG NGUỒN
   Mọi con số, nghiên cứu, trích dẫn → tự mở link kiểm tra
   ⚠️ Không kiểm chứng được → bỏ ý đó hoặc ghi rõ là chưa chắc
                │
                ▼
④ TẠO FILE
   src/content/articles/ten-khong-dau.md
   Frontmatter: title, description, date, category  (+ draft: true)
                │
                ▼
⑤ XEM THỬ
   npm run dev      → bài nháp vẫn hiện
   npm run build && npm run preview  → giống hệt bản thật
                │
                ▼
⑥ XUẤT BẢN
   draft: false
   git add . && git commit -m "Bài mới: ..." && git push
                │
                ▼
⑦ TỰ ĐỘNG (1–2 phút)
   GitHub build → đăng → 22 mục ở Phần 5 tự cập nhật
                │
                ▼
⑧ NGƯỜI ĐỌC
   Tìm thấy qua: trang chủ · chủ đề · thẻ · hành trình ·
   tìm kiếm · Google · RSS · link chia sẻ trên Facebook/Zalo
```

**Chú ý bước ③.** Đây là bước duy nhất không tự động hoá được, và cũng là bước quyết định uy tín lâu dài của thư viện.

---

## Phần 8 — Ba điều dễ làm hỏng hệ thống

Hệ thống này khá bền, nhưng có ba cách phá vỡ nó. Cả ba đều xảy ra khi ai đó "làm cho nhanh".

### 8.1 — Viết thẳng một trang HTML cho một bài viết

**Đừng làm:** tạo `src/pages/bai-viet-dac-biet.astro` chứa nội dung bài viết.

**Vì sao hỏng:** bài đó sẽ không có trong RSS, không có trong sitemap, không có trong tìm kiếm, không hiện ở trang chủ đề, không được tính là bài liên quan. Bạn sẽ có một bài viết "vô hình" — và sáu tháng sau không hiểu vì sao nó không xuất hiện ở đâu cả.

**Làm thay:** nếu bài cần trình bày đặc biệt, dùng `.mdx` và tạo thêm một component trong `src/components/`.

### 8.2 — Viết cứng tên tác giả / tên website vào component

**Đừng làm:** gõ thẳng `Mr. Lucero` hay `Đồng hành cùng con` vào một file `.astro`.

**Vì sao hỏng:** đến lúc muốn đổi, bạn phải đi tìm khắp nơi và chắc chắn sẽ sót.

**Làm thay:** luôn `import { SITE } from '../config/site'`.

**Cách tự kiểm tra:**

```bash
grep -rn "Mr. Lucero" src/ --include=*.astro
```

Lệnh trên **phải không trả về kết quả nào**. Nếu có, đó là chỗ cần sửa.

### 8.3 — Viết liên kết nội bộ mà quên `withBase()`

**Đừng làm:** `<a href="/articles/">`

**Vì sao hỏng:** chạy tốt trên máy bạn, hỏng trên website thật (xem 6.4).

**Làm thay:** `<a href={withBase('/articles/')}>`

**Cách tự kiểm tra:**

```bash
grep -rn 'href="/' src/ --include=*.astro
```

Kết quả trả về **chỉ được phép** là link ra ngoài (`https://…`). Mọi link nội bộ đều phải qua `withBase()`.

---

## Phần 9 — Tự chẩn đoán khi có sự cố

Đi theo cây quyết định này.

### "Website mất hết CSS, chỉ còn chữ đen trên nền trắng"

→ `base` sai. Mở `src/config/site.ts`, đảm bảo `base` khớp **chính xác** tên repo, có dấu `/` ở hai đầu.

### "Actions xanh nhưng vào link thì 404"

→ Chưa bật Pages đúng cách. Settings → Pages → Source → **GitHub Actions** (không phải "Deploy from a branch").

### "Bài mới không hiện ở đâu cả"

Kiểm tra theo thứ tự:

1. `draft:` có phải `true` không?
2. `date` có phải ngày trong tương lai không?
3. File có nằm đúng trong `src/content/articles/` không?
4. Đuôi file có phải `.md` / `.mdx` không?
5. Chạy `npm run build` — có báo lỗi gì không?

### "Actions đỏ"

1. Bấm vào lần chạy đỏ → xem log
2. Đỏ ở bước **"Cài thư viện"** → chưa đẩy `package-lock.json` lên
3. Đỏ ở bước **"Build website"** → chạy `npm run build` ở nhà, lỗi hiện y hệt

### "Một chủ đề bị tách làm hai"

→ Tên chủ đề viết khác nhau giữa các bài. Kiểm tra:

```bash
grep -h "^category:" src/content/articles/*.md* | sort | uniq -c
```

Lệnh này liệt kê mọi cách viết chủ đề kèm số lần xuất hiện. Cách viết nào chỉ xuất hiện một lần rất đáng ngờ.

### "Chia sẻ lên Facebook không hiện ảnh"

1. `siteUrl` còn là `your-username` không?
2. Dùng [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/), bấm **Scrape Again** — Facebook lưu đệm rất lâu
3. Ảnh phải đúng 1200×630

### "Tôi lỡ làm hỏng gì đó và không biết sửa"

```bash
git log --oneline        # xem lịch sử
git diff                 # xem mình vừa sửa gì
git checkout -- .        # bỏ hết thay đổi chưa commit
git revert <mã-commit>   # hoàn tác một commit đã đẩy lên
```

Git giữ lại mọi phiên bản. Bạn không thể mất nội dung, trừ khi tự xoá file và chưa từng commit.

---

## Phần 10 — Kiểm tra sức khoẻ định kỳ

Vài tháng một lần, chạy hết những lệnh dưới đây. Mất khoảng 5 phút.

```bash
# 1. Build sạch — phải không có lỗi
npm run build

# 2. Kiểm tra kiểu dữ liệu và frontmatter
npm run check

# 3. Không có tên riêng bị viết cứng trong giao diện
grep -rn "Mr. Lucero" src/ --include=*.astro          # phải rỗng

# 4. Không có liên kết nội bộ quên withBase()
grep -rn 'href="/' src/ --include=*.astro             # chỉ được có link ngoài

# 5. Kiểm tra chủ đề có bị viết lệch không
grep -h "^category:" src/content/articles/*.md* | sort | uniq -c

# 6. Xem có bài nháp nào bị quên không
grep -l "draft: true" src/content/articles/*

# 7. Xem bản build thật trong trình duyệt
npm run preview
```

Rồi mở website thật và kiểm tra bằng mắt:

- [ ] Trang chủ hiện đúng số bài mong đợi
- [ ] Mở một bài bất kỳ trên **điện thoại**
- [ ] Gõ thử một từ khoá **không dấu** trong trang tìm kiếm
- [ ] `/rss.xml` và `/sitemap-index.xml` mở được
- [ ] Bật chế độ tối, xem chữ có đủ rõ không
- [ ] Dán link một bài vào Zalo hoặc Facebook, xem ảnh và tiêu đề

### Nâng cấp thư viện (mỗi 6–12 tháng)

```bash
npm outdated                 # xem cái gì cũ
npm update                   # nâng cấp trong phạm vi an toàn
npm run build                # PHẢI chạy lại và kiểm tra kỹ
```

> Nâng cấp lớn (ví dụ Astro 7 → 8) thì làm trên một nhánh riêng:
> `git checkout -b nang-cap-astro` — hỏng thì bỏ nhánh, `main` vẫn nguyên.

---

## Phần 11 — Nhật ký thay đổi

Mỗi lần thay đổi hệ thống ở mức đáng kể, hãy thêm một mục vào đây. Sáu tháng sau bạn sẽ cảm ơn chính mình.

### v1.0.0 — 11/08/2026 — Phiên bản đầu tiên

**Nền tảng**

- Astro 7 + TypeScript, sinh HTML tĩnh hoàn toàn
- Đúng 3 thư viện phụ thuộc: `@astrojs/mdx`, `@astrojs/rss`, `@astrojs/sitemap`
- Cấu hình tập trung tại `src/config/site.ts`; `astro.config.mjs` đọc từ đó (chống lệch `base`)
- Chế độ tối: theo hệ điều hành + nút chuyển thủ công, lưu trong trình duyệt

**Nội dung**

- Content Collections với schema đầy đủ, kiểm tra nghiêm ngặt lúc build
- Hỗ trợ cả `.md` và `.mdx`
- Trường `sourceType` và `references` phục vụ nguyên tắc toàn vẹn nguồn
- Thời gian đọc tính tự động từ số từ
- Chủ đề và thẻ suy ra từ nội dung, không có danh sách cứng
- "Hành trình" gom bài theo tình huống cha mẹ gặp phải; hành trình chưa có bài thì tự ẩn

**Trải nghiệm đọc**

- Cột chữ rộng ~704px, cỡ chữ co giãn theo màn hình
- Mục lục tự sinh: cột bên phải trên máy tính, khối gập lại trên điện thoại
- Thanh tiến độ đọc bằng CSS thuần, không dùng JavaScript
- Sáu kiểu hộp Callout: `tip`, `warning`, `say`, `reflect`, `key`, `avoid`
- Vụn đường dẫn, bài liên quan, điều hướng bài trước/sau, nút chia sẻ

**Tìm kiếm & SEO**

- Tìm kiếm phía trình duyệt, không dấu vẫn khớp, không dùng dịch vụ ngoài
- Sitemap, RSS, `robots.txt` sinh tự động theo cấu hình
- Open Graph, Twitter Card, Schema.org (`WebSite`, `BlogPosting`, `BreadcrumbList`)
- Ảnh chia sẻ mặc định 1200×630 + script `npm run og` tạo ảnh riêng cho từng bài

**Khả năng tiếp cận**

- Kiểm tra thực tế ở 360 / 390 / 768 / 1024 / 1440px — **không có tràn ngang trên bất kỳ trang nào**
- Liên kết "bỏ qua điều hướng" là phần tử nhận focus đầu tiên
- Vùng chạm tối thiểu 44px, vòng focus luôn nhìn thấy
- Menu di động dùng `<details>` — chạy cả khi tắt JavaScript
- Tôn trọng `prefers-reduced-motion` và `prefers-color-scheme`

**Nội dung khởi đầu (3 bài)**

1. *Từ phần thưởng đến động lực bên trong* — biên tập từ ghi chép gốc, có đối chiếu nghiên cứu đã kiểm chứng (Lepper 1973; Deci, Koestner & Ryan 1999) **và nêu rõ phần còn tranh luận** (Cameron & Pierce 1994; Eisenberger & Cameron 1996)
2. *Hỏi con học được gì, thay vì hỏi con được mấy điểm*
3. *Cấu trúc thay vì nhắc nhở*

**Triển khai**

- GitHub Actions tự build và đăng khi push lên `main`
- Hỗ trợ cả project site và user site; sẵn sàng gắn tên miền riêng

**Tài liệu**

- `README.md`, `docs/CONTENT_GUIDE.md`, `docs/AI_CONTENT_WORKFLOW.md`, `docs/DEPLOYMENT.md`, `templates/article-template.md`, và tài liệu này

---

### Mẫu ghi cho lần thay đổi sau

```markdown
### v1.1.0 — ngày/tháng/năm — Tên ngắn gọn

**Đã đổi**
- …

**Vì sao**
- …

**Cần chú ý**
- …
```

---

## Phần 12 — Những hướng mở rộng đã được tính sẵn

Hệ thống được dựng sao cho các việc dưới đây làm được **mà không phải đập đi xây lại**. Nêu ở đây để bạn biết mình có sẵn những lựa chọn nào — không có nghĩa là nên làm ngay.

| Muốn thêm | Cách làm | Độ khó |
| --- | --- | --- |
| Chuỗi bài nhiều kỳ | Thêm `series` và `seriesOrder` vào schema, tạo `src/pages/series/[slug].astro` | Dễ |
| Phân trang khi nhiều bài | Dùng `paginate()` của Astro trong `articles/index.astro` | Dễ |
| Trang tác giả (nhiều người viết) | Tạo collection `authors`, liên kết bằng `reference()` | Trung bình |
| Đăng ký nhận bài qua email | Nhúng form của dịch vụ bên ngoài vào Footer | Dễ |
| Bình luận | Dịch vụ bình luận dựa trên GitHub Issues | Trung bình |
| Bản in / xuất PDF từng bài | Đã có CSS `@media print`; thêm nút gọi `window.print()` | Dễ |
| Đa ngôn ngữ | Astro có sẵn cơ chế i18n; cần tổ chức lại thư mục nội dung | Khó |
| Ảnh chia sẻ riêng cho mọi bài | Chạy `npm run og` trong bước build của GitHub Actions | Trung bình |

**Nguyên tắc khi mở rộng:** giữ nguyên hai thứ — *nội dung là file Markdown*, và *chủ đề do nội dung quyết định*. Còn lại đổi thoải mái.

---

## Lời cuối

Hệ thống này được thiết kế để **một người có thể duy trì trong nhiều năm**.

Điều đó có nghĩa là mỗi lần bạn định thêm một tính năng, câu hỏi đáng hỏi không phải *"làm được không?"* mà là:

> **"Sáu tháng nữa, khi quên hết mọi thứ, tôi có còn hiểu và sửa được cái này không?"**

Nếu câu trả lời là không, thì thứ đáng làm nhất có lẽ là viết thêm một bài viết mới — vì đó mới là tài sản thật của dự án.

---

<small>

Tài liệu này là bản `.md` gốc. Bản `.html` đi kèm được tạo ra từ chính file này để đọc cho dễ.
Sửa nội dung thì sửa file `.md`. Muốn tạo lại bản `.html` (cần cài [pandoc](https://pandoc.org)):

```bash
pandoc dong-hanh-guide.md -o dong-hanh-guide.html --standalone --toc --toc-depth=2 --metadata title="Đồng hành cùng hệ thống"
```

Không có pandoc cũng không sao — bản `.md` đọc tốt trên GitHub và trong mọi trình soạn thảo.

</small>
