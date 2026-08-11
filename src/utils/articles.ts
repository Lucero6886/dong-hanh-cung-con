/* =============================================================================
 *  LỚP TRUY VẤN BÀI VIẾT
 * =============================================================================
 *  Mọi trang trên website đều lấy dữ liệu qua các hàm ở file này, không gọi
 *  getCollection() trực tiếp. Nhờ vậy quy tắc "ẩn bài nháp", "sắp xếp theo
 *  ngày", "tính thời gian đọc" chỉ tồn tại ở MỘT chỗ duy nhất.
 * ========================================================================== */

import { getCollection, type CollectionEntry } from 'astro:content';
import { SITE } from '../config/site';
import { getCategoryMeta, JOURNEYS, type Journey } from '../config/taxonomy';
import { slugify } from './slugify';
import { estimateReadingTime, toPlainText, excerpt } from './readingTime';

export type Article = CollectionEntry<'articles'>;

/** Bài viết đã được bổ sung các trường tính toán sẵn. */
export interface EnrichedArticle {
  entry: Article;
  slug: string;
  title: string;
  subtitle?: string;
  description: string;
  date: Date;
  updated?: Date;
  author: string;
  category: string;
  categorySlug: string;
  tags: string[];
  tagSlugs: string[];
  ageGroups: string[];
  featured: boolean;
  coverImage?: string;
  coverAlt?: string;
  readingTime: number;
  plainText: string;
  sourceType: 'ghi-chep-goc' | 'bien-tap-mo-rong' | 'tong-hop';
}

function enrich(entry: Article): EnrichedArticle {
  const d = entry.data;
  const plainText = toPlainText(entry.body ?? '');
  return {
    entry,
    slug: entry.id,
    title: d.title,
    subtitle: d.subtitle,
    description: d.description,
    date: d.date,
    updated: d.updated,
    author: d.author ?? SITE.author,
    category: d.category,
    categorySlug: getCategoryMeta(d.category).slug,
    tags: d.tags,
    tagSlugs: d.tags.map(slugify),
    ageGroups: d.ageGroups,
    featured: d.featured,
    coverImage: d.coverImage,
    coverAlt: d.coverAlt,
    readingTime: d.readingTime ?? estimateReadingTime(entry.body ?? ''),
    plainText,
    sourceType: d.sourceType,
  };
}

/**
 * Tất cả bài đã xuất bản, mới nhất trước.
 * Bài `draft: true` bị loại ở mọi môi trường trừ khi chạy `npm run dev`,
 * để bạn vẫn xem thử được bản nháp trên máy mình.
 */
export async function getPublishedArticles(): Promise<EnrichedArticle[]> {
  const showDrafts = import.meta.env.DEV;
  const all = await getCollection('articles', ({ data }) => showDrafts || !data.draft);
  return all.map(enrich).sort((a, b) => b.date.getTime() - a.date.getTime());
}

/** Bài nổi bật cho trang chủ. Thiếu bài nổi bật thì lấy bù bằng bài mới nhất. */
export async function getFeaturedArticles(limit = SITE.featuredLimit): Promise<EnrichedArticle[]> {
  const all = await getPublishedArticles();
  const featured = all.filter((a) => a.featured);
  if (featured.length >= limit) return featured.slice(0, limit);
  const filler = all.filter((a) => !a.featured).slice(0, limit - featured.length);
  return [...featured, ...filler];
}

/* -----------------------------------------------------------------------------
 *  CHỦ ĐỀ & THẺ — được suy ra từ nội dung, không phải từ danh sách cứng
 * -------------------------------------------------------------------------- */

export interface TaxonomyBucket {
  name: string;
  slug: string;
  description: string;
  order: number;
  articles: EnrichedArticle[];
}

export async function getCategoriesWithArticles(): Promise<TaxonomyBucket[]> {
  const all = await getPublishedArticles();
  const map = new Map<string, TaxonomyBucket>();

  for (const a of all) {
    const meta = getCategoryMeta(a.category);
    if (!map.has(meta.slug)) {
      map.set(meta.slug, { ...meta, articles: [] });
    }
    map.get(meta.slug)!.articles.push(a);
  }

  return [...map.values()].sort(
    (x, y) => x.order - y.order || x.name.localeCompare(y.name, 'vi')
  );
}

