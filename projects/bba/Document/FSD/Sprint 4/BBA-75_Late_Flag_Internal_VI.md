# BBA-75 Late flag (internal only) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | Late flag (internal only) |
| Mã ticket | BBA-75 |
| Mã WBS | 3.2.1.03 |
| Mã tài liệu | FRD-BBA-75 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-75: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc đánh dấu "Late" khi trẻ đến sau giờ chốt, chỉ nhân viên thấy, dùng cho báo cáo của Centre. 3 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

Centre cần biết trẻ nào thường đến muộn để trao đổi với gia đình và sắp xếp hoạt động buổi sáng. Hệ thống tự đánh dấu "Late" khi trẻ được nhận sau giờ chốt của Centre. Dấu này chỉ dùng nội bộ, không bao giờ hiện cho phụ huynh.

Mục tiêu đo được: 100% lượt nhận sau giờ chốt có dấu Late; 0 màn hình, thông báo hay file gửi phụ huynh có dấu Late.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Giờ chốt theo Centre. Tự đánh dấu Late khi nhận trẻ sau giờ chốt. Hiện Late trên bảng điểm danh và báo cáo của Centre. Tính lại khi giờ nhận được sửa. Ẩn hoàn toàn với phụ huynh. | Đón trẻ muộn và phí đón muộn. Thông báo cho phụ huynh về việc đến muộn. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Teacher, Centre Admin / School Admin, Centre Director | Lớp / Centre của mình. | Xem dấu Late và báo cáo đến muộn. |
| HQ Admin | Mọi Centre. | Đặt giờ chốt của từng Centre. |
| HQ Ops (District Manager, Operations Manager) | Các Centre mình phụ trách. | Xem báo cáo đến muộn. |
| Phụ huynh | — | Không thấy dấu Late ở bất kỳ đâu. |
| Hệ thống | Toàn hệ thống. | So giờ nhận với giờ chốt, đánh dấu và tính lại. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Daily operations › Class attendance, báo cáo điểm danh | Dấu Late nội bộ. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Đánh dấu trẻ đến muộn, chỉ dùng nội bộ

#### User Story

Là Centre Director, tôi muốn hệ thống tự đánh dấu trẻ đến sau giờ chốt và cho tôi xem số lần đến muộn của từng trẻ, để trao đổi với gia đình khi cần mà phụ huynh không thấy dấu này trên ứng dụng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Mỗi Centre có một giờ chốt đến muộn (mặc định 9:15); HQ Admin đổi được, mỗi lần đổi được lưu lịch sử. |
| FR-002 | Khi trẻ được nhận sau giờ chốt, hệ thống tự gắn dấu "Late" cho lượt nhận đó; nhận đúng giờ chốt không bị tính muộn. |
| FR-003 | Bảng điểm danh của lớp hiện chữ "Late (staff only)" cạnh giờ nhận của trẻ đến muộn. |
| FR-004 | Báo cáo điểm danh của Centre có cột số lần đến muộn của mỗi trẻ trong khoảng ngày đã chọn, và bộ lọc "Late only". |
| FR-005 | Khi giờ nhận được sửa (BBA-77), hệ thống tính lại dấu Late theo giờ mới. |
| FR-006 | Dấu Late không xuất hiện trong Parents App, thông báo gửi phụ huynh, hoá đơn, hay bất kỳ tài liệu nào gửi phụ huynh. |
| FR-007 | Khi giờ chốt thay đổi, chỉ các lượt nhận từ ngày thay đổi trở đi dùng giờ chốt mới; dấu Late của những ngày trước giữ nguyên. |

#### Functional Flow - Main (Luồng chính)

1. Trẻ được nhận lúc 09:34, giờ chốt 9:15 (FR-002).
2. Bảng điểm danh hiện "Late (staff only)" (FR-003).
3. Cuối tháng, Centre Director xem báo cáo số lần đến muộn (FR-004).

#### Functional Flow - Alternative (Luồng thay thế)

1. Giờ nhận được sửa sớm hơn giờ chốt: dấu Late bị bỏ (FR-005).
2. HQ Admin đổi giờ chốt của Centre (FR-001, FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Giờ chốt nhập sai định dạng: không lưu (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Dấu Late do hệ thống tự gắn theo giờ nhận và giờ chốt; nhân viên không gắn hay bỏ bằng tay. |
| BR-002 | Dấu Late chỉ nhân viên thấy, không bao giờ hiện cho phụ huynh. |
| BR-003 | Giờ chốt là thiết lập theo Centre. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Giờ chốt không phải giờ hợp lệ (giờ:phút). | Không lưu; hiện "Enter a time such as 09:15." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Class attendance — dấu Late | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Giờ chốt đến muộn | Giờ | Có | 09:15 | VAL-001. | Thiết lập theo Centre. |
| Late (staff only) | Chữ cạnh giờ nhận | Khi đến muộn | — | — | FR-003. |
| Số lần đến muộn | Cột báo cáo | — | — | — | FR-004. |
| Late only | Bộ lọc báo cáo | Không | Tắt | — | FR-004. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lượt nhận lưu dấu Late và giờ chốt dùng để tính. |
| DATA-002 | Mỗi lần đổi giờ chốt lưu giá trị cũ, giá trị mới, ngày áp dụng, người đổi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | giờ chốt của Centre là 9:15 | Noah được nhận lúc 09:34 | bảng điểm danh hiện "09:34 · Late (staff only)" | FR-002; FR-003; BR-001 |
| AC-002 | giờ chốt 9:15 | trẻ được nhận đúng 09:15 | không có dấu Late | FR-002 |
| AC-003 | Noah có dấu Late hôm nay | phụ huynh của Noah mở Parents App và đọc thông báo nhận trẻ | không có chữ Late ở bất kỳ đâu | FR-006; BR-002 |
| AC-004 | Noah đến muộn 4 lần trong tháng 9 | Centre Director xem báo cáo tháng 9, lọc Late only | Noah hiện số lần đến muộn là 4 | FR-004 |
| AC-005 | giờ nhận 09:34 bị nhập nhầm | nhân viên sửa thành 08:34 | dấu Late bị bỏ | FR-005 |
| AC-006 | HQ Admin đổi giờ chốt từ 9:15 sang 9:00 từ ngày 01/12 | xem lượt nhận 09:10 ngày 30/11 và ngày 01/12 | ngày 30/11 không Late; ngày 01/12 Late | FR-001; FR-007; BR-003; DATA-002 |
| AC-007 | HQ Admin nhập giờ chốt "9h" | chọn lưu | không lưu, hiện "Enter a time such as 09:15." | VAL-001 |

#### Dependencies (Phụ thuộc)

Class attendance; báo cáo điểm danh; sửa điểm danh có lý do (BBA-77); thiết lập theo Centre.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Trẻ học buổi chiều (Half Day PM) dùng giờ chốt riêng hay không tính đến muộn? | Centre Director / HQ Ops | Cao |  |
| OQ-02 | Trẻ đi xe đưa đón đến muộn vì xe có bị tính Late không? | Centre Director / HQ Ops | Trung bình |  |
| OQ-03 | Centre Director có được tự đổi giờ chốt của Centre mình không, hay chỉ HQ Admin? | HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Chỉ HQ Admin đổi giờ chốt. | FR-001 — chờ OQ-03 |
| AS-02 | Một giờ chốt chung cho mọi trẻ của Centre. | FR-001 — chờ OQ-01 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Giờ chốt đến muộn | Giờ mà trẻ được nhận sau giờ đó bị tính là đến muộn. |
| Late (staff only) | Dấu đến muộn chỉ nhân viên thấy. |
