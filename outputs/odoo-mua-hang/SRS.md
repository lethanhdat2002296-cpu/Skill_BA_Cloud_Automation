# SRS — Quy trình mua hàng trên Odoo

| Thuộc tính | Giá trị |
|---|---|
| Mã dự án | odoo-mua-hang |
| Phiên bản | 0.3 (cập nhật theo trả lời câu hỏi mở lần 1 và khảo sát lần 3 — Yêu cầu báo giá) |
| Ngày | 2026-10-20 |
| Tài liệu liên quan | URD.md, brainstorm.md, ui/flows.md |
| Trạng thái | Chờ review |

**Lịch sử phiên bản**

| Phiên bản | Ngày | Thay đổi | Nguồn | Ảnh hưởng |
|---|---|---|---|---|
| 0.1 | 2026-10-20 | Bản đầu tiên | inputs/odoo-mua-hang/khao-sat-lan-1.md | Toàn bộ |
| 0.2 | 2026-10-20 | Khảo sát lần 2 — phiếu Yêu cầu mua hàng: phân loại vật tư Nhập kho / Dịch vụ; 3 cách tạo YCMH (trực tiếp, từ Hợp đồng, từ Báo giá NCC); số phiếu `Mã BP_XXXX_DD_MM_YY`; đầu phiếu và dòng mới (kho nhận theo dòng); duyệt 3 cấp Trưởng nhóm → MH → BOD; tự điền NCC và giá theo Hợp đồng → Price List; chặn trùng vật tư + NCC; mua dịch vụ bằng RFQ trực tiếp | inputs/odoo-mua-hang/khao-sat-lan-2-yeu-cau-mua-hang.md; inputs/odoo-mua-hang/_changes/20261020-074707.md | Sửa FR-01, FR-02, FR-03, FR-05, FR-13, FR-16, FR-17, NFR-02, SCR-01, SCR-02, SCR-03, SCR-04; thêm FR-19 → FR-25, SCR-11, SCR-12, AS-26 → AS-38, OQ-22 → OQ-33; OQ-04 đã trả lời; SCR-05 chỉ cập nhật nền (số phiếu, cột Nhập kho) |
| 0.3 | 2026-10-20 | Trả lời câu hỏi mở lần 1: Odoo 17 Odoo.sh/on-premise; không gộp YCMH; đơn mua không ngưỡng; YCMH bị từ chối về Nháp + email. Khảo sát lần 3 — Yêu cầu báo giá: Dịch vụ tạo thẳng PO; ĐNTT bắt buộc trước khi duyệt; bỏ Waiting PO, duyệt xong → PO + tự tạo DO; RFQ kế thừa YCMH, thêm ngày dự kiến / thực tế nhận hàng, mã truy vết YCMH; "Send email" gửi riêng từng NCC; tự đọc Excel báo giá từ email reply; so sánh và chọn 1 NCC cho cả phiếu (bỏ RFQ thay thế); quy trình vẽ lại bằng Activity – Swimlane | inputs/odoo-mua-hang/tra-loi-cau-hoi-mo-lan-1.md; inputs/odoo-mua-hang/khao-sat-lan-3-yeu-cau-bao-gia.md; inputs/odoo-mua-hang/_changes/20261020-084051.md; inputs/odoo-mua-hang/_changes/20261020-093008.md | Sửa FR-03, FR-05, FR-06, FR-08 → FR-13, FR-15 → FR-18, FR-21, FR-25, NFR-08, SCR-02 → SCR-10, SCR-12, mục 7; bỏ FR-07; thêm FR-26, FR-27, NFR-10, AS-39 → AS-47, OQ-34 → OQ-39; OQ-01, OQ-06, OQ-11, OQ-16 đã trả lời |

## 1. Giới thiệu

### 1.1 Mục đích
Tài liệu đặc tả yêu cầu phần mềm cho quy trình mua hàng trên Odoo 17 (Purchase, Inventory, Approvals, Accounting), dành cho đội phát triển Odoo, QA và khách hàng. Tài liệu là căn cứ để ước lượng, phát triển module tuỳ biến và nghiệm thu.

### 1.2 Phạm vi
- **Trong phạm vi:**
  - Yêu cầu mua hàng trên Approvals cho vật tư Nhập kho, tạo theo 3 cách (trực tiếp, từ Hợp đồng, từ Báo giá NCC), duyệt 3 cấp (Trưởng nhóm → Nhân viên MH → BOD). *(v0.2)*
  - Phân loại vật tư Nhập kho / Dịch vụ; vật tư Dịch vụ mua bằng RFQ tạo trực tiếp, không qua YCMH, không có phiếu DO. *(v0.2)*
  - Danh mục Hợp đồng mua hàng và danh mục Báo giá NCC; tự điền NCC và đơn giá theo Hợp đồng → Price List. *(v0.2)*
  - Tự tạo RFQ gộp theo vendor khi yêu cầu được duyệt xong.
  - Gửi email RFQ riêng tới N NCC từ một lần soạn ("Send email"); tự lưu email NCC trả lời và đọc file Excel báo giá; so sánh giá và chọn 1 NCC cho cả phiếu. *(v0.3 — bỏ RFQ thay thế)*
  - Gửi duyệt và duyệt đơn mua hàng 1 cấp, không ngưỡng giá trị. *(v0.3)*
  - Đề nghị thanh toán (chứng từ mới) bắt buộc tạo trước khi gửi duyệt đơn; Kế toán duyệt và ghi nhận thanh toán. *(v0.3)*
  - Đơn duyệt xong chuyển `PO` và tự tạo phiếu DO theo kho nhận (vật tư Nhập kho); đơn Dịch vụ không tạo DO. *(v0.3 — bỏ trạng thái `Đã duyệt`, `Waiting PO` và nút "Xác nhận đã nhận hàng")*
  - RFQ/PO đánh số theo mẫu `Mã phòng ban-PO-XXXX-DD-MM-YYYY`, ghi mã Yêu cầu mua hàng gốc và lưu ngầm mã để truy vấn. *(v0.3)*
  - Nhập kho theo phiếu DO, nhận thiếu tạo backorder.
  - Cấu hình người duyệt, mẫu email, mẫu Excel báo giá, hộp thư nhận báo giá. *(v0.3 — bỏ ngưỡng)*
- **Ngoài phạm vi:** hoá đơn nhà cung cấp và đối chiếu 3 bên (AS-15); kiểm soát ngân sách; cổng vendor (AS-16); đa tiền tệ (AS-17); báo cáo phân tích mua hàng.

### 1.3 Thuật ngữ
| Thuật ngữ | Giải thích |
|---|---|
| Yêu cầu mua hàng (YCMH) | Phiếu đề xuất mua do Người đề xuất tạo, model `approval.request` loại Purchases |
| RFQ | Request for Quotation — Yêu cầu báo giá gửi vendor, model `purchase.order` ở trạng thái Nháp / RFQ |
| RFQ thay thế | **[Đã bỏ — v0.3]** RFQ cho vendor khác cùng nhu cầu (Alternatives); thay bằng gửi email riêng tới N NCC trên cùng 1 RFQ |
| Đơn mua hàng | `purchase.order` từ trạng thái Chờ duyệt trở đi |
| PO | Trạng thái đơn mua hàng đã duyệt xong (state `purchase` của Odoo); vật tư Nhập kho có phiếu DO *(sửa v0.3)* |
| Waiting PO | **[Đã bỏ — v0.3]** Trạng thái chờ hàng về sau khi có ĐNTT |
| Đề nghị thanh toán (ĐNTT) | Chứng từ mới yêu cầu Kế toán thanh toán cho vendor theo một đơn mua hàng |
| Phiếu DO | Phiếu nhập kho (Receipt, `stock.picking` loại incoming) tạo tự động khi đơn được duyệt (AS-12, sửa v0.3) |
| Vendor | Nhà cung cấp (`res.partner` có bảng giá nhà cung cấp) |
| MH | Phòng / Nhân viên Mua hàng |
| Backorder | Phiếu DO mới cho phần hàng chưa nhận đủ |
| Chatter | Khung lịch sử trao đổi và theo dõi thay đổi bên phải form Odoo |
| Activity | Việc cần làm Odoo giao cho một người dùng, có hạn xử lý |
| Vật tư Nhập kho | Vật tư có quản lý tồn kho, mua qua YCMH, nhận hàng bằng phiếu DO (AS-26) |
| Vật tư Dịch vụ | Vật tư không tồn kho, mua bằng RFQ trực tiếp, không có YCMH và phiếu DO (AS-26, FR-25) |
| Hợp đồng mua hàng | Hợp đồng khung với NCC (Purchase Agreement loại Blanket Order): vật tư, đơn giá, thời hạn hiệu lực (AS-30) |
| Báo giá NCC | Báo giá nhà cung cấp gửi công ty, lưu ở danh mục mới; khác RFQ "Yêu cầu báo giá" do công ty gửi đi (AS-33) |
| Price List | Bảng giá nhà cung cấp chuẩn Odoo (`product.supplierinfo`) trên tab Mua của vật tư |
| Nguồn giá | Nơi lấy NCC và đơn giá của dòng YCMH: Hợp đồng, Báo giá NCC, Price List, Nhập tay hoặc Không có |
| Kho nhận (cột "Nhập kho") | Kho sẽ nhập hàng của một dòng YCMH; một phiếu có nhiều kho (AS-29) |
| Trưởng nhóm | Quản lý trực tiếp của người tạo trên hồ sơ nhân viên, duyệt cấp 1 YCMH (AS-34) |
| BOD | Ban giám đốc, duyệt cấp 3 YCMH (AS-34) |
| Mã BP | Mã bộ phận của người tạo, phần đầu của số phiếu YCMH (AS-28) |
| Send email | Nút trên RFQ: soạn 1 email, chọn nhiều NCC (ngăn cách ";"), hệ thống gửi riêng từng NCC (FR-06) |
| Mã Yêu cầu mua hàng (trên RFQ) | Mã YCMH gốc của RFQ, hiển thị và lưu ngầm để truy vấn (FR-27) |
| Ngày dự kiến / thực tế nhận hàng | Ngày dự kiến do MH nhập trên RFQ; ngày thực tế = ngày hoàn tất phiếu DO (AS-43) |

## 2. Mô tả tổng quan

### 2.1 Bối cảnh hệ thống
Toàn bộ quy trình chạy trong một CSDL Odoo 17 Enterprise (AS-01). Approvals quản lý Yêu cầu mua hàng; Purchase quản lý RFQ và đơn mua hàng; Accounting quản lý Đề nghị thanh toán và thanh toán; Inventory quản lý phiếu DO. Máy chủ email (SMTP) gửi RFQ cho vendor và thông báo cho người dùng.

```mermaid
flowchart LR
  ND([Người đề xuất]) --> AP[Approvals - Yêu cầu mua hàng]
  HD[Purchase - Hợp đồng mua hàng] -->|Tạo YCMH, tra giá| AP
  BG[Purchase - Báo giá NCC] -->|Tạo YCMH| AP
  MH([Nhân viên MH - dịch vụ]) -->|RFQ trực tiếp| PU
  AP -->|Duyệt xong - tự tạo| PU[Purchase - RFQ và Đơn mua hàng]
  PU -->|Email RFQ riêng từng NCC| VD([Vendor])
  VD -->|Reply kèm Excel báo giá| PU
  PU -->|Đề nghị thanh toán| AC[Accounting]
  PU -->|Duyệt xong - tự tạo phiếu DO| IN[Inventory]
  AC -->|Thanh toán| VD
```

### 2.2 Vai trò người dùng
| Vai trò | Hệ thống | Quyền chính |
|---|---|---|
| Người đề xuất | Backend — Approvals, Purchase (đọc Hợp đồng, Báo giá NCC) | Tạo YCMH trực tiếp / từ Hợp đồng / từ Báo giá NCC; sửa, gửi, huỷ YCMH của mình |
| Nhân viên MH | Backend — Approvals, Purchase, Accounting | Duyệt cấp 2 YCMH; quản lý Hợp đồng, Báo giá NCC; tạo PO dịch vụ trực tiếp; tạo, gửi email, huỷ RFQ; so sánh và chọn NCC; tạo ĐNTT; gửi duyệt đơn *(sửa v0.3)* |
| Trưởng nhóm | Backend — Approvals | Duyệt cấp 1 YCMH do thành viên nhóm tạo *(v0.2, thay vai trò Trưởng phòng)* |
| BOD | Backend — Approvals | Duyệt cấp 3 YCMH *(v0.2)* |
| Trưởng phòng Mua hàng | Backend — Purchase | Duyệt đơn mua hàng 1 cấp, không ngưỡng (AS-39) |
| Giám đốc | Backend — Purchase | **[Đã bỏ — v0.3]** ~~Duyệt đơn mua hàng từ ngưỡng~~ — không còn ngưỡng (tra-loi-cau-hoi-mo-lan-1.md) |
| Kế toán | Backend — Accounting | Duyệt, từ chối ĐNTT; ghi nhận thanh toán |
| Thủ kho | Backend — Inventory | Xác nhận phiếu DO, tạo backorder |
| Quản trị hệ thống | Backend — Settings | Cấu hình người duyệt, mẫu email, mẫu Excel báo giá, hộp thư nhận báo giá *(sửa v0.3)* |

### 2.3 Giả định & phụ thuộc
- **Giả định:** xem mục 9.1 (AS-01 … AS-47).
- **Phụ thuộc:**
  - Odoo 17 Enterprise với các module `purchase`, `purchase_requisition` (Blanket Order), `approvals`, `approval_purchase`, `stock`, `account_accountant` (AS-01).
  - Module tuỳ biến mới `purchase_flow_custom` (tên đề xuất) chứa toàn bộ thay đổi; không sửa mã nguồn lõi.
  - Máy chủ SMTP đã cấu hình trong Odoo.
  - Incoming mail server (IMAP/POP) và alias email cho RFQ để nhận email NCC trả lời (AS-45). *(v0.3)*
  - Thư viện đọc file `.xlsx` (openpyxl, có sẵn trong Odoo 17) cho FR-26. *(v0.3)*
  - Dữ liệu Price List (`product.supplierinfo`) và Hợp đồng mua hàng còn hiệu lực (AS-30, AS-31).
  - Vật tư được phân loại đúng Nhập kho / Dịch vụ trước go-live (AS-26).
  - Hồ sơ nhân viên có Bộ phận (kèm Mã BP) và Trưởng nhóm (Manager) (AS-28, AS-34).

## 3. Yêu cầu chức năng

### FR-01 — Tạo và gửi Yêu cầu mua hàng
- **Mô tả:** Người đề xuất tạo YCMH trực tiếp tại menu "Yêu cầu mua hàng" (cách 1 trong 3 cách tạo; cách 2, 3 ở FR-22, FR-23), gồm nhiều dòng vật tư Nhập kho, rồi gửi duyệt. *(Sửa v0.2 — nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md)*
- **Vai trò:** Người đề xuất
- **Truy vết:** US-01 · Màn hình: SCR-01, SCR-02
- **Input:**
  - Đầu phiếu: Người tạo (mặc định người đăng nhập, chỉ đọc); Bộ phận (từ hồ sơ nhân viên, chỉ đọc); Ngày tạo (tự động); Nguồn tạo (Trực tiếp / Hợp đồng / Báo giá NCC, chỉ đọc); Ngày cần hàng (date, tuỳ chọn, AS-35); Ghi chú (text, tuỳ chọn); Tệp đính kèm.
  - Dòng: Vật tư (bắt buộc, chỉ loại Nhập kho); Đơn vị tính (bắt buộc); Nhập kho — kho nhận (bắt buộc, AS-29); Số lượng (bắt buộc, > 0); Nhà cung cấp (tự điền theo FR-24, bắt buộc trước khi MH duyệt cấp 2); Đơn giá và Nguồn giá (tự điền theo FR-24); Ghi chú.
