# [Nháp] BBA-71 Consent status per child & send consent request — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + **file câu hỏi phản hồi BBA_SMS_S4 (Q-73-04 đến Q-73-15)** + Plane BBA-488, BBA-492 + SRS Children & Families, Parents App, Daily Operations, Teacher App + prototype SMS (Safety overview › Consent compliance).
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-71/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. **Gửi consent:** Centre Director tạo consent ở Surveys & consents và gửi theo **lớp hoặc cả Centre**, có ngày đóng (Q-73-04); tạo consent luôn kèm **Announcement có link** (Q-73-08). Email chỉ gửi khi người tạo chọn — **bỏ** "tự gửi email cho phụ huynh chưa có app".
2. **Loại và vòng đời** (Q-73-04, Q-73-12):
   - Privacy policy, Medical authorisation, Media release: thu **một lần lúc nhập học** (trong registration form), theo từng trẻ, **không hết hạn**. Nội dung Media release khác nhau theo brand.
   - Field trip / learning journey, Ad hoc: **theo từng chuyến / sự kiện**, có ngày đóng.
   - Crossroad: **chỉ Singapore**, chỉ Centre không có sân ngoài trời, **gia hạn hằng năm** đầu năm học (tháng 1).
3. Một trẻ có **nhiều consent đang mở cùng loại**, mỗi cái gắn một sự kiện (Q-73-14).
4. Người nhận: mặc định **cả hai phụ huynh**; mỗi trẻ cấu hình "cả hai" hoặc "chỉ người liên hệ chính" (Q-73-07).
5. Trả lời trong app → **tự tick mục Consent trong checklist học sinh** (Q-73-08).
6. Thẻ tổng quan "đã trả lời / tổng", bấm vào chỉ hiện người chưa trả lời; có bộ lọc consent (mong muốn của BBA, DOTB thiết kế — Q-73-10).
7. Giữ từ nháp trước: tên trạng thái theo prototype; bảng Consents ở tab Documents; tuỳ chọn yêu cầu đồng ý lại khi có phiên bản mới (Plane BBA-488); Consent compliance.

---

## US-001 - Trạng thái consent của từng trẻ và gửi yêu cầu

#### User Story

