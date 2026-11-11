# BBA-67 US-001 Tab Enrolment – bản nháp (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Child record |
| Tính năng | 3.1.1.02 Child record tabs – Read views › Tab Enrolment (US-001) |
| Mã ticket | BBA-67 |
| Mã WBS | 3.1.1.02 |
| Mã tài liệu | FRD-3.1_Child_Record_Read_Tabs — bản nháp US-001 |
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
| 0.1 (nháp) | 11/11/2026 | Business Analysis | Bản nháp riêng cho US-001 sau khi rà soát lại theo SRS Children & Families v0.1 và ticket BBA-67; dùng để thay mục 6.1 của FRD Child Record Tabs – Read Views khi được duyệt. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả các lần ghi danh, dòng thời gian thay đổi trạng thái và programme, lịch sử lớp học, việc thay đổi trạng thái đang chờ (case) và các trường hợp đặc biệt. 7 câu hỏi mở ở mục 4 cần BBA chốt.

## 2. Những gì thay đổi so với US-001 hiện tại

| Nội dung | US-001 hiện tại (v0.2) | Bản nháp này | Lý do |
|---|---|---|---|
| Lịch sử lớp học | "Đổi lớp" nằm trong dòng thời gian, lấy từ Joining & Leaving. | Tách thành phần "Lịch sử lớp học": xếp lớp, đổi lớp, lên playgroup lúc 18 tháng, lên lớp đầu năm học. | Đổi lớp do Classes ghi nhận (BR-CHF-046); SRS có tab "Class history" riêng. |
| Đổi programme | Chưa có. | Có trong dòng thời gian, lấy từ change record. | SRS: đổi programme nửa ngày ↔ cả ngày tạo change record (AC-CHF-004). |
| Trạng thái của lần ghi danh | Chưa nêu danh sách. | Enrolled, Temporary withdrawal, Withdrawn, Graduated. | BR-CHF-006. |
| Liên kết "Start a withdrawal / temporary withdrawal / transfer" | Có (FR-005). | Bỏ. | Là thao tác tạo, trái với tab chỉ đọc; chờ OQ-RT-17. |
| Đánh dấu SUG / Staff / KA child | Có (FR-006). | Bỏ khỏi tab Enrolment. | Không có trong ticket BBA-67 và SRS Children & Families; là thông tin học phí mà Teacher không được xem; đề xuất chuyển sang tab Finance, chờ OQ-RT-04. |
| Trạng thái "Transferred" ở AC-003 | Có. | Thay bằng câu hỏi mở. | Không có trong 4 trạng thái của SRS; chờ OQ-RT-12. |
| Trường hợp đặc biệt | Chưa có. | Hồ sơ tạo tay, trẻ chưa sinh, lớp đã đóng, trẻ đã thôi học. | BR-CHF-001, 002, 007, 008, 049. |

## 3. Yêu cầu chức năng

### 3.1 US-001 - Tab Enrolment: lịch sử ghi danh và lớp học

#### User Story

Là School Admin, tôi muốn xem trên hồ sơ trẻ các lần ghi danh, các lần đổi trạng thái, đổi programme và lịch sử lớp học của trẻ, để trả lời phụ huynh về ngày bắt đầu học, lớp, chương trình học hay tiến độ thôi học mà không phải mở Joining & Leaving.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab Enrolment chỉ hiển thị, không có thao tác sửa hay tạo; gồm 3 phần theo thứ tự: Cases, Các lần ghi danh, Lịch sử lớp học. |
| FR-002 | Đầu phần "Các lần ghi danh" có dòng tóm tắt số lần ghi danh và số lần đang học, ví dụ "2 enrolments · 1 running now". Lần ghi danh đang học là lần có trạng thái Enrolled hoặc Temporary withdrawal (AS-RT-08). |
| FR-003 | Danh sách các lần ghi danh: lần đang học ở đầu, các lần còn lại mới nhất trước. Mỗi lần ghi danh hiển thị: Centre (kèm brand), level, lớp hiện tại của lần ghi danh, trạng thái (Enrolled, Temporary withdrawal, Withdrawn, Graduated), programme (Full day / Half day), ngày ghi danh, ngày bắt đầu học, ngày kết thúc (đang học thì hiện "—"), pháp nhân, loại chương trình, năm học (các trường sau Centre chờ OQ-RT-13). |
| FR-004 | Mỗi lần ghi danh có dòng thời gian thay đổi, mới nhất trước: bắt đầu học, tạm nghỉ, quay lại sau tạm nghỉ, chuyển Centre, thôi học, tốt nghiệp (từ Joining & Leaving) và đổi programme (từ change record của hồ sơ trẻ). Mỗi dòng ghi: loại thay đổi, giá trị trước → sau nếu có (ví dụ "Half day → Full day"), ngày hiệu lực, người thực hiện, người duyệt nếu có. |
| FR-005 | Phần "Lịch sử lớp học" liệt kê mỗi lần trẻ vào một lớp, mới nhất trước: level · lớp (ví dụ "N2 · Sunbeams"), từ ngày – đến ngày (lớp hiện tại thì "đến ngày" hiện "—"), lý do (xếp lớp, đổi lớp, lên playgroup lúc 18 tháng, lên lớp đầu năm học), người thực hiện. |
| FR-006 | Phần "Cases" hiển thị việc thay đổi trạng thái đang chờ của trẻ (thôi học, tạm nghỉ, chuyển Centre): loại, ngày tạo, bước đang chờ, ví dụ "Withdrawal raised 2026-09-30 · waiting on the Centre Director". Không có case đang mở thì hiện "No open case." (AS-RT-10). |
| FR-007 | Chọn một lần ghi danh mở màn chi tiết ghi danh của Joining & Leaving; chọn một case mở màn case của Joining & Leaving; chọn một lớp trong lịch sử lớp học mở màn chi tiết lớp của Classes. |
| FR-008 | Hồ sơ trẻ chưa có lần ghi danh nào: phần "Các lần ghi danh" hiện "No enrolment for this child." (chờ OQ-RT-14). |
| FR-009 | Trẻ chưa sinh: lần ghi danh hiện ngày bắt đầu học dự kiến, ví dụ "Starts 2027-03-01" (AS-RT-12). |

