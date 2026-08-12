#!/usr/bin/env python3
# =============================================================================
#  TẠO BỘ ẢNH THƯƠNG HIỆU ELS TỪ MỘT FILE LOGO DUY NHẤT
# =============================================================================
#  Chỉ cần chạy lại khi ĐỔI LOGO. Ngày thường không phải đụng tới.
#
#  Cách chạy:
#      pip install pillow numpy scipy vtracer cairosvg
#      python3 scripts/make-brand-assets.py <đường-dẫn-file-logo>
#
#  Đầu vào : một file ảnh logo nền trắng (.jpg/.png), càng lớn càng tốt.
#  Đầu ra  : thư mục public/brand/
#      els-logo.svg          logo đầy đủ, vector, nét ở mọi cỡ
#      els-logo.png          bản ảnh 640px dự phòng
#      els-mark.svg / .png   chỉ quả địa cầu + mũ cử nhân (bỏ chữ vòng cung)
#      favicon-32.png        icon tab trình duyệt
#      favicon-192.png       icon khi lưu ra màn hình chính Android
#      apple-touch-icon.png  icon khi lưu ra màn hình chính iPhone/iPad
#
#  VÌ SAO PHẢI CÓ BẢN "MARK" RIÊNG:
#  Logo đầy đủ có hai dòng chữ vòng cung. Thu xuống 32px thì chữ thành vệt mờ
#  và cả logo thành một cục. Bản mark bỏ chữ đi nên ở cỡ nhỏ vẫn nhận ra hình.
#
#  VÌ SAO PHẢI DÒ VECTOR (trace):
#  File gốc là ảnh chụp điểm ảnh — phóng to là vỡ. Bản .svg vẽ lại logo bằng
#  đường cong toán học nên nét ở mọi kích thước, kể cả khi in.
#  ⚠️  Bản .svg này là bản DỰNG LẠI, không phải file gốc của người thiết kế.
#      Rất sát bản gốc, đủ tốt cho website. Nếu in ấn khổ lớn hoặc cần sửa
#      từng nét, hãy xin file .ai gốc từ người đã thiết kế logo.
# =============================================================================

import re
import subprocess
import sys
from pathlib import Path

import cairosvg
import numpy as np
import vtracer
from PIL import Image, ImageFilter
from scipy.ndimage import binary_dilation

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "brand"
TMP = ROOT / ".brand-tmp"

# Bảng màu thương hiệu, đo trực tiếp từ file logo gốc.
WHITE = (255, 255, 255)
BLUE = (28, 74, 152)   # #1C4A98 — quả địa cầu và mũi tên
GOLD = (210, 149, 0)   # #D29500 — mũ cử nhân
RED = (252, 11, 7)     # #FC0B07 — chữ "Lucero's English System" và viền mũ
BLACK = (6, 6, 6)      # #060606 — chữ "Friendly - Effective - International"
PALETTE = [WHITE, BLUE, GOLD, RED, BLACK]


def masks(arr):
    """Tách các mảng màu của logo. Trả về (xanh, vàng, đỏ, đen)."""
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    mx, mn = arr.max(axis=2), arr.min(axis=2)
    sat = mx - mn
    return (
        (b > 60) & (b - r > 35) & (b - g > 20),
        (r > 120) & (g > 80) & (b < 120) & (r - b > 60) & (g - b > 35),
        (r > 110) & (r - g > 40) & (r - b > 40),
        (mx < 140) & (sat < 60),
    )


