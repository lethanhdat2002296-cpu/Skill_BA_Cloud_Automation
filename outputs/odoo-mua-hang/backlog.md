# Product Backlog — Quy trình mua hàng trên Odoo

| Thuộc tính | Giá trị |
|---|---|
| Mã dự án | odoo-mua-hang |
| Phiên bản | 0.3 |
| Ngày | 2026-11-07 |
| Nguồn | outputs/odoo-mua-hang/URD.md v0.3; UC.md v0.3; SRS.md v0.3 |
| Thang điểm | Fibonacci 1, 2, 3, 5, 8, 13 — story mốc 3 điểm: US-15 — Duyệt hoặc từ chối đơn mua hàng |

## 1. Quy ước
- Story point đo **độ lớn tương đối** (khối lượng + độ phức tạp + rủi ro), không đo giờ.
- Story > 8 điểm phải tách trước khi đưa vào sprint; 13 điểm chỉ chấp nhận tạm ở release sau.
- Ưu tiên MoSCoW lấy từ URD; thứ tự trong release theo phụ thuộc rồi ưu tiên.
- Release R1 = mọi story Must (chạy được luồng YCMH → RFQ → chọn NCC → ĐNTT → duyệt → PO → nhập kho); R2 = story Should (AS-49).

## 2. Epic

| Epic | Tên | Mục tiêu (đo được) | User story | Release | Tổng điểm |
|---|---|---|---|---|---|
| EP-01 | Danh mục Hợp đồng và Báo giá NCC | 100% vật tư có hợp đồng còn hiệu lực được tra giá tự động | US-22, US-23 | R1 | 8 |
| EP-02 | Yêu cầu mua hàng và duyệt 3 cấp | 100% đơn mua vật tư Nhập kho có YCMH đã duyệt làm gốc (AS-02) | US-01, US-21, US-19, US-20, US-14, US-05, US-24, US-02 | R1 | 32 |
| EP-03 | Yêu cầu báo giá và chọn nhà cung cấp | 0 RFQ tạo tay; báo giá NCC ghi nhận trên RFQ, so sánh được | US-06, US-27, US-07, US-09, US-26 | R1 | 37 |
| EP-04 | Đơn mua hàng, Đề nghị thanh toán và duyệt | 100% đơn có ĐNTT trước khi duyệt; duyệt xong tự thành PO | US-11, US-10, US-15, US-12, US-16, US-25 | R1 | 26 |
| EP-05 | Nhận hàng nhập kho | Tồn kho cập nhật đúng số thực nhận theo phiếu DO | US-17 | R1 | 2 |
| EP-06 | Theo dõi, huỷ và cấu hình | Người dùng tự theo dõi tiến độ; đổi người duyệt không cần sửa code | US-03, US-04, US-13, US-18 | R2 | 8 |

## 3. Story theo epic

### EP-01 — Danh mục Hợp đồng và Báo giá NCC

#### US-22 — Quản lý danh mục Hợp đồng mua hàng
- **Story:** Là Nhân viên MH, tôi muốn lưu hợp đồng với nhà cung cấp gồm vật tư, đơn giá và thời hạn hiệu lực, để hệ thống dùng giá hợp đồng khi tạo Yêu cầu mua hàng.
- **Epic:** EP-01 · **Ưu tiên:** Must · **Story point:** 3 · **Release:** R1
- **Căn cứ ước lượng:** Blanket Order chuẩn + ràng buộc vật tư Nhập kho, kiểm tra ngày hiệu lực
- **Truy vết:** UC-16, UC-18 · FR-20 · SCR-11
- **Phụ thuộc:** Không có
- **Acceptance criteria:**
  1. **Given** tôi nhập Số hợp đồng, Nhà cung cấp, Hiệu lực từ, Hiệu lực đến và ít nhất một dòng vật tư có đơn giá > 0 **When** tôi bấm "Xác nhận" **Then** hợp đồng chuyển "Đang hiệu lực".
  2. **Given** dòng hợp đồng chọn vật tư loại "Dịch vụ" **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Hợp đồng chỉ áp dụng cho vật tư Nhập kho".
  3. **Given** "Hiệu lực đến" sớm hơn "Hiệu lực từ" **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Ngày kết thúc phải sau ngày bắt đầu".

#### US-23 — Quản lý danh mục Báo giá NCC
- **Story:** Là Nhân viên MH, tôi muốn lưu báo giá nhà cung cấp gửi về gồm vật tư, đơn giá và hạn hiệu lực, để người đề xuất tạo Yêu cầu mua hàng từ báo giá đó.
- **Epic:** EP-01 · **Ưu tiên:** Must · **Story point:** 5 · **Release:** R1
- **Căn cứ ước lượng:** Model + form mới Báo giá NCC, tệp bắt buộc, tác vụ hết hiệu lực hằng ngày (UC-18)
- **Truy vết:** UC-17, UC-18 · FR-21 · SCR-12
- **Phụ thuộc:** Không có
- **Acceptance criteria:**
  1. **Given** tôi nhập Số báo giá, Nhà cung cấp, Ngày báo giá, Hiệu lực đến, ít nhất một dòng vật tư có đơn giá > 0 và đính kèm file báo giá **When** tôi bấm "Xác nhận" **Then** báo giá chuyển "Còn hiệu lực".
  2. **Given** ngày hiện tại sau "Hiệu lực đến" **When** hệ thống chạy kiểm tra hằng ngày **Then** báo giá chuyển "Hết hiệu lực".

### EP-02 — Yêu cầu mua hàng và duyệt 3 cấp

