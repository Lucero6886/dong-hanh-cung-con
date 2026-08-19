#!/usr/bin/env python3
# =============================================================================
#  SINH TOÀN BỘ HÌNH MINH HOẠ CHO WEBSITE
# =============================================================================
#  Chạy:  python3 scripts/make-figures.py
#  Cần:   pip install pillow cairosvg
#
#  Sinh ra hai loại file, đều nằm trong `public/images/articles/`:
#
#    <slug>-cover.png   Ảnh bìa 1200×630. Hiện ở thẻ bài ngoài trang danh sách,
#                       ở đầu bài, VÀ là ảnh xem trước khi dán link lên
#                       Facebook/Zalo. Phải là .png — mạng xã hội không đọc .svg.
#
#    <slug>-fXX.svg     Sơ đồ trong thân bài. Dùng .svg vì nó nét ở mọi cỡ màn
#                       hình, nhẹ, và sửa được bằng trình soạn thảo văn bản.
#
#  ⚠️  File này GHI ĐÈ toàn bộ hình cũ mỗi lần chạy. Muốn sửa một hình thì sửa
#      phần khai báo trong file này rồi chạy lại — đừng sửa thẳng file .svg,
#      vì lần chạy sau nó sẽ bị ghi đè.
#
#  Toàn bộ màu sắc, cỡ chữ và khuôn hình nằm ở `scripts/figures_lib.py`.
# =============================================================================

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import cairosvg  # noqa: E402
from figures_lib import *  # noqa: E402,F403

OUT = ROOT / "public" / "images" / "articles"

# =============================================================================
#  PHẦN 1 — ẢNH BÌA
# =============================================================================
#  Mỗi chủ đề có một HOẠ TIẾT riêng. Nhờ vậy các bài cùng chủ đề nhìn là thấy
#  cùng một họ, còn các chủ đề khác nhau thì phân biệt được ngay từ thẻ bài.
# =============================================================================

CW, CH = 1200, 630
C_PAD = 76
ART_X = 760          # hoạ tiết bắt đầu từ đây
ART_CX, ART_CY = 960, 315


def m_arcs(c1, c2):
    """Các cung tròn đồng tâm — nở ra."""
    p = []
    for i, r in enumerate([70, 116, 162, 208]):
        col = c1 if i % 2 == 0 else c2
        op = 0.92 - i * 0.19
        p.append(f'<circle cx="{ART_CX}" cy="{ART_CY}" r="{r}" fill="none" '
                 f'stroke="{col}" stroke-width="{16 - i*2.5:.1f}" opacity="{op:.2f}" '
                 f'stroke-linecap="round" stroke-dasharray="{r*3.6:.0f} {r*6.3:.0f}" '
                 f'transform="rotate({-52 + i*26} {ART_CX} {ART_CY})"/>')
    p.append(f'<circle cx="{ART_CX}" cy="{ART_CY}" r="26" fill="{c1}"/>')
    return "".join(p)


def m_bars(c1, c2):
    """Các cột cao dần."""
    p, x = [], ART_CX - 150
    for i, h in enumerate([64, 112, 168, 232]):
        col = c1 if i < 3 else c2
        p.append(f'<rect x="{x}" y="{ART_CY+120-h}" width="58" height="{h}" rx="16" '
                 f'fill="{col}" opacity="{0.42 + i*0.19:.2f}"/>')
        x += 78
    return "".join(p)


def m_dots(c1, c2):
    """Lưới chấm, vài chấm được nhấn."""
    p = []
    hi = {(1, 1), (2, 2), (3, 1), (2, 0)}
    for r in range(5):
        for c in range(5):
            x, y = ART_CX - 152 + c * 76, ART_CY - 152 + r * 76
            on = (r, c) in hi
            # chấm nền dùng màu trung tính để chấm được nhấn nổi hẳn lên
            p.append(f'<circle cx="{x}" cy="{y}" r="{21 if on else 10}" '
                     f'fill="{c1 if on else GRAY}" opacity="{1 if on else 0.9}"/>')
    for (r, c) in sorted(hi):
        x, y = ART_CX - 152 + c * 76, ART_CY - 152 + r * 76
        p.append(f'<circle cx="{x}" cy="{y}" r="33" fill="none" stroke="{c2}" '
                 f'stroke-width="3" opacity="0.35"/>')
    return "".join(p)


def m_rungs(c1, c2):
    """Các bậc xếp chồng — bậc trên cùng được nhấn."""
    p = []
    for i in range(5):
        y = ART_CY - 150 + i * 66
        on = i == 0
        w = 312 - i * 30
        p.append(f'<rect x="{ART_CX - w/2:.0f}" y="{y}" width="{w:.0f}" height="48" rx="15" '
                 f'fill="{c1 if on else c2}" opacity="{1 if on else 0.46 - i*0.08:.2f}"/>')
    return "".join(p)


