#!/usr/bin/env python3
# =============================================================================
#  GẮN HÌNH VÀO CÁC BÀI VIẾT
# =============================================================================
#  Chạy:  python3 scripts/attach-figures.py
#  Chạy SAU khi đã chạy `make-figures.py`.
#
#  Script làm hai việc:
#
#   1. Thêm hai dòng `coverImage` và `coverAlt` vào phần khai báo đầu mỗi bài.
#      Nhờ đó ảnh bìa hiện ở ba chỗ cùng lúc: thẻ bài ngoài trang danh sách,
#      đầu bài viết, và ảnh xem trước khi dán link lên Facebook/Zalo.
#
#   2. Chèn thẻ <Figure … /> vào đúng vị trí trong thân bài.
#
#  Script CHẠY ĐƯỢC NHIỀU LẦN mà không hỏng: nếu bài đã có ảnh bìa hoặc đã có
#  hình rồi thì nó bỏ qua, không chèn trùng.
# =============================================================================

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "src/content/articles"
IMG = ROOT / "public/images/articles"

# =============================================================================
#  VỊ TRÍ CHÈN HÌNH
# =============================================================================
#  Mỗi dòng: slug → [(mã hình, mô tả cho trình đọc màn hình, chú thích, đoạn mốc)]
#
#  "đoạn mốc" là một đoạn chữ CÓ THẬT và DUY NHẤT trong bài. Hình sẽ được chèn
#  ngay sau đoạn đó. Nếu đoạn mốc không khớp hoặc khớp nhiều chỗ, script báo lỗi
#  và không sửa gì — an toàn hơn là chèn nhầm chỗ.
# =============================================================================

