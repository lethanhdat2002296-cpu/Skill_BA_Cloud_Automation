---
name: wireframe
description: Vẽ wireframe HTML low/mid-fidelity tông xám cho từng màn hình SCR-xx từ ui/flows.md và Screen Inventory của SRS, chỉ dùng component trong design kit (storefront kiểu Magento 2, backend kiểu Odoo), vẽ đủ trạng thái (mặc định, rỗng, lỗi, loading, thành công), desktop 1440px và mobile 390px cho storefront, kèm trang gallery ui/index.html. Dùng sau ui-spec trong srs-pipeline, hoặc khi user yêu cầu "vẽ wireframe", "mockup màn hình", "phác thảo UI", "dựng màn hình HTML". Keywords - wireframe, mockup, low-fidelity, HTML prototype, design kit, Magento storefront, Odoo backend, list view, form view, chatter, screen states. Không hỏi user.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *)
---

# wireframe — HTML từ design kit

## Input
- `outputs/<du-an>/ui/flows.md` (mục 3: danh sách màn + bố cục) — bắt buộc.
- `outputs/<du-an>/SRS.md` mục 6 (trường, hành động, trạng thái, FR).
- Design kit trong thư mục skill này:
  - `design-kit/tokens.css` — **toàn bộ** CSS (token + component). Không viết CSS mới.
  - `design-kit/components-storefront.html` — markup mẫu storefront.
  - `design-kit/components-backend.html` — markup mẫu backend.
  - `design-kit/patterns.md` — quy ước khoảng cách, đặt nút, trạng thái, nhãn. **Đọc trước khi vẽ.**

## Cách làm

1. Đọc `patterns.md` và file component tương ứng loại màn (đọc một lần, dùng cho mọi màn).
2. Với mỗi SCR trong `flows.md` mục 3, tạo `outputs/<du-an>/ui/screens/SCR-xx-<slug>.html` theo khung bên dưới:
   - Copy khối markup từ kit, đổi nhãn/dữ liệu cho đúng nghiệp vụ. **Chỉ dùng class có trong `tokens.css`.** `style=""` chỉ cho kích thước (width, min-height, grid-template-columns).
   - Mỗi trạng thái trong cột "Trạng thái" của Screen Inventory là một `<section class="wf-state">` chứa nguyên một `.wf-frame`. State đầu tiên luôn là `default`.
   - Mọi trường và hành động trong Screen Inventory phải xuất hiện trên state `default` (hoặc state phù hợp).
   - Dữ liệu mẫu thực tế (tên người Việt, mã đơn, VND) theo `patterns.md` mục 5.
   - Không `<img>`, không link/font/script ngoài. Ảnh → `<span class="wf-img"></span>`.
3. Chạy script đồng bộ asset + kiểm tra + tạo gallery:
   ```bash
   python .claude/skills/wireframe/scripts/build_ui.py <du-an>
   ```
   Script: copy `tokens.css` vào `ui/assets/`, kiểm tra từng màn (comment đầu file, meta, class lạ, URL ngoài, `<img>`, state), so khớp với ảnh dự kiến trong SRS mục 6.2, và sinh `ui/index.html`. Sửa mọi `ERROR`; `WARN` class lạ → thay bằng class của kit.
4. Màn nào cần thông tin không có trong SRS → tự quyết theo `patterns.md`, cập nhật Screen Inventory trong SRS.md và thêm `AS-xx`/`OQ-xx` nếu là quyết định nghiệp vụ.

## Khung file màn hình

```html
<!doctype html>
<!--
  SCR-03 — Chi tiết yêu cầu đổi trả
  FR: FR-05, FR-06, FR-07
  Loại: backend · Khung: 1440
  Trạng thái: default, approved, error
  Nguồn: SRS.md mục 6 · ui/flows.md mục 3
-->
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="wf-screen" content="SCR-03">
<meta name="wf-type" content="backend">
<meta name="wf-fr" content="FR-05, FR-06, FR-07">
<title>SCR-03 — Chi tiết yêu cầu đổi trả</title>
<link rel="stylesheet" href="../assets/tokens.css">
</head>
<body>
<div class="wf-doc-header"><strong>SCR-03 · Chi tiết yêu cầu đổi trả</strong><span class="wf-doc-meta">backend · FR-05, FR-06, FR-07</span></div>

<section class="wf-state" data-state="default" data-label="Chờ duyệt">
  <div class="wf-frame">
    <!-- markup copy từ kit -->
  </div>
  <div class="wf-notes"><ol><li>Nút "Duyệt" chỉ hiện với nhóm Quản lý CSKH (FR-06).</li></ol></div>
</section>

<section class="wf-state" data-state="error" data-label="Lỗi: thiếu lý do từ chối">
  <div class="wf-frame">…</div>
</section>
</body>
</html>
```

Quy tắc khung:
- `wf-type` = `storefront` hoặc `backend` (khớp cột "Loại" SRS). Storefront được chụp thêm ở 390px — kit tự responsive, **không** vẽ file mobile riêng; kiểm tra bố cục mobile bằng các class `sf-*` và `wf-table--stack`.
- `data-state`: chữ thường không dấu (`default`, `empty`, `loading`, `error`, `success`, `approved`…), là hậu tố tên PNG.
- `data-label`: nhãn tiếng Việt hiển thị trên ảnh.
- Modal/toast: đặt trong `.wf-frame` (frame có `position: relative`), modal dùng `.wf-overlay`.

## Gallery `ui/index.html`
Do `build_ui.py` sinh tự động (nhóm storefront/backend, thumbnail PNG nếu đã render, link tới HTML, FR, các state). Không sửa tay — chạy lại script.

## Output
- `outputs/<du-an>/ui/screens/SCR-xx-<slug>.html`
- `outputs/<du-an>/ui/assets/tokens.css`
- `outputs/<du-an>/ui/index.html`
