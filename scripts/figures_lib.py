# =============================================================================
#  THƯ VIỆN DỰNG HÌNH MINH HOẠ — dùng chung cho toàn website
# =============================================================================
#  File này KHÔNG tự chạy. Nó là bộ khuôn để `make-figures.py` gọi tới.
#
#  Ba thứ nó giữ cho cả website nhất quán:
#    1. Bảng màu   — đã kiểm định bằng công cụ đo, kể cả cho người mù màu
#    2. Cỡ chữ     — một thang duy nhất, không mỗi hình một kiểu
#    3. Khuôn hình — 8 dạng biểu đồ/sơ đồ, mọi hình đều dựng từ đó
#
#  ⚠️  VÌ SAO HÌNH LUÔN CÓ NỀN SÁNG, KỂ CẢ Ở CHẾ ĐỘ TỐI:
#  Hình được lưu thành file ảnh riêng, nên nó KHÔNG đọc được website đang ở
#  chế độ sáng hay tối. Nếu để nền trong suốt, chữ đen sẽ biến mất trên nền tối.
#  Nên mỗi hình tự mang một "tấm thẻ" nền sáng của riêng nó — ở chế độ tối,
#  nó hiện ra như một tấm thẻ sáng đặt trên trang tối. Đây là chủ ý, không phải lỗi.
# =============================================================================

from __future__ import annotations
import html
import re

# ── 1. MÀU ────────────────────────────────────────────────────────────────────
# Ba màu dữ liệu dưới đây đã chạy qua bộ kiểm tra của quy chuẩn trực quan hoá
# (dải sáng, độ bão hoà, khoảng cách khi mô phỏng mù màu, độ tương phản với nền)
# và ĐẠT toàn bộ. Đừng đổi lẻ một màu — đổi thì phải chạy lại bộ kiểm tra.
SURFACE = "#faf8f3"   # nền tấm thẻ
BORDER  = "#e6e0d4"
INK     = "#1d2b2a"   # chữ chính
INK_2   = "#4a5a58"   # chữ phụ
MUTED   = "#7d8a88"   # chú thích
GRID    = "#eae4d8"   # lưới, trục — luôn mờ hơn dữ liệu

TEAL = "#1e8163"      # ô 1 — lấy từ màu xanh lá của website
BLUE = "#3f6bbf"      # ô 2 — lấy từ màu xanh dương của logo ELS
CLAY = "#b04c26"      # ô 3 — lấy từ màu nâu đất phụ của website
GRAY = "#c9c3b7"      # màu "làm mờ đi" khi muốn nhấn một cột duy nhất

# Tối đa 3 màu dữ liệu trên một hình. Cần nhiều hơn → gộp lại hoặc tách hình.
SERIES = [TEAL, BLUE, CLAY]

# ── 2. CHỮ ────────────────────────────────────────────────────────────────────
# Hình .svg do TRÌNH DUYỆT vẽ chữ, nên dùng đúng bộ font của website.
FONT = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Roboto, "
        "'Helvetica Neue', Arial, sans-serif")
# Ảnh bìa .png do máy chủ vẽ sẵn, nên phải gọi tên font có thật trên máy.
FONT_PNG = "Inter Display, Inter, DejaVu Sans, sans-serif"

T_TITLE = 19   # tiêu đề hình
T_BODY  = 15   # nhãn chính
T_SMALL = 13   # nhãn phụ, số liệu
T_TINY  = 11.5 # chú thích nguồn


# ── 3. TIỆN ÍCH ───────────────────────────────────────────────────────────────
def esc(s: str) -> str:
    return html.escape(str(s), quote=False)


def num(v) -> str:
    """Số kiểu Việt Nam: dấu phẩy làm dấu thập phân. 28.7 → 28,7

    Dấu trừ dùng ký tự ASCII, không dùng ký tự toán học U+2212 — vài phông
    thiếu ký tự đó và sẽ hiện thành ô vuông.
    """
    return f"{v:g}".replace(".", ",")


