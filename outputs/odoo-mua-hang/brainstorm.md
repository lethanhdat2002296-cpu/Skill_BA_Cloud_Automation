# Brainstorm — Quy trình mua hàng trên Odoo

> Nguồn đã đọc: `khao-sat-lan-1.md`, `khao-sat-lan-2-yeu-cau-mua-hang.md`, `_changes/20261020-074707.md`. Ngày tạo: 2026-10-20. Cập nhật v0.2: 2026-10-20 (khảo sát lần 2 — chi tiết phiếu Yêu cầu mua hàng; lần 2 được ưu tiên khi khác lần 1).
> Input chỉ có một buổi khảo sát, mô tả luồng chính của Purchase. Phần lớn chi tiết vai trò, ngưỡng duyệt, kế toán, kho chưa có → ghi thành giả định (AS) kèm câu hỏi xác nhận (OQ).

## 1. Bối cảnh & vấn đề
**Đã biết**
- Khách hàng đang dùng Odoo với 4 module: Purchase, Inventory, Approvals, Accounting (nguồn: khao-sat-lan-1.md).
- Khách hàng muốn chuẩn hoá quy trình mua hàng khép kín trên Odoo: Yêu cầu mua hàng → duyệt → Yêu cầu báo giá (RFQ) → chọn giá → duyệt đơn → Đề nghị thanh toán → nhận hàng → phiếu DO (nguồn: khao-sat-lan-1.md).
- Vật tư chia 2 loại "Nhập kho" và "Dịch vụ". Dịch vụ không qua Yêu cầu mua hàng, không có hợp đồng, không tạo phiếu nhập kho; MH tạo RFQ trực tiếp, vẫn duyệt đơn (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; _changes/20261020-074707.md).
- Yêu cầu mua hàng tạo theo 3 cách: trực tiếp tại menu, từ Hợp đồng, từ Báo giá NCC; phát sinh danh mục Hợp đồng và Báo giá NCC (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; _changes/20261020-074707.md).
- Luồng có các bước tự động hoá ngoài chuẩn Odoo: tự tạo RFQ gộp theo vendor sau khi duyệt, trạng thái riêng `Waiting PO`, nút chuyển `Waiting PO` → `PO` kèm tự tạo phiếu DO (nguồn: khao-sat-lan-1.md).

**Giả định**
- AS-01: Hệ thống chạy Odoo 17 Enterprise, triển khai on-premise hoặc Odoo.sh (cho phép module tuỳ biến). Lý do: module Approvals chỉ có ở bản Enterprise; các bước tự động hoá cần code tuỳ biến → xác nhận ở OQ-01.

**Chưa biết**
- OQ-01: Phiên bản Odoo, edition (Enterprise/Community) và hình thức hosting (Odoo Online không cho cài module tuỳ biến)?
- OQ-02: Vấn đề hiện tại khách gặp phải là gì (mua hàng ngoài hệ thống, duyệt qua email/giấy, khó truy vết)? Đo được bằng chỉ số nào?

## 2. Mục tiêu kinh doanh
**Đã biết**
- Toàn bộ vòng đời mua hàng được thực hiện và truy vết trên Odoo, từ yêu cầu tới nhận hàng (nguồn: khao-sat-lan-1.md).

**Giả định**
- AS-02: Mục tiêu đo bằng: 100% đơn mua hàng có Yêu cầu mua hàng đã duyệt làm gốc; 100% đơn mua hàng có lịch sử duyệt lưu trên chatter. Giá trị KPI cụ thể chưa có → xác nhận ở OQ-03.

**Chưa biết**
- OQ-03: KPI và giá trị mục tiêu (thời gian xử lý một yêu cầu, tỉ lệ mua đúng quy trình…)? Mốc go-live?