#### Functional Flow - Main (Luồng chính)

1. School Admin mở hồ sơ trẻ và chọn tab Enrolment (FR-001).
2. Hệ thống hiển thị Cases, dòng tóm tắt, danh sách các lần ghi danh kèm dòng thời gian, và lịch sử lớp học (FR-002 đến FR-006).
3. School Admin chọn một lần ghi danh, một case hoặc một lớp để mở màn của module sở hữu (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ đã chuyển Centre hoặc ghi danh lại: danh sách hiện đủ các lần ghi danh, lần đang học ở đầu (FR-003).
2. Trẻ đã thôi học hoặc tốt nghiệp: tab vẫn hiển thị đầy đủ lịch sử; dòng tóm tắt ghi "0 running now" (FR-002; BR-002).
3. Lớp cũ của trẻ đã đóng: lịch sử lớp học vẫn hiện tên lớp đó (FR-005; BR-002).
4. Trẻ ở lại lớp khi lên lớp đầu năm học: lịch sử lớp học không có dòng mới cho năm đó (FR-005; BR-003).
5. Hồ sơ trẻ chưa có lần ghi danh: hiện "No enrolment for this child." (FR-008).
6. Trẻ chưa sinh: lần ghi danh hiện ngày bắt đầu học dự kiến (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò không được xem tab Enrolment (Enrichment Trainer theo mục 4 của FRD): không có tab Enrolment (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Trạng thái của trẻ chỉ đổi qua Joining & Leaving; tab Enrolment chỉ hiển thị (BR-CHF-006; AC-CHF-005). |
| BR-002 | Lần ghi danh, dòng thời gian và lịch sử lớp học không bị xoá; trẻ đã thôi học, tốt nghiệp và lớp đã đóng vẫn xem được (BR-CHF-007; BR-CHF-008; BR-CHF-049). |
| BR-003 | Mọi lần vào lớp có ngày hiệu lực; lên lớp đầu năm học lấy đầu năm học mới làm ngày hiệu lực; trẻ sơ sinh lên playgroup lúc 18 tháng (BR-CHF-046; BR-CHF-047; BR-CHF-048). |
| BR-004 | Đổi programme được ghi bằng change record có người sửa, người duyệt và ngày hiệu lực (BR-CHF-005; AC-CHF-004). |
| BR-005 | Người được mở hồ sơ trẻ thấy toàn bộ lịch sử ghi danh của trẻ, kể cả lần ghi danh ở Centre khác (AS-RT-09). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Vai trò không được xem tab Enrolment. | Không hiển thị tab Enrolment trên hồ sơ trẻ. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-01 - Tab Enrolment | Chưa có wireframe cho bản nháp này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Cases | Phần | Có | Case đang mở hoặc "No open case." | — | FR-006; chọn mở case (FR-007). |
| Dòng tóm tắt | Text | Có | Ví dụ "2 enrolments · 1 running now" | — | FR-002. |
| Thẻ ghi danh | Card | Khi có | Lần đang học ở đầu | — | FR-003; chọn mở chi tiết ghi danh (FR-007). |
| Dòng thời gian | Danh sách | Khi có | Mới nhất trước | — | FR-004. |
| Lịch sử lớp học | Bảng | Khi có | Mới nhất trước | — | FR-005; chọn lớp mở chi tiết lớp (FR-007). |
| Thông báo trống | Text | Khi không có | "No enrolment for this child." | — | FR-008. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Tab đọc từ Joining & Leaving: lần ghi danh (Centre, level, lớp, trạng thái, programme, ngày ghi danh, ngày bắt đầu học, ngày kết thúc, pháp nhân, loại chương trình, năm học), các lần đổi trạng thái (loại, ngày hiệu lực, người thực hiện, người duyệt), case đang mở (loại, ngày tạo, bước đang chờ); từ Classes: các lần vào lớp (lớp, level, từ ngày, đến ngày, lý do, người thực hiện); từ change record của hồ sơ trẻ: đổi programme (giá trị cũ, giá trị mới, người sửa, người duyệt, ngày hiệu lực); từ Organisation: brand của Centre. Tab không ghi dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan ghi danh ở Small Wonder Tampines ngày 2025-11-24, bắt đầu học 2026-01-05, lớp N2 · Sunbeams, Full day, đang học | School Admin mở tab Enrolment | dòng tóm tắt "1 enrolment · 1 running now"; thẻ ghi danh hiện Small Wonder Tampines, N2 · Sunbeams, Enrolled, Full day, 2025-11-24, 2026-01-05, ngày kết thúc "—" | FR-001; FR-002; FR-003; DATA-001 |
| AC-002 | Ethan đổi từ Half day sang Full day hiệu lực 2026-11-01, School Admin Nadia Salleh sửa | School Admin mở tab Enrolment | dòng thời gian có "Half day → Full day · 2026-11-01 · Nadia Salleh" | FR-004; BR-004 |
| AC-003 | Ethan có đơn thôi học tạo 2026-09-30, đang chờ Centre Director | School Admin mở tab Enrolment | phần Cases hiện "Withdrawal raised 2026-09-30 · waiting on the Centre Director"; chọn thì mở màn case của Joining & Leaving | FR-006; FR-007 |
| AC-004 | Ethan không có case đang mở | School Admin mở tab Enrolment | phần Cases hiện "No open case."; không có liên kết bắt đầu case | FR-006; FR-001 |
| AC-005 | Ethan vào N2 · Sunbeams từ 2026-01-05 và lên K1 · Honeycombs từ 2027-01-04 qua lên lớp đầu năm học | người dùng mở tab Enrolment | lịch sử lớp học có 2 dòng: "K1 · Honeycombs · 2027-01-04 – — · lên lớp đầu năm học" ở đầu, rồi "N2 · Sunbeams · 2026-01-05 – 2027-01-03 · xếp lớp" | FR-005; BR-003 |
| AC-006 | lớp N2 · Sunbeams đã đóng cuối năm 2026 | người dùng mở tab Enrolment của Ethan | lịch sử lớp học vẫn hiện "N2 · Sunbeams" | FR-005; BR-002 |
| AC-007 | Mia Wong thôi học tháng 6/2026 | School Admin mở tab Enrolment của Mia | tab hiện lần ghi danh với trạng thái Withdrawn, dòng thời gian có lần thôi học, dòng tóm tắt "1 enrolment · 0 running now" | FR-002; FR-004; BR-002 |
| AC-008 | Lucas chuyển từ Small Wonder Tampines sang Bukit Timah ngày 2026-06-01 | nhân viên Centre Bukit Timah mở tab Enrolment | có 2 thẻ ghi danh, lần ở Bukit Timah ở đầu; dòng thời gian của lần cũ có "chuyển Centre · 2026-06-01" | FR-003; FR-004; BR-005 |
| AC-009 | Ethan có trạng thái Enrolled | Centre Director mở tab Enrolment | không có thao tác đổi trạng thái trên tab | BR-001 |
| AC-010 | người dùng đang xem tab Enrolment | người dùng chọn thẻ ghi danh Small Wonder Tampines | màn chi tiết ghi danh của Joining & Leaving mở | FR-007 |
| AC-011 | hồ sơ trẻ được tạo tay, chưa có lần ghi danh | School Admin mở tab Enrolment | phần ghi danh hiện "No enrolment for this child." | FR-008 |
| AC-012 | trẻ chưa sinh có ngày bắt đầu học dự kiến 2027-03-01 | School Admin mở tab Enrolment | thẻ ghi danh hiện "Starts 2027-03-01" | FR-009 |
| AC-013 | Enrichment Trainer được xem hồ sơ trẻ | Enrichment Trainer mở hồ sơ trẻ | không có tab Enrolment | VAL-001 |

#### Dependencies (Phụ thuộc)

Joining & Leaving (lần ghi danh, trạng thái, case); Children & Families › Classes (xếp lớp, đổi lớp, lên lớp); change record của hồ sơ trẻ (đổi programme); Organisation (brand); Roles & permissions (vai trò được xem tab).

## 4. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-RT-04 | Đánh dấu SUG child, Staff child, KA child hiển thị ở đâu (đề xuất: tab Finance), ai được xem, sửa ở đâu; ý nghĩa của SUG và KA? | Business Owner | Cao |  |
| OQ-RT-12 | Khi trẻ chuyển Centre, lần ghi danh cũ mang trạng thái nào? SRS chỉ có Enrolled, Temporary withdrawal, Withdrawn, Graduated. | Business Owner | Cao |  |
| OQ-RT-13 | Xác nhận các trường của một lần ghi danh: ticket BBA-67 chỉ nêu Centre, lớp, programme, các ngày, thay đổi trạng thái. Có cần brand, pháp nhân, loại chương trình, năm học không? | Business Owner | Trung bình |  |
| OQ-RT-14 | Hồ sơ trẻ tạo tay (không qua Enrolment) có tạo lần ghi danh không? | Business Owner | Trung bình |  |
| OQ-RT-15 | Nhân viên Centre mới có xem được lần ghi danh của trẻ ở Centre cũ không? | Business Owner | Trung bình |  |
| OQ-RT-16 | Tab Enrolment có thay cho tab "Class history" mà SRS liệt kê không? | Business Owner | Trung bình |  |
| OQ-RT-17 | Tab Enrolment có cần liên kết bắt đầu thôi học, tạm nghỉ, chuyển Centre không, hay chỉ bắt đầu ở Joining & Leaving? | Business Owner | Trung bình |  |
| OQ-RT-18 | Lịch sử ghi danh và lớp học trên Taidii có được chuyển sang hệ thống mới không? | Business Owner | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 4)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-RT-08 | Lần ghi danh đang học là lần có trạng thái Enrolled hoặc Temporary withdrawal. | FR-002 |
| AS-RT-09 | Người được mở hồ sơ trẻ thấy toàn bộ lịch sử ghi danh, kể cả ở Centre khác. | BR-005 — chờ OQ-RT-15 |
| AS-RT-10 | Tab không có liên kết bắt đầu case; việc bắt đầu case làm ở Joining & Leaving. | FR-006 — chờ OQ-RT-17 |
| AS-RT-11 | Tab Enrolment gồm nội dung "Class history" của SRS. | FR-005 — chờ OQ-RT-16 |
| AS-RT-12 | Trẻ chưa sinh có lần ghi danh với ngày bắt đầu học dự kiến. | FR-009 |

## 5. Tài liệu tham khảo

Số trang tính theo bản Word gốc của SRS khi xuất PDF khổ A4.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | Plane — dự án BBA Phase 1, ticket BBA-67 (WBS 3.1.1.02) | Description: enrolment history (centre, class, programme, dates, status changes) | — | Phạm vi US-001. |
| 2 | BBA-SMS-SRS-Children-and-Families-v0.1 | §1 Purpose & scope; §1.2 Not in Phase 1 | 3 | Hồ sơ trẻ thay Taidii; không đổi trạng thái bằng tay. |
| 3 | BBA-SMS-SRS-Children-and-Families-v0.1 | §2 Who uses it | 3–4 | Vai trò. |
| 4 | BBA-SMS-SRS-Children-and-Families-v0.1 | §3 P1 Child profile from enrolment | 4 | Hồ sơ trẻ sinh ra từ ghi danh; xếp lớp có ngày hiệu lực. |
| 5 | BBA-SMS-SRS-Children-and-Families-v0.1 | §3 P5 Class set-up and assignment; P6 Annual promotion | 5 | Lịch sử lớp học (FR-005). |
| 6 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.1 Children (View child profile, Assign class, Change class, View status, Apply access scope) | 6 | FR-001, FR-005, BR-001, BR-005. |
| 7 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Child records (BR-CHF-001, 002, 005, 006, 007) | 8 | FR-008, FR-009, BR-001, BR-002, BR-004. |
| 8 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Child records (BR-CHF-008) | 9 | BR-002. |
| 9 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Classes (BR-CHF-046, 047, 048, 049) | 10 | FR-005, BR-002, BR-003. |
| 10 | BBA-SMS-SRS-Children-and-Families-v0.1 | §8 Acceptance criteria (AC-CHF-001, 004, 005, 006, 007) | 11–12 | FR-004, BR-001, AC-007. |