#### US-01 — Tạo và gửi Yêu cầu mua hàng
- **Story:** Là Người đề xuất, tôi muốn tạo phiếu Yêu cầu mua hàng trực tiếp tại menu "Yêu cầu mua hàng" gồm nhiều vật tư Nhập kho và gửi duyệt, để bộ phận Mua hàng mua đúng hàng tôi cần.
- **Epic:** EP-02 · **Ưu tiên:** Must · **Story point:** 8 · **Release:** R1
- **Căn cứ ước lượng:** Tuỳ biến approval.request: số phiếu theo bộ phận, dòng có kho nhận, 2 quy tắc kiểm tra, lọc vật tư Nhập kho
- **Truy vết:** UC-01 · FR-01, FR-19 · SCR-01, SCR-02, SCR-04
- **Phụ thuộc:** Không có
- **Acceptance criteria:**
  1. **Given** tôi thuộc bộ phận Hành chính (mã HC) **When** tôi lưu phiếu mới ngày 20/10/2026 **Then** phiếu nhận số `HC_0012_20_10_26` (AS-28), Người tạo, Bộ phận, Ngày tạo tự điền theo tôi.
  2. **Given** phiếu có ít nhất một dòng đủ Vật tư, Đơn vị tính, Nhập kho, Số lượng **When** tôi bấm "Gửi duyệt" **Then** phiếu chuyển "Chờ duyệt" và Trưởng nhóm của tôi nhận activity duyệt.
  3. **Given** tôi tìm vật tư trên dòng **When** danh sách vật tư hiện ra **Then** danh sách chỉ có vật tư loại "Nhập kho", không có vật tư "Dịch vụ".
  4. **Given** hai dòng cùng vật tư và cùng nhà cung cấp **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Trùng vật tư và nhà cung cấp với dòng <số dòng>".
  5. **Given** một dòng để trống số lượng **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Không được để trống số lượng".

#### US-21 — Tự điền nhà cung cấp và đơn giá
- **Story:** Là Người đề xuất, tôi muốn hệ thống tự điền nhà cung cấp và đơn giá khi tôi chọn vật tư, để không phải tra hợp đồng hay bảng giá.
- **Epic:** EP-02 · **Ưu tiên:** Must · **Story point:** 5 · **Release:** R1
- **Căn cứ ước lượng:** Tra giá 2 nguồn (Hợp đồng → Price List), khoá / mở ô giá, nguồn giá
- **Truy vết:** UC-01, UC-02 · FR-24 · SCR-02
- **Phụ thuộc:** US-22
- **Acceptance criteria:**
  1. **Given** vật tư "Giấy A4 Double A 80gsm" có hợp đồng HĐ-HH-2026-01 còn hiệu lực, giá 78.000₫ **When** tôi chọn vật tư trên YCMH tạo trực tiếp **Then** dòng tự điền nhà cung cấp Hồng Hà, đơn giá 78.000₫, nguồn giá "Hợp đồng HĐ-HH-2026-01".
  2. **Given** vật tư "Bút bi Thiên Long TL-027" không có hợp đồng còn hiệu lực nhưng có Price List Hồng Hà 4.500₫ **When** tôi chọn vật tư **Then** dòng tự điền Hồng Hà, 4.500₫, nguồn giá "Price List".
  3. **Given** vật tư không có hợp đồng và không có Price List **When** tôi chọn vật tư **Then** nhà cung cấp và đơn giá để trống, nguồn giá "Không có", tôi chọn nhà cung cấp bằng tay.

#### US-19 — Tạo Yêu cầu mua hàng từ Hợp đồng
- **Story:** Là Người đề xuất, tôi muốn tạo Yêu cầu mua hàng ngay từ một Hợp đồng còn hiệu lực, để dùng sẵn nhà cung cấp và đơn giá đã ký.
- **Epic:** EP-02 · **Ưu tiên:** Must · **Story point:** 3 · **Release:** R1
- **Căn cứ ước lượng:** Nút trên hợp đồng, chép dòng, khoá giá
- **Truy vết:** UC-01 · FR-22 · SCR-02, SCR-11
- **Phụ thuộc:** US-01, US-22
- **Acceptance criteria:**
  1. **Given** Hợp đồng HĐ-HH-2026-01 "Đang hiệu lực" **When** tôi bấm "Tạo yêu cầu mua hàng" trên hợp đồng **Then** hệ thống mở YCMH mới có Nguồn tạo = HĐ-HH-2026-01, chép mọi dòng vật tư với nhà cung cấp, đơn giá của hợp đồng và số lượng để trống.
  2. **Given** dòng được chép từ hợp đồng **When** tôi sửa đơn giá **Then** ô đơn giá bị khoá.
  3. **Given** hợp đồng đã hết hiệu lực **When** tôi mở hợp đồng **Then** nút "Tạo yêu cầu mua hàng" không hiển thị.

#### US-20 — Tạo Yêu cầu mua hàng từ Báo giá NCC
- **Story:** Là Người đề xuất, tôi muốn tạo Yêu cầu mua hàng từ một Báo giá NCC còn hiệu lực, để dùng sẵn vật tư và giá nhà cung cấp đã báo.
- **Epic:** EP-02 · **Ưu tiên:** Must · **Story point:** 2 · **Release:** R1
- **Căn cứ ước lượng:** Như US-19, dùng lại logic chép dòng
- **Truy vết:** UC-01 · FR-23 · SCR-02, SCR-12
- **Phụ thuộc:** US-19, US-23
- **Acceptance criteria:**
  1. **Given** Báo giá NCC BG-PV-1510 còn hiệu lực **When** tôi bấm "Tạo yêu cầu mua hàng" **Then** YCMH mới có Nguồn tạo = BG-PV-1510, chép mọi dòng với nhà cung cấp và đơn giá của báo giá, số lượng để trống.
  2. **Given** báo giá quá ngày "Hiệu lực đến" **When** tôi mở báo giá **Then** nút "Tạo yêu cầu mua hàng" không hiển thị.

