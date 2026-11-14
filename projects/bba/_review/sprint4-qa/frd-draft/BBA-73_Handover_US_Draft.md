# [Nháp] BBA-73 Handover recording (dropped off by / picked up by) — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + SRS Daily Operations, Attendance App, Centre Director App + prototype SMS (Class attendance, cột Handover).
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-73/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. "Other" + ghi chú → **"Someone else" + Name + Relationship** (2 ô riêng) theo SRS Attendance App.
2. OQ-01 đã có câu trả lời trong SRS: **không có người đón một lần**, mọi người đón phải qua duyệt (BR-CDP-025) → giữ chặn, đóng OQ-01.
3. Người duyệt người đón: Centre Director hoặc School Admin (BR-CDP-024).
4. Thông báo cho phụ huynh không nhắc cờ đến muộn và tên nhân viên ở cổng (BR-ATT-051).

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Check-out chỉ người đã duyệt, **không có override**; người lạ → Centre gọi phụ huynh, phụ huynh điền đủ thông tin ngay rồi người đó mới được đón (Q-75-02, Q-75-04) → FR-004.
- Xe đưa đón: bộ lọc theo xe chỉ để gom; **nhận / trả từng trẻ, ảnh riêng**; người giao là tài xế, người nhận về là phụ xe của công ty xe (Q-75-10) → FR-008.
- Parents App hiện ảnh lúc giao nhận (Q-81-02) → FR-010.
- Ô nhập tay ở check-in: DOTB tự quyết (Q-75-02) → chỉ hiện khi chọn "Someone else".

**Cập nhật theo Plane (14/11/2026)**
- Không có task "BBA input…" riêng cho BBA-73; [BBA confirm] BBA-1087 chưa có comment.
- Mô tả ticket BBA-73 ghi "'other' with note" và "picker verification **warning** if not on the list" — BBA đã chốt mới hơn ở Q-75-04: **chặn, không override** → giữ FR-004 (chặn).
- BBA-544 (Todo, chưa trả lời): người đón một lần **không có ở Phase 1** (khớp BR-002); phụ huynh thêm người đón cần duyệt, **xoá có hiệu lực ngay**; workshop recap ghi người duyệt là **"teacher or Centre Director"** — lệch với SRS BR-CDP-024 (Centre Director hoặc School Admin) → OQ-06. Câu "người mới chưa duyệt có được đón không" vẫn mở ở BBA-544 nhưng Q-75-02/04 đã chốt là không.
- BBA-494: Attendance app **chạy khi mất mạng và tự đồng bộ** (Phase 1) → FR-011 mới, AS-04, AS-05, OQ-07; wireframe thêm trạng thái "iPad cổng · mất mạng".
- BBA-493: BBA hỏi giữ log dữ liệu cá nhân **tới 3 năm sau khi trẻ rời trường**, chưa chốt; liên hệ DPO@busybeesasia.com → liên quan OQ-05 (thời gian lưu ảnh), chưa đủ để đóng.
- Wireframe thêm: "Someone else · thiếu quan hệ" (VAL-001), "Trả trẻ lên xe" (phụ xe — OQ-04), "iPad cổng · mất mạng".

---

## US-001 - Ghi người đưa trẻ đến và người đón trẻ về

#### User Story

Là nhân viên ở cổng, khi nhận và trả trẻ tôi muốn chọn nhanh người đưa / người đón từ danh sách của trẻ và được hệ thống chặn nếu người đón không có trong danh sách, để trẻ chỉ được giao cho đúng người.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(sửa)* | Khi nhận trẻ, nhân viên chọn "Brought by" từ danh sách gồm phụ huynh và người được phép đón đã duyệt của trẻ, hoặc chọn "Someone else" và nhập Name, Relationship (cả hai bắt buộc). |
| FR-002 | Khi trả trẻ, nhân viên chọn "Collected by" từ danh sách người được phép đón đã duyệt (gồm cả phụ huynh). Mỗi người hiện ảnh, họ tên, quan hệ với trẻ và 4 ký tự cuối giấy tờ, để nhân viên đối chiếu. |
| FR-003 *(sửa)* | Người phụ huynh đã thêm nhưng Centre Director / School Admin chưa duyệt hiện với chữ "Pending approval" và không chọn được khi trả trẻ. |
| FR-004 *(sửa)* | Khi người đến đón không có trong danh sách, nhân viên chọn "Not on the list"; hệ thống không cho trả trẻ và hiện hướng dẫn "Do not release the child. Call the parent to add this person in the Parents App. The person can collect the child once approved." Không có cơ chế override (Q-75-04). |
| FR-005 | Giờ nhận và giờ trả mặc định là giờ hiện tại; nhân viên sửa được trong cùng ngày; giờ trả không được trước giờ nhận. |
| FR-006 | Bảng điểm danh của lớp có cột "Handover" ghi "Dropped off by" và "Picked up by" kèm tên người. |
| FR-007 *(sửa)* | Thông báo nhận trẻ và trả trẻ gửi cho phụ huynh ghi tên người đưa / người đón và giờ; không nhắc cờ đến muộn và tên nhân viên ở cổng. |
| FR-008 *(sửa)* | Bộ lọc theo tuyến xe gom trẻ của một xe vào một danh sách; nhận và trả vẫn làm từng trẻ, mỗi trẻ một bản ghi và ảnh riêng. Lúc xe đến, người giao là tài xế; lúc xe về, người nhận là phụ xe của công ty xe (Q-75-10). |
| FR-009 | Mỗi lượt nhận / trả lưu người đưa / người đón, giờ, nhân viên thực hiện và thiết bị dùng (SMS web hoặc ứng dụng điểm danh). |
| FR-011 *(mới)* | Ở ứng dụng điểm danh tại cổng, khi mất mạng nhân viên vẫn nhận / trả trẻ: danh sách người đón đã duyệt lấy theo lần đồng bộ gần nhất (hiện thời điểm đồng bộ); lượt nhận / trả lưu trên máy và tự gửi khi có mạng; thông báo cho phụ huynh gửi khi lượt đó được đồng bộ (Plane BBA-494; AS-04, AS-05). |
| FR-010 *(mới)* | Mỗi lượt nhận / trả chụp ảnh trẻ cùng người giao / nhận; Parents App hiện ảnh này để phụ huynh thấy ai đưa / đón (Q-75-10, Q-81-02; SRS Daily Operations "Check out: time, photo and the person collecting"). |

