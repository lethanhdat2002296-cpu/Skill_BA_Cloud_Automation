# Biên bản khảo sát lần 3 — Phiếu "Yêu cầu báo giá"

| Thuộc tính | Giá trị |
|---|---|
| Nguồn | Chat (BA dự án) |
| Ngày tài liệu | không ghi |
| Ngày nạp | 2026-10-20 |
| Loại | Biên bản khảo sát (ghi chú BA) — triển khai theo Scrum, mô tả từng tính năng |

## Tóm tắt
- Vật tư "Dịch vụ": không tạo YCMH, không tạo Yêu cầu báo giá; tạo thẳng PO, bắt buộc tạo Đề nghị thanh toán trước khi duyệt; duyệt xong không tạo DO.
- Vật tư "Nhập kho": nhập báo giá xong bắt buộc tạo Đề nghị thanh toán rồi mới được duyệt; duyệt xong chuyển trạng thái PO và tự động tạo phiếu DO.
- Phiếu Yêu cầu báo giá kế thừa đầu phiếu và chi tiết từ Yêu cầu mua hàng; bổ sung Nhà cung cấp (phải xác định chính xác), Ngày dự kiến nhận hàng, Ngày nhận hàng thực tế, mã theo mẫu "Mã phòng ban-PO-XXXX-DD-MM-YYYY", lưu ngầm mã phiếu cũ.
- Nút "Send email": chọn nhiều nhà cung cấp (ngăn cách bằng ";"), soạn như email thường, hệ thống tách gửi riêng từng nhà cung cấp.
- So sánh giá: NCC reply email kèm file Excel báo giá; Odoo tự lưu, tự đọc Excel (NCC – Vật tư – Giá); nút xem so sánh giá.

## Nội dung có cấu trúc

### Dành cho vật tư "Dịch vụ"
1. Đã ghi trước đó: vật tư "Dịch vụ" không cần tạo phiếu YCMH.
2. Bổ sung: không cần tạo "Yêu cầu báo giá"; tạo thẳng PO rồi làm quy trình duyệt bình thường.
3. Sau khi tạo PO, user bắt buộc tạo "Đề nghị thanh toán" trước rồi mới được duyệt.
4. Không tạo DO sau khi duyệt xong.

### Dành cho vật tư "Nhập kho"
1. Sau khi xin được báo giá về và nhập vào, user bắt buộc tạo "Đề nghị thanh toán" rồi mới được phép đến bước duyệt.
2. Duyệt xong chuyển sang trạng thái PO và tự động tạo phiếu DO.

### Thông tin trong phiếu "Yêu cầu báo giá"
1. Kế thừa thông tin từ "Yêu cầu mua hàng" sang "Yêu cầu báo giá".
2. Đầu phiếu bổ sung:
   1. Nhà cung cấp (đã phải xác định chính xác).
   2. Ngày dự kiến nhận hàng.
   3. Ngày nhận hàng thực tế.
   4. Mã "Yêu cầu mua hàng" — format: "Mã phòng ban- PO - XXXX - DD - MM - YYYY".
   5. Các thông tin còn lại kế thừa từ "Yêu cầu mua hàng".
   6. Lưu ngầm mã phiếu cũ để tiện truy vấn.
3. Chi tiết phiếu: kế thừa các thông tin từ "Yêu cầu mua hàng".

### Chức năng
1. **Gửi email xin báo giá đến các nhà cung cấp:** màn hình "Yêu cầu báo giá" có button "Send email". Bấm vào mở popup: gửi đến nhà cung cấp nào (chọn nhiều, ngăn cách bằng ";"), tiêu đề, nội dung… như gửi email bình thường. Khác biệt: gửi đến N nhà cung cấp nhưng khi gửi sẽ tách từng nhà cung cấp ra gửi riêng.
2. **So sánh giá:** nhà cung cấp reply email → Odoo tự lưu câu trả lời và tự đính kèm file Excel báo giá. Hệ thống tự đọc file Excel lấy NCC – Vật tư – Giá. Có button cho user bấm để xem so sánh giá.

### Việc cần làm
- Cập nhật lại các quy trình theo sơ đồ Activity – Swimlane.
- "Trước mắt đến đây đã" — các phần khác khảo sát tiếp.

## Nguyên văn

```text
Update tiếp theo: Hiện tại, tao đang triển khai theo quy trình Scrum thành ra sẽ đi từng tính năng và mô tả chi tiết nhất có thể
Về phiếu "Yêu cầu báo giá"

* Dành cho "Dịch vụ"

1. Trước đó tao nhớ có note lại thông tin là. Đối với loại vật tư "Dịch vụ" không cần tạo phiếu YCMH. Giờ update thêm là sẽ không cần tạo "Yêu cầu báo giá" . Mà sẽ tạo thẳng ra PO luôn rồi sẽ làm quy trình duyệt bình thường. Tuy nhiên, đối với loại "Dịch vụ" sau khi tạo PO xong, User sẽ phải tạo luôn cả "Đề nghị thanh toán" Bắt buộc tạo "Đề nghị thanh toán" trước rồi mới được duyệt. Và sẽ không tạo DO sau khi duyệt xong

* Dành cho "Nhập kho"

1. Đối với loại vật tư "Nhập kho", sau khi đã xin được báo giá về nhập vô, User cũng phải bắt buộc tạo "Đề nghị thanh toán" rồi mới được phép đến bước duyệt. Duyệt xong sẽ chuyển sang trạng thái PO. Và tụ động tạo phiếu DO

* Thông tin trong phiếu

1. Kế thừa thông tin từ "Yêu cầu mua hàng" sang "Yêu cầu báo giá"
2. Ở đầu phiếu: Bổ sung thêm các thông tin cần thiết. 
   1. Nhà cung cấp (Này đã phải xác định chính xác) 
   2. Ngày dự kiến nhận hàng:
   3. Ngày nhận hàng thực tế
   4. Mã "Yêu cầu mua hàng" - Format như sau: "Mã phòng ban- PO - XXXX - DD - MM - YYYY"
   5. Các thông tin còn lại kế thừa từ "Yêu cầu mua hàng"
   6. Lưu ngầm mã phiếu cũ để tiện cho việc truy vấn 
3. Ở chi tiết phiếu: Bổ sung thêm các thông tin cần thiết
   1. Các thông tin từ "Yêu cầu mua hàng" kế thừa lại
4. Chức năng:
   1. Gửi email xin báo giá đến các nhà cung cấp. 
      1. Mô tả: Ở màn hình "Yêu cầu báo giá", thiết kế 1 button tên "Send email" . Khi click vào, popup màn hình. Các thông tin bên trong gồm gửi đến Nhà cung cấp nào. Chọn nhiều nhà cung cấp, sẽ ngăn cách nhau bằng ";". Tiêu đề, nội dung v.v... y hệt gửi 1 email bình thường. Khác biệt ở đây là gửi đến N nhà cung cấp nhưng khi gửi mail sẽ tách từng nhà cung cấp ra gửi riêng.
   2. Chức năng so sánh giá:
      1. Mô tả: Khi nhà cung cấp reply Email, Odoo sẽ tự động lưu câu trả lời của nhà cung cấp lại và tự đính kèm theo file Excel báo giá. Lúc này, hệ thống sẽ tự đọc vô file excel này lấy các thông tin như NCC - Vật tư - giá. Khi này, thiết kế 1 button cho phép User bấm vào để xem so sánh các giá với nhau. 
5. Update lại các quy trình theo sơ đồ Activity - Swimlane nha 
6. Trước mắt đến đây đã
```
