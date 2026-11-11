# BBA-67 US-002 Tab Enrichment – bản nháp (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Child record |
| Tính năng | 3.1.1.02 Child record tabs – Read views › Tab Enrichment (US-002) |
| Mã ticket | BBA-67 |
| Mã WBS | 3.1.1.02 |
| Mã tài liệu | FRD-3.1_Child_Record_Read_Tabs — bản nháp US-002 |
| Sprint | 4 |
| Phiên bản | 0.1 (nháp) |
| Trạng thái | BẢN NHÁP ĐỂ RÀ SOÁT |
| Ngày | 11/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 (nháp) | 11/11/2026 | Business Analysis | Bản nháp riêng cho US-002 theo SRS Learning v0.1 mục 7.1, 7.2; giữ các quy tắc hiển thị của FRD v0.4. Mã FR, BR, VAL, AC đánh tiếp theo FRD v0.4. | HaiNguyen |

**Mức sẵn sàng:** Đã mô tả các lớp enrichment của trẻ (tên lớp, chương trình, lịch học, trainer, phí mỗi buổi, ngày bắt đầu, ngày kết thúc, trạng thái), cách hiển thị lớp đang học và đã kết thúc, phạm vi xem của trainer. 2 câu hỏi mở ở mục 5 cần BBA chốt.

## 2. Tab Enrichment hiểu theo SRS Learning

| Điểm chính | Căn cứ trong SRS Learning v0.1 |
|---|---|
| Tab là cửa sổ nhìn sang Learning, không phải nơi quản lý. HQ Enrichment team tạo lớp, thêm và gỡ học sinh; muốn thay đổi thì vào Learning › Enrichment. | §2 Who uses it (tr.4); BR-LRN-033 (tr.11) |
| Các lớp enrichment của trẻ được hiển thị trên hồ sơ trẻ; một trẻ có thể học nhiều lớp. | §7.2 Show on child profile (tr.9); BR-LRN-036 (tr.11) |
| Thông tin của lớp: tên lớp, chương trình, lịch học (thứ, giờ), trainer, phí mỗi buổi. | §7.1 View class list, Create class (tr.8) |
| Thông tin của trẻ trong lớp: ngày bắt đầu, ngày kết thúc, trạng thái Active / Left. | §7.2 View students in class (tr.9) |
| Mục đích: người xem hồ sơ trẻ biết trẻ đang học thêm gì, từ khi nào, với ai; trả lời được phụ huynh, hiểu vì sao có hoá đơn enrichment (phí tháng = số buổi theo lịch × phí mỗi buổi) và biết lịch của trẻ trong ngày. | §3 P5, P6 (tr.5); BR-LRN-040, BR-LRN-044 (tr.11) |

## 3. Những gì thay đổi so với US-002 hiện tại (FRD v0.4)

| Nội dung | US-002 hiện tại | Bản nháp này | Lý do |
|---|---|---|---|
| Thông tin mỗi lớp | Programme (tên, loại), Centre, Day and time, Trainer, Start date, End date, Sessions attended this month. | Class name, Programme, Schedule, Trainer, Fee per session, Start date, End date, Status. | Lấy đúng SRS Learning §7.1, §7.2. |
| Phí mỗi buổi, trạng thái Active / Left | Chưa có. | Có. | §7.1, §7.2. |
| Số buổi tham dự trong tháng | Có. | Không đưa vào. | Không thuộc §7.1, §7.2; điểm danh enrichment chỉ để theo dõi (BR-LRN-039); chờ OQ-RT-03. |
| Centre của lớp | Có. | Không đưa vào. | Ngoài danh sách thông tin đã chốt. |
| Current / Past | Theo việc đã có End date (AS-RT-03). | Theo trạng thái Active / Left. | §7.2 có trạng thái; không cần giả định AS-RT-03 nữa. |
| Cách kết thúc | "Withdrawn in the Parents App", "No refund", "Switched to / from", "Left the school". | Chỉ các cách có trong SRS: Enrichment team gỡ trẻ khỏi lớp, trẻ thôi học ở Centre, lớp bị đóng. | SRS Learning §1.2: đăng ký và rút qua Parents App không thuộc Phase 1; đổi chương trình không có trong SRS. Chờ OQ-RT-17. |
| Quy tắc hiển thị | End date "—" khi đang học; mặc định Current; Start date mới nhất trước; liên kết tên lớp; trạng thái rỗng; dòng "Left the school · enrichment invoices stop after …". | Giữ nguyên. | Theo yêu cầu giữ quy tắc hiển thị. |
| Nút thêm, sửa, gỡ | Không nêu. | Ghi rõ không có. | Tab chỉ để xem. |

## 4. Yêu cầu chức năng

### 4.1 US-002 - Tab Enrichment: các lớp enrichment của trẻ

#### User Story

