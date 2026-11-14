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
| Phiên bản | 0.2 (nháp) |
| Trạng thái | BẢN NHÁP ĐỂ RÀ SOÁT |
| Ngày | 11/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 (nháp) | 11/11/2026 | Business Analysis | Bản nháp riêng cho US-001 sau khi rà soát theo SRS Children & Families v0.1 và ticket BBA-67. | HaiNguyen |
| 0.2 (nháp) | 11/11/2026 | Business Analysis | Viết lại theo đúng nghĩa của Enrolment trong SRS: ghi danh là bước xác nhận sau đăng ký, mọi thay đổi sau đó thuộc Joining & leaving. Tab chỉ mô tả thông tin ghi danh và các thay đổi sau ghi danh; bỏ phần đi sâu về lịch sử lớp học, case và đổi programme. | HaiNguyen |

**Mức sẵn sàng:** Đã mô tả thông tin ghi danh của trẻ, các thay đổi sau ghi danh do Joining & leaving ghi nhận, trẻ chưa tới ngày bắt đầu học và trẻ chưa sinh. 6 câu hỏi mở ở mục 5 cần BBA chốt.

## 2. Enrolment hiểu theo SRS

| Điểm chính | Căn cứ trong SRS Children & Families v0.1 |
|---|---|
| Ghi danh được xác nhận thì trẻ có trạng thái Enrolled, tức đã là học sinh, kể cả khi chưa tới ngày bắt đầu học. | AC-CHF-001 (tr.11); §3 P1 bước 1–2 (tr.4) |
| Đăng ký (Registration) diễn ra trước: hồ sơ trẻ được tạo từ dữ liệu đăng ký, phiếu đăng ký đã ký là một giấy tờ trong hồ sơ trẻ. Ghi danh (Enrolment) là bước xác nhận sau cùng. | §3 P1 bước 2 (tr.4); §4 mục 1.4 View document (tr.7); BR-CHF-030 (tr.9); §6.2 (tr.11) |
| Có thể ghi danh cho trẻ chưa sinh bằng ngày dự sinh; phụ huynh giữ chỗ từ lúc mang thai, phổ biến ở infant care tại Singapore. | §4 mục 1.1 Create profile for an unborn child (tr.5); BR-CHF-002, BR-CHF-003 (tr.8) |
| Các thay đổi sau ghi danh (tạm nghỉ, thôi học, tốt nghiệp) đều thuộc Joining & leaving, không quay lại Enrolment. | §1.2 (tr.3); §4 mục 1.1 View status (tr.6); BR-CHF-006 (tr.8); AC-CHF-005 (tr.11) |

Vì vậy tab Enrolment chỉ **mô tả**: trẻ được ghi danh vào đâu, từ khi nào, và sau đó đã có những thay đổi gì. Tab không có thao tác.

## 3. Những gì thay đổi so với US-001 hiện tại

| Nội dung | US-001 hiện tại (v0.2 của FRD) | Bản nháp này |
|---|---|---|
| Ý nghĩa tab | Danh sách nhiều lần ghi danh, dòng thời gian, case, đánh dấu học phí. | Thông tin ghi danh của trẻ và các thay đổi sau ghi danh. |
| Trẻ chưa tới ngày bắt đầu học | Chưa nêu. | Vẫn là Enrolled; tab ghi rõ ngày bắt đầu học. |
| Trẻ chưa sinh | Chưa nêu. | Ghi danh theo ngày dự sinh. |
| Case đang mở, liên kết bắt đầu case | Có (khối Cases). | Không đưa vào; chờ OQ-RT-17. |
| Đánh dấu SUG / Staff / KA child | Có (khối Flags). | Không đưa vào; chờ OQ-RT-04. |
| Brand, pháp nhân, loại chương trình, năm học | Có. | Không đưa vào; chờ OQ-RT-13. |
| Trạng thái "Transferred" | Có ở AC-003. | Không dùng; chờ OQ-RT-12. |

## 4. Yêu cầu chức năng

### 4.1 US-001 - Tab Enrolment: thông tin ghi danh của trẻ

#### User Story

