# Biến ghi chép thô thành bài viết, có trợ lý AI hỗ trợ

Tài liệu này mô tả quy trình chuyển **ghi chép rời, file Word, bản ghi trao đổi, suy ngẫm cá nhân** thành một bài viết hoàn chỉnh trên website — mà **không đánh mất luận điểm gốc của bạn**.

---

## Nguyên tắc số một

> **Trợ lý AI là biên tập viên, không phải tác giả.**
>
> Nó sắp xếp lại, làm rõ, đề xuất cấu trúc. Nó **không** được đổi điều bạn muốn nói.
> Mọi câu trong bài đăng lên đều là câu bạn đã đọc và đồng ý.

---

## Sơ đồ quy trình

```
        GHI CHÉP THÔ
   (Word, tin nhắn, ghi âm, ghi vội)
              │
              ▼
    ① PHÂN TÍCH NỘI DUNG
    Luận điểm chính là gì? Ý phụ nào? Chỗ nào còn thiếu?
              │
              ▼
    ② TÁCH SỰ KIỆN / QUAN ĐIỂM
    Đâu là nguyên tắc · quan sát cá nhân · khẳng định cần nguồn
              │
              ▼
    ③ DỰNG CẤU TRÚC BÀI
    Đề xuất dàn ý — BẠN DUYỆT trước khi viết
              │
              ▼
    ④ BIÊN TẬP
    Viết thành văn, giữ nguyên luận điểm gốc
              │
              ▼
    ⑤ KIỂM CHỨNG  (chỉ khi bài có khẳng định khoa học)
    Tra nguồn thật. Không tra được → bỏ ý đó hoặc ghi rõ là chưa chắc
              │
              ▼
    ⑥ BÀI VIẾT CHO CHA MẸ
    Giọng điềm đạm, không phán xét, có việc cụ thể để thử
              │
              ▼
    ⑦ XUẤT RA MARKDOWN/MDX
    Kèm frontmatter đầy đủ
              │
              ▼
    ⑧ ĐẨY LÊN GITHUB
    git add . && git commit && git push
              │
              ▼
    ⑨ TỰ ĐỘNG ĐĂNG
    GitHub Actions build và đăng website
```

Bước ①–⑦ làm cùng trợ lý AI. Bước ⑧–⑨ là hai câu lệnh.

---

## Quy tắc toàn vẹn nguồn

Khi chuyển ghi chép của bạn thành bài viết, phải phân biệt rạch ròi ba loại nội dung:

| Loại | Nghĩa là | Xử lý thế nào |
| --- | --- | --- |
| **NỘI DUNG GỐC** | Ý bạn đã viết/đã nói | Giữ nguyên luận điểm. Được sửa câu chữ cho mượt, **không** được đổi ý. |
| **MỞ RỘNG BIÊN TẬP** | Ví dụ, câu hỏi, gợi ý do AI thêm vào | Phải được bạn duyệt. Ghi nhận trong `editorNote`. |
| **NGHIÊN CỨU BÊN NGOÀI** | Số liệu, lý thuyết, trích dẫn | **Bắt buộc** có nguồn kiểm chứng được trong `references`. |

### Không bao giờ được bịa

- Tên bài báo khoa học, tên sách
- Tên tác giả, năm xuất bản
- Con số thống kê
- Lý thuyết tâm lý học
- Câu trích dẫn
- Đường link

**Không kiểm chứng được thì phải nói ra.** Một bài viết trung thực nói "chỗ này tôi chưa chắc" có giá trị hơn một bài viết trơn tru mà bịa nguồn.

---

## Mẫu prompt dùng lại được

Copy nguyên khối dưới đây, dán vào trợ lý AI, kèm ghi chép của bạn.

````text
VAI TRÒ
Bạn là biên tập viên nội dung giáo dục cho một website dành cho cha mẹ Việt Nam
tên là "Đồng hành cùng con". Bạn KHÔNG phải tác giả. Luận điểm là của tôi.

ĐẦU VÀO
[Dán ghi chép thô / nội dung file Word / bản ghi trao đổi ở đây]

QUY TẮC TOÀN VẸN NGUỒN — QUAN TRỌNG NHẤT
1. Không được thay đổi luận điểm cốt lõi của tôi. Nếu bạn thấy luận điểm đó có
   vấn đề, hãy NÓI RA ở phần ghi chú cuối, đừng tự sửa trong bài.
