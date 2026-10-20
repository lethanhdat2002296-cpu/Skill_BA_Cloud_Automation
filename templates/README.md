# templates/

## reference.docx (tùy chọn)
Style Word của công ty cho pandoc. Nếu có file `templates/reference.docx`, `to_docx.py` tự dùng.

Tạo từ style mặc định của pandoc rồi chỉnh trong Word:
```bash
pandoc -o templates/reference.docx --print-default-data-file reference.docx
```
Mở file trong Word → sửa **Styles** (Heading 1–3, Normal, Table, Caption, Title…), không cần sửa nội dung → lưu.

## Template SRS công ty (tùy chọn)
Đặt `templates/template-srs-company.md` nếu muốn thay `.claude/skills/write-srs/template-srs.md`.
Phải giữ đủ 9 mục (`## 1.` … `## 9.`) và định dạng mã `### FR-xx — Tên`, bảng Screen Inventory, dòng ảnh `ui/png/SCR-xx-<slug>.png` để `check_srs.py` và `to_docx.py` hoạt động.
