# Patterns — quy ước vẽ wireframe

Áp dụng cho mọi màn trong `outputs/<du-an>/ui/screens/`. Mục tiêu: các màn nhìn như **một bộ**, người review tập trung vào nội dung, không vào màu sắc.

## 1. Màu
- Chỉ tông xám (`--wf-gray-*`). **Một** màu nhấn `--wf-accent` duy nhất, chỉ dùng cho `.wf-btn--primary`.
- Mỗi vùng màn hình tối đa **1** nút primary (nút hành động chính của vùng đó). Modal: nút primary ở footer.
- Trạng thái (badge, alert, statusbar) phân biệt bằng **kiểu** (solid / soft / outline / dashed, icon ✓ ! ✕), không bằng màu.

## 2. Khoảng cách (bội số 4px)
| Token | px | Dùng cho |
|---|---|---|
| `--wf-s2` | 8 | khoảng cách trong nhóm nhỏ (icon–text, các badge) |
| `--wf-s3` | 12 | giữa các phần tử cùng hàng, padding ô bảng |
| `--wf-s4` | 16 | giữa các field trong form, padding card |
| `--wf-s5` | 24 | giữa các khối/section, lề container |
| `--wf-s6` | 32 | giữa các vùng lớn của trang |
- Dùng class layout (`wf-stack`, `wf-row`, `wf-grid-*`, `wf-split`) thay vì margin lẻ. `style=""` chỉ dùng cho kích thước cụ thể (width cột, min-height).

## 3. Đặt nút
- **Storefront form/trang:** nút chính bên **phải** dưới form; nút quay lại/huỷ dạng `wf-btn--ghost` bên trái (`wf-row wf-row--between`). Mobile: nút chính full width (`wf-btn--block`).
- **Storefront tóm tắt (cart/checkout):** nút chính full width trong `sf-summary`.
- **Backend list:** nút "Mới" (primary) đầu tiên ở góc trái control panel.
- **Backend form:** nút hành động trạng thái nằm trái `be-form-header`, theo thứ tự: hành động chính (primary) → hành động phụ → huỷ (ghost). Statusbar bên phải. Chỉ hiện nút hợp lệ với trạng thái hiện tại.
- **Modal:** storefront: `[spacer] [Huỷ] [Xác nhận-primary]`. Backend (Odoo): `[Xác nhận-primary] [Huỷ]` bên trái.
- Nhãn nút là **động từ + đối tượng**: "Gửi yêu cầu", "Duyệt", "Tạo phiếu nhập kho". Không dùng "OK", "Submit".

## 4. Trạng thái màn hình
Mỗi trạng thái là một `<section class="wf-state" data-state="<key>" data-label="<Nhãn>">` chứa nguyên một `.wf-frame`.

| Trạng thái | `data-state` | Cách vẽ |
|---|---|---|
| Mặc định | `default` | Dữ liệu mẫu thực tế (tên người Việt, mã đơn, số tiền VND). Luôn là state đầu tiên. |
| Rỗng | `empty` | `wf-empty` có icon, tiêu đề, mô tả 1 câu, CTA nếu có hành động tiếp theo. |
| Loading | `loading` | `wf-skeleton` giữ bố cục (ưu tiên) hoặc `wf-loading` cho vùng nhỏ. |
| Lỗi validate | `error` | `wf-field--error` + `wf-error-text` dưới đúng field; `wf-alert--error` đầu form tóm tắt nếu ≥ 2 lỗi. |
| Lỗi hệ thống | `error-system` | `wf-alert--error` nêu nguyên nhân + hướng xử lý ("Thử lại", "Liên hệ CSKH"). |
| Thành công | `success` | `wf-toast` (hành động nhỏ) hoặc trang/khối xác nhận với `wf-alert--success` + mã tham chiếu (hành động lớn). |
| Nghiệp vụ | `<trang-thai>` (vd. `approved`) | Form backend ở trạng thái khác: statusbar + nút thay đổi tương ứng. |

- Key `data-state` là chữ thường không dấu, dùng làm hậu tố tên PNG (`SCR-03-xxx--empty.png`).
- Trạng thái chỉ khác một chi tiết nhỏ (vd. 1 field lỗi) vẫn vẽ nguyên frame để ảnh tự giải thích.

## 5. Nhãn & dữ liệu mẫu
- Tiếng Việt có dấu, viết hoa chữ cái đầu câu ("Yêu cầu đổi trả", không "YÊU CẦU ĐỔI TRẢ").
- Thuật ngữ khớp SRS mục 1.3. Tên trường trên màn hình khớp cột "Trường dữ liệu" trong Screen Inventory.
- Tiền: `249.000₫`. Ngày: `12/10/2026`, giờ `09:15`. Điện thoại: `0901 234 567`. Mã đơn Magento 9 chữ số `000001234`.
- Field bắt buộc: `wf-req` (storefront) / `be-field--required` (backend).
- Placeholder input là ví dụ, không lặp lại nhãn.

## 6. Bố cục chuẩn
- **Storefront:** `sf-header` → `sf-nav` → `wf-container` (breadcrumb → tiêu đề → nội dung) → `sf-footer`. Trang tài khoản dùng `sf-account`.
- **Backend list:** `be-app` → `be-topbar` → `be-body` (`be-sidebar` nếu module có nhiều menu) → `be-controlpanel` → `be-content` > `be-list`.
- **Backend form:** `be-topbar` → `be-controlpanel` (breadcrumb List › Bản ghi + pager) → `be-form-header` → `be-form-layout` (`be-sheet` + `be-chatter`).
- Ảnh sản phẩm/banner: luôn `wf-img` (ô xám gạch chéo). Không `<img src>`.

## 7. Chú thích nghiệp vụ
- Đặt `<span class="wf-anno">1</span>` cạnh phần tử cần giải thích; cuối state thêm `<div class="wf-notes"><ol><li>…(FR-xx)</li></ol></div>` (nằm **ngoài** `.wf-frame`, trong `.wf-state`).
- Chỉ chú thích quy tắc không nhìn thấy được (điều kiện hiển thị, tính toán, quyền). Tối đa ~5 chú thích/state.

## 8. Mobile (storefront)
- Không vẽ file riêng. Kit tự chuyển ở ≤ 600px: nav → `sf-burger`, grid 4 → 2 cột, sidebar ẩn, `wf-grid-*` → 1 cột.
- Bảng trên storefront dùng `wf-table wf-table--stack` + `data-label` ở mỗi `td` để thành dạng thẻ trên mobile.
- Phần tử chỉ cho desktop: `sf-hide-mobile`; chỉ cho mobile: `sf-show-mobile`.
