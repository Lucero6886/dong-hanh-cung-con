import type { APIRoute } from 'astro';
import { buildSearchIndex } from '../utils/articles';
import { articleUrl } from '../utils/url';
import { formatDateShort } from '../utils/date';

/**
 * Chỉ mục tìm kiếm, sinh sẵn khi build.
 * Trình duyệt tải một lần rồi lọc tại chỗ — không cần máy chủ, không dịch vụ trả phí.
 * Tên trường viết tắt (t, d, u, c, g, b, x, r) để tệp nhẹ nhất có thể.
 */
export const GET: APIRoute = async () => {
  const index = await buildSearchIndex(articleUrl, formatDateShort);

  return new Response(JSON.stringify(index), {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
