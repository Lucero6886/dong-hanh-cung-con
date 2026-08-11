/**
 * Nguồn cấp RSS — tự động cập nhật, không cần chỉnh tay khi thêm bài.
 * Địa chỉ sau khi deploy: <site>/rss.xml
 */
import rss from '@astrojs/rss';
import { SITE } from '../config/site';
import { getPublishedArticles } from '../utils/articles';
import { articleUrl, absoluteUrl } from '../utils/url';

export async function GET() {
  const articles = await getPublishedArticles();

  return rss({
    title: SITE.title,
    description: SITE.description,
    // Gồm cả `base`, để <link> của kênh trỏ đúng trang chủ khi deploy dạng project site.
    site: absoluteUrl('/'),
    items: articles.map((a) => ({
      title: a.title,
      description: a.description,
      pubDate: a.date,
      link: articleUrl(a.slug),
      categories: [a.category, ...a.tags],
      author: a.author,
    })),
    customData: `<language>${SITE.locale.replace('_', '-')}</language>`,
  });
}