- **Output:** Lưu lần đầu → số phiếu `<Mã BP>_<XXXX>_<DD>_<MM>_<YY>` (AS-28). Gửi duyệt → trạng thái "Chờ duyệt", activity "Duyệt yêu cầu mua hàng" cho Trưởng nhóm của người tạo.
- **Business rules:**
  - BR-01.1: Phải có ít nhất 1 dòng.
  - BR-01.2 *(sửa v0.2)*: Ngày cần hàng không bắt buộc; đã nhập thì phải ≥ ngày hiện tại.
  - BR-01.3: Chỉ sửa được phiếu ở trạng thái "Nháp".
  - BR-01.4: Tổng dự kiến = Σ (Số lượng × Đơn giá), chỉ để tham khảo.
  - BR-01.5 *(mới v0.2)*: Không có 2 dòng trùng cả Vật tư và Nhà cung cấp; dòng chưa có NCC chưa xét trùng.
  - BR-01.6 *(mới v0.2)*: Số lượng không được để trống và phải > 0.
  - BR-01.7 *(mới v0.2)*: Ô Vật tư chỉ liệt kê vật tư loại Nhập kho (FR-19).
  - BR-01.8 *(mới v0.2)*: Số phiếu cấp khi lưu lần đầu; Mã BP = mã bộ phận của người tạo; XXXX đếm theo bộ phận, về 0001 đầu năm (AS-28).
- **Acceptance criteria:**
  1. **Given** người tạo thuộc bộ phận Hành chính (Mã BP `HC`) và bộ phận đã có 11 phiếu năm 2026 **When** lưu phiếu mới ngày 20/10/2026 **Then** phiếu nhận số `HC_0012_20_10_26`.
  2. **Given** phiếu có 1 dòng đủ Vật tư, Đơn vị tính, Nhập kho, Số lượng **When** bấm "Gửi duyệt" **Then** phiếu chuyển "Chờ duyệt" và Trưởng nhóm có activity hạn 1 ngày làm việc (AS-24).
  3. **Given** phiếu không có dòng **When** bấm "Gửi duyệt" **Then** hiện lỗi "Yêu cầu mua hàng phải có ít nhất một sản phẩm" và phiếu giữ "Nháp".
  4. **Given** dòng 2 cùng vật tư "Bút bi Thiên Long TL-027" và cùng NCC Hồng Hà với dòng 1 **When** bấm "Lưu" **Then** hiện lỗi "Trùng vật tư và nhà cung cấp với dòng 1".
  5. **Given** dòng để trống số lượng **When** bấm "Lưu" **Then** hiện lỗi "Không được để trống số lượng" tại ô số lượng.
  6. **Given** người tạo gõ "Vệ sinh" ở ô Vật tư **When** danh sách gợi ý hiện ra **Then** không có vật tư loại Dịch vụ "[DV-005] Vệ sinh công nghiệp văn phòng".
- **Độ ưu tiên:** Must

### FR-02 — Duyệt Yêu cầu mua hàng 3 cấp
- **Mô tả:** YCMH được duyệt tuần tự: cấp 1 Trưởng nhóm (theo người tạo) → cấp 2 Nhân viên MH → cấp 3 BOD. *(Sửa v0.2 — v0.1 là 2 cấp MH → Trưởng phòng; nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md)*
- **Vai trò:** Trưởng nhóm, Nhân viên MH, BOD
- **Truy vết:** US-05, US-14, US-24 · Màn hình: SCR-02
- **Input:** Thao tác "Duyệt" của người duyệt đúng cấp; Nhà cung cấp trên từng dòng (MH bổ sung khi thiếu).
- **Output:** Mỗi cấp duyệt xong → activity cho cấp kế tiếp; cấp 3 duyệt xong → YCMH "Đã duyệt" và kích hoạt FR-05.
- **Business rules:**
  - BR-02.1: Approvals "Approvers sequence" bật; mỗi cấp chỉ thấy nút "Duyệt" khi cấp trước đã duyệt.
  - BR-02.2 *(sửa v0.2)*: Cấp 1 = Manager trên hồ sơ nhân viên của người tạo; người tạo chưa có Manager → chặn gửi duyệt. Cấp 2 = một người thuộc nhóm Nhân viên MH. Cấp 3 = một thành viên nhóm BOD (AS-34).
  - BR-02.3 *(sửa v0.2)*: Khi Nhân viên MH duyệt cấp 2, mọi dòng phải có Nhà cung cấp (AS-32).
  - BR-02.4: Người tạo không được tự duyệt phiếu của mình.
- **Acceptance criteria:**
  1. **Given** phiếu "Chờ duyệt" cấp 1 **When** Trưởng nhóm Phan Thanh Tâm bấm "Duyệt" **Then** cấp 1 chuyển "Đã duyệt" và Nhân viên MH có activity duyệt.
  2. **Given** cấp 1 đã duyệt, dòng "Máy in HP LaserJet M211dw" chưa có NCC **When** Nhân viên MH bấm "Duyệt" **Then** hiện lỗi "Chưa có nhà cung cấp cho: Máy in HP LaserJet M211dw" và phiếu giữ trạng thái.
  3. **Given** cấp 2 chưa duyệt **When** thành viên BOD mở phiếu **Then** nút "Duyệt" không hiển thị.
  4. **Given** cấp 2 đã duyệt **When** thành viên BOD Đỗ Quang Huy bấm "Duyệt" **Then** phiếu chuyển "Đã duyệt" trong cùng giao dịch với việc tạo RFQ (FR-05).
  5. **Given** người tạo chưa có Trưởng nhóm trên hồ sơ nhân viên **When** bấm "Gửi duyệt" **Then** hiện lỗi "Chưa cấu hình Trưởng nhóm cho Nguyễn Thu Hà".
- **Độ ưu tiên:** Must