def square(img: Image.Image, pad_ratio=0.04) -> Image.Image:
    """Đặt ảnh vào giữa một khung vuông trong suốt, chừa lề nhỏ."""
    side = int(max(img.size) * (1 + pad_ratio * 2))
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(img, ((side - img.width) // 2, (side - img.height) // 2), img)
    return canvas


def snap_to_palette(img: Image.Image, scale: int) -> Image.Image:
    """Khử nhiễu JPEG rồi ép mọi điểm ảnh về đúng 5 màu thương hiệu.

    Không làm bước này thì bản vector sinh ra hàng nghìn mảnh vụn từ nhiễu nén,
    file phình to mà nhìn lại xấu hơn.
    """
    img = img.filter(ImageFilter.MedianFilter(3))
    img = img.resize((img.width * scale, img.height * scale), Image.LANCZOS)
    a = np.asarray(img.convert("RGB")).astype(np.int32)
    pal = np.array(PALETTE, dtype=np.int32)
    idx = ((a[:, :, None, :] - pal[None, None, :, :]) ** 2).sum(axis=3).argmin(axis=2)
    return Image.fromarray(pal[idx].astype(np.uint8))


def trace(png_path: Path, svg_path: Path, speckle: int) -> None:
    """Dò ảnh điểm ảnh thành đường cong vector, rồi nén bớt file."""
    vtracer.convert_image_to_svg_py(
        str(png_path), str(svg_path),
        colormode="color", hierarchical="stacked", mode="spline",
        filter_speckle=speckle, color_precision=8, layer_difference=32,
        corner_threshold=60, length_threshold=3.5, max_iterations=12,
        splice_threshold=45, path_precision=2,
    )
    # Nén trước rồi mới bỏ nền: svgo viết lại đường dẫn về dạng gọn và đoán được.
    shrink(svg_path)
    strip_background(svg_path)


def strip_background(svg_path: Path) -> None:
    """Bỏ mảng trắng phủ kín nền để logo đặt được lên nền màu bất kỳ.

    Bộ dò vector luôn vẽ một hình chữ nhật trắng bằng đúng khổ ảnh làm lớp dưới
    cùng. Giữ nó thì logo mang theo một ô trắng, đặt lên nền tối sẽ lộ.
    """
    svg = svg_path.read_text(encoding="utf-8")
    new, n = re.subn(
        r'<path\s+fill="#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})"\s+d="M0 0h\d+v\d+H0z"\s*/>',
        "", svg, count=1,
    )
    if n:
        svg_path.write_text(new, encoding="utf-8")
    else:
        print("    (không thấy lớp nền trắng để bỏ — kiểm tra lại nếu logo có ô trắng)")


def shrink(svg_path: Path) -> None:
    """Chạy svgo để giảm dung lượng. Không có svgo thì bỏ qua, không sao."""
    cfg = TMP / "svgo.config.mjs"
    cfg.write_text(
        "export default {multipass:true,plugins:["
        "{name:'preset-default',params:{overrides:{"
        "convertPathData:{floatPrecision:1,transformPrecision:2},"
        "cleanupNumericValues:{floatPrecision:1},mergePaths:{force:true}}}},"
        "'removeDimensions']};",
        encoding="utf-8",
    )
    before = svg_path.stat().st_size
    r = subprocess.run(
        ["npx", "--yes", "svgo@3", "--config", str(cfg), "-i", str(svg_path), "-o", str(svg_path)],
        capture_output=True, text=True,
    )
    if r.returncode == 0:
        print(f"    svgo: {before // 1024} KB → {svg_path.stat().st_size // 1024} KB")
    else:
        print("    (bỏ qua svgo — không chạy được, file vẫn dùng tốt)")


def png_from_svg(svg_path: Path, out: Path, size: int) -> None:
    cairosvg.svg2png(url=str(svg_path), write_to=str(out),
                     output_width=size, output_height=size)


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Cách dùng: python3 scripts/make-brand-assets.py <file-logo>")
    src = Path(sys.argv[1])
    if not src.exists():
        sys.exit(f"Không tìm thấy file: {src}")

    OUT.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(exist_ok=True)

    im = Image.open(src).convert("RGB")
    arr = np.asarray(im).astype(int)
    h, w = arr.shape[:2]
    ys, xs = np.mgrid[0:h, 0:w]
    blue, gold, red, black = masks(arr)

    # Viền đỏ quanh mũ cử nhân là một phần của hình → giữ.
    # Chữ đỏ vòng cung nằm ngoài vùng đó → bỏ khi làm bản mark.
    near_cap = (xs >= int(w * 0.645)) & (ys <= int(h * 0.49))
    core = blue | gold | (red & near_cap)

    print(f"→ Đọc logo: {src.name} ({w}×{h})")

    # ---- 1. LOGO ĐẦY ĐỦ -----------------------------------------------------
    keep = core | red | black
    yy, xx = np.where(keep)
    pad = 8
    box = (max(int(xx.min()) - pad, 0), max(int(yy.min()) - pad, 0),
           min(int(xx.max()) + pad + 1, w), min(int(yy.max()) + pad + 1, h))
    full = im.crop(box)
    full_sq = Image.new("RGB", (max(full.size),) * 2, WHITE)
    full_sq.paste(full, ((max(full.size) - full.width) // 2,
                         (max(full.size) - full.height) // 2))
    snap_to_palette(full_sq, 3).save(TMP / "full.png")
    print("→ Dò vector logo đầy đủ…")
    trace(TMP / "full.png", OUT / "els-logo.svg", speckle=4)
    png_from_svg(OUT / "els-logo.svg", OUT / "els-logo.png", 640)

    # ---- 2. BẢN MARK: bỏ hai dòng chữ vòng cung -----------------------------
    text = (red & ~near_cap) | black
    erase = binary_dilation(text, iterations=4) & ~core   # chữ + viền mờ của chữ
    clean = arr.copy()
    clean[erase] = 255
    stray = (clean.max(axis=2) < 244) & ~binary_dilation(core, iterations=2)
    clean[stray] = 255                                     # quét nốt vệt lem còn sót

    yy, xx = np.where(core)
    box = (max(int(xx.min()) - pad, 0), max(int(yy.min()) - pad, 0),
           min(int(xx.max()) + pad + 1, w), min(int(yy.max()) + pad + 1, h))
    mark = Image.fromarray(clean.astype(np.uint8)).crop(box)
    mark_sq = Image.new("RGB", (max(mark.size),) * 2, WHITE)
    mark_sq.paste(mark, ((max(mark.size) - mark.width) // 2,
                         (max(mark.size) - mark.height) // 2))
    snap_to_palette(mark_sq, 3).save(TMP / "mark.png")
    print("→ Dò vector bản rút gọn…")
    trace(TMP / "mark.png", OUT / "els-mark.svg", speckle=12)

    png_from_svg(OUT / "els-mark.svg", OUT / "els-mark.png", 256)

    # Icon nhỏ: cắt sát mép hình rồi mới thu nhỏ. Ở cỡ 16–32px, mỗi điểm ảnh
    # lề thừa đều lấy mất phần nhìn thấy được của hình.
    png_from_svg(OUT / "els-mark.svg", TMP / "mark-big.png", 1024)
    tight = Image.open(TMP / "mark-big.png").convert("RGBA")
    tight = tight.crop(tight.getbbox())
    tight = square(tight, pad_ratio=0.015)
    for name, size in [("favicon-32.png", 32), ("favicon-192.png", 192),
                       ("apple-touch-icon.png", 180)]:
        tight.resize((size, size), Image.LANCZOS).save(OUT / name)

    print(f"\n✓ Xong. {len(list(OUT.iterdir()))} file trong public/brand/:")
    for f in sorted(OUT.iterdir()):
        print(f"    {f.name:24s} {f.stat().st_size / 1024:7.1f} KB")


if __name__ == "__main__":
    main()
