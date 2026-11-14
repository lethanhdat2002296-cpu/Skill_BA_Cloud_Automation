# [Nháp] BBA-77 Attendance correction with reason — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + SRS Daily Operations (BR-OPS-002, 022–024), Attendance App (BR-ATT-017–021) + prototype SMS (nút Void trên Class attendance) và CD app ("Attendance corrections"). Không có câu trả lời Plane cho ticket này.
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-77/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. SRS và prototype dùng cách **Void** (huỷ lượt sai, có lý do, có dấu vết) — thêm FR-010 đến FR-012. FRD hiện tại dùng **Correct** (sửa trực tiếp). Giữ cả hai trong bản nháp, **chờ OQ-04** chọn cách nào.
2. Giáo viên **gửi yêu cầu huỷ** để Centre Admin / CD / Senior Teacher được giao duyệt (SRS) → đóng OQ-01.
3. Trên iPad: bản ghi đã đồng bộ bị khoá, muốn đổi phải gửi yêu cầu huỷ (SRS Attendance App).

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- **Check-in nhầm phải Void (gỡ)**, không dùng check-out để thay (Q-81-01) → FR-010; OQ-04 trả lời một phần.
- Ai cũng gửi yêu cầu; Admin, CD, Senior Teacher được chỉ định duyệt, chính họ void không cần duyệt (Q-81-03, Q-75-08) — khớp FR-010, FR-011.
- Void check-in đổi trạng thái đủ điều kiện subsidy và cảnh báo ngày 18; e-Form 1 gửi ECDA ngày có điểm danh thật đầu tiên, lô 12:00 trưa (Q-81-07) → FR-007.
- Audit trail bắt buộc ở Singapore (Q-81-05) — khớp BR-002.
- Chưa đồng bộ sửa trên iPad, đã đồng bộ void trên web: DOTB tự quyết (Q-81-10) — khớp BR-005.

---

## US-001 - Sửa điểm danh có lý do

#### User Story

Là Centre Admin, tôi muốn sửa hoặc huỷ lượt điểm danh bị ghi sai và ghi rõ lý do, để số liệu đúng mà vẫn biết trước đó đã ghi gì.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(chờ OQ-04)* | Ở dòng của trẻ trên bảng điểm danh của một ngày, người có quyền chọn "Correct" để sửa: trạng thái (Present, Absent), giờ nhận, giờ trả, người đưa, người đón. |
| FR-002 | Ô lý do là bắt buộc (ít nhất 10 ký tự); không có lý do thì không lưu. |
| FR-003 | Khi lưu, giá trị cũ, giá trị mới, lý do, người sửa và thời điểm được ghi vào lịch sử của lượt điểm danh; giá trị cũ không bị mất. |
| FR-004 | Trạng thái "On leave" không chọn được khi sửa; nghỉ phép chỉ đến từ đơn xin nghỉ đã duyệt. |
| FR-005 | Sửa giờ nhận thì hệ thống tính lại dấu đến muộn (BBA-75). |
| FR-006 | Sửa trạng thái từ Absent sang Present thì phải nhập giờ nhận; người đưa chọn theo quy tắc nhận trẻ (BBA-73). |
| FR-007 *(sửa)* | Ngày đã sửa hoặc huỷ được tính lại trong báo cáo điểm danh, bảng tổng hợp, trạng thái đủ điều kiện subsidy và danh sách trẻ chưa có ngày đi học trong tháng (kiểm tra ngày 18) (Q-81-07). |
| FR-008 | Chọn biểu tượng lịch sử ở dòng của trẻ để xem mọi lần sửa / huỷ của lượt điểm danh đó. |
| FR-009 | Không sửa được điểm danh của ngày sau hôm nay; ngày cũ hơn số ngày cho phép (AS-02) không sửa được. |
| FR-010 *(mới)* | "Void record" ở dòng của trẻ: hiện lượt đang có (giờ, người đưa / đón, nhiệt độ), ô lý do bắt buộc. Centre Admin, Centre Director và Senior Teacher được giao huỷ trực tiếp, không cần duyệt. Lượt bị huỷ không được tính vào điểm danh; nhân viên ghi lại lượt đúng như bình thường. Check-in nhầm phải huỷ, không dùng check-out để thay (Q-81-01). |
| FR-011 *(mới)* | Teacher và nhân viên dùng iPad ở cổng gửi "Void request" kèm tên và lý do; yêu cầu vào My approvals của Centre Admin, Centre Director và Senior Teacher được giao để duyệt hoặc từ chối; người gửi nhận thông báo kết quả. |
| FR-012 *(mới)* | Tab "Void log" của Class attendance liệt kê lượt đã huỷ: trẻ, lớp, lượt bị huỷ, người yêu cầu, người duyệt (hoặc "Voided directly"), thời điểm, lý do. |

