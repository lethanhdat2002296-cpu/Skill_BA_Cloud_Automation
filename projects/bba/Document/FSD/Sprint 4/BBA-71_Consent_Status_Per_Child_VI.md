# Consent Status per Child and Send Consent Request

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Documents & consents |
| Tính năng | BBA-71 Consent status per child & send consent request |
| Mã tài liệu | FRD-3.1.4.01_Consent_Status_Per_Child |
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
| 0.1 | 10/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Với từng trẻ, Centre cần biết phụ huynh đã đồng ý, từ chối hay chưa trả lời từng consent (ví dụ cho phép dùng ảnh của trẻ, cho trẻ đi tham quan), ở phiên bản nào, trả lời ngày nào, qua kênh nào. Từ đó Centre gửi consent cho phụ huynh, gửi lại khi bị hết hạn và nhắc các gia đình chưa trả lời.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách consent của từng trẻ trên hồ sơ trẻ, gồm mọi phiên bản: trạng thái, phiên bản, ngày trả lời, kênh, số lần nhắc. Tạo và gửi consent cho phụ huynh qua Parents App, tùy chọn email. Gửi lại consent đã hết hạn mà phụ huynh chưa trả lời; không gửi lại consent phụ huynh đã từ chối. Giáo viên xem toàn bộ tab Documents của trẻ, kể cả khi trẻ đã chuyển lớp. Nhắc gia đình chưa trả lời. | Danh sách trẻ còn thiếu consent (Consent compliance). Phát hành phiên bản mới của consent. Phụ huynh rút lại consent. Khảo sát (Survey). Nội dung consent thu lúc nhập học trong registration form (Enrolment). Chặn gắn tên trẻ trong ảnh (Teacher App). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Authorised User | Trẻ trong lớp / Centre được cấp. | Xem consent của trẻ; tạo, gửi, gửi lại, nhắc. |
| Consent Viewer | Trẻ trong phạm vi được cấp. | Chỉ xem consent của trẻ. |
| Teacher | Mọi trẻ, không giới hạn theo lớp đang dạy. | Xem toàn bộ thông tin ở tab Documents của trẻ, kể cả khi trẻ đã chuyển sang lớp khác; không gửi, gửi lại hay nhắc. |
| Phụ huynh | Trẻ của mình. | Nhận consent trên Parents App (và email nếu có), trả lời Agree / Decline. |
| System | Consent và câu trả lời. | Gửi thông báo, tự nhắc, chuyển Expired, lưu lịch sử. |
| Unauthorised User | Ngoài vai trò hoặc phạm vi được cấp. | Không thấy và không thao tác được. |

**Quy tắc chung:** Quyền xem và thao tác theo phân quyền vai trò và phạm vi dữ liệu hiện có (Roles & permissions). Tính năng này không tạo vai trò riêng.

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| **Children & Families** | Danh sách consent của trẻ ở tab Document | Trên hồ sơ trẻ, liệt kê mọi consent của trẻ đã gửi đến phụ huynh; mọi giáo viên xem được, kể cả khi trẻ chuyển lớp. | BBA-71: US-001 |
| **Surveys & consents** | Tạo và gửi consent | Tạo consent, chọn đối tượng nhận và ngày đóng, gửi cho phụ huynh qua Parents App, tùy chọn email. | BBA-71: US-002 |
| **Surveys & consents** | Gửi lại và nhắc | Nhắc gia đình chưa trả lời; gửi lại consent cho trẻ đã hết hạn mà chưa trả lời. | BBA-71: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-71: US-001 - Danh sách consent của trẻ ở tab Document

#### User Story

