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

Năm học chạy từ tháng 1 đến tháng 12. Tháng 11–12, Centre lập lớp của năm sau (tạo lớp, gán giáo viên). Cuối năm, người dùng chuyển cả lớp lên level kế tiếp (ví dụ N2 lên K1) vào lớp đã lập sẵn, thao tác một lần cho cả lớp thay vì chuyển từng trẻ. Lớp cũ và danh sách trẻ của lớp cũ vẫn được giữ.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Lên lớp cả lớp trong cùng Centre (annual promotion): chọn lớp đích đã có của năm học mới và ngày hiệu lực; bỏ chọn trẻ ở lại; xem tác động; xác nhận; kết quả từng trẻ; lịch sử. | Tạo lớp (Classes). Infant lên Playgroup theo tuổi 18 tháng (Infant promotion) và đổi lớp cùng level (Class change). K2 tốt nghiệp (Joining & leaving › Graduation). Chuyển Centre (Transfer). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Lớp và trẻ của Centre được cấp. | Lên lớp cả lớp, chạy lại trẻ lỗi. |
| Class Viewer | Lớp và trẻ trong phạm vi được cấp. | Xem lớp và lịch sử lớp; không thấy Move children up. |
| System | Lớp nguồn, lớp đích, trẻ được chọn. | Chuyển trẻ từ ngày hiệu lực, cập nhật dữ liệu liên quan, báo kết quả, lưu lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo Roles & permissions và phạm vi dữ liệu. Quyền tạo lớp thuộc Classes, không thuộc tính năng này.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Classes** | Chọn lớp đích và ngày hiệu lực | Mở Move children up từ chi tiết lớp; chọn lớp đích đã có của năm học mới và ngày hiệu lực. | BBA-72: US-001 |
| **Classes** | Chọn trẻ và xem tác động | Bỏ chọn trẻ ở lại; xem tác động trước khi xác nhận. | BBA-72: US-002 |
| **Classes** | Xác nhận và kết quả | Xác nhận lên lớp; xem kết quả từng trẻ; lịch sử. | BBA-72: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-72: US-001 - Chọn lớp đích và ngày hiệu lực

#### User Story

Là người dùng, tôi muốn chọn lớp đích của năm học mới và ngày hiệu lực cho cả lớp, để chuẩn bị lên lớp mà không phải chuyển từng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Người dùng có quyền mở luồng lên lớp từ chi tiết lớp (BR-001, BR-002). |
| FR-002 | Người dùng chọn lớp đích trong các lớp đã tạo sẵn (BR-003, BR-004; VAL-001). |
| FR-003 | Người dùng chọn ngày hiệu lực (BR-005). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở lớp, chọn Edit › Move children up (FR-001).
2. Hệ thống hiển thị danh sách lớp đích và ngày hiệu lực mặc định (FR-002, FR-003).
3. Người dùng chọn lớp đích, giữ hoặc đổi ngày hiệu lực, chọn Continue sang US-002.

#### Functional Flow - Alternative (Luồng thay thế)

