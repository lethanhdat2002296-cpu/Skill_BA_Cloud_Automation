# Checklist tự review SRS

Đánh dấu từng mục. Mục không đạt → sửa ngay rồi đánh dấu lại. Ghi số mục đạt vào báo cáo cuối pipeline.

`check_srs.py` tự kiểm các mục có ký hiệu ⚙. Các mục còn lại Claude tự đọc và đánh giá.

## A. Cấu trúc
- [ ] ⚙ Đủ 9 mục (Giới thiệu → Assumptions & Open Questions), đúng thứ tự.
- [ ] ⚙ Không còn placeholder: `{{`, `}}`, `TODO`, `TBD`, `xxx`, `Lorem`, `…` đứng một mình trong ô bảng.
- [ ] ⚙ Mã không trùng: FR, NFR, SCR, AS, OQ.
- [ ] Mã đánh liên tục, không nhảy cóc vô lý.

## B. Yêu cầu chức năng
- [ ] ⚙ Mỗi FR có mục **Acceptance criteria** với ít nhất 1 tiêu chí.
- [ ] Acceptance criteria dạng Given/When/Then, kiểm thử được, có dữ liệu mẫu cụ thể.
- [ ] ⚙ Không có từ mơ hồ trong AC / BR / NFR ("nhanh", "thân thiện", "phù hợp", "có thể", "v.v." — `tools/ba_lint.py`).
- [ ] ⚙ FR `Must` có AC lỗi / ngoại lệ; có ngưỡng thì có AC biên.
- [ ] ⚙ Thông báo hệ thống viết nguyên văn `hiện lỗi "…"` (gom vào 8.2 Danh mục thông báo).
- [ ] Mỗi FR có Input, Output, Business rules, Độ ưu tiên.
- [ ] Luồng ngoại lệ (từ chối, huỷ, quá hạn, lỗi tích hợp) có FR hoặc AC tương ứng.
- [ ] Mọi user story `Must` trong URD được phủ bởi ít nhất 1 FR.
- [ ] Rà lỗ hổng (gap): huỷ giữa chừng, quá hạn/timeout, lỗi tích hợp (mất kết nối, dữ liệu trả về thiếu), sai quyền, dữ liệu biên (0, âm, rỗng, trùng), hai người thao tác cùng lúc (cùng duyệt, cùng sửa).
- [ ] Chứng từ có ≥ 3 trạng thái có sơ đồ + bảng chuyển trạng thái (3.0); mỗi chuyển trạng thái có FR.

## C. Truy vết
- [ ] ⚙ Mỗi FR có ít nhất một SCR hoặc ghi rõ `Không có UI` trong ma trận truy vết.
- [ ] ⚙ Mọi SCR trong ma trận đều tồn tại trong Screen Inventory, và ngược lại mỗi SCR phục vụ ít nhất 1 FR.
- [ ] ⚙ Mọi US được tham chiếu đều tồn tại trong URD.md.
- [ ] Trường "Truy vết" trong từng FR khớp với dòng tương ứng trong ma trận.

## D. Phi chức năng & tích hợp
- [ ] NFR có ngưỡng đo được (giây, %, số người dùng, thời gian lưu trữ).
- [ ] Có NFR về bảo mật/phân quyền và audit log; mục 2.2 có ma trận phân quyền (đối tượng × vai trò).
- [ ] Có model / trường mới → mục 5.4 Từ điển dữ liệu đủ tên kỹ thuật, kiểu, bắt buộc.
- [ ] Mỗi tích hợp ghi rõ chiều, tần suất, xử lý lỗi, source of truth.
- [ ] Bảng mapping trường có kiểu dữ liệu.

## E. Màn hình & wireframe
- [ ] Mỗi SCR có cột Trạng thái và cột Loại (`storefront` / `backend`).
- [ ] ⚙ Mỗi SCR có dòng ảnh `Diagram/Wireframe/png/SCR-xx-<slug>.png` trong mục 6.2 và file ảnh tồn tại (sau render).
- [ ] ⚙ Mỗi SCR có file `Diagram/Wireframe/screens/SCR-xx-<slug>.html` (sau wireframe).
- [ ] Wireframe hiển thị đủ trường dữ liệu và hành động liệt kê trong Screen Inventory.
- [ ] Nhãn trên wireframe khớp thuật ngữ trong SRS.

## F. Assumptions & Open Questions
- [ ] ⚙ Có giả định (AS) thì mục Câu hỏi mở (OQ) không rỗng.
- [ ] Mỗi OQ có người cần trả lời và phạm vi ảnh hưởng.
- [ ] Không có giá trị bịa (giá, SLA, số lượng) mà không gắn AS.

## G. Xuất bản
- [ ] `SRS.docx` tồn tại, mở được, ảnh wireframe hiện trong docx (to_docx.py báo số ảnh nhúng ≥ số SCR).
- [ ] Sơ đồ Mermaid hiện dạng ảnh trong docx (hoặc ghi rõ thiếu mmdc).