Là Centre Director, tôi muốn gửi consent cho các lớp hoặc cả Centre và xem trạng thái từng consent của mỗi trẻ, để trước mỗi hoạt động (chụp ảnh, dã ngoại) tôi biết chắc phụ huynh đã đồng ý và nhắc được gia đình còn thiếu.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(sửa)* | Tab Documents của hồ sơ trẻ có bảng "Consents", mỗi dòng một consent của trẻ: loại (Privacy policy, Medical authorisation, Media release, Field trip / learning journey, Ad hoc, Crossroad), tên sự kiện / chuyến đi (với loại theo sự kiện), phiên bản, trạng thái, câu trả lời gần nhất (phụ huynh, kênh, ngày giờ) hoặc ngày gửi và số lần nhắc, ngày đóng. Một trẻ có thể có nhiều dòng cùng loại, mỗi dòng gắn một sự kiện (Q-73-14). |
| FR-002 | Trạng thái của mỗi dòng là một trong: Not sent, Waiting on the parent, Agreed, Declined, Withdrawn, Expired. |
| FR-003 *(sửa)* | Centre Director tạo consent ở Communication › Surveys & consents: loại, tên sự kiện (với loại theo sự kiện), nội dung, ngày đóng, đối tượng **theo lớp hoặc cả Centre** (Q-73-04). Khi gửi, hệ thống tạo **Announcement kèm link** tới consent (Q-73-08); email chỉ gửi kèm khi người tạo bật "Also send by email" (Q-73-08). Mỗi trẻ trong đối tượng có dòng trạng thái Waiting on the parent. |
| FR-004 *(sửa — chờ OQ-04)* | "Remind" ở dòng Waiting on the parent (trên hồ sơ trẻ hoặc danh sách người chưa trả lời — FR-012) gửi lại thông báo, tăng số lần nhắc và ghi ngày nhắc. Hệ thống tự nhắc 1 ngày trước ngày đóng (SRS Parents App). |
| FR-005 *(sửa)* | Khi phụ huynh trả lời trong Parents App, hệ thống lưu câu trả lời, chữ ký (nếu form yêu cầu), tên phụ huynh, ngày giờ, kênh, phiên bản; kết quả về SMS và **tự tick mục Consent trong checklist học sinh** (Q-73-08). |
| FR-006 | Khi người có quyền công bố phiên bản mới của một consent, họ chọn "Ask families to agree again" (mọi trẻ về Not sent cho phiên bản mới) hoặc "Keep current answers" (câu trả lời phiên bản trước vẫn dùng). "Summary of changes" là bắt buộc (Plane BBA-488). |
| FR-007 *(sửa)* | Vòng đời theo loại (Q-73-12): Privacy policy, Medical authorisation, Media release — thu một lần lúc nhập học trong registration form, theo từng trẻ, không hết hạn; Field trip / learning journey và Ad hoc — dòng Waiting on the parent chuyển **Expired** khi qua ngày đóng; Crossroad — Agreed có hiệu lực tới hết năm học (tháng 12), đầu năm học sau chuyển Expired và cần gia hạn. |
| FR-008 | "Send again" ở dòng Declined hoặc Expired tạo một yêu cầu mới với ngày đóng mới; câu trả lời cũ giữ trong lịch sử. |
| FR-009 *(sửa)* | Phụ huynh rút lại Media release hoặc consent dữ liệu (khi consent cho phép rút) → dòng chuyển Withdrawn; câu đồng ý ban đầu và việc rút lại đều được giữ; Centre Director và HQ Marketing nhận thông báo (Q-73-13: "Marketing cũng phải biết"). |
| FR-010 | "History" ở một dòng mở lịch sử: mọi lần gửi, nhắc, trả lời, rút lại, đổi phiên bản, kèm ngày giờ và người thực hiện. |
| FR-011 | Màn "Consent compliance" (Daily operations › Safety overview) liệt kê trẻ còn thiếu consent theo Centre: Child, Class, Not sent, Waiting on the parent, Declined or withdrawn; lọc Centre, lớp, loại consent; xuất ra Excel. |
| FR-012 *(mới)* | Danh sách consent ở Surveys & consents có thẻ tổng quan mỗi consent "x of y families answered"; chọn thẻ thì chỉ hiện các trẻ chưa trả lời, kèm Remind; có bộ lọc theo loại, lớp, trạng thái, ngày đóng (Q-73-10 — mong muốn của BBA, DOTB thiết kế). |
| FR-013 *(mới)* | Người nhận consent của một trẻ theo cấu hình lúc nhập học: "Both parents" (mặc định) hoặc "Primary contact only"; trường hợp đặc biệt (vd ly hôn) chọn một người (Q-73-07). |
| FR-014 *(mới)* | Loại Crossroad chỉ chọn được cho Centre Singapore được đánh dấu "không có sân ngoài trời" (Q-73-04); nơi đánh dấu chờ OQ-09. |

#### Functional Flow - Main (Luồng chính)