# Bề rộng trung bình một ký tự so với cỡ chữ. Dùng để ngắt dòng cho vừa khung.
# Dấu tiếng Việt nằm trên/dưới nên không làm chữ rộng thêm.
# Hai hệ số này được HIỆU CHUẨN bằng cách đo bề rộng chữ thật trong trình duyệt.
# Ước lượng cũ hụt khoảng 11–15% nên chữ tràn ra ngoài mép thẻ.
_W_REG, _W_BOLD = 0.594, 0.632


def text_w(s: str, size: float, bold: bool = False) -> float:
    """Ước lượng bề rộng một chuỗi. Đủ chính xác để ngắt dòng."""
    narrow = sum(1 for c in s if c in "iíìỉĩịjltrfIÍÌỈĨỊ.,:;'!|()[] ")
    wide = sum(1 for c in s if c in "mwMWĂÂÊÔƠƯĐ—@%")
    base = (_W_BOLD if bold else _W_REG) * size
    return len(s) * base - narrow * base * 0.42 + wide * base * 0.30


def wrap(s: str, size: float, max_w: float, bold: bool = False) -> list[str]:
    """Ngắt chuỗi thành nhiều dòng sao cho mỗi dòng không vượt quá max_w."""
    words, lines, cur = s.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if text_w(trial, size, bold) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def tspan(x, y, s, size=T_BODY, fill=INK, weight="400", anchor="start",
          font=None, opacity=None):
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{font or FONT}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{o}>{esc(s)}</text>')


def multiline(x, y, lines, size, fill=INK, weight="400", lh=1.32,
              anchor="start", font=None):
    return "".join(
        tspan(x, y + i * size * lh, ln, size, fill, weight, anchor, font)
        for i, ln in enumerate(lines)
    )


def rrect(x, y, w, h, r, fill, extra=""):
    w = max(w, 0.01)
    r = min(r, w / 2, h / 2)
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r:.1f}" fill="{fill}"{extra}/>'


def bar_rounded_end(x, y, w, h, r, fill, horizontal=True):
    """Cột có ĐẦU DỮ LIỆU bo tròn, chân neo phẳng vào trục — theo quy chuẩn.

    Vẽ bằng path để chỉ bo hai góc ở đầu, không bo góc ở chân.
    """
    w = max(w, 0.6)
    r = min(r, w / 2 if horizontal else h / 2, h / 2 if horizontal else w / 2)
    if horizontal:
        d = (f"M{x:.1f},{y:.1f} H{x+w-r:.1f} Q{x+w:.1f},{y:.1f} {x+w:.1f},{y+r:.1f} "
             f"V{y+h-r:.1f} Q{x+w:.1f},{y+h:.1f} {x+w-r:.1f},{y+h:.1f} H{x:.1f} Z")
    else:  # cột dọc, đầu ở phía trên
        d = (f"M{x:.1f},{y+h:.1f} V{y+r:.1f} Q{x:.1f},{y:.1f} {x+r:.1f},{y:.1f} "
             f"H{x+w-r:.1f} Q{x+w:.1f},{y:.1f} {x+w:.1f},{y+r:.1f} V{y+h:.1f} Z")
    return f'<path d="{d}" fill="{fill}"/>'


# ── 4. KHUNG HÌNH ─────────────────────────────────────────────────────────────
PAD = 26          # lề trong tấm thẻ
TITLE_GAP = 30    # khoảng dưới tiêu đề