#### Functional Flow - Main (Luồng chính)

1. Buổi sáng, nhân viên chọn trẻ, chọn người đưa (FR-001), lưu giờ nhận (FR-005).
2. Buổi chiều, nhân viên chọn trẻ, chọn người đón, đối chiếu ảnh và giấy tờ (FR-002), lưu giờ trả (FR-005).
3. Phụ huynh nhận thông báo có tên người đưa / người đón (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. *(sửa)* Người đưa không có trong danh sách: chọn "Someone else", nhập tên và quan hệ (FR-001).
2. Trẻ đi xe: nhận theo tuyến xe, trả từng trẻ (FR-008).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người đón không có trong danh sách: không trả trẻ, gọi phụ huynh và Centre Director (FR-004; VAL-002).
2. Người đón đang chờ duyệt: không chọn được (FR-003).
3. Giờ trả trước giờ nhận: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Trẻ chỉ được trả cho người có trong danh sách người được phép đón đã duyệt. |
| BR-002 *(sửa)* | Người mới phải được phụ huynh thêm trong Parents App và Centre Director hoặc School Admin duyệt trước khi đón trẻ. Không có người đón một lần. |
| BR-003 | Người đưa trẻ đến được ghi theo người thật sự đưa trẻ, không phải nhân viên bấm nút. |
| BR-004 | Lượt nhận / trả đã lưu không bị xoá; sửa giờ hoặc người phải có lý do (BBA-77). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 *(sửa)* | Chọn "Someone else" khi nhận trẻ nhưng để trống Name hoặc Relationship. | Không lưu; hiện "Enter the name and relationship of the adult." |
| VAL-002 | Chọn "Not on the list" khi trả trẻ. | Không lưu lượt trả; hiện "Do not release the child. Call the parent and the Centre Director." |
| VAL-003 | Giờ trả trước giờ nhận, hoặc giờ sau thời điểm hiện tại. | Không lưu; hiện "Check the time." |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Brought by *(sửa)* | Danh sách chọn | Có | Trống | VAL-001. | Phụ huynh, người được phép đón, "Someone else". |
| Name, Relationship *(mới)* | Ô nhập | Khi chọn Someone else | Trống | VAL-001. | — |
| Collected by | Danh sách chọn có ảnh | Có | Trống | VAL-002. | Chỉ người đã duyệt; người chờ duyệt bị mờ; có "Not on the list". |
| Time | Giờ | Có | Giờ hiện tại | VAL-003. | — |
| Photo *(mới)* | Chụp ảnh | Có | — | — | FR-010. |
| Bus route *(mới)* | Bộ lọc | Không | All | — | Gom trẻ của một xe (FR-008). |
| Handover *(sửa)* | Cột bảng | — | — | — | "Dropped off by", "Picked up by" (FR-006). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 *(sửa)* | Mỗi lượt nhận / trả lưu: trẻ, loại (nhận / trả), người đưa hoặc người đón (hoặc tên và quan hệ khi Someone else), ảnh, giờ, nhân viên thực hiện, thiết bị. |
| DATA-002 | Mỗi lần chọn "Not on the list" được lưu: trẻ, giờ, nhân viên, để Centre Director xem lại. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | bà ngoại của Ethan có trong danh sách người được phép đón | nhân viên nhận Ethan và chọn bà ngoại | lượt nhận lưu "bà ngoại" và giờ hiện tại; cột Handover hiện "Dropped off by" tên bà | FR-001; FR-005; FR-006 |
| AC-002 *(sửa)* | tài xế gia đình đưa Noah đến, không có trong danh sách | nhân viên chọn "Someone else", Name "Ahmad", Relationship "Family driver" | lượt nhận được lưu kèm tên và quan hệ | FR-001; BR-003 |
| AC-003 *(sửa)* | nhân viên chọn "Someone else" nhưng để trống Relationship | chọn Sign in | không lưu, hiện "Enter the name and relationship of the adult." | VAL-001 |
| AC-004 | chú của trẻ có trong danh sách đã duyệt | nhân viên trả trẻ | danh sách hiện ảnh, họ tên, quan hệ, 4 ký tự cuối giấy tờ của chú; chọn chú thì lượt trả được lưu | FR-002; BR-001 |
| AC-005 | người đến đón không có trong danh sách | nhân viên chọn "Not on the list" | không trả trẻ; hiện "Do not release the child. Call the parent and the Centre Director."; hệ thống lưu lại lần này | FR-004; VAL-002; DATA-002 |
| AC-006 | phụ huynh vừa thêm chú Jason, Centre chưa duyệt | nhân viên mở danh sách người đón | Jason hiện "Pending approval" và không chọn được | FR-003; BR-002 |
| AC-007 | trẻ được nhận lúc 08:12 | nhân viên sửa giờ trả thành 07:50 | không lưu, hiện "Check the time." | FR-005; VAL-003 |
| AC-008 | bố đón trẻ lúc 17:40 | lượt trả được lưu | phụ huynh nhận thông báo có tên người bố và giờ 17:40 | FR-007 |
| AC-009 *(sửa)* | 6 trẻ đi xe tuyến A đến trường | nhân viên lọc tuyến A và nhận từng trẻ | 6 bản ghi riêng, mỗi bản ghi có ảnh của trẻ, người đưa là tài xế tuyến A | FR-008 |
| AC-010 | lượt nhận lưu trên ứng dụng điểm danh ở cổng | Centre Director xem lịch sử | thấy người đưa, giờ, nhân viên, thiết bị | FR-009; DATA-001; BR-004 |
| AC-011 *(mới)* | Noah đến lúc 09:34, sau giờ chốt muộn | phụ huynh nhận thông báo nhận trẻ | thông báo có tên người đưa và giờ; không có chữ "Late" và không có tên nhân viên ở cổng | FR-007 |
| AC-013 *(mới)* | iPad cổng mất mạng, lần đồng bộ gần nhất 16:55 | nhân viên trả Ethan cho bố lúc 17:40 | lượt trả lưu trên iPad với giờ 17:40; khi có mạng, lượt được gửi và phụ huynh nhận thông báo ghi 17:40 | FR-011 |
| AC-012 *(mới)* | Ethan được bố đón lúc 17:40, nhân viên chụp ảnh | phụ huynh mở Parents App | thấy ảnh lúc giao nhận và tên người đón | FR-010 |

#### Dependencies (Phụ thuộc)

Danh sách người được phép đón và việc duyệt (Children & Families, CD app); ứng dụng điểm danh ở cổng; đo nhiệt độ bắt buộc khi nhận trẻ (BBA-74); thông báo trong Parents App; sửa / huỷ điểm danh (BBA-77).

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái |
|---|---|---|
| OQ-01 | Có cho Centre Director trả trẻ cho người ngoài danh sách sau khi gọi phụ huynh không? | **Đã có trong SRS:** không — không có người đón một lần (BR-CDP-025) |
| OQ-02 | Khi nhận trẻ, "Someone else" luôn được phép? | **Đã có trong SRS:** có (SRS Attendance App) |
| OQ-03 | Thông báo cho phụ huynh có ghi tên người đưa / người đón không? | Mở (SRS chỉ cấm cờ muộn và tên nhân viên ở cổng) |
| OQ-04 | Trẻ đi xe về nhà: người nhận là phụ xe của công ty xe (Q-75-10). Phụ xe có phải nằm trong danh sách người đón đã duyệt của từng trẻ không? | Mở |
| OQ-05 *(mới)* | Ảnh và bằng chứng giao nhận lưu bao lâu, ai xem / xuất, có tự xoá không? | Mở (Q-75-12) |
| OQ-06 *(mới)* | Ai duyệt người đón mới: Centre Director và School Admin (SRS BR-CDP-024) hay teacher và Centre Director (workshop recap, Plane BBA-544)? | Mở (BBA-544) |
| OQ-07 *(mới)* | Khi iPad cổng mất mạng: người đón vừa được duyệt sau lần đồng bộ gần nhất chưa có trong danh sách — nhân viên xử lý thế nào? | Mở (BBA-494) |
| AS-03 | Thông báo cho phụ huynh có tên người đưa / người đón. | Chờ OQ-03 |
| AS-04 *(mới)* | Khi mất mạng, danh sách người đón dùng bản của lần đồng bộ gần nhất; người chưa có trong bản đó coi như "Not on the list". | Chờ OQ-07 |
| AS-05 *(mới)* | Thông báo nhận / trả trẻ gửi cho phụ huynh khi lượt đó được đồng bộ, kèm giờ thật của lượt. | FR-011 |
