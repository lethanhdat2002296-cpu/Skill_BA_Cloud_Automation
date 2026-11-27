# Functional Requirements Specification — Authorised Pickup Verification

**Dự án:** Busy Bees Asia SMS · **Module:** Attendance App (gate iPad) — Kiosk · **Tính năng:** BBA-150 Authorised pickup verification  
**Mã tài liệu:** FRD-4.4.1.04_Authorised_Pickup_Verification · **Sprint:** 5 · **Phiên bản:** 0.2 · **Trạng thái:** Bản nháp chờ xác nhận · **Ngày:** 27/11/2026  
**Người soạn:** Business Analysis · **Người review:** HaiNguyen · **Người duyệt:** HaiNguyen

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 26/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 27/11/2026 | Business Analysis | Ẩn hẳn số giấy tờ định danh trên iPad (BBA-66); bổ sung luồng phụ huynh thêm người đón khi Centre gọi (Q-75-04); check-in xe bus từng trẻ (Q-75-10); thêm Câu hỏi mở. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu. Đã đối chiếu bảng câu hỏi Sprint 4 và BBA-66; 1 câu hỏi mở ở mục 7.

## 2. Mục đích và bối cảnh

Tài liệu đặc tả việc xác định người đưa và xác minh người đón trên Attendance App (iPad tại cổng). Khi check-in, nhân viên ghi người đưa trẻ đến. Khi check-out, iPad hiển thị danh sách người được phép đón đã duyệt (ảnh, họ tên, quan hệ) để nhân viên đối chiếu và chọn người đón; người không có trong danh sách không đón được trẻ.

Danh sách người được phép đón do phụ huynh thêm trên Parents App và Centre Director hoặc School Admin duyệt trên SMS (Children & Families). Quy tắc người đưa / người đón thống nhất với BBA-73 (Handover recording) trên SMS.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Chọn người đưa khi check-in (người thân, người được phép đón, Someone else, Bus driver); hiển thị và chọn người đón khi check-out chỉ từ danh sách đã duyệt (thêm Bus attendant với trẻ đi xe bus); chặn check-out khi người đến đón không có trong danh sách và báo Centre; chặn check-out khi trẻ chưa check-in; cập nhật danh sách trên iPad; thông báo check-out cho phụ huynh. | Thêm, duyệt, xoá người được phép đón (Parents App, SMS); đón tạm thời một lần; người đón có thời hạn hiệu lực; Centre Director duyệt đón ngoại lệ trên iPad; chụp ảnh bàn giao (BBA-149); nhiệt độ (BBA-151); sửa thông tin đưa / đón trên SMS (BBA-73). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Nhân viên tại cổng | Trẻ của Centre theo phạm vi iPad. | Chọn người đưa, người đón; lưu check-in / check-out; báo người không có trong danh sách. |
| Centre Director, School Admin | Centre được cấp. | Nhận cảnh báo người không có trong danh sách; duyệt người được phép đón trên SMS. |
| Phụ huynh (Guardian) | Trẻ liên kết với tài khoản. | Thêm, xoá người được phép đón trên Parents App; nhận thông báo check-out. |
| System | Bản ghi điểm danh, danh sách người được phép đón, dịch vụ xe bus. | Cung cấp danh sách trên iPad; kiểm tra người đón; gửi cảnh báo và thông báo; đồng bộ. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-150 gồm hai User Story trên Attendance App, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| Kiosk | Ghi người đưa khi check-in | Chọn người đưa từ người thân, người được phép đón, Someone else hoặc Bus driver. | BBA-150: US-001 |
| Kiosk | Xác minh người đón khi check-out | Đối chiếu và chọn người đón chỉ từ danh sách đã duyệt; chặn và báo khi không có trong danh sách. | BBA-150: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-150: US-001 - Ghi người đưa khi check-in

#### User Story