def frame(width, height, title, body, note=None, subtitle=None):
    """Bọc phần thân vào một tấm thẻ có nền, viền, tiêu đề và dòng nguồn."""
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img">',
        f'<rect width="{width}" height="{height}" rx="14" fill="{SURFACE}"/>',
        f'<rect x="0.75" y="0.75" width="{width-1.5}" height="{height-1.5}" rx="13.25" '
        f'fill="none" stroke="{BORDER}" stroke-width="1.5"/>',
    ]
    if title:
        parts.append(tspan(PAD, PAD + T_TITLE * 0.82, title, T_TITLE, INK, "700"))
    if subtitle:
        parts.append(tspan(PAD, PAD + T_TITLE * 0.82 + 20, subtitle, T_SMALL, MUTED))
    parts.append(body)
    if note:
        lns = note_lines(note, width)
        for i, ln in enumerate(lns):
            parts.append(tspan(PAD, height - PAD - (len(lns) - 1 - i) * 16 + 2,
                               ln, T_TINY, MUTED))
    parts.append("</svg>")
    return "".join(parts)


NOTE_W_SAFETY = 20   # trừ hao vì bề rộng chữ chỉ là ước lượng


def note_lines(note, width):
    return wrap(note, T_TINY, width - PAD * 2 - NOTE_W_SAFETY) if note else []


def note_h(note, width):
    """Chỗ cần chừa ở đáy thẻ cho dòng ghi chú. Tính theo số dòng thật."""
    n = len(note_lines(note, width))
    return 0 if n == 0 else 14 + n * 16


def head_h(title, subtitle=None):
    """Chiều cao phần tiêu đề, để phần thân biết bắt đầu từ đâu."""
    h = PAD + T_TITLE * 0.82 + TITLE_GAP if title else PAD
    if subtitle:
        h += 20
    return h


# =============================================================================
#  BẢY KHUÔN HÌNH
# =============================================================================
#  Mọi hình trên website đều dựng từ một trong bảy khuôn này. Muốn thêm hình mới
#  thì khai báo dữ liệu rồi gọi khuôn, KHÔNG vẽ tay từng hình.
#
#  Chọn khuôn theo VIỆC mà người đọc phải làm:
#    so sánh độ lớn ................ bar_h
#    một cột là điểm nhấn .......... bar_h(emphasis=…)
#    vị trí trên một thang ......... dot_scale
#    trên/dưới một mốc ............. diverging
#    tụt dần qua từng bước ......... steps_down
#    khoảng dao động ............... range_bar
#    các bậc theo thứ tự ........... ladder
#    hai bên đối lập ............... two_col
#    chuỗi việc nối tiếp ........... flow
# =============================================================================

W = 720  # bề rộng chuẩn của mọi hình


def bar_h(title, rows, note=None, subtitle=None, label_w=210, emphasis=None,
          unit="", width=W, color=TEAL, show_axis=True):
    """Cột ngang. rows = [(nhãn, giá trị, ghi_chú_hoặc_None), …]

    emphasis = chỉ số dòng cần nhấn; các dòng còn lại tô xám.
    """
    top = head_h(title, subtitle)
    row_h, gap = 34, 12
    body_h = len(rows) * row_h + (len(rows) - 1) * gap
    height = top + body_h + PAD + note_h(note, width)
    x0 = PAD + label_w
    # Dành sẵn đúng bề rộng mà nhãn số cần, để không bao giờ tràn ra ngoài thẻ.
    val_w = max(text_w(r[2] if r[2] is not None else f"{num(r[1])}{unit}",
                       T_SMALL, True) for r in rows) + 18
    plot_w = width - x0 - PAD - val_w
    vmax = max(abs(r[1]) for r in rows) or 1
    p = []
    if show_axis:
        p.append(f'<line x1="{x0}" y1="{top-8}" x2="{x0}" y2="{top+body_h+4}" '
                 f'stroke="{GRID}" stroke-width="1.5"/>')
    for i, (lab, val, sub) in enumerate(rows):
        y = top + i * (row_h + gap)
        c = color if (emphasis is None or i == emphasis) else GRAY
        bw = plot_w * abs(val) / vmax
        p.append(bar_rounded_end(x0 + 2, y + 4, bw, row_h - 8, 4, c))
        lines = wrap(lab, T_BODY, label_w - 14)
        ly = y + row_h / 2 - (len(lines) - 1) * T_BODY * 0.66 + T_BODY * 0.36
        weight = "700" if (emphasis is not None and i == emphasis) else "400"
        p.append(multiline(x0 - 12, ly, lines, T_BODY, INK, weight, anchor="end"))
        p.append(tspan(x0 + bw + 10, y + row_h / 2 + T_SMALL * 0.36,
                       f"{num(val)}{unit}" if sub is None else sub,
                       T_SMALL, INK_2, "700"))
    return frame(width, round(height), title, "".join(p), note, subtitle)