## 3. Người dùng & vai trò
| Vai trò | Mô tả | Hệ thống | Việc chính | Nguồn |
|---|---|---|---|---|
| Người đề xuất | Nhân viên các phòng ban có nhu cầu mua ("Người tạo") | Odoo backend (Approvals) | Tạo YCMH trực tiếp / từ Hợp đồng / từ Báo giá NCC, gửi, theo dõi | khao-sat-lan-1.md; khao-sat-lan-2-yeu-cau-mua-hang.md |
| Nhân viên Mua hàng (MH) | Nhân viên phòng Mua hàng | Odoo backend (Approvals, Purchase, Accounting) | Duyệt cấp 2 Yêu cầu mua hàng, quản lý danh mục Hợp đồng và Báo giá NCC, tạo RFQ dịch vụ, gửi RFQ, chọn giá, gửi duyệt đơn, tạo Đề nghị thanh toán, xác nhận nhận hàng | khao-sat-lan-1.md |
| Trưởng nhóm | Người duyệt cấp 1 của Yêu cầu mua hàng, theo người tạo (v0.2: thay vai trò "Trưởng phòng") | Odoo backend (Approvals) | Duyệt / từ chối Yêu cầu mua hàng | khao-sat-lan-2-yeu-cau-mua-hang.md; AS-34 |
| BOD | Ban giám đốc, người duyệt cấp 3 của Yêu cầu mua hàng | Odoo backend (Approvals) | Duyệt / từ chối Yêu cầu mua hàng | khao-sat-lan-2-yeu-cau-mua-hang.md; AS-34 |
| Người duyệt đơn mua hàng | Người duyệt sau khi MH chọn giá | Odoo backend (Purchase) | Duyệt / từ chối đơn mua hàng | khao-sat-lan-1.md ("vô quy trình duyệt"); danh tính: AS-08 |
| Kế toán | Kế toán công nợ phải trả | Odoo backend (Accounting) | Tiếp nhận, xử lý Đề nghị thanh toán | AS-10 |
| Thủ kho | Nhân viên kho nhận hàng | Odoo backend (Inventory) | Kiểm đếm, xác nhận phiếu nhập kho (DO) | AS-12 |
| Quản trị hệ thống | IT / key user | Odoo backend (Settings) | Cấu hình người duyệt, ngưỡng, mẫu email | Đề xuất của BA |

## 4. Phạm vi
| In scope | Out of scope | Giai đoạn sau |
|---|---|---|
| Yêu cầu mua hàng (3 cách tạo) + duyệt 3 cấp (Trưởng nhóm, MH, BOD) — v0.2 | Hoá đơn nhà cung cấp (vendor bill) và đối chiếu 3 bên — dùng chuẩn Odoo (AS-15) | Cổng vendor tự nhập báo giá (portal) |
| Tự tạo RFQ gộp theo vendor | Kiểm soát ngân sách theo phòng ban | Báo cáo phân tích mua hàng |
| Gửi email RFQ tới nhiều vendor, so sánh và chọn giá | Mua hàng nhập khẩu, đa tiền tệ (AS-17) | Ứng dụng mobile |
| Duyệt đơn mua hàng sau khi chọn giá | ~~Quản lý hợp đồng khung với vendor~~ (v0.2: đưa vào phạm vi) | |
| Danh mục Hợp đồng mua hàng, danh mục Báo giá NCC — v0.2 | | |
| Phân loại vật tư Nhập kho / Dịch vụ; mua dịch vụ bằng RFQ trực tiếp — v0.2 | | |
| Tự điền NCC và đơn giá theo Hợp đồng → Price List — v0.2 | | |
| Đề nghị thanh toán + trạng thái `Waiting PO` | | |
| Xác nhận nhận hàng (`Waiting PO` → `PO`) + tự tạo phiếu DO | | |
| Nhập kho theo phiếu DO | | |

## 5. Quy trình nghiệp vụ
### 5.1 AS-IS
- Input không mô tả quy trình hiện tại → OQ-02.

