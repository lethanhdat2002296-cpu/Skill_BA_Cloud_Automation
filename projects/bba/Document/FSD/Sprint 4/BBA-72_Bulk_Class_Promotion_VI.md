# Move Whole Class up a Level (Bulk Promotion)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Classes |
| Tính năng | BBA-72 Move whole class up a level (bulk promotion) |
| Mã tài liệu | FRD-3.1.5.01_Bulk_Class_Promotion |
| Sprint | 4 |
| Phiên bản | 0.3 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 22/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 14/11/2026 | Business Analysis | Bổ sung theo phản hồi của BBA. | |
| 0.3 | 22/11/2026 | Business Analysis | Theo góp ý: xác định lại tính năng, tách 3 User Story (chọn lớp đích và ngày hiệu lực; xem trước trẻ và tác động; xác nhận và kết quả). Lớp cũ giữ danh sách trẻ; cập nhật trạng thái trẻ trong lớp và trạng thái lớp. Đối chiếu prototype. | |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Năm học chạy từ tháng 1 đến tháng 12. Cuối năm, Centre chuyển cả lớp lên level kế tiếp (ví dụ N2 lên K1) cho năm học mới. Thay vì chuyển từng trẻ, người dùng chọn lớp, chọn lớp đích và ngày hiệu lực, xem trước trẻ và tác động, bỏ chọn trẻ ngoại lệ, rồi xác nhận một lần. Việc lên lớp không làm mất lớp cũ: lớp cũ và danh sách trẻ của lớp cũ vẫn còn, chỉ trạng thái của trẻ trong lớp và trạng thái lớp được cập nhật.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Lên lớp cả lớp trong cùng Centre (annual promotion): chọn lớp đích năm học mới, tạo lớp đích khi chưa có, ngày hiệu lực; xem trước trẻ, bỏ chọn trẻ ngoại lệ; xem tác động (lớp, ghi danh, học phí, thread của lớp); xác nhận; kết quả từng trẻ và chạy lại trẻ lỗi; giữ lớp cũ và danh sách trẻ cũ; lịch sử từng trẻ. | Lên lớp từng trẻ (Infant promotion) và đổi lớp từng trẻ (class change). K2 tốt nghiệp (Joining & leaving › Graduation). Chuyển sang Centre khác (Transfer). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Lớp và trẻ của Centre được cấp. | Lên lớp cả lớp, tạo lớp đích, chạy lại trẻ lỗi. |
| Class Viewer | Lớp và trẻ trong phạm vi được cấp. | Xem lớp và lịch sử lớp; không thấy Move children up. |
| System | Lớp nguồn, lớp đích, trẻ được chọn. | Chuyển từng trẻ từ ngày hiệu lực, cập nhật trạng thái trẻ trong lớp và trạng thái lớp, cập nhật ghi danh, học phí, thread; báo kết quả; lưu lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Classes** | Chọn lớp đích và ngày hiệu lực | Từ chi tiết lớp chọn Move children up; chọn lớp đích năm học mới (tạo mới nếu chưa có) và ngày hiệu lực. | BBA-72: US-001 |
| **Classes** | Xem trước trẻ và tác động | Danh sách trẻ sẽ lên lớp, bỏ chọn trẻ ngoại lệ; tác động tới lớp, ghi danh, học phí, thread của lớp. | BBA-72: US-002 |
| **Classes** | Xác nhận và kết quả | Chuyển trẻ từ ngày hiệu lực; lớp cũ giữ danh sách trẻ; cập nhật trạng thái trẻ trong lớp và trạng thái lớp; kết quả từng trẻ, chạy lại trẻ lỗi; lịch sử. | BBA-72: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-72: US-001 - Chọn lớp đích và ngày hiệu lực

#### User Story

