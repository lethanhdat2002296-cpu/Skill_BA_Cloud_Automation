# BBA-76 Centre/brand overview today (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | Centre/brand overview today |
| Mã ticket | BBA-76 |
| Mã WBS | 3.2.1.06 |
| Mã tài liệu | FRD-BBA-76 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-76: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả bảng tổng hợp điểm danh hôm nay theo Centre và brand cho HQ / District Manager, cách tính số trẻ dự kiến và xem chi tiết đến từng lớp. 2 câu hỏi mở ở mục 7 cần HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

HQ và District Manager cần nhìn một bảng là biết hôm nay mỗi Centre đã nhận bao nhiêu trẻ so với số trẻ dự kiến, bao nhiêu trẻ đã về và còn bao nhiêu trẻ trong trường, theo từng brand, có tổng toàn bộ, và mở xuống được từng lớp.

Mục tiêu đo được: người dùng HQ thấy số liệu của mọi Centre trong phạm vi của mình trên một màn hình, kèm giờ cập nhật.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Bảng theo Centre: brand, số trẻ đã đến / dự kiến, đã về, còn ở trường. Lọc brand, Centre. Dòng tổng. Mở xuống lớp của Centre, rồi đến bảng điểm danh của lớp. Giờ cập nhật và làm mới. | Số liệu nhân viên. Báo cáo điểm danh theo khoảng ngày (báo cáo điểm danh). Biểu đồ. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| HQ Admin | Mọi Centre. | Xem bảng tổng hợp. |
| District Manager, Operations Manager | Các Centre mình phụ trách. | Xem bảng tổng hợp của các Centre đó. |
| Centre Director | Centre của mình. | Xem dòng của Centre mình và các lớp. |
| Hệ thống | Toàn hệ thống. | Tính số liệu theo điểm danh hôm nay. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Daily operations › Attendance | Bảng tổng hợp hôm nay theo Centre / brand. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Bảng tổng hợp điểm danh hôm nay theo Centre và brand

#### User Story

Là District Manager, tôi muốn xem trong một bảng số trẻ đã đến, đã về và còn ở trường của từng Centre tôi phụ trách, để biết ngay Centre nào có số trẻ đến thấp bất thường và mở xem lớp nào.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Bảng có một dòng cho mỗi Centre trong phạm vi người dùng: Centre, brand, "Signed in of expected" (ví dụ "5 of 7"), "Signed out", "Still in". |
| FR-002 | Số trẻ dự kiến của một Centre = trẻ đang học có lịch học hôm nay, trừ trẻ có nghỉ phép đã duyệt hôm nay và trẻ đang tạm nghỉ. |
| FR-003 | "Still in" = số trẻ đã đến trừ số trẻ đã về; lượt điểm danh đã bị huỷ không được tính. |
| FR-004 | Lọc theo brand và Centre; mặc định "All brands", "All centres" trong phạm vi người dùng; sắp xếp mặc định theo tên Centre. |
| FR-005 | Cuối bảng có dòng tổng: số Centre đang xem, tổng trẻ đã đến / dự kiến, tổng đã về, tổng còn ở trường (ví dụ "15 of 15 centres · 15 children signed in of 20 expected"). |
| FR-006 | Chọn một Centre mở bảng các lớp của Centre với cùng các cột; chọn một lớp mở bảng điểm danh của lớp đó. |
| FR-007 | Bảng ghi "Updated at" kèm giờ lấy số liệu và có nút "Refresh". |
| FR-008 | Centre không có trẻ dự kiến hôm nay (ví dụ ngày Centre đóng cửa) vẫn hiện với "0 of 0". |

#### Functional Flow - Main (Luồng chính)