#### Functional Flow - Main (Luồng chính)

1. Centre Admin mở bảng điểm danh ngày cần sửa, chọn Correct hoặc Void record ở dòng của trẻ (FR-001, FR-010).
2. Centre Admin sửa giá trị hoặc xác nhận huỷ, nhập lý do (FR-002), chọn lưu.
3. Hệ thống lưu lịch sử (FR-003), tính lại dấu đến muộn và số liệu (FR-005, FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Trẻ bị đánh vắng nhầm: sửa sang Present, nhập giờ nhận (FR-006).
2. Xem lịch sử sửa (FR-008).
3. *(mới)* Giáo viên gửi yêu cầu huỷ; Centre Admin duyệt; lượt bị huỷ (FR-011).
4. *(mới)* Centre Director xem Void log (FR-012).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không có lý do: không lưu (VAL-001).
2. Giờ trả trước giờ nhận: không lưu (VAL-002).
3. Ngày quá giới hạn sửa: không sửa được (VAL-003).
4. Người không có quyền: không có nút Correct, Void record (VAL-004).
5. *(mới)* Yêu cầu huỷ bị từ chối: lượt giữ nguyên, người gửi nhận lý do từ chối (FR-011).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mọi lần sửa hoặc huỷ điểm danh phải có lý do. |
| BR-002 | Giá trị cũ luôn được giữ trong lịch sử; không ai xoá được lịch sử. |
| BR-003 | Centre Admin, Centre Director, Senior Teacher được giao và HQ Admin được sửa / huỷ trực tiếp. |
| BR-004 | Nghỉ phép chỉ đến từ đơn xin nghỉ đã duyệt, không sửa tay. |
| BR-005 *(mới)* | Trên iPad, bản ghi chưa đồng bộ được sửa ngay; bản ghi đã đồng bộ bị khoá, muốn đổi phải gửi yêu cầu huỷ (SRS BR-ATT-017–021). Không huỷ trực tiếp trên iPad vì dùng tài khoản chung của Centre. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Lý do trống hoặc dưới 10 ký tự. | Không lưu; hiện "Enter a reason (at least 10 characters)." |
| VAL-002 | Giờ trả trước giờ nhận, hoặc sửa sang Present mà không có giờ nhận. | Không lưu; hiện "Check the times." |
| VAL-003 | Ngày sau hôm nay hoặc cũ hơn giới hạn sửa. | Không có nút Correct / Void record; hiện "This day can no longer be corrected." khi rê chuột. |
| VAL-004 | Người dùng không có quyền sửa. | Không có nút Correct / Void record; Teacher thấy "Request void". |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Correct *(chờ OQ-04)* | Nút / menu ⋯ | Theo quyền | — | VAL-003; VAL-004. | Mở cửa sổ sửa. |
| Void record *(mới)* | Menu ⋯ | Theo quyền | — | VAL-003; VAL-004. | Mở cửa sổ huỷ (FR-010). |
| Request void *(mới)* | Menu ⋯ | Teacher | — | — | FR-011. |
| Status | Danh sách chọn | Có | Giá trị hiện tại | — | Present, Absent (FR-004). |
| Sign-in / sign-out time | Giờ | Theo trạng thái | Giá trị hiện tại | VAL-002. | — |
| Reason | Ô nhập | Có | Trống | VAL-001. | — |
| History | Cửa sổ chi tiết | — | Đóng | — | FR-008. |
| Void log *(mới)* | Tab | — | — | — | FR-012. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lần sửa lưu: trẻ, ngày điểm danh, trường được sửa, giá trị cũ, giá trị mới, lý do, người sửa, thời điểm. |
| DATA-002 *(mới)* | Mỗi lần huỷ lưu: lượt bị huỷ, người yêu cầu, người duyệt (hoặc huỷ trực tiếp), thời điểm, lý do; yêu cầu bị từ chối lưu thêm lý do từ chối. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Chloe bị đánh vắng nhầm hôm qua | Centre Admin sửa sang Present, giờ nhận 08:20, lý do "Trẻ có đến, ghi nhầm khi nhận" | điểm danh hôm qua là Present 08:20; lịch sử có Absent → Present, lý do, người sửa | FR-001; FR-003; FR-006; BR-002 |
| AC-002 | Centre Admin sửa giờ nhưng để trống lý do | chọn lưu | không lưu, hiện "Enter a reason (at least 10 characters)." | FR-002; VAL-001; BR-001 |
| AC-003 | giờ nhận 09:34 có dấu Late | sửa thành 08:34 có lý do | dấu Late bị bỏ | FR-005 |
| AC-004 | Centre Admin mở cửa sổ sửa | xem danh sách trạng thái | không có On leave | FR-004; BR-004 |
| AC-005 | giờ nhận 08:12 | sửa giờ trả thành 07:00 | không lưu, hiện "Check the times." | VAL-002 |
| AC-006 *(sửa)* | Teacher mở bảng điểm danh | xem menu ở dòng của trẻ | không có Correct, Void record; có Request void | VAL-004; BR-003 |
| AC-007 | Chloe là trẻ Singapore chưa có ngày đi học trong tháng | sửa một ngày sang Present | Chloe không còn trong danh sách "No attendance this month" | FR-007 |
| AC-008 | ngày cũ hơn giới hạn sửa | Centre Admin xem dòng của trẻ | không có nút Correct, Void record | FR-009; VAL-003 |
| AC-009 | lượt điểm danh đã sửa 2 lần | Centre Director mở lịch sử | thấy 2 lần sửa với giá trị cũ, giá trị mới, lý do, người sửa, thời điểm | FR-008; DATA-001 |
| AC-010 *(mới)* | Noah bị nhận nhầm ở cổng lúc 09:34 | Centre Director chọn Void record, lý do "Signed in against the wrong child at the gate" | lượt bị huỷ không còn tính; Void log có dòng "Voided directly" với người, thời điểm, lý do | FR-010; FR-012; DATA-002 |
| AC-011 *(mới)* | giáo viên gửi yêu cầu huỷ lượt của Noah | Centre Admin duyệt trong My approvals | lượt bị huỷ; giáo viên nhận thông báo "approved"; Void log ghi người yêu cầu và người duyệt | FR-011; FR-012 |
| AC-012 *(mới)* | lượt nhận trên iPad đã đồng bộ | nhân viên ở cổng mở lượt đó trên iPad | không sửa được; chỉ có "Request void" | BR-005 |

#### Dependencies (Phụ thuộc)

Class attendance; ghi người đưa / người đón (BBA-73); dấu đến muộn (BBA-75); My approvals; báo cáo điểm danh; danh sách trẻ chưa có ngày đi học trong tháng; quyền giao cho Senior Teacher.

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái |
|---|---|---|
| OQ-01 | Giáo viên có được gửi yêu cầu sửa không? | **Đã có trong SRS:** gửi yêu cầu huỷ, người được giao duyệt (BR-OPS-022; BR-ATT-019, 020) |
| OQ-02 | Sau mốc nào điểm danh bị khoá: cuối ngày, chốt tháng, sau khi gửi subsidy? | Mở — cao (Q-81-09) |
| OQ-03 | Có danh mục lý do (reason code) ngoài ô nhập tự do không? | Mở (Q-81-05) |
| OQ-04 *(mới)* | Check-in nhầm cả lượt → **Void** (đã chốt, Q-81-01). Còn sai giờ / người (lượt đúng nhưng ghi sai) thì sửa trực tiếp (Correct) hay cũng Void rồi ghi lại? | Mở — cao |
| OQ-05 *(mới)* | Trường nào được sửa: giờ, người giao / nhận, ảnh, nhiệt độ, trạng thái nghỉ? | Mở (Q-81-02) |
| OQ-06 *(mới)* | Phụ huynh có được báo khi lượt nhận / trả đã gửi bị sửa hoặc huỷ không? | Mở (Q-81-08) |
| OQ-07 *(mới)* | Huỷ check-in sau 12:00 (e-Form 1 đã gửi ECDA) thì xử lý thế nào? | Mở (Q-81-07, Q-81-09) |
| AS-02 | Chỉ sửa được ngày trong tháng hiện tại và tháng trước. | Chờ OQ-02 |
| AS-03 | Lý do tối thiểu 10 ký tự. | — |
