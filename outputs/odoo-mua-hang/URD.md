# URD — Quy trình mua hàng trên Odoo

| Thuộc tính | Giá trị |
|---|---|
| Mã dự án | odoo-mua-hang |
| Phiên bản | 0.3 (cập nhật theo trả lời câu hỏi mở lần 1 và khảo sát lần 3 — Yêu cầu báo giá) |
| Ngày | 2026-10-20 |
| Nguồn | inputs/odoo-mua-hang/khao-sat-lan-1.md; inputs/odoo-mua-hang/khao-sat-lan-2-yeu-cau-mua-hang.md; inputs/odoo-mua-hang/_changes/20261020-074707.md; inputs/odoo-mua-hang/tra-loi-cau-hoi-mo-lan-1.md; inputs/odoo-mua-hang/khao-sat-lan-3-yeu-cau-bao-gia.md; inputs/odoo-mua-hang/_changes/20261020-084051.md; inputs/odoo-mua-hang/_changes/20261020-093008.md; outputs/odoo-mua-hang/brainstorm.md |
| Trạng thái | Chờ khách hàng review |

## 1. Giới thiệu

### 1.1 Mục đích
Tài liệu mô tả yêu cầu của người dùng cho quy trình mua hàng trên Odoo (Purchase, Inventory, Approvals, Accounting), nhằm chuẩn hoá toàn bộ vòng đời mua hàng từ Yêu cầu mua hàng tới nhận hàng nhập kho, có duyệt và truy vết đầy đủ.

### 1.2 Phạm vi
- **Trong phạm vi:** Yêu cầu mua hàng (tạo trực tiếp, từ Hợp đồng, từ Báo giá NCC) và duyệt 3 cấp; danh mục Hợp đồng mua hàng và Báo giá NCC; tự điền NCC và đơn giá theo Hợp đồng → Price List; phân loại vật tư Nhập kho / Dịch vụ, mua dịch vụ bằng PO trực tiếp (v0.3); tự tạo Yêu cầu báo giá (RFQ) theo NCC, kế thừa YCMH và gắn mã YCMH (v0.3); gửi email riêng tới N NCC, tự đọc Excel báo giá, so sánh và chọn 1 NCC cho cả phiếu (v0.3); Đề nghị thanh toán bắt buộc trước khi duyệt đơn (v0.3); duyệt đơn mua hàng không ngưỡng; duyệt xong chuyển `PO` và tự tạo phiếu DO (v0.3, bỏ `Waiting PO`); nhập kho theo phiếu DO.
- **Ngoài phạm vi:** hoá đơn nhà cung cấp và đối chiếu 3 bên (AS-15); kiểm soát ngân sách; cổng vendor tự nhập báo giá (AS-16); đa tiền tệ (AS-17).

### 1.3 Mục tiêu kinh doanh
| # | Mục tiêu | Chỉ số đo | Giá trị mục tiêu |
|---|---|---|---|
| 1 | Mọi giao dịch mua vật tư Nhập kho đi qua quy trình | Tỉ lệ đơn mua vật tư Nhập kho có Yêu cầu mua hàng đã duyệt làm gốc | 100% (AS-02) |
| 2 | Truy vết được người duyệt và thời điểm duyệt | Tỉ lệ đơn mua hàng có lịch sử duyệt trên chatter | 100% (AS-02) |
| 3 | Giảm thao tác thủ công khi lập RFQ | Số RFQ phải tạo tay từ yêu cầu đã duyệt | 0 (RFQ tạo tự động) |

## 2. Vai trò người dùng

| Vai trò | Mô tả | Hệ thống sử dụng | Tần suất |
|---|---|---|---|
| Người đề xuất | Nhân viên các phòng ban có nhu cầu mua ("Người tạo" phiếu) | Odoo backend — Approvals, Purchase (xem Hợp đồng, Báo giá NCC) | Theo nhu cầu, vài lần/tháng |
| Nhân viên Mua hàng (MH) | Duyệt cấp 2 YCMH; quản lý Hợp đồng, Báo giá NCC; xử lý RFQ, đơn mua hàng | Odoo backend — Approvals, Purchase, Accounting | Hằng ngày |
| Trưởng nhóm | Duyệt cấp 1 Yêu cầu mua hàng, theo người tạo (AS-34; v0.2 thay "Trưởng phòng") | Odoo backend — Approvals | Hằng ngày |
| BOD | Ban giám đốc, duyệt cấp 3 Yêu cầu mua hàng (AS-34) | Odoo backend — Approvals | Hằng ngày |
| Người duyệt đơn mua hàng | Trưởng phòng Mua hàng; Giám đốc với đơn từ ngưỡng (AS-08) | Odoo backend — Purchase | Hằng ngày |
| Kế toán | Xử lý Đề nghị thanh toán (AS-10) | Odoo backend — Accounting | Hằng ngày |
| Thủ kho | Nhập kho theo phiếu DO (AS-12) | Odoo backend — Inventory | Hằng ngày |
| Quản trị hệ thống | Cấu hình người duyệt, ngưỡng, mẫu email | Odoo backend — Settings | Khi thay đổi chính sách |

## 3. User stories theo vai trò

### 3.1 Người đề xuất

#### US-01 — Tạo và gửi Yêu cầu mua hàng
- **Story:** Là Người đề xuất, tôi muốn tạo phiếu Yêu cầu mua hàng trực tiếp tại menu "Yêu cầu mua hàng" gồm nhiều vật tư Nhập kho và gửi duyệt, để bộ phận Mua hàng mua đúng hàng tôi cần.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-1.md; khao-sat-lan-2-yeu-cau-mua-hang.md (v0.2); AS-28, AS-29, AS-35
- **Acceptance criteria:**
  1. **Given** tôi thuộc bộ phận Hành chính (mã HC) **When** tôi lưu phiếu mới ngày 20/10/2026 **Then** phiếu nhận số `HC_0012_20_10_26` (AS-28), Người tạo, Bộ phận, Ngày tạo tự điền theo tôi.
  2. **Given** phiếu có ít nhất một dòng đủ Vật tư, Đơn vị tính, Nhập kho, Số lượng **When** tôi bấm "Gửi duyệt" **Then** phiếu chuyển "Chờ duyệt" và Trưởng nhóm của tôi nhận activity duyệt.
  3. **Given** tôi tìm vật tư trên dòng **When** danh sách vật tư hiện ra **Then** danh sách chỉ có vật tư loại "Nhập kho", không có vật tư "Dịch vụ".
  4. **Given** hai dòng cùng vật tư và cùng nhà cung cấp **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Trùng vật tư và nhà cung cấp với dòng <số dòng>".
  5. **Given** một dòng để trống số lượng **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Không được để trống số lượng".

#### US-02 — Sửa và gửi lại yêu cầu bị từ chối
- **Story:** Là Người đề xuất, tôi muốn yêu cầu bị từ chối tự về Nháp và tôi nhận email nêu lý do, để sửa và gửi lại ngay mà không phải tạo phiếu mới.
- **Ưu tiên:** Must
- **Nguồn:** tra-loi-cau-hoi-mo-lan-1.md (v0.3); AS-09
- **Acceptance criteria:**
  1. **Given** phiếu của tôi bị từ chối ở cấp bất kỳ **When** người duyệt xác nhận từ chối **Then** phiếu về "Nháp" và tôi nhận email nêu người từ chối, cấp duyệt và lý do.
  2. **Given** phiếu bị từ chối đã về "Nháp" **When** tôi mở phiếu **Then** đầu phiếu hiện thông báo lý do từ chối gần nhất và chatter còn lịch sử từ chối.
  3. **Given** tôi sửa dòng và bấm "Gửi duyệt" **When** hệ thống ghi nhận **Then** phiếu chuyển "Chờ duyệt" từ cấp 1.