#### US-14 — Duyệt cấp 1 Yêu cầu mua hàng
- **Story:** Là Trưởng nhóm, tôi muốn duyệt hoặc từ chối Yêu cầu mua hàng do thành viên nhóm tạo, để kiểm soát nhu cầu mua của nhóm.
- **Epic:** EP-02 · **Ưu tiên:** Must · **Story point:** 5 · **Release:** R1
- **Căn cứ ước lượng:** Dựng chuỗi duyệt 3 cấp, cấp 1 theo Manager của người tạo
- **Truy vết:** UC-03 · FR-02, FR-03, FR-16 · SCR-02
- **Phụ thuộc:** US-01
- **Acceptance criteria:**
  1. **Given** phiếu "Chờ duyệt" do thành viên nhóm tôi tạo **When** tôi bấm "Duyệt" **Then** phiếu chuyển sang chờ Nhân viên MH duyệt (cấp 2).
  2. **Given** phiếu do người không thuộc nhóm tôi tạo **When** tôi mở phiếu **Then** nút "Duyệt" không hiển thị với tôi.
  3. **Given** tôi bấm "Từ chối" và nhập lý do **When** tôi xác nhận **Then** phiếu về "Nháp" và Người đề xuất nhận email kèm lý do (AS-09).

#### US-05 — Duyệt cấp 2 Yêu cầu mua hàng
- **Story:** Là Nhân viên MH, tôi muốn kiểm tra và duyệt hoặc từ chối Yêu cầu mua hàng sau khi Trưởng nhóm duyệt, để chỉ những nhu cầu hợp lệ đi tiếp tới BOD.
- **Epic:** EP-02 · **Ưu tiên:** Must · **Story point:** 3 · **Release:** R1
- **Căn cứ ước lượng:** Cấp 2 nhóm MH + kiểm tra mọi dòng có NCC
- **Truy vết:** UC-03 · FR-02, FR-03, FR-16 · SCR-02
- **Phụ thuộc:** US-14
- **Acceptance criteria:**
  1. **Given** phiếu đã được Trưởng nhóm duyệt **When** tôi bấm "Duyệt" **Then** phiếu chuyển sang chờ BOD duyệt và BOD nhận activity duyệt.
  2. **Given** phiếu có dòng chưa có nhà cung cấp **When** tôi bấm "Duyệt" **Then** hệ thống chặn và báo tên vật tư thiếu nhà cung cấp (AS-32).
  3. **Given** tôi bấm "Từ chối" **When** tôi để trống lý do **Then** hệ thống không cho xác nhận và báo "Vui lòng nhập lý do từ chối".
  4. **Given** Trưởng nhóm chưa duyệt **When** tôi mở phiếu **Then** nút "Duyệt" không hiển thị với tôi.

#### US-24 — Duyệt cấp 3 Yêu cầu mua hàng
- **Story:** Là thành viên BOD, tôi muốn duyệt cuối Yêu cầu mua hàng đã qua Trưởng nhóm và MH, để chỉ những nhu cầu được ban giám đốc đồng ý mới sinh RFQ.
- **Epic:** EP-02 · **Ưu tiên:** Must · **Story point:** 3 · **Release:** R1
- **Căn cứ ước lượng:** Cấp 3 nhóm BOD, một thành viên duyệt là đủ, kích hoạt tạo RFQ
- **Truy vết:** UC-03 · FR-02, FR-03, FR-16 · SCR-02
- **Phụ thuộc:** US-05
- **Acceptance criteria:**
  1. **Given** phiếu đã được Nhân viên MH duyệt **When** một thành viên BOD bấm "Duyệt" **Then** phiếu chuyển "Đã duyệt" và hệ thống tạo RFQ theo US-06.
  2. **Given** phiếu chưa được MH duyệt **When** thành viên BOD mở phiếu **Then** nút "Duyệt" không hiển thị.
  3. **Given** thành viên BOD bấm "Từ chối" và nhập lý do **When** xác nhận **Then** phiếu về "Nháp" và Người đề xuất nhận email kèm lý do (AS-09).

#### US-02 — Sửa và gửi lại yêu cầu bị từ chối
- **Story:** Là Người đề xuất, tôi muốn yêu cầu bị từ chối tự về Nháp và tôi nhận email nêu lý do, để sửa và gửi lại ngay mà không phải tạo phiếu mới.
- **Epic:** EP-02 · **Ưu tiên:** Must · **Story point:** 3 · **Release:** R1
- **Căn cứ ước lượng:** Từ chối về Nháp, đặt lại cấp duyệt, mẫu email, hiện lý do đầu phiếu
- **Truy vết:** UC-01 · FR-03 · SCR-02
- **Phụ thuộc:** US-14
- **Acceptance criteria:**
  1. **Given** phiếu của tôi bị từ chối ở cấp bất kỳ **When** người duyệt xác nhận từ chối **Then** phiếu về "Nháp" và tôi nhận email nêu người từ chối, cấp duyệt và lý do.
  2. **Given** phiếu bị từ chối đã về "Nháp" **When** tôi mở phiếu **Then** đầu phiếu hiện thông báo lý do từ chối gần nhất và chatter còn lịch sử từ chối.
  3. **Given** tôi sửa dòng và bấm "Gửi duyệt" **When** hệ thống ghi nhận **Then** phiếu chuyển "Chờ duyệt" từ cấp 1.