### FR-03 — Từ chối và gửi lại Yêu cầu mua hàng
- **Mô tả:** Người duyệt ở cấp bất kỳ từ chối YCMH kèm lý do; YCMH về "Nháp" và hệ thống gửi email cho người tạo; người tạo sửa và gửi lại. *(Sửa v0.3 — nguồn: tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #6. v0.2: phiếu chuyển "Từ chối", bấm "Về nháp" mới sửa được)*
- **Vai trò:** Trưởng nhóm, Nhân viên MH, BOD, Người đề xuất
- **Truy vết:** US-02, US-05, US-14, US-24 · Màn hình: SCR-02
- **Input:** Lý do từ chối (text, bắt buộc).
- **Output:** YCMH "Nháp"; trạng thái mọi người duyệt đặt lại; tin nhắn chatter "Từ chối bởi <người duyệt> (cấp <n>): <lý do>"; email cho người tạo; thông báo lý do ở đầu phiếu.
- **Business rules:**
  - BR-03.1: Lý do bắt buộc, tối thiểu 10 ký tự (AS-25).
  - BR-03.2 *(sửa v0.3)*: Từ chối → YCMH về "Nháp" ngay, không còn trạng thái "Từ chối"; gửi lại thì duyệt từ cấp 1.
  - BR-03.3 *(mới v0.3)*: Email gửi người tạo: tiêu đề "Yêu cầu mua hàng <số phiếu> bị từ chối", nội dung có người từ chối, cấp duyệt, lý do, link mở phiếu.
  - BR-03.4 *(mới v0.3)*: Quy tắc về Nháp áp dụng cho YCMH; đơn mua hàng theo FR-10, ĐNTT theo FR-12 (_changes/20261020-084051.md #6: "trước mắt cứ là YCMH").
- **Acceptance criteria:**
  1. **Given** thành viên BOD bấm "Từ chối" **When** để trống lý do và bấm "Xác nhận" **Then** hiện lỗi "Vui lòng nhập lý do từ chối" và hộp thoại không đóng.
  2. **Given** lý do hợp lệ **When** bấm "Xác nhận" **Then** phiếu về "Nháp", đầu phiếu hiện lý do và người tạo nhận email tiêu đề "Yêu cầu mua hàng HC_0012_20_10_26 bị từ chối".
  3. **Given** phiếu bị từ chối đã về "Nháp" **When** người tạo sửa và bấm "Gửi duyệt" **Then** phiếu chuyển "Chờ duyệt" cấp 1 và chatter còn lịch sử lần từ chối trước.
- **Độ ưu tiên:** Must

### FR-04 — Huỷ Yêu cầu mua hàng
- **Mô tả:** Người đề xuất huỷ YCMH chưa duyệt xong.
- **Vai trò:** Người đề xuất
- **Truy vết:** US-04 · Màn hình: SCR-02
- **Input:** Thao tác "Huỷ".
- **Output:** YCMH "Đã huỷ"; activity duyệt đang mở bị xoá.
- **Business rules:**
  - BR-04.1: Chỉ huỷ được khi trạng thái là "Nháp", "Chờ duyệt" hoặc "Từ chối" (AS-14).
- **Acceptance criteria:**
  1. **Given** phiếu "Chờ duyệt" **When** người đề xuất bấm "Huỷ" **Then** phiếu chuyển "Đã huỷ" và activity của người duyệt bị xoá.
  2. **Given** phiếu "Đã duyệt" **When** mở phiếu **Then** nút "Huỷ" không hiển thị.
- **Độ ưu tiên:** Should

### FR-05 — Tự động tạo RFQ gộp theo vendor
- **Mô tả:** Khi YCMH chuyển "Đã duyệt", hệ thống tạo RFQ: YCMH có N nhà cung cấp khác nhau → N RFQ; chỉ 1 nhà cung cấp → đúng 1 RFQ (xác nhận ở khao-sat-lan-2-yeu-cau-mua-hang.md).
- **Vai trò:** Hệ thống
- **Truy vết:** US-06 · Màn hình: Không có UI (kết quả hiển thị ở SCR-02, SCR-04)
- **Input:** Dòng YCMH đã xác định vendor (BR-02.3).
- **Output:** n RFQ trạng thái "Nháp" (n = số vendor khác nhau); mỗi RFQ có `Yêu cầu mua hàng` = YCMH gốc; activity "Gửi RFQ" cho Nhân viên MH đã duyệt cấp 1.
- **Business rules:**
  - BR-05.1: Nhóm dòng theo vendor; mỗi YCMH sinh RFQ riêng, không gộp vào RFQ của YCMH khác (AS-05).
  - BR-05.2 *(sửa v0.2)*: Dòng RFQ lấy vật tư, ghi chú, số lượng, đơn vị tính, kho nhận; ngày cần hàng (nếu có) → `date_planned`; đơn giá = đơn giá trên dòng YCMH (Hợp đồng / Báo giá NCC / Price List / nhập tay), trống thì = 0.
  - BR-05.5 *(mới v0.2)*: Không tách RFQ theo kho: dòng cùng NCC nhưng khác kho nhận vẫn chung 1 RFQ, mỗi dòng giữ kho nhận của mình (AS-29, quyết định #14).
  - BR-05.7 *(mới v0.3)*: Kế thừa đầu phiếu từ YCMH: Người tạo YCMH, Bộ phận, Ghi chú; Ngày cần hàng → Ngày dự kiến nhận hàng (AS-43); NCC của RFQ = NCC của nhóm dòng, bắt buộc.
  - BR-05.8 *(mới v0.3)*: Số RFQ và mã truy vết YCMH theo FR-27.
  - BR-05.6 *(mới v0.2)*: Dòng có nguồn giá Hợp đồng → RFQ liên kết hợp đồng đó (`requisition_id`); RFQ có dòng từ 2 hợp đồng khác nhau thì liên kết hợp đồng của dòng đầu tiên, các dòng còn lại ghi số hợp đồng ở ghi chú dòng.
  - BR-05.3: Chạy một lần cho mỗi YCMH (cờ `rfq_generated`); duyệt lại không tạo RFQ trùng.
  - BR-05.4: Lỗi khi tạo RFQ → huỷ toàn bộ giao dịch duyệt, YCMH giữ trạng thái cũ, hiện lỗi cho người duyệt.
- **Acceptance criteria:**
  1. **Given** YCMH có 3 dòng: 2 dòng vendor "Công ty Văn phòng phẩm Hồng Hà", 1 dòng vendor "Công ty TNHH Tin học Phong Vũ" **When** BOD duyệt **Then** tạo đúng 2 RFQ Nháp, RFQ Hồng Hà có 2 dòng, RFQ Phong Vũ có 1 dòng.
  2. **Given** RFQ đã tạo **When** mở RFQ **Then** trường "Yêu cầu mua hàng" hiện mã YCMH gốc và mở được phiếu gốc.
  3. **Given** YCMH đã có cờ `rfq_generated` **When** hàm tạo RFQ được gọi lại **Then** không có RFQ mới nào được tạo.
  4. **Given** YCMH có 2 dòng cùng NCC Phong Vũ, một dòng kho "Kho chính", một dòng kho "Kho chi nhánh Bình Dương" **When** BOD duyệt **Then** tạo 1 RFQ Phong Vũ có 2 dòng, mỗi dòng giữ đúng kho nhận.
  5. **Given** dòng "Giấy A4 Double A 80gsm" có nguồn giá Hợp đồng HĐ-HH-2026-01 giá 78.000₫ **When** RFQ được tạo **Then** dòng RFQ có đơn giá 78.000₫ và RFQ liên kết HĐ-HH-2026-01.
- **Độ ưu tiên:** Must

### FR-06 — Gửi email xin báo giá tới nhiều nhà cung cấp ("Send email")
- **Mô tả:** Trên RFQ, nút "Send email" mở popup soạn email như email thường; ô "Gửi đến" chọn nhiều NCC, ngăn cách bằng ";"; khi gửi, hệ thống tách gửi riêng từng NCC. *(Sửa v0.3 — nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; v0.2: mỗi RFQ một email tới vendor của RFQ, gửi hàng loạt từ danh sách)*
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-07 · Màn hình: SCR-04, SCR-05
- **Input:** Gửi đến (một hoặc nhiều NCC hoặc địa chỉ email, ngăn cách ";"; mặc định NCC của RFQ); Tiêu đề; Nội dung (mẫu "Yêu cầu báo giá", có bảng sản phẩm của phiếu); Tệp đính kèm (PDF RFQ, file Excel mẫu báo giá — AS-44).
- **Output:** N email riêng, mỗi email 1 người nhận; 1 tin nhắn chatter liệt kê các NCC đã gửi; RFQ trạng thái "RFQ" (state `sent`); danh sách "NCC được hỏi giá" của RFQ cập nhật.
- **Business rules:**
  - BR-06.1: NCC không có email → chặn gửi, báo tên NCC, không gửi email nào (AS-13).
  - BR-06.2 *(sửa v0.3)*: N người nhận → N email riêng; không dùng To/CC chung (_changes/20261020-093008.md #7).
  - BR-06.3: Gửi lại được; trạng thái giữ nguyên; NCC mới được thêm vào danh sách hỏi giá.
  - BR-06.4 *(mới v0.3)*: Reply-to của email là alias của RFQ để email trả lời gắn đúng RFQ (FR-26).
  - BR-06.5 *(mới v0.3)*: PO Dịch vụ không có nút "Send email" (FR-25).
  - BR-06.6 *(sửa v0.3)*: Bỏ thao tác gửi hàng loạt nhiều RFQ từ danh sách (SCR-03).
- **Acceptance criteria:**
  1. **Given** RFQ HC-PO-0012-20-10-2026-02 "Nháp" **When** bấm "Send email", nhập "Công ty TNHH Tin học Phong Vũ; Công ty CP Thế Giới Di Động; Công ty TNHH Thiết bị Minh Khoa" và bấm "Gửi" **Then** hệ thống gửi 3 email riêng, mỗi email chỉ có 1 người nhận, RFQ chuyển "RFQ".
  2. **Given** danh sách có "Công ty TNHH An Phát" chưa có email **When** bấm "Gửi" **Then** hiện lỗi "Nhà cung cấp Công ty TNHH An Phát chưa có email" và không email nào được gửi.
  3. **Given** email đã gửi **When** mở chatter RFQ **Then** có 1 tin nhắn liệt kê 3 NCC đã gửi, tệp đính kèm và thời điểm.
- **Độ ưu tiên:** Must

### FR-07 — Tạo RFQ thay thế cho vendor khác **[Đã bỏ — v0.3]**
- **Lý do bỏ:** giữ 1 RFQ, gửi email riêng tới N NCC (FR-06), so sánh và chọn NCC cho cả phiếu (FR-08) — khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md quyết định #8.
- **Mô tả:** Từ một RFQ, Nhân viên MH tạo RFQ cho vendor khác với cùng dòng sản phẩm để so sánh giá (Alternatives, AS-06).
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-08 · Màn hình: Không có UI (đã bỏ)
- **Input:** Vendor (bắt buộc); Sao chép dòng sản phẩm (mặc định bật).
- **Output:** RFQ Nháp mới cùng nhóm thay thế; tab "Báo giá thay thế" ở các RFQ trong nhóm liệt kê nhau.
- **Business rules:**
  - BR-07.1: Một vendor chỉ có một RFQ trong một nhóm thay thế.
  - BR-07.2: Chỉ tạo được khi RFQ ở trạng thái "Nháp" hoặc "RFQ".
  - BR-07.3: RFQ thay thế kế thừa trường "Yêu cầu mua hàng" của RFQ gốc.
- **Acceptance criteria:**
  1. **Given** RFQ P00012 vendor Hồng Hà **When** bấm "Tạo RFQ thay thế", chọn vendor "Công ty CP Thiên Long" và "Tạo" **Then** RFQ P00014 vendor Thiên Long được tạo với cùng sản phẩm, số lượng và xuất hiện trong tab "Báo giá thay thế" của P00012.
  2. **Given** Thiên Long đã có RFQ trong nhóm **When** chọn lại Thiên Long **Then** hiện lỗi "Vendor Công ty CP Thiên Long đã có RFQ trong nhóm này".
- **Độ ưu tiên:** Must

### FR-08 — So sánh giá và chọn nhà cung cấp
- **Mô tả:** Nút "So sánh giá" trên RFQ mở bảng so sánh báo giá của các NCC đã hỏi (đọc từ Excel theo FR-26 hoặc nhập tay); MH chọn 1 NCC cho cả phiếu; RFQ đổi NCC và đơn giá theo báo giá đó. *(Sửa v0.3 — nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #8. v0.2: so sánh giữa các RFQ thay thế, chọn theo dòng)*
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-09 · Màn hình: SCR-04, SCR-06
- **Input:** Báo giá NCC gắn với RFQ (FR-26) hoặc nhập tay; thao tác "Chọn NCC này".
- **Output:** RFQ có NCC = NCC được chọn; đơn giá, ngày giao từng dòng = báo giá; nguồn giá dòng "Báo giá NCC <số>"; chatter "Đổi NCC: A → B, tổng X → Y"; các báo giá còn lại đánh dấu "Không chọn".
- **Business rules:**
  - BR-08.1 *(sửa v0.3)*: Bảng so sánh: mỗi vật tư của RFQ một hàng, mỗi NCC một cột (đơn giá, thành tiền), hàng tổng và ngày giao theo NCC; đánh dấu giá thấp nhất từng dòng và tổng thấp nhất.
  - BR-08.2 *(sửa v0.3)*: Chọn 1 NCC cho cả phiếu, không tách theo dòng (_changes/20261020-093008.md #8).
  - BR-08.3 *(sửa v0.3)*: NCC thiếu giá ở bất kỳ dòng nào → không chọn được.
  - BR-08.4 *(sửa v0.3)*: Chỉ chọn được khi RFQ ở "Nháp" hoặc "RFQ" và chưa có ĐNTT; đã có ĐNTT thì đổi NCC làm ĐNTT chưa duyệt bị huỷ (BR-11.4).
  - BR-08.5 *(mới v0.3)*: MH nhập tay báo giá cho một NCC khi file Excel lỗi hoặc NCC báo giá ngoài email (AS-45).
  - BR-08.6 *(mới v0.3)*: Chỉ dùng báo giá mới nhất của mỗi NCC (báo giá cũ "Đã thay thế", AS-46).
- **Acceptance criteria:**
  1. **Given** RFQ có báo giá Phong Vũ (tổng 63.570.000₫) và Thế Giới Di Động (tổng 64.200.000₫) **When** bấm "So sánh giá" **Then** bảng có 2 cột NCC và cột Phong Vũ được đánh dấu "Tổng thấp nhất".
  2. **Given** NCC hiện tại là Phong Vũ **When** chọn cột Thế Giới Di Động, bấm "Chọn NCC này" và xác nhận **Then** RFQ đổi NCC sang Công ty CP Thế Giới Di Động, đơn giá các dòng theo báo giá này, chatter ghi "Đổi NCC: Công ty TNHH Tin học Phong Vũ → Công ty CP Thế Giới Di Động".
  3. **Given** báo giá Minh Khoa thiếu giá "Máy in HP LaserJet M211dw" **When** bấm "Chọn NCC này" ở cột Minh Khoa **Then** hiện lỗi "Báo giá của Công ty TNHH Thiết bị Minh Khoa thiếu giá cho Máy in HP LaserJet M211dw".
  4. **Given** RFQ chưa có báo giá nào **When** bấm "So sánh giá" **Then** màn hình hiện "Chưa có báo giá NCC nào được ghi nhận".
- **Độ ưu tiên:** Must

### FR-09 — Gửi duyệt đơn mua hàng (Approve)
- **Mô tả:** Sau khi chọn NCC và tạo ĐNTT, Nhân viên MH bấm "Approve" để đơn vào quy trình duyệt; áp dụng cho RFQ vật tư Nhập kho và PO Dịch vụ. *(Sửa v0.3 — nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md)*
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-10 · Màn hình: SCR-04
- **Input:** RFQ trạng thái "RFQ" (Nhập kho) hoặc PO dịch vụ "Nháp"; ĐNTT của đơn.
- **Output:** Đơn trạng thái "Chờ duyệt" (state `to approve`); activity cho Trưởng phòng Mua hàng (FR-10).
- **Business rules:**
  - BR-09.1: Mọi dòng số lượng > 0 phải có đơn giá > 0.
  - BR-09.2: Đơn phải có ít nhất 1 dòng số lượng > 0.
  - BR-09.3: Ghi nhận "Người gửi duyệt" và thời điểm.
  - BR-09.4 *(mới v0.3)*: Bắt buộc có ĐNTT ở trạng thái "Chờ kế toán duyệt", "Đã duyệt" hoặc "Đã thanh toán" (AS-40).
- **Acceptance criteria:**
  1. **Given** RFQ "RFQ", mọi dòng có giá, ĐNTT DNTT/2026/0007 "Chờ kế toán duyệt" **When** bấm "Approve" **Then** đơn chuyển "Chờ duyệt" và Trưởng phòng Mua hàng có activity duyệt.
  2. **Given** một dòng số lượng 10, đơn giá 0 **When** bấm "Approve" **Then** hiện lỗi "Chưa nhập đơn giá cho sản phẩm Mực in HP 107A" và đơn giữ "RFQ".
  3. **Given** đơn chưa có ĐNTT **When** bấm "Approve" **Then** hiện lỗi "Phải tạo Đề nghị thanh toán trước khi gửi duyệt" và đơn giữ trạng thái.
- **Độ ưu tiên:** Must

### FR-10 — Duyệt hoặc từ chối đơn mua hàng
- **Mô tả:** Đơn "Chờ duyệt" được Trưởng phòng Mua hàng duyệt 1 cấp, không phân ngưỡng giá trị; duyệt xong đơn chuyển PO (FR-13). *(Sửa v0.3 — nguồn: tra-loi-cau-hoi-mo-lan-1.md; người duyệt: AS-39. v0.2: 2 cấp, ngưỡng 50.000.000₫)*
- **Vai trò:** Trưởng phòng Mua hàng
- **Truy vết:** US-15 · Màn hình: SCR-03, SCR-04
- **Input:** Thao tác "Duyệt" / "Từ chối" + lý do.
- **Output:** Duyệt → đơn "PO" và tạo phiếu DO (FR-13); Từ chối → đơn Nhập kho về "RFQ", đơn Dịch vụ về "Nháp".
- **Business rules:**
  - BR-10.1 *(sửa v0.3)*: Một cấp duyệt, không ngưỡng giá trị (AS-39).
  - BR-10.2 *(bỏ v0.3)*: ~~Cấp 2 chỉ duyệt được khi cấp 1 đã duyệt~~ — không còn cấp 2.
  - BR-10.3: Lý do từ chối bắt buộc, tối thiểu 10 ký tự (AS-25); về "RFQ" giữ nguyên NCC, giá đã chọn và ĐNTT; MH nhận email kèm lý do. Hộp thoại nhập lý do dùng chung mẫu với SCR-02 trạng thái "Từ chối - nhập lý do".
  - BR-10.4: Nhân viên MH gửi duyệt không được tự duyệt đơn của mình.
  - BR-10.5: Bộ lọc "Chờ tôi duyệt" trên danh sách đơn chỉ hiện đơn có activity duyệt của người đăng nhập.
- **Acceptance criteria:**
  1. **Given** đơn "Chờ duyệt" tổng 69.927.000₫ **When** Trưởng phòng Mua hàng bấm "Duyệt" **Then** đơn chuyển "PO".
  2. **Given** đơn "Chờ duyệt" tổng 120.000.000₫ **When** Trưởng phòng Mua hàng bấm "Duyệt" **Then** đơn chuyển "PO", không có thêm cấp duyệt.
  3. **Given** Trưởng phòng Mua hàng bấm "Từ chối" với lý do "Giá cao hơn hợp đồng năm" **When** xác nhận **Then** đơn về "RFQ" và Nhân viên MH nhận email chứa lý do.
- **Độ ưu tiên:** Must

### FR-11 — Tạo Đề nghị thanh toán trước khi gửi duyệt
- **Mô tả:** Sau khi chọn NCC (Nhập kho) hoặc tạo PO dịch vụ, Nhân viên MH bắt buộc tạo ĐNTT và gửi Kế toán trước khi gửi duyệt đơn. *(Sửa v0.3 — nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md. v0.2: ĐNTT tạo sau khi đơn được duyệt, đơn chuyển Waiting PO)*
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-11 · Màn hình: SCR-04, SCR-08
- **Input:** Đơn mua hàng (tự điền mã RFQ/PO); Vendor (tự điền); Số tiền đề nghị (mặc định = tổng đơn, bắt buộc, > 0); Ngày đề nghị thanh toán (bắt buộc); Hình thức thanh toán (Chuyển khoản / Tiền mặt, bắt buộc); Tài khoản ngân hàng vendor (bắt buộc khi Chuyển khoản); Nội dung; Tệp đính kèm (báo giá, hợp đồng).
- **Output:** ĐNTT mã `DNTT/<năm>/<4 số>` trạng thái "Chờ kế toán duyệt"; đơn giữ trạng thái hiện tại và đủ điều kiện "Approve" (FR-09); activity cho nhóm Kế toán.
- **Business rules:**
  - BR-11.1 *(sửa v0.3)*: Tạo được từ RFQ "RFQ" đã chọn NCC hoặc PO dịch vụ "Nháp"; mỗi đơn tối đa 1 ĐNTT chưa bị từ chối.
  - BR-11.2: Số tiền đề nghị ≤ tổng đơn.
  - BR-11.3 *(sửa v0.3)*: Bỏ trạng thái `Waiting PO`; gửi ĐNTT không đổi trạng thái đơn.
  - BR-11.4 *(mới v0.3)*: Đổi NCC hoặc đơn giá sau khi tạo ĐNTT → ĐNTT chưa duyệt bị huỷ, MH tạo ĐNTT mới.
- **Acceptance criteria:**
  1. **Given** RFQ HC-PO-0012-20-10-2026-02 "RFQ", NCC Phong Vũ, tổng 69.927.000₫ **When** bấm "Tạo đề nghị thanh toán" **Then** mở form ĐNTT điền sẵn NCC, mã đơn, số tiền 69.927.000₫.
  2. **Given** ĐNTT hợp lệ **When** bấm "Gửi kế toán" **Then** ĐNTT "Chờ kế toán duyệt", RFQ giữ "RFQ" và nút "Approve" dùng được.
  3. **Given** số tiền 70.000.000₫ > tổng đơn **When** bấm "Gửi kế toán" **Then** hiện lỗi "Số tiền đề nghị vượt tổng giá trị đơn mua hàng".
  4. **Given** hình thức "Chuyển khoản" và không chọn tài khoản ngân hàng **When** bấm "Gửi kế toán" **Then** hiện lỗi tại trường "Tài khoản ngân hàng".
- **Độ ưu tiên:** Must

### FR-12 — Kế toán xử lý Đề nghị thanh toán
- **Mô tả:** Kế toán duyệt hoặc từ chối ĐNTT; ĐNTT đã duyệt được ghi nhận thanh toán.
- **Vai trò:** Kế toán
- **Truy vết:** US-16 · Màn hình: SCR-07, SCR-08
- **Input:** Thao tác "Duyệt"/"Từ chối" + lý do; khi ghi nhận thanh toán: Sổ nhật ký (Ngân hàng/Tiền mặt), Ngày thanh toán, Số tiền.
- **Output:** ĐNTT "Đã duyệt" / "Từ chối" / "Đã thanh toán"; bút toán thanh toán `account.payment` loại outbound cho vendor, liên kết ĐNTT.
- **Business rules:**
  - BR-12.1 *(sửa v0.3)*: Từ chối ĐNTT → đơn đang "Chờ duyệt" về "RFQ" (dịch vụ: "Nháp"); đơn đã "PO" giữ "PO"; MH tạo ĐNTT mới (AS-41).
  - BR-12.2: Thanh toán là khoản trả trước cho vendor (chưa đối trừ hoá đơn, AS-10); đối trừ hoá đơn theo chuẩn Odoo (AS-15).
  - BR-12.3: Số tiền ghi nhận thanh toán = số tiền đề nghị (không thanh toán một phần, AS-10).
  - BR-12.4 *(sửa v0.3)*: ĐNTT được duyệt hoặc thanh toán không đổi trạng thái đơn.
- **Acceptance criteria:**
  1. **Given** ĐNTT "Chờ kế toán duyệt" **When** Kế toán bấm "Duyệt" **Then** ĐNTT chuyển "Đã duyệt".
  2. **Given** ĐNTT "Đã duyệt" **When** bấm "Ghi nhận thanh toán", chọn sổ "Ngân hàng Vietcombank", ngày 25/10/2026, "Xác nhận" **Then** tạo payment 12.500.000₫ trạng thái Posted và ĐNTT chuyển "Đã thanh toán".
  3. **Given** Kế toán bấm "Từ chối" với lý do hợp lệ **When** xác nhận **Then** ĐNTT "Từ chối", đơn đang "Chờ duyệt" về "RFQ", Nhân viên MH nhận email lý do.
- **Độ ưu tiên:** Must

### FR-13 — Duyệt xong chuyển PO và tự tạo phiếu DO
- **Mô tả:** Khi Trưởng phòng Mua hàng bấm "Duyệt", đơn chuyển `PO` (xác nhận đơn chuẩn Odoo) và hệ thống tự tạo phiếu DO cho vật tư Nhập kho; đơn Dịch vụ không tạo DO. *(Sửa v0.3 — nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3. v0.2: nút "Xác nhận đã nhận hàng" chuyển Waiting PO → PO)*
- **Vai trò:** Hệ thống, Trưởng phòng Mua hàng
- **Truy vết:** US-12, US-25 · Màn hình: SCR-04, SCR-09
- **Input:** Đơn được duyệt (FR-10).
- **Output:** Đơn state `purchase` (hiển thị "PO"); phiếu DO (`stock.picking` incoming) "Sẵn sàng" cho mỗi kho nhận; activity cho Thủ kho; "Ngày nhận hàng thực tế" cập nhật khi phiếu DO cuối cùng hoàn tất.
- **Business rules:**
  - BR-13.1 *(sửa v0.3)*: Chạy tự động trong cùng giao dịch với thao tác "Duyệt"; không còn nút riêng.
  - BR-13.2: Gọi `button_confirm` chuẩn của Odoo để sinh phiếu nhập kho; không tự xác nhận phiếu DO (AS-12).
  - BR-13.3 *(sửa v0.2)*: Kho nhận lấy theo từng dòng đơn (kho nhận từ YCMH, AS-29).
  - BR-13.4 *(mới v0.2)*: Tạo một phiếu DO cho mỗi kho nhận khác nhau trên đơn (tuỳ biến, vì Odoo chuẩn nhận mỗi đơn vào một kho).
  - BR-13.5 *(sửa v0.3)*: Đơn Dịch vụ duyệt xong là `PO`, không sinh phiếu DO.
  - BR-13.6 *(mới v0.3)*: "Ngày nhận hàng thực tế" = ngày hoàn tất phiếu DO cuối cùng của đơn, chỉ đọc (AS-43).
- **Acceptance criteria:**
  1. **Given** đơn "Chờ duyệt" có 2 dòng cùng Kho chính **When** Trưởng phòng Mua hàng bấm "Duyệt" **Then** đơn chuyển "PO" và tạo phiếu `WH/IN/00031` "Sẵn sàng" có 2 dòng đúng số lượng.
  2. **Given** đơn có 2 dòng Kho chính và 1 dòng Kho chi nhánh Bình Dương **When** được duyệt **Then** tạo 2 phiếu DO: một phiếu 2 dòng vào Kho chính, một phiếu 1 dòng vào Kho chi nhánh Bình Dương.
  3. **Given** PO dịch vụ MH-PO-0003-21-10-2026 "Chờ duyệt" **When** được duyệt **Then** đơn chuyển "PO" và smart button "Phiếu DO" hiện 0.
  4. **Given** phiếu WH/IN/00031 hoàn tất ngày 29/10/2026 **When** mở đơn **Then** "Ngày nhận hàng thực tế" hiện 29/10/2026.
- **Độ ưu tiên:** Must

### FR-14 — Nhập kho theo phiếu DO
- **Mô tả:** Thủ kho kiểm đếm, nhập số lượng thực nhận và xác nhận phiếu DO; nhận thiếu tạo backorder.
- **Vai trò:** Thủ kho
- **Truy vết:** US-17 · Màn hình: SCR-09
- **Input:** Số lượng thực nhận từng dòng; lựa chọn "Tạo backorder" / "Không tạo backorder" khi nhận thiếu.
- **Output:** Phiếu DO "Hoàn tất"; tồn kho tăng; số lượng đã nhận trên dòng đơn mua hàng cập nhật; backorder nếu có.
- **Business rules:**
  - BR-14.1: Dùng luồng Validate và backorder chuẩn Odoo Inventory.
  - BR-14.2: Số lượng thực nhận > số lượng đặt → cảnh báo, Thủ kho xác nhận lần 2.
- **Acceptance criteria:**
  1. **Given** phiếu DO "Sẵn sàng" yêu cầu 200 bút bi **When** Thủ kho nhập 200 và bấm "Xác nhận" **Then** phiếu "Hoàn tất" và tồn kho bút bi tăng 200.
  2. **Given** nhập 150/200 **When** bấm "Xác nhận" và chọn "Tạo backorder" **Then** phiếu hiện tại hoàn tất 150 và tạo phiếu DO mới 50 trạng thái "Sẵn sàng".
- **Độ ưu tiên:** Must

### FR-15 — Huỷ RFQ và đơn mua hàng
- **Mô tả:** Nhân viên MH huỷ RFQ hoặc đơn mua hàng chưa ở `PO`.
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-13 · Màn hình: SCR-04
- **Input:** Lý do huỷ (bắt buộc).
- **Output:** Đơn "Đã huỷ"; ĐNTT liên quan ở trạng thái "Nháp"/"Chờ kế toán duyệt"/"Đã duyệt" bị huỷ theo.
- **Business rules:**
  - BR-15.1: Không huỷ được đơn ở `PO` hoặc có ĐNTT "Đã thanh toán" (AS-14).
- **Acceptance criteria:**
  1. **Given** đơn "Chờ duyệt", ĐNTT "Chờ kế toán duyệt" **When** MH bấm "Huỷ" với lý do hợp lệ **Then** đơn và ĐNTT cùng chuyển "Đã huỷ".
  2. **Given** ĐNTT "Đã thanh toán" **When** MH bấm "Huỷ" **Then** hiện lỗi "Đơn đã được thanh toán, liên hệ Kế toán để xử lý".
- **Độ ưu tiên:** Should

### FR-16 — Thông báo và activity
- **Mô tả:** Hệ thống tạo activity và gửi email ở mỗi bước chuyển giao.
- **Vai trò:** Hệ thống
- **Truy vết:** US-05, US-14, US-15, US-16, US-24 · Màn hình: Không có UI
- **Input:** Sự kiện chuyển trạng thái.
- **Output:** Activity (hạn 1 ngày làm việc, AS-24) + email theo bảng quy tắc.
- **Business rules:**
  - BR-16.1 *(sửa v0.3)*: Sự kiện → người nhận: YCMH gửi duyệt → Trưởng nhóm; Trưởng nhóm duyệt → Nhân viên MH; MH duyệt → nhóm BOD; YCMH bị từ chối → người tạo (email, FR-03); RFQ tạo → Nhân viên MH; NCC gửi báo giá → Nhân viên MH (FR-26); đơn gửi duyệt → Trưởng phòng Mua hàng; đơn bị từ chối → Nhân viên MH; ĐNTT gửi → nhóm Kế toán; ĐNTT bị từ chối → Nhân viên MH; phiếu DO tạo → nhóm Thủ kho.
  - BR-16.2: Activity của bước đã xử lý được đánh dấu hoàn thành tự động.
- **Acceptance criteria:**
  1. **Given** đơn gửi duyệt **When** Trưởng phòng Mua hàng duyệt **Then** activity của Trưởng phòng Mua hàng chuyển hoàn thành trong cùng thao tác.
  2. **Given** ĐNTT bị từ chối **When** sự kiện xảy ra **Then** Nhân viên MH nhận 1 email tiêu đề "ĐNTT DNTT/2026/0007 bị từ chối".
- **Độ ưu tiên:** Must

### FR-17 — Truy vết và tra cứu chứng từ
- **Mô tả:** Danh sách và smart button liên kết YCMH ↔ RFQ/đơn ↔ ĐNTT ↔ phiếu DO; bộ lọc theo vai trò.
- **Vai trò:** Tất cả
- **Truy vết:** US-03 · Màn hình: SCR-01, SCR-02, SCR-03, SCR-04, SCR-11, SCR-12
- **Input:** Bộ lọc, nhóm, tìm kiếm.
- **Output:** Danh sách lọc; smart button có số đếm.
- **Business rules:**
  - BR-17.1 *(sửa v0.2)*: Bộ lọc mặc định: Người đề xuất "Của tôi"; Trưởng nhóm "Nhóm của tôi"; MH "Đang xử lý"; BOD "Chờ tôi duyệt".
  - BR-17.2 *(sửa v0.3)*: Smart button YCMH: "RFQ/Đơn mua hàng", "Hợp đồng" hoặc "Báo giá NCC" (khi tạo từ chứng từ đó); đơn: "Yêu cầu mua hàng", "Báo giá NCC" (số báo giá đã nhận), "Đề nghị thanh toán", "Phiếu DO"; Hợp đồng và Báo giá NCC: "Yêu cầu mua hàng".
  - BR-17.3 *(sửa v0.3)*: Danh sách đơn có cột Trạng thái hiển thị nhãn: Nháp, RFQ, Chờ duyệt, PO, Đã huỷ; cột Loại: Nhập kho / Dịch vụ.
- **Acceptance criteria:**
  1. **Given** YCMH sinh 2 RFQ **When** mở YCMH **Then** smart button "RFQ/Đơn mua hàng" hiện 2 và mở danh sách đúng 2 phiếu.
  2. **Given** Người đề xuất mở danh sách YCMH **When** không đổi bộ lọc **Then** chỉ thấy phiếu của mình.
- **Độ ưu tiên:** Should

### FR-18 — Cấu hình người duyệt, mẫu email và mẫu báo giá
- **Mô tả:** Quản trị hệ thống cấu hình người duyệt đơn mua hàng, mẫu email, mẫu file Excel báo giá và hộp thư nhận báo giá. *(Sửa v0.3 — bỏ ngưỡng duyệt; nguồn: tra-loi-cau-hoi-mo-lan-1.md)*
- **Vai trò:** Quản trị hệ thống
- **Truy vết:** US-18 · Màn hình: SCR-10
- **Input:** Người duyệt đơn mua hàng (user, bắt buộc); Mẫu email RFQ; Mẫu email thông báo từ chối; Mẫu file Excel báo giá (.xlsx); Hộp thư nhận báo giá (alias, bắt buộc).
- **Output:** Cấu hình lưu theo công ty; áp dụng cho đơn gửi duyệt và email gửi sau thời điểm lưu.
- **Business rules:**
  - BR-18.1: Chỉ nhóm "Quản trị mua hàng" thấy menu cấu hình.
  - BR-18.2: Đơn đang "Chờ duyệt" giữ người duyệt đã giao lúc gửi.
  - BR-18.3 *(mới v0.3)*: Mẫu Excel phải có đủ cột theo AS-44; thiếu cột thì không lưu được.
  - BR-18.4 *(bỏ v0.3)*: ~~Ngưỡng duyệt cấp 2~~ — không còn ngưỡng.
- **Acceptance criteria:**
  1. **Given** đổi người duyệt đơn mua hàng sang Phạm Thị Lan và lưu **When** MH gửi duyệt đơn mới **Then** Phạm Thị Lan nhận activity duyệt.
  2. **Given** để trống "Người duyệt đơn mua hàng" **When** bấm "Lưu" **Then** hiện lỗi "Vui lòng chọn người duyệt đơn mua hàng".
  3. **Given** tải lên mẫu Excel thiếu cột "Đơn giá" **When** bấm "Lưu" **Then** hiện lỗi "Mẫu báo giá thiếu cột: Đơn giá".
- **Độ ưu tiên:** Should

### FR-19 — Phân loại vật tư Nhập kho / Dịch vụ
- **Mô tả:** Mỗi vật tư thuộc một trong hai loại "Nhập kho" hoặc "Dịch vụ"; loại vật tư quyết định luồng mua. *(Mới v0.2 — nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md)*
- **Vai trò:** Quản trị hệ thống, Nhân viên MH
- **Truy vết:** US-01, US-25 · Màn hình: SCR-02, SCR-04
- **Input:** Loại sản phẩm trên form vật tư (chuẩn Odoo): Lưu kho = Nhập kho, Dịch vụ = Dịch vụ (AS-26).
- **Output:** Bộ lọc vật tư trên YCMH, Hợp đồng, Báo giá NCC, RFQ tạo trực tiếp; luồng nhận hàng có hoặc không có phiếu DO.
- **Business rules:**
  - BR-19.1: YCMH, Hợp đồng mua hàng, Báo giá NCC chỉ chọn được vật tư Nhập kho.
  - BR-19.2: Vật tư Dịch vụ không qua YCMH, không có hợp đồng, không tạo phiếu DO.
  - BR-19.3: RFQ tạo trực tiếp (không từ YCMH) chỉ chứa vật tư Dịch vụ (FR-25).
- **Acceptance criteria:**
  1. **Given** vật tư "[DV-005] Vệ sinh công nghiệp văn phòng" loại Dịch vụ **When** người tạo tìm vật tư trên dòng YCMH **Then** vật tư này không hiện trong danh sách.
  2. **Given** dòng hợp đồng chọn vật tư Dịch vụ **When** bấm "Lưu" **Then** hiện lỗi "Hợp đồng chỉ áp dụng cho vật tư Nhập kho".
- **Độ ưu tiên:** Must

### FR-20 — Danh mục Hợp đồng mua hàng
- **Mô tả:** Nhân viên MH lưu hợp đồng khung với NCC gồm vật tư, đơn giá, thời hạn hiệu lực; dùng để tạo YCMH (FR-22) và tự tra giá (FR-24). Xây trên Purchase Agreements loại Hợp đồng khung (AS-30). *(Mới v0.2 — nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md)*
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-22 · Màn hình: SCR-11
- **Input:** Số hợp đồng (bắt buộc, không trùng); Nhà cung cấp (bắt buộc); Hiệu lực từ, Hiệu lực đến (bắt buộc); Người phụ trách; Tham chiếu NCC; Tệp hợp đồng. Dòng: Vật tư (Nhập kho), Đơn vị tính, Đơn giá (> 0), Số lượng hợp đồng (tuỳ chọn).
- **Output:** Hợp đồng trạng thái Nháp → Đang hiệu lực → Hết hiệu lực; smart button "Yêu cầu mua hàng", "RFQ/Đơn mua hàng".
- **Business rules:**
  - BR-20.1: Chỉ vật tư Nhập kho (BR-19.1).
  - BR-20.2: Hiệu lực đến > Hiệu lực từ.
  - BR-20.3: Còn hiệu lực = trạng thái "Đang hiệu lực" và ngày hiện tại nằm trong [Hiệu lực từ, Hiệu lực đến] (AS-30).
  - BR-20.4: Tác vụ chạy hằng ngày 00:05 (AS-38) chuyển hợp đồng quá "Hiệu lực đến" sang "Hết hiệu lực".
  - BR-20.5: Không kiểm tra số lượng hợp đồng còn lại khi tạo YCMH hoặc tra giá (AS-30, OQ-26).
- **Acceptance criteria:**
  1. **Given** hợp đồng Nháp đủ thông tin, có 1 dòng đơn giá > 0 **When** bấm "Xác nhận" **Then** hợp đồng chuyển "Đang hiệu lực".
  2. **Given** Hiệu lực đến 31/12/2025, Hiệu lực từ 01/01/2026 **When** bấm "Lưu" **Then** hiện lỗi "Ngày kết thúc phải sau ngày bắt đầu".
  3. **Given** hợp đồng HĐ-HH-2025-03 có Hiệu lực đến 31/12/2025 **When** tác vụ hằng ngày chạy ngày 01/01/2026 **Then** hợp đồng chuyển "Hết hiệu lực".
- **Độ ưu tiên:** Must

### FR-21 — Danh mục Báo giá NCC
- **Mô tả:** Nhân viên MH lưu báo giá NCC gửi công ty gồm vật tư, đơn giá, hạn hiệu lực; dùng để tạo YCMH (FR-23). Model mới `purchase.vendor.quote` (AS-33). *(Mới v0.2 — nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md; _changes/20261020-074707.md quyết định #13)*
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-23, US-26 · Màn hình: SCR-12
- **Input:** Số báo giá (bắt buộc); Nhà cung cấp (bắt buộc); Ngày báo giá (bắt buộc); Hiệu lực đến (bắt buộc); Người nhận; Tệp báo giá (bắt buộc). Dòng: Vật tư (Nhập kho), Đơn vị tính, Đơn giá (> 0), Số lượng tối thiểu, Ghi chú.
- **Output:** Báo giá trạng thái Nháp → Còn hiệu lực → Hết hiệu lực; smart button "Yêu cầu mua hàng".
- **Business rules:**
  - BR-21.1: Chỉ vật tư Nhập kho (BR-19.1).
  - BR-21.2: Hiệu lực đến ≥ Ngày báo giá.
  - BR-21.3: Báo giá NCC không tham gia tự tra giá FR-24 (AS-33).
  - BR-21.4: Tác vụ hằng ngày 00:05 (AS-38) chuyển báo giá quá "Hiệu lực đến" sang "Hết hiệu lực".
  - BR-21.5 *(mới v0.3)*: Báo giá NCC cũng được tạo tự động từ email NCC trả lời (FR-26), có trường "RFQ liên quan"; báo giá mới của cùng NCC trên cùng RFQ chuyển báo giá cũ sang "Đã thay thế" (AS-46).
- **Acceptance criteria:**
  1. **Given** báo giá Nháp đủ thông tin, có tệp báo giá **When** bấm "Xác nhận" **Then** báo giá chuyển "Còn hiệu lực".
  2. **Given** báo giá chưa đính kèm tệp **When** bấm "Xác nhận" **Then** hiện lỗi "Vui lòng đính kèm file báo giá của NCC".
  3. **Given** báo giá BG-PV-1510 hiệu lực đến 15/11/2026 **When** tác vụ hằng ngày chạy ngày 16/11/2026 **Then** báo giá chuyển "Hết hiệu lực".
- **Độ ưu tiên:** Must

### FR-22 — Tạo Yêu cầu mua hàng từ Hợp đồng
- **Mô tả:** Từ một hợp đồng còn hiệu lực, người dùng bấm "Tạo yêu cầu mua hàng" để mở YCMH điền sẵn dòng của hợp đồng. *(Mới v0.2 — nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md)*
- **Vai trò:** Người đề xuất
- **Truy vết:** US-19 · Màn hình: SCR-11, SCR-02
- **Input:** Hợp đồng còn hiệu lực; số lượng từng dòng do người tạo nhập.
- **Output:** YCMH "Nháp" có Nguồn tạo = số hợp đồng; dòng chép từ hợp đồng; smart button "Hợp đồng".
- **Business rules:**
  - BR-22.1: Nút chỉ hiện khi hợp đồng còn hiệu lực (BR-20.3).
  - BR-22.2: Chép mọi dòng hợp đồng; Số lượng để trống; người tạo xoá dòng không cần (AS-36).
  - BR-22.3: NCC, đơn giá các dòng chép từ hợp đồng bị khoá; nguồn giá "Hợp đồng <số>".
  - BR-22.4: Được thêm dòng vật tư khác; dòng thêm tự tra giá theo FR-24.
  - BR-22.5: Người tạo, Bộ phận, số phiếu theo người bấm nút (FR-01).
- **Acceptance criteria:**
  1. **Given** hợp đồng HĐ-HH-2026-01 "Đang hiệu lực" có 2 dòng **When** bấm "Tạo yêu cầu mua hàng" **Then** mở YCMH Nháp có Nguồn tạo "Hợp đồng HĐ-HH-2026-01", 2 dòng NCC Hồng Hà, đơn giá theo hợp đồng, số lượng trống.
  2. **Given** dòng chép từ hợp đồng **When** người tạo bấm vào ô đơn giá **Then** ô không cho sửa.
  3. **Given** hợp đồng "Hết hiệu lực" **When** mở hợp đồng **Then** nút "Tạo yêu cầu mua hàng" không hiển thị.
- **Độ ưu tiên:** Must

### FR-23 — Tạo Yêu cầu mua hàng từ Báo giá NCC
- **Mô tả:** Từ một Báo giá NCC còn hiệu lực, người dùng bấm "Tạo yêu cầu mua hàng" để mở YCMH điền sẵn dòng của báo giá. *(Mới v0.2 — nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md)*
- **Vai trò:** Người đề xuất
- **Truy vết:** US-20 · Màn hình: SCR-12, SCR-02
- **Input:** Báo giá NCC "Còn hiệu lực"; số lượng từng dòng do người tạo nhập.
- **Output:** YCMH "Nháp" có Nguồn tạo = số báo giá; dòng chép từ báo giá; smart button "Báo giá NCC".
- **Business rules:**
  - BR-23.1: Nút chỉ hiện khi báo giá "Còn hiệu lực".
  - BR-23.2: Chép mọi dòng; số lượng để trống; NCC, đơn giá khoá; nguồn giá "Báo giá NCC <số>" (AS-36).
  - BR-23.3: Số lượng nhập nhỏ hơn "Số lượng tối thiểu" của dòng báo giá → cảnh báo, vẫn cho lưu.
- **Acceptance criteria:**
  1. **Given** báo giá BG-PV-1510 "Còn hiệu lực" có 2 dòng **When** bấm "Tạo yêu cầu mua hàng" **Then** mở YCMH Nháp có Nguồn tạo "Báo giá NCC BG-PV-1510", 2 dòng NCC Phong Vũ, đơn giá theo báo giá, số lượng trống.
  2. **Given** dòng Mực in HP 107A có số lượng tối thiểu 5 **When** người tạo nhập 3 **Then** hiện cảnh báo "Thấp hơn số lượng tối thiểu của báo giá (5)" và vẫn lưu được.
- **Độ ưu tiên:** Must

### FR-24 — Tự điền nhà cung cấp và đơn giá (Hợp đồng → Price List)
- **Mô tả:** Khi chọn vật tư trên dòng YCMH (không chép từ hợp đồng / báo giá), hệ thống tự điền NCC và đơn giá: ưu tiên hợp đồng còn hiệu lực, không có thì Price List. *(Mới v0.2 — nguồn: khao-sat-lan-2-yeu-cau-mua-hang.md)*
- **Vai trò:** Hệ thống, Người đề xuất
- **Truy vết:** US-21 · Màn hình: SCR-02
- **Input:** Vật tư, Đơn vị tính, Số lượng của dòng; ngày hiện tại.
- **Output:** Nhà cung cấp, Đơn giá, Nguồn giá ("Hợp đồng <số>", "Price List", "Nhập tay", "Không có").
- **Business rules:**
  - BR-24.1: Bước 1 — tìm dòng hợp đồng còn hiệu lực (BR-20.3) có vật tư này; có nhiều → đơn giá thấp nhất, bằng nhau → hợp đồng hết hạn sớm nhất (AS-31).
  - BR-24.2: Bước 2 — không có hợp đồng → Price List chuẩn Odoo theo thứ tự, số lượng tối thiểu, ngày hiệu lực (AS-31).
  - BR-24.3: Không có cả hai → NCC, đơn giá để trống, nguồn giá "Không có"; người tạo chọn NCC bằng tay (nguồn giá "Nhập tay").
  - BR-24.4: Giá từ hợp đồng bị khoá; giá từ Price List sửa được, sửa thì nguồn giá chuyển "Nhập tay" (AS-32).
  - BR-24.5: Tra lại khi đổi Vật tư, Đơn vị tính hoặc Số lượng; không tra lại sau khi phiếu đã gửi duyệt.
- **Acceptance criteria:**
  1. **Given** "Giấy A4 Double A 80gsm" có hợp đồng HĐ-HH-2026-01 còn hiệu lực giá 78.000₫ và Price List Thiên Long 79.000₫ **When** chọn vật tư **Then** dòng điền NCC Hồng Hà, 78.000₫, nguồn giá "Hợp đồng HĐ-HH-2026-01".
  2. **Given** "Bút bi Thiên Long TL-027" không có hợp đồng còn hiệu lực, Price List Hồng Hà 4.500₫ **When** chọn vật tư **Then** dòng điền NCC Hồng Hà, 4.500₫, nguồn giá "Price List".
  3. **Given** "Máy in HP LaserJet M211dw" không có hợp đồng và Price List **When** chọn vật tư **Then** NCC, đơn giá trống, nguồn giá "Không có".
  4. **Given** hợp đồng HĐ-HH-2025-03 hết hiệu lực là nguồn duy nhất của vật tư **When** chọn vật tư **Then** hệ thống bỏ qua hợp đồng đó và tra Price List.
- **Độ ưu tiên:** Must

### FR-25 — Mua Dịch vụ bằng PO trực tiếp
- **Mô tả:** Nhân viên MH tạo thẳng PO cho vật tư Dịch vụ trong Purchase, không YCMH, không Yêu cầu báo giá; bắt buộc tạo ĐNTT trước khi gửi duyệt; duyệt xong là PO, không tạo DO. *(Sửa v0.3 — nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md. v0.2: RFQ trực tiếp, có gửi email và chọn giá)*
- **Vai trò:** Nhân viên MH
- **Truy vết:** US-25 · Màn hình: SCR-03, SCR-04
- **Input:** NCC (bắt buộc); dòng vật tư Dịch vụ (Vật tư, Số lượng, Đơn giá, Ngày thực hiện dự kiến); Ngày dự kiến nhận hàng.
- **Output:** PO dịch vụ "Nháp" số theo FR-27; trạng thái Nháp → Chờ duyệt → PO.
- **Business rules:**
  - BR-25.1: Đơn tạo trực tiếp chỉ chứa vật tư Dịch vụ (BR-19.3).
  - BR-25.2 *(sửa v0.3)*: Không có bước "Send email", đọc báo giá, so sánh giá; statusbar không có bước "RFQ".
  - BR-25.3 *(mới v0.3)*: Bắt buộc ĐNTT trước khi "Approve" (FR-09, FR-11).
  - BR-25.4 *(sửa v0.3)*: Duyệt xong chuyển `PO`, không sinh phiếu DO (BR-13.5).
  - BR-25.5: Đơn dịch vụ không tính vào KPI "có YCMH làm gốc" (AS-02).
- **Acceptance criteria:**
  1. **Given** MH bấm "Mới" ở danh sách đơn mua, chọn NCC Sao Việt và vật tư "[DV-005] Vệ sinh công nghiệp văn phòng" **When** bấm "Lưu" **Then** PO dịch vụ MH-PO-0003-21-10-2026 "Nháp" được tạo, không có trường Yêu cầu mua hàng và không có nút "Send email".
  2. **Given** đơn tạo trực tiếp có dòng vật tư Nhập kho "Giấy A4 Double A 80gsm" **When** bấm "Lưu" **Then** hiện lỗi "Vật tư Nhập kho phải mua qua Yêu cầu mua hàng".
  3. **Given** PO dịch vụ chưa có ĐNTT **When** bấm "Approve" **Then** hiện lỗi "Phải tạo Đề nghị thanh toán trước khi gửi duyệt".
  4. **Given** PO dịch vụ "Chờ duyệt" **When** Trưởng phòng Mua hàng duyệt **Then** đơn chuyển "PO" và không có phiếu DO.
- **Độ ưu tiên:** Must

### FR-26 — Nhận email trả lời và đọc file Excel báo giá
- **Mô tả:** NCC reply email RFQ kèm file Excel; Odoo tự lưu email vào chatter RFQ, đính kèm file, đọc Excel lấy NCC – Vật tư – Đơn giá – Ngày giao và tạo Báo giá NCC gắn với RFQ. *(Mới v0.3 — nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md)*
- **Vai trò:** Hệ thống, Nhân viên MH
- **Truy vết:** US-26 · Màn hình: SCR-04, SCR-06
- **Input:** Email trả lời tới alias của RFQ; tệp `.xlsx` theo mẫu (AS-44).
- **Output:** Tin nhắn chatter kèm file; Báo giá NCC (FR-21) "Còn hiệu lực" có "RFQ liên quan" và dòng vật tư – giá; activity "Có báo giá mới" cho Nhân viên MH; lỗi đọc file ghi trên chatter.
- **Business rules:**
  - BR-26.1: Nhận email qua incoming mail server và alias của RFQ (AS-45); email trả lời ghép vào RFQ theo thread.
  - BR-26.2: NCC xác định theo email người gửi khớp danh sách NCC đã gửi (FR-06); không khớp → chatter ghi "Không xác định được NCC", không tạo báo giá, MH gán tay.
  - BR-26.3: Chỉ đọc file `.xlsx` theo mẫu, cột: Mã vật tư, Tên vật tư, ĐVT, Số lượng, Đơn giá, Ngày giao, Ghi chú; ghép dòng theo Mã vật tư của RFQ.
  - BR-26.4: Sai mẫu, thiếu cột, đơn giá không phải số hoặc mã vật tư không có trên RFQ → không tạo báo giá, chatter ghi lỗi kèm tên file và lý do; MH nhập tay (BR-08.5).
  - BR-26.5: Báo giá mới của cùng NCC → báo giá cũ "Đã thay thế" (AS-46).
  - BR-26.6: Giới hạn file theo NFR-10.
- **Acceptance criteria:**
  1. **Given** NCC Phong Vũ reply kèm `BaoGia_PhongVu.xlsx` đúng mẫu có 2 dòng **When** Odoo nhận email **Then** chatter RFQ có email trả lời và file, RFQ có báo giá NCC mới của Phong Vũ: Mực in HP 107A 765.000₫, Máy in HP LaserJet M211dw 6.990.000₫.
  2. **Given** Thế Giới Di Động trả lời kèm `BaoGia_TGDD.xlsx` thiếu cột "Đơn giá" **When** Odoo nhận email **Then** chatter ghi "Không đọc được BaoGia_TGDD.xlsx: thiếu cột Đơn giá" và không có báo giá mới.
  3. **Given** email trả lời từ địa chỉ không thuộc NCC đã gửi **When** Odoo nhận email **Then** chatter ghi "Không xác định được NCC" và không tạo báo giá.
  4. **Given** Phong Vũ gửi báo giá lần 2 **When** đọc xong **Then** báo giá lần 1 của Phong Vũ chuyển "Đã thay thế".
- **Độ ưu tiên:** Must

### FR-27 — Đánh số RFQ/PO và truy vết Yêu cầu mua hàng gốc
- **Mô tả:** RFQ/PO đánh số theo mẫu "Mã phòng ban-PO-XXXX-DD-MM-YYYY" (AS-42); RFQ hiển thị Mã Yêu cầu mua hàng gốc và lưu ngầm mã đó để truy vấn. *(Mới v0.3 — nguồn: khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #6)*
- **Vai trò:** Hệ thống, Người đề xuất, Nhân viên MH
- **Truy vết:** US-27 · Màn hình: SCR-03, SCR-04
- **Input:** YCMH gốc (nếu có); bộ phận; ngày.
- **Output:** Số RFQ/PO; trường "Mã Yêu cầu mua hàng" (chỉ đọc, bấm mở YCMH); trường ẩn `origin_request_code` lưu mã YCMH dạng text.
- **Business rules:**
  - BR-27.1: RFQ từ YCMH: `<Mã BP YCMH>-PO-<XXXX YCMH>-<DD>-<MM>-<YYYY>-<NN>`; NN là thứ tự RFQ của YCMH (01, 02…) (AS-42).
  - BR-27.2: PO dịch vụ: `<Mã BP người tạo>-PO-<XXXX>-<DD>-<MM>-<YYYY>`; XXXX đếm riêng theo bộ phận, về 0001 đầu năm (AS-42).
  - BR-27.3: Mã YCMH lưu ngầm không đổi khi YCMH bị huỷ hoặc đổi số; tìm kiếm danh sách RFQ/PO theo cả trường ẩn.
  - BR-27.4: Mã chuẩn Odoo của đơn (P00012…) không hiển thị.
- **Acceptance criteria:**
  1. **Given** YCMH HC_0012_20_10_26 có 2 NCC **When** BOD duyệt **Then** tạo 2 RFQ số HC-PO-0012-20-10-2026-01 (Hồng Hà) và HC-PO-0012-20-10-2026-02 (Phong Vũ), mỗi RFQ hiện "Mã Yêu cầu mua hàng" HC_0012_20_10_26.
  2. **Given** gõ "HC_0012" ở ô tìm kiếm danh sách RFQ **When** tìm **Then** hiện đúng 2 RFQ của YCMH đó.
  3. **Given** bộ phận MH đã có 2 PO dịch vụ năm 2026 **When** MH lưu PO dịch vụ mới ngày 21/10/2026 **Then** đơn nhận số MH-PO-0003-21-10-2026.
- **Độ ưu tiên:** Must

## 4. Yêu cầu phi chức năng

### NFR-01 — Hiệu năng
- **Yêu cầu:** Mở danh sách và form YCMH, đơn mua hàng, ĐNTT ≤ 2 giây ở p95 với 50 người dùng đồng thời và 20.000 đơn mua hàng/năm (AS-21). Tạo RFQ cho YCMH 50 dòng ≤ 5 giây.
- **Cách kiểm chứng:** Kiểm thử tải trên môi trường staging có dữ liệu giả lập tương đương.

### NFR-02 — Bảo mật và phân quyền
- **Yêu cầu:** Nhóm quyền mới: Người đề xuất, Trưởng nhóm, Nhân viên MH, BOD, Trưởng phòng Mua hàng, Kế toán ĐNTT, Quản trị mua hàng. Record rule: Người đề xuất chỉ đọc/sửa YCMH của mình; Trưởng nhóm đọc YCMH của thành viên nhóm; BOD đọc mọi YCMH; chỉ Nhân viên MH tạo, sửa Hợp đồng và Báo giá NCC *(sửa v0.2)*; chỉ Kế toán duyệt và ghi nhận thanh toán ĐNTT.
- **Cách kiểm chứng:** Kiểm thử ma trận quyền với 1 tài khoản mỗi nhóm.

### NFR-03 — Audit log
- **Yêu cầu:** Mọi thay đổi trạng thái, người duyệt, số tiền, đơn giá được tracking trên chatter kèm người và thời điểm. Không xoá được YCMH, đơn, ĐNTT đã rời trạng thái "Nháp"; chỉ huỷ.
- **Cách kiểm chứng:** Thực hiện trọn quy trình, kiểm tra chatter từng chứng từ; thử xoá chứng từ đã gửi.

### NFR-04 — Toàn vẹn dữ liệu
- **Yêu cầu:** Duyệt YCMH và tạo RFQ chạy trong một giao dịch; lỗi thì rollback toàn bộ. Hai người bấm duyệt đồng thời chỉ một thao tác thành công, thao tác còn lại nhận lỗi "Phiếu đã được cập nhật, vui lòng tải lại".
- **Cách kiểm chứng:** Kiểm thử tự động (unit test Odoo) cho tạo RFQ và duyệt đồng thời.

### NFR-05 — Khả dụng
- **Yêu cầu:** Hệ thống sẵn sàng 99,5% trong giờ làm việc 08:00–18:00, thứ 2–thứ 7 (AS-22).
- **Cách kiểm chứng:** Giám sát uptime hằng tháng.

### NFR-06 — Ngôn ngữ và định dạng
- **Yêu cầu:** Giao diện, email, mẫu in tiếng Việt; tiền VND `12.500.000₫`; ngày `dd/mm/yyyy`; múi giờ Asia/Ho_Chi_Minh.
- **Cách kiểm chứng:** Kiểm tra giao diện, email và PDF mẫu.

### NFR-07 — Tương thích trình duyệt
- **Yêu cầu:** Chrome và Edge 2 phiên bản mới nhất, màn hình ≥ 1366px (AS-23).
- **Cách kiểm chứng:** Kiểm thử thủ công trên 2 trình duyệt.

### NFR-08 — Gửi email
- **Yêu cầu:** Email gửi qua SMTP cấu hình sẵn; email lỗi hiện biểu tượng lỗi trên chatter và được cron chuẩn Odoo gửi lại; không chặn chuyển trạng thái. *(v0.3)* Hộp thư nhận báo giá đọc mỗi 5 phút; email trả lời gắn đúng RFQ ≥ 99% (đo trên 100 email thử).
- **Cách kiểm chứng:** Tắt SMTP tạm thời, gửi RFQ, kiểm tra trạng thái và hàng đợi email.

### NFR-09 — Khả năng bảo trì
- **Yêu cầu:** Toàn bộ tuỳ biến nằm trong module `purchase_flow_custom`, kế thừa model chuẩn, không sửa mã nguồn lõi; có unit test cho FR-01, FR-05, FR-08, FR-10, FR-11, FR-13, FR-24.
- **Cách kiểm chứng:** Code review; chạy test suite khi nâng cấp.

### NFR-10 — Xử lý file báo giá *(mới v0.3)*
- **Yêu cầu:** Chỉ nhận `.xlsx`, ≤ 5 MB, ≤ 500 dòng; đọc xong ≤ 60 giây sau khi email tới hộp thư; file khác định dạng bị từ chối và ghi chatter (AS-47). Không chạy macro, không mở file `.xlsm`.
- **Cách kiểm chứng:** Gửi 20 email thử với file đúng mẫu, sai mẫu, quá dung lượng; đo thời gian từ lúc email tới đến lúc có báo giá.

## 5. Tích hợp & dữ liệu

### 5.1 Hệ thống ngoài
| Hệ thống | Mục đích | Giao thức | Chiều | Tần suất | Xử lý lỗi |
|---|---|---|---|---|---|
| Approvals → Purchase | Tạo RFQ từ YCMH đã duyệt | ORM nội bộ Odoo | Approvals → Purchase | Realtime khi duyệt cấp cuối | Rollback giao dịch, hiện lỗi cho người duyệt |
| Purchase → Accounting | ĐNTT, payment | ORM nội bộ Odoo | Purchase → Accounting | Realtime | Validate trước khi lưu, hiện lỗi |
| Purchase → Inventory | Phiếu DO khi đơn được duyệt *(sửa v0.3)* | ORM nội bộ Odoo (`button_confirm`) | Purchase → Inventory | Realtime | Rollback, đơn giữ "Chờ duyệt" |
| Hộp thư đến (IMAP/POP) *(v0.3)* | Nhận email NCC trả lời kèm Excel | IMAP/TLS | NCC → Odoo | Cron đọc thư 5 phút | Thư không ghép được RFQ → hộp "Chưa xử lý", báo Nhân viên MH |
| Máy chủ SMTP | Email RFQ, thông báo | SMTP/TLS | Odoo → vendor, người dùng | Hàng đợi email Odoo, cron mỗi 5 phút | Gửi lại theo cron chuẩn; lỗi hiện trên chatter |

- Source of truth: CSDL Odoo cho mọi đối tượng.

### 5.2 API
| API | Method | Endpoint | Request chính | Response chính |
|---|---|---|---|---|
| Duyệt YCMH (mở rộng) | ORM | `approval.request.action_approve()` | id YCMH | YCMH đã cập nhật; gọi `_generate_rfqs()` khi duyệt cấp cuối |
| Tạo RFQ theo vendor | ORM | `approval.request._generate_rfqs()` | dòng YCMH | danh sách `purchase.order` mới |
| Gửi duyệt đơn | ORM | `purchase.order.action_submit_approval()` | id đơn | state `to approve`, danh sách cấp duyệt |
| Duyệt đơn | ORM | `purchase.order.action_approve_level()` | id đơn | state `approved` khi đủ cấp |
| Tạo ĐNTT | ORM | `purchase.order.action_create_payment_request()` | id đơn | form `purchase.payment.request` mới |
| Xác nhận nhận hàng | ORM | `purchase.order.action_confirm_receipt()` | id đơn | state `purchase`, `stock.picking` mới |
| Ghi nhận thanh toán | ORM | `purchase.payment.request.action_register_payment()` | sổ nhật ký, ngày | `account.payment` posted |
| Tra NCC và giá *(v0.2)* | ORM | `approval.product.line._compute_vendor_price()` | vật tư, ĐVT, số lượng, ngày | NCC, đơn giá, nguồn giá |
| Tạo YCMH từ Hợp đồng *(v0.2)* | ORM | `purchase.requisition.action_create_purchase_request()` | id hợp đồng | form `approval.request` mới |
| Tạo YCMH từ Báo giá NCC *(v0.2)* | ORM | `purchase.vendor.quote.action_create_purchase_request()` | id báo giá | form `approval.request` mới |
| Gửi email N NCC *(v0.3)* | ORM | `purchase.order.action_send_rfq_multi()` | id RFQ, danh sách NCC, tiêu đề, nội dung, tệp | N `mail.mail`, state `sent` |
| Nhận email trả lời *(v0.3)* | ORM | `purchase.order.message_update()` → `_parse_quote_excel()` | email, tệp .xlsx | `purchase.vendor.quote` mới hoặc lỗi trên chatter |
| So sánh / chọn NCC *(v0.3)* | ORM | `purchase.order.action_compare_quotes()`, `action_select_vendor_quote()` | id RFQ, id báo giá | bảng so sánh; RFQ đổi NCC và giá |
| Hết hiệu lực hợp đồng / báo giá *(v0.2)* | Cron | `_cron_expire_contracts_quotes()` | — | trạng thái Hết hiệu lực |

### 5.3 Mapping trường dữ liệu
| Nguồn | Đích | Kiểu | Ghi chú |
|---|---|---|---|
| `approval.request.name` | `purchase.order.approval_request_id` | many2one | Liên kết YCMH gốc (trường mới) |
| `approval.product.line.product_id` | `purchase.order.line.product_id` | many2one | |
| `approval.product.line.description` | `purchase.order.line.name` | text | |
| `approval.product.line.quantity` | `purchase.order.line.product_qty` | float | Quy đổi theo đơn vị tính mua |
| `approval.product.line.product_uom_id` | `purchase.order.line.product_uom` | many2one | |
| `approval.product.line.vendor_id` (mới) | `purchase.order.partner_id` | many2one | Khoá gộp RFQ (BR-05.1); tự điền theo FR-24 |
| `approval.product.line.price_unit` (mới, v0.2) | `purchase.order.line.price_unit` | monetary | BR-05.2 |
| `approval.product.line.price_source` (mới, v0.2) | — | selection | Hợp đồng / Báo giá NCC / Price List / Nhập tay / Không có |
| `approval.product.line.warehouse_id` (mới, v0.2) | `purchase.order.line.warehouse_id` (mới) → `stock.picking.picking_type_id` | many2one | Kho nhận; một phiếu DO mỗi kho (BR-13.4) |
| `approval.product.line.contract_line_id` (mới, v0.2) | `purchase.order.requisition_id` | many2one | BR-05.6 |
| `approval.request.source_document` (mới, v0.2) | — | reference | Hợp đồng hoặc Báo giá NCC nguồn |
| `purchase.requisition.line.price_unit` | `approval.product.line.price_unit` | monetary | Tạo từ hợp đồng / tra giá |
| `purchase.vendor.quote.line.price_unit` (model mới) | `approval.product.line.price_unit` | monetary | Tạo từ báo giá NCC |
| `approval.request.name` *(v0.3)* | `purchase.order.origin_request_code` (mới, ẩn) | char | Lưu ngầm mã YCMH (BR-27.3) |
| `approval.request.date_needed` *(v0.3)* | `purchase.order.date_expected_receipt` (mới) | date | Ngày dự kiến nhận hàng (AS-43) |
| `stock.picking.date_done` (DO cuối cùng) *(v0.3)* | `purchase.order.date_actual_receipt` (mới) | date | Ngày nhận hàng thực tế (BR-13.6) |
| Excel cột Mã vật tư, Đơn giá, Ngày giao *(v0.3)* | `purchase.vendor.quote.line.product_id`, `price_unit`, `date_planned` | many2one, monetary, date | FR-26; `purchase.vendor.quote.purchase_id` = RFQ |
| `purchase.vendor.quote.line.price_unit` (báo giá được chọn) *(v0.3)* | `purchase.order.line.price_unit` | monetary | FR-08 chọn NCC |
| `approval.request.date_needed` (mới) | `purchase.order.line.date_planned` | date | |
| `purchase.order.id` | `purchase.payment.request.purchase_id` | many2one | Model mới |
| `purchase.order.partner_id` | `purchase.payment.request.partner_id` | many2one | |
| `purchase.order.amount_total` | `purchase.payment.request.amount` | monetary | Giá trị mặc định, sửa được ≤ tổng |
| `purchase.payment.request.amount` | `account.payment.amount` | monetary | payment_type `outbound` |
| `purchase.order.line.product_qty` | `stock.move.product_uom_qty` | float | Sinh bởi `button_confirm` |

## 6. Screen Inventory

### 6.1 Danh sách màn hình
| SCR | Tên | Vai trò | Trường dữ liệu | Hành động | Trạng thái | FR | Loại |
|---|---|---|---|---|---|---|---|
| SCR-01 | Danh sách Yêu cầu mua hàng | Người đề xuất, Trưởng nhóm, Nhân viên MH, BOD | Số phiếu, Người tạo, Bộ phận, Ngày tạo, Nguồn tạo, Tổng dự kiến, Trạng thái | Mới, Tìm kiếm, Lọc, Nhóm theo | Mặc định, Rỗng | FR-01, FR-17 | backend |
| SCR-02 | Yêu cầu mua hàng | Người đề xuất, Trưởng nhóm, Nhân viên MH, BOD | Số phiếu, Người tạo, Bộ phận, Ngày tạo, Nguồn tạo, Ngày cần hàng, Ghi chú, Dòng (Vật tư, Đơn vị tính, Nhập kho, Số lượng, Nhà cung cấp, Đơn giá, Nguồn giá, Thành tiền, Ghi chú), Tổng dự kiến, Người duyệt 3 cấp và trạng thái duyệt, Tệp đính kèm | Gửi duyệt, Duyệt, Từ chối, Về nháp, Huỷ, RFQ/Đơn mua hàng, Hợp đồng | Nháp, Tạo từ Hợp đồng, Chờ duyệt cấp 2, Đã duyệt, Từ chối - nhập lý do, Bị từ chối - về Nháp, Lỗi validate | FR-01, FR-02, FR-03, FR-04, FR-17, FR-19, FR-22, FR-23, FR-24 | backend |
| SCR-03 | Danh sách RFQ và Đơn mua hàng | Nhân viên MH, Trưởng phòng Mua hàng | Số phiếu, Nhà cung cấp, Mã Yêu cầu mua hàng, Loại, Ngày dự kiến nhận hàng, Tổng tiền, Trạng thái | Mới, Tìm theo mã YCMH, Lọc Chờ tôi duyệt, Nhóm theo trạng thái | Mặc định, Rỗng | FR-10, FR-17, FR-25, FR-27 | backend |
| SCR-04 | RFQ và Đơn mua hàng | Nhân viên MH, Trưởng phòng Mua hàng | Số phiếu, Nhà cung cấp, Mã Yêu cầu mua hàng, Người tạo YCMH, Bộ phận, Ngày dự kiến nhận hàng, Ngày nhận hàng thực tế, Ghi chú, Dòng (Vật tư, Số lượng, Đơn vị tính, Nhập kho, Đơn giá, Nguồn giá, Ngày giao dự kiến, Thành tiền), Tổng tiền, Báo giá NCC, Duyệt, Lý do | Send email, So sánh giá, Tạo đề nghị thanh toán, Approve, Duyệt, Từ chối, Huỷ, Yêu cầu mua hàng, Báo giá NCC, Đề nghị thanh toán, Phiếu DO | Nháp, RFQ - đã nhận báo giá, Lỗi chưa có ĐNTT, Chờ duyệt, PO, PO dịch vụ | FR-06, FR-08, FR-09, FR-10, FR-11, FR-13, FR-15, FR-17, FR-19, FR-25, FR-26, FR-27 | backend |
| SCR-11 | Hợp đồng mua hàng | Nhân viên MH, Người đề xuất | Số hợp đồng, Nhà cung cấp, Loại, Hiệu lực từ, Hiệu lực đến, Người phụ trách, Tham chiếu NCC, Dòng (Vật tư, Đơn vị tính, Đơn giá, Số lượng hợp đồng, Đã đặt), Tệp hợp đồng | Tạo yêu cầu mua hàng, Xác nhận, Đóng hợp đồng, Yêu cầu mua hàng, RFQ/Đơn mua hàng | Đang hiệu lực, Hết hiệu lực | FR-20, FR-22 | backend |
| SCR-12 | Báo giá NCC | Nhân viên MH, Người đề xuất | Số báo giá, Nhà cung cấp, Ngày báo giá, Hiệu lực đến, Người nhận, Tệp báo giá, RFQ liên quan, Dòng (Vật tư, Đơn vị tính, Đơn giá, Số lượng tối thiểu, Ghi chú) | Tạo yêu cầu mua hàng, Xác nhận, Huỷ, Yêu cầu mua hàng | Còn hiệu lực, Hết hiệu lực | FR-21, FR-23, FR-26 | backend |
| SCR-05 | Gửi email yêu cầu báo giá | Nhân viên MH | Gửi đến (nhiều NCC, ngăn cách ";"), Tiêu đề, Nội dung (bảng sản phẩm), Tệp đính kèm (PDF RFQ, Excel mẫu báo giá), Mẫu email | Gửi, Huỷ | Mặc định, Lỗi NCC chưa có email, Đã gửi | FR-06 | backend |
| SCR-06 | So sánh giá | Nhân viên MH | Vật tư, Số lượng, NCC (cột), Đơn giá, Thành tiền, Tổng theo NCC, Ngày giao, Nhãn Giá thấp nhất / Tổng thấp nhất, Nguồn báo giá (Excel / nhập tay) | Chọn NCC này, Nhập tay báo giá, Đóng | Mặc định, Đã chọn NCC, Rỗng | FR-08, FR-26 | backend |
| SCR-07 | Danh sách Đề nghị thanh toán | Kế toán, Nhân viên MH | Mã, Đơn mua hàng, Vendor, Số tiền, Ngày đề nghị, Hình thức, Trạng thái | Lọc Chờ kế toán duyệt, Nhóm theo trạng thái, Tìm kiếm | Mặc định, Rỗng | FR-12 | backend |
| SCR-08 | Đề nghị thanh toán | Nhân viên MH, Kế toán | Mã, RFQ / Đơn mua hàng, Vendor, Số tiền, Ngày đề nghị, Hình thức thanh toán, Tài khoản ngân hàng, Nội dung, Tệp đính kèm, Thanh toán | Gửi kế toán, Duyệt, Từ chối, Ghi nhận thanh toán, Huỷ | Nháp, Lỗi validate, Chờ kế toán duyệt, Ghi nhận thanh toán, Đã thanh toán | FR-11, FR-12 | backend |
| SCR-09 | Phiếu DO - nhập kho | Thủ kho | Mã, Vendor, Chứng từ gốc, Ngày dự kiến, Kho nhận, Dòng (Sản phẩm, Số lượng yêu cầu, Số lượng thực nhận, Đơn vị tính) | Xác nhận, Tạo backorder, Không tạo backorder | Sẵn sàng, Nhận thiếu - backorder, Hoàn tất | FR-13, FR-14 | backend |
| SCR-10 | Cấu hình duyệt mua hàng | Quản trị hệ thống | Người duyệt đơn mua hàng, Mẫu email RFQ, Mẫu email từ chối, Mẫu file Excel báo giá, Hộp thư nhận báo giá | Lưu, Huỷ bỏ | Mặc định, Lỗi validate | FR-18 | backend |

### 6.2 Wireframe

#### SCR-01 — Danh sách Yêu cầu mua hàng
Danh sách YCMH nhóm theo trạng thái, bộ lọc mặc định theo vai trò. Điểm vào để tạo phiếu mới.

![SCR-01 — Danh sách Yêu cầu mua hàng](ui/png/SCR-01-danh-sach-yeu-cau-mua-hang.png)

#### SCR-02 — Yêu cầu mua hàng
Form YCMH: đầu phiếu theo khảo sát lần 2, dòng vật tư Nhập kho có kho nhận và nguồn giá tự điền, khối người duyệt 3 cấp. Nút hiển thị theo trạng thái và cấp duyệt. *(Sửa v0.2)*

![SCR-02 — Yêu cầu mua hàng](ui/png/SCR-02-yeu-cau-mua-hang.png)

#### SCR-03 — Danh sách RFQ và Đơn mua hàng
Danh sách RFQ và đơn mua hàng: Nháp → RFQ → Chờ duyệt → PO; cột Mã Yêu cầu mua hàng và Loại; tìm theo mã YCMH, lọc "Chờ tôi duyệt". *(Sửa v0.3)*

![SCR-03 — Danh sách RFQ và Đơn mua hàng](ui/png/SCR-03-danh-sach-don-mua-hang.png)

#### SCR-04 — RFQ và Đơn mua hàng
Form trung tâm: statusbar Nháp → RFQ → Chờ duyệt → PO (dịch vụ: Nháp → Chờ duyệt → PO); đầu phiếu kế thừa YCMH, có ngày dự kiến / thực tế nhận hàng và mã YCMH gốc; nút đổi theo trạng thái. *(Sửa v0.3)*

![SCR-04 — RFQ và Đơn mua hàng](ui/png/SCR-04-don-mua-hang.png)

#### SCR-05 — Gửi email yêu cầu báo giá
Popup "Send email": chọn nhiều NCC ngăn cách ";", soạn như email thường, hệ thống gửi riêng từng NCC; đính kèm PDF RFQ và Excel mẫu báo giá. *(Sửa v0.3)*

![SCR-05 — Gửi email yêu cầu báo giá](ui/png/SCR-05-gui-email-yeu-cau-bao-gia.png)

#### SCR-06 — So sánh báo giá
Bảng so sánh báo giá của các NCC trên cùng 1 RFQ (vật tư theo hàng, NCC theo cột), đánh dấu giá thấp nhất, chọn 1 NCC cho cả phiếu. *(Sửa v0.3)*

![SCR-06 — So sánh báo giá](ui/png/SCR-06-so-sanh-bao-gia.png)

#### SCR-07 — Danh sách Đề nghị thanh toán
Danh sách ĐNTT cho Kế toán, lọc mặc định "Chờ kế toán duyệt".

![SCR-07 — Danh sách Đề nghị thanh toán](ui/png/SCR-07-danh-sach-de-nghi-thanh-toan.png)

#### SCR-08 — Đề nghị thanh toán
Form ĐNTT gắn với một RFQ / đơn mua hàng, tạo trước khi gửi duyệt đơn; Kế toán duyệt và ghi nhận thanh toán. *(Sửa v0.3)*

![SCR-08 — Đề nghị thanh toán](ui/png/SCR-08-de-nghi-thanh-toan.png)

#### SCR-09 — Phiếu DO - nhập kho
Phiếu nhập kho tạo tự động khi đơn được duyệt; Thủ kho nhập số lượng thực nhận; hoàn tất thì cập nhật Ngày nhận hàng thực tế của đơn. *(Sửa v0.3)*

![SCR-09 — Phiếu DO - nhập kho](ui/png/SCR-09-phieu-do-nhap-kho.png)

#### SCR-10 — Cấu hình duyệt mua hàng
Trang Settings của Purchase: người duyệt đơn mua hàng (1 cấp), mẫu email, mẫu Excel báo giá, hộp thư nhận báo giá. *(Sửa v0.3 — bỏ ngưỡng)*

![SCR-10 — Cấu hình duyệt mua hàng](ui/png/SCR-10-cau-hinh-duyet-mua-hang.png)

#### SCR-11 — Hợp đồng mua hàng
Hợp đồng khung với NCC: vật tư, đơn giá, thời hạn hiệu lực; nút "Tạo yêu cầu mua hàng" khi còn hiệu lực. *(Mới v0.2)*

![SCR-11 — Hợp đồng mua hàng](ui/png/SCR-11-hop-dong-mua-hang.png)

#### SCR-12 — Báo giá NCC
Báo giá nhà cung cấp gửi công ty; nút "Tạo yêu cầu mua hàng" khi còn hiệu lực. *(Mới v0.2)*

![SCR-12 — Báo giá NCC](ui/png/SCR-12-bao-gia-ncc.png)

## 7. User flow

### 7.1 Luồng chính — Activity – Swimlane *(sửa v0.3)*

Quy trình vẽ lại theo yêu cầu khảo sát lần 3 (đặc tả `ui/swimlanes/*.json`, vẽ bằng `render-screens/scripts/swimlane.py`). Sơ đồ 1, 2: vật tư Nhập kho; sơ đồ 3: vật tư Dịch vụ.

![Swimlane 1 — Vật tư Nhập kho: Yêu cầu mua hàng](ui/diagrams/swimlane-01-yeu-cau-mua-hang.png)

![Swimlane 2 — Vật tư Nhập kho: Yêu cầu báo giá → PO → nhập kho](ui/diagrams/swimlane-02-yeu-cau-bao-gia-po.png)

![Swimlane 3 — Vật tư Dịch vụ: PO trực tiếp](ui/diagrams/swimlane-03-dich-vu.png)

### 7.2 Luồng từ chối *(sửa v0.3)*

```mermaid
flowchart TD
  A{SCR-02 Người duyệt YCMH} -- Từ chối và nhập lý do --> B[YCMH về Nháp, email cho người tạo]
  B --> C[Người tạo sửa, gửi lại]
  C --> A
  D{SCR-04 Trưởng phòng Mua hàng} -- Từ chối và nhập lý do --> E[Đơn Nhập kho về RFQ, dịch vụ về Nháp]
  E --> F[MH chọn lại NCC hoặc sửa, Approve lại]
  F --> D
  G{SCR-08 Kế toán} -- Từ chối và nhập lý do --> H[ĐNTT Từ chối, đơn Chờ duyệt về RFQ]
  H --> I[MH tạo ĐNTT mới]
  I --> G
```

### 7.3 Luồng nhận thiếu hàng

```mermaid
flowchart TD
  A[SCR-09 Phiếu DO Sẵn sàng] --> B{Số lượng thực nhận bằng yêu cầu?}
  B -- Có --> C[Xác nhận - Hoàn tất]
  B -- Không --> D{Tạo backorder?}
  D -- Có --> E[Hoàn tất phần đã nhận và tạo phiếu DO mới cho phần thiếu]
  D -- Không --> F[Hoàn tất phần đã nhận, đóng phần thiếu]
```

### 7.4 Luồng tạo Yêu cầu mua hàng và tự điền giá *(v0.2)*

```mermaid
flowchart TD
  A{Cách tạo YCMH} -- Trực tiếp --> B[SCR-02 Chọn vật tư Nhập kho]
  A -- Từ hợp đồng --> C[SCR-11 Hợp đồng còn hiệu lực - Tạo yêu cầu mua hàng]
  A -- Từ báo giá --> D[SCR-12 Báo giá NCC còn hiệu lực - Tạo yêu cầu mua hàng]
  C --> E[SCR-02 Dòng chép từ hợp đồng - NCC và giá khoá]
  D --> F[SCR-02 Dòng chép từ báo giá - NCC và giá khoá]
  B --> G{Có hợp đồng còn hiệu lực?}
  G -- Có --> H[Điền NCC và giá hợp đồng]
  G -- Không --> I{Có Price List?}
  I -- Có --> J[Điền NCC và giá Price List]
  I -- Không --> K[Người tạo chọn NCC bằng tay]
  E --> L[Nhập số lượng, kho nhận]
  F --> L
  H --> L
  J --> L
  K --> L
  L --> M{Trùng vật tư và NCC hoặc thiếu số lượng?}
  M -- Có --> N[SCR-02 Lỗi validate]
  M -- Không --> O[Gửi duyệt - Trưởng nhóm]
```

## 8. Ma trận truy vết

| FR | Tên | URD (US) | Màn hình (SCR) |
|---|---|---|---|
| FR-01 | Tạo và gửi Yêu cầu mua hàng | US-01 | SCR-01, SCR-02 |
| FR-02 | Duyệt Yêu cầu mua hàng 3 cấp | US-05, US-14, US-24 | SCR-02 |
| FR-03 | Từ chối và gửi lại Yêu cầu mua hàng | US-02, US-05, US-14, US-24 | SCR-02 |
| FR-04 | Huỷ Yêu cầu mua hàng | US-04 | SCR-02 |
| FR-05 | Tự động tạo RFQ gộp theo vendor | US-06 | Không có UI |
| FR-06 | Gửi email xin báo giá tới nhiều nhà cung cấp | US-07 | SCR-04, SCR-05 |
| FR-07 | Tạo RFQ thay thế cho vendor khác [Đã bỏ — v0.3] | US-08 | Không có UI (đã bỏ) |
| FR-08 | So sánh giá và chọn nhà cung cấp | US-09 | SCR-04, SCR-06 |
| FR-09 | Gửi duyệt đơn mua hàng | US-10 | SCR-04 |
| FR-10 | Duyệt hoặc từ chối đơn mua hàng | US-15 | SCR-03, SCR-04 |
| FR-11 | Tạo Đề nghị thanh toán trước khi gửi duyệt | US-11 | SCR-04, SCR-08 |
| FR-12 | Kế toán xử lý Đề nghị thanh toán | US-16 | SCR-07, SCR-08 |
| FR-13 | Duyệt xong chuyển PO và tự tạo phiếu DO | US-12, US-25 | SCR-04, SCR-09 |
| FR-14 | Nhập kho theo phiếu DO | US-17 | SCR-09 |
| FR-15 | Huỷ RFQ và đơn mua hàng | US-13 | SCR-04 |
| FR-16 | Thông báo và activity | US-05, US-14, US-15, US-16, US-24 | Không có UI |
| FR-17 | Truy vết và tra cứu chứng từ | US-03 | SCR-01, SCR-02, SCR-03, SCR-04, SCR-11, SCR-12 |
| FR-18 | Cấu hình người duyệt, mẫu email và mẫu báo giá | US-18 | SCR-10 |
| FR-19 | Phân loại vật tư Nhập kho / Dịch vụ | US-01, US-25 | SCR-02, SCR-04 |
| FR-20 | Danh mục Hợp đồng mua hàng | US-22 | SCR-11 |
| FR-21 | Danh mục Báo giá NCC | US-23, US-26 | SCR-12 |
| FR-22 | Tạo Yêu cầu mua hàng từ Hợp đồng | US-19 | SCR-11, SCR-02 |
| FR-23 | Tạo Yêu cầu mua hàng từ Báo giá NCC | US-20 | SCR-12, SCR-02 |
| FR-24 | Tự điền nhà cung cấp và đơn giá (Hợp đồng → Price List) | US-21 | SCR-02 |
| FR-25 | Mua Dịch vụ bằng PO trực tiếp | US-25 | SCR-03, SCR-04 |
| FR-26 | Nhận email trả lời và đọc file Excel báo giá | US-26 | SCR-04, SCR-06 |
| FR-27 | Đánh số RFQ/PO và truy vết Yêu cầu mua hàng gốc | US-27 | SCR-03, SCR-04 |

## 9. Assumptions & Open Questions

### 9.1 Giả định
| Mã | Giả định | Lý do chọn | Liên quan |
|---|---|---|---|
| AS-01 | Odoo 17 Enterprise, on-premise hoặc Odoo.sh, cho phép module tuỳ biến — **xác nhận v0.3** (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #1) | Approvals là module Enterprise; cần code tuỳ biến | Toàn hệ thống, NFR-09 |
| AS-02 | KPI *(sửa v0.2)*: 100% đơn mua vật tư Nhập kho có YCMH đã duyệt làm gốc và lịch sử duyệt trên chatter | Input chưa có KPI | Mục 1 |
| AS-03 | **[Đã thay — v0.2]** ~~YCMH duyệt tuần tự MH → Trưởng phòng~~. Khảo sát lần 2 xác nhận Trưởng nhóm → MH → BOD; chi tiết AS-34 | khao-sat-lan-2-yeu-cau-mua-hang.md | FR-02, SCR-02 |
| AS-04 | **[Đã thay — v0.2]** ~~Vendor trên dòng → bảng giá NCC; thiếu thì chặn duyệt cấp 1~~. Khảo sát lần 2: Hợp đồng → Price List; chi tiết AS-30, AS-31, AS-32 | khao-sat-lan-2-yeu-cau-mua-hang.md | FR-02, FR-05, FR-24 |
| AS-05 | Mỗi YCMH sinh RFQ riêng theo vendor, không gộp với YCMH khác — **xác nhận v0.3** (tra-loi-cau-hoi-mo-lan-1.md) | Giữ truy vết 1 YCMH → n RFQ | FR-05 |
| AS-06 | **[Đã thay — v0.3]** ~~Hỏi giá nhiều vendor bằng RFQ thay thế (Alternatives)~~. Giữ 1 RFQ, gửi email riêng tới N NCC (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #8) | Tính năng chuẩn Odoo | FR-07, SCR-04 |
| AS-07 | **[Đã thay — v0.3]** ~~Chọn giá theo dòng; RFQ không được chọn tự huỷ~~. Chọn 1 NCC cho cả phiếu, RFQ đổi NCC và giá (_changes/20261020-093008.md #8) | Linh hoạt chọn vendor theo sản phẩm | FR-08, SCR-06 |
| AS-08 | **[Đã thay — v0.3]** ~~Trưởng phòng Mua hàng duyệt mọi đơn; tổng ≥ 50.000.000₫ thêm Giám đốc~~. Không có ngưỡng (tra-loi-cau-hoi-mo-lan-1.md); người duyệt: AS-39 | Thông lệ phân cấp duyệt | FR-09, FR-10, FR-18 |
| AS-09 | *(Sửa v0.3)* Từ chối bắt buộc lý do. YCMH bị từ chối về Nháp và gửi email cho người tạo (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #6); đơn mua hàng về RFQ (dịch vụ: Nháp); ĐNTT: AS-41 | Không mất dữ liệu đã nhập | FR-03, FR-10 |
| AS-10 | ĐNTT là chứng từ mới gắn 1 đơn; là khoản trả trước, thanh toán đủ số tiền đề nghị | Input chỉ nêu tên chứng từ | FR-11, FR-12, SCR-08 |
| AS-11 | **[Đã thay — v0.3]** ~~Đơn chuyển Waiting PO khi ĐNTT được gửi kế toán~~. Bỏ Waiting PO; ĐNTT tạo trước khi gửi duyệt (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3) | Theo input | FR-11 |
| AS-12 | Phiếu DO = phiếu nhập kho (Receipt), tạo "Sẵn sàng"; Thủ kho xác nhận; nhận thiếu tạo backorder | Thuật ngữ DO chưa rõ; v0.2: khảo sát lần 2 nhắc "phiếu Nhập kho" cho vật tư Nhập kho | FR-13, FR-14, SCR-09 |
| AS-13 | Vendor phải có email mới gửi được RFQ | Gửi RFQ qua email | FR-06, SCR-05 |
| AS-14 | Huỷ YCMH trước khi duyệt xong; huỷ đơn trước PO và khi chưa thanh toán | Tránh huỷ chứng từ đã phát sinh kho/tiền | FR-04, FR-15 |
| AS-15 | Hoá đơn nhà cung cấp dùng chuẩn Odoo, ngoài phạm vi | Input không đề cập | FR-12 |
| AS-16 | **[Đã thay — v0.3]** ~~MH nhập giá vendor thủ công vào RFQ~~. Hệ thống đọc Excel từ email NCC reply; nhập tay khi file lỗi (khao-sat-lan-3-yeu-cau-bao-gia.md; AS-45) | Không có cổng vendor | FR-08 |
| AS-17 | Chỉ dùng VND | Input không đề cập ngoại tệ | NFR-06 |
| AS-18 | Thông báo qua activity Odoo + email | Kênh chuẩn Odoo | FR-16 |
| AS-19 | *(Sửa v0.2)* Dòng YCMH bắt buộc vật tư Nhập kho, đơn vị tính, kho nhận, số lượng > 0 (không để trống — khảo sát lần 2 xác nhận); ngày cần hàng không bắt buộc, đã nhập thì ≥ hôm nay | Dữ liệu tối thiểu để tạo RFQ | FR-01 |
| AS-20 | *(Sửa v0.2)* Mã tự động: YCMH theo AS-28 (thay `YCMH/<năm>/<4 số>`), `DNTT/<năm>/<4 số>`; RFQ/đơn dùng mã chuẩn `P<5 số>` | Quy ước sequence Odoo | FR-01, FR-11 |
| AS-21 | Quy mô: 50 người dùng đồng thời, 20.000 đơn mua hàng/năm | Input chưa có số liệu | NFR-01 |
| AS-22 | Khả dụng 99,5% giờ làm việc 08:00–18:00, thứ 2–thứ 7 | Thông lệ hệ thống nội bộ | NFR-05 |
| AS-23 | Trình duyệt Chrome/Edge 2 phiên bản mới nhất, màn hình ≥ 1366px | Thông lệ Odoo backend | NFR-07 |
| AS-24 | Activity duyệt/xử lý có hạn 1 ngày làm việc | Input chưa có SLA xử lý | FR-01, FR-16 |
| AS-25 | Lý do từ chối/huỷ tối thiểu 10 ký tự | Tránh lý do rỗng nghĩa | FR-03, FR-10, FR-12, FR-15 |
| AS-26 | Vật tư "Nhập kho" = sản phẩm loại Lưu kho (storable) của Odoo; vật tư "Dịch vụ" = sản phẩm loại Dịch vụ; không dùng loại Tiêu dùng | Khảo sát lần 2 chỉ nêu 2 loại | FR-19 |
| AS-27 | **[Đã thay — v0.3]** ~~Đơn dịch vụ dùng chung nút "Xác nhận đã nhận hàng"~~. Đơn dịch vụ duyệt xong là PO, không có bước nhận hàng (khao-sat-lan-3-yeu-cau-bao-gia.md) | Giữ một luồng trạng thái cho mọi đơn | FR-13, FR-25 |
| AS-28 | Số phiếu YCMH = `<Mã BP>_<XXXX>_<DD>_<MM>_<YY>`: Mã BP là mã bộ phận của người tạo; XXXX đếm riêng theo bộ phận, về 0001 đầu mỗi năm; DD_MM_YY là ngày tạo (vd. `HC_0012_20_10_26`) | Mẫu số phiếu chưa nói cách đếm XXXX | FR-01 |
| AS-29 | Kho nhận (cột "Nhập kho") mặc định là kho chính của công ty, người tạo sửa được theo từng dòng; một đơn mua sinh một phiếu DO cho mỗi kho nhận | Một YCMH có nhiều kho (người làm chốt); Odoo chuẩn nhận mỗi đơn vào một kho | FR-01, FR-05, FR-13 |
| AS-30 | Hợp đồng = Purchase Agreement loại Hợp đồng khung (Blanket Order); còn hiệu lực khi trạng thái "Đang hiệu lực" và ngày hiện tại nằm trong khoảng hiệu lực; không kiểm tra số lượng còn lại | Tính năng chuẩn Odoo, có NCC, đơn giá, ngày hiệu lực | FR-20, FR-22, FR-24 |
| AS-31 | Nhiều hợp đồng còn hiệu lực cùng vật tư → chọn đơn giá thấp nhất, bằng nhau thì hợp đồng hết hạn sớm nhất. Price List chọn theo quy tắc chuẩn Odoo (thứ tự, số lượng tối thiểu, hiệu lực) | Input chưa có tiêu chí chọn | FR-24 |
| AS-32 | Giá lấy từ hợp đồng bị khoá; giá từ Price List sửa được; không có nguồn giá thì người tạo nhập tay NCC (đơn giá tuỳ chọn). Mọi dòng phải có NCC trước khi Nhân viên MH duyệt cấp 2 | Bảo đảm tạo được RFQ theo NCC | FR-02, FR-24 |
| AS-33 | Báo giá NCC là danh mục mới (NCC, ngày báo giá, hiệu lực đến, dòng vật tư – đơn giá); không tham gia tự tra giá; hết hiệu lực thì không tạo được YCMH | Quy tắc tra giá chỉ nêu Hợp đồng và Price List | FR-21, FR-23 |
| AS-34 | Trưởng nhóm = quản lý trực tiếp (Manager) trên hồ sơ nhân viên của người tạo; người tạo chưa có Trưởng nhóm thì chặn gửi duyệt. BOD = nhóm quyền "BOD", một thành viên duyệt là đủ | Input chỉ nêu "Trưởng nhóm (theo người tạo)" và "BOD" | FR-02 |
| AS-35 | Đầu phiếu giữ "Ngày cần hàng" (không bắt buộc, làm ngày dự kiến trên RFQ); "Lý do mua" bỏ, thay bằng "Ghi chú" (không bắt buộc) | Khảo sát lần 2 không nhắc 2 trường này | FR-01 |
| AS-36 | Tạo YCMH từ Hợp đồng / Báo giá NCC: chép mọi dòng, số lượng để trống cho người tạo nhập, dòng không cần thì xoá; NCC và đơn giá khoá theo chứng từ nguồn; được thêm dòng vật tư khác (tự tra giá) | Input chưa mô tả chi tiết | FR-22, FR-23 |
| AS-37 | Giữ cả hai lớp duyệt: YCMH (Trưởng nhóm → MH → BOD) và đơn mua hàng sau chọn giá (AS-08) cho tới khi khảo sát phiếu tiếp theo | Khảo sát lần 2 mới đi chi tiết phiếu YCMH | FR-09, FR-10 |
| AS-38 | Tác vụ chuyển Hợp đồng / Báo giá NCC sang "Hết hiệu lực" chạy hằng ngày lúc 00:05 | Ngoài giờ làm việc, trước khi người dùng tra giá | FR-20, FR-21 |
| AS-39 | Đơn mua hàng duyệt 1 cấp bởi Trưởng phòng Mua hàng, không phân ngưỡng giá trị | tra-loi-cau-hoi-mo-lan-1.md: không có ngưỡng; người duyệt chưa nói | FR-10, FR-18 |
| AS-40 | Gửi duyệt đơn yêu cầu ĐNTT đã gửi Kế toán (trạng thái "Chờ kế toán duyệt" trở lên); không cần Kế toán duyệt xong | khao-sat-lan-3-yeu-cau-bao-gia.md chỉ nói "bắt buộc tạo ĐNTT trước" | FR-09, FR-11 |
| AS-41 | ĐNTT bị Kế toán từ chối: đơn đang Chờ duyệt về RFQ (dịch vụ: Nháp); đơn đã PO giữ PO; MH tạo ĐNTT mới | Input chưa nói | FR-12 |
| AS-42 | Số RFQ/PO = `<Mã BP>-PO-<XXXX>-<DD>-<MM>-<YYYY>-<NN>`: Mã BP, XXXX, ngày lấy từ YCMH gốc, NN là thứ tự RFQ trong YCMH (vd. `HC-PO-0012-20-10-2026-02`). PO dịch vụ: `<Mã BP người tạo>-PO-<XXXX>-<DD>-<MM>-<YYYY>`, XXXX đếm riêng (vd. `MH-PO-0003-21-10-2026`). Mã YCMH gốc lưu ngầm ở trường ẩn | Mẫu ở khao-sat-lan-3-yeu-cau-bao-gia.md; mục tiêu truy vết RFQ → YCMH (_changes/20261020-093008.md #6) | FR-27 |
| AS-43 | Ngày dự kiến nhận hàng mặc định = Ngày cần hàng của YCMH (trống thì ngày tạo RFQ + 7 ngày), MH sửa được; Ngày nhận hàng thực tế = ngày hoàn tất phiếu DO cuối cùng của đơn, chỉ đọc | Input chưa nói cách lấy ngày | FR-05, FR-13 |
| AS-44 | Email xin báo giá có bảng sản phẩm của phiếu trong nội dung, đính kèm PDF RFQ và file Excel mẫu báo giá (Mã vật tư, Tên vật tư, ĐVT, Số lượng, Đơn giá, Ngày giao, Ghi chú) | Muốn tự đọc Excel thì cần mẫu cố định | FR-06, FR-26 |
| AS-45 | Odoo nhận reply qua incoming mail server và alias của RFQ; NCC xác định theo email người gửi; file sai mẫu thì MH nhập tay báo giá | Cơ chế mail gateway chuẩn của Odoo | FR-26, FR-08 |
| AS-46 | Kết quả đọc Excel lưu thành Báo giá NCC (FR-21) gắn với RFQ; báo giá mới của cùng NCC thay báo giá cũ ("Đã thay thế") | Tận dụng danh mục Báo giá NCC đã có | FR-21, FR-26 |
| AS-47 | File báo giá chỉ nhận .xlsx, ≤ 5 MB, ≤ 500 dòng; đọc xong ≤ 60 giây sau khi email tới | Giới hạn an toàn khi xử lý file đính kèm | NFR-10 |

### 9.2 Câu hỏi mở
| Mã | Câu hỏi | Người cần trả lời | Ảnh hưởng tới |
|---|---|---|---|
| OQ-01 | **Đã trả lời (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #1):** Odoo 17 bản trả phí, Odoo.sh hoặc on-premise, cài được module tuỳ biến | IT khách hàng | Toàn hệ thống, NFR-09 |
| OQ-02 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md):** quy trình hiện tại làm thủ công, cần cải thiện. Còn mở: các bước hiện tại và chỉ số đo được | Khách hàng | Mục 1 |
| OQ-03 | KPI, giá trị mục tiêu và mốc go-live? | Khách hàng | Mục 1 |
| OQ-04 | **Đã trả lời (khao-sat-lan-2-yeu-cau-mua-hang.md):** duyệt tuần tự Trưởng nhóm (theo người tạo) → User MH → BOD | Khách hàng | FR-02, SCR-02 |
| OQ-05 | **Đã trả lời một phần (khao-sat-lan-2-yeu-cau-mua-hang.md):** Hợp đồng còn hiệu lực → Price List. Còn mở: không có cả hai thì xử lý thế nào → OQ-28 | Phòng Mua hàng | FR-02, FR-05, FR-24 |
| OQ-06 | **Đã trả lời (tra-loi-cau-hoi-mo-lan-1.md):** không cho phép gộp nhiều YCMH cùng vendor vào một RFQ | Phòng Mua hàng | FR-05 |
| OQ-07 | **Đã trả lời một phần (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #8):** 1 RFQ gửi email riêng tới N NCC; chọn 1 NCC cho cả phiếu. Còn mở: số NCC tối thiểu / tối đa (OQ-39) | Phòng Mua hàng | FR-07, FR-08, SCR-06 |
| OQ-08 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md):** đơn mua hàng không có ngưỡng giá trị. Còn mở: ai duyệt đơn (AS-39) | Ban giám đốc | FR-10, FR-18 |
| OQ-09 | **Đã trả lời một phần (tra-loi-cau-hoi-mo-lan-1.md; _changes/20261020-084051.md #6):** YCMH bị từ chối về Nháp và gửi email cho người tạo. Còn mở: đơn mua hàng và ĐNTT bị từ chối | Khách hàng | FR-03, FR-10 |
| OQ-10 | ĐNTT là tạm ứng trước khi nhận hàng hay thanh toán theo hoá đơn? Ai duyệt? Có thanh toán một phần không? | Kế toán | FR-11, FR-12, SCR-08 |
| OQ-11 | **Đã trả lời (khao-sat-lan-3-yeu-cau-bao-gia.md; _changes/20261020-093008.md #3):** bỏ Waiting PO; ĐNTT tạo trước khi duyệt, duyệt xong là PO + DO, không chờ thanh toán | Kế toán / Mua hàng | FR-11, FR-13 |
| OQ-12 | "Phiếu DO" là phiếu gì? Tự hoàn tất nhập kho hay Thủ kho xác nhận? | Kho | FR-13, FR-14, SCR-09 |
| OQ-13 | Hoá đơn nhà cung cấp và đối chiếu có trong dự án không? | Kế toán | FR-12 |
| OQ-14 | Số người dùng và số YCMH, đơn mua hàng mỗi tháng? | Khách hàng | NFR-01 |
| OQ-15 | Có mẫu email / mẫu in RFQ, ĐNTT theo mẫu công ty không? | Phòng Mua hàng | FR-06, FR-18, SCR-05 |
| OQ-16 | **Đã trả lời (khao-sat-lan-3-yeu-cau-bao-gia.md):** NCC reply email kèm file Excel báo giá; không cần cổng vendor | Phòng Mua hàng | FR-08 |
| OQ-17 | Có mua hàng bằng ngoại tệ không? | Kế toán | NFR-06 |
| OQ-18 | Ngoài activity và email, có cần kênh thông báo khác (Zalo, SMS) không? | Khách hàng | FR-16 |
| OQ-19 | Quy tắc đánh mã YCMH, ĐNTT theo mẫu công ty? | Kế toán | FR-01, FR-11 |
| OQ-20 | Yêu cầu khả dụng, giờ làm việc và trình duyệt chuẩn của công ty? | IT khách hàng | NFR-05, NFR-07 |
| OQ-21 | Thời hạn xử lý mỗi bước duyệt? Quá hạn có nhắc hoặc chuyển cấp không? Quy định về nội dung lý do từ chối? | Khách hàng | FR-03, FR-16 |
| OQ-22 | Vật tư "Nhập kho" ứng với loại sản phẩm nào trong Odoo? Có dùng loại Tiêu dùng (consumable) không? | IT khách hàng | FR-19 |
| OQ-23 | **Đã trả lời một phần (khao-sat-lan-3-yeu-cau-bao-gia.md):** đơn dịch vụ duyệt xong là PO, không tạo DO, không có bước nhận hàng. Còn mở: có cần nghiệm thu dịch vụ không | Phòng Mua hàng | FR-13, FR-25 |
| OQ-24 | XXXX trong số phiếu đếm theo bộ phận hay toàn công ty? Về 0001 theo năm, tháng hay ngày? Mã BP lấy ở đâu? | Kế toán / IT | FR-01 |
| OQ-25 | Kho nhận mặc định của dòng là kho nào? Bộ phận nào được chọn kho nào? | Kho | FR-01, FR-13 |
| OQ-26 | Hợp đồng có giới hạn số lượng / giá trị không? Có trừ luỹ kế và chặn khi vượt không? | Phòng Mua hàng | FR-20, FR-24 |
| OQ-27 | Nhiều hợp đồng hoặc nhiều dòng Price List cùng vật tư thì chọn theo tiêu chí nào? | Phòng Mua hàng | FR-24 |
| OQ-28 | Người tạo được sửa NCC và đơn giá hệ thống tự điền không? Không có cả hợp đồng lẫn Price List thì xử lý thế nào? | Phòng Mua hàng | FR-02, FR-24 |
| OQ-29 | Báo giá NCC có tham gia tự tra giá không? Ai nhập báo giá, có cần duyệt không? | Phòng Mua hàng | FR-21, FR-23 |
| OQ-30 | Người tạo không có Trưởng nhóm thì xử lý thế nào? BOD cần một hay tất cả thành viên duyệt? Có phân ngưỡng giá trị không? | Ban giám đốc | FR-02 |
| OQ-31 | Có cần "Ngày cần hàng" và "Lý do mua" trên đầu phiếu không? | Khách hàng | FR-01 |
| OQ-32 | Tạo YCMH từ Hợp đồng / Báo giá: chép mọi dòng hay chọn dòng? Có được thêm vật tư ngoài chứng từ nguồn không? | Phòng Mua hàng | FR-22, FR-23 |
| OQ-33 | BOD đã duyệt YCMH thì đơn mua hàng sau khi chọn giá còn cần duyệt nữa không? | Ban giám đốc | FR-09, FR-10 |
| OQ-34 | Gửi duyệt đơn chỉ cần tạo / gửi ĐNTT, hay phải chờ Kế toán duyệt ĐNTT? | Kế toán / Mua hàng | FR-09, FR-11 |
| OQ-35 | ĐNTT bị Kế toán từ chối thì đơn mua hàng xử lý thế nào? | Kế toán | FR-12 |
| OQ-36 | Mẫu "Mã phòng ban-PO-XXXX-DD-MM-YYYY": XXXX và ngày lấy từ YCMH hay đếm riêng? 1 YCMH sinh nhiều RFQ thì phân biệt thế nào? PO dịch vụ đánh số ra sao? Mẫu này khác mẫu số YCMH "Mã BP_XXXX_DD_MM_YY" — có thống nhất không? | Kế toán / Mua hàng | FR-27, FR-01 |
| OQ-37 | Nhận nhiều đợt (backorder) thì "Ngày nhận hàng thực tế" lấy ngày nào? | Kho | FR-13 |
| OQ-38 | Mẫu file Excel báo giá do ai cung cấp, gồm cột nào? NCC không dùng mẫu thì xử lý ra sao? Hộp thư nhận báo giá là địa chỉ nào? | Phòng Mua hàng / IT | FR-26 |
| OQ-39 | Một RFQ được hỏi giá tối đa bao nhiêu NCC? Có bắt buộc đủ số báo giá tối thiểu trước khi chọn NCC không? | Phòng Mua hàng | FR-06, FR-08 |
