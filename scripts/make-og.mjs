#!/usr/bin/env node
/* =============================================================================
 *  TẠO ẢNH XEM TRƯỚC KHI CHIA SẺ (Open Graph, 1200 × 630)
 * =============================================================================
 *  Chạy:  npm run og
 *         npm run og -- --title "Tiêu đề bài" --out public/images/articles/ten.png
 *
 *  Script KHÔNG cần cài thêm thư viện nào. Nó dựng một trang HTML rồi nhờ
 *  trình duyệt Chrome/Chromium có sẵn trên máy chụp lại thành ảnh PNG.
 *
 *  Nếu máy không tự tìm thấy Chrome, chỉ đường dẫn thủ công:
 *      CHROME_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe" npm run og
 *
 *  Không chạy được cũng không sao — website vẫn hoạt động bình thường và dùng
 *  ảnh mặc định có sẵn trong public/social/og-default.png.
 * ========================================================================== */

import { execFileSync } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync, readFileSync, rmSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { tmpdir } from 'node:os';
import { inflateSync, deflateSync } from 'node:zlib';

const W = 1200;
const H = 630;

/* --- Tham số dòng lệnh ----------------------------------------------------- */
const args = process.argv.slice(2);
const arg = (name, fallback) => {
  const i = args.indexOf(`--${name}`);
  return i !== -1 && args[i + 1] ? args[i + 1] : fallback;
};

const title = arg('title', 'Đồng hành cùng con');
const subtitle = arg('subtitle', 'Hiểu con hơn · Đồng hành đúng cách · Cùng con trưởng thành');
const out = resolve(arg('out', 'public/social/og-default.png'));

/* --- Tìm trình duyệt ------------------------------------------------------- */
const CANDIDATES = [
  process.env.CHROME_PATH,
  '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
  '/usr/bin/google-chrome',
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  `${process.env.LOCALAPPDATA ?? ''}\\Google\\Chrome\\Application\\chrome.exe`,
].filter(Boolean);

const chrome = CANDIDATES.find((p) => {
  try {
    return existsSync(p);
  } catch {
    return false;
  }
});

if (!chrome) {
  console.error('✗ Không tìm thấy Chrome/Chromium trên máy này.');
  console.error('  Đặt biến môi trường CHROME_PATH trỏ tới file chrome rồi chạy lại.');
  process.exit(1);
}

const run = (extraArgs, url) =>
  execFileSync(
    chrome,
    ['--headless', '--disable-gpu', '--no-sandbox', '--hide-scrollbars', ...extraArgs, url],
    { stdio: ['ignore', 'pipe', 'ignore'], maxBuffer: 32 * 1024 * 1024 }
  ).toString();

/* -----------------------------------------------------------------------------
 *  BƯỚC 1 — Đo chiều cao khung nhìn thật
 *  Chrome ở chế độ headless vẫn trừ đi phần khung cửa sổ, nên `--window-size`
 *  không bằng đúng vùng vẽ. Ta đo trước để bù lại, thay vì đoán một con số cứng.
 * -------------------------------------------------------------------------- */
const probe = resolve(tmpdir(), `og-probe-${process.pid}.html`);
writeFileSync(
  probe,
  `<!doctype html><meta charset="utf-8"><body><i id="v"></i>
   <script>document.getElementById('v').textContent = innerHeight;</script>`,
  'utf8'
);

let offset = 0;
try {
  const dom = run(['--dump-dom', `--window-size=${W},${H}`], `file://${probe}`);
  const m = dom.match(/<i id="v">(\d+)<\/i>/);
  if (m) offset = Math.max(0, H - Number(m[1]));
} catch {
  /* đo không được thì dùng 0 và cắt ảnh sau */
} finally {
  rmSync(probe, { force: true });
}

/* --- Mẫu ảnh --------------------------------------------------------------- */
const esc = (s) => String(s).replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' })[c]);
const titleSize = title.length > 58 ? 56 : title.length > 40 ? 66 : 78;

