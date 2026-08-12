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
  /**
   * Gốc tên miền, KHÔNG có dấu "/" ở cuối.
   * Tài khoản GitHub: Lucero6886 → địa chỉ luôn viết thường: lucero6886.github.io
   */
  siteUrl: 'https://lucero6886.github.io',

  /** Thư mục con — phải trùng tên repo. Repo tên `dong-hanh-cung-con`. */
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
    'Thư viện bài viết dành cho cha mẹ Việt Nam, đi cùng con từ khi mang thai đến khi con trưởng thành: phát triển não bộ theo từng giai đoạn, động lực, thói quen, giao tiếp, cảm xúc, kỷ luật tích cực và tuổi teen.',

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
 * 2B) THƯƠNG HIỆU ELS — ĐƠN VỊ THỰC HIỆN
 * -----------------------------------------------------------------------------
 *  Website vẫn mang tên "Đồng hành cùng con"; ELS đứng phía sau với vai trò
 *  đơn vị thực hiện. Người đọc là cha mẹ đi tìm nội dung nuôi dạy con — họ tìm
 *  chủ đề trước, thương hiệu sau.
 *
 *  ⚙️  Muốn gỡ toàn bộ thương hiệu khỏi website: đổi `enabled` thành false.
 *      Không phải sửa thêm bất kỳ file nào khác.
 * -------------------------------------------------------------------------- */

export const BRAND = {
  /** false → website trở lại y như trước khi có ELS. */
  enabled: true,

  /** Tên viết tắt, dùng ở những chỗ chật (thanh trên, chú thích ảnh). */
  shortName: 'ELS',

  /** Tên đầy đủ, dùng ở chân trang và trang Giới thiệu. */
  name: "Lucero's English System",

  /** Khẩu hiệu in trên logo. */
  tagline: 'Friendly · Effective · International',

  /**
   * Logo đầy đủ (có hai dòng chữ vòng cung), dạng vector nên nét ở mọi cỡ.
   * Chỉ dùng ở chỗ đủ rộng để đọc được chữ — hiện là trang Giới thiệu.
   * Bản `.png` cùng tên nằm sẵn cạnh đó để dự phòng.
   */
  logo: '/brand/els-logo.svg',

  /**
   * Bản rút gọn: chỉ quả địa cầu và mũ cử nhân, đã bỏ hai dòng chữ.
   * Dùng cho mọi chỗ nhỏ — thanh trên, chân trang, cuối bài, icon tab.
   * Lý do: thu logo đầy đủ xuống 34px thì chữ thành vệt mờ, nhìn như một vết bẩn.
   */
  logoMark: '/brand/els-mark.svg',

  logoAlt: "Logo ELS — Lucero's English System",

  /** Dòng nhỏ dưới tên website ở thanh trên. Để '' nếu không muốn hiện. */
  byline: 'một dự án của ELS',

  /**
   * Đoạn giới thiệu ở chân trang và trang Giới thiệu.
   * ⚠️  Đây là chỗ bạn NÊN đọc lại và sửa cho đúng với thực tế của trung tâm.
   */
  blurb:
    'ELS — Lucero’s English System là nơi tác giả dạy học và làm việc với trẻ mỗi ngày. Nhiều bài viết trên website bắt đầu từ những trao đổi thật với phụ huynh và học sinh trong quá trình đó.',

  /**
   * Trang chính hoặc Facebook của ELS.
   * Để chuỗi rỗng '' → logo hiển thị bình thường nhưng không thành liên kết.
   */
  url: '',
} as const;

/* -----------------------------------------------------------------------------
 * 3) BẢN QUYỀN CHÂN TRANG
 *    {year} sẽ được thay bằng năm hiện tại khi build.
 * -------------------------------------------------------------------------- */

export const COPYRIGHT = {
  holder: "ELS — Lucero's English System",
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