2. Đánh dấu rõ ba loại nội dung:
   [GỐC]     — ý có trong ghi chép của tôi
   [MỞ RỘNG] — ví dụ / câu hỏi / gợi ý bạn thêm vào
   [NGHIÊN CỨU] — khẳng định cần nguồn bên ngoài
3. TUYỆT ĐỐI không bịa: tên nghiên cứu, tác giả, năm, số liệu, trích dẫn, link.
   Không chắc thì ghi "chưa kiểm chứng" và để tôi quyết định.
4. Với mọi khẳng định [NGHIÊN CỨU], nêu cả mức độ tranh cãi nếu có.

GIỌNG ĐIỆU
- Điềm đạm, ấm áp, tôn trọng cha mẹ, thực tế
- Dùng "cha mẹ có thể cân nhắc…" thay vì "cha mẹ phải…"
- Không giật gân, không gây sợ hãi, không làm người đọc thấy có lỗi
- Không nhiều emoji, không khẩu hiệu sáo rỗng
- KHÔNG chẩn đoán trẻ trong bất kỳ trường hợp nào
- Người đọc phải thấy: hiểu vấn đề rõ hơn, có việc cụ thể để thử, không bị phán xét

CẤU TRÚC (bỏ mục nào không phù hợp — không cần ép đủ)
1. Mở đầu ngắn, nêu tình huống cha mẹ nhận ra ngay
2. Ý chính (dùng <Callout type="key">)
3. Vấn đề thật sự nằm ở đâu
4. Giải thích
5. Ví dụ thực tế
6. Điều nên hạn chế (<Callout type="avoid">)
7. Điều cha mẹ có thể thử — đánh số, cụ thể
8. Câu nói mẫu (<Callout type="say">)
9. Lưu ý theo lứa tuổi
10. Câu hỏi suy ngẫm (<Callout type="reflect">)
11. Ý chính khép lại

ĐẦU RA
Một file .mdx hoàn chỉnh, sẵn sàng bỏ vào src/content/articles/, gồm:

- Tên file đề xuất (không dấu, gạch ngang)
- Frontmatter đầy đủ:
  title, description (120–160 ký tự), date, category, tags (3–5),
  ageGroups, featured, draft: true, sourceType, editorNote, references
- Nội dung bài. Trong bài chỉ dùng ## trở xuống, KHÔNG dùng #
- Callout phải có dòng trống trước và sau nội dung bên trong

category chọn trong: Đồng hành cùng con · Động lực & thói quen · Học tập & tự học ·
Giao tiếp cha mẹ – con · Cảm xúc & tâm lý · Kỷ luật tích cực · Tự lập & trách nhiệm ·
Công nghệ & trẻ em · Tuổi teen · Góc suy ngẫm của cha mẹ

SAU BÀI VIẾT, LIỆT KÊ RIÊNG
A. Những chỗ bạn mở rộng thêm ngoài ghi chép của tôi
B. Những khẳng định cần tôi kiểm chứng trước khi đăng
C. Những chỗ bạn thấy luận điểm của tôi có thể gây tranh cãi
````

---

## Prompt cho từng bước riêng lẻ

### ① Phân tích nội dung

```text
Đọc ghi chép sau và trả lời gọn:
1. Luận điểm cốt lõi là gì? (một câu)
2. Có mấy ý phụ? Liệt kê.
3. Chỗ nào lập luận còn thiếu mắt xích?
4. Chỗ nào là quan điểm cá nhân đang được nói như thể là sự thật hiển nhiên?
5. Bài này hợp với chủ đề nào, thẻ nào?
Chưa cần viết bài.

[ghi chép]
```

### ② Tách sự kiện / quan điểm

```text
Chia nội dung sau thành bốn nhóm:
A. Nguyên tắc giáo dục (tương đối ổn định)
B. Quan sát / suy ngẫm cá nhân của tác giả
C. Khẳng định cần dẫn nguồn khoa học
D. Gợi ý thực hành

Riêng nhóm C, ghi rõ: khẳng định đó là gì, và cần loại nguồn nào để chứng minh.

[nội dung]
```

