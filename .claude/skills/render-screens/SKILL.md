---
name: render-screens
description: Chụp wireframe HTML ra PNG (Playwright), kiểm tra layout, render sơ đồ Mermaid và swimlane vào Diagram/Flow/. Dùng sau wireframe hoặc khi user nói "chụp màn hình", "render sơ đồ".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *), Bash(npx mmdc *), Bash(mmdc *)
---

# render-screens — HTML → PNG + review bằng mắt

## Input
- `projects/<du-an>/Diagram/Wireframe/screens/*.html` (từ skill `wireframe`).
- `projects/<du-an>/Document/SRS/SRS.md` mục 6 (để đối chiếu trường/hành động).
- `projects/<du-an>/Diagram/Wireframe/flows.md` (Mermaid).

## Bước 1 — Chụp
```bash
python .claude/skills/render-screens/scripts/shot.py <du-an>
```
- Mỗi `.wf-state` một ảnh; storefront thêm ảnh `-mobile` ở 390px. Tên ảnh: xem docstring `shot.py` / `CLAUDE.md`.
- Script in `LAYOUT [...]` cho lỗi phát hiện tự động (tràn ngang, vượt mép frame, chữ bị cắt, nhãn nút xuống dòng) và danh sách ảnh để review.
- Lỗi "chưa cài Playwright" → chạy `pip install playwright` rồi `python -m playwright install --with-deps chromium` (hoặc xem `setup/cloud-setup.sh`), chạy lại. Không cài được → ghi vào báo cáo, bỏ qua bước này, **không dừng pipeline**.

## Bước 2 — Review bằng mắt (bắt buộc)
Mở **từng ảnh** bằng Read (ảnh default desktop của mọi màn + ảnh mobile của storefront + các state khác ít nhất lướt qua). Với mỗi ảnh, đối chiếu dòng SCR tương ứng trong Screen Inventory:

| Kiểm tra | Dấu hiệu lỗi |
|---|---|
| Layout | Cột chồng lên nhau, khối lệch, khoảng trắng lớn bất thường, footer giữa trang |
| Chữ | Tràn khỏi ô/nút, bị cắt, xuống dòng xấu ở nút/badge, ký tự lỗi font (ô vuông) |
| Đủ nội dung | Thiếu trường dữ liệu / hành động / trạng thái liệt kê trong Screen Inventory |
| Nhất quán | Nhãn khác thuật ngữ SRS; > 1 nút primary trong một vùng; dùng màu ngoài tông xám |
| Mobile (storefront) | Tràn ngang, bảng không chuyển dạng thẻ, nút chính bị đẩy khuất |

Có lỗi → sửa HTML (chỉ dùng class kit, theo `wireframe/design-kit/patterns.md`) → chụp lại riêng màn đó:
```bash
python .claude/skills/render-screens/scripts/shot.py <du-an> --only SCR-03
```
Lặp tới khi ảnh sạch (tối đa 3 vòng mỗi màn; còn lỗi thì ghi vào báo cáo cuối).

## Bước 3 — Render Mermaid
```bash
python .claude/skills/render-screens/scripts/render_mermaid.py <du-an>
```
- Ra `Diagram/Flow/flows-NN.png` (từ `Diagram/Wireframe/flows.md`) và `Diagram/Flow/srs-NN.png` (từ `SRS.md`).
- Mở xem 1–2 sơ đồ để chắc chắn render đúng. Lỗi cú pháp Mermaid → sửa khối Mermaid trong file nguồn (bỏ ký tự đặc biệt trong label, bọc label bằng `["..."]`), chạy lại.
- Không có mmdc/npx → script cảnh báo, giữ code Mermaid; ghi vào báo cáo.

## Bước 3b — Sơ đồ Activity – Swimlane (khi SRS cần)
Mermaid không vẽ được swimlane thẳng lane, nên dùng script riêng:
```bash
python .claude/skills/render-screens/scripts/swimlane.py <du-an>
```
- Đặc tả mỗi sơ đồ là một file `projects/<du-an>/Diagram/Flow/swimlanes/<ten>.json` (lane, bước, mũi tên — xem docstring script). Dùng `"orientation": "vertical"` (lane là cột) để vừa trang A4 khi nhúng Word; ≤ 6 lane và ≤ 12 bước mỗi sơ đồ, quy trình dài thì tách nhiều sơ đồ.
- Sơ đồ **BPMN**: thêm `"notation": "bpmn"` vào JSON → start event vòng mảnh, end event viền đậm, gateway thoi có ×, `type: "timer"` cho sự kiện hẹn giờ; nhánh gateway sang lane khác đi ra từ cạnh thoi. Đặt bước sao cho đường dọc trong lane đích không cắt qua bước khác.
- Ra `Diagram/Flow/swimlane-<ten>.png`; SRS tham chiếu bằng dòng ảnh `![…](Diagram/Flow/swimlane-<ten>.png)`.
- Mở xem từng ảnh: nhãn mũi tên không đè nhau, mũi tên không cắt qua bước.

## Bước 4 — Cập nhật gallery
`shot.py` tự chạy lại `wireframe/scripts/build_ui.py` để `Diagram/Wireframe/index.html` có thumbnail. Kiểm tra số ảnh: mỗi SCR trong SRS mục 6.2 phải có `Diagram/Wireframe/png/SCR-xx-<slug>.png`.

## Output
- `projects/<du-an>/Diagram/Wireframe/png/*.png`
- `projects/<du-an>/Diagram/Flow/*.png`
- `projects/<du-an>/Diagram/Wireframe/index.html` (cập nhật thumbnail)
