
## Định dạng Word theo mẫu DOTB FRS (12/11/2026)
- Mẫu: "DOTB | FUNCTIONAL REQUIREMENTS SPECIFICATION" (file PDF user gửi 12/11/2026). Áp cho mọi FRD Sprint 4.
- Cách làm: tải file Word đang có trên Drive (nội dung mới nhất của user) → `python3 tools/frs_format.py <file.docx>` → đẩy file mới lên Drive cùng tên. Script chỉ đổi trình bày, không đổi chữ:
  khổ Letter, đầu trang "DOTB | FUNCTIONAL REQUIREMENTS SPECIFICATION", chân trang "<BBA SMS | BBA CRM> · <tên tài liệu> · v<phiên bản> | Page N",
  tiêu đề "Functional Requirements Specification" + tên tính năng màu xanh, bảng thuộc tính → 3 dòng "Nhãn: giá trị",
  heading Calibri xanh, thân bài Arial 11pt, bảng chỉ kẻ ngang xanh, chữ bảng 8,5pt.
- FRD xuất mới từ Markdown: chạy `to_docx.py` như cũ rồi chạy thêm `tools/frs_format.py` trên file .docx.