#### US-03 — Theo dõi yêu cầu và chứng từ liên quan
- **Story:** Là Người đề xuất, tôi muốn xem trạng thái yêu cầu và các RFQ, đơn mua hàng, phiếu DO sinh ra từ nó, để biết khi nào có hàng.
- **Ưu tiên:** Should
- **Nguồn:** Đề xuất của BA (brainstorm)
- **Acceptance criteria:**
  1. **Given** yêu cầu đã duyệt xong **When** tôi mở phiếu **Then** tôi thấy nút thông minh "RFQ/Đơn mua hàng" kèm số lượng chứng từ và mở được danh sách chứng từ đó.
  2. **Given** tôi mở danh sách Yêu cầu mua hàng **When** tôi dùng bộ lọc mặc định "Của tôi" **Then** danh sách chỉ hiện các phiếu tôi tạo.

#### US-04 — Huỷ yêu cầu chưa duyệt xong
- **Story:** Là Người đề xuất, tôi muốn huỷ yêu cầu khi không còn nhu cầu, để Mua hàng không xử lý thừa.
- **Ưu tiên:** Should
- **Nguồn:** AS-14
- **Acceptance criteria:**
  1. **Given** phiếu ở trạng thái "Nháp", "Chờ duyệt" hoặc "Từ chối" **When** tôi bấm "Huỷ" **Then** phiếu chuyển "Đã huỷ" và các activity duyệt đang mở bị xoá.
  2. **Given** phiếu đã "Đã duyệt" **When** tôi mở phiếu **Then** nút "Huỷ" không hiển thị.

#### US-19 — Tạo Yêu cầu mua hàng từ Hợp đồng
- **Story:** Là Người đề xuất, tôi muốn tạo Yêu cầu mua hàng ngay từ một Hợp đồng còn hiệu lực, để dùng sẵn nhà cung cấp và đơn giá đã ký.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-2-yeu-cau-mua-hang.md; AS-30, AS-36
- **Acceptance criteria:**
  1. **Given** Hợp đồng HĐ-HH-2026-01 "Đang hiệu lực" **When** tôi bấm "Tạo yêu cầu mua hàng" trên hợp đồng **Then** hệ thống mở YCMH mới có Nguồn tạo = HĐ-HH-2026-01, chép mọi dòng vật tư với nhà cung cấp, đơn giá của hợp đồng và số lượng để trống.
  2. **Given** dòng được chép từ hợp đồng **When** tôi sửa đơn giá **Then** ô đơn giá bị khoá.
  3. **Given** hợp đồng đã hết hiệu lực **When** tôi mở hợp đồng **Then** nút "Tạo yêu cầu mua hàng" không hiển thị.

#### US-20 — Tạo Yêu cầu mua hàng từ Báo giá NCC
- **Story:** Là Người đề xuất, tôi muốn tạo Yêu cầu mua hàng từ một Báo giá NCC còn hiệu lực, để dùng sẵn vật tư và giá nhà cung cấp đã báo.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-2-yeu-cau-mua-hang.md; _changes/20261020-074707.md; AS-33, AS-36
- **Acceptance criteria:**
  1. **Given** Báo giá NCC BG-PV-1510 còn hiệu lực **When** tôi bấm "Tạo yêu cầu mua hàng" **Then** YCMH mới có Nguồn tạo = BG-PV-1510, chép mọi dòng với nhà cung cấp và đơn giá của báo giá, số lượng để trống.
  2. **Given** báo giá quá ngày "Hiệu lực đến" **When** tôi mở báo giá **Then** nút "Tạo yêu cầu mua hàng" không hiển thị.

#### US-21 — Tự điền nhà cung cấp và đơn giá
- **Story:** Là Người đề xuất, tôi muốn hệ thống tự điền nhà cung cấp và đơn giá khi tôi chọn vật tư, để không phải tra hợp đồng hay bảng giá.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-2-yeu-cau-mua-hang.md; AS-30, AS-31, AS-32
- **Acceptance criteria:**
  1. **Given** vật tư "Giấy A4 Double A 80gsm" có hợp đồng HĐ-HH-2026-01 còn hiệu lực, giá 78.000₫ **When** tôi chọn vật tư trên YCMH tạo trực tiếp **Then** dòng tự điền nhà cung cấp Hồng Hà, đơn giá 78.000₫, nguồn giá "Hợp đồng HĐ-HH-2026-01".
  2. **Given** vật tư "Bút bi Thiên Long TL-027" không có hợp đồng còn hiệu lực nhưng có Price List Hồng Hà 4.500₫ **When** tôi chọn vật tư **Then** dòng tự điền Hồng Hà, 4.500₫, nguồn giá "Price List".
  3. **Given** vật tư không có hợp đồng và không có Price List **When** tôi chọn vật tư **Then** nhà cung cấp và đơn giá để trống, nguồn giá "Không có", tôi chọn nhà cung cấp bằng tay.

### 3.2 Nhân viên Mua hàng (MH)

#### US-05 — Duyệt cấp 2 Yêu cầu mua hàng
- **Story:** Là Nhân viên MH, tôi muốn kiểm tra và duyệt hoặc từ chối Yêu cầu mua hàng sau khi Trưởng nhóm duyệt, để chỉ những nhu cầu hợp lệ đi tiếp tới BOD.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-1.md; khao-sat-lan-2-yeu-cau-mua-hang.md (v0.2: MH là cấp 2); AS-32, AS-09
- **Acceptance criteria:**
  1. **Given** phiếu đã được Trưởng nhóm duyệt **When** tôi bấm "Duyệt" **Then** phiếu chuyển sang chờ BOD duyệt và BOD nhận activity duyệt.
  2. **Given** phiếu có dòng chưa có nhà cung cấp **When** tôi bấm "Duyệt" **Then** hệ thống chặn và báo tên vật tư thiếu nhà cung cấp (AS-32).
  3. **Given** tôi bấm "Từ chối" **When** tôi để trống lý do **Then** hệ thống không cho xác nhận và báo "Vui lòng nhập lý do từ chối".
  4. **Given** Trưởng nhóm chưa duyệt **When** tôi mở phiếu **Then** nút "Duyệt" không hiển thị với tôi.

#### US-06 — Nhận RFQ tự động gộp theo vendor
- **Story:** Là Nhân viên MH, tôi muốn hệ thống tự tạo RFQ ngay khi yêu cầu được duyệt xong, gộp các sản phẩm cùng vendor vào một phiếu, để không phải lập RFQ thủ công.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-1.md; AS-05
- **Acceptance criteria:**
  1. **Given** yêu cầu có 3 dòng: 2 dòng vendor A, 1 dòng vendor B **When** cấp duyệt cuối bấm "Duyệt" **Then** hệ thống tạo đúng 2 RFQ trạng thái "Nháp": RFQ vendor A có 2 dòng, RFQ vendor B có 1 dòng.
  2. **Given** RFQ được tạo tự động **When** tôi mở RFQ **Then** trường "Yêu cầu mua hàng" trỏ về phiếu gốc và mỗi dòng giữ số lượng, đơn vị tính, ngày cần hàng của dòng yêu cầu.
  3. **Given** yêu cầu đã sinh RFQ **When** có người bấm "Duyệt" lại trên cùng phiếu **Then** hệ thống không tạo thêm RFQ trùng.

