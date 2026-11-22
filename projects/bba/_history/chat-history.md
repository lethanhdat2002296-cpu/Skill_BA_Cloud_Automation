# Lịch sử hỏi đáp — BBA Sprint 4

> Ghi lại từng câu hỏi của user và câu trả lời của Claude, theo thứ tự thời gian. Mới nhất ở cuối.

---

## 22/11/2026 — Làm lại tài liệu BBA-71 → BBA-77

**User:**
> Tạm thời đã ổn.
> Giờ các tài liệu từ BBA-71 đến BBA-77
> 1. Theo format của các tài liệu trước
> 2. Nội dung làm kỹ theo tiêu đề của task.
> 3. Khi tham khảo Prototype và test thử trên đó. Các tính năng nào không dính líu đến nội dung của task thì bỏ qua không mô tả nó
> 4. Mỗi câu hỏi của tao và câu trả lời của mày hãy lưu history lại trên github nhé.

**Claude:**
Đã viết lại 7 tài liệu theo format BBA-50/66/51/52 (mỗi tính năng một User Story; FR ngắn, quy tắc ở BR/VAL/DATA; bỏ mục Giả định và Tài liệu tham khảo; câu hỏi đã có câu trả lời thì xoá). Đã đọc comment của Hải trên Drive, task trên Plane và thử trên prototype; tính năng không thuộc task thì bỏ. Mới sửa trên máy, chưa đẩy Drive / Git (chờ "update").

| Ticket | User Story | Thay đổi chính |
|---|---|---|
| BBA-71 Consent | 3: danh sách consent của trẻ theo phiên bản; tạo và gửi; gửi lại và nhắc | Theo comment Hải; bỏ Consent compliance, phát hành phiên bản mới, rút lại, checklist; nhắc tối đa 1 lần/ngày; chỉ sửa consent khi chưa ai trả lời (prototype) |
| BBA-72 Bulk promotion | 3: chọn lớp đích và ngày hiệu lực; xem trước trẻ và tác động; xác nhận và kết quả | Theo comment Hải: lớp cũ giữ danh sách trẻ, cập nhật trạng thái trẻ trong lớp và trạng thái lớp; tạo lớp đích ngay trong luồng (prototype) |
| BBA-73 Handover | 3: ghi người đưa; ghi người đón; quản lý thông tin đưa / đón | Theo comment Hải: ghi nhận và quản lý trên SMS; bỏ iPad / mất mạng; không ấn định sáng / chiều |
| BBA-74 Temperature | 3: ghi lần đo; cảnh báo sốt và lần đo còn thiếu; xem, sửa, phụ huynh xem | Bỏ °F, Bluetooth, iPad, xuất Excel |
| BBA-75 Late flag | 3: giờ chốt; tự đánh dấu Late nội bộ; báo cáo đến muộn | Bỏ đón muộn; thêm OQ về "Mark late — teacher judgement" của prototype |
| BBA-76 Overview today | 2: bảng tổng hợp theo Centre / brand; mở xuống lớp | District Manager → Cluster Head |
| BBA-77 Attendance correction | 3: sửa trạng thái; sửa giờ; lịch sử sửa | Thêm Void có lý do + xác nhận, Absent cần lý do và người báo (prototype) |