PLAN = {
 "nao-cua-con-dang-xay-theo-kieu-nao": [
  ("f1", "Biểu đồ các mốc tuổi đạt đỉnh của từng chỉ số não: độ dày vỏ não 1,7 tuổi; chất xám 5,9 tuổi; thể tích đại não 12,5 tuổi; chất xám dưới vỏ 14,4 tuổi; chất trắng 28,7 tuổi. Hai vạch tham chiếu ở tuổi 6 và tuổi 25 đều không trùng chỉ số nào.",
   "Không có một mốc chung nào cả — và không mốc nào rơi vào 6 hay 25.",
   "Không con số nào rơi vào 6. Cũng không con số nào rơi vào 25 — chúng ta sẽ quay lại chuyện đó ở bài về tuổi teen."),
  ("f2", "Bảng hai cột so sánh: cột trái là ba lĩnh vực có bằng chứng vững về giai đoạn nhạy cảm (thị giác, âm thanh lời nói, gắn bó xã hội); cột phải là ba khẳng định không tìm thấy bằng chứng (cửa sổ vàng cho toán, giai đoạn nhạy cảm cho âm nhạc, sau tuổi này não không tiếp thu được).",
   "Bằng chứng vững chỉ tập trung ở nhóm giác quan và tri giác.",
   "Không có nghiên cứu nào thiết lập được những cửa sổ đó. Chúng được suy diễn từ ví dụ thị giác rồi mở rộng ra mọi thứ."),
 ],
 "ke-chuyen-the-nao-cho-con-doi": [
  ("f1", "Biểu đồ cột so sánh bốn câu chuyện: Thỏ và Rùa, Pinocchio, Cậu bé chăn cừu đều bằng mốc so sánh, tức không tạo thay đổi. Chuyện George Washington thú nhận rồi được cha ôm làm trẻ ít nói dối hơn 3,1 lần.",
   "Chỉ một trong bốn câu chuyện tạo ra thay đổi đo được.",
   "Tác dụng biến mất hoàn toàn."),
  ("f2", "Bảng hai cột: truyện có nhân vật là con vật biết nói cho kết quả 22,9% xử sự công bằng, gần bằng nhóm không đọc gì là 21,9%. Truyện có nhân vật là người trong tình huống quen thuộc cho 46,8%, sau hai đến bốn tuần tăng lên 58,8%.",
   "Cùng một bài học, đổi nhân vật thì kết quả đổi hẳn.",
   "Cùng bài học ấy, kể về **một đứa trẻ trong lớp học vẽ**: tỷ lệ lên **46,75%**, và sau hai đến bốn tuần còn tăng tiếp lên **58,82%**."),
 ],
 "tam-guong-gan-hon-danh-nhan": [
  ("f1", "Biểu đồ hai chiều: hai nhóm đọc về phần vật lộn của các nhà khoa học có điểm số tăng; nhóm chỉ đọc về thành tựu có điểm số giảm xuống dưới mức trước khi nghiên cứu bắt đầu.",
   "Kể phần vật lộn thì điểm tăng. Chỉ kể thành tựu thì điểm giảm.",
   "Nghĩa là: cách chúng ta kể về người vĩ đại — chỉ nêu họ đã đạt được gì — không phải là trung tính. Nó **có hại**."),
 ],
 "tu-giac-khong-moc-len-tu-loi-nhac": [
  ("f1", "Biểu đồ hai chiều quanh mốc không: thưởng vật chất đã hứa trước làm giảm hứng thú tự nhiên 0,36; thưởng bất ngờ gần như không ảnh hưởng 0,01; lời khen làm tăng 0,33.",
   "Vấn đề nằm ở đúng một loại phần thưởng, không phải ở mọi phần thưởng.",
   "Nghĩa là: người bị ảnh hưởng nặng nhất chính là nhóm chúng ta hay áp dụng nhất."),
  ("f2", "Bảng hai cột so sánh cách khen: cột trái là những câu đặt lên vai con một danh hiệu; cột phải là những câu chỉ mô tả điều con vừa làm.",
   "Cột phải nghe khô hơn, nhưng không đặt lên vai con một danh hiệu nào phải giữ.",
   "Cột phải chỉ **mô tả điều đã xảy ra**. Nghe khô hơn. Nhưng nó không đặt lên vai con một danh hiệu nào phải giữ."),
 ],
 "neu-thi-cach-xay-thoi-quen": [
  ("f1", "Sơ đồ hai bước: phần NẾU là một tình huống cụ thể nhìn thấy được và chắc chắn xảy ra trong ngày; phần THÌ là một việc nhỏ làm xong trong vài giây.",
   "Cả sức mạnh của câu này nằm ở chỗ phần NẾU phải nhìn thấy được.",
   "Cột phải có một **thời điểm cụ thể** để bấu vào. Cột trái thì không có gì cả."),
  ("f2", "Biểu đồ khoảng: con số phổ biến là 21 ngày, còn nghiên cứu thật cho khoảng dao động từ 4 tới 335 ngày với trung vị khoảng 63 ngày.",
   "Khoảng dao động mới là điều đáng chú ý, không phải con số trung bình.",
   "Khoảng dao động mới là điều đáng chú ý. **Bốn ngày tới ba trăm ba mươi lăm ngày.** Nghĩa là hai đứa trẻ làm cùng một việc, một đứa quen sau một tuần, đứa kia sau gần một năm — và cả hai đều bình thường."),
 ],
 "di-cung-con-khong-di-thay-con": [
  ("f1", "Sơ đồ sáu bậc của cái thang giúp đỡ, từ bậc một là Chờ, xuống dần qua Hỏi, Gợi, Chỉ một bước, Cùng làm, tới bậc sáu là Làm hộ. Bậc một được đánh dấu là chỗ nên bắt đầu.",
   "Luôn bắt đầu từ bậc trên cùng, và chỉ bước xuống một bậc mỗi lần.",
   "Phần lớn chúng ta nhảy thẳng từ bậc 1 xuống bậc 6. Không phải vì lười — mà vì đang vội, và vì thương."),
 ],
 "nam-dieu-ai-cung-noi-ve-nuoi-con": [
  ("f1", "Biểu đồ bốn cột tụt dần: từ nghiên cứu gốc với 35 trẻ, xuống còn một nửa khi làm lại với 918 trẻ, còn một phần ba sau khi tính hoàn cảnh gia đình, và gần như bằng không sau khi tính năng lực sẵn có của trẻ.",
   "Liên hệ tan dần qua từng bước kiểm tra chặt chẽ hơn.",
   "Nhóm nghiên cứu cũng theo dõi tiếp tới tuổi 26 và tìm thấy rất ít."),
  ("f2", "Bảng bốn câu hỏi để tự kiểm tra một lời khuyên nuôi con, chia làm hai nhóm: hỏi về bằng chứng, và hỏi về động cơ cùng độ bền của kết quả.",
   "Bốn câu này dùng được cho cả những điều bạn sẽ gặp trong tương lai.",
   "**4. \"Có ai đã thử làm lại chưa?\"** Một nghiên cứu chưa ai kiểm chứng lại thì mới là một giả thuyết thú vị, chưa phải một sự thật."),
 ],
 "nao-tuoi-teen-dang-xay-lai": [
  ("f1", "Biểu đồ cột về giấc ngủ tuổi teen: khuyến nghị 8 đến 10 tiếng, thực tế một đứa trẻ đi ngủ 11 giờ rưỡi dậy 6 giờ chỉ ngủ 6,5 tiếng, thiếu khoảng 2,5 tiếng mỗi ngày.",
   "Thiếu hai tiếng rưỡi mỗi ngày, suốt nhiều năm, ở đúng giai đoạn não cần ngủ nhất.",
   "Đặt hai điều này cạnh nhau với lịch học Việt Nam — vào lớp 7 giờ sáng, học thêm tối, bài tập tới khuya — và bạn có một đứa trẻ thiếu ngủ kinh niên suốt nhiều năm ở đúng giai đoạn não cần ngủ nhất."),
  ("f2", "Bảng hai cột phân biệt giải thích và bào chữa: cột trái là những câu đổi cách người lớn làm; cột phải là những câu bỏ đi việc người lớn phải làm.",
   "Cùng một dữ kiện khoa học, hai cách dùng cho hai kết quả trái ngược.",
   "Cột trái đổi **cách mình làm**. Cột phải bỏ **việc mình phải làm**."),
 ],
 "sau-nam-dau-doi": [
  ("f1", "Bảng hai cột: ba việc có bằng chứng trong sáu năm đầu và đều miễn phí; ba thứ chưa có bằng chứng nhưng bán rất chạy.",
   "Ba thứ có bằng chứng vững nhất đều không bán được, vì chúng miễn phí.",
   "Đó là ý nghĩa hợp lý của chữ \"vàng\": **rẻ hơn khi làm sớm**, chứ không phải *không thể làm sau*."),
 ],
 "sau-den-muoi-hai-tuoi": [
  ("f1", "Bảng hai cột: bốn thứ làm suy giảm khả năng tự điều khiển bản thân là căng thẳng, thiếu ngủ, cô đơn và thiếu vận động; năm thứ nâng đỡ nó là ngủ đủ, vận động thật, có bạn thân, được giao việc nhà và giỏi được một thứ gì đó.",
   "Ba trong bốn thứ ở cột trái thường tăng lên khi ta thêm một lớp học nữa.",
   "Ba trong bốn thứ ấy thường tăng lên khi ta thêm lớp học."),
 ],
 "chin-thang-danh-sach-ngan": [
  ("f1", "Bảng hai cột về thai giáo: phần khoa học có thật gồm thai nhi nghe được từ tuần 26 đến 28 và nhận ra giọng mẹ; phần bị thổi phồng gồm hiệu ứng Mozart, tai nghe áp lên bụng bầu và DHA làm con thông minh hơn.",
   "Marketing trộn hai thứ vốn rất khác nhau vào làm một.",
   "Nếu bạn thích nghe nhạc khi mang bầu — cứ nghe. Có bằng chứng cho thấy nhạc **làm giảm lo âu của người mẹ**, và đó đã là lý do đủ tốt. Chỉ đừng mua nó như mua một khoản đầu tư vào chỉ số IQ của con."),
 ],
 "ky-luat-khong-phai-la-phat": [
  ("f1", "Bảng hai cột về hậu quả: cột trái là những hình phạt không liên quan tới việc con làm; cột phải là những hậu quả gắn trực tiếp với việc con làm.",
   "Điểm khác biệt không nằm ở nặng hay nhẹ, mà ở chỗ hậu quả có liên quan tới việc con làm hay không.",
   "Nhưng cột bên phải **giảm dần theo thời gian**, còn cột bên trái thì lặp lại mãi."),
 ],
 "man-hinh-tu-dem-gio-sang-thoa-thuan": [
  ("f1", "Sơ đồ hai bước: câu hỏi cũ là mấy tiếng một ngày là đủ; câu hỏi mới là màn hình có đang lấn vào giấc ngủ, bữa ăn và trò chuyện không.",
   "Trọng tâm đã dịch chuyển khỏi việc đếm giờ.",
   "Thay vào đó là mấy nguyên tắc gần với đời sống hơn: bảo vệ giấc ngủ và thời gian gia đình, trò chuyện với con về những gì con gặp trên mạng, người lớn làm gương, và nuôi những mối quan hệ ngoài đời."),
 ],
 "khi-con-da-truong-thanh": [
  ("f1", "Bảng hai cột phân biệt hỗ trợ và kiểm soát: hỗ trợ là giúp không kèm điều kiện; kiểm soát là giúp kèm theo một khoản nợ ngầm.",
   "Từ bên ngoài hai thứ trông giống nhau; khác nhau ở chỗ có kèm điều kiện hay không.",
   "Đưa tiền, cho lời khuyên khi được hỏi, để phòng cho con về ở lúc khó khăn — đó là **hỗ trợ**. Quyết định thay, gây áp lực, dùng sự giúp đỡ làm đòn bẩy — đó là **kiểm soát**. Hai thứ trông giống nhau từ bên ngoài và khác hẳn nhau từ bên trong."),
 ],
 "muoi-lam-phut-nhung-la-that": [
  ("f1", "Sơ đồ hai bước phân biệt có mặt hờ và có mặt thật: có mặt hờ là cùng phòng nhưng mắt ở điện thoại; có mặt thật là không màn hình, con dẫn chuyện, người lớn đáp đúng vào thứ con đang nói.",
   "Thứ đọng lại ở trẻ không phải số giờ, mà là những phút chúng biết chắc mình đang được chú ý.",
   None),
 ],
 "con-gian-va-minh-cung-gian": [
  ("f1", "Sơ đồ ba bước xử lý khi cả hai cùng đang nóng: hạ nhịp của chính mình trước, rồi gọi tên cảm xúc của con, rồi mới quay lại nói chuyện khi cả hai đã nguội.",
   "Thứ tự quan trọng hơn nội dung: mình trước, rồi mới tới con.",
   None),
 ],
 "khi-con-noi-con-chan-hoc": [
  ("f1", "Bảng hai cột: bên trái là câu con nói ra; bên phải là bốn khả năng có thể đang xảy ra bên dưới, gồm không theo kịp, theo kịp quá dễ, có chuyện với bạn bè hoặc thầy cô, và đang mệt quá tải.",
   "Cùng một câu nói có thể có bốn nghĩa rất khác nhau.",
   None),
 ],
 "cau-truc-thay-vi-nhac-nho": [
  ("f1", "Bảng hai cột: lời nhắc cần người lớn có mặt mới chạy; cấu trúc thì tự chạy, gồm giờ cố định, chuỗi việc cố định và một tấm bảng nhìn thấy được.",
   "Chừng nào còn có người nhắc, đứa trẻ không cần bộ nhắc của riêng nó.",
   None),
 ],
 "hoi-con-hoc-duoc-gi-thay-vi-hoi-may-diem": [
  ("f1", "Bảng hai cột so sánh hai câu hỏi: hỏi về điểm hướng sự chú ý ra ngoài về phía kết quả do người khác chấm; hỏi về điều học được hướng sự chú ý vào trong về thứ con vừa có thêm.",
   "Vấn đề không phải bỏ hẳn câu hỏi về điểm, mà là thứ tự hỏi.",
   None),
 ],
 "cam-giac-co-loi-vi-di-lam": [
  ("f1", "Bảng hai cột so sánh hai câu hỏi: câu hỏi cũ hầu như luôn cho ra câu trả lời chưa; câu hỏi mới chỉ vào một việc cụ thể và trả lời được.",
   "Một câu hỏi trả lời được thì hữu ích hơn một câu hỏi luôn cho ra cảm giác thiếu sót.",
   None),
 ],
 "khi-con-bat-dau-dong-cua-phong": [
  ("f1", "Sơ đồ hai bước: điều cha mẹ sợ khi con đóng cửa phòng, và điều thường đang thực sự xảy ra.",
   "Cánh cửa đóng lại thường là việc bình thường của tuổi này, không phải dấu hiệu quan hệ hỏng.",
   None),
 ],
 "tu-phan-thuong-den-dong-luc-ben-trong": [
  ("f1", "Sơ đồ ba chặng: làm vì được thưởng, làm vì thấy mình làm được, làm vì thấy có nghĩa.",
   "Không có công tắc nào chuyển thẳng từ chặng một sang chặng ba.",
   None),
 ],
}