### EP-03 — Yêu cầu báo giá và chọn nhà cung cấp

#### US-06 — Nhận RFQ tự động gộp theo vendor
- **Story:** Là Nhân viên MH, tôi muốn hệ thống tự tạo RFQ ngay khi yêu cầu được duyệt xong, gộp các sản phẩm cùng vendor vào một phiếu, để không phải lập RFQ thủ công.
- **Epic:** EP-03 · **Ưu tiên:** Must · **Story point:** 5 · **Release:** R1
- **Căn cứ ước lượng:** Nhóm dòng theo NCC, tạo N RFQ, kế thừa đầu phiếu, chống tạo trùng
- **Truy vết:** UC-05 · FR-05 · Không có UI
- **Phụ thuộc:** US-24
- **Acceptance criteria:**
  1. **Given** yêu cầu có 3 dòng: 2 dòng vendor A, 1 dòng vendor B **When** cấp duyệt cuối bấm "Duyệt" **Then** hệ thống tạo đúng 2 RFQ trạng thái "Nháp": RFQ vendor A có 2 dòng, RFQ vendor B có 1 dòng.
  2. **Given** RFQ được tạo tự động **When** tôi mở RFQ **Then** trường "Yêu cầu mua hàng" trỏ về phiếu gốc và mỗi dòng giữ số lượng, đơn vị tính, ngày cần hàng của dòng yêu cầu.
  3. **Given** yêu cầu đã sinh RFQ **When** có người bấm "Duyệt" lại trên cùng phiếu **Then** hệ thống không tạo thêm RFQ trùng.

#### US-27 — Biết RFQ được tạo từ Yêu cầu mua hàng nào
- **Story:** Là Nhân viên MH, tôi muốn RFQ ghi rõ mã Yêu cầu mua hàng gốc và tìm được RFQ theo mã đó, để truy vết đơn mua về nhu cầu ban đầu.
- **Epic:** EP-03 · **Ưu tiên:** Must · **Story point:** 3 · **Release:** R1
- **Căn cứ ước lượng:** Sequence theo YCMH + hậu tố NN, trường hiển thị + trường ẩn, tìm kiếm
- **Truy vết:** UC-05, UC-08 · FR-27 · SCR-03, SCR-04
- **Phụ thuộc:** US-06
- **Acceptance criteria:**
  1. **Given** YCMH HC_0012_20_10_26 sinh 2 RFQ **When** tôi mở mỗi RFQ **Then** trường "Mã Yêu cầu mua hàng" hiện HC_0012_20_10_26 và bấm vào mở được YCMH gốc.
  2. **Given** tôi gõ "HC_0012" ở ô tìm kiếm danh sách RFQ **When** tìm **Then** danh sách hiện đúng 2 RFQ của YCMH đó.
  3. **Given** YCMH gốc đã bị huỷ **When** tôi tìm theo mã YCMH **Then** vẫn tìm được RFQ nhờ mã lưu ngầm.

#### US-07 — Gửi email xin báo giá tới nhiều nhà cung cấp
- **Story:** Là Nhân viên MH, tôi muốn bấm "Send email" trên RFQ, chọn nhiều nhà cung cấp và soạn một email, để hệ thống gửi riêng cho từng nhà cung cấp xin báo giá.
- **Epic:** EP-03 · **Ưu tiên:** Must · **Story point:** 8 · **Release:** R1
- **Căn cứ ước lượng:** Wizard gửi nhiều NCC, tách email, reply-to alias, đính kèm PDF + Excel mẫu
- **Truy vết:** UC-06 · FR-06 · SCR-04, SCR-05
- **Phụ thuộc:** US-06 (mẫu email, mẫu Excel nạp sẵn — AS-49)
- **Acceptance criteria:**
  1. **Given** RFQ "Nháp" **When** tôi bấm "Send email" **Then** popup mở với ô "Gửi đến" điền sẵn NCC của RFQ, tiêu đề, nội dung có bảng sản phẩm của phiếu, đính kèm PDF RFQ và file Excel mẫu báo giá.
  2. **Given** tôi nhập 3 NCC ngăn cách bằng ";" **When** bấm "Gửi" **Then** hệ thống gửi 3 email riêng, mỗi email chỉ có 1 người nhận, và RFQ chuyển "RFQ".
  3. **Given** một NCC chưa có email **When** bấm "Gửi" **Then** hệ thống chặn, báo tên NCC và không gửi email nào.

#### US-09 — So sánh giá và chọn nhà cung cấp
- **Story:** Là Nhân viên MH, tôi muốn bấm "So sánh giá" để xem báo giá của các NCC cạnh nhau và chọn 1 NCC cho cả phiếu, để chọn giá tốt nhất mà không phải tạo nhiều RFQ.
- **Epic:** EP-03 · **Ưu tiên:** Must · **Story point:** 8 · **Release:** R1
- **Căn cứ ước lượng:** Màn so sánh vật tư × NCC, đánh dấu giá thấp nhất, chọn NCC cập nhật giá cả phiếu
- **Truy vết:** UC-08 · FR-08 · SCR-04, SCR-06
- **Phụ thuộc:** US-26.1
- **Acceptance criteria:**
  1. **Given** RFQ đã có báo giá của 2 NCC **When** tôi bấm "So sánh giá" **Then** màn hình hiện mỗi vật tư một hàng, mỗi NCC một cột với đơn giá, thành tiền, tổng, và đánh dấu giá thấp nhất từng dòng, tổng thấp nhất.
  2. **Given** tôi bấm "Chọn NCC này" ở cột Công ty CP Thế Giới Di Động **When** xác nhận **Then** RFQ đổi NCC sang Thế Giới Di Động, đơn giá các dòng lấy theo báo giá của NCC này.
  3. **Given** báo giá của một NCC thiếu giá cho một vật tư **When** tôi bấm "Chọn NCC này" ở cột đó **Then** hệ thống chặn và báo vật tư thiếu giá.