Là nhân viên tại cổng, tôi muốn ghi ai đưa trẻ đến, để Centre và phụ huynh biết trẻ được bàn giao bởi ai.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải yêu cầu chọn người đưa cho mỗi lần check-in. |
| FR-002 | Danh sách người đưa gồm người thân của trẻ, người được phép đón đã duyệt, Someone else; thêm Bus driver với trẻ đi xe bus. |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên tìm trẻ và mở Check in.
2. Hệ thống hiển thị danh sách người đưa theo FR-002, mỗi người có ảnh (nếu có), họ tên, quan hệ.
3. Nhân viên chọn người đưa, chụp ảnh (BBA-149), nhập nhiệt độ (BBA-151) và Save. Hệ thống lưu bản ghi với người đưa (FR-001).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người đưa không có trong danh sách: nhân viên chọn Someone else, nhập họ tên và quan hệ với trẻ (BR-002).
2. Trẻ đi xe bus: nhân viên lọc theo xe để gom trẻ của một xe vào danh sách; check-in vẫn làm từng trẻ, người đưa mặc định là Bus driver kèm số xe (BR-003; Q-75-10).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ đã check-in hôm nay: không có Check in; hiện “Already checked in at <giờ>”.
2. Someone else thiếu họ tên hoặc quan hệ: báo lỗi, không lưu (VAL-001).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi check-in ghi một người đưa. Không ghi, không hiển thị nhân viên bấm nút. |
| BR-002 | Người đưa không có trong danh sách: chọn Someone else, nhập họ tên và quan hệ (bắt buộc). Người đưa không cần duyệt (Q-75-02). |
| BR-003 | Bus driver chỉ có với trẻ được gán dịch vụ xe bus; kèm số xe. Lọc theo xe chỉ gom danh sách; mỗi trẻ một bản ghi check-in riêng (Q-75-10). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Someone else thiếu họ tên hoặc quan hệ. | Báo “Enter the name and relationship of the adult.” và không lưu. |
| VAL-002 | Chưa chọn người đưa. | Nút Save không dùng được. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-150: UI-US-001 - Check in (người đưa) | https://bba-attendance-visitor.lovable.app/ |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Dropped off by | Danh sách chọn | Có | Chưa chọn; Bus driver khi check-in theo xe bus | FR-001;FR-002;VAL-002 | Ảnh, họ tên, quan hệ của từng người. |
| Someone else | Lựa chọn | — | — | BR-002 | Mở ô nhập họ tên, quan hệ. |
| Họ tên / Quan hệ | Ô nhập | Khi chọn Someone else | Trống | VAL-001 | Thông tin người đưa ngoài danh sách. |
| Bus driver (số xe) | Lựa chọn | — | Chỉ trẻ đi xe bus | BR-003 | Ví dụ “Bus driver · Bus 2”. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Lưu người đưa với bản ghi check-in: loại (người thân / người được phép đón / Someone else / Bus driver), mã người hoặc họ tên và quan hệ nhập tay, số xe. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Mia có mẹ, bố là người thân và bà là người được phép đón | nhân viên mở Check in cho Mia | danh sách người đưa có mẹ, bố, bà và Someone else | FR-002 |
| AC-002 | Người giúp việc Siti đưa Noah đến | nhân viên chọn Someone else, nhập “Siti”, “Helper” và Save | bản ghi có người đưa Siti, quan hệ Helper | BR-002 |
| AC-003 | Như AC-002, để trống quan hệ | nhân viên chọn Save | báo “Enter the name and relationship of the adult.”, không lưu | VAL-001 |
| AC-004 | Lucas đi Bus 2, Mia không đi xe bus | nhân viên mở Check in của từng trẻ | Lucas có lựa chọn “Bus driver · Bus 2”; Mia không có | BR-003 |
| AC-005 | Mia đã check-in lúc 08:10 | nhân viên mở Mia | hiện “Already checked in at 08:10”, không có Check in | FR-001 |

#### Dependencies (Phụ thuộc)

Người thân của trẻ, người được phép đón (Children & Families); dịch vụ xe bus; BBA-149; BBA-151; BBA-73.

### 6.2 BBA-150: US-002 - Xác minh người đón khi check-out

#### User Story