Là Centre Director, tôi muốn chọn lớp đích của năm học mới và ngày hiệu lực cho cả lớp, để chuẩn bị lên lớp mà không phải chuyển từng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Ở chi tiết lớp, người dùng có quyền chọn Actions › Move children up để mở luồng lên lớp (BR-001, BR-002). |
| FR-002 | Người dùng chọn lớp đích trong các lớp của level kế tiếp, năm học mới, cùng Centre; chưa có lớp thì tạo lớp đích ngay trong luồng (BR-003). |
| FR-003 | Người dùng chọn ngày hiệu lực; hệ thống đề xuất sẵn (BR-004). |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở lớp N2 · Sunbeams, chọn Actions › Move children up (FR-001).
2. Hệ thống hiển thị lớp đích năm học mới của level K1 kèm sĩ số và ngày hiệu lực đề xuất (FR-002, FR-003).
3. Centre Director chọn lớp đích, giữ hoặc đổi ngày hiệu lực, chọn Continue sang US-002.

#### Functional Flow - Alternative (Luồng thay thế)

1. Chưa có lớp K1 cho năm học mới: hệ thống báo và hiện form tạo lớp (Name, Level, Capacity, Room); Centre Director chọn Create a class, lớp mới được chọn làm lớp đích (FR-002; BR-003).
2. Lớp ở level K2: không có Move children up; chi tiết lớp chỉ dẫn sang Joining & leaving › Graduation (BR-002).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ngày hiệu lực trước hôm nay: không cho tiếp tục (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Chỉ lên lớp trong cùng Centre. Chuyển sang Centre khác là Transfer (Joining & leaving). |
| BR-002 | Lớp ở level cao nhất của Centre không có Move children up. Lớp K2: chỉ dẫn sang Graduation. Centre không mở level kế tiếp (chưa tới K2): chỉ dẫn sang Transfer. |
| BR-003 | Lớp đích phải thuộc level kế tiếp, năm học mới, cùng Centre. Chưa có lớp nào như vậy thì người dùng tạo lớp trong luồng; lớp tạo xong dùng được ngay làm lớp đích. |
| BR-004 | Ngày hiệu lực mặc định là ngày bắt đầu Term 1 của năm học mới theo lịch term của brand. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Ngày hiệu lực trước hôm nay. | Không cho tiếp tục; báo lỗi "The effective date cannot be in the past." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up — bước Request | Prototype: Classes › chi tiết lớp › Actions › Move children up |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Move children up | Mục trong Actions | Theo quyền | Ẩn ở lớp level cao nhất | — | Mở luồng lên lớp (FR-001; BR-002). |
| Thanh bước | Display | — | Request | — | Request › Children › Impact › Confirmation. |
| Destination class — <năm> | Danh sách chọn | Có | Lớp đầu tiên của level kế tiếp | — | Mỗi lớp hiện level, "x of y enrolled", số chỗ còn lại (FR-002). |
| Tạo lớp đích | Form | Khi chưa có lớp | — | — | Name, Level (level kế tiếp), Capacity, Room; nút Create a class (BR-003). |
| Effective date | Chọn ngày | Có | Ngày bắt đầu Term 1 năm học mới | VAL-001. | FR-003; BR-004. |
| Back / Continue / Close | Nút | — | — | VAL-001. | Chuyển bước hoặc đóng. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Lớp tạo trong luồng lưu như lớp tạo ở Classes (tên, level, năm học, sĩ số, phòng, Centre, người tạo). |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp N2 · Sunbeams năm 2026; đã có lớp K1 · Honeycombs năm 2027 cùng Centre | Centre Director chọn Actions › Move children up | danh sách lớp đích chỉ có lớp K1 năm 2027 của cùng Centre, mặc định K1 · Honeycombs kèm sĩ số; ngày hiệu lực là ngày bắt đầu Term 1 năm 2027 | FR-001; FR-002; FR-003; BR-001; BR-004 |
| AC-002 | chưa có lớp K1 nào năm 2027 ở Centre | Centre Director chọn Move children up | hệ thống báo chưa có lớp năm 2027 và hiện form tạo lớp; tạo K1 · Honeybees xong thì lớp này là lớp đích | FR-002; BR-003 |
| AC-003 | lớp K2 · Blossom | Centre Director mở Actions | không có Move children up; có chỉ dẫn sang Graduation | BR-002 |
| AC-004 | Centre chỉ mở tới N2 | Centre Director mở Actions của lớp N2 | không có Move children up; có chỉ dẫn sang Transfer | BR-002 |
| AC-005 | Centre Director chọn ngày hiệu lực là hôm qua | chọn Continue | không sang bước sau, hiện "The effective date cannot be in the past." | VAL-001 |
| AC-006 | Teacher không có quyền lên lớp | Teacher mở Actions của lớp | không có Move children up | FR-001 |

#### Dependencies (Phụ thuộc)

Classes (lớp năm học mới, sĩ số); level Centre có mở; lịch term theo brand; Joining & leaving (Graduation, Transfer).

### 6.2 BBA-72: US-002 - Xem trước trẻ và tác động

#### User Story

Là Centre Director, tôi muốn xem trước trẻ nào sẽ lên lớp và việc lên lớp ảnh hưởng gì, bỏ chọn được trẻ ngoại lệ, để chắc chắn trước khi xác nhận.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Hệ thống liệt kê mọi trẻ đang học trong lớp nguồn, mỗi trẻ có ô chọn, mặc định được chọn (BR-005, BR-006). |
| FR-005 | Người dùng bỏ chọn trẻ ngoại lệ (học lại, sắp rút, sắp chuyển Centre); trẻ bị bỏ chọn ở lại lớp nguồn (BR-005). |
| FR-006 | Hệ thống hiển thị tác động của việc lên lớp trước khi xác nhận (BR-007, BR-008). |

#### Functional Flow - Main (Luồng chính)

1. Hệ thống hiển thị danh sách trẻ của lớp nguồn, tất cả được chọn (FR-004).
2. Centre Director bỏ chọn trẻ học lại, chọn Continue (FR-005).
3. Hệ thống hiển thị tác động; Centre Director chọn Continue sang US-003 (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lớp đích vượt sĩ số sau khi chuyển: hiển thị cảnh báo, vẫn tiếp tục được (BR-008).
2. Centre Director chọn Back để đổi lớp đích hoặc ngày hiệu lực (US-001).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không còn trẻ nào được chọn: không tiếp tục được (VAL-002).
2. Trẻ đã có đổi lớp, transfer hoặc withdrawal chờ hiệu lực: trẻ bị bỏ chọn, không chọn lại được (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Mặc định mọi trẻ đang học được chọn ("Moves up"). Trẻ bị bỏ chọn ở lại lớp nguồn, không thay đổi gì. |
| BR-006 | Trẻ đã có đổi lớp, transfer hoặc withdrawal chưa tới ngày hiệu lực không được chọn, kèm lý do và ngày. |
| BR-007 | Tác động gồm: số trẻ lên lớp đích; sĩ số lớp đích sau khi chuyển; số trẻ lớp nguồn còn lại và số trẻ kết thúc ở lớp nguồn; level trong ghi danh đổi từ level cũ sang level mới từ ngày hiệu lực; học phí tính theo level mới từ ngày hiệu lực; thread tin nhắn mới với giáo viên lớp đích, thread cũ vẫn đọc được. |
| BR-008 | Lớp đích vượt sĩ số tối đa chỉ cảnh báo, không chặn. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-002 | Không còn trẻ nào được chọn. | Nút Continue tắt. |
| VAL-003 | Trẻ đã có đổi lớp, transfer hoặc withdrawal chưa tới ngày hiệu lực. | Ô chọn của trẻ tắt; ghi "Already has a class change on DD/MM/YYYY" (hoặc transfer / withdrawal). |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up — bước Children, Impact | Prototype: Move children up › Continue |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Danh sách trẻ | Bảng có ô chọn | Có ít nhất 1 trẻ | Tất cả được chọn | VAL-002; VAL-003. | Mỗi dòng: tên trẻ, "Moves up" khi được chọn, lý do khi không chọn được (FR-004; FR-005). |
| Impact | Section | — | — | — | Các dòng tác động theo nhóm Class, Enrolment, Billing, Access (BR-007). |
| Cảnh báo sĩ số | Thông báo | — | Khi vượt sĩ số | — | Ví dụ "K1 · Honeybees would hold 22 of 20" (BR-008). |
| Back / Continue | Nút | — | — | VAL-002. | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| — | Xem trước không lưu dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-007 | lớp Sunbeams có 16 trẻ đang học | Centre Director sang bước Children | 16 trẻ được chọn sẵn, mỗi trẻ ghi "Moves up" | FR-004; BR-005 |
| AC-008 | 2 trẻ học lại N2 | Centre Director bỏ chọn 2 trẻ, sang bước Impact | tác động hiện "14 of 16 children move into K1 · Honeycombs"; Sunbeams giữ 2 trẻ | FR-005; FR-006; BR-007 |
| AC-009 | lớp Honeycombs tối đa 20, đã có 8 trẻ | 14 trẻ được chọn | tác động hiện "K1 · Honeycombs would hold 22 of 20" kèm cảnh báo; Continue vẫn bật | BR-008 |
| AC-010 | ngày hiệu lực 04/01/2027 | Centre Director xem Impact | có dòng "Level moves from N2 to K1 on 04/01/2027", "Fees re-resolve from the new level on that date" và dòng thread tin nhắn mới | BR-007 |
| AC-011 | Centre Director bỏ chọn tất cả trẻ | nhìn nút Continue | nút tắt | VAL-002 |
| AC-012 | một trẻ có transfer, ngày học cuối 31/12/2026 | Centre Director xem bước Children | trẻ đó không được chọn, ô chọn tắt, ghi lý do transfer kèm ngày | BR-006; VAL-003 |

#### Dependencies (Phụ thuộc)

US-001; ghi danh của trẻ; biểu phí theo level (Fees & Payments); thread của lớp (Communication).

### 6.3 BBA-72: US-003 - Xác nhận và kết quả

#### User Story

Là Centre Director, tôi muốn xác nhận một lần để cả lớp lên lớp mới mà lớp cũ vẫn giữ danh sách trẻ, và biết trẻ nào đã chuyển, trẻ nào lỗi, để xử lý tiếp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-007 | Khi xác nhận, hệ thống chuyển từng trẻ được chọn sang lớp đích từ ngày hiệu lực và cập nhật ghi danh, học phí, danh sách điểm danh, thread của lớp (BR-009, BR-010). |
| FR-008 | Lớp cũ và danh sách trẻ của lớp cũ được giữ; hệ thống cập nhật trạng thái của trẻ trong lớp cũ và trạng thái lớp cũ (BR-011, BR-012). |
| FR-009 | Hệ thống hiển thị kết quả từng trẻ và cho chạy lại trẻ lỗi (BR-013). |
| FR-010 | Hệ thống ghi lịch sử cho từng trẻ và cho lớp (DATA-001, DATA-002). |

#### Functional Flow - Main (Luồng chính)

1. Ở bước Confirmation, hệ thống tóm tắt "n children move into <lớp đích> on <ngày>"; Centre Director chọn Done (FR-007).
2. Hệ thống chuyển từng trẻ, cập nhật trạng thái trẻ trong lớp cũ và trạng thái lớp cũ, ghi lịch sử (FR-007, FR-008, FR-010).
3. Hệ thống hiển thị kết quả từng trẻ (FR-009).

#### Functional Flow - Alternative (Luồng thay thế)

1. Một số trẻ không chuyển được: kết quả ghi Not moved kèm lý do; Centre Director chọn Retry, chỉ trẻ lỗi được chạy lại (FR-009; BR-013).
2. Trước ngày hiệu lực, người dùng mở lớp cũ hoặc hồ sơ trẻ: trẻ vẫn ở lớp cũ (BR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Lỗi khi chuyển một trẻ: trẻ đó giữ nguyên lớp cũ, các trẻ khác vẫn được chuyển (BR-013).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-009 | Mọi thay đổi (lớp, level trong ghi danh, học phí, danh sách điểm danh, thread) bắt đầu từ ngày hiệu lực. Trước ngày đó trẻ vẫn ở lớp cũ trên mọi màn hình. |
| BR-010 | Hoá đơn đã phát hành không bị sửa; học phí theo level mới chỉ áp cho hoá đơn tạo sau ngày hiệu lực. Thread lớp cũ chuyển chỉ đọc. |
| BR-011 | Việc lên lớp không xoá trẻ khỏi lớp cũ: lớp cũ giữ danh sách trẻ; với mỗi trẻ được chuyển, lần xếp lớp ở lớp cũ kết thúc vào ngày trước ngày hiệu lực và trạng thái của trẻ trong lớp cũ chuyển sang đã lên lớp, kèm lớp mới. Trẻ bị bỏ chọn giữ trạng thái đang học ở lớp cũ. |
| BR-012 | Trạng thái lớp cũ được cập nhật theo số trẻ còn đang học từ ngày hiệu lực: còn trẻ thì giữ Open; không còn trẻ thì lớp chuyển sang Closed (OQ-02). Lớp đã có trẻ không bị xoá. |
| BR-013 | Mỗi trẻ được chuyển độc lập: một trẻ lỗi không chặn trẻ khác. Retry chỉ chạy lại trẻ Not moved và không chuyển trùng trẻ đã Moved. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up — bước Confirmation; kết quả | Prototype: Move children up › Confirmation |
| Classes — chi tiết lớp › Children, History | Prototype: Classes › chi tiết lớp |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tóm tắt xác nhận | Display | — | — | — | "n children move into <lớp đích> on <ngày>". |
| Done | Nút | — | — | — | Xác nhận lên lớp (FR-007). |
| Kết quả | Thẻ đếm + bảng | — | Sau khi xác nhận | — | Moved / Not moved / Stayed; cột Child, Destination class, Result, Reason (FR-009). |
| Retry | Nút | — | Chỉ hiện khi có trẻ Not moved | — | Chạy lại trẻ lỗi (BR-013). |
| Lớp cũ › Children | Danh sách | — | — | — | Vẫn hiện trẻ đã lên lớp, kèm trạng thái đã lên lớp, lớp mới và ngày kết thúc (BR-011). |
| Lớp cũ › trạng thái lớp | Nhãn | — | Open | — | Theo BR-012. |
| Lớp › History | Danh sách | — | — | — | Dòng lên lớp: lớp cũ → lớp mới, số trẻ, ngày hiệu lực, người thực hiện, thời điểm (FR-010). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi trẻ được chuyển lưu: lớp và level cũ, lớp và level mới, ngày hiệu lực, ngày kết thúc ở lớp cũ, trạng thái trong lớp cũ, người thực hiện, thời điểm xác nhận. |
| DATA-002 | Mỗi lần lên lớp lưu: lớp nguồn, lớp đích, ngày hiệu lực, số trẻ Moved, Not moved (kèm lý do), Stayed, trạng thái lớp nguồn sau khi chuyển, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-013 | 14 trẻ được chọn, ngày hiệu lực 04/01/2027 | Centre Director chọn Done | 14 trẻ ở lớp K1 · Honeycombs từ 04/01/2027; kết quả hiện 14 Moved | FR-007; FR-009 |
| AC-014 | đã xác nhận, hôm nay 15/12/2026 | giáo viên mở điểm danh lớp Sunbeams ngày 20/12/2026 | 14 trẻ vẫn ở Sunbeams; từ 04/01/2027 trẻ ở danh sách điểm danh Honeycombs | BR-009 |
| AC-015 | đã xác nhận | Centre Director mở lớp Sunbeams › Children sau 04/01/2027 | vẫn thấy 14 trẻ đã lên lớp, mỗi trẻ ghi trạng thái đã lên lớp, lớp K1 · Honeycombs, ngày kết thúc 03/01/2027; 2 trẻ ở lại ghi đang học | FR-008; BR-011 |
| AC-016 | 2 trẻ ở lại Sunbeams | qua ngày 04/01/2027 | lớp Sunbeams vẫn Open | BR-012 |
| AC-017 | tất cả 16 trẻ lên lớp | qua ngày 04/01/2027 | lớp Sunbeams chuyển Closed, danh sách 16 trẻ và lịch sử vẫn còn | BR-012 |
| AC-018 | hoá đơn tháng 1/2027 chưa tạo | hoá đơn tháng 1/2027 được tạo | 14 trẻ tính học phí K1 | BR-010 |
| AC-019 | 3 trẻ được chọn, việc chuyển của Chloe lỗi | Centre Director xem kết quả | 2 Moved, Chloe Not moved kèm lý do và vẫn ở Sunbeams; Retry chỉ chạy lại Chloe | BR-013 |
| AC-020 | Ethan đã Moved | Centre Director chọn Retry | Ethan không bị chuyển lần nữa; lịch sử Ethan chỉ có một dòng lên lớp | BR-013; DATA-001 |
| AC-021 | đã xác nhận | Centre Director mở lịch sử một trẻ | có dòng lớp cũ, lớp mới, ngày hiệu lực, người thực hiện | FR-010; DATA-001 |
| AC-022 | 14 trẻ đã lên Honeycombs từ 04/01/2027 | phụ huynh một trẻ mở Messages ngày 05/01/2027 | thấy thread lớp Honeycombs; thread Sunbeams chỉ đọc | BR-010 |

#### Dependencies (Phụ thuộc)

US-001, US-002; ghi danh; Fees & Payments (biểu phí theo level); danh sách điểm danh; Communication (thread của lớp).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Việc lên lớp có cần ai duyệt (ví dụ HQ Ops) trước khi có hiệu lực không? Có cho huỷ trước ngày hiệu lực không? | Centre Director / HQ Ops | Trung bình | |
| OQ-02 | Lớp cũ không còn trẻ từ ngày hiệu lực: hệ thống tự chuyển Closed hay Centre Director đóng tay? Tên trạng thái của trẻ trong lớp cũ sau khi lên lớp là gì (đề xuất "Moved up")? | Centre Director / HQ Ops | Trung bình | |
| OQ-03 | Trẻ đang tạm nghỉ (tối đa 3 tháng, vẫn trong hệ thống) có được lên lớp cùng lớp không? | Centre Director / HQ Ops | Trung bình | |
| OQ-04 | Phụ huynh và giáo viên có nhận thông báo khi lên lớp không? | Centre Director / HQ Ops | Thấp | |
| OQ-05 | Centre không mở level kế tiếp (ví dụ junior campus ở Malaysia): cuối năm dùng Bulk transfer children (Administration) hay Transfer từng trẻ; Centre nhận xếp trẻ vào level nào? | HQ Ops | Cao | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Level | Cấp lớp theo độ tuổi: Infant, Playgroup, N1, N2, K1, K2; mỗi Centre chỉ mở một số level. |
| Annual promotion | Cuối năm học, cả lớp lên level kế tiếp trong cùng Centre. |
| Lớp nguồn / lớp đích | Lớp hiện tại của trẻ / lớp năm học mới trẻ được chuyển tới. |
| Ngày hiệu lực | Ngày việc lên lớp bắt đầu áp dụng. |
| Học lại | Trẻ ở lại level cũ thêm một năm. |
| Graduation | Trẻ K2 rời trường vào tháng 12 (Joining & leaving). |
| Transfer | Trẻ chuyển sang Centre khác (Joining & leaving). |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Kết quả lên lớp | Moved, Not moved, Stayed. | Lựa chọn trẻ và kết quả xử lý. |
| Trạng thái lớp | Open, Closed. | Số trẻ đang học (BR-012). |
