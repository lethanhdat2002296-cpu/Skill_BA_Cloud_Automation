# Consent Status per Child and Send Consent Request

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Documents & consents |
| Tính năng | BBA-71 Consent status per child & send consent request |
| Mã tài liệu | FRD-3.1.4.01_Consent_Status_Per_Child |
| Sprint | 4 |
| Phiên bản | 0.4 |
| Trạng thái | BẢN NHÁP CHỜ XÁC NHẬN |
| Ngày | 22/11/2026 |
| Người soạn | Business Analysis |
| Người review | HaiNguyen |
| Người duyệt | HaiNguyen |

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.3 | 16/11/2026 | Business Analysis | FR viết dạng tổng quan; quy tắc chi tiết chuyển xuống Business Rules. | |
| 0.4 | 22/11/2026 | Business Analysis | Theo góp ý: tách thành 3 User Story theo chức năng (xem danh sách consent theo phiên bản; tạo và gửi; gửi lại và nhắc). Bỏ Consent compliance (ngoài phạm vi), bỏ phát hành phiên bản mới, rút lại consent, tick checklist và chặn gắn tên ảnh. Đối chiếu prototype. | |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Với từng trẻ, Centre cần biết phụ huynh đã đồng ý, từ chối hay chưa trả lời từng consent (ví dụ cho phép dùng ảnh của trẻ, cho trẻ đi tham quan), ở phiên bản nào, trả lời ngày nào, qua kênh nào. Từ đó Centre gửi consent cho phụ huynh, gửi lại khi bị từ chối hoặc hết hạn, và nhắc các gia đình chưa trả lời.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách consent của từng trẻ trên hồ sơ trẻ, gồm mọi phiên bản: trạng thái, phiên bản, ngày trả lời, kênh, số lần nhắc. Tạo và gửi consent cho phụ huynh qua Parents App, tuỳ chọn email. Gửi lại consent bị từ chối hoặc hết hạn. Nhắc gia đình chưa trả lời. | Danh sách trẻ còn thiếu consent (Consent compliance). Phát hành phiên bản mới của consent. Phụ huynh rút lại consent. Khảo sát (Survey). Nội dung consent thu lúc nhập học trong registration form (Enrolment). Chặn gắn tên trẻ trong ảnh (Teacher App). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ trong lớp / Centre được cấp. | Xem consent của trẻ; tạo, gửi, gửi lại, nhắc. |
| Consent Viewer | Trẻ trong phạm vi được cấp. | Chỉ xem consent của trẻ. |
| Phụ huynh | Trẻ của mình. | Nhận consent trên Parents App (và email nếu có), trả lời Agree / Decline. |
| System | Consent và câu trả lời. | Gửi thông báo, tự nhắc, chuyển Expired, lưu lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Children & Families** | Danh sách consent của trẻ | Trên hồ sơ trẻ, liệt kê mọi consent của trẻ ở các phiên bản, kèm trạng thái, ngày trả lời, kênh, số lần nhắc. | BBA-71: US-001 |
| **Surveys & consents** | Tạo và gửi consent | Tạo consent, chọn đối tượng nhận và ngày đóng, gửi cho phụ huynh qua Parents App, tuỳ chọn email. | BBA-71: US-002 |
| **Surveys & consents** | Gửi lại và nhắc | Nhắc gia đình chưa trả lời; gửi lại consent cho trẻ bị từ chối hoặc hết hạn. | BBA-71: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-71: US-001 - Danh sách consent của trẻ

#### User Story