Là nhân viên tại cổng, tôi muốn chỉ trả trẻ cho người đã được duyệt và đối chiếu được mặt người đón, để trẻ không bị đón nhầm.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-003 | Hệ thống phải hiển thị danh sách người được phép đón đã duyệt của trẻ khi check-out, mỗi người có ảnh lớn, họ tên, quan hệ. |
| FR-004 | Hệ thống phải chỉ cho chọn người đón trong danh sách đã duyệt; thêm Bus attendant với trẻ đi xe bus. |
| FR-005 | Khi người đến đón không có trong danh sách, hệ thống phải không cho check-out, hiển thị hướng dẫn và gửi cảnh báo cho Centre Director và School Admin. |
| FR-006 | Hệ thống phải gửi thông báo check-out cho mỗi phụ huynh, nêu người đón và giờ. |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên tìm trẻ và mở Check out.
2. Hệ thống hiển thị danh sách người được phép đón đã duyệt (FR-003).
3. Nhân viên đối chiếu mặt người đón với ảnh và chọn người đón (FR-004).
4. Nhân viên chụp ảnh (BBA-149) và Save. Hệ thống lưu bản ghi; khi bản ghi tới SMS, phụ huynh nhận thông báo check-out (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người đến đón không có trong danh sách: nhân viên chọn Person not on the list. Hệ thống hiển thị hướng dẫn theo BR-007, không cho lưu check-out, gửi cảnh báo (FR-005).
2. Người đến đón chưa có trong danh sách và phụ huynh xác nhận qua điện thoại: phụ huynh thêm người đó trên Parents App và người đó được duyệt; khi iPad cập nhật danh sách (BR-006), nhân viên chọn người đó và check-out (BR-007; Q-75-04).
3. Trẻ đi xe bus về: chọn Bus attendant kèm số xe; check-out từng trẻ một.
4. iPad mất mạng: dùng danh sách đã lưu trên iPad gần nhất, hiển thị “Pickup list last updated <giờ>” (BR-006).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa check-in hôm nay: hiển thị “<Tên trẻ> is not checked in today.” và nút Check in first; không check-out (VAL-003).
2. Trẻ không có người được phép đón nào: hiển thị “No approved pickup persons” và áp dụng luồng người không có trong danh sách (BR-007).
3. Trẻ đã check-out hôm nay: không có Check out; hiển thị “Already checked out at <giờ>”.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-004 | Người đón chỉ chọn từ danh sách người được phép đón đã duyệt. Người đang chờ duyệt, bị từ chối hoặc đã bị xoá không hiển thị. Không có người đón tạm thời và không có cơ chế cho đón ngoại lệ (override) trên iPad (Q-75-02, Q-75-04). |
| BR-005 | Người được phép đón không có thời hạn hiệu lực; còn hiệu lực đến khi phụ huynh xoá. |
| BR-006 | iPad cập nhật danh sách người được phép đón tối đa mỗi 5 phút khi có mạng và mỗi lần mở Check out. Phụ huynh xoá một người thì người đó không còn chọn được từ lần cập nhật kế tiếp. |
| BR-007 | Người không có trong danh sách: hiển thị “Only approved pickup persons can collect <tên trẻ>. Contact the Centre Director. A parent can add a new person in the Parents App.”. Centre gọi phụ huynh; phụ huynh thêm đủ thông tin người đón trên Parents App; người đó chỉ đón được khi đã có trong danh sách đã duyệt. Đến lúc đó trẻ ở lại Centre (Q-75-04). |
| BR-008 | Cảnh báo người không có trong danh sách gửi Centre Director và School Admin của Centre (in-app trên SMS và Centre Director App), gồm tên trẻ, lớp, thời điểm. |
| BR-009 | Không check-out trẻ chưa check-in. Mỗi trẻ một check-out mỗi ngày. |
| BR-010 | Thông báo check-out gửi khi bản ghi tới SMS, nêu họ tên người đón và giờ check-out thực tế; không nêu nhân viên tại cổng. |
| BR-011 | Không hiển thị số giấy tờ định danh (NRIC / FIN / passport) và số điện thoại của người đón trên iPad. Số giấy tờ là trường được bảo vệ theo vai trò (BBA-66 US-003); tài khoản Centre trên iPad không có quyền xem. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Mở Check out cho trẻ chưa check-in. | Hiện “<Tên trẻ> is not checked in today.” và Check in first; không check-out. |
| VAL-004 | Chưa chọn người đón. | Nút Save không dùng được. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-150: UI-US-002 - Check out (người đón) | https://bba-attendance-visitor.lovable.app/ |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Collected by | Danh sách chọn | Có | Chưa chọn | FR-003;FR-004;VAL-004;BR-004;BR-011 | Thẻ người được phép đón: ảnh lớn, họ tên, quan hệ. |
| Bus attendant (số xe) | Lựa chọn | — | Chỉ trẻ đi xe bus | FR-004 | Ví dụ “Bus attendant · Bus 2”. |
| Person not on the list | Thao tác | — | Luôn hiện | FR-005;BR-007 | Hiện hướng dẫn, gửi cảnh báo; không lưu check-out. |
| Pickup list last updated | Thông điệp | — | Hiện khi mất mạng | BR-006 | Thời điểm cập nhật danh sách gần nhất. |
| Check in first | Thao tác | — | Hiện khi trẻ chưa check-in | VAL-003 | Mở Check in của trẻ. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Lưu người đón với bản ghi check-out: mã người được phép đón hoặc Bus attendant và số xe. |
| DATA-003 | Lưu cảnh báo người không có trong danh sách: trẻ, Centre, thời điểm, iPad; gửi theo BR-008. |
| DATA-004 | Lưu trên iPad bản sao danh sách người được phép đón của trẻ trong phạm vi iPad và thời điểm cập nhật. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-006 | Mia có mẹ, bà (đã duyệt) và chú David (chờ duyệt) | nhân viên mở Check out cho Mia | chỉ hiện mẹ và bà, mỗi người có ảnh, họ tên, quan hệ; không có số giấy tờ, số điện thoại | FR-003;BR-004;BR-011 |
| AC-007 | Người đến đón Mia không có trong danh sách | nhân viên chọn Person not on the list | hiện hướng dẫn theo BR-007; không lưu check-out; Centre Director và School Admin nhận cảnh báo | FR-005;BR-007;BR-008 |
| AC-008 | Sarah xoá Uncle David lúc 10:00, iPad có mạng | nhân viên mở Check out cho Emma lúc 10:10 | Uncle David không có trong danh sách | BR-006 |
| AC-009 | Noah chưa check-in hôm nay | nhân viên mở Check out cho Noah | hiện “Noah is not checked in today.” và Check in first | VAL-003;BR-009 |
| AC-010 | Nhân viên check-out Emma cho Grandma Lim lúc 17:30 | bản ghi tới SMS | mỗi phụ huynh của Emma nhận thông báo nêu Grandma Lim và 17:30 | FR-006;BR-010 |
| AC-011 | iPad mất mạng từ 15:00, danh sách cập nhật lúc 14:58 | nhân viên mở Check out lúc 16:00 | danh sách lúc 14:58 được dùng, hiện “Pickup list last updated 14:58” | BR-006 |
| AC-012 | Lucas đi Bus 2 về | nhân viên mở Check out cho Lucas | có lựa chọn “Bus attendant · Bus 2” | FR-004 |
| AC-013 | Chú David đến đón Mia, chưa có trong danh sách; Centre gọi mẹ Mia | mẹ Mia thêm chú David trên Parents App, chú David được duyệt và iPad cập nhật danh sách | nhân viên chọn được chú David và check-out Mia | BR-006;BR-007 |

#### Dependencies (Phụ thuộc)

US-001; người được phép đón (Parents App, SMS Children & Families); dịch vụ xe bus; BBA-149; thông báo Parents App; Centre Director App; BBA-73. BBA-66 (trường được bảo vệ).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Nguồn | Giả định đang dùng | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Người phụ huynh thêm gấp khi Centre gọi điện có cần Centre Director / School Admin duyệt trước khi đón không? | Q-75-04 | Có: chỉ người đã duyệt mới hiện trên iPad (BR-004). |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Người đưa (Dropped off by) | Người lớn bàn giao trẻ cho Centre khi check-in. |
| Người đón (Collected by) | Người nhận trẻ từ Centre khi check-out. |
| Người được phép đón | Người phụ huynh thêm trên Parents App, được Centre Director / School Admin duyệt. |
| Someone else | Người đưa không có trong danh sách; nhân viên nhập họ tên, quan hệ. |
| Person not on the list | Người đến đón không có trong danh sách đã duyệt; không được đón trẻ. |
