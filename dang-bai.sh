#!/usr/bin/env bash
# =============================================================================
#  ĐĂNG BÀI LÊN WEBSITE — chạy trong WSL Ubuntu
# =============================================================================
#  Cách dùng:   ./dang-bai.sh
#               ./dang-bai.sh "lời nhắn cho lần này"
#
#  Nó làm đúng việc mà GitHub Desktop vẫn làm, theo đúng thứ tự:
#     1. Liệt kê file nào đã đổi
#     2. CHO BẠN XEM từng chữ được thêm (xanh) / bỏ đi (đỏ)
#     3. HỎI Ý BẠN  ← bước quan trọng nhất, đừng bỏ
#     4. Commit và Push
#
#  Bước 3 chính là lý do có file này. Đưa việc đăng bài về dòng lệnh mà bỏ
#  bước xem lại thì mới là nguy hiểm — nút Push không phải thứ bảo vệ bạn,
#  việc NHÌN TRƯỚC KHI ĐĂNG mới là.
# =============================================================================

set -u

# Thư mục dự án = chính thư mục chứa file này. Nhờ vậy nếu bạn đổi chỗ hoặc
# đổi tên thư mục dự án, file này vẫn chạy đúng, không phải sửa gì.
DU_AN="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$DU_AN" || { echo "✗ Không vào được thư mục dự án:"; echo "  $DU_AN"; exit 1; }

# --- Kiểm tra vài thứ hay hỏng trước khi bắt đầu ---------------------------
if [ ! -d .git ]; then
  echo "✗ Thư mục này không phải dự án git:"
  echo "  $DU_AN"
  echo "  File dang-bai.sh phải nằm ngay trong thư mục dự án."
  exit 1
fi

if [ -f .git/index.lock ]; then
  echo "⚠ Có file khoá .git/index.lock — thường do GitHub Desktop đang mở."
  echo "  Hãy đóng GitHub Desktop rồi chạy lại. Nếu vẫn còn, xoá file đó đi:"
  echo "  rm '$DU_AN/.git/index.lock'"
  exit 1
fi

# --- 1. Có gì thay đổi không? ----------------------------------------------
if [ -z "$(git status --porcelain)" ]; then
  echo "✓ Không có gì thay đổi. Website đang khớp với bản trên mạng."
  exit 0
fi

echo "════════════════════════════════════════════════════════"
echo "  NHỮNG FILE ĐÃ THAY ĐỔI"
echo "════════════════════════════════════════════════════════"
git -c color.status=always status --short
echo

# --- 2. Xem từng chữ đổi ----------------------------------------------------
# Phải "git add" TRƯỚC khi xem, nếu không thì file MỚI (bài viết mới Claude
# vừa tạo) sẽ không hiện một chữ nào trong phần so sánh — git chỉ so sánh
# những file nó đã biết. Đây đúng là trường hợp bạn cần nhìn kỹ nhất.
# Nếu bạn trả lời "không" ở bước 3, dòng "git reset" phía dưới sẽ hoàn tác
# việc đánh dấu này, thư mục của bạn về đúng như trước khi chạy.
huy_danh_dau() { git reset --quiet >/dev/null 2>&1 || true; }
trap 'echo; echo "✓ Đã dừng giữa đường. Không có gì được đăng."; huy_danh_dau; exit 130' INT

git add -A || { echo "✗ Lỗi khi chuẩn bị file."; exit 1; }

echo "════════════════════════════════════════════════════════"
echo "  TỪNG CHỮ ĐƯỢC THÊM / BỎ ĐI"
echo "  (bấm phím cách để xem tiếp · bấm  q  để thoát ra)"
echo "════════════════════════════════════════════════════════"
read -rp "Bấm Enter để xem… "
git -c color.diff=always diff --staged \
    -- . ':(exclude)*.png' ':(exclude)*.svg' ':(exclude)*.jpg' | less -R
echo
echo "— Ảnh (.png, .svg, .jpg) không hiện ở trên vì là hình, không phải chữ."
echo "  Nếu có ảnh nào đổi, tên nó nằm ở danh sách đầu trang."
echo

# --- 3. Hỏi ý ---------------------------------------------------------------
echo "════════════════════════════════════════════════════════"
read -rp "Đăng những thay đổi này lên mạng?  (gõ  co  rồi Enter): " TRA_LOI
if [ "$TRA_LOI" != "co" ] && [ "$TRA_LOI" != "có" ]; then
  echo "✓ Đã dừng. Không có gì được đăng. Thư mục của bạn vẫn nguyên."
  huy_danh_dau
  exit 0
fi

# --- 4. Commit và push ------------------------------------------------------
trap - INT
LOI_NHAN="${1:-cập nhật nội dung}"
git commit -m "$LOI_NHAN" || { echo "✗ Lỗi khi ghi lại thay đổi."; exit 1; }

echo
echo "Đang đẩy lên GitHub…"
if git push; then
  echo
  echo "════════════════════════════════════════════════════════"
  echo "  ✓ XONG. Đã đăng."
  echo "════════════════════════════════════════════════════════"
  echo "  Lời nhắn : $LOI_NHAN"
  echo "  Mã lần này: $(git rev-parse --short HEAD)"
  echo
  echo "  Website tự dựng lại trong khoảng 2–3 phút:"
  echo "  https://lucero6886.github.io/dong-hanh-cung-con/"
  echo
  echo "  Xem quá trình dựng (nếu muốn chắc):"
  echo "  https://github.com/Lucero6886/dong-hanh-cung-con/actions"
else
  echo
  echo "✗ Đẩy lên KHÔNG thành công. Thay đổi đã được ghi lại ở máy bạn,"
  echo "  chỉ là chưa lên mạng. Không mất gì cả."
  echo
  echo "  Hai nguyên nhân hay gặp:"
  echo
  echo "  1. Chưa đăng nhập  (báo Authentication failed, hoặc hỏi mật khẩu)"
  echo "     → mở GitHub Desktop bấm Push một lần cho lần này,"
  echo "       rồi nhắn Claude để cài phần đăng nhập cho WSL."
  echo
  echo "  2. Trên mạng có thay đổi mới hơn  (báo rejected / non-fast-forward)"
  echo "     → thường do bạn đã sửa bài trực tiếp trên web GitHub. Gõ:"
  echo "         git pull --rebase"
  echo "       rồi chạy lại ./dang-bai.sh"
  exit 1
fi