#### US-07 — Gửi email xin báo giá tới nhiều nhà cung cấp
- **Story:** Là Nhân viên MH, tôi muốn bấm "Send email" trên RFQ, chọn nhiều nhà cung cấp và soạn một email, để hệ thống gửi riêng cho từng nhà cung cấp xin báo giá.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-3-yeu-cau-bao-gia.md (v0.3); tra-loi-cau-hoi-mo-lan-1.md; AS-13, AS-44
- **Acceptance criteria:**
  1. **Given** RFQ "Nháp" **When** tôi bấm "Send email" **Then** popup mở với ô "Gửi đến" điền sẵn NCC của RFQ, tiêu đề, nội dung có bảng sản phẩm của phiếu, đính kèm PDF RFQ và file Excel mẫu báo giá.
  2. **Given** tôi nhập 3 NCC ngăn cách bằng ";" **When** bấm "Gửi" **Then** hệ thống gửi 3 email riêng, mỗi email chỉ có 1 người nhận, và RFQ chuyển "RFQ".
  3. **Given** một NCC chưa có email **When** bấm "Gửi" **Then** hệ thống chặn, báo tên NCC và không gửi email nào.

#### US-08 — Hỏi giá thêm vendor khác cho cùng nhu cầu **[Đã bỏ — v0.3]**
- **Lý do bỏ:** giữ 1 RFQ, gửi email riêng tới N NCC (US-07) và so sánh, chọn NCC cho cả phiếu (US-09) — _changes/20261020-093008.md quyết định #8.
- **Story:** Là Nhân viên MH, tôi muốn tạo RFQ thay thế cho vendor khác với cùng sản phẩm, để so sánh giá trước khi chọn.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-1.md ("gửi Email đến nhiều vendor"); AS-06
- **Acceptance criteria:**
  1. **Given** một RFQ đang mở **When** tôi bấm "Tạo RFQ thay thế", chọn vendor C và xác nhận **Then** hệ thống tạo RFQ mới cho vendor C với cùng dòng sản phẩm, số lượng và liên kết vào nhóm thay thế của RFQ gốc.
  2. **Given** vendor C đã có RFQ trong nhóm thay thế **When** tôi chọn lại vendor C **Then** hệ thống báo "Vendor C đã có RFQ trong nhóm này".

#### US-09 — So sánh giá và chọn nhà cung cấp
- **Story:** Là Nhân viên MH, tôi muốn bấm "So sánh giá" để xem báo giá của các NCC cạnh nhau và chọn 1 NCC cho cả phiếu, để chọn giá tốt nhất mà không phải tạo nhiều RFQ.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-3-yeu-cau-bao-gia.md (v0.3); _changes/20261020-093008.md #8; AS-46
- **Acceptance criteria:**
  1. **Given** RFQ đã có báo giá của 2 NCC **When** tôi bấm "So sánh giá" **Then** màn hình hiện mỗi vật tư một hàng, mỗi NCC một cột với đơn giá, thành tiền, tổng, và đánh dấu giá thấp nhất từng dòng, tổng thấp nhất.
  2. **Given** tôi bấm "Chọn NCC này" ở cột Công ty CP Thế Giới Di Động **When** xác nhận **Then** RFQ đổi NCC sang Thế Giới Di Động, đơn giá các dòng lấy theo báo giá của NCC này.
  3. **Given** báo giá của một NCC thiếu giá cho một vật tư **When** tôi bấm "Chọn NCC này" ở cột đó **Then** hệ thống chặn và báo vật tư thiếu giá.

#### US-10 — Gửi duyệt đơn mua hàng
- **Story:** Là Nhân viên MH, tôi muốn bấm "Approve" sau khi chọn NCC và tạo Đề nghị thanh toán, để đơn vào quy trình duyệt.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-1.md; khao-sat-lan-3-yeu-cau-bao-gia.md (v0.3); AS-39, AS-40
- **Acceptance criteria:**
  1. **Given** RFQ trạng thái "RFQ", mọi dòng có giá và có ĐNTT "Chờ kế toán duyệt" **When** tôi bấm "Approve" **Then** đơn chuyển "Chờ duyệt" và Trưởng phòng Mua hàng nhận activity duyệt.
  2. **Given** đơn chưa có ĐNTT **When** tôi bấm "Approve" **Then** hệ thống chặn và báo "Phải tạo Đề nghị thanh toán trước khi gửi duyệt".
  3. **Given** RFQ có dòng số lượng > 0 nhưng đơn giá = 0 **When** tôi bấm "Approve" **Then** hệ thống chặn và báo "Chưa nhập đơn giá cho sản phẩm <tên>".

#### US-11 — Tạo Đề nghị thanh toán trước khi gửi duyệt
- **Story:** Là Nhân viên MH, tôi muốn tạo Đề nghị thanh toán ngay sau khi chọn NCC, để đơn đủ điều kiện gửi duyệt và Kế toán chuẩn bị thanh toán.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-3-yeu-cau-bao-gia.md (v0.3); AS-10, AS-40
- **Acceptance criteria:**
  1. **Given** RFQ trạng thái "RFQ" đã chọn NCC **When** tôi bấm "Tạo đề nghị thanh toán" **Then** hệ thống mở phiếu ĐNTT điền sẵn NCC, mã RFQ, số tiền = tổng đơn.
  2. **Given** phiếu ĐNTT hợp lệ **When** tôi bấm "Gửi kế toán" **Then** ĐNTT chuyển "Chờ kế toán duyệt", RFQ giữ trạng thái "RFQ" và nút "Approve" được mở.
  3. **Given** số tiền đề nghị lớn hơn tổng đơn **When** tôi bấm "Gửi kế toán" **Then** hệ thống chặn và báo "Số tiền đề nghị vượt tổng giá trị đơn mua hàng".

#### US-12 — Đơn duyệt xong tự chuyển PO và tạo phiếu DO
- **Story:** Là Nhân viên MH, tôi muốn đơn được duyệt xong tự chuyển PO và tạo phiếu DO cho kho, để không phải thao tác thêm bước nhận hàng. *(Sửa v0.3 — v0.2 là nút "Xác nhận đã nhận hàng" chuyển Waiting PO → PO; nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3)*
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-3-yeu-cau-bao-gia.md; AS-12, AS-29, AS-43
- **Acceptance criteria:**
  1. **Given** đơn vật tư Nhập kho "Chờ duyệt" **When** Trưởng phòng Mua hàng bấm "Duyệt" **Then** đơn chuyển "PO" và hệ thống tạo phiếu DO trạng thái "Sẵn sàng" cho mỗi kho nhận.
  2. **Given** đơn đã "PO" **When** tôi mở đơn **Then** không có nút "Xác nhận đã nhận hàng" và smart button "Phiếu DO" hiện số phiếu.
  3. **Given** Thủ kho hoàn tất phiếu DO ngày 29/10/2026 **When** tôi mở đơn **Then** "Ngày nhận hàng thực tế" hiện 29/10/2026.