export async function getTagsWithArticles(): Promise<TaxonomyBucket[]> {
  const all = await getPublishedArticles();
  const map = new Map<string, TaxonomyBucket>();

  for (const a of all) {
    for (const tag of a.tags) {
      const slug = slugify(tag);
      if (!map.has(slug)) {
        map.set(slug, { name: tag, slug, description: '', order: 0, articles: [] });
      }
      map.get(slug)!.articles.push(a);
    }
  }

  return [...map.values()].sort(
    (x, y) => y.articles.length - x.articles.length || x.name.localeCompare(y.name, 'vi')
  );
}

/* -----------------------------------------------------------------------------
 *  HÀNH TRÌNH
 * -------------------------------------------------------------------------- */

export interface JourneyBucket extends Journey {
  articles: EnrichedArticle[];
}

export async function getJourneysWithArticles(): Promise<JourneyBucket[]> {
  const all = await getPublishedArticles();
  return JOURNEYS.map((j) => ({
    ...j,
    articles: all.filter(
      (a) =>
        (j.tags ?? []).some((t) => a.tags.includes(t)) ||
        (j.categories ?? []).includes(a.category)
    ),
  }));
}

/* -----------------------------------------------------------------------------
 *  BÀI LIÊN QUAN
 * -----------------------------------------------------------------------------
 *  Chấm điểm đơn giản, dễ hiểu, không cần thư viện ngoài:
 *    cùng chủ đề        +3
 *    mỗi thẻ trùng      +2
 *    mỗi độ tuổi trùng  +1
 *  Không đủ bài liên quan thì lấy bù bằng bài mới nhất để khối này không trống.
 * -------------------------------------------------------------------------- */

export async function getRelatedArticles(
  current: EnrichedArticle,
  limit = SITE.relatedLimit
): Promise<EnrichedArticle[]> {
  const all = await getPublishedArticles();
  const others = all.filter((a) => a.slug !== current.slug);

  const scored = others
    .map((a) => {
      let score = 0;
      if (a.category === current.category) score += 3;
      score += a.tags.filter((t) => current.tags.includes(t)).length * 2;
      score += a.ageGroups.filter((g) => current.ageGroups.includes(g)).length;
      return { a, score };
    })
    .filter((s) => s.score > 0)
    .sort((x, y) => y.score - x.score || y.a.date.getTime() - x.a.date.getTime())
    .map((s) => s.a);

  if (scored.length >= limit) return scored.slice(0, limit);
  const used = new Set(scored.map((a) => a.slug));
  const filler = others.filter((a) => !used.has(a.slug)).slice(0, limit - scored.length);
  return [...scored, ...filler];
}

/** Bài trước / bài sau theo thứ tự thời gian (dùng cho điều hướng cuối bài). */
export async function getAdjacentArticles(current: EnrichedArticle) {
  const all = await getPublishedArticles(); // mới → cũ
  const i = all.findIndex((a) => a.slug === current.slug);
  return {
    newer: i > 0 ? all[i - 1] : undefined,
    older: i >= 0 && i < all.length - 1 ? all[i + 1] : undefined,
  };
}

/* -----------------------------------------------------------------------------
 *  CHỈ MỤC TÌM KIẾM
 * -------------------------------------------------------------------------- */

export interface SearchRecord {
  t: string;   // title
  d: string;   // description
  u: string;   // url (đã gắn base)
  c: string;   // category
  g: string[]; // tags
  b: string;   // body rút gọn
  x: string;   // ngày hiển thị
  r: number;   // phút đọc
}

export async function buildSearchIndex(
  urlFor: (slug: string) => string,
  dateFmt: (d: Date) => string
): Promise<SearchRecord[]> {
  const all = await getPublishedArticles();
  return all.map((a) => ({
    t: a.title,
    d: a.description,
    u: urlFor(a.slug),
    c: a.category,
    g: a.tags,
    b: excerpt(a.plainText, 1500),
    x: dateFmt(a.date),
    r: a.readingTime,
  }));
}
