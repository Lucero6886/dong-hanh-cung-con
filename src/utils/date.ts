/** Định dạng ngày kiểu Việt Nam: "10 tháng 8, 2026". */
export function formatDate(date: Date): string {
  return new Intl.DateTimeFormat('vi-VN', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
    timeZone: 'UTC',
  }).format(date);
}

/** Dạng ngắn cho thẻ card: "10/08/2026". */
export function formatDateShort(date: Date): string {
  return new Intl.DateTimeFormat('vi-VN', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    timeZone: 'UTC',
  }).format(date);
}

/** Chuỗi ISO cho thuộc tính datetime="" và dữ liệu có cấu trúc Schema.org. */
export function isoDate(date: Date): string {
  return date.toISOString();
}