Là School Admin, tôi muốn xem trên hồ sơ trẻ trẻ được ghi danh vào Centre, lớp, chương trình nào, từ ngày nào và sau đó đã có thay đổi gì, để trả lời phụ huynh mà không phải mở Joining & leaving.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab Enrolment chỉ hiển thị, không có thao tác sửa hay tạo; gồm 2 phần: Thông tin ghi danh, Thay đổi sau ghi danh. |
| FR-002 | Phần "Thông tin ghi danh" hiển thị: Centre, level, lớp, programme (Full day / Half day), ngày ghi danh (ngày xác nhận), ngày bắt đầu học, trạng thái hiện tại (Enrolled, Temporary withdrawal, Withdrawn, Graduated). |
| FR-003 | Trẻ chưa tới ngày bắt đầu học: trạng thái vẫn là Enrolled, ngày bắt đầu học hiển thị như bình thường. Trẻ chưa sinh: hiển thị thêm ngày dự sinh. |
| FR-004 | Phần "Thay đổi sau ghi danh" liệt kê các thay đổi do Joining & leaving ghi nhận (tạm nghỉ, thôi học, tốt nghiệp), mới nhất trước; mỗi dòng ghi loại thay đổi và ngày hiệu lực. Chưa có thay đổi nào thì hiển thị một dòng thông báo chưa có thay đổi. |
| FR-005 | Chọn thông tin ghi danh mở màn ghi danh của module Enrolment; chọn một thay đổi mở màn tương ứng của Joining & leaving. |

#### Functional Flow - Main (Luồng chính)