const html = `<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:#fbfaf6}
  .frame{
    position:absolute;top:0;left:0;width:${W}px;height:${H}px;
    display:flex;flex-direction:column;justify-content:space-between;
    padding:74px 80px;
    background:
      radial-gradient(ellipse 70% 90% at 88% 6%, #dcebe5 0%, transparent 62%),
      linear-gradient(160deg,#fbfaf6 0%,#efeee6 100%);
    font-family:"Noto Sans","DejaVu Sans","Segoe UI",system-ui,sans-serif;
    color:#1d2b2a;
  }
  .top{display:flex;align-items:center;gap:16px}
  .badge{width:44px;height:44px;border-radius:11px;background:#2e6f60;position:relative;flex:none}
  .badge::after{content:"";position:absolute;left:50%;top:11px;transform:translateX(-50%);
    width:13px;height:13px;border-radius:50%;background:#e0a06f}
  .brand{font-size:23px;font-weight:700;letter-spacing:.02em;color:#1e5348}
  .rule{height:7px;width:132px;background:#b0603a;border-radius:99px;margin-bottom:28px}
  h1{font-size:${titleSize}px;line-height:1.14;letter-spacing:-.028em;max-width:1010px;font-weight:800}
  .sub{font-size:26px;color:#4b5c5a;line-height:1.45;max-width:920px;margin-top:20px}
  .foot{font-size:21px;color:#5b6b69}
</style></head><body>
  <div class="frame">
    <div class="top"><div class="badge"></div><div class="brand">Đồng hành cùng con</div></div>
    <div>
      <div class="rule"></div>
      <h1>${esc(title)}</h1>
      <p class="sub">${esc(subtitle)}</p>
    </div>
    <div class="foot">Thư viện bài viết dành cho cha mẹ</div>
  </div>
</body></html>`;

/* -----------------------------------------------------------------------------
 *  BƯỚC 2 — Chụp ảnh với cửa sổ đã bù chiều cao
 * -------------------------------------------------------------------------- */
const page = resolve(tmpdir(), `og-page-${process.pid}.html`);
writeFileSync(page, html, 'utf8');
mkdirSync(dirname(out), { recursive: true });

try {
  run(
    [
      '--force-device-scale-factor=1',
      `--window-size=${W},${H + offset}`,
      `--screenshot=${out}`,
    ],
    `file://${page}`
  );
} catch (err) {
  console.error('✗ Chụp ảnh thất bại:', err.message);
  process.exit(1);
} finally {
  rmSync(page, { force: true });
}

/* -----------------------------------------------------------------------------
 *  BƯỚC 3 — Cắt ảnh về đúng 1200 × 630
 * -----------------------------------------------------------------------------
 *  Ảnh chụp ra cao hơn do phần bù ở bước 1. Vì ta chỉ cắt bớt các hàng ở PHÍA
 *  DƯỚI, các hàng còn lại không phụ thuộc vào hàng bị bỏ — nên chỉ cần cắt ngắn
 *  dữ liệu điểm ảnh rồi ghi lại, không cần thư viện xử lý ảnh nào.
 * -------------------------------------------------------------------------- */
function crc32(buf) {
  let c;
  const table = crc32.table ?? (crc32.table = Array.from({ length: 256 }, (_, n) => {
    c = n;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    return c >>> 0;
  }));
  let crc = 0xffffffff;
  for (let i = 0; i < buf.length; i++) crc = table[(crc ^ buf[i]) & 0xff] ^ (crc >>> 8);
  return (crc ^ 0xffffffff) >>> 0;
}

function chunk(type, data) {
  const len = Buffer.alloc(4);
  len.writeUInt32BE(data.length);
  const body = Buffer.concat([Buffer.from(type, 'ascii'), data]);
  const crc = Buffer.alloc(4);
  crc.writeUInt32BE(crc32(body));
  return Buffer.concat([len, body, crc]);
}

function cropTop(file, targetH) {
  const png = readFileSync(file);
  const sig = png.subarray(0, 8);

  let pos = 8;
  let ihdr = null;
  const idat = [];
  while (pos < png.length) {
    const len = png.readUInt32BE(pos);
    const type = png.toString('ascii', pos + 4, pos + 8);
    const data = png.subarray(pos + 8, pos + 8 + len);
    if (type === 'IHDR') ihdr = Buffer.from(data);
    else if (type === 'IDAT') idat.push(data);
    else if (type === 'IEND') break;
    pos += 12 + len;
  }
  if (!ihdr) throw new Error('PNG không hợp lệ');

  const width = ihdr.readUInt32BE(0);
  const height = ihdr.readUInt32BE(4);
  const depth = ihdr[8];
  const colorType = ihdr[9];
  const interlace = ihdr[12];
  if (height === targetH) return false;              // đã đúng kích thước
  if (depth !== 8 || interlace !== 0) return false;  // định dạng lạ — bỏ qua, không làm hỏng ảnh

  const channels = { 0: 1, 2: 3, 4: 2, 6: 4 }[colorType];
  if (!channels) return false;

  const stride = width * channels + 1;
  const raw = inflateSync(Buffer.concat(idat));
  const cropped = raw.subarray(0, stride * targetH);

  ihdr.writeUInt32BE(targetH, 4);
  writeFileSync(
    file,
    Buffer.concat([
      sig,
      chunk('IHDR', ihdr),
      chunk('IDAT', deflateSync(cropped, { level: 9 })),
      chunk('IEND', Buffer.alloc(0)),
    ])
  );
  return true;
}

try {
  cropTop(out, H);
} catch (err) {
  console.warn('! Không cắt được ảnh về đúng kích thước:', err.message);
}

console.log(`✓ Đã tạo ảnh ${W}×${H}: ${out}`);