def m_path(c1, c2):
    """Đường đi có các chặng — dùng cho loạt bài theo giai đoạn."""
    pts = [(ART_CX - 168, ART_CY + 128), (ART_CX - 76, ART_CY + 34),
           (ART_CX + 16, ART_CY + 76), (ART_CX + 108, ART_CY - 56),
           (ART_CX + 176, ART_CY - 142)]
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    p = [f'<path d="{d}" fill="none" stroke="{c2}" stroke-width="9" opacity="0.34" '
         f'stroke-linecap="round" stroke-linejoin="round"/>']
    for i, (x, y) in enumerate(pts):
        r = 15 + i * 4
        p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c1}" opacity="{0.5+i*0.125:.2f}"/>')
    return "".join(p)


def m_bloom(c1, c2):
    """Các tia toả ra từ một điểm."""
    import math
    p = []
    for i in range(9):
        a = math.radians(-104 + i * 26)
        x2 = ART_CX + math.cos(a) * (200 if i % 2 == 0 else 152)
        y2 = ART_CY + math.sin(a) * (200 if i % 2 == 0 else 152)
        p.append(f'<line x1="{ART_CX}" y1="{ART_CY}" x2="{x2:.0f}" y2="{y2:.0f}" '
                 f'stroke="{c1 if i % 2 == 0 else c2}" stroke-width="11" '
                 f'opacity="{0.30 + (i%3)*0.22:.2f}" stroke-linecap="round"/>')
    p.append(f'<circle cx="{ART_CX}" cy="{ART_CY}" r="30" fill="{c1}"/>')
    return "".join(p)


def m_nest(c1, c2):
    """Các khung lồng nhau — dùng cho chủ đề về giới hạn, cấu trúc."""
    p = []
    for i, s in enumerate([230, 172, 114, 56]):
        col = c1 if i % 2 == 0 else c2
        p.append(f'<rect x="{ART_CX-s/2:.0f}" y="{ART_CY-s/2:.0f}" width="{s}" height="{s}" '
                 f'rx="{s*0.24:.0f}" fill="none" stroke="{col}" stroke-width="{15-i*2}" '
                 f'opacity="{0.30 + i*0.22:.2f}"/>')
    return "".join(p)


def m_wave(c1, c2):
    """Đường cong đi lên — dùng cho chủ đề về thay đổi theo thời gian."""
    p = []
    for i, (dy, col, op, sw) in enumerate([(46, c2, 0.26, 10), (0, c1, 1.0, 12)]):
        d = (f"M{ART_CX-192},{ART_CY+112+dy} C{ART_CX-96},{ART_CY+108+dy} "
             f"{ART_CX-72},{ART_CY-24+dy} {ART_CX+12},{ART_CY-36+dy} "
             f"S{ART_CX+120},{ART_CY-140+dy} {ART_CX+192},{ART_CY-150+dy}")
        p.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" '
                 f'opacity="{op}" stroke-linecap="round"/>')
    p.append(f'<circle cx="{ART_CX+192}" cy="{ART_CY-150}" r="22" fill="{c1}"/>')
    return "".join(p)


# Chủ đề → (hoạ tiết, màu chính, màu phụ)
MOTIF = {
    "Đồng hành cùng con":                ("path",  TEAL, BLUE),
    "Mang thai & năm đầu đời":           ("arcs",  TEAL, BLUE),
    "Não bộ & các giai đoạn phát triển": ("bloom", BLUE, TEAL),
    "Nhân cách & tấm gương":             ("dots",  TEAL, CLAY),
    "Động lực & thói quen":              ("bars",  TEAL, CLAY),
    "Học tập & tự học":                  ("wave",  BLUE, TEAL),
    "Giao tiếp cha mẹ – con":            ("arcs",  BLUE, CLAY),
    "Cảm xúc & tâm lý":                  ("wave",  CLAY, TEAL),
    "Kỷ luật tích cực":                  ("nest",  CLAY, TEAL),
    "Tự lập & trách nhiệm":              ("rungs", TEAL, BLUE),
    "Công nghệ & trẻ em":                ("nest",  BLUE, TEAL),
    "Tuổi teen":                         ("bloom", CLAY, BLUE),
    "Góc suy ngẫm của cha mẹ":           ("dots",  BLUE, CLAY),
}
MOTIF_FN = {"arcs": m_arcs, "bars": m_bars, "dots": m_dots, "rungs": m_rungs,
            "path": m_path, "bloom": m_bloom, "nest": m_nest, "wave": m_wave}


