---
name: write-srs
description: Viết SRS (Software Requirements Specification) đầy đủ từ URD.md và brainstorm.md, tách theo phân hệ trong outputs/<du-an>/srs/*.md (script ghép thành SRS.md) - yêu cầu chức năng FR-xx, phi chức năng NFR-xx, tích hợp & mapping dữ liệu, Screen Inventory SCR-xx, user flow Mermaid, ma trận truy vết FR-SCR-URD tự sinh, Assumptions & Open Questions; kèm checklist tự review và script xuất SRS.docx bằng pandoc. Dùng sau write-urd trong srs-pipeline, hoặc khi user yêu cầu "viết SRS", "đặc tả yêu cầu phần mềm", "functional requirements", "xuất SRS ra Word". Keywords - SRS, software requirements specification, functional requirements, non-functional requirements, screen inventory, traceability matrix, integration mapping, Magento 2, Odoo, docx export, pandoc. Không hỏi user.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *), Bash(pandoc *)
---

# write-srs — Software Requirements Specification

## Input
- `outputs/<du-an>/URD.md` (bắt buộc), `outputs/<du-an>/brainstorm.md`, `inputs/<du-an>/`.

## File trong skill
| File | Dùng khi |
|---|---|
| `template-srs.md` | Khung nội dung từng mục SRS (dùng làm mẫu cho các file trong `srs/`). Template công ty (`templates/template-srs-company.md`) nếu có thì ưu tiên, nhưng **giữ đủ 9 mục** và định dạng mã. |
| `checklist.md` | Tự review sau khi viết xong và ở cuối pipeline. |
| `scripts/build_srs.py` | Ghép `srs/*.md` → `SRS.md`, tự sinh mục 8; `--index` in chỉ mục mã → file. |
| `scripts/split_srs.py` | Chuyển SRS.md một file (dự án cũ) sang `srs/` — chỉ dùng một lần. |
| `scripts/check_srs.py` | Kiểm tra tự động: mã trùng, thiếu AC, truy vết, placeholder, ảnh. Tự ghép lại nếu `srs/` mới hơn `SRS.md`. |
| `scripts/to_docx.py` | Xuất `SRS.md` → `SRS.docx` (pandoc), render Mermaid, nhúng ảnh. Tự ghép lại nếu cần. |

## Cấu trúc file — SRS tách theo phân hệ

Viết vào `outputs/<du-an>/srs/`, **không viết tay `SRS.md`** (file đó do `build_srs.py` sinh ra):

| File | Nội dung |
|---|---|
| `00-dau-trang.md` | `# SRS — <Tên>`, bảng thuộc tính (Phiên bản 0.1), bảng **Lịch sử phiên bản** |
| `01-gioi-thieu.md` | `## 1. Giới thiệu` |
| `02-tong-quan.md` | `## 2. Mô tả tổng quan` |
| `03-00-chuc-nang.md` | `## 3. Yêu cầu chức năng` + phần dùng chung (mô hình trạng thái, quy ước) |
| `03-NN-<phan-he>.md` | `### 3.N <Phân hệ>` + các `#### FR-xx — Tên` của phân hệ đó |
| `04-phi-chuc-nang.md` | `## 4. Yêu cầu phi chức năng` (`### NFR-xx — Tên`) |
| `05-tich-hop.md` | `## 5. Tích hợp & dữ liệu` |
| `06-man-hinh.md` | `## 6. Screen Inventory` (6.1 bảng, 6.2 ảnh wireframe) |
| `07-user-flow.md` | `## 7. User flow` |
| `09-gia-dinh-cau-hoi.md` | `## 9. Assumptions & Open Questions` |

- **Không có file `08`**: ma trận truy vết được sinh tự động từ dòng "Truy vết" của từng FR.
- **Phân hệ** = nhóm nghiệp vụ người dùng nhận ra (vd. "Yêu cầu mua hàng", "Báo giá", "Thanh toán"), 3–8 FR mỗi phân hệ. Mục đích: lần cập nhật sau chỉ phải mở 1–2 file khoảng 100 dòng.

## Cách viết

1. **Mục 1–2:** lấy từ URD + brainstorm. Thuật ngữ: mọi từ viết tắt xuất hiện trong tài liệu.
2. **Mục 3 — FR:** tách user story thành chức năng hệ thống. Một US có thể sinh nhiều FR, một FR có thể phục vụ nhiều US.
   - Heading đúng dạng `#### FR-01 — Tên` (script dựa vào dạng này). Mã FR đánh liên tục toàn tài liệu, không đánh lại theo phân hệ.
   - Đủ các trường: Mô tả, Vai trò, **Truy vết**, Input, Output, Business rules, Acceptance criteria, Độ ưu tiên.
   - Dòng Truy vết **bắt buộc** đúng dạng: `- **Truy vết:** US-01, US-02 · Màn hình: SCR-01, SCR-02` hoặc `· Màn hình: Không có UI`. Đây là nguồn duy nhất của ma trận truy vết.
   - Acceptance criteria Given/When/Then, đánh số, kiểm thử được. Kế thừa từ URD và chi tiết hoá ở mức hệ thống (trạng thái, thông báo lỗi cụ thể, giá trị giới hạn).
   - Chức năng chạy nền (job đồng bộ, email, cron) vẫn là FR, ghi `Màn hình: Không có UI`.
3. **Mục 4 — NFR:** tối thiểu các nhóm: hiệu năng, bảo mật/phân quyền, khả dụng, audit log, đa ngôn ngữ/định dạng (tiền tệ VND, ngày dd/mm/yyyy), tương thích trình duyệt/mobile. Ngưỡng số cụ thể; không có trong input → đề xuất + `AS-xx`.
4. **Mục 5 — Tích hợp:** mỗi hệ thống ngoài một dòng; API chính; bảng mapping trường giữa hai hệ thống (Magento ↔ Odoo…). Ghi rõ source of truth và cách xử lý lỗi đồng bộ.
5. **Mục 6 — Screen Inventory:**
   - 6.1: một dòng cho mỗi màn hình. Cột "Trạng thái" liệt kê trạng thái cần vẽ (Rỗng / Lỗi / Loading / Thành công / trạng thái nghiệp vụ như Chờ duyệt, Đã duyệt…). Cột "Loại" chỉ nhận `storefront` hoặc `backend`.
   - Gom màn hợp lý: list + form của cùng một đối tượng backend là 2 SCR; modal/wizard lớn là SCR riêng, modal xác nhận nhỏ vẽ chung trong màn cha (trạng thái).
   - 6.2: mỗi SCR một heading `#### SCR-xx — Tên`, mô tả ngắn và **dòng ảnh** `![SCR-xx — Tên](ui/png/SCR-xx-<slug>.png)`. Slug quyết định ở đây và dùng xuyên suốt (HTML, PNG). Ảnh được tạo ở bước render-screens; đường dẫn phải khớp.
6. **Mục 7 — User flow:** Mermaid `flowchart`. Ít nhất: luồng chính end-to-end + luồng ngoại lệ quan trọng. Node dùng tên màn (SCR-xx) khi có. Dùng cú pháp Mermaid đơn giản (không HTML trong label, không ký tự `"` lồng).
7. **Mục 8:** không viết — tự sinh.
8. **Mục 9:** gộp toàn bộ AS/OQ từ brainstorm + URD + phát sinh mới (đánh tiếp số). Cột "Ảnh hưởng tới" ghi FR/SCR liên quan.

## Sau khi viết
```bash
python .claude/skills/write-srs/scripts/build_srs.py <du-an>
python .claude/skills/write-srs/scripts/check_srs.py <du-an>
```
- Lúc này chưa có ảnh/HTML nên script chỉ cảnh báo (`WARN`) về ảnh — bình thường. Mọi `ERROR` phải sửa ngay (trong `srs/`, rồi ghép lại).
- Đi qua `checklist.md` phần "Nội dung".

## Xuất Word (chạy sau render-screens)
```bash
python .claude/skills/write-srs/scripts/to_docx.py <du-an>
```
- Dùng `templates/reference.docx` nếu có (style Word công ty).
- Tự render các khối ```` ```mermaid ```` thành PNG (`ui/diagrams/srs-*.png`) bằng mermaid-cli; không có mmdc thì giữ nguyên code block và cảnh báo.
- In ra số ảnh đã nhúng trong docx; báo lỗi nếu ảnh tham chiếu không tồn tại.

## Output
`outputs/<du-an>/srs/*.md` → `outputs/<du-an>/SRS.md` (sinh ra) → `SRS.docx` ở bước xuất.
