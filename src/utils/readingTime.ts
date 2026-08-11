import { SITE } from '../config/site';

/**
 * Ước lượng thời gian đọc (phút) từ nội dung Markdown thô.
 *
 * Được tính TỰ ĐỘNG khi build — bạn không cần điền tay.
 * Nếu muốn ghi đè, thêm `readingTime: 8` vào frontmatter của bài.
 */
export function estimateReadingTime(markdown: string): number {
  const plain = toPlainText(markdown);
  const words = plain.split(/\s+/).filter(Boolean).length;
  return Math.max(1, Math.round(words / SITE.wordsPerMinute));
}

/**
 * Bóc Markdown/MDX về văn bản thuần.
 * Dùng cho: đếm từ, tạo đoạn trích, và xây chỉ mục tìm kiếm.
 */
export function toPlainText(markdown: string): string {
  return markdown
    .replace(/^---[\s\S]*?---/, '')            // frontmatter còn sót
    .replace(/```[\s\S]*?```/g, ' ')           // khối code
    .replace(/`[^`]*`/g, ' ')                  // code inline
    .replace(/<[^>]+>/g, ' ')                  // thẻ HTML / component MDX
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')     // ảnh
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')   // liên kết → giữ chữ
    .replace(/^\s{0,3}#{1,6}\s+/gm, '')        // dấu #
    .replace(/^\s{0,3}>\s?/gm, '')             // trích dẫn
    .replace(/^\s*[-*+]\s+/gm, '')             // gạch đầu dòng
    .replace(/^\s*\d+\.\s+/gm, '')             // danh sách số
    .replace(/[*_~]{1,3}/g, '')                // in đậm / nghiêng
    .replace(/\s+/g, ' ')
    .trim();
}

/** Cắt văn bản theo số ký tự, không cắt giữa từ. */
export function excerpt(text: string, maxChars = 180): string {
  if (text.length <= maxChars) return text;
  const cut = text.slice(0, maxChars);
  const lastSpace = cut.lastIndexOf(' ');
  return `${cut.slice(0, lastSpace > 0 ? lastSpace : maxChars)}…`;
}