def cover_svg(title, category, eyebrow=None):
    motif, c1, c2 = MOTIF.get(category, ("arcs", TEAL, BLUE))
    art = MOTIF_FN[motif](c1, c2)

    # Cỡ chữ tiêu đề co lại nếu tiêu đề dài, để luôn vừa bốn dòng
    tw = ART_X - C_PAD - 40
    for size in (60, 54, 48, 43, 39):
        lines = wrap(title, size, tw, bold=True)
        if len(lines) <= 4:
            break
    lh = size * 1.16
    block_h = len(lines) * lh
    ty = (CH - block_h) / 2 + size * 0.80

    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" '
         f'width="{CW}" height="{CH}">',
         f'<rect width="{CW}" height="{CH}" fill="{SURFACE}"/>',
         # dải màu mảnh bên trái, làm mốc thị giác
         f'<rect x="0" y="0" width="10" height="{CH}" fill="{c1}"/>',
         art]
    p.append(tspan(C_PAD, 96, (eyebrow or category).upper(), 21, c1, "700",
                   font=FONT_PNG))
    p.append(f'<rect x="{C_PAD}" y="112" width="52" height="4" rx="2" fill="{c1}" opacity="0.55"/>')
    p.append(multiline(C_PAD, ty, lines, size, INK, "700", lh=1.16, font=FONT_PNG))
    p.append(f'<line x1="{C_PAD}" y1="{CH-104}" x2="{C_PAD+300}" y2="{CH-104}" '
             f'stroke="{BORDER}" stroke-width="2"/>')
    p.append(tspan(C_PAD, CH - 66, "Đồng hành cùng con", 24, INK_2, "700", font=FONT_PNG))
    p.append(tspan(C_PAD, CH - 40, "một dự án của ELS", 17, MUTED, "400", font=FONT_PNG))
    p.append("</svg>")
    return "".join(p)


# =============================================================================
#  PHẦN 2 — SƠ ĐỒ TRONG THÂN BÀI
# =============================================================================
#  Mỗi mục dưới đây là: slug bài → danh sách các hình.
#  Mỗi hình là (tên_file_rút_gọn, chuỗi_svg).
# =============================================================================

