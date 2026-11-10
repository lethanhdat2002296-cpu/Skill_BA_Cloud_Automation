# BBA-74 Temperature readings (≥3/day) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | Temperature readings (≥3/day) |
| Mã ticket | BBA-74 |
| Mã WBS | 3.2.1.02 |
| Mã tài liệu | FRD-BBA-74 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-74: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc đo nhiệt độ ít nhất 3 lần mỗi ngày theo thời điểm, cảnh báo khi trẻ sốt, nhắc lần đo còn thiếu và phụ huynh xem kết quả. 4 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

Mỗi ngày, mỗi trẻ được đo nhiệt độ ít nhất 3 lần: khi đến trường, trước giờ ngủ trưa và trước khi về; đo thêm khi giáo viên thấy trẻ có dấu hiệu bất thường. Trẻ có nhiệt độ từ ngưỡng sốt trở lên được báo ngay cho giáo viên chủ nhiệm và Centre Director. Phụ huynh xem được các lần đo trong ngày của con.

Mục tiêu đo được: mọi lần đo có giờ và thời điểm đo; mọi lần đo từ ngưỡng sốt trở lên được báo trong vòng 1 phút sau khi lưu.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Thêm lần đo: nhiệt độ, giờ, thời điểm (On arrival, Before nap, Before pickup, Extra). Đếm số lần đo trong ngày so với 3 lần bắt buộc. Đánh dấu và báo khi trẻ sốt. Nhiệt kế kết nối tự điền số. Sửa lần đo có lịch sử. Phụ huynh xem trong mục Attendance của Parents App. Xuất danh sách nhiệt độ. | Nhiệt độ của nhân viên (BBA-79). Theo dõi bệnh truyền nhiễm, quy định cho trẻ nghỉ ở nhà. Ghi nhận cho uống thuốc. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Teacher, Centre Admin / School Admin | Lớp / Centre của mình. | Đo và ghi nhiệt độ. |
| Centre Director | Centre của mình. | Nhận báo trẻ sốt; xem trẻ còn thiếu lần đo. |
| HQ Admin | Mọi Centre. | Đặt ngưỡng sốt theo quốc gia. |
| Phụ huynh (Parents App) | Con mình. | Xem các lần đo trong ngày. |
| Hệ thống | Toàn hệ thống. | Đánh dấu sốt, gửi thông báo, đếm lần đo. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Daily operations › Class attendance (cột Screening) | Ghi nhiệt độ, cảnh báo sốt, phụ huynh xem. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Đo nhiệt độ ít nhất 3 lần mỗi ngày

#### User Story

Là giáo viên, tôi muốn ghi nhanh nhiệt độ của trẻ theo từng thời điểm trong ngày và được hệ thống nhắc khi trẻ sốt hoặc còn thiếu lần đo, để phát hiện sớm trẻ không khoẻ và báo cho phụ huynh.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | "Add reading" cho mỗi trẻ: nhiệt độ (bộ chọn mặc định 36,5 °C, từ 36 đến 40 °C, bước 0,1; hoặc nhập tay), giờ (mặc định hiện tại), thời điểm: On arrival, Before nap, Before pickup, Extra. |
| FR-002 | Thời điểm Extra bắt buộc ghi lý do đo thêm (ví dụ "trẻ mệt, má đỏ"). |
| FR-003 | Nhiệt kế đã kết nối với máy tính bảng tự điền nhiệt độ; nhân viên vẫn chọn thời điểm. |
| FR-004 | Mỗi trẻ cần 3 lần đo trong ngày: On arrival, Before nap, Before pickup. Bảng điểm danh hiện số lần đã đo / 3 (ví dụ "2 / 3") và thời điểm còn thiếu. |
| FR-005 | Lần đo từ ngưỡng sốt trở lên (theo quốc gia, mặc định 37,5 °C) hiện màu đỏ trên bảng điểm danh; giáo viên chủ nhiệm và Centre Director nhận thông báo trong app có tên trẻ, nhiệt độ, giờ. |
| FR-006 | Trước giờ về, Centre Director thấy danh sách trẻ còn thiếu lần đo bắt buộc trong ngày. |
| FR-007 | Phụ huynh xem trong mục Attendance của Parents App: mỗi lần đo có giờ, thời điểm, nhiệt độ. |
| FR-008 | Sửa hoặc xoá một lần đo phải có lý do; lịch sử giữ giá trị cũ, người sửa, thời điểm. |
| FR-009 | Đo nhiệt độ vẫn dùng được khi ứng dụng điểm danh mất mạng; dữ liệu đồng bộ khi có mạng lại. |
| FR-010 | Xuất danh sách nhiệt độ theo khoảng ngày và lớp ra Excel. |

#### Functional Flow - Main (Luồng chính)

