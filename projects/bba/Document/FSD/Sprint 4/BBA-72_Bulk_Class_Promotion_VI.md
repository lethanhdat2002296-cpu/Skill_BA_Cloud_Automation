# Bulk Class Promotion

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Classes |
| Tính năng | BBA-72 Bulk Class Promotion |
| Mã tài liệu | FRD-3.1.5.01_Bulk_Class_Promotion |
| Sprint | 4 |
| Phiên bản | 0.1 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 10/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Năm học chạy từ tháng 1 đến tháng 12. Tháng 11–12, Centre lập lớp của năm sau (tạo lớp, gán giáo viên). Cuối năm, người dùng chuyển toàn bộ trẻ của một lớp lên lớp ở level kế tiếp (ví dụ N2 lên K1) đã lập sẵn, trong một lần thao tác thay vì chuyển từng trẻ. Lớp cũ và danh sách trẻ của lớp cũ vẫn được giữ.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Lên lớp cả lớp trong cùng Centre (annual promotion): chọn lớp đích đã có của năm học mới và ngày hiệu lực; chọn toàn bộ trẻ, bỏ chọn trẻ ở lại; xác nhận; kết quả từng trẻ; lịch sử. | Tác động của việc lên lớp tới học phí, hoá đơn, thread tin nhắn, danh sách điểm danh (thuộc module liên quan). Tạo lớp (Classes). Infant lên Playgroup theo tuổi 18 tháng (Infant promotion) và đổi lớp cùng level (Class change). K2 tốt nghiệp (Joining & leaving › Graduation). Chuyển Centre (Transfer). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Lớp và trẻ của Centre được cấp. | Lên lớp cả lớp |
| System | Lớp nguồn, lớp đích, trẻ được chọn. | Chuyển trẻ sang lớp đích từ ngày hiệu lực, báo kết quả, lưu lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo Roles & permissions và phạm vi dữ liệu. Quyền tạo lớp thuộc Classes, không thuộc tính năng này.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Classes** | Chuyển cả lớp lên level mới | Từ chi tiết lớp chọn Move children up; chọn lớp đích và ngày hiệu lực; chọn toàn bộ trẻ, bỏ chọn trẻ ở lại; xác nhận; xem kết quả từng trẻ. | BBA-72: US-001 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-72: US-001 - Chuyển cả lớp lên level mới

#### User Story

