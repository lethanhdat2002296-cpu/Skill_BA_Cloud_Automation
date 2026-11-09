# Đối chiếu mã — {{Tên dự án}}

> Sinh khi nhập tài liệu có sẵn (skill `doc-import`). Mỗi yêu cầu / mục của tài liệu gốc có **một dòng**; không có dòng = bị sót.
> Kiểm tra: `python .claude/skills/doc-import/scripts/check_import.py {{du-an}}`.
> Xử lý: **Giữ** (nội dung giữ nguyên ý) · **Viết lại** (đổi câu chữ cho đo được, ý không đổi) · **Tách** (1 mã gốc → nhiều mã mới) · **Gộp vào <mã gốc>** · **Bỏ: <lý do>** · **Mâu thuẫn → OQ-xx**.

## {{ten-file-goc.docx}} — {{FSD}} v{{1.2}} · {{tác giả / đơn vị}} · {{ngày tài liệu}}

| Mã gốc | Mục gốc | Nội dung (tóm tắt) | Mã mới | Xử lý |
|---|---|---|---|---|
| {{REQ-012}} | {{§3.2 Duyệt đơn mua hàng}} | {{Trưởng phòng duyệt đơn trên 50 triệu}} | {{FR-02 · BR-02.1}} | {{Giữ}} |
| {{REQ-013}} | {{§3.2}} | {{Gửi email khi duyệt}} | {{FR-16}} | {{Tách: email → FR-16, activity → FR-02}} |
| {{—}} | {{§4.1 Báo cáo tồn kho}} | {{…}} | {{—}} | {{Bỏ: ngoài phạm vi giai đoạn 1 (AS-03)}} |