Là School Admin, tôi muốn xem trẻ đang học thêm những lớp enrichment nào, từ khi nào, với trainer nào, lịch học và phí mỗi buổi, để trả lời phụ huynh, giải thích hoá đơn enrichment và biết lịch của trẻ trong ngày.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-006 | Tab Enrichment chỉ hiển thị; không có nút thêm, sửa hay gỡ trẻ khỏi lớp. Mọi thay đổi thực hiện ở Learning › Enrichment. |
| FR-007 | Section "Enrichment programmes" hiển thị mỗi lớp enrichment của trẻ một dòng: Class name, Programme, Schedule (thứ và giờ, ví dụ "Tue 15:30–16:15"), Trainer, Fee per session (ví dụ "SGD 30"), Start date, End date, Status (Active / Left). |
| FR-008 | Bộ lọc Current / Past: mặc định Current (lớp có trạng thái Active); Past hiển thị lớp có trạng thái Left. |
| FR-009 | Lớp trẻ đang học có End date "—"; End date chỉ có khi trẻ rời lớp. Các dòng sắp theo Start date, mới nhất trước. |
| FR-010 | Dòng lớp đã kết thúc ghi cách kết thúc: "Removed from the class" (Enrichment team gỡ trẻ, kèm End date); "Class closed" (lớp bị đóng, End date là ngày đóng lớp); "Left the school · enrichment invoices stop after" kèm ngày học cuối (trẻ thôi học ở Centre). |
| FR-011 | Chọn tên lớp mở màn chi tiết lớp enrichment trong Learning › Enrichment. |
| FR-012 | Trẻ chưa học lớp enrichment nào: hiển thị "No enrichment programme for this child." |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn tab Enrichment; hệ thống hiển thị các lớp đang học (FR-006, FR-007, FR-008).
2. Người dùng xem lịch học, trainer, phí mỗi buổi để trả lời phụ huynh (FR-007).
3. Người dùng chọn tên lớp(FR-011).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Past để xem các lớp đã kết thúc và cách kết thúc (FR-008, FR-010).
2. Trẻ thôi học ở Centre: mọi lớp enrichment đang học kết thúc vào ngày học cuối (FR-010; BR-008).
3. Trẻ chưa học enrichment: trạng thái rỗng (FR-012).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Enrichment Trainer mở hồ sơ trẻ không thuộc lớp enrichment của mình: hồ sơ không mở (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-004 | Enrichment Trainer chỉ thấy lớp enrichment được giao cho mình (BR-LRN-033). |
| BR-005 | HQ Enrichment team quản lý lớp và học sinh enrichment; hồ sơ trẻ chỉ hiển thị (BR-LRN-033). |
| BR-006 | Một trẻ có thể học nhiều lớp enrichment; mọi lớp đều hiện trên hồ sơ trẻ (BR-LRN-036). |
| BR-007 | Mỗi trẻ trong lớp có ngày bắt đầu; gỡ trẻ khỏi lớp phải có ngày kết thúc; không tính phí sau ngày kết thúc (BR-LRN-035; SRS Learning §7.2 Remove student). |
| BR-008 | Trẻ thôi học ở Centre thì mọi lớp enrichment kết thúc vào ngày học cuối của trẻ (BR-LRN-037). |
| BR-009 | Lớp bị đóng thì trẻ đang học có ngày kết thúc là ngày đóng lớp (SRS Learning §7.1 Close class). |
| BR-010 | Phí enrichment hằng tháng của mỗi lớp = số buổi theo lịch trong tháng, từ ngày bắt đầu đến ngày kết thúc, × phí mỗi buổi; ngày lễ vẫn tính, buổi vắng không trừ (BR-LRN-040; BR-LRN-042). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Trẻ không thuộc lớp enrichment nào của Enrichment Trainer. | Không hiển thị hồ sơ trẻ cho Enrichment Trainer. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-02 - Tab Enrichment | Chưa có wireframe cho bản nháp này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Current / Past | Bộ lọc | Có | Current | — | FR-008. |
| Section Enrichment programmes | Danh sách | Có | Start date mới nhất trước | — | Các cột ở FR-007; tên lớp là liên kết (FR-011). |
| Cách kết thúc | Text | Khi trạng thái Left | — | — | FR-010. |
| Trạng thái rỗng | Text | Khi không có lớp | "No enrichment programme for this child." | — | FR-012. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Tab đọc từ Learning › Enrichment: lớp (class name, programme, weekdays, start time, end time, trainer, fee per session, status Active / Closed, ngày đóng lớp), trẻ trong lớp (start date, end date, status Active / Left, cách kết thúc: gỡ khỏi lớp, lớp đóng, thôi học ở Centre). Tab không ghi dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-008 | Ethan học Mandarin Explorers (thứ Ba 15:30–16:15, SGD 30 mỗi buổi) và Speech & Drama (thứ Năm 15:30–16:30) từ 2026-07-01 | School Admin mở tab Enrichment | có 2 dòng, mỗi dòng có Class name, Programme, Schedule, Trainer, Fee per session, Start date 2026-07-01, End date "—", Status Active | FR-007; FR-008; FR-009; DATA-002 |
| AC-009 | Ethan học 2 lớp enrichment | School Admin xem tab Enrichment | không có nút thêm, sửa hay gỡ trẻ khỏi lớp | FR-006; BR-005; BR-006 |
| AC-010 | Enrichment team gỡ Ethan khỏi Little Chefs, End date 2026-06-30 | School Admin chọn Past | Little Chefs hiện Status Left, End date 2026-06-30, "Removed from the class" | FR-008; FR-010; BR-007 |
| AC-011 | lớp Art Explorers bị đóng ngày 2026-12-18 khi Ethan đang học | School Admin chọn Past | Art Explorers hiện Status Left, End date 2026-12-18, "Class closed" | FR-010; BR-009 |
| AC-012 | Lucas thôi học ở Centre, ngày học cuối 2026-10-31, đang học Speech & Drama | School Admin mở tab Enrichment sau 2026-10-31 | Speech & Drama ở Past với End date 2026-10-31 và "Left the school · enrichment invoices stop after 2026-10-31" | FR-010; BR-008 |
| AC-013 | lớp Mandarin Explorers học thứ Ba, SGD 30 mỗi buổi; tháng 10/2026 có 4 thứ Ba | phụ huynh hỏi vì sao hoá đơn enrichment tháng 10 của Ethan có SGD 120 | School Admin thấy trên tab Schedule "Tue" và Fee per session "SGD 30", đủ để giải thích 4 buổi × SGD 30 | FR-007; BR-010 |
| AC-014 | School Admin đang xem tab Enrichment | chọn "Mandarin Explorers" | màn chi tiết lớp Mandarin Explorers trong Learning › Enrichment mở | FR-011 |
| AC-015 | Adam chưa học enrichment | School Admin mở tab Enrichment | hiện "No enrichment programme for this child." | FR-012 |
| AC-016 | Enrichment Trainer dạy Speech & Drama, Adam không học lớp này | trainer tìm Adam | không mở được hồ sơ Adam | VAL-001; BR-004 |

#### Dependencies (Phụ thuộc)

Learning › Enrichment (lớp, trẻ trong lớp); Joining & leaving (ngày học cuối khi trẻ thôi học); Fees & Payments (hoá đơn enrichment).

## 5. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-RT-03 | Tab Enrichment có cần hiển thị số buổi tham dự hoặc chi tiết từng buổi (có mặt / vắng) không? SRS Learning §7.3 có điểm danh từng buổi nhưng chỉ để theo dõi, không ảnh hưởng phí. | Business Owner | Thấp |  |
| OQ-RT-17 | FRD v0.4 có quy tắc "rút enrichment qua Parents App, không hoàn tiền" và "đổi chương trình báo trước 1 tháng". SRS Learning §1.2 ghi đăng ký và rút qua Parents App không thuộc Phase 1, và không nói tới đổi chương trình. Hai quy tắc này có áp dụng ở Phase 1 không? | Business Owner | Cao |  |

Khi gộp vào FRD chính: bỏ giả định AS-RT-03 vì Current / Past đã theo trạng thái Active / Left của SRS.

## 6. Tài liệu tham khảo

Số trang tính theo bản Word gốc của SRS khi xuất PDF khổ A4.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | Plane — dự án BBA Phase 1, ticket BBA-67 (WBS 3.1.1.02) | Description: enrichment programmes, each linking to the module screen | — | Phạm vi US-002. |
| 2 | BBA-SMS-SRS-Learning-v0.1 | §1.2 Not in Phase 1 (Enrichment) | 3 | OQ-RT-17. |
| 3 | BBA-SMS-SRS-Learning-v0.1 | §2 Who uses it (HQ Enrichment team, Enrichment trainer) | 4 | BR-004; BR-005. |
| 4 | BBA-SMS-SRS-Learning-v0.1 | §3 P5 Enrichment class and students; P6 Enrichment monthly charges | 5 | Mục 2; BR-010. |
| 5 | BBA-SMS-SRS-Learning-v0.1 | §7.1 Enrichment classes (View class list, Create class) | 8 | FR-007. |
| 6 | BBA-SMS-SRS-Learning-v0.1 | §7.1 Enrichment classes (Close class, Restrict trainer view) | 9 | BR-004; BR-009. |
| 7 | BBA-SMS-SRS-Learning-v0.1 | §7.2 Enrichment students (View students in class, Show on child profile, Remove student, Auto-end on centre withdrawal) | 9 | FR-007; FR-010; BR-007; BR-008. |
| 8 | BBA-SMS-SRS-Learning-v0.1 | §7.3 Enrichment attendance | 9 | OQ-RT-03. |
| 9 | BBA-SMS-SRS-Learning-v0.1 | §5 Enrichment classes and students (BR-LRN-033, 035, 036, 037, 039); Enrichment charges (BR-LRN-040, 042, 044) | 11 | BR-004 đến BR-010. |