#### US-13 — Huỷ RFQ hoặc đơn mua hàng
- **Story:** Là Nhân viên MH, tôi muốn huỷ RFQ hoặc đơn mua hàng không còn dùng, để danh sách chỉ còn chứng từ đang xử lý.
- **Ưu tiên:** Should
- **Nguồn:** AS-14
- **Acceptance criteria:**
  1. **Given** đơn ở trạng thái trước `PO` **When** tôi bấm "Huỷ" và nhập lý do **Then** đơn chuyển "Đã huỷ" và lý do ghi trên chatter.
  2. **Given** đơn có Đề nghị thanh toán ở trạng thái "Đã thanh toán" **When** tôi bấm "Huỷ" **Then** hệ thống chặn và báo "Đơn đã được thanh toán, liên hệ Kế toán để xử lý".

#### US-22 — Quản lý danh mục Hợp đồng mua hàng
- **Story:** Là Nhân viên MH, tôi muốn lưu hợp đồng với nhà cung cấp gồm vật tư, đơn giá và thời hạn hiệu lực, để hệ thống dùng giá hợp đồng khi tạo Yêu cầu mua hàng.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-2-yeu-cau-mua-hang.md; AS-30
- **Acceptance criteria:**
  1. **Given** tôi nhập Số hợp đồng, Nhà cung cấp, Hiệu lực từ, Hiệu lực đến và ít nhất một dòng vật tư có đơn giá > 0 **When** tôi bấm "Xác nhận" **Then** hợp đồng chuyển "Đang hiệu lực".
  2. **Given** dòng hợp đồng chọn vật tư loại "Dịch vụ" **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Hợp đồng chỉ áp dụng cho vật tư Nhập kho".
  3. **Given** "Hiệu lực đến" sớm hơn "Hiệu lực từ" **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Ngày kết thúc phải sau ngày bắt đầu".

#### US-23 — Quản lý danh mục Báo giá NCC
- **Story:** Là Nhân viên MH, tôi muốn lưu báo giá nhà cung cấp gửi về gồm vật tư, đơn giá và hạn hiệu lực, để người đề xuất tạo Yêu cầu mua hàng từ báo giá đó.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-2-yeu-cau-mua-hang.md; _changes/20261020-074707.md; AS-33
- **Acceptance criteria:**
  1. **Given** tôi nhập Số báo giá, Nhà cung cấp, Ngày báo giá, Hiệu lực đến, ít nhất một dòng vật tư có đơn giá > 0 và đính kèm file báo giá **When** tôi bấm "Xác nhận" **Then** báo giá chuyển "Còn hiệu lực".
  2. **Given** ngày hiện tại sau "Hiệu lực đến" **When** hệ thống chạy kiểm tra hằng ngày **Then** báo giá chuyển "Hết hiệu lực".

#### US-25 — Mua Dịch vụ bằng PO trực tiếp
- **Story:** Là Nhân viên MH, tôi muốn tạo thẳng PO cho vật tư Dịch vụ, không cần Yêu cầu mua hàng và Yêu cầu báo giá, để mua dịch vụ nhanh nhưng vẫn có ĐNTT và duyệt đơn. *(Sửa v0.3 — v0.2 là RFQ trực tiếp)*
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-3-yeu-cau-bao-gia.md; AS-42
- **Acceptance criteria:**
  1. **Given** tôi bấm "Mới" ở danh sách đơn mua và chọn vật tư Dịch vụ **When** tôi lưu **Then** PO dịch vụ "Nháp" được tạo với số `MH-PO-<XXXX>-<DD>-<MM>-<YYYY>`, không có trường Yêu cầu mua hàng và không có nút "Send email".
  2. **Given** PO dịch vụ chưa có ĐNTT **When** tôi bấm "Approve" **Then** hệ thống chặn và báo "Phải tạo Đề nghị thanh toán trước khi gửi duyệt".
  3. **Given** PO dịch vụ "Chờ duyệt" **When** Trưởng phòng Mua hàng bấm "Duyệt" **Then** đơn chuyển "PO" và không có phiếu DO nào được tạo.
  4. **Given** đơn tạo trực tiếp có vật tư "Nhập kho" **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Vật tư Nhập kho phải mua qua Yêu cầu mua hàng".

#### US-26 — Tự đọc file Excel báo giá từ email NCC
- **Story:** Là Nhân viên MH, tôi muốn hệ thống tự lưu email NCC trả lời và đọc file Excel báo giá đính kèm, để không phải gõ lại giá từng NCC.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-3-yeu-cau-bao-gia.md (v0.3); AS-44, AS-45, AS-46
- **Acceptance criteria:**
  1. **Given** NCC Phong Vũ reply email RFQ kèm file Excel đúng mẫu **When** Odoo nhận email **Then** chatter RFQ có email trả lời kèm file và RFQ có báo giá NCC mới với giá từng vật tư.
  2. **Given** file Excel sai mẫu **When** Odoo nhận email **Then** chatter ghi lỗi kèm tên file và lý do, tôi nhập tay báo giá cho NCC đó.
  3. **Given** NCC gửi báo giá lần 2 **When** hệ thống đọc xong **Then** báo giá lần 1 của NCC đó chuyển "Đã thay thế" và màn so sánh dùng báo giá lần 2.

#### US-27 — Biết RFQ được tạo từ Yêu cầu mua hàng nào
- **Story:** Là Nhân viên MH, tôi muốn RFQ ghi rõ mã Yêu cầu mua hàng gốc và tìm được RFQ theo mã đó, để truy vết đơn mua về nhu cầu ban đầu.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-3-yeu-cau-bao-gia.md (v0.3); _changes/20261020-093008.md #6; AS-42
- **Acceptance criteria:**
  1. **Given** YCMH HC_0012_20_10_26 sinh 2 RFQ **When** tôi mở mỗi RFQ **Then** trường "Mã Yêu cầu mua hàng" hiện HC_0012_20_10_26 và bấm vào mở được YCMH gốc.
  2. **Given** tôi gõ "HC_0012" ở ô tìm kiếm danh sách RFQ **When** tìm **Then** danh sách hiện đúng 2 RFQ của YCMH đó.
  3. **Given** YCMH gốc đã bị huỷ **When** tôi tìm theo mã YCMH **Then** vẫn tìm được RFQ nhờ mã lưu ngầm.

### 3.3 Trưởng nhóm

#### US-14 — Duyệt cấp 1 Yêu cầu mua hàng
- **Story:** Là Trưởng nhóm, tôi muốn duyệt hoặc từ chối Yêu cầu mua hàng do thành viên nhóm tạo, để kiểm soát nhu cầu mua của nhóm.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-2-yeu-cau-mua-hang.md (v0.2: thay "Trưởng phòng duyệt cấp 2"); AS-34, AS-09
- **Acceptance criteria:**
  1. **Given** phiếu "Chờ duyệt" do thành viên nhóm tôi tạo **When** tôi bấm "Duyệt" **Then** phiếu chuyển sang chờ Nhân viên MH duyệt (cấp 2).
  2. **Given** phiếu do người không thuộc nhóm tôi tạo **When** tôi mở phiếu **Then** nút "Duyệt" không hiển thị với tôi.
  3. **Given** tôi bấm "Từ chối" và nhập lý do **When** tôi xác nhận **Then** phiếu chuyển "Từ chối" và Người đề xuất nhận thông báo kèm lý do.