1. District Manager mở Attendance; hệ thống hiện bảng các Centre mình phụ trách (FR-001, FR-004).
2. District Manager xem dòng tổng (FR-005), chọn một Centre có số trẻ đến thấp (FR-006).
3. District Manager chọn một lớp để xem bảng điểm danh (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lọc theo một brand (FR-004).
2. Làm mới số liệu (FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có Centre nào: bảng trống (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Người dùng chỉ thấy Centre trong phạm vi của mình. |
| BR-002 | Số liệu tính theo điểm danh hôm nay; lượt đã huỷ không được tính. |
| BR-003 | Bảng chỉ để xem; không nhận hay trả trẻ từ bảng này. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có Centre nào. | Hiện "No centres match these filters." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Attendance — tổng hợp hôm nay | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Brand, Centre | Bộ lọc | Không | All | VAL-001. | FR-004. |
| Bảng Centre | Bảng | Có | Theo tên Centre | — | FR-001; FR-006. |
| Dòng tổng | Chữ | Có | — | — | FR-005. |
| Updated at, Refresh | Chữ, nút | Có | Giờ mở màn | — | FR-007. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Bảng đọc điểm danh hôm nay, lịch học, nghỉ phép đã duyệt và trạng thái tạm nghỉ của trẻ; không lưu dữ liệu mới. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Small Wonder Tampines có 7 trẻ dự kiến, 5 trẻ đã đến, chưa ai về | HQ Admin mở bảng | dòng Tampines hiện "5 of 7", Signed out 0, Still in 5 | FR-001; FR-003 |
| AC-002 | Centre có 8 trẻ có lịch hôm nay, 1 trẻ nghỉ phép đã duyệt | hệ thống tính | số dự kiến là 7 | FR-002 |
| AC-003 | District Manager phụ trách 4 Centre | mở bảng | chỉ thấy 4 Centre đó | FR-004; BR-001 |
| AC-004 | 15 Centre, tổng 15 trẻ đã đến, 20 dự kiến | xem cuối bảng | dòng "15 of 15 centres · 15 children signed in of 20 expected" | FR-005 |
| AC-005 | đang xem bảng | chọn Tampines rồi chọn lớp Sunbeams | mở bảng các lớp của Tampines, rồi bảng điểm danh lớp Sunbeams | FR-006 |
| AC-006 | một lượt điểm danh bị huỷ | hệ thống tính | lượt đó không được tính vào đã đến | FR-003; BR-002 |
| AC-007 | bảng mở lúc 09:00, có thêm trẻ đến lúc 09:05 | chọn Refresh | số liệu mới, "Updated at 09:05" | FR-007 |
| AC-008 | Agape Punggol đóng cửa hôm nay | mở bảng | Agape Punggol hiện "0 of 0" | FR-008 |
| AC-009 | lọc brand Odyssey trong phạm vi District Manager không có Odyssey | xem bảng | hiện "No centres match these filters." | VAL-001 |
| AC-010 | Centre Director mở bảng | xem | chỉ có dòng Centre của mình; không có nút nhận / trả trẻ | BR-003; BR-001; DATA-001 |

#### Dependencies (Phụ thuộc)

Class attendance; nghỉ phép đã duyệt; trạng thái tạm nghỉ (Joining & leaving); phạm vi Centre của người dùng (Users & permissions).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | "Expected" có trừ trẻ bị đánh vắng bằng tay trong ngày không? | HQ Ops | Trung bình |  |
| OQ-02 | Số liệu cần tự làm mới sau bao nhiêu phút, hay chỉ khi bấm Refresh? | HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Trẻ dự kiến = trẻ đang học có lịch học hôm nay, trừ nghỉ phép đã duyệt và tạm nghỉ; không trừ trẻ bị đánh vắng bằng tay. | FR-002 — chờ OQ-01 |
| AS-02 | Số liệu làm mới khi mở màn và khi bấm Refresh. | FR-007 — chờ OQ-02 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Signed in of expected | Số trẻ đã đến trên số trẻ dự kiến đến hôm nay. |
| Still in | Số trẻ đã đến mà chưa về. |