1. *(sửa)* Centre Director tạo consent (vd Field trip "Singapore Zoo 28/11"), chọn lớp, ngày đóng, gửi; hệ thống tạo Announcement kèm link (FR-003).
2. Phụ huynh trả lời trong Parents App; kết quả về SMS, tick checklist (FR-005).
3. *(sửa)* Centre Director xem thẻ "x of y answered", chọn để thấy trẻ chưa trả lời và nhắc (FR-012, FR-004).
4. Centre Director mở hồ sơ trẻ, tab Documents, xem bảng Consents (FR-001, FR-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. Phụ huynh không đồng ý hoặc consent quá ngày đóng: Centre Director chọn Send again (FR-007, FR-008).
2. Consent có phiên bản mới: người công bố chọn yêu cầu đồng ý lại hoặc giữ câu trả lời (FR-006).
3. Phụ huynh rút lại Media release (FR-009).
4. Đầu năm học: Crossroad của năm trước chuyển Expired, Centre gửi gia hạn (FR-007).
5. Centre Director mở Consent compliance để xem trẻ nào còn thiếu trước một hoạt động (FR-011).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ không có phụ huynh nào có tài khoản Parents App và người tạo không bật email: không gửi được cho trẻ đó (VAL-001).
2. Người dùng không có quyền gửi consent: không có nút gửi (VAL-002).
3. Công bố phiên bản mới không có tóm tắt thay đổi: không lưu (VAL-003).
4. *(mới)* Tạo consent không có ngày đóng (loại theo sự kiện): không gửi được (VAL-004).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Câu trả lời ghi rõ phụ huynh nào trả lời, ngày giờ, kênh và chữ ký khi form yêu cầu. |
| BR-002 | Câu trả lời cho phiên bản cũ chỉ còn dùng cho phiên bản mới khi người công bố chọn "Keep current answers". |
| BR-003 | Câu trả lời cũ và việc rút lại không bao giờ bị xoá. |
| BR-004 *(sửa)* | Centre Director tạo và gửi consent cho các lớp của Centre; Teacher chỉ xem consent của lớp mình (Q-73-04). |
| BR-005 | Trẻ không có Media release đã Agreed không được chụp, đăng hay gắn tên; hệ thống chặn hoặc cảnh báo khi gắn tên trẻ (Q-73-13; SRS BR-TCH-030). |
| BR-006 *(mới)* | Privacy policy, Medical authorisation, Media release thu một lần lúc nhập học theo từng trẻ và không hết hạn; Field trip, Ad hoc theo từng sự kiện; Crossroad gia hạn hằng năm (Q-73-12). |
| BR-007 *(mới)* | Email không gửi mặc định; chỉ gửi khi người tạo chọn (Q-73-08). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 *(sửa)* | Trẻ không có phụ huynh nào có tài khoản Parents App và người tạo không bật email. | Không gửi cho trẻ đó; dòng hiện "No guardian of this child can receive this in the app." |
| VAL-002 | Người dùng không có quyền gửi consent. | Không hiển thị Send, Remind, Send again. |
| VAL-003 | Công bố phiên bản mới mà để trống "Summary of changes". | Không lưu; hiện "Enter a summary of changes." |
| VAL-004 *(mới)* | Consent loại Field trip / Ad hoc / Crossroad không có ngày đóng. | Không gửi; hiện "Choose a closing date." |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Bảng Consents | Bảng ở tab Documents | Có | Mỗi consent một dòng | — | Cột: Consent, Event, Version, Status, Answer / last action, Closing date (FR-001). |
| Remind | Nút | Theo quyền | Dòng Waiting on the parent | VAL-002. | FR-004. |
| Send again | Nút | Theo quyền | Dòng Declined, Expired | VAL-001; VAL-002. | FR-008. |
| History | Liên kết | — | — | — | FR-010. |
| New consent *(mới)* | Form ở Surveys & consents | Theo quyền | — | VAL-004. | Loại, Event, nội dung, Closing date, Audience (lớp / cả Centre), "Also send by email" (tắt) (FR-003). |
| Thẻ "x of y answered" *(mới)* | Thẻ trên danh sách consent | — | — | — | Bấm → chỉ trẻ chưa trả lời (FR-012). |
| Publish new version | Hộp thoại | Theo quyền | "Ask families to agree again" | VAL-003. | FR-006. |
| Consent compliance | Màn danh sách | — | Centre của người dùng | — | FR-011. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 *(sửa)* | Mỗi consent lưu: loại, sự kiện, nội dung, phiên bản, đối tượng (lớp / Centre), ngày đóng, người tạo, có gửi email hay không, Announcement kèm theo. |
| DATA-002 | Mỗi câu trả lời lưu: câu trả lời, chữ ký, phụ huynh, ngày giờ, kênh, phiên bản; việc rút lại lưu thêm ngày giờ rút. |
| DATA-003 | Mỗi phiên bản lưu: số phiên bản, ngày, tóm tắt thay đổi, người công bố, lựa chọn đồng ý lại / giữ câu trả lời. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 *(sửa)* | Centre Director tạo Field trip "Singapore Zoo" cho lớp N2 · Sunbeams, ngày đóng 26/11/2026 | chọn Send | phụ huynh lớp Sunbeams nhận Announcement có link; mỗi trẻ có dòng "Field trip · Singapore Zoo" Waiting on the parent | FR-001; FR-003 |
| AC-002 | dòng đang Waiting on the parent, đã nhắc 1 lần | Centre Director chọn Remind | số lần nhắc là 2 và có ngày nhắc mới | FR-004 |
| AC-003 *(sửa)* | Field trip đóng ngày 26/11 | ngày 25/11 phụ huynh chưa trả lời | hệ thống tự nhắc và số lần nhắc tăng 1 | FR-004 |
| AC-004 *(sửa)* | mẹ của Ethan đồng ý Field trip trong Parents App | Centre Director mở bảng consent | dòng hiện Agreed, tên người mẹ, ngày giờ, kênh Parents App; mục Consent trong checklist học sinh được tick | FR-005; BR-001; DATA-002 |
| AC-005 | Ethan đã Agreed Privacy policy phiên bản 2 | HQ Admin công bố phiên bản 3 và chọn "Ask families to agree again" | dòng Privacy policy của Ethan hiện v3, Not sent; câu trả lời v2 vẫn có trong lịch sử | FR-006; BR-002 |
| AC-006 *(sửa)* | Field trip của Noah Waiting on the parent | qua ngày đóng | dòng chuyển Expired và có nút Send again | FR-007; FR-008 |
| AC-007 *(sửa)* | phụ huynh rút lại Media release | Centre Director mở bảng | dòng hiện Withdrawn; lịch sử có cả câu đồng ý và việc rút lại; Centre Director và HQ Marketing đã nhận thông báo | FR-009; BR-003 |
| AC-008 *(sửa)* | trẻ không có phụ huynh nào có Parents App, người tạo không bật email | Centre Director gửi consent cho lớp | dòng của trẻ hiện "No guardian of this child can receive this in the app." | VAL-001 |
| AC-009 | Teacher mở hồ sơ trẻ lớp mình | xem bảng consent | thấy trạng thái, không có nút gửi | VAL-002; BR-004 |
| AC-010 *(sửa)* | người tạo bật "Also send by email" | gửi consent | phụ huynh nhận cả Announcement trong app và email | FR-003; BR-007 |
| AC-011 | dòng đã có 3 lần gửi và nhắc | Centre Director chọn History | lịch sử hiện đủ 3 lần với ngày giờ, người thực hiện | FR-010 |
| AC-012 | Ethan đã Agreed Media release v2 | HQ Admin công bố v3 (sửa chính tả) và chọn "Keep current answers" | dòng hiện v3, trạng thái Agreed theo câu trả lời v2 | FR-006; BR-002 |
| AC-013 | HQ Admin công bố phiên bản mới, để trống Summary of changes | chọn Publish | không lưu, hiện "Enter a summary of changes." | VAL-003 |
| AC-014 | Noah chưa trả lời Field trip và đã từ chối Media release | Centre Director mở Consent compliance | dòng Noah có Field trip ở cột Waiting on the parent và Media release ở cột Declined or withdrawn | FR-011 |
| AC-015 *(mới)* | Field trip "Singapore Zoo" gửi cho 18 gia đình, 12 đã trả lời | Centre Director chọn thẻ "12 of 18 families answered" | danh sách chỉ còn 6 trẻ chưa trả lời, mỗi dòng có Remind | FR-012 |
| AC-016 *(mới)* | Ethan đang có Field trip "Singapore Zoo" mở | Centre Director gửi tiếp Ad hoc "Cooking day" | hồ sơ Ethan có 2 dòng mở, mỗi dòng gắn một sự kiện | FR-001 |
| AC-017 *(mới)* | Mia cấu hình "Primary contact only" | consent được gửi cho lớp của Mia | chỉ người liên hệ chính của Mia nhận | FR-013 |
| AC-018 *(mới)* | Centre Malaysia | Centre Director tạo consent | không có loại Crossroad | FR-014 |
| AC-019 *(mới)* | Centre Director tạo Field trip không chọn ngày đóng | chọn Send | không gửi, hiện "Choose a closing date." | VAL-004 |
| AC-020 *(mới)* | Noah chưa có Media release ở trạng thái Agreed | giáo viên gắn tên Noah vào một ảnh | không gắn được tên Noah, hiện lý do chưa có Media release | BR-005 |
| AC-021 *(mới)* | Ethan đồng ý Privacy policy, Medical authorisation, Media release trong registration form ngày 05/01/2026 | Centre Director mở tab Consents ngày 13/11/2026 | ba dòng ở trạng thái Agreed, không có ngày đóng, không chuyển Expired | FR-002; FR-007; BR-006 |

#### Dependencies (Phụ thuộc)

Communication › Surveys & consents và Announcements; registration form (consent một lần); checklist học sinh; Parents App; cấu hình người nhận của trẻ; thông tin Centre (không có sân ngoài trời).

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái / Quyết định của BBA |
|---|---|---|
| OQ-01 *(sửa)* | Nội dung từng loại consent (Media release khác theo brand). | Loại đã chốt (Q-73-04); cần file "Consent Types" (BBA-488) để lấy nội dung |
| OQ-02 | "Expired" nghĩa là gì, thời hạn từng loại. | **Đã chốt:** theo vòng đời từng loại (Q-73-12) → FR-007 |
| OQ-03 | Phiên bản mới có cần đồng ý lại không. | **Đã chốt:** tuỳ từng lần (Plane BBA-488) → FR-006 |
| OQ-04 | Nhắc thủ công hay tự động; giới hạn số lần và khoảng cách? | Mở — BBA chưa trả lời (Q-73-09) |
| OQ-05 | Phụ huynh trả lời qua email có cần ký không? | Mở — email giờ chỉ là kênh báo kèm, trả lời vẫn trong app (Q-73-08) |
| OQ-06 | Gửi consent ở đâu. | **Đã chốt:** CD gửi theo lớp / cả Centre (Q-73-04); hồ sơ trẻ chỉ xem, nhắc, gửi lại |
| OQ-07 *(mới)* | Consent gửi sau (Field trip, Ad hoc, Crossroad) cần **một hay cả hai** phụ huynh đồng ý? Form đăng ký đã chốt cần 2 chữ ký. | Mở — cao (Q-73-06) |
| OQ-08 *(mới)* | Gia hạn Crossroad tạo tự động đầu năm học hay Centre tạo tay? | Mở (Q-73-12) |
| OQ-09 *(mới)* | Ai đánh dấu Centre "không có sân ngoài trời" và ở đâu? | Mở |
| AS-01 | Thêm trạng thái Withdrawn. | Theo SRS Parents App BR-PAR-036 |
| AS-02 *(bỏ)* | ~~Phụ huynh chưa có Parents App nhận yêu cầu qua email.~~ | Bỏ — email do người tạo chọn (Q-73-08) |
| AS-03 *(sửa)* | Expired = qua ngày đóng (Field trip, Ad hoc) hoặc hết năm học (Crossroad). | Theo Q-73-12 |
| AS-05 | Bảng Consents nằm ở tab Documents (theo prototype). | Chờ xác nhận |
| — | Bằng chứng lưu (Q-73-15) và cách đếm lần nhắc (Q-73-10): DOTB tự quyết → theo DATA-002, FR-004. | DOTB quyết định |
