# [Nháp] BBA-76 Centre-brand overview today — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + câu trả lời của BBA (Plane BBA-524) + SRS Daily Operations, Centre Director App + prototype SMS `/operations` (bảng theo Centre) và CD app `/attendance`.
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-76/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. **"District Manager" → "Cluster Head"** (BBA-524: "DM will now be known as Cluster Heads").
2. FRD đã khớp prototype SMS (Centre, Brand, Signed in of expected, Signed out, Still in, dòng tổng). Giữ nguyên.
3. CD app có thêm "Not yet in" và "Absent" — có cần cho bảng HQ không → OQ-03.

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Temporary withdrawal: không điểm danh, không tính enrolment number, vẫn trong student list (có tag), ẩn khỏi Attendance app (Q-80-01, Q-80-03) — khớp FR-002.
- Điểm danh gắn với **bản ghi enrolment**, không gắn hồ sơ trẻ (Q-80-03) → DATA-001.
- "Today" theo Centre hay người xem như nhau vì SG, MY cùng UTC+8 (Q-80-08) → BR-002.
- iPad offline: DOTB tự quyết (Q-80-05).
- Còn mở: nghỉ phép có trừ khỏi expected (Q-80-03), realtime (Q-80-04), drill-down (Q-80-07), 3 stream (Q-80-09), export (Q-80-11).

---

## US-001 - Bảng tổng hợp điểm danh hôm nay theo Centre và brand

#### User Story

*(sửa)* Là Cluster Head, tôi muốn xem trong một bảng số trẻ đã đến, đã về và còn ở trường của từng Centre tôi phụ trách, để biết ngay Centre nào có số trẻ đến thấp bất thường và mở xem lớp nào.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Bảng có một dòng cho mỗi Centre trong phạm vi người dùng: Centre, Brand, "Signed in of expected" (ví dụ "68 of 72"), "Signed out", "Still in". |
| FR-002 | Số trẻ dự kiến của một Centre = trẻ đang học có lịch học hôm nay, trừ trẻ có nghỉ phép đã duyệt hôm nay và trẻ đang tạm nghỉ. |
| FR-003 | "Still in" = số trẻ đã đến trừ số trẻ đã về; lượt điểm danh đã bị huỷ không được tính. |
| FR-004 | Lọc theo brand và Centre; mặc định "All brands", "All centres" trong phạm vi người dùng; sắp xếp mặc định theo tên Centre. |
| FR-005 | Cuối bảng có dòng tổng: số Centre đang xem, tổng trẻ đã đến / dự kiến, tổng đã về, tổng còn ở trường (ví dụ "5 of 5 centres · 224 children signed in of 246 expected · 20 signed out · 204 still in"). |
| FR-006 | Chọn một Centre mở bảng các lớp của Centre với cùng các cột; chọn một lớp mở bảng điểm danh của lớp đó. |
| FR-007 | Bảng ghi "Updated" kèm giờ lấy số liệu và có nút "Refresh". |
| FR-008 | Centre không có trẻ dự kiến hôm nay (ví dụ ngày Centre đóng cửa) vẫn hiện với "0 of 0". |

#### Functional Flow - Main (Luồng chính)

