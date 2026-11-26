# Move Whole Class up a Level

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Classes |
| Tính năng | BBA-72 Move whole class up a level (bulk promotion) |
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

Cuối năm học, Centre chuyển cả lớp lên level kế tiếp cho năm học mới (ví dụ N2 lên K1). Người dùng thao tác một lần cho cả lớp thay vì chuyển từng trẻ. Lớp cũ và danh sách trẻ của lớp cũ vẫn được giữ.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Lên lớp cả lớp trong cùng Centre: chọn lớp đích và ngày hiệu lực; xem trước trẻ và tác động; bỏ chọn trẻ ở lại; xác nhận; kết quả từng trẻ; lịch sử. | Đổi lớp từng trẻ (class change), Infant lên Playgroup lúc 18 tháng. K2 tốt nghiệp (Joining & leaving › Graduation). Chuyển Centre (Transfer). Tạo, sửa, đóng lớp ngoài luồng lên lớp (Classes). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Lớp và trẻ của Centre được cấp. | Lên lớp cả lớp, tạo lớp đích trong luồng, chạy lại trẻ lỗi. |
| Class Viewer | Lớp và trẻ trong phạm vi được cấp. | Xem lớp và lịch sử lớp; không thấy Move children up. |
| System | Lớp nguồn, lớp đích, trẻ được chọn. | Chuyển trẻ từ ngày hiệu lực, cập nhật dữ liệu liên quan, báo kết quả, lưu lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo Roles & permissions và phạm vi dữ liệu. Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Classes** | Chọn lớp đích và ngày hiệu lực | Mở Move children up từ chi tiết lớp; chọn lớp đích năm học mới và ngày hiệu lực. | BBA-72: US-001 |
| **Classes** | Xem trước trẻ và tác động | Danh sách trẻ sẽ lên lớp, bỏ chọn trẻ ở lại; xem tác động trước khi xác nhận. | BBA-72: US-002 |
| **Classes** | Xác nhận và kết quả | Xác nhận lên lớp; xem kết quả từng trẻ; lịch sử. | BBA-72: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-72: US-001 - Chọn lớp đích và ngày hiệu lực

#### User Story

Là người dùng, tôi muốn chọn lớp đích của năm học mới và ngày hiệu lực cho cả lớp, để chuẩn bị lên lớp mà không phải chuyển từng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Người dùng có quyền mở luồng lên lớp từ chi tiết lớp (BR-001, BR-002). |
| FR-002 | Người dùng chọn lớp đích; chưa có lớp đích thì tạo ngay trong luồng (BR-003, BR-004). |
| FR-003 | Người dùng chọn ngày hiệu lực (BR-005; VAL-001). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở lớp, chọn Actions › Move children up (FR-001).
2. Hệ thống đề xuất lớp đích và ngày hiệu lực (FR-002, FR-003).
3. Người dùng giữ hoặc đổi lớp đích, ngày hiệu lực, chọn Continue sang US-002.

#### Functional Flow - Alternative (Luồng thay thế)