### 3.4 Người duyệt đơn mua hàng

#### US-15 — Duyệt hoặc từ chối đơn mua hàng
- **Story:** Là Trưởng phòng Mua hàng, tôi muốn duyệt đơn sau khi MH chọn NCC và tạo ĐNTT, để kiểm soát mua hàng. *(Sửa v0.3 — bỏ ngưỡng giá trị; nguồn: tra-loi-cau-hoi-mo-lan-1.md)*
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-1.md; tra-loi-cau-hoi-mo-lan-1.md; AS-39, AS-09
- **Acceptance criteria:**
  1. **Given** đơn "Chờ duyệt" tổng 69.927.000₫ **When** tôi bấm "Duyệt" **Then** đơn chuyển "PO" (US-12).
  2. **Given** đơn "Chờ duyệt" tổng 120.000.000₫ **When** tôi bấm "Duyệt" **Then** đơn chuyển "PO", không cần thêm cấp duyệt nào.
  3. **Given** tôi bấm "Từ chối" và nhập lý do **When** tôi xác nhận **Then** đơn vật tư Nhập kho về "RFQ" (đơn dịch vụ về "Nháp") và Nhân viên MH nhận email kèm lý do.

### 3.5 Kế toán

#### US-16 — Xử lý Đề nghị thanh toán
- **Story:** Là Kế toán, tôi muốn duyệt hoặc từ chối Đề nghị thanh toán và ghi nhận thanh toán, để trả tiền vendor đúng đơn đã duyệt.
- **Ưu tiên:** Must
- **Nguồn:** AS-10
- **Acceptance criteria:**
  1. **Given** Đề nghị thanh toán "Chờ kế toán duyệt" **When** tôi bấm "Duyệt" **Then** phiếu chuyển "Đã duyệt".
  2. **Given** phiếu "Đã duyệt" **When** tôi bấm "Ghi nhận thanh toán", chọn sổ nhật ký và ngày thanh toán, xác nhận **Then** hệ thống tạo bút toán thanh toán cho vendor và phiếu chuyển "Đã thanh toán".
  3. **Given** tôi bấm "Từ chối" và nhập lý do **When** tôi xác nhận **Then** phiếu chuyển "Từ chối", đơn mua hàng quay về "Đã duyệt" và Nhân viên MH nhận thông báo.

### 3.6 Thủ kho

#### US-17 — Nhập kho theo phiếu DO
- **Story:** Là Thủ kho, tôi muốn kiểm đếm hàng theo phiếu DO và xác nhận, để tồn kho cập nhật đúng số thực nhận.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-1.md; AS-12
- **Acceptance criteria:**
  1. **Given** phiếu DO "Sẵn sàng" **When** tôi nhập số lượng thực nhận bằng số lượng yêu cầu và bấm "Xác nhận" **Then** phiếu chuyển "Hoàn tất" và tồn kho tăng đúng số lượng.
  2. **Given** số lượng thực nhận nhỏ hơn số lượng yêu cầu **When** tôi bấm "Xác nhận" và chọn "Tạo backorder" **Then** hệ thống hoàn tất phần đã nhận và tạo phiếu DO mới cho phần còn thiếu.

### 3.7 Quản trị hệ thống

#### US-18 — Cấu hình người duyệt, mẫu email và mẫu báo giá
- **Story:** Là Quản trị hệ thống, tôi muốn cấu hình người duyệt đơn mua hàng, mẫu email và mẫu file Excel báo giá, để thay đổi chính sách mà không cần sửa code. *(Sửa v0.3 — bỏ ngưỡng duyệt)*
- **Ưu tiên:** Should
- **Nguồn:** Đề xuất của BA (brainstorm); tra-loi-cau-hoi-mo-lan-1.md; AS-39, AS-44
- **Acceptance criteria:**
  1. **Given** tôi thuộc nhóm Quản trị **When** tôi đổi người duyệt đơn mua hàng và lưu **Then** các đơn gửi duyệt sau thời điểm lưu giao activity cho người duyệt mới.
  2. **Given** tôi tải lên mẫu Excel báo giá mới **When** MH gửi email RFQ sau đó **Then** email đính kèm mẫu mới.
  3. **Given** người dùng không thuộc nhóm Quản trị **When** họ mở menu cấu hình mua hàng **Then** menu không hiển thị.

### 3.8 BOD

#### US-24 — Duyệt cấp 3 Yêu cầu mua hàng
- **Story:** Là thành viên BOD, tôi muốn duyệt cuối Yêu cầu mua hàng đã qua Trưởng nhóm và MH, để chỉ những nhu cầu được ban giám đốc đồng ý mới sinh RFQ.
- **Ưu tiên:** Must
- **Nguồn:** khao-sat-lan-2-yeu-cau-mua-hang.md; AS-34
- **Acceptance criteria:**
  1. **Given** phiếu đã được Nhân viên MH duyệt **When** một thành viên BOD bấm "Duyệt" **Then** phiếu chuyển "Đã duyệt" và hệ thống tạo RFQ theo US-06.
  2. **Given** phiếu chưa được MH duyệt **When** thành viên BOD mở phiếu **Then** nút "Duyệt" không hiển thị.
  3. **Given** thành viên BOD bấm "Từ chối" và nhập lý do **When** xác nhận **Then** phiếu chuyển "Từ chối" và Người đề xuất nhận thông báo kèm lý do.

## 4. Quy trình nghiệp vụ mong muốn (TO-BE)

Sơ đồ Activity – Swimlane (v0.3; đặc tả trong `ui/swimlanes/`, ảnh trong `ui/diagrams/`):

![Swimlane 1 — Vật tư Nhập kho: Yêu cầu mua hàng](ui/diagrams/swimlane-01-yeu-cau-mua-hang.png)

![Swimlane 2 — Vật tư Nhập kho: Yêu cầu báo giá → PO → nhập kho](ui/diagrams/swimlane-02-yeu-cau-bao-gia-po.png)

![Swimlane 3 — Vật tư Dịch vụ: PO trực tiếp](ui/diagrams/swimlane-03-dich-vu.png)

| Bước | Vai trò | Mô tả | User story |
|---|---|---|---|
| 0 | Nhân viên MH | Lưu Hợp đồng, Báo giá NCC | US-22, US-23 |
| 1 | Người đề xuất | Tạo (trực tiếp / từ Hợp đồng / từ Báo giá NCC) và gửi Yêu cầu mua hàng | US-01, US-02, US-04, US-19, US-20, US-21 |
| 2a | Trưởng nhóm | Duyệt cấp 1 | US-14 |
| 2b | Nhân viên MH | Duyệt cấp 2 | US-05 |
| 3 | BOD | Duyệt cấp 3 | US-24 |
| 4 | Hệ thống | Tạo RFQ theo NCC, kế thừa YCMH, gắn mã YCMH | US-06, US-27 |
| 5 | Nhân viên MH | Send email tới N NCC (gửi riêng từng NCC) | US-07 |
| 6 | Hệ thống | Lưu reply, đọc Excel báo giá | US-26 |
| 7 | Nhân viên MH | So sánh giá, chọn 1 NCC cho cả phiếu | US-09 |
| 8 | Nhân viên MH | Tạo Đề nghị thanh toán (bắt buộc), gửi Kế toán | US-11 |
| 9 | Nhân viên MH | Bấm Approve | US-10 |
| 10 | Trưởng phòng Mua hàng | Duyệt đơn (không ngưỡng) | US-15 |
| 11 | Hệ thống | Chuyển PO, tự tạo phiếu DO | US-12 |
| 12 | Kế toán | Duyệt và ghi nhận thanh toán | US-16 |
| 13 | Thủ kho | Nhập kho theo phiếu DO | US-17 |
| DV | Nhân viên MH | Dịch vụ: tạo PO trực tiếp → ĐNTT → Approve → PO, không DO | US-25 |
| — | Người đề xuất / MH | Theo dõi, huỷ chứng từ | US-03, US-13 |