#### US-26 — Tự đọc file Excel báo giá từ email NCC
- **Story:** Là Nhân viên MH, tôi muốn hệ thống tự lưu email NCC trả lời và đọc file Excel báo giá đính kèm, để không phải gõ lại giá từng NCC.
- **Epic:** EP-03 · **Ưu tiên:** Must · **Release:** R1
- **Đã tách thành:** US-26.1, US-26.2
- **Lý do tách:** ước lượng 13 điểm (> 8) — nhận email, nhập tay và đọc file có thể giao riêng.

#### US-26.1 — Nhận email NCC trả lời và nhập tay báo giá
- **Story:** Là Nhân viên MH, tôi muốn email NCC trả lời tự gắn vào RFQ và tôi nhập được báo giá bằng tay, để có báo giá trên RFQ kể cả khi NCC không dùng file mẫu.
- **Tách từ:** US-26 — Cách nhập dữ liệu / giao diện — nhập tay trước, đọc file sau
- **Epic:** EP-03 · **Ưu tiên:** Must · **Story point:** 5 · **Release:** R1
- **Căn cứ ước lượng:** Incoming mail + alias, ghép thread, xác định NCC theo người gửi, form nhập tay Báo giá NCC gắn RFQ
- **Truy vết:** UC-07 · FR-21, FR-26 · SCR-04, SCR-06, SCR-12
- **Phụ thuộc:** US-07, US-23
- **Acceptance criteria:**
  1. **Given** NCC Phong Vũ trả lời email RFQ HC-PO-0012-20-10-2026-02 **When** Odoo nhận email **Then** chatter RFQ có email trả lời và tệp đính kèm.
  2. **Given** email trả lời từ địa chỉ không thuộc NCC đã được hỏi giá **When** Odoo nhận email **Then** chatter ghi "Không xác định được NCC" và không tạo báo giá.
  3. **Given** RFQ có NCC Minh Khoa đã được hỏi giá **When** tôi nhập tay báo giá Minh Khoa với giá 2 vật tư và lưu **Then** RFQ có Báo giá NCC mới của Minh Khoa, nguồn "Nhập tay".

#### US-26.2 — Tự đọc file Excel báo giá thành Báo giá NCC
- **Story:** Là Nhân viên MH, tôi muốn hệ thống tự đọc file Excel báo giá NCC gửi kèm email, để không phải gõ lại giá từng NCC.
- **Tách từ:** US-26 — Biến thể quy tắc / nỗ lực lớn — phần đọc file và xử lý lỗi tách riêng
- **Epic:** EP-03 · **Ưu tiên:** Must · **Story point:** 8 · **Release:** R1
- **Căn cứ ước lượng:** Đọc .xlsx theo mẫu, ghép Mã vật tư, 4 loại lỗi file, giới hạn dung lượng, báo giá cũ "Đã thay thế"
- **Truy vết:** UC-07 · FR-21, FR-26 · SCR-04, SCR-06, SCR-12
- **Phụ thuộc:** US-26.1
- **Acceptance criteria:**
  1. **Given** Phong Vũ trả lời kèm `BaoGia_PhongVu.xlsx` đúng mẫu 2 dòng **When** Odoo nhận email **Then** RFQ có Báo giá NCC mới: Mực in HP 107A 765.000₫, Máy in HP LaserJet M211dw 6.990.000₫.
  2. **Given** file `BaoGia_TGDD.xlsx` thiếu cột "Đơn giá" **When** Odoo nhận email **Then** chatter ghi "Không đọc được BaoGia_TGDD.xlsx: thiếu cột Đơn giá" và không có báo giá mới.
  3. **Given** Phong Vũ gửi báo giá lần 2 **When** đọc xong **Then** báo giá lần 1 của Phong Vũ chuyển "Đã thay thế".
  4. **Given** file 6 MB **When** Odoo nhận email **Then** chatter ghi file vượt 5 MB và không đọc (NFR-10).

### EP-04 — Đơn mua hàng, Đề nghị thanh toán và duyệt

#### US-11 — Tạo Đề nghị thanh toán trước khi gửi duyệt
- **Story:** Là Nhân viên MH, tôi muốn tạo Đề nghị thanh toán ngay sau khi chọn NCC, để đơn đủ điều kiện gửi duyệt và Kế toán chuẩn bị thanh toán.
- **Epic:** EP-04 · **Ưu tiên:** Must · **Story point:** 8 · **Release:** R1
- **Căn cứ ước lượng:** Model + form ĐNTT mới, quy tắc số tiền / tài khoản, activity Kế toán
- **Truy vết:** UC-09 · FR-11 · SCR-04, SCR-08
- **Phụ thuộc:** US-09
- **Acceptance criteria:**
  1. **Given** RFQ trạng thái "RFQ" đã chọn NCC **When** tôi bấm "Tạo đề nghị thanh toán" **Then** hệ thống mở phiếu ĐNTT điền sẵn NCC, mã RFQ, số tiền = tổng đơn.
  2. **Given** phiếu ĐNTT hợp lệ **When** tôi bấm "Gửi kế toán" **Then** ĐNTT chuyển "Chờ kế toán duyệt", RFQ giữ trạng thái "RFQ" và nút "Approve" được mở.
  3. **Given** số tiền đề nghị lớn hơn tổng đơn **When** tôi bấm "Gửi kế toán" **Then** hệ thống chặn và báo "Số tiền đề nghị vượt tổng giá trị đơn mua hàng".

