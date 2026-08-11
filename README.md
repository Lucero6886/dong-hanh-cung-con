# Đồng hành cùng con

> Hiểu con hơn · Đồng hành đúng cách · Cùng con trưởng thành

Thư viện bài viết dành cho cha mẹ Việt Nam về giáo dục trẻ và hành trình đồng hành cùng con.

Đây là một **website tĩnh**: không có máy chủ, không có cơ sở dữ liệu, không có tài khoản đăng nhập, không có chi phí vận hành. Bạn viết bài bằng Markdown, đẩy lên GitHub, website tự build và tự đăng.

---

## Mục lục

- [Website này hoạt động thế nào](#website-này-hoạt-động-thế-nào)
- [Công nghệ](#công-nghệ)
- [Yêu cầu trước khi bắt đầu](#yêu-cầu-trước-khi-bắt-đầu)
- [Cài đặt](#cài-đặt)
- [Chạy trên máy mình](#chạy-trên-máy-mình)
- [Cấu trúc thư mục](#cấu-trúc-thư-mục)
- [Thêm một bài viết mới](#thêm-một-bài-viết-mới)
- [Build](#build)
- [Đăng lên GitHub Pages](#đăng-lên-github-pages)
- [Tuỳ chỉnh website](#tuỳ-chỉnh-website)
- [Xử lý sự cố](#xử-lý-sự-cố)
- [Tài liệu khác](#tài-liệu-khác)

---

## Website này hoạt động thế nào

Một câu để nhớ:

> **Nội dung nằm trong file Markdown. Giao diện nằm trong code. Hai thứ đó tách rời nhau.**

Điều đó có nghĩa là:

- Thêm một file `.md` vào `src/content/articles/` → website **tự động** tạo trang bài viết, thêm vào trang chủ, thêm vào trang chủ đề, tạo trang thẻ, cập nhật RSS, cập nhật sitemap và cập nhật chỉ mục tìm kiếm.
- Bạn **không bao giờ** phải sửa trang chủ, trang danh mục hay file cấu hình khi đăng bài mới.
- Sau này đổi hoàn toàn giao diện, các bài viết vẫn còn nguyên vẹn và dùng lại được.

Xem giải thích chi tiết bằng hình trong [`dong-hanh-guide.md`](./dong-hanh-guide.md) — tài liệu đồng hành giúp bạn làm chủ hệ thống.

---

## Công nghệ

| Thành phần | Lựa chọn | Vì sao |
| --- | --- | --- |
| Khung sườn | [Astro](https://astro.build) 7 | Sinh HTML tĩnh, gửi rất ít JavaScript xuống trình duyệt |
| Nội dung | Markdown / MDX + Content Collections | Nội dung là file văn bản, dễ mang đi nơi khác |
| Ngôn ngữ | TypeScript | Sai frontmatter là báo lỗi ngay lúc build |
| Giao diện | CSS thuần (2 file) | Không phụ thuộc framework CSS, không sợ lỗi thời |
| Tìm kiếm | JSON tĩnh + JavaScript nhỏ | Không cần dịch vụ trả phí |
| Lưu trữ | GitHub Pages | Miễn phí, không cần máy chủ |
| Tự động hoá | GitHub Actions | Đẩy code là tự đăng |

**Tổng số thư viện phụ thuộc: 3** (`@astrojs/mdx`, `@astrojs/rss`, `@astrojs/sitemap`). Không có React, không có Tailwind, không có cơ sở dữ liệu.

---

## Yêu cầu trước khi bắt đầu

- **Node.js phiên bản 20 trở lên** — tải tại <https://nodejs.org> (chọn bản LTS).
  Kiểm tra: `node -v`
- **Git** — tải tại <https://git-scm.com>
  Kiểm tra: `git --version`
- Một tài khoản **GitHub** miễn phí.

Không cần biết lập trình để viết bài. Chỉ cần biết dùng một trình soạn thảo văn bản.

---

## Cài đặt

```bash
git clone https://github.com/<tài-khoản-của-bạn>/dong-hanh-cung-con.git
cd dong-hanh-cung-con
npm install
```

---

## Chạy trên máy mình

```bash
npm run dev
```

Mở trình duyệt tại địa chỉ hiện trong terminal (thường là <http://localhost:4321/dong-hanh-cung-con/>).

Sửa file rồi lưu → trình duyệt tự tải lại. Bấm `Ctrl + C` để dừng.

> Ở chế độ `dev`, các bài có `draft: true` **vẫn hiện** để bạn xem thử. Khi build thật thì chúng bị ẩn.

### Toàn bộ lệnh có sẵn

| Lệnh | Việc nó làm |
| --- | --- |
| `npm run dev` | Chạy website trên máy, tự tải lại khi sửa file |
| `npm run build` | Build website ra thư mục `dist/` |
| `npm run preview` | Xem thử bản đã build, giống hệt bản thật |
| `npm run check` | Kiểm tra lỗi TypeScript và lỗi frontmatter |
| `npm run og` | Tạo ảnh xem trước khi chia sẻ (1200×630) |

---

## Cấu trúc thư mục

```
dong-hanh-cung-con/
├── .github/workflows/deploy.yml   ← tự động build & đăng khi push
│
├── public/                        ← file tĩnh, copy nguyên xi khi build
│   ├── favicon.svg
│   ├── images/articles/           ← ẢNH BÀI VIẾT ĐỂ Ở ĐÂY
│   └── social/og-default.png      ← ảnh xem trước mặc định khi chia sẻ
│
├── src/
│   ├── config/
│   │   ├── site.ts                ← ⭐ SỬA Ở ĐÂY: tên site, tên miền, menu, bản quyền
│   │   └── taxonomy.ts            ← mô tả các chủ đề & hành trình
│   │
│   ├── content/articles/          ← ⭐ VIẾT BÀI Ở ĐÂY (.md / .mdx)
│   ├── content.config.ts          ← quy định các trường frontmatter hợp lệ
│   │
│   ├── components/                ← các mảnh giao diện dùng lại
│   ├── layouts/                   ← khung trang (BaseLayout, ArticleLayout)
│   ├── pages/                     ← mỗi file = một địa chỉ trên website
│   ├── styles/                    ← global.css + article.css
│   └── utils/                     ← hàm dùng chung (slug, ngày, thời gian đọc…)
│
├── docs/                          ← tài liệu hướng dẫn
├── templates/article-template.md  ← mẫu bài viết để copy
├── scripts/make-og.mjs            ← tạo ảnh chia sẻ
├── astro.config.mjs
└── package.json
```

**Ba thư mục bạn dùng thường xuyên:**

1. `src/content/articles/` — viết bài
2. `public/images/articles/` — bỏ ảnh
3. `src/config/site.ts` — chỉnh thông tin website

Mọi thứ còn lại chỉ đụng tới khi muốn đổi giao diện.

---

## Thêm một bài viết mới

### Cách nhanh nhất

```bash
# 1. Copy file mẫu
cp templates/article-template.md src/content/articles/ten-bai-viet-moi.md

# 2. Mở file vừa tạo, sửa frontmatter và viết nội dung
#    Nhớ đổi draft: true  →  draft: false  khi muốn đăng

# 3. Xem thử
npm run dev

# 4. Đăng
git add .
git commit -m "Bài mới: Tên bài viết"
git push
```

Khoảng 1–2 phút sau, website tự cập nhật. Xong.

### Frontmatter tối thiểu

```yaml
---
title: "Tiêu đề bài viết"
description: "Một hai câu tóm tắt, hiện trên Google và khi chia sẻ."
date: 2026-08-11
category: "Động lực & thói quen"
tags: ["động lực", "trách nhiệm"]
draft: false
---
```

Bốn trường đầu là bắt buộc. Thiếu là `npm run build` báo lỗi kèm tên file — đó là chủ ý, để không đăng nhầm bài hỏng.

**Tên file chính là địa chỉ bài viết:**
`cau-truc-thay-vi-nhac-nho.md` → `/articles/cau-truc-thay-vi-nhac-nho/`
Nên đặt tên không dấu, dùng gạch ngang.

Hướng dẫn đầy đủ (ảnh, hộp callout, trích nguồn, bài nháp…): [`docs/CONTENT_GUIDE.md`](./docs/CONTENT_GUIDE.md)

---

## Build

```bash
npm run build     # kết quả nằm trong dist/
npm run preview   # xem thử bản vừa build
```

Nếu `npm run build` chạy xong không lỗi thì bản đăng lên GitHub cũng sẽ chạy được — vì GitHub chạy đúng lệnh đó.

---

## Đăng lên GitHub Pages

### Lần đầu tiên (làm một lần duy nhất)

**Bước 1 — Sửa cấu hình.** Mở `src/config/site.ts`, sửa khối `DEPLOY`:

```ts
export const DEPLOY = {
  siteUrl: 'https://TEN-TAI-KHOAN-GITHUB.github.io',
  base: '/dong-hanh-cung-con/',   // đúng bằng tên repo, có dấu / ở hai đầu
};
```

> Nếu repo của bạn tên là `TEN-TAI-KHOAN.github.io` thì đặt `base: '/'`.

**Bước 2 — Tạo repo và đẩy code lên:**

```bash
git init
git add .
git commit -m "Khởi tạo website Đồng hành cùng con"
git branch -M main
git remote add origin https://github.com/TEN-TAI-KHOAN/dong-hanh-cung-con.git
git push -u origin main
```

**Bước 3 — Bật GitHub Pages.** Đây là bước hay bị bỏ sót:

> Vào repo trên GitHub → tab **Settings** → mục **Pages** (cột trái)
> → phần **Build and deployment** → **Source**: chọn **GitHub Actions**

Không chọn "Deploy from a branch".

**Bước 4 — Chờ và kiểm tra.** Vào tab **Actions**, chờ dấu ✓ màu xanh (khoảng 1–2 phút). Website nằm tại:
`https://TEN-TAI-KHOAN.github.io/dong-hanh-cung-con/`

### Những lần sau

```bash
git add .
git commit -m "Bài mới: ..."
git push
```

Chỉ vậy thôi. Chi tiết và cách gắn tên miền riêng: [`docs/DEPLOYMENT.md`](./docs/DEPLOYMENT.md)

---

## Tuỳ chỉnh website

Gần như mọi thứ nằm trong **`src/config/site.ts`**:

| Muốn đổi | Sửa ở |
| --- | --- |
| Tên website, khẩu hiệu, mô tả | `SITE` |
| Tên miền, thư mục con | `DEPLOY` |
| Tác giả mặc định | `SITE.author` |
| Menu điều hướng | `NAV` |
| Liên kết mạng xã hội | `SOCIAL_LINKS` |
| Dòng bản quyền cuối trang | `COPYRIGHT` |
| Số bài hiện trên trang chủ | `SITE.featuredLimit`, `SITE.latestLimit` |
| Mô tả các chủ đề | `src/config/taxonomy.ts` → `CATEGORIES` |
| Các "hành trình" | `src/config/taxonomy.ts` → `JOURNEYS` |
| Màu sắc, phông chữ | `src/styles/global.css` → khối `:root` |

Không có tên tác giả hay tên website nào bị viết cứng rải rác trong code.

---

## Xử lý sự cố

**`npm run build` báo lỗi về một bài viết**
Thông báo lỗi có ghi tên file và tên trường sai. Thường là thiếu `description`, hoặc `date` sai định dạng (phải là `2026-08-11`, không phải `11/08/2026`).

**Website đăng lên nhưng mất hết CSS, chữ trơ trọi**
`base` trong `src/config/site.ts` không khớp tên repo. Repo tên `abc` thì phải là `base: '/abc/'`.

**Actions chạy xanh nhưng vào link thì 404**
Chưa làm Bước 3 ở trên (chọn Source = GitHub Actions).

**Bài viết mới không hiện**
Kiểm tra `draft:` — nếu là `true` thì bài bị ẩn khi build thật. Đổi thành `false`.

**Ảnh không hiện**
Ảnh phải nằm trong `public/`, và đường dẫn viết từ gốc `public`:
ảnh ở `public/images/articles/abc.webp` → viết `coverImage: "/images/articles/abc.webp"`.

**Actions báo lỗi `npm ci`**
File `package-lock.json` chưa được đẩy lên. Chạy `git add package-lock.json && git commit -m "lockfile" && git push`.

---

## Tài liệu khác

| File | Nội dung |
| --- | --- |
| [`dong-hanh-guide.md`](./dong-hanh-guide.md) | **Tài liệu đồng hành** — hiểu bản chất hệ thống, nhật ký thay đổi |
| [`docs/CONTENT_GUIDE.md`](./docs/CONTENT_GUIDE.md) | Hướng dẫn viết bài đầy đủ (dành cho người không rành web) |
| [`docs/AI_CONTENT_WORKFLOW.md`](./docs/AI_CONTENT_WORKFLOW.md) | Biến ghi chép thô thành bài viết bằng trợ lý AI |
| [`docs/DEPLOYMENT.md`](./docs/DEPLOYMENT.md) | Đăng website, xử lý lỗi, gắn tên miền riêng |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | Quy ước biên tập và kỹ thuật |
| [`templates/article-template.md`](./templates/article-template.md) | Mẫu bài viết để copy |

---

## Giấy phép

Mã nguồn: giấy phép MIT (xem [`LICENSE`](./LICENSE)).
Nội dung bài viết: bản quyền thuộc tác giả, xem dòng bản quyền ở chân trang website.
