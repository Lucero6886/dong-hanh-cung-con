/* =============================================================================
 *  PHÂN LOẠI NỘI DUNG: CHỦ ĐỀ (CATEGORY) & HÀNH TRÌNH (JOURNEY)
 * =============================================================================
 *  NGUYÊN TẮC QUAN TRỌNG:
 *  Hệ thống là "content-driven" — chủ đề của website được quyết định bởi
 *  frontmatter trong các file bài viết, KHÔNG phải bởi file này.
 *
 *  File này chỉ bổ sung phần MÔ TẢ và THỨ TỰ cho những chủ đề bạn muốn chăm chút.
 *  Nếu bạn viết một bài với `category: "Một chủ đề hoàn toàn mới"` mà chưa khai
 *  báo ở đây, website VẪN tự tạo trang chủ đề đó với slug tự sinh.
 *  → Bạn không bao giờ bị kẹt vì danh sách cứng.
 * ========================================================================== */

import { slugify } from '../utils/slugify';

export interface CategoryMeta {
  /** Tên chính xác như viết trong frontmatter `category:` của bài viết. */
  name: string;
  /** Đường dẫn tuỳ chỉnh. Bỏ trống → tự sinh từ tên (bỏ dấu tiếng Việt). */
  slug?: string;
  /** Mô tả ngắn hiển thị trên trang chủ đề. */
  description: string;
  /** Thứ tự hiển thị (số nhỏ lên trước). */
  order: number;
}

export const CATEGORIES: CategoryMeta[] = [
  {
    name: 'Đồng hành cùng con',
    description:
      'Những góc nhìn nền tảng về vai trò của cha mẹ: có mặt, quan sát, và bước cùng con thay vì đi thay con.',
    order: 1,
  },
  {
    name: 'Động lực & thói quen',
    description:
      'Vì sao trẻ hành động? Cách nuôi dưỡng động lực bền vững và xây dựng thói quen mà không biến mọi việc thành giao dịch.',
    order: 2,
  },
  {
    name: 'Học tập & tự học',
    description:
      'Đồng hành với việc học của con: từ điểm số sang hiểu biết, từ nhắc nhở sang khả năng tự học.',
    order: 3,
  },
  {
    name: 'Giao tiếp cha mẹ – con',
    slug: 'giao-tiep',
    description:
      'Cách đặt câu hỏi, cách lắng nghe, cách nói điều khó nói — để cánh cửa trò chuyện giữa cha mẹ và con luôn mở.',
    order: 4,
  },
  {
    name: 'Cảm xúc & tâm lý',
    description:
      'Giúp trẻ gọi tên và điều tiết cảm xúc, và giúp cha mẹ giữ được sự bình tĩnh của chính mình.',
    order: 5,
  },
  {
    name: 'Kỷ luật tích cực',
    description:
      'Đặt giới hạn rõ ràng mà vẫn tôn trọng: kỷ luật hướng tới hiểu biết và tự điều chỉnh, không hướng tới sợ hãi.',
    order: 6,
  },
  {
    name: 'Tự lập & trách nhiệm',
    description:
      'Từng bước trao lại cho con quyền quyết định và phần việc của con, theo mức độ phù hợp với lứa tuổi.',
    order: 7,
  },
  {
    name: 'Công nghệ & trẻ em',
    description:
      'Thiết bị, màn hình và Internet trong đời sống gia đình: thoả thuận thay vì kiểm soát, đồng hành thay vì cấm đoán.',
    order: 8,
  },
  {
    name: 'Tuổi teen',
    description:
      'Giai đoạn con cần khoảng cách để trưởng thành — và vẫn cần cha mẹ ở gần theo một cách khác.',
    order: 9,
  },
  {
    name: 'Góc suy ngẫm của cha mẹ',
    description:
      'Những ghi chép, câu hỏi và tự vấn của người lớn trên hành trình làm cha mẹ.',
    order: 10,
  },
];