#### US-10 — Gửi duyệt đơn mua hàng
- **Story:** Là Nhân viên MH, tôi muốn bấm "Approve" sau khi chọn NCC và tạo Đề nghị thanh toán, để đơn vào quy trình duyệt.
- **Epic:** EP-04 · **Ưu tiên:** Must · **Story point:** 2 · **Release:** R1
- **Căn cứ ước lượng:** Nút Approve + 3 điều kiện kiểm tra
- **Truy vết:** UC-10 · FR-09 · SCR-04
- **Phụ thuộc:** US-11
- **Acceptance criteria:**
  1. **Given** RFQ trạng thái "RFQ", mọi dòng có giá và có ĐNTT "Chờ kế toán duyệt" **When** tôi bấm "Approve" **Then** đơn chuyển "Chờ duyệt" và Trưởng phòng Mua hàng nhận activity duyệt.
  2. **Given** đơn chưa có ĐNTT **When** tôi bấm "Approve" **Then** hệ thống chặn và báo "Phải tạo Đề nghị thanh toán trước khi gửi duyệt".
  3. **Given** RFQ có dòng số lượng > 0 nhưng đơn giá = 0 **When** tôi bấm "Approve" **Then** hệ thống chặn và báo "Chưa nhập đơn giá cho sản phẩm <tên>".

#### US-15 — Duyệt hoặc từ chối đơn mua hàng
- **Story:** Là Trưởng phòng Mua hàng, tôi muốn duyệt đơn sau khi MH chọn NCC và tạo ĐNTT, để kiểm soát mua hàng.
- **Epic:** EP-04 · **Ưu tiên:** Must · **Story point:** 3 · **Release:** R1
- **Căn cứ ước lượng:** Duyệt 1 cấp, từ chối về RFQ / Nháp kèm email
- **Truy vết:** UC-11 · FR-10, FR-16 · SCR-03, SCR-04
- **Phụ thuộc:** US-10
- **Acceptance criteria:**
  1. **Given** đơn "Chờ duyệt" tổng 69.927.000₫ **When** tôi bấm "Duyệt" **Then** đơn chuyển "PO" (US-12).
  2. **Given** đơn "Chờ duyệt" tổng 120.000.000₫ **When** tôi bấm "Duyệt" **Then** đơn chuyển "PO", không cần thêm cấp duyệt nào.
  3. **Given** tôi bấm "Từ chối" và nhập lý do **When** tôi xác nhận **Then** đơn vật tư Nhập kho về "RFQ" (đơn dịch vụ về "Nháp") và Nhân viên MH nhận email kèm lý do.

#### US-12 — Đơn duyệt xong tự chuyển PO và tạo phiếu DO
- **Story:** Là Nhân viên MH, tôi muốn đơn được duyệt xong tự chuyển PO và tạo phiếu DO cho kho, để không phải thao tác thêm bước nhận hàng.
- **Epic:** EP-04 · **Ưu tiên:** Must · **Story point:** 5 · **Release:** R1
- **Căn cứ ước lượng:** button_confirm + tách phiếu DO theo kho nhận + Ngày nhận hàng thực tế
- **Truy vết:** UC-11 · FR-13 · SCR-04, SCR-09
- **Phụ thuộc:** US-15
- **Acceptance criteria:**
  1. **Given** đơn vật tư Nhập kho "Chờ duyệt" **When** Trưởng phòng Mua hàng bấm "Duyệt" **Then** đơn chuyển "PO" và hệ thống tạo phiếu DO trạng thái "Sẵn sàng" cho mỗi kho nhận.
  2. **Given** đơn đã "PO" **When** tôi mở đơn **Then** không có nút "Xác nhận đã nhận hàng" và smart button "Phiếu DO" hiện số phiếu.
  3. **Given** Thủ kho hoàn tất phiếu DO ngày 29/10/2026 **When** tôi mở đơn **Then** "Ngày nhận hàng thực tế" hiện 29/10/2026.

#### US-16 — Xử lý Đề nghị thanh toán
- **Story:** Là Kế toán, tôi muốn duyệt hoặc từ chối Đề nghị thanh toán và ghi nhận thanh toán, để trả tiền vendor đúng đơn đã duyệt.
- **Epic:** EP-04 · **Ưu tiên:** Must · **Story point:** 5 · **Release:** R1
- **Căn cứ ước lượng:** Duyệt / từ chối ĐNTT, ghi nhận thanh toán outbound, xử lý đơn khi bị từ chối
- **Truy vết:** UC-12 · FR-12, FR-16 · SCR-07, SCR-08
- **Phụ thuộc:** US-11
- **Acceptance criteria:**
  1. **Given** Đề nghị thanh toán "Chờ kế toán duyệt" **When** tôi bấm "Duyệt" **Then** phiếu chuyển "Đã duyệt".
  2. **Given** phiếu "Đã duyệt" **When** tôi bấm "Ghi nhận thanh toán", chọn sổ nhật ký và ngày thanh toán, xác nhận **Then** hệ thống tạo bút toán thanh toán cho vendor và phiếu chuyển "Đã thanh toán".
  3. **Given** tôi bấm "Từ chối" và nhập lý do **When** tôi xác nhận **Then** phiếu chuyển "Từ chối", đơn đang "Chờ duyệt" về "RFQ" (đơn dịch vụ về "Nháp") và Nhân viên MH nhận email kèm lý do (AS-41).

