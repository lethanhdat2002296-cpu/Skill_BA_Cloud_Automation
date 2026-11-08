# Biên bản họp kickoff — Tính năng đổi trả hàng online

- **Thời gian:** 09:00–10:30, 06/10/2026
- **Hình thức:** Google Meet
- **Khách hàng (Mộc An Fashion — dữ liệu giả lập):** chị Hạnh (Trưởng CSKH), anh Tùng (Quản lý kho), chị Linh (Kế toán)
- **Nhà cung cấp:** BA Minh, Dev lead Khoa

## 1. Hiện trạng
- Website chạy **Magento 2.4.6** (Luma tuỳ biến), backend vận hành dùng **Odoo 17** (Sales, Inventory, Accounting). Đơn hàng từ Magento đã đồng bộ sang Odoo qua connector có sẵn (đồng bộ 5 phút/lần).
- Khách muốn đổi/trả phải gọi hotline hoặc nhắn fanpage. CSKH ghi vào Google Sheet, chụp ảnh khách gửi qua Zalo, rồi báo kho.
- Mỗi tháng khoảng **300–350 yêu cầu**, CSKH mất trung bình **3 ngày** để phản hồi. Nhiều khách khiếu nại vì không biết yêu cầu đang ở bước nào.
- Kế toán hoàn tiền thủ công dựa trên Sheet, hay bị sót hoặc hoàn trùng.

## 2. Mong muốn
- Khách tự tạo yêu cầu đổi/trả trên website, từ trang "Đơn hàng của tôi", chọn sản phẩm + số lượng + lý do, đính kèm ảnh.
- Chỉ đơn **đã giao thành công** và trong **7 ngày** kể từ ngày giao mới được tạo yêu cầu.
- Hàng sale > 50% **không** được trả, chỉ được đổi size.
- Yêu cầu tự đẩy sang Odoo để CSKH duyệt. Duyệt xong khách nhận email kèm hướng dẫn gửi hàng.
- Kho nhận hàng, kiểm tra tình trạng, xác nhận trên Odoo → nếu trả hàng thì kế toán hoàn tiền (credit note), nếu đổi thì tạo đơn đổi mới giá 0đ.
- Khách xem được trạng thái yêu cầu trên website (Mới → Chờ duyệt → Đã duyệt → Đã nhận hàng → Hoàn tất / Từ chối).
- Chị Hạnh muốn có báo cáo số yêu cầu theo lý do mỗi tháng để làm việc với nhà cung cấp.

## 3. Ý kiến các bên
- Anh Tùng: kho cần thấy danh sách hàng sắp về để chuẩn bị, và ghi được tình trạng hàng nhận (nguyên vẹn / lỗi / thiếu phụ kiện). Hàng lỗi thì không nhập lại kho bán.
- Chị Linh: hoàn tiền về phương thức thanh toán ban đầu nếu là thẻ/VNPay; đơn COD thì hoàn chuyển khoản, cần khách cung cấp số tài khoản. Chưa chốt ai nhập số tài khoản.
- Chị Hạnh: phí ship gửi trả do ai chịu thì "tuỳ trường hợp", sẽ gửi chính sách sau.

## 4. Việc cần làm
- [ ] Khách gửi chính sách đổi trả chính thức (hạn: 10/10).
- [ ] Nhà cung cấp gửi bản SRS + wireframe để review (hạn: 20/10).
- Go-live mong muốn: **trước 15/11/2026** để kịp mùa sale cuối năm.