1. Khi nhận trẻ, nhân viên đo và ghi On arrival (FR-001).
2. Trước giờ ngủ và trước khi về, giáo viên ghi Before nap, Before pickup (FR-001, FR-004).
3. Phụ huynh xem các lần đo trong Parents App (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ có dấu hiệu bất thường: ghi Extra kèm lý do (FR-002).
2. Trẻ sốt: hệ thống báo giáo viên chủ nhiệm và Centre Director (FR-005).
3. Ghi nhầm: sửa có lý do (FR-008).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Nhập tay ngoài khoảng cho phép: không lưu (VAL-001).
2. Extra không có lý do: không lưu (VAL-002).
3. Giờ đo trước giờ nhận trẻ hoặc sau hiện tại: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mỗi trẻ có ít nhất 3 lần đo mỗi ngày đi học; không giới hạn số lần đo thêm. |
| BR-002 | Ngưỡng sốt là thiết lập theo quốc gia (mặc định 37,5 °C). |
| BR-003 | Lần đo đã lưu không bị xoá mất; sửa hoặc xoá đều có lý do và lịch sử. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Nhập tay nhiệt độ ngoài khoảng 34,0–42,0 °C (AS-02). | Không lưu; hiện "Check the temperature." |
| VAL-002 | Thời điểm Extra không có lý do. | Không lưu; hiện "Enter why this extra reading was taken." |
| VAL-003 | Giờ đo trước giờ nhận trẻ hoặc sau thời điểm hiện tại. | Không lưu; hiện "Check the time." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Class attendance — Add reading | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Nhiệt độ (°C) | Bộ chọn số / nhập tay | Có | 36,5 | VAL-001. | Nhiệt kế kết nối tự điền. |
| Thời điểm | Danh sách chọn | Có | Thời điểm còn thiếu sớm nhất | — | On arrival, Before nap, Before pickup, Extra. |
| Lý do (Extra) | Ô nhập | Khi Extra | Trống | VAL-002. | — |
| Giờ | Giờ | Có | Hiện tại | VAL-003. | — |
| Số lần đo | Chữ | — | "x / 3" | — | FR-004. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần đo lưu: trẻ, nhiệt độ, giờ, thời điểm, lý do (Extra), cách nhập (bộ chọn, nhập tay, nhiệt kế), nhân viên, thiết bị. |
| DATA-002 | Mỗi lần sửa / xoá lưu giá trị cũ, giá trị mới, lý do, người sửa, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan vừa được nhận lúc 08:12 | nhân viên ghi 36,6 °C, On arrival | lần đo lưu với giờ 08:12; bảng hiện "1 / 3" | FR-001; FR-004 |
| AC-002 | Ethan đã có On arrival | giáo viên ghi 38,1 °C, Before nap | ô hiện màu đỏ; giáo viên chủ nhiệm và Centre Director nhận thông báo "Ethan Lim 38,1 °C 12:40" | FR-005; BR-002 |
| AC-003 | trẻ có dấu hiệu mệt | giáo viên ghi Extra không có lý do | không lưu, hiện "Enter why this extra reading was taken." | FR-002; VAL-002 |
| AC-004 | nhiệt kế đã kết nối | giáo viên đo | nhiệt độ tự điền; giáo viên chọn thời điểm và lưu | FR-003 |
| AC-005 | 16:30, 3 trẻ chưa có Before pickup | Centre Director mở danh sách trẻ thiếu lần đo | thấy 3 trẻ và thời điểm còn thiếu | FR-006; BR-001 |
| AC-006 | Ethan có 3 lần đo trong ngày | phụ huynh mở Attendance | thấy 3 lần đo với giờ, thời điểm, nhiệt độ | FR-007 |
| AC-007 | giáo viên ghi nhầm 37,9 thay vì 36,9 | giáo viên sửa và nhập lý do | giá trị mới được lưu; lịch sử giữ 37,9, lý do, người sửa | FR-008; BR-003; DATA-002 |
| AC-008 | nhân viên nhập tay 3,7 | chọn lưu | không lưu, hiện "Check the temperature." | VAL-001 |
| AC-009 | ứng dụng điểm danh mất mạng | nhân viên ghi nhiệt độ | lần đo được giữ trên máy và lên hệ thống khi có mạng lại | FR-009 |
| AC-010 | Centre Director chọn lớp Sunbeams, tháng 9 | chọn xuất | file Excel có mọi lần đo của lớp trong tháng | FR-010 |
| AC-011 | trẻ được nhận lúc 08:12 | giáo viên ghi lần đo lúc 07:30 | không lưu, hiện "Check the time." | VAL-003 |

#### Dependencies (Phụ thuộc)

Class attendance; ứng dụng điểm danh ở cổng và nhiệt kế kết nối; thiết lập ngưỡng sốt theo quốc gia; thông báo trong app; Parents App (Attendance).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Phụ huynh có nhận thông báo ngay khi con sốt không, hay chỉ xem trong Attendance? | Centre Director / HQ Ops | Cao |  |
| OQ-02 | Trẻ học nửa ngày (không ngủ trưa) cần mấy lần đo bắt buộc? | Centre Director / HQ Ops | Trung bình |  |
| OQ-03 | Nhắc lần đo còn thiếu gửi cho ai và vào giờ nào? | Centre Director / HQ Ops | Trung bình |  |
| OQ-04 | Khoảng nhiệt độ hợp lệ khi nhập tay là bao nhiêu? | HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Danh sách trẻ thiếu lần đo chỉ hiện cho Centre Director, không gửi thông báo. | FR-006 — chờ OQ-03 |
| AS-02 | Khoảng hợp lệ khi nhập tay: 34,0–42,0 °C. | VAL-001 — chờ OQ-04 |
| AS-03 | Thời điểm Extra bắt buộc ghi lý do. | FR-002 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Thời điểm đo | On arrival (khi đến trường), Before nap (trước giờ ngủ trưa), Before pickup (trước khi về), Extra (đo thêm khi thấy bất thường). |
| Ngưỡng sốt | Nhiệt độ từ mức này trở lên được coi là sốt; thiết lập theo quốc gia. |
