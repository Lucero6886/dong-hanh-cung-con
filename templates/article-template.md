---
# =============================================================================
#  MẪU BÀI VIẾT — sao chép file này vào src/content/articles/ rồi sửa
# =============================================================================
#  Cách dùng nhanh:
#    1. Copy file này thành src/content/articles/ten-bai-viet-khong-dau.md
#    2. Sửa phần frontmatter dưới đây (phần giữa hai dấu ---)
#    3. Viết nội dung bên dưới
#    4. Xoá các dòng bắt đầu bằng # (đây chỉ là chú thích hướng dẫn)
#    5. git add . && git commit -m "Bài mới: ..." && git push
#
#  Tên file chính là đường dẫn bài viết:
#    cau-truc-thay-vi-nhac-nho.md  →  /articles/cau-truc-thay-vi-nhac-nho/
#  Nên đặt tên file KHÔNG DẤU, dùng gạch ngang, không dùng khoảng trắng.
#
#  Muốn dùng các hộp <Callout>? Đổi đuôi file thành .mdx (xem docs/CONTENT_GUIDE.md)
# =============================================================================

# --- BẮT BUỘC ----------------------------------------------------------------
title: "Tiêu đề bài viết"
description: "Một hoặc hai câu tóm tắt. Câu này hiện trên thẻ bài viết, trên Google và khi chia sẻ lên Facebook/Zalo."
date: 2026-08-11
category: "Động lực & thói quen"

# --- TUỲ CHỌN (xoá dòng nào không dùng) --------------------------------------
# subtitle: "Tiêu đề phụ, hiện ngay dưới tiêu đề chính"
# updated: 2026-09-01
# author: "Mr. Lucero"          # bỏ trống thì lấy tác giả mặc định trong src/config/site.ts

tags:
  - động lực
  - trách nhiệm

ageGroups:
  - "6–10"
  - "11–14"

featured: false                  # true = hiện ở khối "Bài viết nổi bật" trang chủ
draft: true                      # true = chưa đăng. ĐỔI THÀNH false KHI MUỐN XUẤT BẢN

# coverImage: "/images/articles/ten-anh.webp"
# coverAlt: "Mô tả ảnh cho người dùng trình đọc màn hình"
# readingTime: 8                 # bỏ trống thì hệ thống tự tính

# Bài này bắt nguồn từ đâu:
#   ghi-chep-goc      = biên tập từ ghi chép/trao đổi gốc của bạn
#   bien-tap-mo-rong  = bạn viết mới, mở rộng từ nguyên tắc giáo dục
#   tong-hop          = tổng hợp có dẫn nguồn bên ngoài
sourceType: "bien-tap-mo-rong"

# editorNote: "Ghi chú biên tập hiện ở cuối bài. Nêu rõ phần nào là quan sát cá nhân, phần nào là mở rộng."

# Nguồn tham khảo — CHỈ ghi những gì bạn kiểm chứng được. Không bịa.
# references:
#   - label: "Tên tác giả (năm). Tên bài. Tên tạp chí, tập(số), trang."
#     url: "https://doi.org/..."
#     note: "Ghi chú ngắn về nguồn này"
---

Đoạn mở đầu: nêu tình huống cụ thể mà cha mẹ nhận ra ngay. Hai đến bốn câu, không lý thuyết.

## Vấn đề thật sự nằm ở đâu

Mô tả vấn đề một cách bình tĩnh, không phán xét. Tránh nói "cha mẹ phải…" — ưu tiên "cha mẹ có thể cân nhắc…", "một cách tiếp cận có thể hữu ích là…".

## Giải thích

Vì sao chuyện đó xảy ra. Nếu đây là quan sát cá nhân, hãy nói rõ. Nếu là kết quả nghiên cứu, phải có nguồn ở mục `references` phía trên.

## Ví dụ thực tế

Một hoặc hai tình huống cụ thể. Ví dụ tốt hơn lời khuyên chung chung.

## Điều nên hạn chế

Nêu điều cần tránh mà không làm người đọc thấy có lỗi.

## Điều cha mẹ có thể thử

**1. Việc thứ nhất.**
Mô tả ngắn gọn, cụ thể, làm được ngay.

**2. Việc thứ hai.**
Mô tả ngắn gọn.

## Vài lưu ý theo lứa tuổi

**Khoảng 6–10 tuổi.** …

**Khoảng 11–14 tuổi.** …

## Câu hỏi để suy ngẫm

- Câu hỏi thứ nhất?
- Câu hỏi thứ hai?

## Ý chính

Một đoạn ngắn nhắc lại điều quan trọng nhất của bài.
