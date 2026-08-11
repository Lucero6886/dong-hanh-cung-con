/* =============================================================================
 *  MÔ HÌNH DỮ LIỆU BÀI VIẾT (CONTENT COLLECTION)
 * =============================================================================
 *  Đây là "hợp đồng" giữa file Markdown và website.
 *  Mọi bài viết trong src/content/articles/ phải khai báo frontmatter đúng theo
 *  schema bên dưới. Nếu sai, `npm run build` sẽ BÁO LỖI RÕ RÀNG kèm tên file —
 *  đó là chủ ý: thà lỗi lúc build còn hơn đăng lên rồi mới phát hiện.
 *
 *  Muốn thêm một trường mới (ví dụ `series`)? Thêm một dòng vào schema ở đây,
 *  không cần sửa chỗ nào khác.
 * ========================================================================== */

import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
// Astro 7 khuyến nghị nhập z từ 'astro/zod' thay vì từ 'astro:content'.
import { z } from 'astro/zod';

const articles = defineCollection({
  // Bộ nạp quét thư mục — thêm file .md/.mdx là tự động có bài mới.
  loader: glob({ base: './src/content/articles', pattern: '**/*.{md,mdx}' }),

  schema: z.object({
    /* --- BẮT BUỘC ------------------------------------------------------- */

    /** Tiêu đề bài viết. Cũng là thẻ <h1> và <title>. */
    title: z.string().min(1),

    /** Mô tả 1–2 câu. Dùng cho SEO, thẻ card và ảnh xem trước khi chia sẻ. */
    description: z.string().min(1),

    /** Ngày đăng, dạng YYYY-MM-DD. */
    date: z.coerce.date(),

    /** Tên chủ đề — viết đúng như trong src/config/taxonomy.ts, hoặc đặt tên mới. */
    category: z.string().min(1),

    /* --- TUỲ CHỌN ------------------------------------------------------- */

    /** Tiêu đề phụ hiển thị ngay dưới tiêu đề chính. */
    subtitle: z.string().optional(),

    /** Ngày cập nhật gần nhất. Có giá trị → hiển thị "Cập nhật ...". */
    updated: z.coerce.date().optional(),

    /** Bỏ trống → dùng SITE.author trong src/config/site.ts. */
    author: z.string().optional(),

    /** Thẻ giúp người đọc tìm bài liên quan. */
    tags: z.array(z.string()).default([]),

    /** Độ tuổi phù hợp, ví dụ: ["6–10", "11–14"]. */
    ageGroups: z.array(z.string()).default([]),

    /** true → bài xuất hiện ở khối "Bài viết nổi bật" trên trang chủ. */
    featured: z.boolean().default(false),

    /** true → bài KHÔNG được xuất bản (ẩn khỏi mọi trang, RSS và sitemap). */
    draft: z.boolean().default(false),

    /** Ảnh bìa trong public/, ví dụ: "/images/articles/ten-anh.webp". */
    coverImage: z.string().optional(),

    /** Mô tả ảnh bìa cho người dùng trình đọc màn hình. */
    coverAlt: z.string().optional(),

    /** Ghi đè thời gian đọc (phút). Bỏ trống → hệ thống tự tính. */
    readingTime: z.number().int().positive().optional(),

    /**
     * Nguồn tham khảo. Hiển thị ở cuối bài trong mục "Nguồn tham khảo".
     * KHÔNG bịa nguồn — chỉ ghi những gì kiểm chứng được.
     */
    references: z
      .array(
        z.object({
          label: z.string(),
          url: z.url().optional(),
          note: z.string().optional(),
        })
      )
      .default([]),

    /**
     * Ghi rõ bài này bắt nguồn từ đâu — phục vụ nguyên tắc "toàn vẹn nguồn".
     *  - 'ghi-chep-goc'   : biên tập từ ghi chép/trao đổi của chính tác giả
     *  - 'bien-tap-mo-rong': tác giả viết mới, mở rộng từ nguyên tắc giáo dục
     *  - 'tong-hop'       : tổng hợp có dẫn nguồn bên ngoài
     */
    sourceType: z
      .enum(['ghi-chep-goc', 'bien-tap-mo-rong', 'tong-hop'])
      .default('bien-tap-mo-rong'),

    /** Ghi chú biên tập hiển thị ở cuối bài (in nhỏ). */
    editorNote: z.string().optional(),
  }),
});

export const collections = { articles };