Là người dùng của Centre, tôi muốn xem trên hồ sơ trẻ toàn bộ consent của trẻ ở các phiên bản, kèm trạng thái và câu trả lời, để trước mỗi hoạt động tôi biết phụ huynh đã đồng ý hay chưa.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab Documents của hồ sơ trẻ hiển thị danh sách consent của trẻ, mỗi phiên bản một dòng (BR-001, BR-002). |
| FR-002 | Mỗi dòng hiển thị trạng thái, phiên bản, câu trả lời (người trả lời, ngày, kênh) và số lần nhắc (BR-003, BR-004). |
| FR-003 | Từ danh sách, người dùng có quyền mở Surveys & consents để gửi, gửi lại hoặc nhắc (US-002, US-003). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở hồ sơ trẻ, chọn tab Documents (FR-001).
2. Hệ thống hiển thị khu vực Consents: mỗi dòng là một consent ở một phiên bản, kèm trạng thái, câu trả lời và số lần nhắc (FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Open Surveys & consents để gửi, gửi lại hoặc nhắc (FR-003).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa có consent nào: khu vực Consents hiển thị "No consents yet."

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Danh sách gồm mọi consent của trẻ ở mọi phiên bản: phiên bản cũ vẫn hiển thị kèm câu trả lời của phiên bản đó; dòng mới nhất ở trên. |
| BR-002 | Một trẻ có thể có nhiều dòng cùng loại consent, mỗi dòng gắn một sự kiện, ví dụ Field trip "Singapore Zoo" và Field trip "Science Centre". |
| BR-003 | Trạng thái mỗi dòng là một trong: Not sent (chưa gửi), Sent, awaiting parent (đã gửi, chờ phụ huynh), Agreed (đồng ý), Declined (từ chối), Expired (hết hạn). |
| BR-004 | Câu trả lời ghi rõ phụ huynh nào trả lời, ngày giờ trả lời và kênh (Parents App / Registration form). Câu trả lời cũ không bao giờ bị xoá. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| — | — | — |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record — Documents › Consents | Prototype: Children & families › hồ sơ trẻ › Documents |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Consents · n | Tiêu đề khu vực | — | n = số dòng | — | Danh sách consent của trẻ (FR-001). |
| Open Surveys & consents | Nút | Theo quyền | — | — | Mở Communication › Surveys & consents (FR-003). |
| Consent | Cột | — | — | — | Loại consent và sự kiện (nếu có), ví dụ "Field trip · Singapore Zoo" (BR-002). |
| Version | Cột | — | — | — | Phiên bản và tháng phát hành, ví dụ "v3.1 (Jan 2026)" (BR-001). |
| Status | Cột (nhãn) | — | — | — | BR-003. |
| Answered | Cột | — | "—" khi chưa trả lời | — | Người trả lời; ngày trả lời · kênh (BR-004). |
| Reminders | Cột | — | 0 | — | Số lần đã nhắc và ngày nhắc gần nhất (US-003). |
| Closing date | Cột | — | "—" khi không có hạn | — | DD/MM/YYYY. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi câu trả lời lưu: consent, phiên bản, trẻ, phụ huynh trả lời, câu trả lời (Agree / Decline), ngày giờ, kênh. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Mia có PDPA data sharing v3.1 Agreed ngày 06/01/2026 và Outings and excursions v1.4 đã gửi, chưa trả lời | người dùng mở tab Documents của Mia | khu vực Consents có 2 dòng: PDPA data sharing · v3.1 · Agreed · 06/01/2026; Outings and excursions · v1.4 · Sent, awaiting parent · "—" | FR-001; FR-002; BR-003 |
| AC-002 | Ethan đã Agreed Media release v1.0, sau đó được gửi và Agreed Media release v2.0 | người dùng mở tab Documents của Ethan | có 2 dòng Media release (v2.0 ở trên, v1.0 ở dưới), mỗi dòng có câu trả lời của phiên bản đó | FR-001; BR-001 |
| AC-003 | mẹ của Ethan đồng ý Field trip "Singapore Zoo" trong Parents App ngày 20/11/2026 | người dùng mở tab Documents của Ethan | dòng hiện Agreed, tên người mẹ, ngày 20/11/2026, kênh Parents App | FR-002; BR-004; DATA-001 |
| AC-004 | Ethan có Field trip "Singapore Zoo" và Field trip "Science Centre" | người dùng mở tab Documents của Ethan | có 2 dòng Field trip, mỗi dòng gắn một sự kiện | FR-001; BR-002 |
| AC-005 | Teacher chỉ có quyền xem consent | Teacher mở tab Documents của trẻ lớp mình | thấy danh sách consent, không có nút Open Surveys & consents | FR-003 |

#### Dependencies (Phụ thuộc)

Hồ sơ trẻ (tab Documents); câu trả lời của phụ huynh từ Parents App và registration form.

### 6.2 BBA-71: US-002 - Tạo và gửi consent

#### User Story

Là Centre Director, tôi muốn tạo consent và gửi cho phụ huynh của các lớp hoặc cả Centre, để thu sự đồng ý trước một hoạt động.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Người dùng có quyền tạo consent ở Communication › Surveys & consents (BR-005). |
| FR-005 | Người dùng gửi consent cho phụ huynh của các lớp hoặc cả Centre qua Parents App, tuỳ chọn gửi thêm email (BR-006, BR-007). |
| FR-006 | Tab Consents ở Surveys & consents liệt kê các consent đã gửi, kèm số gia đình đã trả lời; mở một consent để xem ai đã trả lời và ai chưa (BR-008). |

#### Functional Flow - Main (Luồng chính)

1. Centre Director chọn New consent, nhập loại, tên sự kiện, nội dung, chọn Centre, lớp, ngày đóng (FR-004; VAL-001).
2. Centre Director chọn Send; phụ huynh của các trẻ được chọn nhận consent trên Parents App; mỗi trẻ có dòng Sent, awaiting parent (FR-005; BR-006).
3. Phụ huynh trả lời Agree / Decline; câu trả lời hiện ở hồ sơ trẻ (US-001) và ở consent (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Centre Director bật Also send by email: phụ huynh nhận thêm email (FR-005; BR-007).
2. Consent chưa có ai trả lời: Centre Director sửa được nội dung; đã có người trả lời thì không sửa được (BR-005).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thiếu ngày đóng, tiêu đề hoặc nội dung: không gửi (VAL-001).
2. Trẻ không có phụ huynh nào nhận được consent: không gửi cho trẻ đó (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Consent chỉ sửa được khi chưa có phụ huynh nào trả lời. |
| BR-006 | Người nhận consent của trẻ theo cấu hình lúc nhập học: "Both parents" (mặc định) hoặc "Primary contact only". |
| BR-007 | Consent luôn gửi qua Parents App; email chỉ gửi khi người tạo bật Also send by email. |
| BR-008 | Một consent đã gửi hiển thị: số gia đình đã trả lời trên tổng số (ví dụ "1 of 6"), danh sách đã trả lời (tên phụ huynh, câu trả lời, ngày giờ) và danh sách chưa trả lời (tên trẻ, các phụ huynh nhận). |
| BR-009 | Consent Field trip và Ad hoc: dòng chưa trả lời chuyển Expired khi qua ngày đóng. Crossroad: Agreed có hiệu lực tới hết năm học, đầu năm sau chuyển Expired. Consent thu lúc nhập học (Privacy policy, Medical authorisation, Media release) không hết hạn. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Để trống tiêu đề, nội dung hoặc ngày đóng; ngày đóng trước hôm nay. | Không gửi; báo lỗi tại trường. |
| VAL-002 | Trẻ không có phụ huynh nào có tài khoản Parents App và người tạo không bật email. | Không gửi cho trẻ đó; dòng của trẻ hiện "No guardian of this child can receive this." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Surveys & consents — tab Consents | Prototype: Communication › Surveys & consents › Consents |
| New consent (popup) | Prototype: New consent |
| Consent detail (popup) | Prototype: bấm một consent trong danh sách |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| **Danh sách consent** | | | | | |
| New consent | Nút | Theo quyền | — | — | Mở popup New consent. |
| Tìm kiếm; Status, Centre, Class | Ô tìm kiếm; bộ lọc | Không | Tất cả | — | Lọc danh sách. |
| Title, Audience, Deadline, Responses, Status | Cột | — | — | — | Responses dạng "x of y"; Status Open / Closed (FR-006). |
| **New consent** | | | | | |
| Type | Danh sách chọn | Có | — | — | Loại consent: Media release, Field trip / learning journey, Medical authorisation, Ad hoc… |
| Title | Ô nhập | Có | Trống | VAL-001. | Tên consent / sự kiện. |
| Consent text | Ô nhập nhiều dòng | Có | Trống | VAL-001. | Nội dung phụ huynh đọc; phụ huynh trả lời Agree hoặc Decline. |
| Centre, Level, Class | Danh sách chọn | Centre: Có | Level, Class: tất cả | — | Đối tượng nhận. |
| Deadline | Chọn ngày | Có | Trống | VAL-001. | Ngày đóng (BR-009). |
| Also send by email | Công tắc | Không | Tắt | — | BR-007. |
| Cancel / Send | Nút | — | — | VAL-001; VAL-002. | Huỷ hoặc gửi (FR-005). |
| **Consent detail** | | | | | |
| Phần đầu | Display | — | — | — | Tên, Centre, ngày đóng, "x of y answered", trạng thái. |
| Results | Section | — | — | — | Câu hỏi và số câu trả lời theo từng lựa chọn. |
| Answered · n | Danh sách | — | — | — | Tên phụ huynh, câu trả lời, ngày giờ (BR-008). |
| Not answered · n | Danh sách | — | — | — | Tên trẻ và các phụ huynh nhận (BR-008). |
| Edit | Nút | Theo quyền | Tắt khi đã có người trả lời | — | Sửa consent (BR-005). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi consent lưu: loại, tiêu đề, nội dung, phiên bản, Centre, lớp nhận, ngày đóng, có gửi email hay không, người tạo, thời điểm gửi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-006 | Centre Director tạo Field trip "Singapore Zoo" cho lớp Sunbeams, ngày đóng 26/11/2026 | chọn Send | phụ huynh lớp Sunbeams nhận consent trên Parents App; mỗi trẻ lớp Sunbeams có dòng "Field trip · Singapore Zoo" Sent, awaiting parent | FR-004; FR-005; BR-006 |
| AC-007 | người tạo bật Also send by email | gửi consent | phụ huynh nhận cả trên Parents App và email | FR-005; BR-007 |
| AC-008 | consent gửi cho 6 trẻ, 1 gia đình đã trả lời | Centre Director mở consent | phần đầu hiện "1 of 6 answered"; danh sách Answered có 1 gia đình, Not answered có 5 trẻ kèm phụ huynh nhận | FR-006; BR-008 |
| AC-009 | consent đã có 1 phụ huynh trả lời | Centre Director mở consent | nút Edit bị tắt | BR-005 |
| AC-010 | Mia cấu hình "Primary contact only" | consent được gửi cho lớp của Mia | chỉ người liên hệ chính của Mia nhận | BR-006 |
| AC-011 | Centre Director không chọn ngày đóng | chọn Send | không gửi, báo lỗi tại Deadline | VAL-001 |
| AC-012 | trẻ không có phụ huynh nào có Parents App, người tạo không bật email | Centre Director gửi consent cho lớp | dòng của trẻ hiện "No guardian of this child can receive this." | VAL-002 |
| AC-013 | Field trip của Noah Sent, awaiting parent, ngày đóng 26/11/2026 | qua ngày 26/11/2026 | dòng của Noah chuyển Expired | BR-009 |

#### Dependencies (Phụ thuộc)

Parents App (nhận và trả lời consent); dịch vụ notification và email; cấu hình người nhận của trẻ.

### 6.3 BBA-71: US-003 - Gửi lại và nhắc

#### User Story

Là Centre Director, tôi muốn nhắc các gia đình chưa trả lời và gửi lại consent cho trẻ bị từ chối hoặc hết hạn, để có đủ sự đồng ý trước hoạt động.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-007 | Người dùng có quyền gửi nhắc cho phụ huynh của các trẻ chưa trả lời một consent (BR-010). |
| FR-008 | Hệ thống tự nhắc phụ huynh chưa trả lời 1 ngày trước ngày đóng (BR-010). |
| FR-009 | Người dùng có quyền gửi lại consent cho trẻ Declined hoặc Expired (BR-011). |
| FR-010 | Hệ thống lưu mỗi lần gửi, nhắc, gửi lại kèm ngày giờ, người thực hiện và số phụ huynh nhận (DATA-003). |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở consent ở Surveys & consents, chọn Send reminder (FR-007).
2. Hệ thống gửi nhắc cho phụ huynh của các trẻ chưa trả lời, báo "Reminder sent to n parents.", tăng số lần nhắc của từng trẻ và ghi lịch sử (FR-007, FR-010; BR-010).

#### Functional Flow - Alternative (Luồng thay thế)

1. Còn 1 ngày tới ngày đóng: hệ thống tự nhắc (FR-008).
2. Trẻ Declined hoặc Expired: Centre Director chọn Send again cho trẻ đó; trẻ có dòng mới Sent, awaiting parent, câu trả lời cũ giữ nguyên (FR-009; BR-011).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Đã nhắc trong ngày: không nhắc thêm (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-010 | Nhắc chỉ gửi cho phụ huynh của trẻ chưa trả lời; mỗi consent nhắc tối đa một lần mỗi ngày, gồm cả lần tự nhắc. Mỗi lần nhắc tăng số lần nhắc của trẻ và cập nhật ngày nhắc gần nhất. |
| BR-011 | Gửi lại chỉ cho trẻ Declined hoặc Expired; tạo lần gửi mới cho trẻ đó, câu trả lời cũ vẫn lưu trong lịch sử. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Consent đã được nhắc trong ngày. | Nút Send reminder tắt; hiện "Last reminder DD/MM/YYYY · at most once a day". |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Consent detail (popup) | Prototype: Send reminder trong popup consent |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Send reminder | Nút | Theo quyền | Tắt khi đã nhắc trong ngày | VAL-003. | Nhắc phụ huynh của trẻ chưa trả lời (FR-007). |
| Last reminder | Display | — | Hiện sau lần nhắc đầu | — | "Last reminder DD/MM/YYYY · at most once a day". |
| Send again | Nút trên dòng trẻ | Theo quyền | Chỉ hiện với trẻ Declined / Expired | — | Gửi lại cho trẻ đó (FR-009). |
| Lịch sử | Danh sách | — | — | — | Mỗi dòng: ngày giờ, người thực hiện, vai trò, thao tác, số phụ huynh nhận, ví dụ "Reminder sent to 9" (FR-010). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi lần gửi, nhắc, gửi lại lưu: consent, thao tác, người thực hiện (hoặc System khi tự nhắc), ngày giờ, các trẻ và số phụ huynh nhận. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-014 | consent có 6 trẻ chưa trả lời, tổng 9 phụ huynh nhận | Centre Director chọn Send reminder | hiện "Reminder sent to 9 parents."; lịch sử có dòng "Reminder sent to 9"; số lần nhắc của 6 trẻ tăng 1 | FR-007; FR-010; BR-010 |
| AC-015 | consent đã được nhắc hôm nay | Centre Director mở consent | nút Send reminder tắt, hiện "Last reminder" kèm ngày hôm nay | VAL-003; BR-010 |
| AC-016 | Field trip đóng ngày 26/11/2026, Noah chưa trả lời | ngày 25/11/2026 | hệ thống tự nhắc phụ huynh của Noah; lịch sử ghi người thực hiện System | FR-008; DATA-003 |
| AC-017 | Field trip của Noah Expired | Centre Director chọn Send again cho Noah | hồ sơ Noah có dòng mới Sent, awaiting parent; dòng Expired cũ vẫn còn | FR-009; BR-011 |
| AC-018 | Ethan đã Agreed | Centre Director mở consent | dòng của Ethan không có Send again | BR-011 |

#### Dependencies (Phụ thuộc)

US-002; dịch vụ notification.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Consent gửi sau (Field trip, Ad hoc) cần một hay cả hai phụ huynh đồng ý? Form đăng ký cần 2 chữ ký. | Business Owner | Cao | |
| OQ-02 | File "Consent Types" (BBA-488) có "Accuracy of Information" và "Outing" thu lúc nhập học. "Accuracy of Information" có là một loại consent không? "Outing" thu lúc nhập học khác Field trip theo sự kiện thế nào? | Centre Director / HQ Ops | Trung bình | |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Consent | Sự đồng ý của phụ huynh cho một việc cụ thể, ví dụ cho phép dùng ảnh của trẻ hoặc cho trẻ đi tham quan. |
| Phiên bản (Version) | Lần phát hành nội dung của một consent, ví dụ v3.1 (Jan 2026). |
| Ngày đóng (Deadline) | Hạn trả lời của consent; qua ngày này dòng chưa trả lời của Field trip, Ad hoc chuyển Expired. |
| Nhắc (Reminder) | Thông báo gửi lại cho phụ huynh chưa trả lời, tối đa một lần mỗi ngày cho mỗi consent. |
| Gửi lại (Send again) | Gửi lần mới cho trẻ đã Declined hoặc Expired. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Trạng thái consent | Not sent, Sent, awaiting parent, Agreed, Declined, Expired. | Câu trả lời của phụ huynh và ngày đóng. |
| Loại consent | Privacy policy / PDPA data sharing, Medical authorisation, Media release (thu lúc nhập học); Field trip / learning journey, Ad hoc (theo sự kiện); Crossroad (chỉ Centre Singapore không có sân ngoài trời, gia hạn hằng năm). | File "Consent Types" (BBA-488). |
| Kênh trả lời | Parents App, Registration form. | — |
