# [Nháp] BBA-75 Late flag (internal only) — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + SRS Daily Operations (BR-OPS-014, 015), Attendance App (BR-ATT-009, 051), Administration (BR-ADM-040) + prototype SMS (Class attendance: "Late (staff only)", tab "Late arrival & pickup"). Không có câu trả lời Plane cho ticket này.
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-75/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. FRD đã khớp SRS — **giữ nguyên** các yêu cầu.
2. Thông báo cho phụ huynh không bao giờ nhắc cờ muộn (BR-ATT-051) — ghi rõ vào FR-006.
3. Prototype có tab "Late arrival & pickup" (đón muộn) nhưng SRS không có → OQ-04.

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Giờ chốt theo Centre có **buổi sáng và buổi chiều** (vd sau 9:15 sáng, sau 12:15 chiều); tính theo **giờ ghi nhận ở cổng**, không phải giờ đồng bộ (Q-77-03) → FR-001, FR-002; OQ-01 trả lời một phần.
- Late không gắn tay (Q-81-02) — khớp BR-001. Bản ghi offline / backdated tự tính lại: DOTB tự quyết (Q-77-04) — khớp FR-005.
- Chỉ nhân viên thấy — BBA nói "ở Singapore", Malaysia chưa rõ (Q-77-05) → OQ-06.

---

## US-001 - Đánh dấu trẻ đến muộn, chỉ dùng nội bộ

#### User Story

Là Centre Director, tôi muốn hệ thống tự đánh dấu trẻ đến sau giờ chốt và cho tôi xem số lần đến muộn của từng trẻ, để trao đổi với gia đình khi cần mà phụ huynh không thấy dấu này trên ứng dụng.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(sửa)* | Mỗi Centre có giờ chốt đến muộn buổi sáng (mặc định 9:15) và buổi chiều (ví dụ 12:15) (Q-77-03); HQ Admin đổi được ở Centre settings, mỗi lần đổi được lưu lịch sử. |
| FR-002 *(sửa)* | Khi trẻ được nhận sau giờ chốt của buổi tương ứng (OQ-05), hệ thống tự gắn dấu "Late" cho lượt nhận đó; so sánh bằng giờ ghi nhận ở cổng, không phải giờ đồng bộ (Q-77-03); nhận đúng giờ chốt không bị tính muộn. |
| FR-003 | Bảng điểm danh của lớp hiện chữ "Late (staff only)" cạnh giờ nhận của trẻ đến muộn. |
| FR-004 | Báo cáo điểm danh của Centre có cột số lần đến muộn của mỗi trẻ trong khoảng ngày đã chọn, và bộ lọc "Late only". |
| FR-005 | Khi giờ nhận được sửa (BBA-77), hệ thống tính lại dấu Late theo giờ mới. |
| FR-006 *(sửa)* | Dấu Late không xuất hiện trong Parents App, thông báo gửi phụ huynh (kể cả thông báo nhận trẻ), hoá đơn, hay bất kỳ tài liệu nào gửi phụ huynh. |
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

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Late arrival cut-off — morning *(sửa)* | Giờ, ở Centre settings | Có | 09:15 | VAL-001. | Thiết lập theo Centre (FR-001). |
| Late arrival cut-off — afternoon *(mới)* | Giờ, ở Centre settings | Có | 12:15 (ví dụ của BBA) | VAL-001. | Thiết lập theo Centre (FR-001). |
| Late (staff only) | Nhãn cạnh giờ nhận | Khi đến muộn | — | — | FR-003. |
| Late arrival | Tab trên Class attendance | — | Số trẻ đến muộn hôm nay | — | FR-004. |
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
| AC-008 *(mới)* | giờ chốt buổi chiều của Centre là 12:15 | trẻ học buổi chiều được nhận lúc 12:30 | bảng điểm danh hiện "12:30 · Late (staff only)" | FR-001; FR-002 |

#### Dependencies (Phụ thuộc)

Class attendance; báo cáo điểm danh; sửa / huỷ điểm danh (BBA-77); Centre settings.

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái |
|---|---|---|
| OQ-01 | Trẻ học buổi chiều dùng giờ chốt riêng? | **Đã trả lời:** có giờ chốt buổi chiều, vd 12:15 (Q-77-03) |
| OQ-05 *(mới)* | Chọn giờ chốt nào cho một lượt nhận: theo buổi học của trẻ (AM / PM / Full day) hay theo khung giờ lượt nhận? | Mở |
| OQ-06 *(mới)* | Malaysia: phụ huynh có thấy dấu Late không? BBA chỉ nói "ở Singapore" (Q-77-05). | Mở |
| OQ-02 | Trẻ đi xe đưa đón đến muộn vì xe có bị tính Late không? | Mở |
| OQ-03 | Centre Director có được tự đổi giờ chốt của Centre mình không, hay chỉ HQ Admin? | Mở |
| OQ-04 *(mới)* | Có cần cờ "đón muộn" (late pickup) không? Prototype có tab "Late arrival & pickup", SRS không có. | Mở |
| AS-01 | Chỉ HQ Admin đổi giờ chốt. | Chờ OQ-03 |
| AS-02 *(sửa)* | Hai giờ chốt (sáng, chiều) cho mọi trẻ của Centre. | Chờ OQ-05 |