### 5.2 TO-BE
1. Người đề xuất tạo phiếu **Yêu cầu mua hàng** theo 1 trong 3 cách: trực tiếp tại menu, từ **Hợp đồng**, từ **Báo giá NCC**. Đầu phiếu: số phiếu `Mã BP_XXXX_DD_MM_YY`, Người tạo, Bộ phận, Ngày tạo, Ghi chú. Dòng: Vật tư (chỉ loại Nhập kho), ĐVT, Nhập kho (kho nhận), Số lượng, NCC, Ghi chú (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; AS-28, AS-29, AS-35).
   - Chọn vật tư → hệ thống tự điền NCC và đơn giá: ưu tiên hợp đồng còn hiệu lực, không có thì Price List (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; AS-30, AS-31, AS-32).
   - Vật tư Dịch vụ không qua bước này: MH tạo RFQ trực tiếp ở bước 4 (nguồn: _changes/20261020-074707.md).
2. Duyệt tuần tự **Trưởng nhóm** (theo người tạo) → **Nhân viên MH** → **BOD** (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; v0.1 là MH → Trưởng phòng).
3. Khi duyệt xong, hệ thống **tự tạo phiếu Yêu cầu báo giá (RFQ)**: N nhà cung cấp → N RFQ; chỉ 1 nhà cung cấp → đúng 1 RFQ (nguồn: khao-sat-lan-1.md; khao-sat-lan-2-yeu-cau-mua-hang.md).
4. MH **gửi email** tới các vendor xin báo giá; phiếu chuyển trạng thái **RFQ** (nguồn: khao-sat-lan-1.md).
5. Báo giá về, MH **nhập giá, so sánh và chọn giá** (nguồn: khao-sat-lan-1.md; cách so sánh nhiều vendor: AS-06, AS-07).
6. MH bấm **Approve** → phiếu chuyển trạng thái chờ duyệt và đi vào **quy trình duyệt** (nguồn: khao-sat-lan-1.md; người duyệt: AS-08).
7. Duyệt xong, MH tạo phiếu **Đề nghị thanh toán** (nguồn: khao-sat-lan-1.md).
8. Tạo xong Đề nghị thanh toán, phiếu mua hàng chuyển trạng thái **Waiting PO** (nguồn: khao-sat-lan-1.md; thời điểm chuyển: AS-11).
9. Khi nhận được hàng, MH bấm nút chuyển **Waiting PO → PO** để hoàn tất nhận hàng; hệ thống **tự tạo phiếu DO** (nguồn: khao-sat-lan-1.md; định nghĩa DO: AS-12).
10. Thủ kho kiểm đếm và xác nhận phiếu DO; tồn kho tăng (AS-12).
11. Kế toán xử lý Đề nghị thanh toán và ghi nhận thanh toán cho vendor (AS-10).

### 5.3 Ngoại lệ & nhánh rẽ
- Yêu cầu mua hàng bị **từ chối** ở cấp Trưởng nhóm, MH hoặc BOD → bắt buộc lý do, phiếu trả về người đề xuất (AS-09).
- Dòng **không xác định được NCC** (không có hợp đồng, không có Price List, người tạo chưa chọn) → MH không duyệt được cấp 2 (AS-32).
- Chi tiết phiếu **trùng cả vật tư và NCC** → chặn lưu; **số lượng để trống** → chặn lưu (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md).
- Chọn vật tư loại **Dịch vụ** trên YCMH → không cho chọn (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md).
- Hợp đồng / Báo giá NCC **hết hiệu lực** → không tạo được YCMH từ chứng từ đó; hợp đồng hết hiệu lực không dùng để tra giá (AS-30, AS-33).
- Vendor **không có email** → không gửi được RFQ (AS-13).
- Vendor **không phản hồi** báo giá → MH huỷ RFQ hoặc gửi vendor khác (AS-06).
- Đơn mua hàng bị **từ chối** ở bước duyệt → quay lại trạng thái RFQ để MH chọn lại giá (AS-09).
- Đề nghị thanh toán bị **kế toán từ chối** (AS-10).
- **Nhận thiếu hàng** → phiếu DO nhập một phần, phần còn lại thành backorder (AS-12).
- **Huỷ** Yêu cầu mua hàng / RFQ / đơn mua hàng trước khi nhận hàng (AS-14).

