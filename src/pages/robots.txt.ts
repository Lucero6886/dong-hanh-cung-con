import type { APIRoute } from 'astro';
import { absoluteUrl } from '../utils/url';

/**
 * robots.txt được sinh khi build để địa chỉ sitemap luôn khớp với cấu hình
 * trong src/config/site.ts — kể cả khi bạn đổi tên miền hoặc đổi base.
 */
export const GET: APIRoute = () => {
  const body = [
    'User-agent: *',
    'Allow: /',
    '',
    `Sitemap: ${absoluteUrl('/sitemap-index.xml')}`,
    '',
  ].join('\n');

  return new Response(body, {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
