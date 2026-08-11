# Quy ước của dự án

Tài liệu này dành cho bất kỳ ai chạm vào mã nguồn — kể cả chính bạn sau sáu tháng không mở dự án.

---

## Nguyên tắc nền tảng

1. **Giữ cho đơn giản.** Người duy trì dự án này là một người, không phải một đội.
2. **Nội dung phải mang đi được.** Một bài viết nên vẫn là Markdown thuần bất cứ khi nào có thể.
3. **Không thêm thư viện nếu chưa thật cần.** Hiện có đúng 3 thư viện phụ thuộc. Muốn thêm cái thứ tư, hãy tự trả lời: *nó tiết kiệm được bao nhiêu dòng code, và sẽ tốn bao nhiêu công khi nâng cấp?*
4. **Không trừu tượng hoá sớm.** Một thứ lặp lại hai lần thì cứ để lặp. Lặp lần thứ ba mới tách ra dùng chung.
5. **Ưu tiên sinh tĩnh.** Không thêm bất cứ thứ gì cần máy chủ chạy liên tục.
6. **Tối ưu cho việc đọc.** Mọi tính năng phải trả lời được: *điều này giúp cha mẹ đọc dễ hơn ở chỗ nào?*
7. **Di động trước.** Phần lớn người đọc dùng điện thoại.
8. **Khả năng tiếp cận là mặc định, không phải tuỳ chọn.**
9. **Nội dung phải sống lâu hơn giao diện.** Đổi giao diện không được đụng tới file bài viết.

---

## Quy ước bắt buộc về kỹ thuật

Ba quy ước dưới đây, vi phạm là hỏng. Chi tiết vì sao nằm ở [`dong-hanh-guide.md`](./dong-hanh-guide.md) Phần 6 và 8.

### 1. Mọi liên kết nội bộ đi qua `withBase()`

```astro
<!-- ĐÚNG -->
<a href={withBase('/articles/')}>Bài viết</a>

<!-- SAI — chạy được ở máy bạn, hỏng trên GitHub Pages -->
<a href="/articles/">Bài viết</a>
```

Kiểm tra: `grep -rn 'href="/' src/ --include=*.astro` — chỉ được trả về link ra ngoài.

### 2. Không viết cứng danh tính vào component

```astro
<!-- ĐÚNG -->
import { SITE } from '../config/site';
<p>{SITE.author}</p>

<!-- SAI -->
<p>Mr. Lucero</p>
```

Kiểm tra: `grep -rn "Mr. Lucero" src/ --include=*.astro` — phải rỗng.

### 3. Không tạo trang riêng cho một bài viết

Bài viết luôn nằm trong `src/content/articles/`. Một bài viết được code tay thành trang `.astro` sẽ vắng mặt khỏi RSS, sitemap, tìm kiếm, trang chủ đề và mục bài liên quan.

---

## Quy ước viết code

**Truy vấn bài viết:** luôn dùng các hàm trong `src/utils/articles.ts`, không gọi `getCollection()` trực tiếp trong trang. Nhờ vậy quy tắc ẩn bài nháp và sắp xếp theo ngày chỉ tồn tại ở một chỗ.

**Chú thích bằng tiếng Việt**, và giải thích *vì sao* chứ không phải *cái gì*:

```ts
// KHÔNG hữu ích: lấy các bài đã xuất bản
// HỮU ÍCH: bài nháp vẫn hiện khi chạy dev để xem thử, nhưng bị loại khi build thật
```

**CSS:** dùng biến trong `:root`, không viết mã màu trực tiếp trong component. Đổi màu chỉ được sửa một chỗ.

**JavaScript:** chỉ thêm khi tắt nó đi mà trang vẫn dùng được. Xem bảng "không có JavaScript thì sao" trong tài liệu đồng hành.

**Thêm trường frontmatter mới:** sửa `src/content.config.ts`, đặt giá trị mặc định để các bài cũ không bị lỗi, rồi ghi vào `docs/CONTENT_GUIDE.md`.

---

## Quy ước biên tập

Giọng văn: **điềm đạm, ấm áp, tôn trọng, thực tế, trung thực về mức độ chắc chắn.**

| Nên | Tránh |
| --- | --- |
| "Cha mẹ có thể cân nhắc…" | "Cha mẹ phải…" |
| "Trong nhiều trường hợp…" | "Luôn luôn…", "Không bao giờ…" |
| "Điều này còn tuỳ từng đứa trẻ" | Ngụ ý có một công thức đúng duy nhất |
| Nêu cả phía phản biện | Trình bày một chiều như đã ngã ngũ |

**Không bao giờ:**

- Chẩn đoán trẻ
- Bịa nguồn, số liệu, nghiên cứu, trích dẫn, đường link
- Dùng nỗi sợ hoặc cảm giác tội lỗi để thuyết phục
- Trình bày suy diễn cá nhân như thể là kết luận khoa học

**Toàn vẹn nguồn:** khi biên tập từ ghi chép gốc, không được âm thầm đổi luận điểm của tác giả. Phân biệt rõ *nội dung gốc* / *mở rộng biên tập* / *nghiên cứu bên ngoài*, và ghi lại trong `sourceType` cùng `editorNote`.

---

## Trước khi commit

```bash
npm run build     # phải chạy xong không lỗi
npm run preview   # xem thử bản thật, không chỉ bản dev
```

Nếu có sửa giao diện, kiểm tra thêm:

- [ ] Xem ở bề rộng 360px — không có thanh cuộn ngang
- [ ] Bấm phím Tab đi hết trang — luôn nhìn thấy phần tử đang được chọn
- [ ] Bật chế độ tối — chữ vẫn đủ tương phản
- [ ] Tắt JavaScript — vẫn đọc được nội dung

---

## Quy ước commit

Viết bằng tiếng Việt, nêu rõ việc đã làm:

```
Bài mới: Cấu trúc thay vì nhắc nhở
Sửa: căn lề mục lục trên màn hình nhỏ
Cấu hình: đổi tên miền sang donghanhcungcon.vn
Tài liệu: bổ sung hướng dẫn gắn tên miền riêng
```

Thay đổi lớn về hệ thống thì ghi thêm một mục vào **Phần 11 — Nhật ký thay đổi** trong [`dong-hanh-guide.md`](./dong-hanh-guide.md).