### ③ Dựng cấu trúc — duyệt trước khi viết

```text
Đề xuất dàn ý bài viết từ nội dung này. Chỉ dàn ý, chưa viết.
Mỗi mục ghi: tiêu đề mục + một câu mô tả sẽ nói gì.
Đánh dấu mục nào là [GỐC], mục nào là [MỞ RỘNG].
```

> Đây là bước quan trọng nhất để giữ quyền kiểm soát. **Duyệt dàn ý trước khi cho viết.**

### ⑤ Kiểm chứng

```text
Trong bài dưới đây có các khẳng định mang tính khoa học. Với từng khẳng định:
1. Nêu rõ khẳng định
2. Tra nguồn thật (ưu tiên bài báo có DOI)
3. Nếu tìm được: ghi trích dẫn đầy đủ + link DOI
4. Nếu KHÔNG tìm được: nói thẳng "không kiểm chứng được" và đề xuất
   cách viết lại nhẹ hơn hoặc bỏ ý đó
5. Nếu vấn đề còn tranh cãi trong giới học thuật: nêu cả phía phản biện

Tuyệt đối không bịa nguồn.

[bài viết]
```

### ⑥ Soát giọng văn

```text
Đọc bài sau với vai trò người rà soát giọng điệu. Chỉ ra:
1. Câu nào làm cha mẹ thấy bị phán xét hoặc thấy có lỗi
2. Câu nào khẳng định quá chắc so với cơ sở đang có
3. Câu nào nghe như chẩn đoán trẻ
4. Câu nào là khẩu hiệu sáo rỗng, không có nội dung thực
5. Chỗ nào nên đổi "phải" thành "có thể cân nhắc"

Với mỗi lỗi, đề xuất câu thay thế.
```

---

## Ví dụ có thật trong dự án này

Bài [`tu-phan-thuong-den-dong-luc-ben-trong.mdx`](../src/content/articles/tu-phan-thuong-den-dong-luc-ben-trong.mdx) đi đúng quy trình trên:

| Bước | Việc đã làm |
| --- | --- |
| Đầu vào | Một file Word ghi lại trao đổi về động lực bên trong / bên ngoài |
| ① ② | Xác định luận điểm gốc: *thưởng không sai, vấn đề là thông điệp trẻ hình thành* |
| ③ ④ | Giữ nguyên toàn bộ luận điểm, kể cả ý "trẻ không phải người lớn thu nhỏ" |
| ⑤ | Tra thật hai nghiên cứu (Lepper 1973; Deci, Koestner & Ryan 1999) — **và tra cả phía phản biện** (Cameron & Pierce 1994; Eisenberger & Cameron 1996), rồi ghi rõ trong bài rằng đây là vấn đề còn tranh luận |
| ⑥ | Thêm gợi ý theo lứa tuổi và câu hỏi suy ngẫm — ghi rõ là phần mở rộng |
| ⑦ | `sourceType: "ghi-chep-goc"`, `editorNote` nêu rõ phần nào là mở rộng |

Kết quả: luận điểm của tác giả được giữ nguyên, phần khoa học có nguồn thật, và người đọc biết chỗ nào chưa ngã ngũ.

---

## Danh sách kiểm tra sau khi AI trả bài

Trước khi đổi `draft: false`:

- [ ] Tôi đã **đọc hết** bài, không chỉ lướt
- [ ] Luận điểm gốc của tôi còn nguyên, không bị làm nhẹ đi hay bẻ hướng
- [ ] Mọi phần [MỞ RỘNG] tôi đều đồng ý
- [ ] Mọi con số / nghiên cứu / trích dẫn tôi đã **tự kiểm tra link**
- [ ] Không có nguồn nào tôi không mở được
- [ ] Không có câu nào mang tính chẩn đoán trẻ
- [ ] Giọng văn không làm người đọc thấy có lỗi
- [ ] `sourceType` và `editorNote` phản ánh đúng nguồn gốc bài
- [ ] `npm run build` chạy không lỗi

> Nếu chỉ làm được **một** việc trong danh sách này, hãy làm việc thứ tư: **tự mở từng link nguồn.** Đó là chỗ dễ sai nhất và cũng là chỗ tổn hại uy tín nhất.