## 5. Yêu cầu chung (không gắn vai trò)
- Giao diện tiếng Việt; tiền tệ VND định dạng `1.250.000₫`; ngày `dd/mm/yyyy`.
- Mọi chuyển trạng thái, duyệt, từ chối ghi lên chatter kèm người thực hiện và thời điểm.
- Người duyệt nhận activity trên Odoo và email thông báo khi có phiếu chờ duyệt (AS-18).
- Phân quyền theo nhóm: Người đề xuất chỉ xem phiếu của mình; Trưởng nhóm xem phiếu của thành viên nhóm; BOD xem mọi phiếu; MH, Kế toán, Thủ kho xem chứng từ thuộc nghiệp vụ của mình.

## 6. Assumptions & Open Questions

### 6.1 Giả định
| Mã | Giả định | Lý do chọn | Liên quan |
|---|---|---|---|
| AS-01 | Odoo 17 Enterprise, on-premise hoặc Odoo.sh, cho phép module tuỳ biến — **xác nhận v0.3** (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #1) | Approvals là module Enterprise; cần code tuỳ biến | Toàn hệ thống |
| AS-02 | KPI (sửa v0.2): 100% đơn mua vật tư Nhập kho có Yêu cầu mua hàng đã duyệt làm gốc và lịch sử duyệt trên chatter | Input chưa có KPI | Mục 1.3 |
| AS-03 | **[Đã thay — v0.2]** ~~Duyệt tuần tự MH → Trưởng phòng~~. Khảo sát lần 2 xác nhận Trưởng nhóm → MH → BOD | khao-sat-lan-2-yeu-cau-mua-hang.md | US-05, US-14, US-24 |
| AS-04 | **[Đã thay — v0.2]** ~~Vendor trên dòng → bảng giá NCC~~. Khảo sát lần 2: Hợp đồng → Price List; chi tiết AS-30, AS-31, AS-32 | khao-sat-lan-2-yeu-cau-mua-hang.md | US-05, US-06, US-21 |
| AS-05 | Mỗi YCMH sinh RFQ riêng theo vendor, không gộp với YCMH khác — **xác nhận v0.3** (tra-loi-cau-hoi-mo-lan-1.md) | Giữ truy vết 1 yêu cầu → n RFQ | US-06 |
| AS-06 | **[Đã thay — v0.3]** ~~Hỏi giá nhiều vendor bằng RFQ thay thế (Alternatives)~~. Giữ 1 RFQ, gửi email riêng tới N NCC (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #8) | Tính năng chuẩn, không cần custom | US-08 |
| AS-07 | **[Đã thay — v0.3]** ~~Chọn giá theo dòng; RFQ không được chọn tự huỷ~~. Chọn 1 NCC cho cả phiếu, RFQ đổi NCC và giá (_changes/20261020-093008.md #8) | Linh hoạt chọn vendor theo sản phẩm | US-09 |
| AS-08 | **[Đã thay — v0.3]** ~~Trưởng phòng Mua hàng duyệt mọi đơn; tổng ≥ 50.000.000₫ thêm Giám đốc~~. Không có ngưỡng (tra-loi-cau-hoi-mo-lan-1.md); người duyệt: AS-39 | Thông lệ phân cấp duyệt; input chưa có ngưỡng | US-10, US-15, US-18 |
| AS-09 | *(Sửa v0.3)* Từ chối bắt buộc lý do. YCMH bị từ chối về Nháp và gửi email cho người tạo (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #6); đơn mua hàng về RFQ (dịch vụ: Nháp); ĐNTT: AS-41 | Không mất dữ liệu đã nhập | US-02, US-05, US-14, US-15 |
| AS-10 | Đề nghị thanh toán là chứng từ mới gắn 1 đơn mua hàng; Kế toán duyệt và ghi nhận thanh toán | Input chỉ nêu tên chứng từ | US-11, US-16 |
| AS-11 | **[Đã thay — v0.3]** ~~Đơn chuyển Waiting PO khi ĐNTT được gửi kế toán~~. Bỏ Waiting PO; ĐNTT tạo trước khi gửi duyệt (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3) | Theo input: "tạo xong … chuyển waiting PO" | US-11 |
| AS-12 | Phiếu DO = phiếu nhập kho (Receipt), tạo ở trạng thái "Sẵn sàng"; Thủ kho xác nhận; nhận thiếu tạo backorder | Thuật ngữ DO trong input chưa rõ | US-12, US-17 |
| AS-13 | Vendor phải có email mới gửi được RFQ | Gửi RFQ qua email | US-07 |
| AS-14 | Huỷ được yêu cầu trước khi duyệt xong; huỷ được đơn trước trạng thái `PO` và khi chưa thanh toán | Tránh huỷ chứng từ đã phát sinh kho/tiền | US-04, US-13 |
| AS-15 | Hoá đơn nhà cung cấp dùng chuẩn Odoo, ngoài phạm vi | Input không đề cập | Phạm vi |
| AS-16 | **[Đã thay — v0.3]** ~~MH nhập giá vendor thủ công vào RFQ~~. Hệ thống đọc Excel từ email NCC reply; nhập tay khi file lỗi (khao-sat-lan-3-yeu-cau-bao-gia.md; AS-45) | Không có cổng vendor | US-09 |
| AS-17 | Chỉ dùng VND | Input không đề cập ngoại tệ | Phạm vi |
| AS-18 | Thông báo qua activity Odoo + email | Kênh chuẩn của Odoo | Mục 5 |
| AS-19 | (Sửa v0.2) Dòng bắt buộc: vật tư loại Nhập kho, đơn vị tính, kho nhận, số lượng > 0 (không để trống — khảo sát lần 2 xác nhận); ngày cần hàng không bắt buộc (AS-35) | Dữ liệu tối thiểu để tạo RFQ | US-01 |
| AS-20 | *(Sửa v0.3)* Mã tự động: YCMH theo AS-28, `DNTT/<năm>/<4 số>`; RFQ/đơn theo AS-42 (thay mã chuẩn `P<5 số>`) | Theo quy ước sequence Odoo | US-01, US-11 |
| AS-26 | Vật tư "Nhập kho" = sản phẩm loại Lưu kho (storable) của Odoo; vật tư "Dịch vụ" = sản phẩm loại Dịch vụ; không dùng loại Tiêu dùng | Khảo sát lần 2 chỉ nêu 2 loại | US-01, US-25 |
| AS-27 | **[Đã thay — v0.3]** ~~Đơn dịch vụ dùng chung nút "Xác nhận đã nhận hàng"~~. Đơn dịch vụ duyệt xong là PO, không có bước nhận hàng (khao-sat-lan-3-yeu-cau-bao-gia.md) | Giữ một luồng trạng thái cho mọi đơn | US-25 |
| AS-28 | Số phiếu YCMH = `<Mã BP>_<XXXX>_<DD>_<MM>_<YY>`: Mã BP là mã bộ phận của người tạo; XXXX đếm riêng theo bộ phận, về 0001 đầu mỗi năm; DD_MM_YY là ngày tạo (vd. `HC_0012_20_10_26`) | Mẫu số phiếu chưa nói cách đếm XXXX | US-01 |
| AS-29 | Kho nhận (cột "Nhập kho") mặc định là kho chính của công ty, người tạo sửa được theo từng dòng; một đơn mua sinh một phiếu DO cho mỗi kho nhận | Một YCMH có nhiều kho (người làm chốt); Odoo chuẩn nhận mỗi đơn vào một kho | US-01, US-12 |
| AS-30 | Hợp đồng = Purchase Agreement loại Hợp đồng khung (Blanket Order); còn hiệu lực khi trạng thái "Đang hiệu lực" và ngày hiện tại nằm trong khoảng hiệu lực; không kiểm tra số lượng còn lại | Tính năng chuẩn Odoo, có NCC, đơn giá, ngày hiệu lực | US-19, US-21, US-22 |
| AS-31 | Nhiều hợp đồng còn hiệu lực cùng vật tư → chọn đơn giá thấp nhất, bằng nhau thì hợp đồng hết hạn sớm nhất. Price List chọn theo quy tắc chuẩn Odoo (thứ tự, số lượng tối thiểu, hiệu lực) | Input chưa có tiêu chí chọn | US-21 |
| AS-32 | Giá lấy từ hợp đồng bị khoá; giá từ Price List sửa được; không có nguồn giá thì người tạo nhập tay NCC (đơn giá tuỳ chọn). Mọi dòng phải có NCC trước khi Nhân viên MH duyệt cấp 2 | Bảo đảm tạo được RFQ theo NCC | US-05, US-21 |
| AS-33 | Báo giá NCC là danh mục mới (NCC, ngày báo giá, hiệu lực đến, dòng vật tư – đơn giá); không tham gia tự tra giá; hết hiệu lực thì không tạo được YCMH | Quy tắc tra giá chỉ nêu Hợp đồng và Price List | US-20, US-23 |
| AS-34 | Trưởng nhóm = quản lý trực tiếp (Manager) trên hồ sơ nhân viên của người tạo; người tạo chưa có Trưởng nhóm thì chặn gửi duyệt. BOD = nhóm quyền "BOD", một thành viên duyệt là đủ | Input chỉ nêu "Trưởng nhóm (theo người tạo)" và "BOD" | US-14, US-24 |
| AS-35 | Đầu phiếu giữ "Ngày cần hàng" (không bắt buộc, làm ngày dự kiến trên RFQ); "Lý do mua" bỏ, thay bằng "Ghi chú" (không bắt buộc) | Khảo sát lần 2 không nhắc 2 trường này | US-01 |
| AS-36 | Tạo YCMH từ Hợp đồng / Báo giá NCC: chép mọi dòng, số lượng để trống cho người tạo nhập, dòng không cần thì xoá; NCC và đơn giá khoá theo chứng từ nguồn; được thêm dòng vật tư khác (tự tra giá) | Input chưa mô tả chi tiết | US-19, US-20 |
| AS-37 | *(Sửa v0.3)* Giữ cả hai lớp duyệt: YCMH (Trưởng nhóm → MH → BOD) và đơn mua hàng 1 cấp sau khi chọn NCC và tạo ĐNTT (AS-39) — khao-sat-lan-3-yeu-cau-bao-gia.md xác nhận còn bước duyệt đơn | Khảo sát lần 2 mới đi chi tiết phiếu YCMH | US-10, US-15 |
| AS-39 | Đơn mua hàng duyệt 1 cấp bởi Trưởng phòng Mua hàng, không phân ngưỡng giá trị | tra-loi-cau-hoi-mo-lan-1.md: không có ngưỡng; người duyệt chưa nói | US-15, US-18 |
| AS-40 | Gửi duyệt đơn yêu cầu ĐNTT đã gửi Kế toán (trạng thái "Chờ kế toán duyệt" trở lên); không cần Kế toán duyệt xong | khao-sat-lan-3-yeu-cau-bao-gia.md chỉ nói "bắt buộc tạo ĐNTT trước" | US-10, US-11 |
| AS-41 | ĐNTT bị Kế toán từ chối: đơn đang Chờ duyệt về RFQ (dịch vụ: Nháp); đơn đã PO giữ PO; MH tạo ĐNTT mới | Input chưa nói | US-16 |
| AS-42 | Số RFQ/PO = `<Mã BP>-PO-<XXXX>-<DD>-<MM>-<YYYY>-<NN>`: Mã BP, XXXX, ngày lấy từ YCMH gốc, NN là thứ tự RFQ trong YCMH (vd. `HC-PO-0012-20-10-2026-02`). PO dịch vụ: `<Mã BP người tạo>-PO-<XXXX>-<DD>-<MM>-<YYYY>`, XXXX đếm riêng (vd. `MH-PO-0003-21-10-2026`). Mã YCMH gốc lưu ngầm ở trường ẩn | Mẫu ở khao-sat-lan-3-yeu-cau-bao-gia.md; mục tiêu truy vết RFQ → YCMH (_changes/20261020-093008.md #6) | US-27 |
| AS-43 | Ngày dự kiến nhận hàng mặc định = Ngày cần hàng của YCMH (trống thì ngày tạo RFQ + 7 ngày), MH sửa được; Ngày nhận hàng thực tế = ngày hoàn tất phiếu DO cuối cùng của đơn, chỉ đọc | Input chưa nói cách lấy ngày | US-12 |
| AS-44 | Email xin báo giá có bảng sản phẩm của phiếu trong nội dung, đính kèm PDF RFQ và file Excel mẫu báo giá (Mã vật tư, Tên vật tư, ĐVT, Số lượng, Đơn giá, Ngày giao, Ghi chú) | Muốn tự đọc Excel thì cần mẫu cố định | US-07, US-26 |
| AS-45 | Odoo nhận reply qua incoming mail server và alias của RFQ; NCC xác định theo email người gửi; file sai mẫu thì MH nhập tay báo giá | Cơ chế mail gateway chuẩn của Odoo | US-26 |
| AS-46 | Kết quả đọc Excel lưu thành Báo giá NCC (FR-21) gắn với RFQ; báo giá mới của cùng NCC thay báo giá cũ ("Đã thay thế") | Tận dụng danh mục Báo giá NCC đã có | US-09, US-26 |
| AS-47 | File báo giá chỉ nhận .xlsx, ≤ 5 MB, ≤ 500 dòng; đọc xong ≤ 60 giây sau khi email tới | Giới hạn an toàn khi xử lý file đính kèm | US-26 |

### 6.2 Câu hỏi mở
| Mã | Câu hỏi | Người cần trả lời | Liên quan |
|---|---|---|---|
| OQ-01 | **Đã trả lời (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #1):** Odoo 17 bản trả phí, Odoo.sh hoặc on-premise, cài được module tuỳ biến | IT khách hàng | AS-01 |
| OQ-02 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md):** quy trình hiện tại làm thủ công, cần cải thiện. Còn mở: các bước hiện tại và chỉ số đo được | Khách hàng | Bối cảnh |
| OQ-03 | KPI, giá trị mục tiêu và mốc go-live? | Khách hàng | AS-02 |
| OQ-04 | **Đã trả lời (khao-sat-lan-2-yeu-cau-mua-hang.md):** Trưởng nhóm (theo người tạo) → User MH → BOD | Khách hàng | AS-03, US-05, US-14, US-24 |
| OQ-05 | **Đã trả lời một phần (khao-sat-lan-2-yeu-cau-mua-hang.md):** Hợp đồng còn hiệu lực → Price List. Còn mở → OQ-28 | Phòng Mua hàng | AS-04, US-06, US-21 |
| OQ-06 | **Đã trả lời (tra-loi-cau-hoi-mo-lan-1.md):** không cho phép gộp nhiều YCMH cùng vendor vào một RFQ | Phòng Mua hàng | AS-05 |
| OQ-07 | **Đã trả lời một phần (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #8):** 1 RFQ gửi email riêng tới N NCC; chọn 1 NCC cho cả phiếu. Còn mở: số NCC tối thiểu / tối đa (OQ-39) | Phòng Mua hàng | AS-06, AS-07, US-09 |
| OQ-08 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md):** đơn mua hàng không có ngưỡng giá trị. Còn mở: ai duyệt đơn (AS-39) | Ban giám đốc | AS-08, US-15 |
| OQ-09 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #6):** YCMH bị từ chối về Nháp và gửi email cho người tạo. Còn mở: đơn mua hàng và ĐNTT bị từ chối | Khách hàng | AS-09 |
| OQ-10 | Đề nghị thanh toán là tạm ứng trước khi nhận hàng hay thanh toán theo hoá đơn? Ai duyệt, có thanh toán một phần không? | Kế toán | AS-10, US-16 |
| OQ-11 | **Đã trả lời (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3):** bỏ Waiting PO; ĐNTT tạo trước khi duyệt, duyệt xong là PO + DO, không chờ thanh toán | Kế toán / Mua hàng | AS-11 |
| OQ-12 | "Phiếu DO" là phiếu gì? Tự động hoàn tất nhập kho hay để Thủ kho xác nhận? | Kho | AS-12, US-12, US-17 |
| OQ-13 | Hoá đơn nhà cung cấp và đối chiếu có nằm trong dự án không? | Kế toán | AS-15 |
| OQ-14 | Số người dùng và số Yêu cầu mua hàng mỗi tháng? | Khách hàng | Phi chức năng |
| OQ-15 | Có mẫu email / mẫu in RFQ, Đề nghị thanh toán theo mẫu công ty không? | Phòng Mua hàng | US-07 |
| OQ-16 | **Đã trả lời (khao-sat-lan-3-yeu-cau-bao-gia.md):** NCC reply email kèm file Excel báo giá; không cần cổng vendor | Phòng Mua hàng | AS-16 |
| OQ-17 | Có mua hàng bằng ngoại tệ không? | Kế toán | AS-17 |
| OQ-18 | Ngoài activity và email, có cần thông báo qua kênh khác (Zalo, SMS) không? | Khách hàng | AS-18 |
| OQ-19 | Quy tắc đánh mã Yêu cầu mua hàng, Đề nghị thanh toán theo mẫu công ty? | Kế toán | AS-20 |
| OQ-22 | Vật tư "Nhập kho" ứng với loại sản phẩm nào trong Odoo? Có dùng loại Tiêu dùng (consumable) không? | IT khách hàng | AS-26 |
| OQ-23 | **Đã trả lời một phần (khao-sat-lan-3-yeu-cau-bao-gia.md):** đơn dịch vụ duyệt xong là PO, không tạo DO, không có bước nhận hàng. Còn mở: có cần nghiệm thu dịch vụ không | Phòng Mua hàng | AS-27, US-25 |
| OQ-24 | XXXX trong số phiếu đếm theo bộ phận hay toàn công ty? Về 0001 theo năm, tháng hay ngày? Mã BP lấy ở đâu? | Kế toán / IT | AS-28, US-01 |
| OQ-25 | Kho nhận mặc định của dòng là kho nào? Bộ phận nào được chọn kho nào? | Kho | AS-29 |
| OQ-26 | Hợp đồng có giới hạn số lượng / giá trị không? Có trừ luỹ kế và chặn khi vượt không? | Phòng Mua hàng | AS-30, US-22 |
| OQ-27 | Nhiều hợp đồng hoặc nhiều dòng Price List cùng vật tư thì chọn theo tiêu chí nào? | Phòng Mua hàng | AS-31, US-21 |
| OQ-28 | Người tạo được sửa NCC và đơn giá hệ thống tự điền không? Không có cả hợp đồng lẫn Price List thì xử lý thế nào? | Phòng Mua hàng | AS-32, US-21 |
| OQ-29 | Báo giá NCC có tham gia tự tra giá không? Ai nhập báo giá, có cần duyệt không? | Phòng Mua hàng | AS-33, US-20, US-23 |
| OQ-30 | Người tạo không có Trưởng nhóm thì xử lý thế nào? BOD cần một hay tất cả thành viên duyệt? Có phân ngưỡng giá trị không? | Ban giám đốc | AS-34, US-24 |
| OQ-31 | Có cần "Ngày cần hàng" và "Lý do mua" trên đầu phiếu không? | Khách hàng | AS-35 |
| OQ-32 | Tạo YCMH từ Hợp đồng / Báo giá: chép mọi dòng hay chọn dòng? Có được thêm vật tư ngoài chứng từ nguồn không? | Phòng Mua hàng | AS-36, US-19, US-20 |
| OQ-33 | **Đã trả lời (khao-sat-lan-3-yeu-cau-bao-gia.md):** đơn mua hàng vẫn duyệt sau khi chọn NCC và tạo ĐNTT; duyệt xong chuyển PO. Người duyệt: AS-39 | Ban giám đốc | AS-37 |
| OQ-34 | Gửi duyệt đơn chỉ cần tạo / gửi ĐNTT, hay phải chờ Kế toán duyệt ĐNTT? | Kế toán / Mua hàng | AS-40 |
| OQ-35 | ĐNTT bị Kế toán từ chối thì đơn mua hàng xử lý thế nào? | Kế toán | AS-41 |
| OQ-36 | Mẫu "Mã phòng ban-PO-XXXX-DD-MM-YYYY": XXXX và ngày lấy từ YCMH hay đếm riêng? 1 YCMH sinh nhiều RFQ thì phân biệt thế nào? PO dịch vụ đánh số ra sao? Mẫu này khác mẫu số YCMH "Mã BP_XXXX_DD_MM_YY" — có thống nhất không? | Kế toán / Mua hàng | AS-42, AS-28 |
| OQ-37 | Nhận nhiều đợt (backorder) thì "Ngày nhận hàng thực tế" lấy ngày nào? | Kho | AS-43 |
| OQ-38 | Mẫu file Excel báo giá do ai cung cấp, gồm cột nào? NCC không dùng mẫu thì xử lý ra sao? Hộp thư nhận báo giá là địa chỉ nào? | Phòng Mua hàng / IT | AS-44, AS-45 |
| OQ-39 | Một RFQ được hỏi giá tối đa bao nhiêu NCC? Có bắt buộc đủ số báo giá tối thiểu trước khi chọn NCC không? | Phòng Mua hàng | US-07, US-09 |
