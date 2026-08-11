# Đăng website lên GitHub Pages

---

## Trước tiên: chọn kiểu địa chỉ

GitHub Pages có hai kiểu. **Chọn sai là website mất hết CSS**, nên hãy đọc kỹ mục này.

### Kiểu A — Project site (khuyến nghị, và là cấu hình đang dùng)

| | |
| --- | --- |
| Tên repo | `dong-hanh-cung-con` (hoặc tên bất kỳ) |
| Địa chỉ website | `https://TEN-TAI-KHOAN.github.io/dong-hanh-cung-con/` |
| `siteUrl` | `'https://TEN-TAI-KHOAN.github.io'` |
| `base` | `'/dong-hanh-cung-con/'` |

Ưu điểm: một tài khoản GitHub đăng được nhiều website.

### Kiểu B — User site

| | |
| --- | --- |
| Tên repo | **bắt buộc** là `TEN-TAI-KHOAN.github.io` |
| Địa chỉ website | `https://TEN-TAI-KHOAN.github.io/` |
| `siteUrl` | `'https://TEN-TAI-KHOAN.github.io'` |
| `base` | `'/'` |

Ưu điểm: địa chỉ ngắn, không có thư mục con.

---

## Bước 1 — Sửa cấu hình

Mở **`src/config/site.ts`**, sửa khối `DEPLOY` ở đầu file:

```ts
export const DEPLOY = {
  siteUrl: 'https://TEN-TAI-KHOAN-CUA-BAN.github.io',
  base: '/dong-hanh-cung-con/',
};
```

> Đây là **nơi duy nhất** trong toàn dự án khai báo địa chỉ website. `astro.config.mjs` đọc thẳng từ file này, nên không có chỗ thứ hai để quên sửa.

**Quy tắc cho `base`:**

- Phải có dấu `/` ở **cả hai đầu**: `'/dong-hanh-cung-con/'` ✅
- Không phải `'dong-hanh-cung-con'` ❌ hay `'/dong-hanh-cung-con'` ❌
- Phải **khớp chính xác** tên repo, kể cả chữ hoa chữ thường

**Quy tắc cho `siteUrl`:**

- Không có dấu `/` ở cuối: `'https://abc.github.io'` ✅ chứ không phải `'https://abc.github.io/'` ❌
- Không bao gồm phần `base`

---

## Bước 2 — Kiểm tra trước trên máy

```bash
npm run build
npm run preview
```

Mở địa chỉ hiện trong terminal. Nếu website hiển thị đầy đủ giao diện và bấm chuyển trang bình thường thì cấu hình đúng.

Nếu chữ trơ trọi không có màu → `base` sai.

---

## Bước 3 — Tạo repo và đẩy code

```bash
git init
git add .
git commit -m "Khởi tạo website Đồng hành cùng con"
git branch -M main
git remote add origin https://github.com/TEN-TAI-KHOAN/dong-hanh-cung-con.git
git push -u origin main
```

> Nhớ đẩy cả `package-lock.json`. GitHub dùng `npm ci` và lệnh này bắt buộc phải có lockfile.

---

## Bước 4 — Bật GitHub Pages ⚠️

**Đây là bước hay bị bỏ sót nhất.** Không làm bước này thì Actions vẫn chạy xanh nhưng vào link sẽ 404.

1. Vào repo trên GitHub
2. Tab **Settings**
3. Cột trái, mục **Pages**
4. Phần **Build and deployment** → **Source**
5. Chọn **GitHub Actions**

**Không** chọn "Deploy from a branch".

---

## Bước 5 — Chờ build

Vào tab **Actions** của repo. Bạn sẽ thấy workflow "Deploy to GitHub Pages" đang chạy.

- Mất khoảng 1–2 phút
- Dấu ✓ xanh = xong
- Dấu ✗ đỏ = có lỗi, bấm vào để xem log

---

## Bước 6 — Kiểm tra website

Mở `https://TEN-TAI-KHOAN.github.io/dong-hanh-cung-con/` và kiểm tra:

- [ ] Trang chủ hiện đầy đủ giao diện, có màu
- [ ] Bấm vào một bài viết → mở được
- [ ] Bấm vào một chủ đề → mở được
- [ ] Trang tìm kiếm gõ chữ ra kết quả
- [ ] `/rss.xml` mở được
- [ ] `/sitemap-index.xml` mở được
- [ ] Xem trên điện thoại
- [ ] Dán link bài viết vào Facebook/Zalo → hiện đúng tiêu đề và ảnh