def dot_scale(title, points, xmin, xmax, ticks, note=None, subtitle=None,
              xlabel="", width=W, marks=None):
    """Các điểm trên một thang ngang. points = [(nhãn, giá trị, màu), …]

    marks = [(giá trị, nhãn)] — vạch tham chiếu vẽ mờ phía sau.
    """
    top = head_h(title, subtitle)
    row_h = 40
    lab_w = 236
    val_w = max(text_w(num(v), T_SMALL, True) for _, v, _ in points) + 26
    x0, x1 = PAD + lab_w, width - PAD - val_w
    body_h = len(points) * row_h
    height = top + body_h + 46 + PAD + note_h(note, width)

    def sx(v):
        return x0 + (x1 - x0) * (v - xmin) / (xmax - xmin)

    p = []
    for m, ml in (marks or []):
        p.append(f'<line x1="{sx(m):.1f}" y1="{top-10}" x2="{sx(m):.1f}" y2="{top+body_h+6}" '
                 f'stroke="{CLAY}" stroke-width="1.5" stroke-dasharray="4 4" opacity="0.55"/>')
        p.append(tspan(sx(m), top - 16, ml, T_TINY, CLAY, "700", "middle"))
    for t in ticks:
        p.append(f'<line x1="{sx(t):.1f}" y1="{top-2}" x2="{sx(t):.1f}" y2="{top+body_h+6}" '
                 f'stroke="{GRID}" stroke-width="1"/>')
        p.append(tspan(sx(t), top + body_h + 24, str(t), T_SMALL, MUTED, "400", "middle"))
    if xlabel:
        p.append(tspan((x0 + x1) / 2, top + body_h + 42, xlabel, T_TINY, MUTED, "400", "middle"))
    for i, (lab, val, col) in enumerate(points):
        y = top + i * row_h + row_h / 2
        p.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{sx(val):.1f}" y2="{y:.1f}" '
                 f'stroke="{col}" stroke-width="2" opacity="0.32"/>')
        p.append(f'<circle cx="{sx(val):.1f}" cy="{y:.1f}" r="6.5" fill="{col}" '
                 f'stroke="{SURFACE}" stroke-width="2"/>')
        lines = wrap(lab, T_BODY, lab_w - 14)
        ly = y - (len(lines) - 1) * T_BODY * 0.66 + T_BODY * 0.36
        p.append(multiline(x0 - 12, ly, lines, T_BODY, INK, "400", anchor="end"))
        p.append(tspan(sx(val) + 13, y + T_SMALL * 0.36, num(val), T_SMALL, INK_2, "700"))
    return frame(width, round(height), title, "".join(p), note, subtitle)