1. School Admin mở hồ sơ trẻ và chọn tab Enrolment (FR-001).
2. Hệ thống hiển thị thông tin ghi danh và các thay đổi sau ghi danh (FR-002, FR-004).
3. School Admin chọn thông tin ghi danh hoặc một thay đổi để mở màn của module sở hữu (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ đã ghi danh nhưng chưa tới ngày bắt đầu học: trạng thái Enrolled kèm ngày bắt đầu học (FR-003; BR-001).
2. Trẻ chưa sinh: thông tin ghi danh có ngày dự sinh (FR-003).
3. Trẻ đã thôi học hoặc tốt nghiệp: tab vẫn hiển thị đủ thông tin ghi danh và các thay đổi (FR-004; BR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có. Tab chỉ hiển thị; quyền mở hồ sơ trẻ theo FRD Child Record Overview.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Trẻ có trạng thái Enrolled ngay khi ghi danh được xác nhận, kể cả trước ngày bắt đầu học (AC-CHF-001). |
| BR-002 | Mọi thay đổi sau ghi danh (tạm nghỉ, thôi học, tốt nghiệp) thuộc Joining & leaving; tab Enrolment chỉ hiển thị (BR-CHF-006; AC-CHF-005). |
| BR-003 | Thông tin ghi danh và các thay đổi không bị xoá; trẻ đã thôi học, tốt nghiệp vẫn xem được (BR-CHF-007; BR-CHF-008). |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-01 - Tab Enrolment | Chưa có wireframe cho bản nháp này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Thông tin ghi danh | Phần | Có | — | — | FR-002; FR-003; chọn mở màn ghi danh (FR-005). |
| Thay đổi sau ghi danh | Danh sách | Có | Mới nhất trước; dòng thông báo khi chưa có thay đổi | — | FR-004; chọn mở màn Joining & leaving (FR-005). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Tab đọc từ Enrolment: Centre, level, lớp, programme, ngày ghi danh, ngày bắt đầu học; từ hồ sơ trẻ: ngày dự sinh; từ Joining & leaving: trạng thái hiện tại, các thay đổi (loại, ngày hiệu lực). Tab không ghi dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan được ghi danh ở Small Wonder Tampines ngày 2025-11-24, bắt đầu học 2026-01-05, N2 · Sunbeams, Full day | School Admin mở tab Enrolment | phần Thông tin ghi danh hiện đủ Centre, level, lớp, programme, 2 ngày và trạng thái Enrolled; không có nút sửa | FR-001; FR-002; DATA-001 |
| AC-002 | ghi danh của Chloe được xác nhận ngày 2026-11-11, ngày bắt đầu học 2027-01-04 | School Admin mở tab Enrolment ngày 2026-11-12 | trạng thái Enrolled, ngày bắt đầu học 2027-01-04 | FR-003; BR-001 |
| AC-003 | trẻ chưa sinh, ngày dự sinh 2027-01-15, đã ghi danh infant care | School Admin mở tab Enrolment | thông tin ghi danh có ngày dự sinh 2027-01-15 | FR-003 |
| AC-004 | Mia Wong thôi học tháng 6/2026 | School Admin mở tab Enrolment của Mia | trạng thái Withdrawn; phần Thay đổi sau ghi danh có dòng thôi học kèm ngày hiệu lực | FR-004; BR-003 |
| AC-005 | Ethan chưa có thay đổi nào sau ghi danh | School Admin mở tab Enrolment | phần Thay đổi sau ghi danh hiện dòng thông báo chưa có thay đổi | FR-004 |
| AC-006 | Ethan có trạng thái Enrolled | Centre Director mở tab Enrolment | không có thao tác đổi trạng thái trên tab | BR-002 |
| AC-007 | Mia có dòng thôi học | người dùng chọn dòng đó | màn tương ứng của Joining & leaving mở | FR-005 |

#### Dependencies (Phụ thuộc)

Enrolment (thông tin ghi danh); Joining & leaving (trạng thái và các thay đổi sau ghi danh); hồ sơ trẻ (ngày dự sinh).

## 5. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-RT-04 | Đánh dấu SUG child, Staff child, KA child có cần hiển thị trên hồ sơ trẻ không, nếu có thì ở tab nào (đề xuất: tab Finance)? | Business Owner | Cao |  |
| OQ-RT-12 | Chuyển Centre có nằm trong các thay đổi sau ghi danh không, và trạng thái của trẻ khi chuyển là gì? SRS chỉ có Enrolled, Temporary withdrawal, Withdrawn, Graduated. | Business Owner | Cao |  |
| OQ-RT-13 | Thông tin ghi danh có cần thêm brand, pháp nhân, loại chương trình, năm học không? Ticket BBA-67 chỉ nêu Centre, lớp, programme, các ngày, thay đổi trạng thái. | Business Owner | Trung bình |  |
| OQ-RT-16 | Lịch sử lớp học (tab "Class history" trong SRS) hiển thị ở đâu trên hồ sơ trẻ? | Business Owner | Trung bình |  |
| OQ-RT-17 | Tab Enrolment có cần hiển thị case đang mở (thôi học, tạm nghỉ đang chờ duyệt) và liên kết bắt đầu case không? | Business Owner | Trung bình |  |
| OQ-RT-19 | Một trẻ có thể có nhiều lần ghi danh không (ví dụ thôi học rồi ghi danh lại)? Nếu có, tab hiển thị tất cả hay chỉ lần gần nhất? | Business Owner | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 5)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-RT-13 | Tab hiển thị một lần ghi danh (lần gần nhất) của trẻ. | FR-002 — chờ OQ-RT-19 |

## 6. Tài liệu tham khảo

Số trang tính theo bản Word gốc của SRS khi xuất PDF khổ A4.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | Plane — dự án BBA Phase 1, ticket BBA-67 (WBS 3.1.1.02) | Description: enrolment history (centre, class, programme, dates, status changes), each linking to the module screen | — | Phạm vi US-001. |
| 2 | BBA-SMS-SRS-Children-and-Families-v0.1 | §1.2 Not in Phase 1 | 3 | Không đổi trạng thái bằng tay (BR-002). |
| 3 | BBA-SMS-SRS-Children-and-Families-v0.1 | §3 P1 Child profile from enrolment | 4 | Đăng ký trước, ghi danh xác nhận sau (mục 2). |
| 4 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.1 Children (Create profile for an unborn child) | 5 | Trẻ chưa sinh (FR-003). |
| 5 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.1 Children (View status) | 6 | Thay đổi sau ghi danh thuộc Joining & leaving (FR-004, BR-002). |
| 6 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.4 Documents (View document — signed registration form) | 7 | Phiếu đăng ký là giấy tờ trong hồ sơ trẻ (mục 2). |
| 7 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Child records (BR-CHF-002, 003, 006, 007) | 8 | FR-003, BR-002, BR-003. |
| 8 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Child records (BR-CHF-008); Documents (BR-CHF-030) | 9 | BR-003; phiếu đăng ký đã ký (mục 2). |
| 9 | BBA-SMS-SRS-Children-and-Families-v0.1 | §6.2 Documents | 11 | Phiếu đăng ký đã ký (mục 2). |
| 10 | BBA-SMS-SRS-Children-and-Families-v0.1 | §8 Acceptance criteria (AC-CHF-001, 005, 007) | 11–12 | BR-001, BR-002, AC-004. |