def figures():
    F = {}

    # ── Não bộ: các mốc đạt đỉnh ──────────────────────────────────────────
    F["nao-cua-con-dang-xay-theo-kieu-nao"] = [
        ("f1", dot_scale(
            "Mỗi phần của não chín ở một tuổi khác nhau",
            [("Độ dày vỏ não", 1.7, TEAL), ("Chất xám toàn não", 5.9, TEAL),
             ("Thể tích đại não", 12.5, TEAL), ("Chất xám dưới vỏ", 14.4, TEAL),
             ("Chất trắng", 28.7, TEAL)],
            0, 32, [0, 5, 10, 15, 20, 25, 30], xlabel="tuổi đạt đỉnh",
            marks=[(6, "6 tuổi"), (25, "25 tuổi")],
            subtitle="Tổng hợp hơn 100.000 lần chụp não · Nature, 2022",
            note="Không chỉ số nào đạt đỉnh ở tuổi 6, cũng không chỉ số nào đạt đỉnh ở tuổi 25 — "
                 "hai mốc được nhắc tới nhiều nhất. Hỏi “khi nào não con phát triển xong” là một câu hỏi sai.")),
        ("f2", two_col(
            "Giai đoạn nhạy cảm: chỗ nào bằng chứng vững, chỗ nào không",
            ("Bằng chứng vững", TEAL,
             ["Thị giác — từ nghiên cứu trẻ đục thuỷ tinh thể bẩm sinh",
              "Phân biệt âm thanh lời nói trong năm đầu",
              "Gắn bó xã hội sau thiếu thốn chăm sóc nghiêm trọng"]),
            ("Không tìm thấy bằng chứng", CLAY,
             ["“Cửa sổ vàng” cho toán học",
              "“Giai đoạn nhạy cảm” để phát triển âm nhạc",
              "“Sau tuổi này não không tiếp thu được nữa”"]),
            note="Bài tổng quan của Nathan Fox (2014) kết luận: “không có nhiều bằng chứng cho giai đoạn "
                 "nhạy cảm ở các hành vi nhận thức hay xã hội”.")),
    ]

    # ── Kể chuyện ─────────────────────────────────────────────────────────
    F["ke-chuyen-the-nao-cho-con-doi"] = [
        ("f1", bar_h(
            "Truyện nào thật sự làm trẻ bớt nói dối?",
            [("Thỏ và Rùa (nhóm đối chứng)", 1, "mốc so sánh"),
             ("Pinocchio — mũi dài ra", 1, "không đổi"),
             ("Cậu bé chăn cừu — bị sói ăn", 1, "không đổi"),
             ("George Washington — thú nhận rồi được cha ôm", 3.13, "ít nói dối hơn 3,1 lần")],
            emphasis=3, label_w=256,
            subtitle="268 trẻ 3–7 tuổi · Psychological Science, 2014",
            note="Ba truyện đầu bằng đúng mốc so sánh, tức là không tạo ra thay đổi nào. "
                 "Khi nhóm nghiên cứu chỉ đổi cái kết của chuyện Washington thành trừng phạt, "
                 "toàn bộ tác dụng biến mất.")),
        ("f2", two_col(
            "Cùng một bài học, đổi nhân vật thì kết quả đổi hẳn",
            ("Nhân vật là con vật biết nói", CLAY,
             ["Truyện hải ly chia gỗ: 22,9% xử sự công bằng",
              "Nhóm không đọc gì: 21,9% — gần như bằng nhau",
              "Bản truyện con vật còn làm trẻ chia sẻ ÍT hơn"]),
            ("Nhân vật là người, tình huống quen", TEAL,
             ["Truyện một đứa trẻ trong lớp vẽ: 46,8%",
              "Sau 2–4 tuần còn tăng tiếp lên 58,8%",
              "Bản nhân vật người làm trẻ chia sẻ NHIỀU hơn"]),
            note="Trẻ nhỏ không tự bắc cầu từ “con hải ly chia gỗ” sang “mình chia đồ chơi với em”. "
                 "Người lớn tưởng cây cầu ấy hiển nhiên; với trẻ thì không.")),
    ]

    # ── Tấm gương ─────────────────────────────────────────────────────────
    F["tam-guong-gan-hon-danh-nhan"] = [
        ("f1", diverging(
            "Đọc về nhà khoa học: kể phần nào thì điểm số đổi theo hướng nào",
            [("Đọc về vật lộn trí tuệ — bế tắc, thí nghiệm hỏng", 1.0, "điểm tăng"),
             ("Đọc về vật lộn đời thường — nghèo, bị phân biệt", 0.9, "điểm tăng"),
             ("Chỉ đọc về thành tựu (nhóm đối chứng)", -0.7, "điểm GIẢM")],
            label_w=290,
            subtitle="402 học sinh trung học, đo sau 6 tuần · Đại học Columbia",
            note="Nhóm chỉ đọc về thành tựu không những không tăng, mà điểm còn thấp hơn cả kỳ trước khi "
                 "nghiên cứu bắt đầu. Hình vẽ theo chiều tác động, không phải theo độ lớn chính xác.")),
    ]

    # ── Tự giác ───────────────────────────────────────────────────────────
    F["tu-giac-khong-moc-len-tu-loi-nhac"] = [
        ("f1", diverging(
            "Phần thưởng tác động thế nào tới hứng thú tự nhiên của trẻ",
            [("Thưởng vật chất, đã hứa trước", -0.36, "-0,36"),
             ("Thưởng bất ngờ, không hứa trước", 0.01, "0,01"),
             ("Lời khen, phản hồi tích cực", 0.33, "+0,33")],
            label_w=270,
            subtitle="Phân tích gộp 128 nghiên cứu · Psychological Bulletin, 1999",
            note="Số càng âm thì hứng thú tự nhiên càng giảm. Chính bài báo ghi rằng tác hại nặng hơn ở "
                 "trẻ em so với sinh viên đại học. Vấn đề nằm ở đúng một chỗ: hứa trước một phần thưởng "
                 "vật chất cho việc con vốn đã thích.")),
        ("f2", two_col(
            "Khen mô tả việc, đừng khen phong danh hiệu",
            ("Đặt lên vai con một danh hiệu", CLAY,
             ["“Con giỏi quá!”", "“Con thông minh thật.”", "“Con là đứa ngoan.”"]),
            ("Mô tả điều con vừa làm", TEAL,
             ["“Con làm lại ba lần mới xong.”",
              "“Chỗ đó khó mà con tìm ra cách.”",
              "“Con vừa tự dọn bàn. Bố thấy.”"]),
            note="Trong nghiên cứu kinh điển, 38% trẻ được khen thông minh đã khai man điểm số; ở nhóm "
                 "được khen chăm chỉ, con số là 13%.")),
    ]

    # ── Nếu… thì… ─────────────────────────────────────────────────────────
    F["neu-thi-cach-xay-thoi-quen"] = [
        ("f1", flow(
            "Cấu trúc của một câu “nếu… thì…” chạy được",
            [("NẾU", "một tình huống cụ thể, nhìn thấy được, chắc chắn xảy ra trong ngày"),
             ("THÌ", "một việc nhỏ, làm xong trong vài giây, không cần ai nhắc")],
            subtitle="Ví dụ: “Nếu con vừa bước qua cửa, thì con treo cặp lên móc.”",
            note="Câu này chuyển việc nhớ từ trong đầu ra ngoài thế giới. Cái cửa trở thành lời nhắc — "
                 "con không phải tự nhớ nữa.")),
        ("f2", range_bar(
            "Bao lâu thì một việc thành thói quen?",
            [("Điều ai cũng nói", 21, None, 21, GRAY, "21 ngày"),
             ("Nghiên cứu thật", 4, 63, 335, TEAL, "4 – 335 ngày")],
            0, 340, [0, 50, 100, 150, 200, 250, 300], xlabel="số ngày", label_w=170,
            note="Chấm tròn là mức trung vị, khoảng 59–66 ngày. Toàn bộ nghiên cứu này làm trên người lớn, "
                 "chưa từng kiểm chứng ở trẻ em. Và bỏ lỡ một ngày không làm hỏng quá trình.")),
    ]

    # ── Đi cùng con ───────────────────────────────────────────────────────
    F["di-cung-con-khong-di-thay-con"] = [
        ("f1", ladder(
            "Cái thang giúp đỡ — luôn bắt đầu từ bậc trên cùng",
            [(1, "Chờ", "không nói gì, đếm thầm tới mười"),
             (2, "Hỏi", "“Con đang mắc ở chỗ nào?”"),
             (3, "Gợi", "“Thử nhìn lại cái đầu dây bên trái xem”"),
             (4, "Chỉ một bước", "làm mẫu một thao tác, rồi trả lại cho con"),
             (5, "Cùng làm", "hai người cùng làm, con giữ phần chính"),
             (6, "Làm hộ", "bạn làm, con nhìn")],
            note="Phần lớn chúng ta nhảy thẳng từ bậc 1 xuống bậc 6 — không phải vì lười, mà vì đang vội "
                 "và vì nhìn con loay hoay thì khó chịu. Đây là cách sắp xếp cho dễ nhớ, không phải một "
                 "công cụ đã được nghiên cứu kiểm chứng.")),
    ]

    # ── Năm điều ai cũng nói ──────────────────────────────────────────────
    F["nam-dieu-ai-cung-noi-ve-nuoi-con"] = [
        ("f1", steps_down(
            "Thí nghiệm kẹo dẻo: liên hệ còn lại bao nhiêu sau mỗi bước kiểm tra?",
            [("Nghiên cứu gốc, 35 trẻ ở một trường mẫu giáo", 1.0, "mốc gốc"),
             ("Làm lại với 918 trẻ đa dạng hơn", 0.5, "còn một nửa"),
             ("Sau khi tính hoàn cảnh gia đình", 0.33, "còn một phần ba"),
             ("Sau khi tính năng lực sẵn có của trẻ", 0.02, "gần như hết")],
            subtitle="Watts, Duncan & Quan · Psychological Science, 2018",
            note="Và gần như toàn bộ phần lợi ích nhỏ còn lại đến từ việc trẻ chờ được 20 giây — "
                 "không phải 15 phút.")),
        ("f2", two_col(
            "Bốn câu hỏi để tự kiểm tra một lời khuyên nuôi con",
            ("Hỏi về bằng chứng", BLUE,
             ["Nghiên cứu ấy có bao nhiêu người?",
              "Đây là thí nghiệm hay chỉ là quan sát?"]),
            ("Hỏi về động cơ và độ bền", CLAY,
             ["Ai được lợi nếu tôi tin điều này?",
              "Có ai đã thử làm lại chưa?"]),
            note="Quan sát chỉ cho biết hai thứ đi cùng nhau — nó không cho biết cái nào gây ra cái nào.")),
    ]

    # ── Tuổi teen ─────────────────────────────────────────────────────────
    F["nao-tuoi-teen-dang-xay-lai"] = [
        ("f1", bar_h(
            "Giấc ngủ tuổi teen: khuyến nghị và thực tế",
            [("Khuyến nghị cho tuổi 13–18", 9, "8 – 10 tiếng"),
             ("Một đứa trẻ đi ngủ 11h30, dậy 6h", 6.5, "6,5 tiếng"),
             ("Thiếu mỗi ngày", 2.5, "khoảng 2,5 tiếng")],
            emphasis=2, label_w=250, color=CLAY,
            subtitle="Viện Y học Giấc ngủ Hoa Kỳ · lịch học phổ biến ở Việt Nam",
            note="Khi bước vào dậy thì, đồng hồ sinh học của trẻ lùi lại tới hai tiếng — đo được bằng "
                 "nồng độ melatonin trong phòng thí nghiệm. Trẻ 15 tuổi được bảo ngủ lúc 10 giờ thường "
                 "thật sự chưa buồn ngủ.")),
        ("f2", two_col(
            "Giải thích, không phải bào chữa",
            ("Giải thích — đổi cách mình làm", TEAL,
             ["“Đồng hồ sinh học của con lùi thật, nên mình tính lại giờ ngủ.”",
              "“Bạn bè có sức nặng lớn, mình cần bàn trước về những tình huống có bạn bè.”",
              "“Con dễ bùng nổ hơn, nên mình sẽ không xử lý lúc cả hai đang nóng.”"]),
            ("Bào chữa — bỏ việc mình phải làm", CLAY,
             ["“Nó thức khuya vì não nó thế, chịu thôi.”",
              "“Nó bị bạn rủ, không trách nó được.”",
              "“Nó nói hỗn cũng là do tuổi, kệ đi.”"]),
            note="Cột trái đổi cách mình làm. Cột phải bỏ việc mình phải làm.")),
    ]

    # ── Sáu năm đầu ───────────────────────────────────────────────────────
    F["sau-nam-dau-doi"] = [
        ("f1", two_col(
            "Sáu năm đầu: cái gì có bằng chứng, cái gì chưa",
            ("Có bằng chứng — và đều miễn phí", TEAL,
             ["Trò chuyện có qua lại, đáp đúng vào thứ con đang chú ý",
              "Ít nhất một người lớn có mặt đều đặn và đáp lại con",
              "Ngủ đủ, chơi tự do, một cái nhà không quá căng"]),
            ("Chưa có bằng chứng — nhưng bán rất chạy", CLAY,
             ["“Cửa sổ vàng” cho toán học hoặc âm nhạc",
              "Học nhạc để giỏi toán — hiệu ứng biến mất khi nghiên cứu chặt",
              "Thẻ học chữ và ép học sớm khi con không thích"]),
            note="Ý nghĩa hợp lý của chữ “vàng”: nền móng đặt sớm thì RẺ HƠN, chứ không phải "
                 "không thể làm sau.")),
    ]

    # ── Sáu đến mười hai ──────────────────────────────────────────────────
    F["sau-den-muoi-hai-tuoi"] = [
        ("f1", two_col(
            "Khả năng tự điều khiển bản thân: cái gì bào mòn, cái gì nâng đỡ",
            ("Bốn thứ làm suy giảm", CLAY,
             ["Căng thẳng kéo dài", "Thiếu ngủ", "Cô đơn, ít bạn", "Thiếu vận động"]),
            ("Năm thứ nâng đỡ", TEAL,
             ["Ngủ 9–12 tiếng mỗi ngày", "Vận động thật, không phải một tiết thể dục",
              "Có bạn thân", "Được giao việc nhà có hậu quả thật",
              "Giỏi được một thứ gì đó"]),
            subtitle="Adele Diamond · Annual Review of Psychology, 2013",
            note="Ba trong bốn thứ ở cột trái thường TĂNG lên khi ta thêm một lớp học nữa. "
                 "Chúng ta hay thấy con “không tập trung” rồi kết luận là con thiếu ý chí.")),
    ]

    # ── Thai kỳ ───────────────────────────────────────────────────────────
    F["chin-thang-danh-sach-ngan"] = [
        ("f1", two_col(
            "Thai giáo: phần khoa học có thật và phần bị thổi phồng",
            ("Có thật", TEAL,
             ["Thai nhi nghe được từ khoảng tuần 26–28",
              "Trẻ sơ sinh nhận ra giọng mẹ và nhịp điệu tiếng mẹ đẻ",
              "Tử cung lọc bớt âm cao — thứ đi qua chủ yếu là nhịp điệu"]),
            ("Bị thổi phồng", CLAY,
             ["“Nghe Mozart giúp con thông minh hơn”",
              "Tai nghe áp lên bụng bầu — có khuyến cáo KHÔNG nên",
              "DHA làm con thông minh hơn — bằng chứng rất yếu"]),
            note="Giọng của chính bạn truyền nhịp điệu tốt hơn bất kỳ cái loa nào, và miễn phí. "
                 "Khuyến cáo về tai nghe: không áp trực tiếp lên bụng, tránh âm dưới 250 Hz trên 65 dB.")),
    ]

    # ── Kỷ luật ───────────────────────────────────────────────────────────
    F["ky-luat-khong-phai-la-phat"] = [
        ("f1", two_col(
            "Hậu quả có liên quan tới việc con làm, hay không?",
            ("Ít tác dụng — không liên quan", CLAY,
             ["Làm bẩn nhà → cấm xem tivi",
              "Quên bài tập → mắng",
              "Dùng điện thoại quá giờ → tịch thu một tuần"]),
            ("Có liên quan — dạy được điều gì đó", TEAL,
             ["Làm bẩn nhà → cùng lau dọn",
              "Quên bài tập → tự viết lời xin lỗi cô",
              "Quá giờ → hôm sau bớt đúng phần đã dùng quá"]),
            note="Cột phải mất công hơn, và với người bận rộn đó là một cái giá thật. Nhưng cột phải "
                 "giảm dần theo thời gian, còn cột trái thì lặp lại mãi.")),
    ]

    # ── Màn hình ──────────────────────────────────────────────────────────
    F["man-hinh-tu-dem-gio-sang-thoa-thuan"] = [
        ("f1", flow(
            "Trọng tâm đã dịch chuyển khỏi việc đếm giờ",
            [("Câu hỏi cũ", "“Mấy tiếng một ngày là đủ?” — một con số, và nó hiếm khi giúp được gì"),
             ("Câu hỏi mới", "“Màn hình có đang lấn vào giấc ngủ, bữa ăn và trò chuyện không?”")],
            subtitle="Hướng dẫn mới của Viện Nhi khoa Hoa Kỳ, công bố 20/01/2026",
            note="Với cha mẹ bận rộn, đây là một tin tốt: bớt phải canh đồng hồ, thêm vài quy ước rõ ràng.")),
    ]

    # ── Khi con đã trưởng thành ───────────────────────────────────────────
    F["khi-con-da-truong-thanh"] = [
        ("f1", two_col(
            "Hỗ trợ và kiểm soát: nhìn từ ngoài rất giống nhau",
            ("Hỗ trợ — không kèm điều kiện", TEAL,
             ["Đưa tiền khi con cần, không nhắc lại sau đó",
              "Cho lời khuyên KHI ĐƯỢC HỎI",
              "Để phòng cho con về ở lúc khó khăn"]),
            ("Kiểm soát — kèm một khoản nợ", CLAY,
             ["“Bố mẹ lo cho con thế mà con…”",
              "Quyết định thay con rồi báo sau",
              "Dùng sự giúp đỡ làm đòn bẩy"]),
            note="Bài kiểm tra một câu: việc giúp đỡ này có kèm điều kiện không? Kể cả điều kiện ngầm.")),
    ]

    # ── Mười lăm phút ─────────────────────────────────────────────────────
    F["muoi-lam-phut-nhung-la-that"] = [
        ("f1", flow(
            "Mười lăm phút thật khác gì hai tiếng có mặt hờ",
            [("Có mặt hờ", "cùng phòng, nhưng mắt ở điện thoại và câu chuyện bị ngắt giữa chừng"),
             ("Có mặt thật", "không màn hình, con dẫn chuyện, người lớn đáp đúng vào thứ con đang nói")],
            note="Thứ đọng lại ở trẻ không phải số giờ, mà là những phút chúng biết chắc mình đang "
                 "được chú ý trọn vẹn.")),
    ]

    # ── Cơn giận ──────────────────────────────────────────────────────────
    F["con-gian-va-minh-cung-gian"] = [
        ("f1", flow(
            "Thứ tự xử lý khi cả hai cùng đang nóng",
            [("1. Mình trước", "hạ nhịp của chính mình — nói ra thành lời rằng mình đang bực"),
             ("2. Rồi tới con", "gọi tên cảm xúc, không giảng giải, không hỏi lý do"),
             ("3. Nói chuyện sau", "khi cả hai đã nguội, quay lại đúng chuyện đó")],
            note="Người lớn đang nóng không dạy được gì, và đứa trẻ đang quá tải thì năng lực nghe "
                 "đã đóng. Hoãn lại không làm mất uy — nhưng phải nhớ quay lại thật.")),
    ]

    # ── Chán học ──────────────────────────────────────────────────────────
    F["khi-con-noi-con-chan-hoc"] = [
        ("f1", two_col(
            "“Con chán học” thường có nghĩa là một điều khác",
            ("Điều con nói ra", CLAY,
             ["“Con chán học.”", "“Học chán lắm.”", "“Con không muốn đi học.”"]),
            ("Điều có thể đang xảy ra bên dưới", TEAL,
             ["Con không theo kịp và ngại nói ra",
              "Con theo kịp quá dễ nên thấy vô nghĩa",
              "Có chuyện với bạn bè hoặc thầy cô",
              "Con đang mệt, thiếu ngủ, quá tải lịch học"]),
            note="Bốn khả năng cần bốn cách xử lý khác nhau — và cả bốn đều bắt đầu bằng việc hỏi thêm "
                 "thay vì trả lời ngay.")),
    ]

    # ── Cấu trúc thay vì nhắc nhở ─────────────────────────────────────────
    F["cau-truc-thay-vi-nhac-nho"] = [
        ("f1", two_col(
            "Lời nhắc và cấu trúc: cái nào tự chạy khi bạn vắng mặt?",
            ("Lời nhắc — cần bạn có mặt", CLAY,
             ["“Học bài đi con.”", "“Con đánh răng chưa?”", "“Nhớ mang vở nhé.”"]),
            ("Cấu trúc — tự chạy", TEAL,
             ["Một giờ cố định, cùng một chỗ ngồi",
              "Một chuỗi việc cố định trước giờ ngủ",
              "Một cái bảng hoặc tờ giấy dán ở chỗ nhìn thấy"]),
            note="Chừng nào còn có người nhắc, đứa trẻ không cần bộ nhắc của riêng nó.")),
    ]

    # ── Hỏi con học được gì ───────────────────────────────────────────────
    F["hoi-con-hoc-duoc-gi-thay-vi-hoi-may-diem"] = [
        ("f1", two_col(
            "Câu hỏi đầu tiên hướng sự chú ý của con đi đâu?",
            ("“Hôm nay con được mấy điểm?”", CLAY,
             ["Hướng chú ý RA NGOÀI, về phía kết quả do người khác chấm",
              "Tiện: có ngay một con số, so sánh được",
              "Dần thành thước đo con dùng để đánh giá chính mình"]),
            ("“Hôm nay con học được gì?”", TEAL,
             ["Hướng chú ý VÀO TRONG, về thứ chính con vừa có thêm",
              "Khó hơn: câu trả lời đầu tiên thường là “con không biết”",
              "Là một kỹ năng, và kỹ năng thì cần tập"]),
            note="Vấn đề không phải là bỏ hẳn câu hỏi về điểm. Là THỨ TỰ: hỏi điều con học được trước, "
                 "hỏi điểm sau.")),
    ]

    # ── Cảm giác có lỗi ───────────────────────────────────────────────────
    F["cam-giac-co-loi-vi-di-lam"] = [
        ("f1", two_col(
            "Đổi câu hỏi thì đổi được cả câu trả lời",
            ("Câu hỏi hầu như luôn cho ra “chưa”", CLAY,
             ["“Mình đã dành đủ thời gian cho con chưa?”",
              "Không đo được, không kết thúc được",
              "Để lại một cảm giác thiếu sót chung chung"]),
            ("Câu hỏi trả lời được", TEAL,
             ["“Tuần vừa rồi, có lúc nào con biết chắc mình đang được chú ý không?”",
              "Chỉ vào một việc cụ thể",
              "Nếu chưa, nó cho biết chính xác cần làm gì tiếp"]),
            note="Cảm giác có lỗi xuất phát từ một chỗ tử tế — bạn quan tâm. Nhưng bản thân nó không "
                 "làm bạn có thêm thời gian, cũng không làm bạn kiên nhẫn hơn.")),
    ]

    # ── Đóng cửa phòng ────────────────────────────────────────────────────
    F["khi-con-bat-dau-dong-cua-phong"] = [
        ("f1", flow(
            "Cánh cửa đóng lại nghĩa là gì",
            [("Điều ta sợ", "“Con đang xa mình. Mình đang mất con.”"),
             ("Điều thường đang xảy ra", "Con đang tập có một không gian riêng — việc bình thường "
                                          "của tuổi này, không phải dấu hiệu quan hệ hỏng")],
            note="Điều cần giữ không phải cánh cửa mở, mà là việc con vẫn thấy kể với bạn là an toàn.")),
    ]

    # ── Từ phần thưởng đến động lực bên trong ─────────────────────────────
    F["tu-phan-thuong-den-dong-luc-ben-trong"] = [
        ("f1", flow(
            "Đường đi từ động lực bên ngoài vào bên trong",
            [("Làm vì được thưởng", "phần thưởng là lý do; hết thưởng thì hết làm"),
             ("Làm vì thấy mình làm được", "cảm giác năng lực bắt đầu thay chỗ cho phần thưởng"),
             ("Làm vì thấy có nghĩa", "việc đó gắn với điều con thấy đáng làm")],
            note="Không có công tắc nào chuyển thẳng từ chặng một sang chặng ba. Điều cha mẹ làm được "
                 "là đừng dựng thêm rào ở chặng một — cụ thể là đừng hứa thưởng cho việc con vốn đã thích.")),
    ]

    return F