def diverging(title, rows, note=None, subtitle=None, label_w=250, width=W,
              pos_color=TEAL, neg_color=CLAY, unit=""):
    """Cột hai chiều quanh một mốc 0. rows = [(nhãn, giá trị, ghi_chú), …]"""
    top = head_h(title, subtitle)
    row_h, gap = 36, 12
    body_h = len(rows) * row_h + (len(rows) - 1) * gap
    height = top + body_h + 26 + PAD + note_h(note, width)
    x0 = PAD + label_w
    val_w = max(text_w(r[2] or f"{num(r[1])}{unit}", T_SMALL, True) for r in rows) + 16
    half = (width - x0 - PAD - val_w) / 2
    zx = x0 + half
    vmax = max(abs(r[1]) for r in rows) or 1
    p = [f'<line x1="{zx:.1f}" y1="{top-8}" x2="{zx:.1f}" y2="{top+body_h+6}" '
         f'stroke="{INK_2}" stroke-width="1.5"/>',
         tspan(zx, top + body_h + 22, "0", T_SMALL, MUTED, "400", "middle")]
    for i, (lab, val, sub) in enumerate(rows):
        y = top + i * (row_h + gap)
        bw = (half - 26) * abs(val) / vmax
        if val >= 0:
            p.append(bar_rounded_end(zx + 1.5, y + 5, bw, row_h - 10, 4, pos_color))
            tx, anc = width - PAD, "end"
        else:
            d = (f"M{zx-1.5-bw+4:.1f},{y+5:.1f} H{zx-1.5:.1f} V{y+row_h-5:.1f} "
                 f"H{zx-1.5-bw+4:.1f} Q{zx-1.5-bw:.1f},{y+row_h-5:.1f} {zx-1.5-bw:.1f},{y+row_h-9:.1f} "
                 f"V{y+9:.1f} Q{zx-1.5-bw:.1f},{y+5:.1f} {zx-1.5-bw+4:.1f},{y+5:.1f} Z")
            p.append(f'<path d="{d}" fill="{neg_color}"/>')
            tx, anc = width - PAD, "end"
        lines = wrap(lab, T_BODY, label_w - 14)
        ly = y + row_h / 2 - (len(lines) - 1) * T_BODY * 0.66 + T_BODY * 0.36
        p.append(multiline(x0 - 12, ly, lines, T_BODY, INK, "400", anchor="end"))
        p.append(tspan(tx, y + row_h / 2 + T_SMALL * 0.36, sub or f"{num(val)}{unit}",
                       T_SMALL, INK_2, "700", anc))
    return frame(width, round(height), title, "".join(p), note, subtitle)


def steps_down(title, steps, note=None, subtitle=None, width=W, color=TEAL):
    """Cột tụt dần qua từng bước. steps = [(nhãn nhiều dòng, giá trị 0–1, chú), …]"""
    top = head_h(title, subtitle)
    n = len(steps)
    gap = 16
    cw = (width - PAD * 2 - gap * (n - 1)) / n
    plot_h = 138
    lab_h = 74
    height = top + plot_h + 30 + lab_h + PAD + note_h(note, width)
    base = top + plot_h
    p = [f'<line x1="{PAD}" y1="{base+1}" x2="{width-PAD}" y2="{base+1}" '
         f'stroke="{GRID}" stroke-width="1.5"/>']
    for i, (lab, frac, sub) in enumerate(steps):
        x = PAD + i * (cw + gap)
        h = max(plot_h * frac, 3)
        c = color if frac > 0.02 else GRAY
        p.append(bar_rounded_end(x, base - h, cw, h, 5, c, horizontal=False))
        p.append(tspan(x + cw / 2, base - h - 10, sub, T_SMALL, INK_2, "700", "middle"))
        for j, ln in enumerate(wrap(lab, T_SMALL, cw + 6)[:4]):
            p.append(tspan(x + cw / 2, base + 26 + j * 17, ln, T_SMALL, INK_2, "400", "middle"))
        p.append(tspan(x + cw / 2, base + 20, f"{i+1}", T_TINY, MUTED, "700", "middle"))
        if i < n - 1:
            ax = x + cw + gap / 2
            p.append(f'<path d="M{ax-4:.1f},{base+8:.1f} l4,5 l4,-5" fill="none" '
                     f'stroke="{MUTED}" stroke-width="1.5" stroke-linecap="round" '
                     f'stroke-linejoin="round"/>')
    return frame(width, round(height), title, "".join(p), note, subtitle)