## 6. Tích hợp & dữ liệu
| Hệ thống | Vai trò | Dữ liệu trao đổi | Chiều | Tần suất | Nguồn |
|---|---|---|---|---|---|
| Odoo Approvals | Yêu cầu mua hàng + duyệt 2 cấp | Yêu cầu, dòng sản phẩm, người duyệt | Approvals → Purchase | Realtime khi duyệt xong | khao-sat-lan-1.md; Đề xuất của BA |
| Odoo Purchase | RFQ, so sánh giá, duyệt đơn, trạng thái Waiting PO / PO | RFQ, dòng đơn, giá chọn | Purchase → Inventory, Accounting | Realtime | khao-sat-lan-1.md |
| Odoo Accounting | Đề nghị thanh toán, thanh toán vendor | Số tiền, vendor, đơn mua hàng | Purchase → Accounting | Realtime | khao-sat-lan-1.md; AS-10 |
| Odoo Inventory | Phiếu DO (nhập kho) | Sản phẩm, số lượng | Purchase → Inventory | Realtime khi bấm nhận hàng | khao-sat-lan-1.md; AS-12 |
| Email (SMTP) | Gửi RFQ cho vendor, thông báo duyệt | Email + PDF RFQ | Odoo → vendor / người dùng | Khi thao tác | khao-sat-lan-1.md |

- Source of truth: tất cả dữ liệu nằm trong một CSDL Odoo; không có hệ thống ngoài ngoài máy chủ email.

## 7. Ràng buộc & rủi ro
| Loại | Nội dung | Mức độ | Giảm thiểu |
|---|---|---|---|
| Kỹ thuật | Tự tạo RFQ, trạng thái `Waiting PO`, nút chuyển PO, Đề nghị thanh toán đều cần module tuỳ biến | Cao | Xác nhận hosting cho phép custom module (OQ-01) |
| Kỹ thuật | Odoo chuẩn tạo phiếu nhập kho ngay khi xác nhận đơn; quy trình mới dời thời điểm xác nhận đơn sang lúc nhận hàng | Trung bình | Xác nhận đơn (`button_confirm`) đúng lúc bấm "Xác nhận đã nhận hàng" (AS-12) |
| Nghiệp vụ | Thanh toán trước khi nhận hàng có rủi ro vendor không giao | Trung bình | Làm rõ bản chất Đề nghị thanh toán (OQ-10, OQ-11) |
| Nghiệp vụ | Chưa rõ người duyệt và ngưỡng duyệt đơn mua hàng | Cao | AS-08 + OQ-08 trước khi phát triển |
| Dữ liệu | Sản phẩm thiếu bảng giá nhà cung cấp → không xác định được vendor | Trung bình | Chặn duyệt khi dòng thiếu vendor (AS-04); làm sạch dữ liệu trước go-live |

## Đề xuất của BA (chưa phải yêu cầu)
- Dùng loại duyệt **Purchases** có sẵn của Approvals (module `approval_purchase`) cho Yêu cầu mua hàng: chuẩn Odoo đã có chức năng tạo RFQ gộp theo vendor, chỉ cần tuỳ biến để chạy tự động khi duyệt xong.
- Dùng tính năng **Alternatives** (so sánh RFQ thay thế, cần bật Purchase Agreements) để gửi một nhu cầu cho nhiều vendor và chọn giá theo dòng.
- Smart button truy vết hai chiều: Yêu cầu mua hàng ↔ RFQ ↔ Đề nghị thanh toán ↔ phiếu DO.

