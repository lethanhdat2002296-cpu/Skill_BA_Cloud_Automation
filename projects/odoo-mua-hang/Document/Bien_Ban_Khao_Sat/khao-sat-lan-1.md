# Khảo sát lần 1 — Quy trình mua hàng trên Odoo

> Nguồn: mô tả của BA sau buổi khảo sát đầu tiên với khách hàng (nguyên văn).

Hiện tại, tao đang có 1 dự án liên quan đến quy trình mua hàng như sau:

1. Module họ dùng trên Odoo gồm có Purchase, Inventory, Approvals, Accounting
2. Ở Purchase: Quy trình mua hàng gồm như sau
   1. User tạo phiếu "Yêu cầu mua hàng" -> User (MH) và User (Trưởng phòng) duyệt -> Hệ thống tự động tạo ra phiếu "Yêu cầu báo giá" với quy tắc gộp các sản phẩm cùng 1 Vendor lại để ra phiếu, với vendor khác sẽ ra 2 phiếu -> User (MH) sẽ thực hiện gửi Email đến nhiều vendor để xin báo giá (Lúc này, phiếu chuyển sang trạng thái RFQ ) -> Khi đã có báo giá về, User sẽ thực hiện vô check giá và xác định chọn giá -> Sau khi chọn xong, và bấm  Apporove, hệ thống sẽ tự chuyển trạng thái và vô quy trình duyệt. -> Sau khi duyệt xong, User sẽ vô tạo phiếu "Đề nghị thanh toán" -> Sau khi tạo "Đề nghị thanh toán" xong, hệ thống sẽ chuyển trạng thái waiting PO . -> Lúc này, User (MH) khi nhận được hàng, sẽ bấm button để chuyển trạng thái từ Wating PO sang PO để hoàn tấn nhận hàng -> đồng thời hệ thống cũng tự động tạo ra phiếu DO 
3. Hiện tại buổi khảo sát đầu tiền của tao chỉ nhiêu đây hãy tiến hành làm nhé