Là người dùng của Centre, tôi muốn xem trên hồ sơ trẻ toàn bộ consent của trẻ ở các phiên bản, kèm trạng thái và câu trả lời, để trước mỗi hoạt động tôi biết phụ huynh đã đồng ý hay chưa.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Tab Documents của hồ sơ trẻ hiển thị danh sách consent của trẻ (BR-001, BR-002). |
| FR-002 | Mỗi dòng hiển thị trạng thái, phiên bản, câu trả lời (người trả lời, ngày) và số lần nhắc (BR-003). |
| FR-003 | Mọi giáo viên xem được toàn bộ thông tin ở tab Documents của trẻ, kể cả khi trẻ đã chuyển sang lớp khác (BR-004). |
| FR-004 | Từ danh sách, người dùng có quyền mở Surveys & consents để gửi, gửi lại hoặc nhắc (US-002, US-003). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở hồ sơ trẻ, chọn tab Documents (FR-001).
2. Hệ thống hiển thị khu vực Consents: mỗi dòng là một consent cần phụ huynh duyệt, kèm trạng thái, câu trả lời và số lần nhắc (FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng chọn Open Surveys & consents để gửi, gửi lại hoặc nhắc (FR-004).
2. Trẻ đã chuyển từ lớp Sunbeams sang lớp Honeycombs: giáo viên lớp Sunbeams vẫn mở được tab Documents của trẻ và xem toàn bộ thông tin, gồm cả consent gửi trước khi trẻ chuyển lớp (FR-003; BR-004).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa có consent nào: khu vực Consents hiển thị "No consent yet."

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Danh sách gồm mọi consent của trẻ. |
| BR-002 | Một trẻ có thể có nhiều dòng cùng loại consent đang mở cùng lúc, mỗi dòng gắn một sự kiện hoặc một chuyến đi (Field trip, Ad hoc). |
| BR-003 | Trạng thái mỗi dòng là một trong: Not sent (chưa gửi), Sent, awaiting parent (đã gửi, chờ phụ huynh), Agreed (đồng ý), Declined (từ chối), Expired (hết hạn). |
| BR-004 | Quyền xem tab Documents của trẻ (tài liệu và khu vực Consents) không phụ thuộc lớp hiện tại của trẻ: mọi giáo viên đều xem được toàn bộ thông tin, kể cả giáo viên lớp cũ sau khi trẻ chuyển lớp và giáo viên không dạy lớp của trẻ. Lịch sử consent của trẻ đi theo trẻ, không gắn với lớp. Giáo viên chỉ xem, không gửi, gửi lại hay nhắc. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| Child record — Documents › Consents | Prototype: Children & families › hồ sơ trẻ › Documents |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Consents · n | Tiêu đề khu vực | — | n = số dòng | — | Danh sách consent của trẻ (FR-001). |
| Open Surveys & consents | Nút | Theo quyền | — | — | Mở Communication › Surveys & consents (FR-004). |
| Consent | Cột | — | — | — | Loại consent và sự kiện (nếu có), ví dụ "Field trip · Singapore Zoo" (BR-002). |
| Version | Cột | — | — | — | Phiên bản và tháng phát hành, ví dụ "v3.1 (Jan 2026)" (BR-001). |
| Status | Cột (nhãn) | — | — | — | BR-003. |
| Answered | Cột | — | "—" khi chưa trả lời | — | Người trả lời; ngày trả lời (FR-002). |
| Reminders | Cột | — | 0 | — | Số lần đã nhắc và ngày nhắc gần nhất (US-003). |
| Closing date | Cột | — | "—" khi không có hạn | — | DD/MM/YYYY. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi câu trả lời lưu: consent, phiên bản nội dung phụ huynh đã trả lời, trẻ, phụ huynh trả lời, câu trả lời (Agree / Decline), thời điểm trả lời, kênh. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Mia có PDPA data sharing v3.1 Agreed ngày 06/01/2026 và Outings and excursions v1.4 đã gửi, chưa trả lời | người dùng mở tab Documents của Mia | khu vực Consents có 2 dòng: PDPA data sharing · v3.1 · Agreed · 06/01/2026; Outings and excursions · v1.4 · Sent, awaiting parent · "—" | FR-001; FR-002; BR-003 |
| AC-002 | Ethan đã Agreed Media release v1.0, sau đó được gửi và Agreed Media release v2.0 | người dùng mở tab Documents của Ethan | có 2 dòng Media release (v2.0 ở trên, v1.0 ở dưới), mỗi dòng có câu trả lời của phiên bản đó | FR-001; BR-001 |
| AC-003 | mẹ của Ethan đồng ý Field trip "Singapore Zoo" trong Parents App ngày 20/11/2026 | người dùng mở tab Documents của Ethan | dòng hiện Agreed, tên người mẹ, ngày 20/11/2026 | FR-002; DATA-001 |
| AC-004 | Ethan có Field trip "Singapore Zoo" và Field trip "Science Centre" | người dùng mở tab Documents của Ethan | có 2 dòng Field trip, mỗi dòng gắn một sự kiện | FR-001; BR-002 |
| AC-005 | Teacher chỉ có quyền xem consent | Teacher mở tab Documents của trẻ lớp mình | thấy danh sách consent, không có nút Open Surveys & consents | FR-004; BR-004 |
| AC-006 | Ethan chuyển từ lớp Sunbeams sang lớp Honeycombs ngày 04/01/2027; trước đó có Media release Agreed và Field trip "Singapore Zoo" Declined | ngày 10/01/2027, giáo viên lớp Sunbeams mở tab Documents của Ethan | thấy toàn bộ tài liệu và cả 2 dòng consent như giáo viên lớp Honeycombs | FR-003; BR-004 |
| AC-007 | giáo viên lớp Bumblebees không dạy Ethan | mở tab Documents của Ethan | thấy toàn bộ tài liệu và consent của Ethan, không có nút gửi, gửi lại, nhắc | FR-003; BR-004 |

#### Dependencies (Phụ thuộc)

Hồ sơ trẻ (tab Documents); câu trả lời của phụ huynh từ Parents App và registration form.

### 6.2 BBA-71: US-002 - Tạo và gửi consent

#### User Story

Là Người dùng, tôi muốn tạo consent và gửi cho phụ huynh.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-005 | Người dùng có quyền tạo consent. |
| FR-006 | Người dùng gửi consent cho phụ huynh theo lớp hoặc cả Centre qua Parents App kèm Announcement, tuỳ chọn gửi thêm email (BR-007, BR-008). |
| FR-007 | Câu trả lời của phụ huynh trong Parents App được ghi về SMS (BR-009). |
| FR-008 | Tab Consents ở Surveys & consents liệt kê các consent đã gửi, kèm số gia đình đã trả lời, có bộ lọc; mở một consent để xem ai đã trả lời và ai chưa (BR-010, BR-011). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng chọn New consent, nhập loại, tên sự kiện, nội dung, chọn Centre, lớp, ngày đóng (FR-005; VAL-001).
2. Người dùng chọn Send; hệ thống tạo Announcement kèm link tới consent; phụ huynh của các trẻ nhận thông báo trong Parents App; mỗi trẻ có dòng consent hiển thị ở hồ sơ trẻ (FR-006; BR-007, BR-008).
3. Phụ huynh trả lời Agree / Decline trong Parents App; câu trả lời về SMS, hiện ở hồ sơ trẻ (US-001) và ở chi tiết consent, mục Consent trong checklist học sinh được tự tick (FR-007, FR-008; BR-009).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người dùng bật Also send by email: phụ huynh nhận thêm email (FR-006).
2. Consent chưa có ai trả lời: Người dùng sửa được nội dung; đã có người trả lời thì không sửa được (BR-005).
3. Người dùng bấm thẻ "x of y families answered": danh sách chỉ còn các trẻ chưa trả lời để Centre đi nhắc (FR-008; BR-011).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Thiếu ngày đóng, tiêu đề hoặc nội dung: không gửi (VAL-001).
2. Trẻ không có phụ huynh nào nhận được consent: không hiển thị consent tại hồ sơ trẻ cho trẻ đó (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Consent chỉ sửa được khi chưa có phụ huynh nào trả lời. |
| BR-006 | Loại consent: Privacy policy, Medical authorisation, Media release thu một lần lúc nhập học cho từng trẻ, trong registration form; nội dung Media release khác nhau theo brand (Learning Vision, The Schoolhouse, Small Wonder mỗi brand một đoạn). Field trip / learning journey theo từng chuyến (cả Malaysia). Ad hoc theo sự kiện (món ăn, hoạt động). Crossroad chỉ có ở Singapore, chỉ cho Centre không có sân ngoài trời. |
| BR-007 | Người tạo chọn đối tượng nhận theo lớp hoặc cả Centre, kèm ngày đóng. Trong mỗi gia đình, consent mặc định gửi cho cả hai phụ huynh; theo cấu hình lúc nhập học, từng trẻ có thể chỉ gửi cho người liên hệ chính. Trường hợp đặc biệt (ví dụ ly hôn) mặc định chỉ một người nhận, giáo viên vẫn thêm được người kia. |
| BR-008 | Gửi consent luôn tạo Announcement kèm link tới consent; thông báo trong Parents App thuộc nhóm "Surveys + Consents". Email chỉ gửi khi người tạo chọn; còn lại chỉ qua app. |
| BR-009 | Phụ huynh trả lời consent trong Parents App; kết quả đổ về SMS và tự tick mục Consent trong checklist học sinh. |
| BR-010 | Ở Surveys & consents, giáo viên chỉ thấy consent của lớp mình; Centre Director thấy consent của mọi lớp. |
| BR-011 | Một consent đã gửi hiển thị: thẻ tổng quan số gia đình đã trả lời trên tổng số (ví dụ "1 of 6 families answered"), danh sách đã trả lời (tên phụ huynh, câu trả lời, ngày giờ) và danh sách chưa trả lời (tên trẻ, các phụ huynh nhận). Bấm thẻ tổng quan thì chỉ hiện các trẻ chưa trả lời. |
| BR-012 | Consent Field trip và Ad hoc: dòng chưa trả lời chuyển Expired khi qua ngày đóng. Crossroad: gia hạn hằng năm; Agreed có hiệu lực tới hết năm học (năm học từ tháng 1 đến tháng 12), đầu năm học sau chuyển Expired và hệ thống nhắc gia hạn. Consent thu lúc nhập học (Privacy policy, Medical authorisation, Media release) một lần, không hết hạn; Centre có thể hỏi thêm Media release theo sự kiện marketing bằng consent Ad hoc. |

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
| **Danh sách consent** |  |  |  |  |  |
| New consent | Nút | Theo quyền | — | — | Mở popup New consent. |
| Tìm kiếm; Status, Centre, Class | Ô tìm kiếm; bộ lọc | Không | Tất cả | — | Lọc danh sách; giáo viên chỉ thấy lớp mình (BR-010). |
| Title, Audience, Deadline, Responses, Status | Cột | — | — | — | Responses dạng "x of y"; Status Open / Closed (FR-008). |
| **New consent** |  |  |  |  |  |
| Type | Danh sách chọn | Có | — | — | Loại consent theo BR-006; Crossroad chỉ hiện ở Centre Singapore không có sân ngoài trời. |
| Title | Ô nhập | Có | Trống | VAL-001. | Tên consent / sự kiện. |
| Consent text | Ô nhập nhiều dòng | Có | Trống | VAL-001. | Nội dung phụ huynh đọc; phụ huynh trả lời Agree hoặc Decline. |
| Centre, Level, Class | Danh sách chọn | Centre: Có | Level, Class: tất cả | — | Đối tượng nhận: theo lớp hoặc cả Centre (BR-007). |
| Deadline | Chọn ngày | Có | Trống | VAL-001. | Ngày đóng (BR-012). |
| Also send by email | Công tắc | Không | Tắt | — | Gửi thêm email (BR-008). |
| Cancel / Send | Nút | — | — | VAL-001; VAL-002. | Huỷ hoặc gửi (FR-006). |
| **Consent detail** |  |  |  |  |  |
| Phần đầu | Display | — | — | — | Tên, Centre, ngày đóng, thẻ "x of y families answered" (bấm để chỉ xem trẻ chưa trả lời), trạng thái (BR-011). |
| Results | Section | — | — | — | Câu hỏi và số câu trả lời theo từng lựa chọn. |
| Answered · n | Danh sách | — | — | — | Tên phụ huynh, câu trả lời, ngày giờ (BR-011). |
| Not answered · n | Danh sách | — | — | — | Tên trẻ và các phụ huynh nhận (BR-011). |
| Edit | Nút | Theo quyền | Tắt khi đã có người trả lời | — | Sửa consent (BR-005). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Mỗi consent lưu: loại, tiêu đề, nội dung, phiên bản, Centre, lớp nhận, ngày đóng, có gửi email hay không, người tạo, thời điểm gửi. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-008 | Người dùng tạo Field trip "Singapore Zoo" cho lớp Sunbeams, ngày đóng 26/11/2026 | chọn Send | hệ thống tạo Announcement kèm link; phụ huynh lớp Sunbeams nhận thông báo nhóm "Surveys + Consents" trên Parents App; mỗi trẻ lớp Sunbeams có dòng "Field trip · Singapore Zoo" Sent, awaiting parent | FR-005; FR-006; BR-008 |
| AC-009 | người tạo bật Also send by email | gửi consent | phụ huynh nhận cả trên Parents App và email | FR-006; BR-008 |
| AC-010 | người tạo không bật Also send by email | gửi consent | phụ huynh chỉ nhận trên Parents App, không có email | BR-008 |
| AC-011 | Mia cấu hình lúc nhập học "Primary contact only" | consent được gửi cho lớp của Mia | chỉ người liên hệ chính của Mia nhận | BR-007 |
| AC-012 | Ethan không cấu hình riêng | consent được gửi cho lớp của Ethan | cả hai phụ huynh của Ethan nhận | BR-007 |
| AC-013 | mẹ của Ethan đồng ý Field trip trong Parents App | câu trả lời được gửi | câu trả lời có trong SMS; mục Consent trong checklist học sinh của Ethan được tick | FR-007; BR-009 |
| AC-014 | Centre Malaysia | Người dùng mở New consent | danh sách Type không có Crossroad | BR-006 |
| AC-015 | giáo viên lớp Sunbeams; có consent gửi cho lớp Sunbeams và lớp Honeycombs | giáo viên mở Surveys & consents › Consents | chỉ thấy consent của lớp Sunbeams; Centre Director thấy cả hai | FR-008; BR-010 |
| AC-016 | consent gửi cho 6 trẻ, 1 gia đình đã trả lời | Người dùng mở consent | phần đầu hiện "1 of 6 families answered"; danh sách Answered có 1 gia đình, Not answered có 5 trẻ kèm phụ huynh nhận | FR-008; BR-011 |
| AC-017 | consent gửi cho 6 trẻ, 1 gia đình đã trả lời | Người dùng bấm thẻ "1 of 6 families answered" | danh sách chỉ còn 5 trẻ chưa trả lời | FR-008; BR-011 |
| AC-018 | consent đã có 1 phụ huynh trả lời | Người dùng mở consent | nút Edit bị tắt | BR-005 |
| AC-019 | Người dùng không chọn ngày đóng | chọn Send | không gửi, báo lỗi tại Deadline | VAL-001 |
| AC-020 | trẻ không có phụ huynh nào có Parents App, người tạo không bật email | Người dùng gửi consent cho lớp | dòng của trẻ hiện "No guardian of this child can receive this." | VAL-002 |
| AC-021 | Field trip của Noah Sent, awaiting parent, ngày đóng 26/11/2026 | qua ngày 26/11/2026 | dòng của Noah chuyển Expired | BR-012 |
| AC-022 | Crossroad của Chloe Agreed năm học 2026 | sang 01/01/2027 | dòng Crossroad của Chloe chuyển Expired; hệ thống nhắc gia hạn | BR-012 |

#### Dependencies (Phụ thuộc)

Parents App (nhận và trả lời consent); Announcements; dịch vụ notification và email; cấu hình người nhận của trẻ lúc nhập học; checklist học sinh; thông tin Centre (có sân ngoài trời hay không).

### 6.3 BBA-71: US-003 - Gửi lại và nhắc

#### User Story

Là Người dùng, tôi muốn nhắc các gia đình chưa trả lời và gửi lại consent cho phụ huynh khi hết hạn, để có đủ sự đồng ý trước hoạt động.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-009 | Người dùng có quyền gửi nhắc cho phụ huynh của các trẻ chưa trả lời một consent (BR-013). |
| FR-010 | Hệ thống tự nhắc phụ huynh chưa trả lời 1 ngày trước ngày đóng (BR-013). |
| FR-011 | Người dùng có quyền gửi lại consent cho trẻ Expired (BR-014). |
| FR-012 | Hệ thống lưu mỗi lần gửi, nhắc, gửi lại kèm ngày giờ, người thực hiện và số phụ huynh nhận (DATA-003). |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở consent ở Surveys & consents, chọn Send reminder (FR-009).
2. Hệ thống gửi nhắc cho phụ huynh của các trẻ chưa trả lời, báo "Reminder sent to n parents.", tăng số lần nhắc của từng trẻ và ghi lịch sử (FR-009, FR-012; BR-013).

#### Functional Flow - Alternative (Luồng thay thế)

1. Còn 1 ngày tới ngày đóng: hệ thống tự nhắc các phụ huynh chưa trả lời (FR-010).
2. Trẻ Expired: Người dùng chọn Send again cho trẻ đó; trẻ có dòng mới Sent, awaiting parent (FR-011; BR-014).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Đã nhắc trong ngày: không nhắc thêm (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-013 | Nhắc chỉ gửi cho phụ huynh của trẻ chưa trả lời; mỗi consent nhắc tối đa một lần mỗi ngày, gồm cả lần tự nhắc. Mỗi lần nhắc tăng số lần nhắc của trẻ và cập nhật ngày nhắc gần nhất. |
| BR-014 | Chỉ gửi lại khi consent hết hạn (Expired) mà phụ huynh chưa trả lời; tạo lần gửi mới cho trẻ đó, dòng Expired cũ vẫn giữ. Consent phụ huynh đã từ chối (Declined) không được gửi lại. |

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
| Send reminder | Nút | Theo quyền | Tắt khi đã nhắc trong ngày | VAL-003. | Nhắc phụ huynh của trẻ chưa trả lời (FR-009). |
| Last reminder | Display | — | Hiện sau lần nhắc đầu | — | "Last reminder DD/MM/YYYY · at most once a day". |
| Send again | Nút trên dòng trẻ | Theo quyền | Chỉ hiện với trẻ Expired | — | Gửi lại cho trẻ đó (FR-011; BR-014). |
| Lịch sử | Danh sách | — | — | — | Mỗi dòng: ngày giờ, người thực hiện, vai trò, thao tác, số phụ huynh nhận, ví dụ "Reminder sent to 9" (FR-012). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Mỗi lần gửi, nhắc, gửi lại lưu: consent, thao tác, người thực hiện (hoặc System khi tự nhắc), ngày giờ, các trẻ và số phụ huynh nhận. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-023 | consent có 6 trẻ chưa trả lời, tổng 9 phụ huynh nhận | Người dùng chọn Send reminder | hiện "Reminder sent to 9 parents."; lịch sử có dòng "Reminder sent to 9"; số lần nhắc của 6 trẻ tăng 1 | FR-009; FR-012; BR-013 |
| AC-024 | consent đã được nhắc hôm nay | Người dùng mở consent | nút Send reminder tắt, hiện "Last reminder" kèm ngày hôm nay | VAL-003; BR-013 |
| AC-025 | Field trip đóng ngày 26/11/2026, Noah chưa trả lời | ngày 25/11/2026 | hệ thống tự nhắc phụ huynh của Noah; lịch sử ghi người thực hiện System | FR-010; DATA-003 |
| AC-026 | Field trip của Noah Expired | Người dùng chọn Send again cho Noah | hồ sơ Noah có dòng mới Sent, awaiting parent; dòng Expired cũ vẫn còn | FR-011; BR-014 |
| AC-027 | Ethan đã Agreed | Người dùng mở consent | dòng của Ethan không có Send again | BR-014 |
| AC-028 | mẹ của Noah đã Decline Field trip "Singapore Zoo" | Người dùng mở consent | dòng của Noah không có Send again; consent không được gửi lại cho Noah | FR-011; BR-014 |

#### Dependencies (Phụ thuộc)

US-002; dịch vụ notification.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Consent gửi sau (Field trip, Ad hoc, Crossroad) cần một hay cả hai phụ huynh đồng ý? (Form đăng ký đã chốt bắt buộc 2 chữ ký; nếu chỉ có một người thì người đó ký cả hai ô.) | Business Owner | Cao |  |
| OQ-02 | Nhắc gửi thủ công hay tự động; giới hạn số lần và khoảng cách giữa các lần? Tài liệu đang để: người dùng nhắc tay, hệ thống tự nhắc 1 ngày trước ngày đóng, tối đa 1 lần mỗi ngày. | Centre Director / HQ Ops | Trung bình |  |
| OQ-03 | Khi consent có phiên bản mới, câu trả lời của phiên bản cũ còn hiệu lực hay phụ huynh phải trả lời lại? | Business Owner | Cao |  |
| OQ-04 | Gia hạn Crossroad đầu năm học: hệ thống tự tạo yêu cầu gia hạn hay Centre tạo tay? | Centre Director / HQ Ops | Trung bình |  |
| OQ-05 | File "Consent Types" (BBA-488) có "Accuracy of Information" và "Outing" thu lúc nhập học. "Accuracy of Information" có là một loại consent không? "Outing" thu lúc nhập học khác Field trip theo sự kiện thế nào? | Centre Director / HQ Ops | Trung bình |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Consent | Sự đồng ý của phụ huynh cho một việc cụ thể, ví dụ cho phép dùng ảnh của trẻ hoặc cho trẻ đi tham quan. |
| Phiên bản (Version) | Lần phát hành nội dung của một consent, ví dụ v3.1 (Jan 2026). |
| Ngày đóng (Deadline) | Hạn trả lời của consent; qua ngày này dòng chưa trả lời của Field trip, Ad hoc chuyển Expired. |
| Nhắc (Reminder) | Thông báo gửi lại cho phụ huynh chưa trả lời, tối đa một lần mỗi ngày cho mỗi consent. |
| Gửi lại (Send again) | Gửi lần mới cho trẻ có consent đã hết hạn mà chưa trả lời; không áp dụng cho consent đã bị từ chối. |

### Phụ lục B. Danh mục

| Danh mục | Mô tả | Phụ thuộc vào |
|---|---|---|
| Trạng thái consent | Not sent, Sent, awaiting parent, Agreed, Declined, Expired. | Câu trả lời của phụ huynh và ngày đóng. |
| Loại consent | Privacy policy / PDPA data sharing, Medical authorisation, Media release (thu lúc nhập học); Field trip / learning journey, Ad hoc (theo sự kiện); Crossroad (chỉ Centre Singapore không có sân ngoài trời, gia hạn hằng năm). | File "Consent Types" (BBA-488). |
| Kênh trả lời | Parents App, Registration form. | — |