# =============================================================================
#  CHẠY
# =============================================================================

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*"):
        old.unlink()

    import re
    arts = sorted((ROOT / "src/content/articles").glob("*.md*"))
    figs = figures()
    n_cov = n_fig = 0

    print(f"→ {len(arts)} bài viết\n")
    for f in arts:
        slug = f.name.rsplit(".", 1)[0]
        txt = f.read_text(encoding="utf-8")
        fm = txt.split("---")[1]
        get = lambda k: (re.search(rf'^{k}: *"?(.*?)"?$', fm, re.M) or [None, ""])[1]
        title = get("title").replace('\\"', '"')
        cat = get("category")

        cairosvg.svg2png(bytestring=cover_svg(title, cat).encode(),
                         write_to=str(OUT / f"{slug}-cover.png"),
                         output_width=CW, output_height=CH)
        n_cov += 1

        made = []
        for tag, svg in figs.get(slug, []):
            (OUT / f"{slug}-{tag}.svg").write_text(svg, encoding="utf-8")
            made.append(tag)
            n_fig += 1
        print(f"  {slug[:44]:46s} bìa" + (f" + {len(made)} sơ đồ" if made else ""))

    total = sum(p.stat().st_size for p in OUT.iterdir())
    print(f"\n✓ {n_cov} ảnh bìa · {n_fig} sơ đồ · tổng {total/1024/1024:.1f} MB")


if __name__ == "__main__":
    main()
