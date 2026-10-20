---
name: write-srs
description: Viết SRS (Software Requirements Specification) đầy đủ từ URD.md và brainstorm.md - yêu cầu chức năng FR-xx, phi chức năng NFR-xx, tích hợp & mapping dữ liệu, Screen Inventory SCR-xx, user flow Mermaid, ma trận truy vết FR-SCR-URD, Assumptions & Open Questions; kèm checklist tự review và script xuất SRS.docx bằng pandoc. Dùng sau write-urd trong srs-pipeline, hoặc khi user yêu cầu "viết SRS", "đặc tả yêu cầu phần mềm", "functional requirements", "xuất SRS ra Word". Keywords - SRS, software requirements specification, functional requirements, non-functional requirements, screen inventory, traceability matrix, integration mapping, Magento 2, Odoo, docx export, pandoc. Không hỏi user.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *), Bash(pandoc *)
---

# write-srs — Software Requirements Specification

## Input
- `outputs/<du-an>/URD.md` (bắt buộc), `outputs/<du-an>/brainstorm.md`, `inputs/<du-an>/`.

## File trong skill
| File | Dùng khi |
|---|---|
| `template-srs.md` | Khung SRS. Nếu repo có template công ty (vd. `templates/template-srs-company.md`) thì dùng template đó thay thế, nhưng **giữ đủ 9 mục** và định dạng mã bên dưới. |
| `checklist.md` | Tự review sau khi viết xong và ở cuối pipeline. |
| `scripts/check_srs.py` | Kiểm tra tự động: mã trùng, thiếu AC, truy vết, placeholder, ảnh. |
| `scripts/to_docx.py` | Xuất `SRS.md` → `SRS.docx` (pandoc), render Mermaid, nhúng ảnh. |

## Cách viết

1. **Mục 1–2:** lấy từ URD + brainstorm. Thuật ngữ: mọi từ viết tắt xuất hiện trong tài liệu.
2. **Mục 3 — FR:** tách user story thành chức năng hệ thống. Một US có thể sinh nhiều FR, một FR có thể phục vụ nhiều US.
   - Heading đúng dạng `### FR-01 — Tên` (script dựa vào dạng này).
   - Đủ các trường: Mô tả, Vai trò, Truy vết, Input, Output, Business rules, Acceptance criteria, Độ ưu tiên.
   - Acceptance criteria Given/When/Then, đánh số, kiểm thử được. Kế thừa từ URD và chi tiết hoá ở mức hệ thống (trạng thái, thông báo lỗi cụ thể, giá trị giới hạn).
   - Chức năng chạy nền (job đồng bộ, email, cron) vẫn là FR, ghi `Màn hình: Không có UI`.
3. **Mục 4 — NFR:** tối thiểu các nhóm: hiệu năng, bảo mật/phân quyền, khả dụng, audit log, đa ngôn ngữ/định dạng (tiền tệ VND, ngày dd/mm/yyyy), tương thích trình duyệt/mobile. Ngưỡng số cụ thể; không có trong input → đề xuất + `AS-xx`.
4. **Mục 5 — Tích hợp:** mỗi hệ thống ngoài một dòng; API chính; bảng mapping trường giữa hai hệ thống (Magento ↔ Odoo…). Ghi rõ source of truth và cách xử lý lỗi đồng bộ.
5. **Mục 6 — Screen Inventory:**
   - 6.1: một dòng cho mỗi màn hình. Cột "Trạng thái" liệt kê trạng thái cần vẽ (Rỗng / Lỗi / Loading / Thành công / trạng thái nghiệp vụ như Chờ duyệt, Đã duyệt…). Cột "Loại" chỉ nhận `storefront` hoặc `backend`.
   - Gom màn hợp lý: list + form của cùng một đối tượng backend là 2 SCR; modal/wizard lớn là SCR riêng, modal xác nhận nhỏ vẽ chung trong màn cha (trạng thái).
   - 6.2: mỗi SCR một heading `#### SCR-xx — Tên`, mô tả ngắn và **dòng ảnh** `![SCR-xx — Tên](ui/png/SCR-xx-<slug>.png)`. Slug quyết định ở đây và dùng xuyên suốt (HTML, PNG). Ảnh được tạo ở bước render-screens; đường dẫn phải khớp.
6. **Mục 7 — User flow:** Mermaid `flowchart`. Ít nhất: luồng chính end-to-end + luồng ngoại lệ quan trọng. Node dùng tên màn (SCR-xx) khi có. Dùng cú pháp Mermaid đơn giản (không HTML trong label, không ký tự `"` lồng).
7. **Mục 8 — Ma trận truy vết:** mỗi FR một dòng: FR | Tên | US | SCR (hoặc `Không có UI`).
8. **Mục 9:** gộp toàn bộ AS/OQ từ brainstorm + URD + phát sinh mới (đánh tiếp số). Cột "Ảnh hưởng tới" ghi FR/SCR liên quan.

## Sau khi viết
```bash
python .claude/skills/write-srs/scripts/check_srs.py <du-an>
```
- Lúc này chưa có ảnh/HTML nên script chỉ cảnh báo (`WARN`) về ảnh — bình thường. Mọi `ERROR` phải sửa ngay.
- Đi qua `checklist.md` phần "Nội dung".

## Xuất Word (chạy sau render-screens)
```bash
python .claude/skills/write-srs/scripts/to_docx.py <du-an>
```
- Dùng `templates/reference.docx` nếu có (style Word công ty).
- Tự render các khối ```` ```mermaid ```` thành PNG (`ui/diagrams/srs-*.png`) bằng mermaid-cli; không có mmdc thì giữ nguyên code block và cảnh báo.
- In ra số ảnh đã nhúng trong docx; báo lỗi nếu ảnh tham chiếu không tồn tại.

## Output
`outputs/<du-an>/SRS.md` (và `SRS.docx` ở bước xuất).