def range_bar(title, rows, xmin, xmax, ticks, note=None, subtitle=None,
              xlabel="", width=W, label_w=180):
    """Khoảng dao động. rows = [(nhãn, min, mốc_giữa|None, max, màu, chú), …]"""
    top = head_h(title, subtitle)
    row_h = 46
    val_w = max([text_w(r[5], T_SMALL, True) for r in rows if r[5]] or [0]) + 16
    x0, x1 = PAD + label_w, width - PAD - val_w
    body_h = len(rows) * row_h
    height = top + body_h + 46 + PAD + note_h(note, width)

    def sx(v):
        return x0 + (x1 - x0) * (v - xmin) / (xmax - xmin)

    p = []
    for t in ticks:
        p.append(f'<line x1="{sx(t):.1f}" y1="{top-4}" x2="{sx(t):.1f}" y2="{top+body_h+4}" '
                 f'stroke="{GRID}" stroke-width="1"/>')
        p.append(tspan(sx(t), top + body_h + 24, str(t), T_SMALL, MUTED, "400", "middle"))
    if xlabel:
        p.append(tspan((x0 + x1) / 2, top + body_h + 42, xlabel, T_TINY, MUTED, "400", "middle"))
    for i, (lab, lo, mid, hi, col, sub) in enumerate(rows):
        y = top + i * row_h + row_h / 2
        if hi - lo > (xmax - xmin) * 0.006:
            p.append(rrect(sx(lo), y - 7, sx(hi) - sx(lo), 14, 7, col, ' opacity="0.30"'))
        else:  # chỉ một điểm — vẽ thành một vạch rõ, không phải sợi chỉ
            p.append(f'<circle cx="{sx(lo):.1f}" cy="{y:.1f}" r="7" fill="{col}" opacity="0.30"/>')
        p.append(f'<line x1="{sx(lo):.1f}" y1="{y-9:.1f}" x2="{sx(lo):.1f}" y2="{y+9:.1f}" '
                 f'stroke="{col}" stroke-width="2.5" stroke-linecap="round"/>')
        p.append(f'<line x1="{sx(hi):.1f}" y1="{y-9:.1f}" x2="{sx(hi):.1f}" y2="{y+9:.1f}" '
                 f'stroke="{col}" stroke-width="2.5" stroke-linecap="round"/>')
        if mid is not None:
            p.append(f'<circle cx="{sx(mid):.1f}" cy="{y:.1f}" r="6.5" fill="{col}" '
                     f'stroke="{SURFACE}" stroke-width="2"/>')
        lines = wrap(lab, T_BODY, label_w - 14)
        ly = y - (len(lines) - 1) * T_BODY * 0.66 + T_BODY * 0.36
        p.append(multiline(x0 - 12, ly, lines, T_BODY, INK, "400", anchor="end"))
        if sub:
            p.append(tspan(width - PAD, y + T_SMALL * 0.36, sub, T_SMALL, INK_2, "700", "end"))
    return frame(width, round(height), title, "".join(p), note, subtitle)


def ladder(title, rungs, note=None, subtitle=None, width=W, highlight=0):
    """Các bậc theo thứ tự. rungs = [(bậc, tên, ví dụ), …] — bậc 1 ở trên cùng."""
    top = head_h(title, subtitle)
    rh, gap = 52, 9
    body_h = len(rungs) * rh + (len(rungs) - 1) * gap
    height = top + body_h + PAD + note_h(note, width)
    p = []
    for i, (num, name, ex) in enumerate(rungs):
        y = top + i * (rh + gap)
        on = (i == highlight)
        fill = TEAL if on else SURFACE
        p.append(rrect(PAD, y, width - PAD * 2, rh, 10, fill,
                       f' stroke="{TEAL if on else BORDER}" stroke-width="{2 if on else 1.5}"'
                       + ("" if on else "")))
        # số bậc
        p.append(f'<circle cx="{PAD+27}" cy="{y+rh/2:.1f}" r="15" '
                 f'fill="{SURFACE if on else TEAL}" opacity="{1 if on else 0.10}"/>')
        p.append(tspan(PAD + 27, y + rh / 2 + 5.5, str(num), T_BODY,
                       TEAL if on else TEAL, "700", "middle"))
        p.append(tspan(PAD + 54, y + rh / 2 + 5.5, name, T_BODY,
                       SURFACE if on else INK, "700"))
        nx = PAD + 54 + text_w(name, T_BODY, True) + 16
        p.append(tspan(nx, y + rh / 2 + 5, ex, T_SMALL,
                       SURFACE if on else MUTED, "400"))
        if on:
            p.append(tspan(width - PAD - 14, y + rh / 2 + 5, "bắt đầu ở đây", T_TINY,
                           SURFACE, "700", "end"))
    return frame(width, round(height), title, "".join(p), note, subtitle)


