# Brainstorm — Quy trình mua hàng trên Odoo

> Nguồn đã đọc: `khao-sat-lan-1.md`, `khao-sat-lan-2-yeu-cau-mua-hang.md`, `_changes/20261020-074707.md`. Ngày tạo: 2026-10-20. Cập nhật v0.2: 2026-10-20 (khảo sát lần 2 — chi tiết phiếu Yêu cầu mua hàng; lần 2 được ưu tiên khi khác lần 1). Cập nhật v0.3: 2026-10-20 (`tra-loi-cau-hoi-mo-lan-1.md`, `khao-sat-lan-3-yeu-cau-bao-gia.md`, `_changes/20261020-084051.md`, `_changes/20261020-093008.md` — trả lời câu hỏi mở và chi tiết phiếu Yêu cầu báo giá).
> Input chỉ có một buổi khảo sát, mô tả luồng chính của Purchase. Phần lớn chi tiết vai trò, ngưỡng duyệt, kế toán, kho chưa có → ghi thành giả định (AS) kèm câu hỏi xác nhận (OQ).

## 1. Bối cảnh & vấn đề
**Đã biết**
- Khách hàng đang dùng Odoo với 4 module: Purchase, Inventory, Approvals, Accounting (nguồn: khao-sat-lan-1.md).
- Khách hàng muốn chuẩn hoá quy trình mua hàng khép kín trên Odoo: Yêu cầu mua hàng → duyệt → Yêu cầu báo giá (RFQ) → chọn giá → duyệt đơn → Đề nghị thanh toán → nhận hàng → phiếu DO (nguồn: khao-sat-lan-1.md).
- Vật tư chia 2 loại "Nhập kho" và "Dịch vụ". Dịch vụ không qua Yêu cầu mua hàng, không có hợp đồng, không tạo phiếu nhập kho; ~~MH tạo RFQ trực tiếp~~ (v0.3: tạo thẳng PO), vẫn duyệt đơn (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; _changes/20261020-074707.md).
- Yêu cầu mua hàng tạo theo 3 cách: trực tiếp tại menu, từ Hợp đồng, từ Báo giá NCC; phát sinh danh mục Hợp đồng và Báo giá NCC (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; _changes/20261020-074707.md).
- ~~Luồng có trạng thái riêng `Waiting PO`, nút chuyển `Waiting PO` → `PO` kèm tự tạo phiếu DO (khao-sat-lan-1.md)~~ — **v0.3:** bỏ Waiting PO; ĐNTT bắt buộc tạo trước khi duyệt; duyệt xong → PO + tự tạo phiếu DO (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3).
- Odoo 17 bản trả phí, chạy Odoo.sh hoặc on-premise, cài được module tuỳ biến (nguồn: tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #1).
- Quy trình hiện tại làm thủ công, cần cải thiện (nguồn: tra-loi-cau-hoi-mo-lan-1.md).
- Vật tư Dịch vụ (v0.3): không YCMH, không RFQ; tạo thẳng PO → bắt buộc ĐNTT → duyệt → PO, không DO (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md).
- RFQ (v0.3): kế thừa đầu phiếu và dòng từ YCMH; thêm NCC (xác định chính xác), Ngày dự kiến nhận hàng, Ngày nhận hàng thực tế, mã truy vết YCMH; nút "Send email" gửi riêng từng NCC; NCC reply kèm Excel, hệ thống tự đọc giá; nút so sánh giá; giữ 1 RFQ, chọn NCC cho cả phiếu (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #6, #8).

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
| Gửi email RFQ tách riêng tới N NCC, tự đọc Excel báo giá, so sánh và chọn NCC cho cả phiếu — v0.3 | Mua hàng nhập khẩu, đa tiền tệ (AS-17) | Ứng dụng mobile |
| Duyệt đơn mua hàng sau khi chọn giá | ~~Quản lý hợp đồng khung với vendor~~ (v0.2: đưa vào phạm vi) | |
| Danh mục Hợp đồng mua hàng, danh mục Báo giá NCC — v0.2 | | |
| Phân loại vật tư Nhập kho / Dịch vụ; mua dịch vụ bằng RFQ trực tiếp — v0.2 | | |
| Tự điền NCC và đơn giá theo Hợp đồng → Price List — v0.2 | | |
| Đề nghị thanh toán bắt buộc trước khi duyệt đơn — v0.3 (bỏ `Waiting PO`) | | |
| Duyệt xong → `PO` + tự tạo phiếu DO — v0.3 (bỏ nút xác nhận nhận hàng) | | |
| Mua Dịch vụ bằng PO trực tiếp — v0.3 | | |
| Nhập kho theo phiếu DO | | |

## 5. Quy trình nghiệp vụ
### 5.1 AS-IS
- Quy trình hiện tại làm thủ công, chưa có hệ thống hỗ trợ (nguồn: tra-loi-cau-hoi-mo-lan-1.md). Chưa có chi tiết từng bước → OQ-02 (đã trả lời một phần).

### 5.2 TO-BE
1. Người đề xuất tạo phiếu **Yêu cầu mua hàng** theo 1 trong 3 cách: trực tiếp tại menu, từ **Hợp đồng**, từ **Báo giá NCC**. Đầu phiếu: số phiếu `Mã BP_XXXX_DD_MM_YY`, Người tạo, Bộ phận, Ngày tạo, Ghi chú. Dòng: Vật tư (chỉ loại Nhập kho), ĐVT, Nhập kho (kho nhận), Số lượng, NCC, Ghi chú (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; AS-28, AS-29, AS-35).
   - Chọn vật tư → hệ thống tự điền NCC và đơn giá: ưu tiên hợp đồng còn hiệu lực, không có thì Price List (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; AS-30, AS-31, AS-32).
   - Vật tư Dịch vụ không qua bước 1 → 9: MH tạo thẳng PO, tạo ĐNTT, gửi duyệt; duyệt xong là PO, không có DO (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md).
2. Duyệt tuần tự **Trưởng nhóm** (theo người tạo) → **Nhân viên MH** → **BOD** (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; v0.1 là MH → Trưởng phòng).
3. Khi duyệt xong, hệ thống **tự tạo phiếu Yêu cầu báo giá (RFQ)**: N nhà cung cấp → N RFQ; chỉ 1 nhà cung cấp → đúng 1 RFQ (nguồn: khao-sat-lan-1.md; khao-sat-lan-2-yeu-cau-mua-hang.md).
4. RFQ **kế thừa** đầu phiếu và dòng từ YCMH, có NCC, Ngày dự kiến nhận hàng, mã truy vết YCMH (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; AS-42, AS-43).
5. MH bấm **Send email**, chọn nhiều NCC (ngăn cách ";"); hệ thống **gửi riêng từng NCC**; RFQ chuyển **RFQ** (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md).
6. NCC **reply email kèm file Excel**; Odoo tự lưu reply, **đọc Excel** lấy NCC – Vật tư – Giá (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; AS-44, AS-45, AS-46).
7. MH bấm **So sánh giá**, chọn 1 NCC cho cả phiếu; RFQ đổi NCC và đơn giá theo báo giá đó (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #8).
8. MH **bắt buộc tạo Đề nghị thanh toán** và gửi Kế toán (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; AS-40).
9. MH bấm **Approve** → đơn chờ duyệt; Trưởng phòng Mua hàng duyệt, **không có ngưỡng** (nguồn: tra-loi-cau-hoi-mo-lan-1.md; AS-39).
10. Duyệt xong → đơn chuyển **PO** và hệ thống **tự tạo phiếu DO** theo kho nhận (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3).
11. Thủ kho kiểm đếm và xác nhận phiếu DO; tồn kho tăng; Ngày nhận hàng thực tế cập nhật (AS-12, AS-43).
12. Kế toán xử lý Đề nghị thanh toán và ghi nhận thanh toán cho vendor (AS-10).
- *(Đã thay v0.3: các bước "duyệt xong mới tạo ĐNTT", "Waiting PO", "MH bấm Waiting PO → PO" của khảo sát lần 1.)*

### 5.3 Ngoại lệ & nhánh rẽ
- Yêu cầu mua hàng bị **từ chối** ở cấp Trưởng nhóm, MH hoặc BOD → bắt buộc lý do, phiếu **về Nháp** và gửi email cho người tạo (nguồn: tra-loi-cau-hoi-mo-lan-1.md).
- Dòng **không xác định được NCC** (không có hợp đồng, không có Price List, người tạo chưa chọn) → MH không duyệt được cấp 2 (AS-32).
- Chi tiết phiếu **trùng cả vật tư và NCC** → chặn lưu; **số lượng để trống** → chặn lưu (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md).
- Chọn vật tư loại **Dịch vụ** trên YCMH → không cho chọn (nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md).
- Hợp đồng / Báo giá NCC **hết hiệu lực** → không tạo được YCMH từ chứng từ đó; hợp đồng hết hiệu lực không dùng để tra giá (AS-30, AS-33).
- Vendor **không có email** → không gửi được RFQ (AS-13).
- NCC **không phản hồi** → MH gửi thêm NCC khác qua "Send email" (FR-06).
- File Excel báo giá **sai mẫu** hoặc email từ địa chỉ lạ → không tự đọc được, MH nhập tay (AS-45).
- **Chưa có ĐNTT** → không gửi duyệt được đơn (nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md).
- Đơn mua hàng bị **từ chối** ở bước duyệt → quay lại trạng thái RFQ để MH chọn lại giá (AS-09; dịch vụ: về Nháp).
- Đề nghị thanh toán bị **kế toán từ chối** → đơn chưa duyệt quay về RFQ, MH tạo ĐNTT mới (AS-41).
- **Nhận thiếu hàng** → phiếu DO nhập một phần, phần còn lại thành backorder (AS-12).
- **Huỷ** Yêu cầu mua hàng / RFQ / đơn mua hàng trước khi nhận hàng (AS-14).

## 6. Tích hợp & dữ liệu
| Hệ thống | Vai trò | Dữ liệu trao đổi | Chiều | Tần suất | Nguồn |
|---|---|---|---|---|---|
| Odoo Approvals | Yêu cầu mua hàng + duyệt 2 cấp | Yêu cầu, dòng sản phẩm, người duyệt | Approvals → Purchase | Realtime khi duyệt xong | khao-sat-lan-1.md; Đề xuất của BA |
| Odoo Purchase | RFQ, gửi email N NCC, đọc Excel báo giá, so sánh giá, duyệt đơn, PO (v0.3: bỏ Waiting PO) | RFQ, dòng đơn, giá chọn | Purchase → Inventory, Accounting | Realtime | khao-sat-lan-1.md |
| Odoo Accounting | Đề nghị thanh toán, thanh toán vendor | Số tiền, vendor, đơn mua hàng | Purchase → Accounting | Realtime | khao-sat-lan-1.md; AS-10 |
| Odoo Inventory | Phiếu DO (nhập kho) | Sản phẩm, số lượng | Purchase → Inventory | Realtime khi đơn được duyệt (v0.3) | khao-sat-lan-1.md; AS-12 |
| Email (SMTP + incoming mail) | Gửi RFQ riêng từng NCC, nhận reply kèm Excel, thông báo duyệt / từ chối | Email, PDF RFQ, file Excel báo giá | Odoo ↔ NCC; Odoo → người dùng | Khi thao tác; hộp thư đến theo cron (v0.3) | khao-sat-lan-1.md |

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
| AS-01 | Odoo 17 Enterprise, on-premise hoặc Odoo.sh, cho phép module tuỳ biến — **xác nhận v0.3** (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #1) | AS | Toàn hệ thống |
| AS-02 | KPI (sửa v0.2): 100% đơn mua vật tư Nhập kho có Yêu cầu mua hàng đã duyệt làm gốc và lịch sử duyệt trên chatter | AS | Mục tiêu |
| AS-03 | **[Đã thay — v0.2]** ~~Duyệt tuần tự MH → Trưởng phòng~~. Khảo sát lần 2 xác nhận: Trưởng nhóm → MH → BOD (khao-sat-lan-2-yeu-cau-mua-hang.md) | AS | Duyệt yêu cầu |
| AS-04 | **[Đã thay — v0.2]** ~~Vendor trên dòng → bảng giá NCC~~. Khảo sát lần 2: Hợp đồng còn hiệu lực → Price List (khao-sat-lan-2-yeu-cau-mua-hang.md); chi tiết ở AS-30, AS-31, AS-32 | AS | Tạo RFQ |
| AS-05 | Mỗi YCMH sinh RFQ riêng theo vendor, không gộp với YCMH khác — **xác nhận v0.3** (tra-loi-cau-hoi-mo-lan-1.md) | AS | Tạo RFQ |
| AS-06 | **[Đã thay — v0.3]** ~~Hỏi giá nhiều vendor bằng RFQ thay thế (Alternatives)~~. Giữ 1 RFQ, gửi email riêng tới N NCC (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #8) | AS | So sánh giá |
| AS-07 | **[Đã thay — v0.3]** ~~Chọn giá theo dòng; RFQ không được chọn tự huỷ~~. Chọn 1 NCC cho cả phiếu, RFQ đổi NCC và giá (_changes/20261020-093008.md #8) | AS | So sánh giá |
| AS-08 | **[Đã thay — v0.3]** ~~Trưởng phòng Mua hàng duyệt mọi đơn; tổng ≥ 50.000.000₫ thêm Giám đốc~~. Không có ngưỡng (tra-loi-cau-hoi-mo-lan-1.md); người duyệt: AS-39 | AS | Duyệt đơn |
| AS-09 | *(Sửa v0.3)* Từ chối bắt buộc lý do. YCMH bị từ chối về Nháp và gửi email cho người tạo (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #6); đơn mua hàng về RFQ (dịch vụ: Nháp); ĐNTT: AS-41 | AS | Ngoại lệ |
| AS-10 | Đề nghị thanh toán là chứng từ mới gắn với một đơn mua hàng; Kế toán duyệt/từ chối và ghi nhận thanh toán | AS | Kế toán |
| AS-11 | **[Đã thay — v0.3]** ~~Đơn chuyển Waiting PO khi ĐNTT được gửi kế toán~~. Bỏ Waiting PO; ĐNTT tạo trước khi gửi duyệt (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3) | AS | Trạng thái |
| AS-12 | "Phiếu DO" = phiếu nhập kho (Receipt) của Inventory, tạo ở trạng thái Sẵn sàng khi bấm nhận hàng; Thủ kho kiểm đếm và xác nhận; nhận thiếu tạo backorder | AS | Kho |
| AS-13 | Vendor phải có email mới gửi được RFQ | AS | Gửi RFQ |
| AS-14 | Huỷ được Yêu cầu mua hàng trước khi duyệt xong; huỷ được đơn mua hàng trước trạng thái `PO` | AS | Ngoại lệ |
| AS-15 | Hoá đơn nhà cung cấp dùng chuẩn Odoo, ngoài phạm vi đợt này | AS | Phạm vi |
| AS-16 | **[Đã thay — v0.3]** ~~MH nhập giá vendor thủ công vào RFQ~~. Hệ thống đọc Excel từ email NCC reply; nhập tay khi file lỗi (khao-sat-lan-3-yeu-cau-bao-gia.md; AS-45) | AS | So sánh giá |
| AS-17 | Chỉ dùng tiền tệ VND | AS | Phạm vi |
| OQ-01 | **Đã trả lời (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #1):** Odoo 17 bản trả phí, Odoo.sh hoặc on-premise, cài được module tuỳ biến | OQ | AS-01 |
| OQ-02 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md):** quy trình hiện tại làm thủ công, cần cải thiện. Còn mở: các bước hiện tại và chỉ số đo được | OQ | Bối cảnh |
| OQ-03 | KPI, giá trị mục tiêu và mốc go-live? | OQ | AS-02 |
| OQ-04 | **Đã trả lời (khao-sat-lan-2-yeu-cau-mua-hang.md):** duyệt tuần tự Trưởng nhóm (theo người tạo) → User MH → BOD | OQ | AS-03 |
| OQ-05 | **Đã trả lời một phần (khao-sat-lan-2-yeu-cau-mua-hang.md):** ưu tiên hợp đồng còn hiệu lực → Price List. Còn mở: không có cả hai thì xử lý thế nào → OQ-28 | OQ | AS-04 |
| OQ-06 | **Đã trả lời (tra-loi-cau-hoi-mo-lan-1.md):** không cho phép gộp nhiều YCMH cùng vendor vào một RFQ | OQ | AS-05 |
| OQ-07 | **Đã trả lời một phần (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #8):** 1 RFQ gửi email riêng tới N NCC; chọn 1 NCC cho cả phiếu. Còn mở: số NCC tối thiểu / tối đa (OQ-39) | OQ | AS-06, AS-07 |
| OQ-08 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md):** đơn mua hàng không có ngưỡng giá trị. Còn mở: ai duyệt đơn (AS-39) | OQ | AS-08 |
| OQ-09 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #6):** YCMH bị từ chối về Nháp và gửi email cho người tạo. Còn mở: đơn mua hàng và ĐNTT bị từ chối | OQ | AS-09 |
| OQ-10 | Đề nghị thanh toán là tạm ứng trước khi nhận hàng hay thanh toán theo hoá đơn? Ai duyệt, có thanh toán một phần không? | OQ | AS-10 |
| OQ-11 | **Đã trả lời (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3):** bỏ Waiting PO; ĐNTT tạo trước khi duyệt, duyệt xong là PO + DO, không chờ thanh toán | OQ | AS-11 |
| OQ-12 | "Phiếu DO" là phiếu gì? Có tự động hoàn tất nhập kho hay để Thủ kho xác nhận? (v0.2: khảo sát lần 2 nhắc "phiếu Nhập kho" cho vật tư Nhập kho — củng cố AS-12, chưa xác nhận DO = phiếu Nhập kho) | OQ | AS-12 |
| OQ-13 | Quy trình hoá đơn nhà cung cấp và đối chiếu có nằm trong dự án không? | OQ | AS-15 |
| OQ-14 | Số người dùng và số Yêu cầu mua hàng mỗi tháng? | OQ | Phi chức năng |
| OQ-15 | Có mẫu email / mẫu in RFQ, Đề nghị thanh toán theo mẫu công ty không? | OQ | Gửi RFQ |
| OQ-16 | **Đã trả lời (khao-sat-lan-3-yeu-cau-bao-gia.md):** NCC reply email kèm file Excel báo giá; không cần cổng vendor | OQ | AS-16 |
| OQ-17 | Có mua hàng bằng ngoại tệ không? | OQ | AS-17 |
| AS-26 | Vật tư "Nhập kho" = sản phẩm loại Lưu kho (storable) của Odoo; vật tư "Dịch vụ" = sản phẩm loại Dịch vụ; không dùng loại Tiêu dùng | AS | US-01, US-25 |
| AS-27 | **[Đã thay — v0.3]** ~~Đơn dịch vụ dùng chung nút "Xác nhận đã nhận hàng"~~. Đơn dịch vụ duyệt xong là PO, không có bước nhận hàng (khao-sat-lan-3-yeu-cau-bao-gia.md) | AS | US-25 |
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
| OQ-23 | **Đã trả lời một phần (khao-sat-lan-3-yeu-cau-bao-gia.md):** đơn dịch vụ duyệt xong là PO, không tạo DO, không có bước nhận hàng. Còn mở: có cần nghiệm thu dịch vụ không | OQ | AS-27, US-25 |
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
| AS-39 | Đơn mua hàng duyệt 1 cấp bởi Trưởng phòng Mua hàng, không phân ngưỡng giá trị | AS | US-15, US-18 |
| AS-40 | Gửi duyệt đơn yêu cầu ĐNTT đã gửi Kế toán (trạng thái "Chờ kế toán duyệt" trở lên); không cần Kế toán duyệt xong | AS | US-10, US-11 |
| AS-41 | ĐNTT bị Kế toán từ chối: đơn đang Chờ duyệt về RFQ (dịch vụ: Nháp); đơn đã PO giữ PO; MH tạo ĐNTT mới | AS | US-16 |
| AS-42 | Số RFQ/PO = `<Mã BP>-PO-<XXXX>-<DD>-<MM>-<YYYY>-<NN>`: Mã BP, XXXX, ngày lấy từ YCMH gốc, NN là thứ tự RFQ trong YCMH (vd. `HC-PO-0012-20-10-2026-02`). PO dịch vụ: `<Mã BP người tạo>-PO-<XXXX>-<DD>-<MM>-<YYYY>`, XXXX đếm riêng (vd. `MH-PO-0003-21-10-2026`). Mã YCMH gốc lưu ngầm ở trường ẩn | AS | US-27 |
| AS-43 | Ngày dự kiến nhận hàng mặc định = Ngày cần hàng của YCMH (trống thì ngày tạo RFQ + 7 ngày), MH sửa được; Ngày nhận hàng thực tế = ngày hoàn tất phiếu DO cuối cùng của đơn, chỉ đọc | AS | US-12 |
| AS-44 | Email xin báo giá có bảng sản phẩm của phiếu trong nội dung, đính kèm PDF RFQ và file Excel mẫu báo giá (Mã vật tư, Tên vật tư, ĐVT, Số lượng, Đơn giá, Ngày giao, Ghi chú) | AS | US-07, US-26 |
| AS-45 | Odoo nhận reply qua incoming mail server và alias của RFQ; NCC xác định theo email người gửi; file sai mẫu thì MH nhập tay báo giá | AS | US-26 |
| AS-46 | Kết quả đọc Excel lưu thành Báo giá NCC (FR-21) gắn với RFQ; báo giá mới của cùng NCC thay báo giá cũ ("Đã thay thế") | AS | US-09, US-26 |
| AS-47 | File báo giá chỉ nhận .xlsx, ≤ 5 MB, ≤ 500 dòng; đọc xong ≤ 60 giây sau khi email tới | AS | US-26 |
| OQ-34 | Gửi duyệt đơn chỉ cần tạo / gửi ĐNTT, hay phải chờ Kế toán duyệt ĐNTT? | OQ | AS-40 |
| OQ-35 | ĐNTT bị Kế toán từ chối thì đơn mua hàng xử lý thế nào? | OQ | AS-41 |
| OQ-36 | Mẫu "Mã phòng ban-PO-XXXX-DD-MM-YYYY": XXXX và ngày lấy từ YCMH hay đếm riêng? 1 YCMH sinh nhiều RFQ thì phân biệt thế nào? PO dịch vụ đánh số ra sao? Mẫu này khác mẫu số YCMH "Mã BP_XXXX_DD_MM_YY" — có thống nhất không? | OQ | AS-42, AS-28 |
| OQ-37 | Nhận nhiều đợt (backorder) thì "Ngày nhận hàng thực tế" lấy ngày nào? | OQ | AS-43 |
| OQ-38 | Mẫu file Excel báo giá do ai cung cấp, gồm cột nào? NCC không dùng mẫu thì xử lý ra sao? Hộp thư nhận báo giá là địa chỉ nào? | OQ | AS-44, AS-45 |
| OQ-39 | Một RFQ được hỏi giá tối đa bao nhiêu NCC? Có bắt buộc đủ số báo giá tối thiểu trước khi chọn NCC không? | OQ | US-07, US-09 |