1. Chưa có lớp đích: người dùng tạo lớp trong luồng, lớp mới thành lớp đích (FR-002; BR-004).
2. Lớp ở level cao nhất của Centre: không có Move children up, có chỉ dẫn sang Graduation hoặc Transfer (BR-002).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ngày hiệu lực trước hôm nay: không tiếp tục được (VAL-001).
2. Mã lớp tạo mới đã tồn tại: không tạo được lớp (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Chỉ lên lớp trong cùng Centre. Chuyển sang Centre khác là Transfer (Joining & leaving). |
| BR-002 | Lớp ở level cao nhất Centre mở không có Move children up. Lớp K2 chỉ dẫn sang Graduation; Centre không mở level kế tiếp chỉ dẫn sang Transfer. |
| BR-003 | Lớp đích thuộc level kế tiếp, năm học mới, cùng Centre. Hệ thống đề xuất lớp đầu tiên của level kế tiếp. |
| BR-004 | Lớp tạo trong luồng theo quy tắc tạo lớp của Classes: chỉ trong level Centre mở; mã lớp duy nhất trong Centre và năm học. Lớp tạo xong dùng được ngay làm lớp đích. |
| BR-005 | Ngày hiệu lực mặc định là ngày bắt đầu Term 1 của năm học mới theo lịch term của brand. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Ngày hiệu lực trước hôm nay. | Không cho tiếp tục; báo “The effective date cannot be in the past.” |
| VAL-002 | Mã lớp tạo mới trùng mã lớp khác cùng Centre, cùng năm học. | Không tạo lớp; báo lỗi tại trường mã lớp. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up — bước Request | Prototype: Classes › chi tiết lớp › Actions › Move children up |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Move children up | Mục trong Actions | Theo quyền | Ẩn ở lớp level cao nhất | — | FR-001; BR-002. |
| Thanh bước | Display | — | Request | — | Request › Children › Impact › Confirmation. |
| Destination class | Danh sách chọn | Có | Theo BR-003 | — | Mỗi lớp hiện level, sĩ số / tối đa, số chỗ còn lại. |
| Tạo lớp đích | Form | Khi chưa có lớp | — | VAL-002. | Theo form tạo lớp của Classes (BR-004). |
| Effective date | Chọn ngày | Có | Theo BR-005 | VAL-001. | FR-003. |
| Back / Continue / Close | Nút | — | — | VAL-001. | Chuyển bước hoặc đóng. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Lớp tạo trong luồng lưu như lớp tạo ở Classes, kèm người tạo và thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp N2 · Sunbeams năm 2026; đã có lớp K1 · Honeycombs năm 2027 cùng Centre | người dùng chọn Actions › Move children up | danh sách lớp đích chỉ có lớp K1 năm 2027 của cùng Centre, mặc định K1 · Honeycombs; ngày hiệu lực là ngày bắt đầu Term 1 năm 2027 | FR-001; FR-002; FR-003; BR-001; BR-003; BR-005 |
| AC-002 | chưa có lớp K1 năm 2027 ở Centre | người dùng tạo lớp K1 · Honeybees trong luồng | lớp K1 · Honeybees được tạo và là lớp đích | FR-002; BR-004; DATA-001 |
| AC-003 | lớp K1 năm 2027 mã “Kindergarten 1” đã có | người dùng tạo lớp mới cùng mã | không tạo lớp; báo lỗi tại trường mã lớp | VAL-002 |
| AC-004 | lớp K2 · Blossom | người dùng mở Actions | không có Move children up; có chỉ dẫn sang Graduation | BR-002 |
| AC-005 | Centre chỉ mở tới N2 | người dùng mở Actions của lớp N2 | không có Move children up; có chỉ dẫn sang Transfer | BR-002 |
| AC-006 | người dùng chọn ngày hiệu lực là hôm qua | chọn Continue | không sang bước sau; hiện thông báo VAL-001 | VAL-001 |
| AC-007 | Teacher không có quyền lên lớp | Teacher mở Actions của lớp | không có Move children up | FR-001 |

#### Dependencies (Phụ thuộc)

Classes (tạo lớp, sĩ số); level Centre mở (Organisation); lịch term theo brand; Joining & leaving (Graduation, Transfer).

### 6.2 BBA-72: US-002 - Xem trước trẻ và tác động

#### User Story

Là người dùng, tôi muốn xem trước trẻ nào sẽ lên lớp và việc lên lớp ảnh hưởng gì, bỏ chọn được trẻ ở lại, để chắc chắn trước khi xác nhận.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Hệ thống liệt kê trẻ đang học trong lớp nguồn; người dùng bỏ chọn trẻ ở lại (BR-006, BR-007; VAL-003, VAL-004). |
| FR-005 | Hệ thống hiển thị tác động của việc lên lớp trước khi xác nhận (BR-008, BR-009). |

#### Functional Flow - Main (Luồng chính)

1. Hệ thống hiển thị danh sách trẻ của lớp nguồn (FR-004).
2. Người dùng bỏ chọn trẻ ở lại, chọn Continue (FR-004).
3. Hệ thống hiển thị tác động; người dùng chọn Continue sang US-003 (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lớp đích vượt sĩ số tối đa: hiển thị cảnh báo, vẫn tiếp tục được (BR-009).
2. Người dùng chọn Back để đổi lớp đích hoặc ngày hiệu lực (US-001).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không còn trẻ nào được chọn: không tiếp tục được (VAL-003).
2. Trẻ đã có thay đổi chờ hiệu lực: không chọn được trẻ đó (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Mặc định mọi trẻ đang học được chọn. Trẻ bị bỏ chọn (ví dụ học lại) ở lại lớp nguồn, không thay đổi gì. |
| BR-007 | Trẻ đã có đổi lớp, transfer hoặc withdrawal chưa tới ngày hiệu lực không được chọn; hiển thị lý do và ngày. |
| BR-008 | Tác động gồm: số trẻ lên lớp đích; sĩ số lớp đích sau khi chuyển; số trẻ còn lại ở lớp nguồn; level trong ghi danh đổi từ ngày hiệu lực; học phí tính theo level mới từ ngày hiệu lực; trẻ rời thread lớp cũ và vào thread lớp đích. |
| BR-009 | Lớp đích vượt sĩ số tối đa chỉ cảnh báo, không chặn. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Không còn trẻ nào được chọn. | Nút Continue tắt. |
| VAL-004 | Trẻ đã có đổi lớp, transfer hoặc withdrawal chưa tới ngày hiệu lực. | Ô chọn của trẻ tắt; ghi “Already has a class change on DD/MM/YYYY” (hoặc transfer / withdrawal). |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up — bước Children, Impact | Prototype: Move children up › Continue |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Danh sách trẻ | Bảng có ô chọn | Ít nhất 1 trẻ | Tất cả được chọn | VAL-003; VAL-004. | Mỗi dòng: tên trẻ, “Moves up” khi được chọn, lý do khi không chọn được (FR-004). |
| Impact | Section | — | — | — | Nhóm Class, Enrolment, Billing, Access (BR-008). |
| Cảnh báo sĩ số | Thông báo | — | Khi vượt sĩ số | — | Ví dụ “K1 · Honeybees would hold 22 of 20” (BR-009). |
| Back / Continue | Nút | — | — | VAL-003. | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Xem trước không lưu dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-008 | lớp Sunbeams có 16 trẻ đang học | người dùng sang bước Children | 16 trẻ được chọn sẵn, mỗi trẻ ghi “Moves up” | FR-004; BR-006 |
| AC-009 | 2 trẻ học lại N2 | người dùng bỏ chọn 2 trẻ, sang bước Impact | tác động hiện “14 of 16 children move into K1 · Honeycombs”; Sunbeams giữ 2 trẻ | FR-004; FR-005; BR-006; BR-008; DATA-002 |
| AC-010 | lớp Honeycombs tối đa 20, đã có 8 trẻ | 14 trẻ được chọn | tác động hiện “K1 · Honeycombs would hold 22 of 20” kèm cảnh báo; Continue vẫn bật | BR-009 |
| AC-011 | ngày hiệu lực 04/01/2027 | người dùng xem Impact | có dòng đổi level N2 sang K1 từ 04/01/2027, dòng học phí theo level mới và dòng thread lớp mới | BR-008 |
| AC-012 | người dùng bỏ chọn tất cả trẻ | nhìn nút Continue | nút tắt | VAL-003 |
| AC-013 | một trẻ có transfer, ngày học cuối 31/12/2026 | người dùng xem bước Children | ô chọn của trẻ tắt, ghi lý do transfer kèm ngày | BR-007; VAL-004 |

#### Dependencies (Phụ thuộc)

US-001; ghi danh của trẻ; biểu phí theo level (Fees & Payments); thread của lớp (Communication).

### 6.3 BBA-72: US-003 - Xác nhận và kết quả

#### User Story

Là người dùng, tôi muốn xác nhận một lần để cả lớp lên lớp mới mà lớp cũ vẫn giữ danh sách trẻ, và biết trẻ nào đã chuyển, trẻ nào lỗi, để xử lý tiếp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-006 | Người dùng xác nhận; hệ thống chuyển trẻ được chọn sang lớp đích (BR-010, BR-011, BR-012, BR-013). |
| FR-007 | Hệ thống hiển thị kết quả từng trẻ và cho chạy lại trẻ lỗi (BR-014). |
| FR-008 | Hệ thống ghi lịch sử cho từng trẻ và cho lớp (DATA-003, DATA-004). |

#### Functional Flow - Main (Luồng chính)

1. Ở bước Confirmation, hệ thống tóm tắt số trẻ, lớp đích, ngày hiệu lực; người dùng chọn Done (FR-006).
2. Hệ thống chuyển trẻ và ghi lịch sử (FR-006, FR-008).
3. Hệ thống hiển thị kết quả từng trẻ (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Có trẻ không chuyển được: người dùng chọn Retry để chạy lại trẻ lỗi (FR-007; BR-014).
2. Trước ngày hiệu lực, người dùng mở lớp cũ hoặc hồ sơ trẻ: trẻ vẫn ở lớp cũ (BR-010).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Lỗi khi chuyển một trẻ: trẻ đó giữ lớp cũ, các trẻ khác vẫn được chuyển (BR-014).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-010 | Mọi thay đổi (lớp, level trong ghi danh, học phí, danh sách điểm danh, thread) bắt đầu từ ngày hiệu lực. Trước ngày đó trẻ vẫn ở lớp cũ trên mọi màn hình. |
| BR-011 | Hoá đơn đã phát hành không bị sửa; học phí theo level mới áp cho hoá đơn tạo sau ngày hiệu lực. Thread lớp cũ chuyển chỉ đọc. |
| BR-012 | Lớp và danh sách học sinh ở lớp cũ vẫn tồn tại: với mỗi trẻ được chuyển, lần xếp lớp ở lớp cũ kết thúc vào ngày trước ngày hiệu lực, trạng thái của trẻ trong lớp cũ là đã lên lớp, kèm lớp mới. Trẻ bị bỏ chọn giữ trạng thái đang học. |
| BR-013 | Lớp cũ còn trẻ đang học từ ngày hiệu lực thì giữ Open; không còn trẻ thì chuyển Closed (OQ-02). Lớp đã có trẻ chỉ được đóng, không bị xoá; lịch sử được giữ. |
| BR-014 | Mỗi trẻ được chuyển độc lập: một trẻ lỗi không chặn trẻ khác. Retry chỉ chạy lại trẻ Not moved, không chuyển trùng trẻ đã Moved. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up — bước Confirmation; kết quả | Prototype: Move children up › Confirmation |
| Classes — chi tiết lớp › Children, History | Prototype: Classes › chi tiết lớp |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tóm tắt xác nhận | Display | — | — | — | “n children move into <lớp đích> on <ngày>”. |
| Done | Nút | — | — | — | Xác nhận lên lớp (FR-006). |
| Kết quả | Thẻ đếm + bảng | — | Sau khi xác nhận | — | Moved / Not moved / Stayed; cột Child, Destination class, Result, Reason (FR-007). |
| Retry | Nút | — | Khi có trẻ Not moved | — | BR-014. |
| Lớp cũ › Children | Danh sách | — | — | — | Hiện cả trẻ đã lên lớp, kèm trạng thái, lớp mới, ngày kết thúc (BR-012). |
| Lớp › History | Danh sách | — | — | — | Dòng lên lớp: lớp cũ → lớp mới, số trẻ, ngày hiệu lực, người thực hiện, thời điểm (FR-008). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi trẻ được chuyển lưu: lớp và level cũ, lớp và level mới, ngày hiệu lực, ngày kết thúc ở lớp cũ, trạng thái trong lớp cũ, người thực hiện, thời điểm xác nhận. |
| DATA-004 | Mỗi lần lên lớp lưu: lớp nguồn, lớp đích, ngày hiệu lực, số trẻ Moved, Not moved (kèm lý do), Stayed, trạng thái lớp nguồn sau khi chuyển, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-014 | 14 trẻ được chọn, ngày hiệu lực 04/01/2027 | người dùng chọn Done | 14 trẻ ở lớp K1 · Honeycombs từ 04/01/2027; kết quả hiện 14 Moved | FR-006; FR-007 |
| AC-015 | đã xác nhận, hôm nay 15/12/2026 | giáo viên mở điểm danh lớp Sunbeams ngày 20/12/2026 | 14 trẻ vẫn ở Sunbeams; từ 04/01/2027 trẻ ở danh sách điểm danh Honeycombs | BR-010 |
| AC-016 | đã xác nhận | người dùng mở lớp Sunbeams › Children sau 04/01/2027 | vẫn thấy 14 trẻ ghi đã lên lớp, lớp K1 · Honeycombs, ngày kết thúc 03/01/2027; 2 trẻ ở lại ghi đang học | BR-012 |
| AC-017 | 2 trẻ ở lại Sunbeams | qua ngày 04/01/2027 | lớp Sunbeams vẫn Open | BR-013 |
| AC-018 | cả 16 trẻ lên lớp | qua ngày 04/01/2027 | lớp Sunbeams chuyển Closed; danh sách 16 trẻ và lịch sử vẫn còn | BR-013 |
| AC-019 | hoá đơn tháng 1/2027 chưa tạo | hoá đơn tháng 1/2027 được tạo | 14 trẻ tính học phí K1 | BR-011 |
| AC-020 | 3 trẻ được chọn, việc chuyển của Chloe lỗi | người dùng xem kết quả | 2 Moved; Chloe Not moved kèm lý do và vẫn ở Sunbeams; Retry chỉ chạy lại Chloe | FR-007; BR-014 |
| AC-021 | Ethan đã Moved | người dùng chọn Retry | Ethan không bị chuyển lần nữa; lịch sử Ethan có một dòng lên lớp | BR-014; DATA-003 |
| AC-022 | đã xác nhận | người dùng mở History của lớp Sunbeams | có dòng lên lớp: lớp cũ, lớp mới, số trẻ, ngày hiệu lực, người thực hiện | FR-008; DATA-004 |
| AC-023 | 14 trẻ đã lên Honeycombs từ 04/01/2027 | phụ huynh một trẻ mở Messages ngày 05/01/2027 | thấy thread lớp Honeycombs; thread Sunbeams chỉ đọc | BR-011 |

#### Dependencies (Phụ thuộc)

US-001, US-002; ghi danh; Fees & Payments (biểu phí theo level); danh sách điểm danh; Communication (thread của lớp).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Việc lên lớp có cần ai duyệt trước khi có hiệu lực không? Có cho huỷ trước ngày hiệu lực không? | Centre Director / HQ Ops | Trung bình |  |
| OQ-02 | Lớp cũ hết trẻ từ ngày hiệu lực: hệ thống tự chuyển Closed hay người dùng đóng tay (SRS P6 ghi “old classes can be closed”)? Tên trạng thái của trẻ trong lớp cũ sau khi lên lớp là gì (đề xuất “Moved up”)? | Centre Director / HQ Ops | Trung bình |  |
| OQ-03 | Trẻ đang tạm nghỉ có được lên lớp cùng lớp không? | Centre Director / HQ Ops | Trung bình |  |
| OQ-04 | Phụ huynh và giáo viên có nhận thông báo khi lên lớp không? | Centre Director / HQ Ops | Thấp |  |
| OQ-05 | Centre không mở level kế tiếp: cuối năm dùng Bulk transfer children (Administration) hay Transfer từng trẻ? | HQ Ops | Cao |  |
| OQ-06 | SRS P6 cho đổi lớp đích cho từng trẻ (“changes target classes where needed”). Luồng hiện tại chỉ có một lớp đích cho cả lớp. Có cần đổi lớp đích cho từng trẻ (chia lớp nguồn sang nhiều lớp đích) không? | HQ Ops | Cao |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Level | Cấp lớp theo độ tuổi: Infant, Playgroup, N1, N2, K1, K2; mỗi Centre chỉ mở một số level. |
| Annual promotion | Cuối năm học, cả lớp lên level kế tiếp trong cùng Centre. |
| Lớp nguồn / lớp đích | Lớp hiện tại của trẻ / lớp năm học mới trẻ được chuyển tới. |
| Ngày hiệu lực | Ngày việc lên lớp bắt đầu áp dụng. |
| Học lại | Trẻ ở lại level cũ thêm một năm. |
| Graduation | Trẻ K2 rời trường cuối năm (Joining & leaving). |
| Transfer | Trẻ chuyển sang Centre khác (Joining & leaving). |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Kết quả lên lớp | Moved, Not moved, Stayed. | Lựa chọn trẻ và kết quả xử lý. |
| Trạng thái lớp | Open, Closed. | Số trẻ đang học (BR-013). |