Là người dùng, tôi muốn chuyển toàn bộ trẻ của một lớp lên lớp ở level kế tiếp của năm học mới trong một lần thao tác, để không phải chuyển từng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Người dùng có quyền mở luồng lên lớp từ chi tiết lớp (BR-001, BR-002). |
| FR-002 | Người dùng chọn lớp mới trong các lớp đã tạo sẵn và chọn ngày hiệu lực (BR-003, BR-004, BR-005; VAL-001). |
| FR-003 | Hệ thống liệt kê toàn bộ trẻ của lớp hiện tại của trẻ, mặc định chọn tất cả; người dùng bỏ chọn trẻ ở lại (BR-006; VAL-002). |
| FR-004 | Người dùng xác nhận; hệ thống chuyển trẻ được chọn sang lớp mới (BR-007, BR-008, BR-009). |
| FR-005 | Hệ thống hiển thị kết quả số lượng trẻ được chuyển lên lớp (BR-010). |
| FR-006 | Hệ thống ghi lịch sử cho từng trẻ và cho lớp (DATA-001, DATA-002). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở lớp, chọn Edit › Move children up (FR-001).
2. Người dùng chọn lớp mới, giữ hoặc đổi ngày hiệu lực, chọn Continue (FR-002).
3. Hệ thống hiển thị toàn bộ trẻ của lớp hiện tại, tất cả được chọn; người dùng bỏ chọn trẻ ở lại nếu có, chọn Continue (FR-003).
4. Hệ thống thông báo “n children move into <lớp đích> on <ngày>”; người dùng chọn Done (FR-004).
5. Hệ thống chuyển trẻ, ghi lịch sử và hiển thị kết quả từng trẻ (FR-004, FR-005, FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lớp mới vượt sĩ số tối đa: hiển thị cảnh báo, vẫn tiếp tục được (BR-008).
2. Có trẻ không chuyển được: người dùng thao tác lại (FR-005; BR-010).
3. Lớp ở level cao nhất của Centre: không có Move children up, có chỉ dẫn sang Graduation hoặc Transfer (BR-002).
4. Người dùng chọn Back để quay lại bước trước, hoặc Close để đóng mà không chuyển trẻ.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Chưa chọn lớp mới: không tiếp tục được; người có quyền tạo lớp ở Classes rồi làm lại (BR-004; VAL-001).
2. Lớp hiện tại không có trẻ: không có trẻ để chuyển (VAL-002).
3. Lỗi khi chuyển một trẻ: trẻ đó giữ lớp cũ, các trẻ khác vẫn được chuyển (BR-010).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Chỉ lên lớp trong cùng Centre. Chuyển sang Centre khác là Transfer. |
| BR-002 | Lớp ở level cao nhất Centre mở không có Move children up; Centre không mở level kế tiếp chỉ dẫn sang Transfer. |
| BR-003 | Lớp mới thuộc level kế tiếp, năm học mới, cùng Centre. |
| BR-004 | Lớp mới phải được tạo trước ở Classes bởi người có quyền tạo lớp. Luồng lên lớp không tạo lớp. |
| BR-005 | Ngày hiệu lực mặc định là ngày bắt đầu năm học mới. |
| BR-006 | Mặc định chọn toàn bộ trẻ của lớp. Người dùng bỏ chọn trẻ ngoại lệ (ví dụ học lại); trẻ bị bỏ chọn ở lại lớp hiện tại, không thay đổi gì. |
| BR-007 | Trẻ được chọn vào lớp mới và level trong ghi danh đổi sang level mới theo ngày hiệu lực của lớp. |
| BR-008 | Lớp mới vượt sĩ số tối đa chỉ cảnh báo, không chặn. |
| BR-009 | Lớp và danh sách học sinh ở lớp cũ vẫn tồn tại. |
| BR-010 | Mỗi trẻ được chuyển độc lập: một trẻ lỗi không chặn trẻ khác. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Centre chưa có lớp nào của level kế tiếp cho năm học mới. | Báo “There is no class at this centre for <level> the next academic year yet, so there is nowhere for these children to move to.”; không tiếp tục được. |
| VAL-002 | Lớp hiện tại không có trẻ. | Hiển thị “No children are in this class.” |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up |  |
| Classes — chi tiết lớp › Children, History |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Move children up | Mục trong Edit | Theo quyền | Ẩn ở lớp level cao nhất | — | FR-001; BR-002. |
| Destination class — next year | Danh sách chọn | Có | — | VAL-001. | Các lớp theo BR-003, kèm sĩ số / tối đa (FR-002). |
| Effective date | Chọn ngày | Có | Theo BR-005 | — | FR-002. |
| Danh sách trẻ | Danh sách có ô chọn | — | Tất cả được chọn | VAL-002. | Mỗi dòng: tên trẻ, “Moves up” khi được chọn, “Stays in <lớp nguồn>” khi bỏ chọn (FR-003; BR-006). |
| Cảnh báo sĩ số | Thông báo | — | Khi vượt sĩ số | — | “<lớp đích> would hold <n> of <tối đa>” (BR-008). |
| Tóm tắt xác nhận | Display | — | — | — | “n children move into <lớp đích> on <ngày>”. |
| Done | Nút | — | — | — | Xác nhận lên lớp (FR-004). |
| Back / Continue / Close | Nút | — | — | VAL-001; VAL-002. | Chuyển bước hoặc đóng. |
| Kết quả | Bảng | — | Sau khi xác nhận | — | Thông báo số lượng trẻ đã chuyển thành công (FR-005). |
| Lớp cũ › Children | Danh sách | — | — | — | Vẫn hiện trẻ đã lên lớp (BR-009). |
| Lớp › History | Danh sách | — | — | — | Dòng lên lớp: lớp cũ → lớp mới, số trẻ, ngày hiệu lực, người thực hiện, thời điểm (FR-006). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi trẻ được chuyển, lưu lớp và level cũ, lớp và level mới, ngày hiệu lực, người thực hiện, thời điểm xác nhận. |
| DATA-002 | Mỗi lần lên lớp, lưu lớp hiện tại, lớp mới, ngày hiệu lực, số trẻ đã chuyển, lỗi (kèm lý do), ở lại, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp N2 · Sunbeams năm 2026; Centre đã tạo lớp K1 · Honeybees năm 2027 | người dùng chọn Edit › Move children up | danh sách lớp đích có K1 · Honeybees năm 2027 của cùng Centre; ngày hiệu lực mặc định là ngày bắt đầu năm học 2027 | FR-001; FR-002; BR-001; BR-003; BR-005 |
| AC-002 | Centre chưa tạo lớp K1 năm 2027 | người dùng chọn Move children up ở lớp N2 | hiện thông báo VAL-001; không có nút tạo lớp; không tiếp tục được | FR-002; BR-004; VAL-001 |
| AC-003 | lớp K2 · Blossom | người dùng mở Edit | không có Move children up; có chỉ dẫn sang Graduation | BR-002 |
| AC-004 | Centre chỉ mở tới N2 | người dùng mở Edit của lớp N2 | không có Move children up; có chỉ dẫn sang Transfer | BR-002 |
| AC-005 | Teacher không có quyền lên lớp | Teacher mở Edit của lớp | không có Move children up | FR-001 |
| AC-006 | lớp Sunbeams có 16 trẻ | người dùng sang bước chọn trẻ | 16 trẻ được chọn sẵn, mỗi trẻ ghi “Moves up” | FR-003; BR-006 |
| AC-007 | 16 trẻ được chọn, ngày hiệu lực 04/01/2027 | người dùng chọn Done | 16 trẻ ở lớp K1 · Honeybees, level K1 từ 04/01/2027; kết quả hiện 16 trẻ đã chuyển | FR-004; FR-005; BR-007 |
| AC-008 | 2 trẻ học lại N2 | người dùng bỏ chọn 2 trẻ rồi xác nhận | 2 trẻ ghi “Stays in N2 · Sunbeams” và ở lại lớp Sunbeams; 14 trẻ lên K1 · Honeybees | FR-003; FR-004; BR-006; BR-007 |
| AC-009 | lớp Honeybees tối đa 20, đã có 8 trẻ; 14 trẻ được chọn | người dùng sang bước tiếp theo | hiện “K1 · Honeybees would hold 22 of 20” kèm cảnh báo; Continue vẫn bật | BR-008 |
| AC-010 | lớp nguồn không có trẻ | người dùng mở Move children up | hiện “No children are in this class.” | VAL-002 |
| AC-011 | đã xác nhận | người dùng mở lớp Sunbeams › Children sau ngày hiệu lực | Thấy các trẻ đã lên lớp; trẻ ở lại không đổi | FR-004; BR-009 |
| AC-012 | lớp Sunbeams đã có trẻ | người dùng tìm thao tác xoá lớp | không có thao tác xoá; lịch sử lớp còn | BR-009 |
| AC-013 | 3 trẻ được chọn, việc chuyển của Chloe lỗi | người dùng xem kết quả | 2 trẻ đã chuyển; Chloe lỗi kèm lý do và vẫn ở Sunbeams | FR-005; BR-010 |
| AC-014 | đã xác nhận | người dùng mở History của lớp Sunbeams | có dòng lên lớp: lớp cũ, lớp mới, số trẻ, ngày hiệu lực, người thực hiện | FR-006; DATA-002 |

#### Dependencies (Phụ thuộc)

Classes (lớp năm học mới, sĩ số); level Centre mở (Organisation); ghi danh của trẻ; Joining & leaving (Graduation, Transfer).

## 7. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Level | Cấp lớp theo độ tuổi: Infant, Playgroup, N1, N2, K1, K2; mỗi Centre chỉ mở một số level. |
| Annual promotion | Cuối năm học, cả lớp lên level kế tiếp trong cùng Centre. |
| Infant promotion | Trẻ Infant lên Playgroup theo tuổi (18 tháng), bất kỳ lúc nào trong năm, từng trẻ. |
| Class change | Đổi lớp trong cùng level. |
| Lớp nguồn / lớp đích | Lớp hiện tại của trẻ / lớp năm học mới đã tạo sẵn mà trẻ được chuyển tới. |
| Ngày hiệu lực | Ngày việc lên lớp bắt đầu áp dụng. |
| Học lại | Trẻ ở lại level cũ thêm một năm. |
| Graduation | Trẻ K2 rời trường vào tháng 12 (Joining & leaving). |
| Transfer | Trẻ chuyển sang Centre khác (Joining & leaving). |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Kết quả lên lớp | Đã chuyển, Lỗi, Ở lại. | Lựa chọn trẻ và kết quả xử lý. |
