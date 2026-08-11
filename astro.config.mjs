// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

/*
 * Cấu hình build đọc thẳng từ src/config/site.ts để KHÔNG có hai nơi cùng khai
 * báo tên miền. Muốn đổi địa chỉ website → sửa duy nhất src/config/site.ts.
 */
import { DEPLOY } from './src/config/site.ts';

export default defineConfig({
  site: DEPLOY.siteUrl,
  base: DEPLOY.base,

  // Sinh thư mục dạng /articles/ten-bai/index.html — hợp với GitHub Pages.
  trailingSlash: 'ignore',
  build: { format: 'directory' },

  integrations: [
    mdx(),
    sitemap({
      filter: (page) => !page.includes('/404'),
    }),
  ],

  markdown: {
    shikiConfig: {
      // Hai bộ màu để khối code hợp với cả chế độ sáng và tối.
      themes: { light: 'github-light', dark: 'github-dark' },
      wrap: true,
    },
  },

  // Không nén HTML để giữ nguyên khoảng trắng có ý nghĩa trong tiếng Việt.
  compressHTML: true,
});