def cover_alt(title, category):
    """Mô tả ảnh bìa cho người dùng trình đọc màn hình.

    Nháy kép thẳng trong tiêu đề phải đổi thành nháy cong, nếu không nó sẽ
    làm hỏng cú pháp của phần khai báo đầu bài (YAML dùng nháy kép để bọc chuỗi).
    """
    clean = title.replace('"', "”").replace("\\", "")
    return f"Ảnh bìa bài viết “{clean}” — chủ đề {category}"


def main():
    if not IMG.exists() or not list(IMG.glob("*-cover.png")):
        sys.exit("Chưa có hình. Chạy `python3 scripts/make-figures.py` trước đã.")

    n_cov = n_fig = 0
    problems = []

    for f in sorted(ART.glob("*.md*")):
        slug = f.name.rsplit(".", 1)[0]
        txt = f.read_text(encoding="utf-8")
        head, body = txt.split("---", 2)[1], txt.split("---", 2)[2]

        # ── 1. ảnh bìa ────────────────────────────────────────────────────
        if "coverImage:" not in head and (IMG / f"{slug}-cover.png").exists():
            title = (re.search(r'^title: *"?(.*?)"?$', head, re.M) or ["", ""])[1]
            title = title.replace('\\"', '"')
            cat = (re.search(r'^category: *"?(.*?)"?$', head, re.M) or ["", ""])[1]
            alt = cover_alt(title, cat)
            head = re.sub(r"\nfeatured: ",
                          f'\ncoverImage: "/images/articles/{slug}-cover.png"'
                          f'\ncoverAlt: "{alt}"\nfeatured: ',
                          head, count=1)
            n_cov += 1

        # ── 2. hình trong thân bài ────────────────────────────────────────
        for tag, alt, caption, anchor in PLAN.get(slug, []):
            svg = IMG / f"{slug}-{tag}.svg"
            if not svg.exists():
                problems.append(f"{slug}-{tag}: thiếu file hình")
                continue
            if f"{slug}-{tag}.svg" in body:
                continue  # đã chèn rồi
            block = (f'\n\n<Figure\n  src="/images/articles/{slug}-{tag}.svg"\n'
                     f'  alt="{alt}"\n  caption="{caption}" />\n')
            if anchor is None:
                # không có mốc → đặt ngay sau đoạn mở đầu (trước tiêu đề ## đầu tiên)
                m = re.search(r"\n## ", body)
                if not m:
                    problems.append(f"{slug}-{tag}: không tìm được chỗ đặt")
                    continue
                body = body[:m.start()] + block + body[m.start():]
            else:
                cnt = body.count(anchor)
                if cnt != 1:
                    problems.append(f"{slug}-{tag}: đoạn mốc khớp {cnt} lần (cần đúng 1)")
                    continue
                i = body.index(anchor) + len(anchor)
                body = body[:i] + block + body[i:]
            n_fig += 1

        f.write_text(f"---{head}---{body}", encoding="utf-8")

    print(f"✓ {n_cov} ảnh bìa · {n_fig} hình chèn vào thân bài")
    if problems:
        print(f"\n⚠ {len(problems)} chỗ chưa gắn được:")
        for p in problems:
            print("   " + p)
        sys.exit(1)


if __name__ == "__main__":
    main()