1. *(sửa)* Cluster Head mở Overview today; hệ thống hiện bảng các Centre mình phụ trách (FR-001, FR-004).
2. Cluster Head xem dòng tổng (FR-005), chọn một Centre có số trẻ đến thấp (FR-006).
3. Cluster Head chọn một lớp để xem bảng điểm danh (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lọc theo một brand (FR-004).
2. Làm mới số liệu (FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có Centre nào: bảng trống (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Người dùng chỉ thấy Centre trong phạm vi của mình. |
| BR-002 *(sửa)* | Số liệu tính theo điểm danh hôm nay (ngày theo giờ UTC+8 của Singapore và Malaysia, Q-80-08); lượt đã huỷ không được tính. |
| BR-003 | Bảng chỉ để xem; không nhận hay trả trẻ từ bảng này. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có Centre nào. | Hiện "No centres match these filters." |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Brand, Centre | Bộ lọc | Không | All | VAL-001. | FR-004. |
| Bảng Centre | Bảng | Có | Theo tên Centre | — | FR-001; FR-006. |
| Dòng tổng | Chữ | Có | — | — | FR-005. |
| Updated, Refresh | Chữ, nút | Có | Giờ mở màn | — | FR-007. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 *(sửa)* | Bảng đọc điểm danh hôm nay (gắn với bản ghi enrolment, Q-80-03), lịch học, nghỉ phép đã duyệt và trạng thái tạm nghỉ của trẻ; không lưu dữ liệu mới. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Small Wonder Tampines có 72 trẻ dự kiến, 68 trẻ đã đến, 7 trẻ đã về | HQ Admin mở bảng | dòng Tampines hiện "68 of 72", Signed out 7, Still in 61 | FR-001; FR-003 |
| AC-002 | Centre có 8 trẻ có lịch hôm nay, 1 trẻ nghỉ phép đã duyệt | hệ thống tính | số dự kiến là 7 | FR-002 |
| AC-003 *(sửa)* | Cluster Head phụ trách 4 Centre | mở bảng | chỉ thấy 4 Centre đó | FR-004; BR-001 |
| AC-004 | 5 Centre, tổng 224 trẻ đã đến, 246 dự kiến | xem cuối bảng | dòng "5 of 5 centres · 224 children signed in of 246 expected · …" | FR-005 |
| AC-005 | đang xem bảng | chọn Tampines rồi chọn lớp N2 · Sunbeams | mở bảng các lớp của Tampines, rồi bảng điểm danh lớp Sunbeams | FR-006 |
| AC-006 | một lượt điểm danh bị huỷ | hệ thống tính | lượt đó không được tính vào đã đến | FR-003; BR-002 |
| AC-007 | bảng mở lúc 10:00, có thêm trẻ đến lúc 10:05 | chọn Refresh | số liệu mới, "Updated 24/11/2026 10:05" | FR-007 |
| AC-008 | Agape Punggol đóng cửa hôm nay | mở bảng | Agape Punggol hiện "0 of 0" | FR-008 |
| AC-009 *(sửa)* | lọc brand Odyssey trong phạm vi Cluster Head không có Odyssey | xem bảng | hiện "No centres match these filters." | VAL-001 |
| AC-010 | Centre Director mở bảng | xem | chỉ có dòng Centre của mình; không có nút nhận / trả trẻ | BR-003; BR-001; DATA-001 |

#### Dependencies (Phụ thuộc)

Class attendance; nghỉ phép đã duyệt; trạng thái tạm nghỉ (Joining & leaving); phạm vi Centre của người dùng (Users & permissions).

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái |
|---|---|---|
| OQ-01 | "Expected" có trừ trẻ nghỉ phép đã duyệt và trẻ bị đánh vắng bằng tay không? | Mở — Q-80-03 chưa nói thẳng |
| OQ-02 | Số liệu cần realtime hay theo chu kỳ; độ trễ chấp nhận được? | Mở — BBA chưa trả lời (Q-80-04) |
| OQ-04 *(mới)* | Trẻ có nhiều stream (Main, Early Intervention, Enrichment) được đếm thế nào trên bảng? | Mở (Q-80-09) |
| OQ-05 *(mới)* | Drill-down có mức Country / cluster không; giữ bộ lọc nào khi mở xuống? | Mở (Q-80-07) |
| OQ-06 *(mới)* | Có cần xuất bảng; thời gian tải cho toàn bộ brand / country? | Mở (Q-80-11) |
| OQ-03 *(mới)* | Bảng HQ có cần thêm cột "Not yet in" và "Absent" như CD app không? | Mở |
| AS-01 | Trẻ dự kiến = trẻ đang học có lịch hôm nay, trừ nghỉ phép đã duyệt và tạm nghỉ; không trừ trẻ bị đánh vắng bằng tay. | Chờ OQ-01 |
| AS-02 | Số liệu làm mới khi mở màn và khi bấm Refresh. | Chờ OQ-02 |