---

## Những lần đăng sau

```bash
git add .
git commit -m "Bài mới: ..."
git push
```

Hết. Không cần vào GitHub, không cần bấm gì.

---

## Xử lý sự cố

### Website hiện chữ trơ, không có CSS

`base` sai. Repo tên `abc` thì `base` phải là `'/abc/'`.
Sửa `src/config/site.ts`, commit, push lại.

### Actions xanh nhưng link 404

Chưa làm **Bước 4**. Vào Settings → Pages → Source → chọn "GitHub Actions".

### Actions đỏ ở bước "Cài thư viện" (`npm ci`)

Chưa đẩy `package-lock.json`:

```bash
git add package-lock.json
git commit -m "Thêm lockfile"
git push
```

### Actions đỏ ở bước "Build website"

Lỗi trong nội dung hoặc code. Bấm vào log để xem thông báo — thường ghi rõ tên file và trường frontmatter sai.
Cách nhanh: chạy `npm run build` trên máy mình, lỗi hiện y hệt.

### Bài mới không xuất hiện

1. `draft:` có đang là `true` không?
2. `date` có phải ngày trong tương lai không?
3. File có nằm đúng trong `src/content/articles/` không?
4. Đuôi file có phải `.md` hoặc `.mdx` không?

### Chia sẻ lên Facebook không hiện ảnh

1. `siteUrl` phải là địa chỉ thật, không còn là `your-username`
2. Dùng công cụ [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) và bấm "Scrape Again" — Facebook lưu đệm rất lâu
3. Ảnh phải đúng 1200×630px

### Link cũ bị hỏng sau khi đổi tên file

Đổi tên file = đổi địa chỉ bài viết. Nếu bài đã được chia sẻ, hãy cân nhắc giữ tên cũ.
Bắt buộc phải đổi thì tạo một file mới có nội dung chuyển hướng, hoặc chấp nhận link cũ hỏng.

### Muốn quay lại phiên bản trước

```bash
git log --oneline          # xem lịch sử
git revert <mã-commit>     # hoàn tác một thay đổi
git push
```

Mọi phiên bản đều được Git lưu lại — bạn không bao giờ mất nội dung cũ.

---

## Gắn tên miền riêng (làm sau này cũng được)

Website chạy tốt trên GitHub Pages mà không cần tên miền riêng. Khi nào muốn dùng `donghanhcungcon.vn` hay `parents.tenmien.vn`:

### Bước 1 — Trỏ DNS

**Tên miền gốc** (`donghanhcungcon.vn`) — thêm 4 bản ghi A:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

**Tên miền con** (`parents.tenmien.vn`) — thêm một bản ghi CNAME:

```
CNAME   parents   TEN-TAI-KHOAN.github.io.
```

> Địa chỉ IP của GitHub Pages có thể thay đổi. Hãy kiểm tra lại tại
> <https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site>

### Bước 2 — Khai báo với GitHub

Repo → Settings → Pages → **Custom domain** → nhập tên miền → Save.
Chờ DNS kiểm tra xong (vài phút đến vài giờ), rồi tích **Enforce HTTPS**.

GitHub sẽ tự tạo file `CNAME` trong repo. Nếu không, tự tạo `public/CNAME` với đúng một dòng:

```
donghanhcungcon.vn
```

### Bước 3 — Sửa cấu hình

Mở `src/config/site.ts`:

```ts
export const DEPLOY = {
  siteUrl: 'https://donghanhcungcon.vn',
  base: '/',                              // ⚠️ đổi về '/'
};
```

Commit, push. Xong.

> ⚠️ **Đừng quên đổi `base` về `'/'`.** Tên miền riêng không có thư mục con.

### Sau khi đổi tên miền, kiểm tra lại

- [ ] `robots.txt` trỏ đúng sitemap mới
- [ ] `rss.xml` chứa link mới
- [ ] Thẻ canonical trong mã nguồn trang là tên miền mới
- [ ] Khai báo lại sitemap trong Google Search Console

Ba mục đầu **tự cập nhật** khi bạn đổi `siteUrl` — không phải sửa tay ở đâu cả.
