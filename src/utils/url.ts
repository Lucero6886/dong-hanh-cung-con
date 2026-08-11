import { DEPLOY } from '../config/site';

/**
 * Ghép đường dẫn nội bộ với `base` của site.
 *
 * Vì sao cần hàm này: khi deploy dạng project site, website nằm trong thư mục con
 * (ví dụ /dong-hanh-cung-con/). Nếu viết thẳng href="/articles/" thì link sẽ trỏ
 * ra ngoài gốc tên miền và bị 404.
 *
 * ⚠️ MỌI liên kết nội bộ trong dự án đều phải đi qua hàm này.
 *
 *   withBase('/articles/')  →  '/dong-hanh-cung-con/articles/'   (base = '/dong-hanh-cung-con/')
 *   withBase('/articles/')  →  '/articles/'                      (base = '/')
 */
export function withBase(path = '/'): string {
  const rawBase = import.meta.env.BASE_URL || '/';
  const base = rawBase.endsWith('/') ? rawBase.slice(0, -1) : rawBase;
  const p = path.startsWith('/') ? path : `/${path}`;
  return `${base}${p}`;
}

/** Đường dẫn tuyệt đối (có tên miền) — dùng cho canonical, Open Graph, RSS, sitemap. */
export function absoluteUrl(path = '/'): string {
  return new URL(withBase(path), DEPLOY.siteUrl).href;
}

/** Đường dẫn tới trang một bài viết. */
export function articleUrl(slug: string): string {
  return withBase(`/articles/${slug}/`);
}

/** Đường dẫn tới trang một chủ đề. */
export function categoryUrl(slug: string): string {
  return withBase(`/categories/${slug}/`);
}

/** Đường dẫn tới trang một thẻ. */
export function tagUrl(slug: string): string {
  return withBase(`/tags/${slug}/`);
}

/** Đường dẫn tới trang một hành trình. */
export function journeyUrl(slug: string): string {
  return withBase(`/journeys/${slug}/`);
}

/**
 * Ảnh trong thư mục public/ cũng cần tiền tố base.
 * Đường dẫn bắt đầu bằng http(s):// được giữ nguyên.
 */
export function assetUrl(path: string): string {
  if (/^https?:\/\//i.test(path)) return path;
  return withBase(path);
}