#### US-25 — Mua Dịch vụ bằng PO trực tiếp
- **Story:** Là Nhân viên MH, tôi muốn tạo thẳng PO cho vật tư Dịch vụ, không cần Yêu cầu mua hàng và Yêu cầu báo giá, để mua dịch vụ nhanh nhưng vẫn có ĐNTT và duyệt đơn.
- **Epic:** EP-04 · **Ưu tiên:** Must · **Story point:** 3 · **Release:** R1
- **Căn cứ ước lượng:** PO dịch vụ: chặn vật tư Nhập kho, số phiếu riêng, statusbar không có bước RFQ
- **Truy vết:** UC-13 · FR-13, FR-19, FR-25 · SCR-02, SCR-03, SCR-04, SCR-09
- **Phụ thuộc:** US-10, US-11
- **Acceptance criteria:**
  1. **Given** tôi bấm "Mới" ở danh sách đơn mua và chọn vật tư Dịch vụ **When** tôi lưu **Then** PO dịch vụ "Nháp" được tạo với số `MH-PO-<XXXX>-<DD>-<MM>-<YYYY>`, không có trường Yêu cầu mua hàng và không có nút "Send email".
  2. **Given** PO dịch vụ chưa có ĐNTT **When** tôi bấm "Approve" **Then** hệ thống chặn và báo "Phải tạo Đề nghị thanh toán trước khi gửi duyệt".
  3. **Given** PO dịch vụ "Chờ duyệt" **When** Trưởng phòng Mua hàng bấm "Duyệt" **Then** đơn chuyển "PO" và không có phiếu DO nào được tạo.
  4. **Given** đơn tạo trực tiếp có vật tư "Nhập kho" **When** tôi bấm "Lưu" **Then** hệ thống chặn và báo "Vật tư Nhập kho phải mua qua Yêu cầu mua hàng".

### EP-05 — Nhận hàng nhập kho

#### US-17 — Nhập kho theo phiếu DO
- **Story:** Là Thủ kho, tôi muốn kiểm đếm hàng theo phiếu DO và xác nhận, để tồn kho cập nhật đúng số thực nhận.
- **Epic:** EP-05 · **Ưu tiên:** Must · **Story point:** 2 · **Release:** R1
- **Căn cứ ước lượng:** Phiếu nhập kho chuẩn Odoo + cập nhật ngày thực tế của đơn
- **Truy vết:** UC-15 · FR-14 · SCR-09
- **Phụ thuộc:** US-12
- **Acceptance criteria:**
  1. **Given** phiếu DO "Sẵn sàng" **When** tôi nhập số lượng thực nhận bằng số lượng yêu cầu và bấm "Xác nhận" **Then** phiếu chuyển "Hoàn tất" và tồn kho tăng đúng số lượng.
  2. **Given** số lượng thực nhận nhỏ hơn số lượng yêu cầu **When** tôi bấm "Xác nhận" và chọn "Tạo backorder" **Then** hệ thống hoàn tất phần đã nhận và tạo phiếu DO mới cho phần còn thiếu.

### EP-06 — Theo dõi, huỷ và cấu hình

#### US-03 — Theo dõi yêu cầu và chứng từ liên quan
- **Story:** Là Người đề xuất, tôi muốn xem trạng thái yêu cầu và các RFQ, đơn mua hàng, phiếu DO sinh ra từ nó, để biết khi nào có hàng.
- **Epic:** EP-06 · **Ưu tiên:** Should · **Story point:** 2 · **Release:** R2
- **Căn cứ ước lượng:** Smart button và bộ lọc có sẵn
- **Truy vết:** UC-04 · FR-17 · SCR-01, SCR-02, SCR-03, SCR-04, SCR-11, SCR-12
- **Phụ thuộc:** US-06
- **Acceptance criteria:**
  1. **Given** yêu cầu đã duyệt xong **When** tôi mở phiếu **Then** tôi thấy nút thông minh "RFQ/Đơn mua hàng" kèm số lượng chứng từ và mở được danh sách chứng từ đó.
  2. **Given** tôi mở danh sách Yêu cầu mua hàng **When** tôi dùng bộ lọc mặc định "Của tôi" **Then** danh sách chỉ hiện các phiếu tôi tạo.

#### US-04 — Huỷ yêu cầu chưa duyệt xong
- **Story:** Là Người đề xuất, tôi muốn huỷ yêu cầu khi không còn nhu cầu, để Mua hàng không xử lý thừa.
- **Epic:** EP-06 · **Ưu tiên:** Should · **Story point:** 1 · **Release:** R2
- **Căn cứ ước lượng:** Nút huỷ theo trạng thái, xoá activity
- **Truy vết:** UC-04 · FR-04 · SCR-02
- **Phụ thuộc:** US-01
- **Acceptance criteria:**
  1. **Given** phiếu ở trạng thái "Nháp" hoặc "Chờ duyệt" **When** tôi bấm "Huỷ" **Then** phiếu chuyển "Đã huỷ" và các activity duyệt đang mở bị xoá.
  2. **Given** phiếu đã "Đã duyệt" **When** tôi mở phiếu **Then** nút "Huỷ" không hiển thị.

