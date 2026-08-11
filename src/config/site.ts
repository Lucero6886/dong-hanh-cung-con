/* =============================================================================
 *  CẤU HÌNH TRUNG TÂM CỦA WEBSITE
 * =============================================================================
 *  Đây là file DUY NHẤT bạn cần sửa để thay đổi danh tính website, đường dẫn
 *  triển khai, menu, mạng xã hội và bản quyền.
 *
 *  Không có thông tin nào ở đây bị lặp lại (hard-code) trong các file khác.
 *  Sửa ở đây → toàn bộ website tự cập nhật.
 *
 *  File này cũng được `astro.config.mjs` đọc, nên nó là nguồn sự thật duy nhất
 *  cho cả phần hiển thị lẫn phần build/deploy.
 * ========================================================================== */

/* -----------------------------------------------------------------------------
 * 1) TRIỂN KHAI (DEPLOY) — PHẦN QUAN TRỌNG NHẤT PHẢI SỬA
 * -----------------------------------------------------------------------------
 *  ⚠️  BẮT BUỘC ĐỔI `siteUrl` và `base` trước khi deploy lên GitHub Pages.
 *      Nếu để sai, CSS và toàn bộ liên kết trên site thật sẽ hỏng.
 *
 *  ┌─ Trường hợp A — Project site (đang chọn) ──────────────────────────────┐
 *  │  Repo tên:  dong-hanh-cung-con                                         │
 *  │  Địa chỉ :  https://<username>.github.io/dong-hanh-cung-con/           │
 *  │  siteUrl :  'https://<username>.github.io'                             │
 *  │  base    :  '/dong-hanh-cung-con/'                                     │
 *  └────────────────────────────────────────────────────────────────────────┘
 *
 *  ┌─ Trường hợp B — User site ─────────────────────────────────────────────┐
 *  │  Repo tên:  <username>.github.io                                       │
 *  │  Địa chỉ :  https://<username>.github.io/                              │
 *  │  siteUrl :  'https://<username>.github.io'                             │
 *  │  base    :  '/'                                                        │
 *  └────────────────────────────────────────────────────────────────────────┘
 *
 *  ┌─ Trường hợp C — Tên miền riêng (sau này) ──────────────────────────────┐
 *  │  siteUrl :  'https://donghanhcungcon.vn'                               │
 *  │  base    :  '/'                                                        │
 *  │  (kèm theo file public/CNAME — xem docs/DEPLOYMENT.md)                 │
 *  └────────────────────────────────────────────────────────────────────────┘
 * -------------------------------------------------------------------------- */

export const DEPLOY = {
  /** Gốc tên miền, KHÔNG có dấu "/" ở cuối. ĐỔI "your-username" thành tài khoản GitHub của bạn. */
  siteUrl: 'https://your-username.github.io',

  /** Thư mục con. Project site → '/ten-repo/'. User site hoặc tên miền riêng → '/'. */
  base: '/dong-hanh-cung-con/',
} as const;

/* -----------------------------------------------------------------------------
 * 2) DANH TÍNH WEBSITE
 * -------------------------------------------------------------------------- */

export const SITE = {
  /** Tên đầy đủ, dùng cho thẻ <title> và Open Graph. */
  title: 'Đồng hành cùng con',

  /** Tên ngắn, hiển thị ở logo trên thanh điều hướng. */
  shortTitle: 'Đồng hành cùng con',

  /** Khẩu hiệu ba nhịp của dự án. */
  tagline: 'Hiểu con hơn · Đồng hành đúng cách · Cùng con trưởng thành',

  /** Mô tả mặc định cho SEO (dùng khi trang không có mô tả riêng). */
  description:
    'Thư viện bài viết dành cho cha mẹ Việt Nam về giáo dục trẻ và hành trình đồng hành cùng con: động lực, thói quen, giao tiếp, cảm xúc, kỷ luật tích cực và tuổi teen.',

  /** Tác giả mặc định của bài viết. Có thể ghi đè trong frontmatter từng bài. */
  author: 'Mr. Lucero',

  /** Email liên hệ. Để chuỗi rỗng '' nếu chưa muốn công khai. */
  email: '',

  language: 'vi',
  locale: 'vi_VN',

  /** Số bài hiển thị ở mỗi khối trên trang chủ. */
  featuredLimit: 3,
  latestLimit: 6,
  relatedLimit: 3,

  /** Tốc độ đọc trung bình tiếng Việt (từ/phút) — dùng để ước lượng thời gian đọc. */
  wordsPerMinute: 200,
} as const;

/* -----------------------------------------------------------------------------
 * 3) BẢN QUYỀN CHÂN TRANG
 *    {year} sẽ được thay bằng năm hiện tại khi build.
 * -------------------------------------------------------------------------- */

export const COPYRIGHT = {
  holder: 'Mr. Lucero',
  line: '© {year} {holder} · Đồng hành cùng con',
  note: 'Nội dung giáo dục dành cho cha mẹ. Bảo lưu mọi quyền trừ khi có ghi chú khác.',
  disclaimer:
    'Các bài viết mang tính chia sẻ giáo dục, không thay thế tư vấn y tế, tâm lý hoặc giáo dục chuyên môn dành riêng cho từng trẻ.',
} as const;

/* -----------------------------------------------------------------------------
 * 4) MENU ĐIỀU HƯỚNG
 *    Thêm/bớt dòng ở đây là menu tự đổi. Đường dẫn viết dạng '/xxx/'.
 * -------------------------------------------------------------------------- */

export const NAV: ReadonlyArray<{ label: string; href: string }> = [
  { label: 'Trang chủ', href: '/' },
  { label: 'Bài viết', href: '/articles/' },
  { label: 'Chủ đề', href: '/categories/' },
  { label: 'Hành trình', href: '/journeys/' },
  { label: 'Tìm kiếm', href: '/search/' },
  { label: 'Giới thiệu', href: '/about/' },
];

/* -----------------------------------------------------------------------------
 * 5) MẠNG XÃ HỘI — để mảng rỗng [] nếu chưa có
 * -------------------------------------------------------------------------- */

export const SOCIAL_LINKS: ReadonlyArray<{ label: string; href: string }> = [
  // { label: 'Facebook', href: 'https://facebook.com/...' },
  // { label: 'YouTube',  href: 'https://youtube.com/@...' },
];

/** Tài khoản X/Twitter dạng '@handle' cho thẻ twitter:site. Để '' nếu không có. */
export const TWITTER_HANDLE = '';

/* -----------------------------------------------------------------------------
 * 6) ẢNH XEM TRƯỚC KHI CHIA SẺ (Open Graph)
 *    Ảnh mặc định dùng cho mọi trang chưa có coverImage riêng.
 *    Kích thước chuẩn: 1200 × 630 px.
 * -------------------------------------------------------------------------- */

export const DEFAULT_OG_IMAGE = '/social/og-default.png';
