/**
 * Chuyển chuỗi tiếng Việt có dấu thành slug an toàn cho URL.
 *
 *   "Động lực & thói quen"   →  "dong-luc-thoi-quen"
 *   "Giao tiếp cha mẹ – con"  →  "giao-tiep-cha-me-con"
 *
 * Cách làm: tách dấu bằng NFD rồi xoá các dấu tổ hợp (U+0300–U+036F).
 * Riêng chữ "đ/Đ" không tách được bằng NFD nên phải xử lý riêng.
 */
export function slugify(input: string): string {
  return input
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .replace(/đ/g, 'd')
    .replace(/Đ/g, 'd')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
}