def two_col(title, left, right, note=None, subtitle=None, width=W):
    """Hai cột đối lập. left/right = (tiêu đề cột, màu, [mục, …])"""
    top = head_h(title, subtitle)
    cw = (width - PAD * 2 - 18) / 2
    n = max(len(left[2]), len(right[2]))
    item_h = 0
    cols = []
    for (ct, col, items) in (left, right):
        wrapped = [wrap(it, T_SMALL, cw - 34) for it in items]
        cols.append((ct, col, wrapped))
        item_h = max(item_h, sum(len(w) for w in wrapped))
    body_h = 44 + item_h * 19 + n * 12 + 16
    height = top + body_h + PAD + note_h(note, width)
    p = []
    for k, (ct, col, wrapped) in enumerate(cols):
        x = PAD + k * (cw + 18)
        p.append(rrect(x, top, cw, body_h, 12, col, ' opacity="0.07"'))
        p.append(f'<rect x="{x:.1f}" y="{top}" width="{cw:.1f}" height="4" rx="2" fill="{col}"/>')
        p.append(tspan(x + 16, top + 32, ct, T_BODY, col, "700"))
        yy = top + 58
        for wlines in wrapped:
            p.append(f'<circle cx="{x+21:.1f}" cy="{yy-4.5:.1f}" r="3.2" fill="{col}"/>')
            p.append(multiline(x + 32, yy, wlines, T_SMALL, INK_2, "400", lh=1.30))
            yy += len(wlines) * 19 + 12
    return frame(width, round(height), title, "".join(p), note, subtitle)


def flow(title, steps, note=None, subtitle=None, width=W, color=TEAL):
    """Chuỗi việc nối tiếp bằng mũi tên. steps = [(nhãn, mô tả), …]"""
    top = head_h(title, subtitle)
    n = len(steps)
    aw = 30
    cw = (width - PAD * 2 - aw * (n - 1)) / n
    wrapped = [(wrap(a, T_BODY, cw - 22, True), wrap(b, T_SMALL, cw - 22)) for a, b in steps]
    box_h = 26 + max(len(a) * 20 + len(b) * 18 for a, b in wrapped)
    height = top + box_h + PAD + note_h(note, width)
    p = []
    for i, (aw_lines, bw_lines) in enumerate(wrapped):
        x = PAD + i * (cw + aw)
        p.append(rrect(x, top, cw, box_h, 11, color, ' opacity="0.08"'))
        p.append(multiline(x + 14, top + 26, aw_lines, T_BODY, color, "700", lh=1.25))
        p.append(multiline(x + 14, top + 26 + len(aw_lines) * 20 + 4, bw_lines,
                           T_SMALL, INK_2, "400", lh=1.28))
        if i < n - 1:
            ax = x + cw + aw / 2
            ay = top + box_h / 2
            p.append(f'<path d="M{ax-8:.1f},{ay:.1f} H{ax+6:.1f} M{ax+1:.1f},{ay-5:.1f} '
                     f'l5,5 l-5,5" fill="none" stroke="{MUTED}" stroke-width="2" '
                     f'stroke-linecap="round" stroke-linejoin="round"/>')
    return frame(width, round(height), title, "".join(p), note, subtitle)