#### US-13 — Huỷ RFQ hoặc đơn mua hàng
- **Story:** Là Nhân viên MH, tôi muốn huỷ RFQ hoặc đơn mua hàng không còn dùng, để danh sách chỉ còn chứng từ đang xử lý.
- **Epic:** EP-06 · **Ưu tiên:** Should · **Story point:** 2 · **Release:** R2
- **Căn cứ ước lượng:** Huỷ đơn kèm lý do, chặn khi đã thanh toán, huỷ ĐNTT theo
- **Truy vết:** UC-14 · FR-15 · SCR-04
- **Phụ thuộc:** US-11
- **Acceptance criteria:**
  1. **Given** đơn ở trạng thái trước `PO` **When** tôi bấm "Huỷ" và nhập lý do **Then** đơn chuyển "Đã huỷ" và lý do ghi trên chatter.
  2. **Given** đơn có Đề nghị thanh toán ở trạng thái "Đã thanh toán" **When** tôi bấm "Huỷ" **Then** hệ thống chặn và báo "Đơn đã được thanh toán, liên hệ Kế toán để xử lý".

#### US-18 — Cấu hình người duyệt, mẫu email và mẫu báo giá
- **Story:** Là Quản trị hệ thống, tôi muốn cấu hình người duyệt đơn mua hàng, mẫu email và mẫu file Excel báo giá, để thay đổi chính sách mà không cần sửa code.
- **Epic:** EP-06 · **Ưu tiên:** Should · **Story point:** 3 · **Release:** R2
- **Căn cứ ước lượng:** Trang Settings: người duyệt, mẫu email, mẫu Excel có kiểm tra cột, hộp thư
- **Truy vết:** UC-19 · FR-18 · SCR-10
- **Phụ thuộc:** Không có
- **Acceptance criteria:**
  1. **Given** tôi thuộc nhóm Quản trị **When** tôi đổi người duyệt đơn mua hàng và lưu **Then** các đơn gửi duyệt sau thời điểm lưu giao activity cho người duyệt mới.
  2. **Given** tôi tải lên mẫu Excel báo giá mới **When** MH gửi email RFQ sau đó **Then** email đính kèm mẫu mới.
  3. **Given** người dùng không thuộc nhóm Quản trị **When** họ mở menu cấu hình mua hàng **Then** menu không hiển thị.

## 4. Kế hoạch phát hành

| Release | Mục tiêu | Epic | Story | Tổng điểm |
|---|---|---|---|---|
| R1 (MVP) | Chạy được luồng YCMH → RFQ → so sánh, chọn NCC → ĐNTT → duyệt → PO → nhập kho; mua dịch vụ bằng PO | EP-01 → EP-05 | 23 | 105 |
| R2 | Theo dõi, huỷ chứng từ, cấu hình người duyệt và mẫu không cần sửa code | EP-06 | 4 | 8 |

Thứ tự gợi ý trong R1 (theo phụ thuộc): EP-01 → US-01, US-14, US-05, US-24 → US-21, US-19, US-20, US-02 → EP-03 → EP-04 → EP-05. Với velocity giả định 20 điểm / sprint 2 tuần (AS-50), R1 cần khoảng 6 sprint.

## 5. Definition of Ready / Definition of Done

**Ready** (đưa vào sprint khi đủ):
- Story theo mẫu Là / tôi muốn / để; có ≥ 2 AC Given/When/Then, có ít nhất 1 AC ngoại lệ.
- Có truy vết FR (và SCR nếu có UI); wireframe màn liên quan đã được khách xem.
- Story point ≤ 8; phụ thuộc đã xong hoặc cùng sprint.
- Không còn OQ chặn story (OQ liên quan đã trả lời hoặc có AS được chấp nhận) — đặc biệt OQ-34, OQ-36, OQ-38 cho EP-03, EP-04.
- Dữ liệu mẫu (NCC, vật tư Nhập kho / Dịch vụ, kho, bộ phận, người duyệt) có trên môi trường test.

**Done:**
- Mọi AC đạt khi kiểm thử trên môi trường test Odoo 17; không còn lỗi mức nghiêm trọng.
- Code review xong; module cài / nâng cấp được trên bản sao dữ liệu thật.
- Quyền truy cập theo nhóm (Người đề xuất, Trưởng nhóm, MH, BOD, Kế toán, Thủ kho) đã kiểm.
- Tài liệu (SRS / hướng dẫn sử dụng) cập nhật nếu hành vi khác đặc tả.
- PO / khách hàng xác nhận demo.

## 6. Assumptions & Open Questions (phát sinh khi lập backlog)

### 6.1 Giả định
| Mã | Giả định | Lý do chọn | Liên quan |
|---|---|---|---|
| AS-49 | Release R1 gồm mọi story Must; story Should (US-03, US-04, US-13, US-18) sang R2; trong R1 người duyệt đơn và mẫu email cấu hình sẵn bằng dữ liệu khởi tạo | Đủ chạy luồng end-to-end sớm nhất; cấu hình có thể làm tay lúc đầu | EP-06, US-18 |
| AS-50 | Velocity đội phát triển 20 điểm / sprint 2 tuần | Chưa có dữ liệu đội; dùng để ước số sprint, không cam kết ngày | Mục 4 |

### 6.2 Câu hỏi mở
| Mã | Câu hỏi | Người cần trả lời | Liên quan |
|---|---|---|---|
| OQ-41 | Có cần go-live theo release (R1 trước, R2 sau) không, hay chờ đủ cả R1 + R2? Mốc go-live mong muốn? | Khách hàng | Mục 4, OQ-03 |