/** Trả về mô tả/slug của một chủ đề. Chủ đề chưa khai báo vẫn hoạt động bình thường. */
export function getCategoryMeta(name: string): Required<CategoryMeta> {
  const found = CATEGORIES.find((c) => c.name === name);
  if (found) {
    return {
      name: found.name,
      slug: found.slug ?? slugify(found.name),
      description: found.description,
      order: found.order,
    };
  }
  return { name, slug: slugify(name), description: '', order: 999 };
}

/* -----------------------------------------------------------------------------
 *  HÀNH TRÌNH (JOURNEY)
 * -----------------------------------------------------------------------------
 *  Hành trình gom bài viết theo TÌNH HUỐNG cha mẹ đang gặp, thay vì theo chủ đề
 *  học thuật. Một bài có thể thuộc nhiều hành trình.
 *
 *  Cách hoạt động: một bài thuộc hành trình nếu tag HOẶC category của nó khớp
 *  với `tags` / `categories` khai báo bên dưới. Không cần sửa gì trong bài viết.
 *
 *  Hành trình chưa có bài nào sẽ tự động ẩn khỏi trang chủ (không tạo trang trống).
 * -------------------------------------------------------------------------- */

export interface Journey {
  slug: string;
  title: string;
  description: string;
  /** Bài có bất kỳ tag nào trong danh sách này sẽ thuộc hành trình. */
  tags?: string[];
  /** Bài thuộc bất kỳ chủ đề nào trong danh sách này cũng được tính. */
  categories?: string[];
}

export const JOURNEYS: Journey[] = [
  {
    slug: 'khi-con-chua-co-dong-luc',
    title: 'Khi con chưa có động lực',
    description:
      'Con làm bài chỉ khi được nhắc, hoặc chỉ khi có phần thưởng. Nhóm bài này bàn về cách chuyển dần từ động lực bên ngoài sang động lực bên trong.',
    tags: ['động lực', 'phần thưởng', 'tự giác'],
  },
  {
    slug: 'khi-con-ngai-hoc',
    title: 'Khi con ngại học',
    description:
      'Con né tránh bài vở, sợ sai, hoặc học chỉ để đối phó. Nhóm bài này bàn về việc khôi phục ý nghĩa của việc học.',
    tags: ['tự học', 'học tiếng Anh', 'giáo dục'],
    categories: ['Học tập & tự học'],
  },
  {
    slug: 'khi-con-chua-tu-giac',
    title: 'Khi con chưa tự giác',
    description:
      'Việc của con vẫn đang là việc của cha mẹ. Nhóm bài này bàn về cách xây dựng cấu trúc và trao lại trách nhiệm.',
    tags: ['thói quen', 'trách nhiệm', 'tự giác'],
    categories: ['Tự lập & trách nhiệm'],
  },
  {
    slug: 'khi-kho-giao-tiep',
    title: 'Khi cha mẹ và con khó giao tiếp',
    description:
      'Câu chuyện dừng lại ở "bình thường ạ". Nhóm bài này bàn về cách mở lại cuộc trò chuyện.',
    tags: ['giao tiếp', 'cha mẹ'],
    categories: ['Giao tiếp cha mẹ – con'],
  },
  {
    slug: 'khi-con-buoc-vao-tuoi-teen',
    title: 'Khi con bước vào tuổi teen',
    description:
      'Con cần khoảng cách, nhưng vẫn cần chỗ dựa. Nhóm bài này bàn về việc điều chỉnh vai trò của cha mẹ.',
    tags: ['tuổi teen'],
    categories: ['Tuổi teen'],
  },
  {
    slug: 'khi-con-gap-that-bai',
    title: 'Khi con gặp thất bại',
    description:
      'Điểm kém, thua cuộc, bị từ chối. Nhóm bài này bàn về cách đồng hành để thất bại trở thành một phần của trưởng thành.',
    tags: ['cảm xúc', 'trách nhiệm'],
    categories: ['Cảm xúc & tâm lý'],
  },
];