## Assumptions & Open Questions
| Mã | Nội dung | Loại (AS/OQ) | Liên quan |
|---|---|---|---|
| AS-01 | Odoo 17 Enterprise, on-premise hoặc Odoo.sh, cho phép module tuỳ biến | AS | Toàn hệ thống |
| AS-02 | KPI (sửa v0.2): 100% đơn mua vật tư Nhập kho có Yêu cầu mua hàng đã duyệt làm gốc và lịch sử duyệt trên chatter | AS | Mục tiêu |
| AS-03 | **[Đã thay — v0.2]** ~~Duyệt tuần tự MH → Trưởng phòng~~. Khảo sát lần 2 xác nhận: Trưởng nhóm → MH → BOD (khao-sat-lan-2-yeu-cau-mua-hang.md) | AS | Duyệt yêu cầu |
| AS-04 | **[Đã thay — v0.2]** ~~Vendor trên dòng → bảng giá NCC~~. Khảo sát lần 2: Hợp đồng còn hiệu lực → Price List (khao-sat-lan-2-yeu-cau-mua-hang.md); chi tiết ở AS-30, AS-31, AS-32 | AS | Tạo RFQ |
| AS-05 | Mỗi Yêu cầu mua hàng sinh RFQ riêng theo vendor; không gộp dòng vào RFQ của yêu cầu khác | AS | Tạo RFQ |
| AS-06 | "Gửi email đến nhiều vendor" = gửi RFQ cho vendor của phiếu và tạo RFQ thay thế (Alternatives) cho vendor khác cùng sản phẩm | AS | So sánh giá |
| AS-07 | Chọn giá theo từng dòng sản phẩm; RFQ không còn dòng nào được chọn tự huỷ | AS | So sánh giá |
| AS-08 | Duyệt đơn mua hàng: Trưởng phòng Mua hàng duyệt mọi đơn; tổng đơn ≥ 50.000.000₫ cần thêm Giám đốc duyệt | AS | Duyệt đơn |
| AS-09 | Từ chối ở mọi cấp bắt buộc nhập lý do; Yêu cầu mua hàng trả về Nháp, đơn mua hàng trả về RFQ | AS | Ngoại lệ |
| AS-10 | Đề nghị thanh toán là chứng từ mới gắn với một đơn mua hàng; Kế toán duyệt/từ chối và ghi nhận thanh toán | AS | Kế toán |
| AS-11 | Đơn chuyển `Waiting PO` ngay khi Đề nghị thanh toán được gửi, không chờ thanh toán xong | AS | Trạng thái |
| AS-12 | "Phiếu DO" = phiếu nhập kho (Receipt) của Inventory, tạo ở trạng thái Sẵn sàng khi bấm nhận hàng; Thủ kho kiểm đếm và xác nhận; nhận thiếu tạo backorder | AS | Kho |
| AS-13 | Vendor phải có email mới gửi được RFQ | AS | Gửi RFQ |
| AS-14 | Huỷ được Yêu cầu mua hàng trước khi duyệt xong; huỷ được đơn mua hàng trước trạng thái `PO` | AS | Ngoại lệ |
| AS-15 | Hoá đơn nhà cung cấp dùng chuẩn Odoo, ngoài phạm vi đợt này | AS | Phạm vi |
| AS-16 | MH nhập giá vendor gửi về (qua email) thủ công vào RFQ; không dùng cổng vendor | AS | So sánh giá |
| AS-17 | Chỉ dùng tiền tệ VND | AS | Phạm vi |
| OQ-01 | Phiên bản Odoo, edition và hosting? | OQ | AS-01 |
| OQ-02 | Quy trình hiện tại (AS-IS) và vấn đề đang gặp? | OQ | Bối cảnh |
| OQ-03 | KPI, giá trị mục tiêu và mốc go-live? | OQ | AS-02 |
| OQ-04 | **Đã trả lời (khao-sat-lan-2-yeu-cau-mua-hang.md):** duyệt tuần tự Trưởng nhóm (theo người tạo) → User MH → BOD | OQ | AS-03 |
| OQ-05 | **Đã trả lời một phần (khao-sat-lan-2-yeu-cau-mua-hang.md):** ưu tiên hợp đồng còn hiệu lực → Price List. Còn mở: không có cả hai thì xử lý thế nào → OQ-28 | OQ | AS-04 |
| OQ-06 | Có gộp dòng của nhiều Yêu cầu mua hàng cùng vendor vào một RFQ không? | OQ | AS-05 |
| OQ-07 | Một nhu cầu được hỏi giá bao nhiêu vendor? Chọn giá theo dòng hay cả phiếu? Tiêu chí chọn? | OQ | AS-06, AS-07 |
| OQ-08 | Ai duyệt đơn mua hàng sau khi chọn giá? Có phân cấp theo giá trị không, ngưỡng bao nhiêu? | OQ | AS-08 |
| OQ-09 | Khi bị từ chối, phiếu quay về đâu? Có cho gửi lại không? | OQ | AS-09 |
| OQ-10 | Đề nghị thanh toán là tạm ứng trước khi nhận hàng hay thanh toán theo hoá đơn? Ai duyệt, có thanh toán một phần không? | OQ | AS-10 |
| OQ-11 | Có phải chờ thanh toán xong mới nhận hàng không? | OQ | AS-11 |
| OQ-12 | "Phiếu DO" là phiếu gì? Có tự động hoàn tất nhập kho hay để Thủ kho xác nhận? (v0.2: khảo sát lần 2 nhắc "phiếu Nhập kho" cho vật tư Nhập kho — củng cố AS-12, chưa xác nhận DO = phiếu Nhập kho) | OQ | AS-12 |
| OQ-13 | Quy trình hoá đơn nhà cung cấp và đối chiếu có nằm trong dự án không? | OQ | AS-15 |
| OQ-14 | Số người dùng và số Yêu cầu mua hàng mỗi tháng? | OQ | Phi chức năng |
| OQ-15 | Có mẫu email / mẫu in RFQ, Đề nghị thanh toán theo mẫu công ty không? | OQ | Gửi RFQ |
| OQ-16 | Vendor gửi báo giá qua kênh nào? Có cần cổng để vendor tự nhập giá không? | OQ | AS-16 |
| OQ-17 | Có mua hàng bằng ngoại tệ không? | OQ | AS-17 |
| AS-26 | Vật tư "Nhập kho" = sản phẩm loại Lưu kho (storable) của Odoo; vật tư "Dịch vụ" = sản phẩm loại Dịch vụ; không dùng loại Tiêu dùng | AS | US-01, US-25 |
| AS-27 | Đơn dịch vụ dùng chung nút "Xác nhận đã nhận hàng" để chuyển Waiting PO → PO, không sinh phiếu DO | AS | US-25 |
| AS-28 | Số phiếu YCMH = `<Mã BP>_<XXXX>_<DD>_<MM>_<YY>`: Mã BP là mã bộ phận của người tạo; XXXX đếm riêng theo bộ phận, về 0001 đầu mỗi năm; DD_MM_YY là ngày tạo (vd. `HC_0012_20_10_26`) | AS | US-01 |
| AS-29 | Kho nhận (cột "Nhập kho") mặc định là kho chính của công ty, người tạo sửa được theo từng dòng; một đơn mua sinh một phiếu DO cho mỗi kho nhận | AS | US-01, US-12 |
| AS-30 | Hợp đồng = Purchase Agreement loại Hợp đồng khung (Blanket Order); còn hiệu lực khi trạng thái "Đang hiệu lực" và ngày hiện tại nằm trong khoảng hiệu lực; không kiểm tra số lượng còn lại | AS | US-19, US-21, US-22 |
| AS-31 | Nhiều hợp đồng còn hiệu lực cùng vật tư → chọn đơn giá thấp nhất, bằng nhau thì hợp đồng hết hạn sớm nhất. Price List chọn theo quy tắc chuẩn Odoo (thứ tự, số lượng tối thiểu, hiệu lực) | AS | US-21 |
| AS-32 | Giá lấy từ hợp đồng bị khoá; giá từ Price List sửa được; không có nguồn giá thì người tạo nhập tay NCC (đơn giá tuỳ chọn). Mọi dòng phải có NCC trước khi Nhân viên MH duyệt cấp 2 | AS | US-05, US-21 |
| AS-33 | Báo giá NCC là danh mục mới (NCC, ngày báo giá, hiệu lực đến, dòng vật tư – đơn giá); không tham gia tự tra giá; hết hiệu lực thì không tạo được YCMH | AS | US-20, US-23 |
| AS-34 | Trưởng nhóm = quản lý trực tiếp (Manager) trên hồ sơ nhân viên của người tạo; người tạo chưa có Trưởng nhóm thì chặn gửi duyệt. BOD = nhóm quyền "BOD", một thành viên duyệt là đủ | AS | US-14, US-24 |
| AS-35 | Đầu phiếu giữ "Ngày cần hàng" (không bắt buộc, làm ngày dự kiến trên RFQ); "Lý do mua" bỏ, thay bằng "Ghi chú" (không bắt buộc) | AS | US-01 |
| AS-36 | Tạo YCMH từ Hợp đồng / Báo giá NCC: chép mọi dòng, số lượng để trống cho người tạo nhập, dòng không cần thì xoá; NCC và đơn giá khoá theo chứng từ nguồn; được thêm dòng vật tư khác (tự tra giá) | AS | US-19, US-20 |
| AS-37 | Giữ cả hai lớp duyệt: YCMH (Trưởng nhóm → MH → BOD) và đơn mua hàng sau chọn giá (AS-08) cho tới khi khảo sát phiếu tiếp theo | AS | US-10, US-15 |
| OQ-22 | Vật tư "Nhập kho" ứng với loại sản phẩm nào trong Odoo? Có dùng loại Tiêu dùng (consumable) không? | OQ | AS-26 |
| OQ-23 | Đơn dịch vụ hoàn tất bằng nút nào? Có cần nghiệm thu / biên bản trước khi chuyển PO không? | OQ | AS-27, US-25 |
| OQ-24 | XXXX trong số phiếu đếm theo bộ phận hay toàn công ty? Về 0001 theo năm, tháng hay ngày? Mã BP lấy ở đâu? | OQ | AS-28, US-01 |
| OQ-25 | Kho nhận mặc định của dòng là kho nào? Bộ phận nào được chọn kho nào? | OQ | AS-29 |
| OQ-26 | Hợp đồng có giới hạn số lượng / giá trị không? Có trừ luỹ kế và chặn khi vượt không? | OQ | AS-30, US-22 |
| OQ-27 | Nhiều hợp đồng hoặc nhiều dòng Price List cùng vật tư thì chọn theo tiêu chí nào? | OQ | AS-31, US-21 |
| OQ-28 | Người tạo được sửa NCC và đơn giá hệ thống tự điền không? Không có cả hợp đồng lẫn Price List thì xử lý thế nào? | OQ | AS-32, US-21 |
| OQ-29 | Báo giá NCC có tham gia tự tra giá không? Ai nhập báo giá, có cần duyệt không? | OQ | AS-33, US-20, US-23 |
| OQ-30 | Người tạo không có Trưởng nhóm thì xử lý thế nào? BOD cần một hay tất cả thành viên duyệt? Có phân ngưỡng giá trị không? | OQ | AS-34, US-24 |
| OQ-31 | Có cần "Ngày cần hàng" và "Lý do mua" trên đầu phiếu không? | OQ | AS-35 |
| OQ-32 | Tạo YCMH từ Hợp đồng / Báo giá: chép mọi dòng hay chọn dòng? Có được thêm vật tư ngoài chứng từ nguồn không? | OQ | AS-36, US-19, US-20 |
| OQ-33 | BOD đã duyệt YCMH thì đơn mua hàng sau khi chọn giá còn cần duyệt nữa không? | OQ | AS-37 |