1. Lớp ở level cao nhất của Centre: không có Move children up, có chỉ dẫn sang Graduation hoặc Transfer (BR-002).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Chưa có lớp đích: không tiếp tục được; người có quyền tạo lớp ở Classes rồi làm lại (BR-004; VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Chỉ lên lớp trong cùng Centre. Chuyển sang Centre khác, kể cả junior campus sang senior campus khác brand, là Transfer. |
| BR-002 | Lớp ở level cao nhất Centre mở không có Move children up. Lớp K2 chỉ dẫn sang Graduation (Joining & leaving); Centre không mở level kế tiếp chỉ dẫn sang Transfer. |
| BR-003 | Lớp đích thuộc level kế tiếp, năm học mới, cùng Centre. |
| BR-004 | Lớp đích phải được tạo trước ở Classes bởi người có quyền tạo lớp. Luồng lên lớp không tạo lớp. |
| BR-005 | Ngày hiệu lực mặc định là ngày bắt đầu năm học mới. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Centre chưa có lớp nào của level kế tiếp cho năm học mới. | Báo “There is no class at this centre for <level> the next academic year yet, so there is nowhere for these children to move to.”; không tiếp tục được. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up — bước Request | Prototype: Classes › chi tiết lớp › Move children up |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Move children up | Mục trong Edit | Theo quyền | Ẩn ở lớp level cao nhất | — | FR-001; BR-002. |
| Thanh bước | Display | — | Request | — | Request › Rules and effective date › Impact › Confirmation. |
| Destination class — next year | Danh sách chọn | Có | — | VAL-001. | Các lớp theo BR-003 (FR-002). |
| Effective date | Chọn ngày | Có | Theo BR-005 | — | FR-003. |
| Back / Continue / Close | Nút | — | — | VAL-001. | Chuyển bước hoặc đóng. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Bước chọn lớp đích không lưu dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp N2 · Sunbeams năm 2026; Centre đã tạo lớp K1 · Honeybees năm 2027 | người dùng chọn Edit › Move children up | danh sách lớp đích có K1 · Honeybees năm 2027 của cùng Centre; ngày hiệu lực mặc định là ngày bắt đầu năm học 2027 | FR-001; FR-002; FR-003; BR-001; BR-003; BR-005; DATA-001 |
| AC-002 | Centre chưa tạo lớp K1 năm 2027 | người dùng chọn Move children up ở lớp N2 | hiện thông báo VAL-001; không có nút tạo lớp; không tiếp tục được | FR-002; BR-004; VAL-001 |
| AC-003 | lớp K2 · Blossom | người dùng mở Edit | không có Move children up; có chỉ dẫn sang Graduation | BR-002 |
| AC-004 | Centre chỉ mở tới N2 | người dùng mở Edit của lớp N2 | không có Move children up; có chỉ dẫn sang Transfer | BR-002 |
| AC-005 | Teacher không có quyền lên lớp | Teacher mở Edit của lớp | không có Move children up | FR-001 |

#### Dependencies (Phụ thuộc)

Classes (lớp năm học mới, sĩ số); level Centre mở (Organisation); Joining & leaving (Graduation, Transfer).

### 6.2 BBA-72: US-002 - Chọn trẻ và xem tác động

#### User Story

Là người dùng, tôi muốn bỏ chọn trẻ ở lại và xem việc lên lớp ảnh hưởng gì, để chắc chắn trước khi xác nhận.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Hệ thống liệt kê trẻ của lớp nguồn; người dùng bỏ chọn trẻ ở lại (BR-006; VAL-002). |
| FR-005 | Hệ thống hiển thị tác động của việc lên lớp trước khi xác nhận (BR-007, BR-008). |

#### Functional Flow - Main (Luồng chính)

1. Hệ thống hiển thị danh sách trẻ của lớp nguồn (FR-004).
2. Người dùng bỏ chọn trẻ ở lại, chọn Continue (FR-004).
3. Hệ thống hiển thị tác động; người dùng chọn Continue sang US-003 (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lớp đích vượt sĩ số tối đa: hiển thị cảnh báo, vẫn tiếp tục được (BR-008).
2. Người dùng chọn Back để đổi lớp đích hoặc ngày hiệu lực (US-001).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Lớp nguồn không có trẻ: không có trẻ để chọn (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Mặc định chọn cả lớp. Người dùng bỏ chọn trẻ ngoại lệ (ví dụ học lại). Trẻ bị bỏ chọn ở lại lớp nguồn, không thay đổi gì. |
| BR-007 | Tác động gồm: Class — số trẻ vào lớp đích, sĩ số lớp đích sau khi chuyển, số trẻ còn lại ở lớp nguồn và số lần xếp lớp kết thúc; Enrolment — level đổi từ level cũ sang level mới vào ngày hiệu lực; Billing — học phí tính lại theo level mới từ ngày hiệu lực; Access — thread tin nhắn mới với giáo viên lớp đích, thread cũ vẫn đọc được. |
| BR-008 | Sĩ số tối đa của lớp do Centre Director cấu hình. Lớp đích vượt sĩ số tối đa chỉ cảnh báo, không chặn. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-002 | Lớp nguồn không có trẻ. | Hiển thị “No children are in this class.” |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Move children up — bước Rules and effective date, Impact | Prototype: Move children up › Continue |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Danh sách trẻ | Danh sách có ô chọn | — | Tất cả được chọn | VAL-002. | Mỗi dòng: tên trẻ, “Moves up” khi được chọn, “Stays in <lớp nguồn>” khi bỏ chọn (FR-004; BR-006). |
| Impact | Section | — | — | — | Các dòng theo nhóm Class, Enrolment, Billing, Access (BR-007). |
| Cảnh báo sĩ số | Thông báo | — | Khi vượt sĩ số | — | “<lớp đích> would hold <n> of <tối đa>” (BR-008). |
| Back / Continue | Nút | — | — | — | — |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Xem trước không lưu dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-006 | lớp Sunbeams có 16 trẻ | người dùng sang bước chọn trẻ | 16 trẻ được chọn sẵn, mỗi trẻ ghi “Moves up” | FR-004; BR-006 |
| AC-007 | 2 trẻ học lại N2 | người dùng bỏ chọn 2 trẻ, sang bước Impact | 2 trẻ ghi “Stays in N2 · Sunbeams”; Impact hiện “14 of 16 children move into K1 · Honeybees” | FR-004; FR-005; BR-006; BR-007; DATA-002 |
| AC-008 | lớp Honeybees tối đa 20, đã có 8 trẻ; 14 trẻ được chọn | người dùng xem Impact | hiện “K1 · Honeybees would hold 22 of 20” kèm cảnh báo; Continue vẫn bật | BR-008 |
| AC-009 | ngày hiệu lực 04/01/2027 | người dùng xem Impact | có dòng “Level moves from N2 to K1 on 2027-01-04”, “Fees re-resolve from the new level on that date” và dòng thread tin nhắn mới | BR-007 |
| AC-010 | lớp nguồn không có trẻ | người dùng mở Move children up | hiện “No children are in this class.” | VAL-002 |

#### Dependencies (Phụ thuộc)

US-001; ghi danh của trẻ; biểu phí theo level (Fees & Payments); thread của lớp (Communication).

### 6.3 BBA-72: US-003 - Xác nhận và kết quả

#### User Story

Là người dùng, tôi muốn xác nhận một lần để cả lớp lên lớp mới mà lớp cũ vẫn giữ danh sách trẻ, và biết trẻ nào đã chuyển, trẻ nào lỗi, để xử lý tiếp.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-006 | Người dùng xác nhận; hệ thống chuyển trẻ được chọn sang lớp đích (BR-009, BR-010, BR-011, BR-012). |
| FR-007 | Hệ thống hiển thị kết quả từng trẻ và cho chạy lại trẻ lỗi (BR-013). |
| FR-008 | Hệ thống ghi lịch sử cho từng trẻ và cho lớp (DATA-003, DATA-004). |

#### Functional Flow - Main (Luồng chính)

1. Ở bước Confirmation, hệ thống tóm tắt “n children move into <lớp đích> on <ngày>”; người dùng chọn Done (FR-006).
2. Hệ thống chuyển trẻ và ghi lịch sử (FR-006, FR-008).
3. Hệ thống hiển thị kết quả từng trẻ (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Có trẻ không chuyển được: người dùng chọn Retry để chạy lại trẻ lỗi (FR-007; BR-013).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Lỗi khi chuyển một trẻ: trẻ đó giữ lớp cũ, các trẻ khác vẫn được chuyển (BR-013).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-009 | Trẻ vào lớp đích, level trong ghi danh đổi và học phí tính theo level mới từ ngày hiệu lực. |
| BR-010 | Hoá đơn đã phát hành không bị sửa, không bị void; điều chỉnh hoá đơn đã phát hành làm bằng credit note theo Fees & Payments. |
| BR-011 | Trẻ lên lớp có thread tin nhắn mới với lớp đích. Thread lớp cũ chuyển inactive, chỉ xem, giữ tới khi trẻ rời trường. |
| BR-012 | Lớp và danh sách học sinh ở lớp cũ vẫn tồn tại: với mỗi trẻ được chuyển, lần xếp lớp ở lớp cũ kết thúc và trạng thái của trẻ trong lớp cũ được cập nhật; trạng thái lớp cũ được cập nhật. Trẻ bị bỏ chọn giữ nguyên ở lớp cũ. Lớp đã có trẻ chỉ được đóng, không bị xoá; lịch sử được giữ. |
| BR-013 | Mỗi trẻ được chuyển độc lập: một trẻ lỗi không chặn trẻ khác. Retry chỉ chạy lại trẻ lỗi, không chuyển trùng trẻ đã chuyển. |

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
| Kết quả | Bảng | — | Sau khi xác nhận | — | Trẻ, lớp đích, kết quả (đã chuyển / lỗi / ở lại), lý do lỗi (FR-007). |
| Retry | Nút | — | Khi có trẻ lỗi | — | BR-013. |
| Lớp cũ › Children | Danh sách | — | — | — | Vẫn hiện trẻ đã lên lớp, kèm trạng thái mới (BR-012). |
| Lớp › History | Danh sách | — | — | — | Dòng lên lớp: lớp cũ → lớp mới, số trẻ, ngày hiệu lực, người thực hiện, thời điểm (FR-008). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi trẻ được chuyển lưu: lớp và level cũ, lớp và level mới, ngày hiệu lực, trạng thái trong lớp cũ, người thực hiện, thời điểm xác nhận. |
| DATA-004 | Mỗi lần lên lớp lưu: lớp nguồn, lớp đích, ngày hiệu lực, số trẻ đã chuyển, lỗi (kèm lý do), ở lại, người thực hiện, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-011 | 14 trẻ được chọn, ngày hiệu lực 04/01/2027 | người dùng chọn Done | 14 trẻ ở lớp K1 · Honeybees, level K1 từ 04/01/2027; kết quả hiện 14 trẻ đã chuyển | FR-006; FR-007; BR-009 |
| AC-012 | hoá đơn tháng 12/2026 của 14 trẻ đã phát hành theo level N2 | người dùng xác nhận lên lớp | hoá đơn tháng 12/2026 không đổi | BR-010 |
| AC-013 | 14 trẻ đã lên Honeybees | phụ huynh một trẻ mở Messages sau ngày hiệu lực | thấy thread lớp Honeybees; thread Sunbeams chỉ xem | BR-011 |
| AC-014 | đã xác nhận | người dùng mở lớp Sunbeams › Children sau ngày hiệu lực | vẫn thấy 14 trẻ đã lên lớp kèm trạng thái mới; 2 trẻ ở lại không đổi | BR-012 |
| AC-015 | lớp Sunbeams đã có trẻ | người dùng tìm thao tác xoá lớp | không có thao tác xoá; lịch sử lớp còn | BR-012 |
| AC-016 | 3 trẻ được chọn, việc chuyển của Chloe lỗi | người dùng xem kết quả | 2 trẻ đã chuyển; Chloe lỗi kèm lý do và vẫn ở Sunbeams; Retry chỉ chạy lại Chloe | FR-007; BR-013 |
| AC-017 | Ethan đã chuyển | người dùng chọn Retry | Ethan không bị chuyển lần nữa; lịch sử Ethan có một dòng lên lớp | BR-013; DATA-003 |
| AC-018 | đã xác nhận | người dùng mở History của lớp Sunbeams | có dòng lên lớp: lớp cũ, lớp mới, số trẻ, ngày hiệu lực, người thực hiện | FR-008; DATA-004 |

#### Dependencies (Phụ thuộc)

US-001, US-002; ghi danh; Fees & Payments (biểu phí theo level, credit note); Communication (thread của lớp).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Có cho lên lịch trước và huỷ trước ngày hiệu lực không? Có chặn ngày hiệu lực trong quá khứ không? (Q-74-07 chưa trả lời) | Centre Director / HQ Ops | Trung bình |  |
| OQ-02 | Lớp cũ hết trẻ: tự chuyển Closed hay người dùng đóng tay? Tên trạng thái của trẻ trong lớp cũ sau khi lên lớp? (Q-74-15 chưa trả lời) | Centre Director / HQ Ops | Trung bình |  |
| OQ-03 | Trẻ ở trạng thái nào được lên lớp? Trẻ đang tạm nghỉ (tối đa 3 tháng, vẫn trong hệ thống), trẻ có withdrawal hoặc transfer chờ hiệu lực có được chọn không? (Q-74-06 chưa nói) | Centre Director / HQ Ops | Cao |  |
| OQ-04 | Phụ huynh và giáo viên có nhận thông báo khi lên lớp không, hay Centre dùng Announcement? (Q-74-15 chưa trả lời) | Centre Director / HQ Ops | Thấp |  |
| OQ-05 | Centre không mở level kế tiếp: cuối năm dùng Bulk transfer children (Administration) hay Transfer từng trẻ? | HQ Ops | Cao |  |
| OQ-06 | Trẻ ở lại giữ lớp hoặc chuyển sang lớp khác cùng level (Q-74-03). Có cần chia một lớp nguồn sang nhiều lớp đích hoặc đổi lớp đích cho từng trẻ không? | HQ Ops | Cao |  |
| OQ-07 | Hệ thống có tự đề xuất lớp đích không, theo quy tắc nào? (Q-74-03 chưa có quy tắc) | HQ Ops | Trung bình |  |
| OQ-08 | Học phí theo level mới áp từ ngày hiệu lực hay từ đầu tháng sau? (Q-74-09 chưa rõ) | HQ Finance | Cao |  |
| OQ-09 | Danh sách điểm danh và thread chuyển ngay khi xác nhận hay vào ngày hiệu lực? (Q-74-10 chưa trả lời) | HQ Ops | Trung bình |  |

## 8. Phụ lục

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

### Phụ lục C. Nguồn đối chiếu

| Nội dung | Nguồn |
|---|---|
| Chỉ cùng Centre; Transfer; Graduation | Excel Q-74-01, Q-74-02 |
| Lớp đích tạo trước ở Classes, luồng không tạo lớp | Góp ý trên Drive 26/11/2026; Excel Q-74-07 |
| Bỏ chọn trẻ ngoại lệ | SRS Children & Families P6; Excel Q-74-03 |
| Sĩ số chỉ cảnh báo | Excel Q-74-08; SRS BR-CHF-045 |
| Hoá đơn đã phát hành, credit note | Excel Q-74-09 |
| Thread lớp cũ inactive, giữ tới khi rời trường | Excel Q-74-10 |
| Tác động (Impact), thông báo chưa có lớp đích | Prototype Move children up; Excel Q-74-11 (DOTB tự quyết) |
| Lỗi từng trẻ, Retry không chuyển trùng | Excel Q-74-12, Q-74-13 (DOTB tự quyết) |
| Lớp có trẻ chỉ đóng, không xoá | SRS BR-CHF-049 |
| Ngày hiệu lực mặc định | SRS Children & Families P6 |
