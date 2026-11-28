# Lịch sử trao đổi BA — BBA-729 / BBA-145 Child Switcher

Ngày: 28/11/2026 (GMT+7)
Dự án: Busy Bees Asia SMS — Parents App, Account & Home.
Phạm vi lưu: cuộc trao đổi về review scope BBA-729 trong phiên chat này, từ yêu cầu lúc 09:12 đến phần giải thích lúc 10:36.
Định dạng: bản ghi Markdown nội dung trao đổi; các bảng, sơ đồ và demo tương tác được chuyển thành nội dung tĩnh. Không phải bản export nguyên văn toàn bộ giao diện ChatGPT. Vì repository ở chế độ Public, đường dẫn Google Docs nội bộ được lược bỏ. Không bao gồm nội dung ngoài cuộc trao đổi này.

## 01 — Người dùng (09:12)

> Truy cập vào git tên "Skill_BA_Cloud_Automation" 
> 1. Đọc review tài liệu trên
> 2. Check trên doc [đường dẫn Google Docs nội bộ đã lược bỏ] tài liệu này. 
> 3. Đánh giá scope trong BBA729 này xem thử nó đang nằm trong phạm vi như nào nhé.
> 4. Tài liệu này liên quan đến nghiệp vụ không có tech trong nhé. Nên phạm vi đừng đưa tech vào

Tệp đính kèm: BBA-729_Review_BBA-145.md.

## 02 — Trợ lý (09:12) — Review Scope BBA-729 – BBA-145 Child Switcher

### 1. Đánh giá tổng quan

Bản chất chức năng: Cho phép phụ huynh lựa chọn trẻ mà mình muốn theo dõi trên Parents App, đảm bảo thông tin hiển thị đúng trẻ và đúng phạm vi quyền của phụ huynh.

| Thuộc tính | Phạm vi |
|---|---|
| Task BA | BBA-729 |
| Tính năng | BBA-145 – Child Switcher |
| Project | Busy Bees Asia SMS |
| Application | Parents App |
| Module | 4.1 – Account & Home |
| Đối tượng sử dụng | Parent / Guardian |
| Loại nghiệp vụ | Lựa chọn trẻ, kiểm soát phạm vi thông tin được xem |
| Phạm vi tổ chức ghi trong FRS | Cross Brand, Cross Centre, Cross Country |
| Nghiệp vụ phụ thuộc | Children & Families, Child Enrolment, Notifications |

BBA-729 chỉ nên đặc tả những gì phụ huynh được phép thực hiện, điều kiện thực hiện, quy tắc nghiệp vụ và kết quả mong đợi. Không mở rộng sang thiết kế giải pháp kỹ thuật hoặc đặc tả lại các module phụ thuộc.

FRS v0.1: 2 User Stories, 5 FR, 9 BR, 2 Validation Rules, 12 AC. Kết quả review: REVISE. Tài liệu đúng hướng về chức năng chính nhưng chưa đủ chặt chẽ về ranh giới nghiệp vụ và các trường hợp ngoại lệ.

### 2. Đối chiếu Skill BA

Nguồn đã đọc:
- [CLAUDE.md](https://github.com/lethanhdat2002296-cpu/Skill_BA_Cloud_Automation/blob/main/CLAUDE.md)
- [Brainstorm Skill](https://github.com/lethanhdat2002296-cpu/Skill_BA_Cloud_Automation/blob/main/.claude/skills/brainstorm/SKILL.md)
- [URD Skill](https://github.com/lethanhdat2002296-cpu/Skill_BA_Cloud_Automation/blob/main/.claude/skills/write-urd/SKILL.md)
- [SRS Skill](https://github.com/lethanhdat2002296-cpu/Skill_BA_Cloud_Automation/blob/main/.claude/skills/write-srs/SKILL.md)
- [SRS Checklist](https://github.com/lethanhdat2002296-cpu/Skill_BA_Cloud_Automation/blob/main/.claude/skills/write-srs/checklist.md)
- [FRS BBA-145 v0.1](https://github.com/lethanhdat2002296-cpu/Skill_BA_Cloud_Automation/blob/claude/modest-bell-d5dt19/outputs/bba-sms/sprint-5/FRS-BBA-145-child-switcher.md)
- [Children & Families SRS](https://github.com/lethanhdat2002296-cpu/Skill_BA_Cloud_Automation/blob/ccr-dba2efbb-fdrbzc/projects/bba/Document/SRS/BBA-SMS-SRS-Children-and-Families-v0.1.md)
- Google Docs Sprint 5 (đường dẫn nội bộ lược bỏ), bản nháp 26/11/2026.
- Tệp review Markdown đính kèm.

FRS GitHub và Google Docs tương đồng về nghiệp vụ. Chỉ áp dụng nguyên tắc BA, không áp dụng toàn bộ cấu trúc SRS kỹ thuật.

### 3. Ranh giới nghiệp vụ

Children & Families, Joining & Leaving và Enrolment/Class cung cấp thông tin. Child Switcher xác định trẻ đang được theo dõi. Home, Attendance, Routines, Learning và Fees sử dụng phạm vi trẻ khi phù hợp.

Ví dụ: Guardian Sarah liên kết với Emma và Sophia. Việc chuyển từ Emma sang Sophia không thay đổi hồ sơ, lớp, Centre hay trạng thái ghi danh của Emma.

### 4. In Scope (đề xuất lần review đầu)

| ID | Business Scope | Mô tả |
|---|---|---|
| SC-01 | Child Card | Hiển thị trẻ đang chọn |
| SC-02 | Child List | Danh sách trẻ được phép lựa chọn |
| SC-03 | Child Selection | Lựa chọn và chuyển đổi trẻ |
| SC-04 | Cross Brand | Chuyển giữa trẻ khác Brand |
| SC-05 | Cross Centre | Chuyển giữa trẻ khác Centre |
| SC-06 | Cross Country | Chuyển giữa trẻ khác quốc gia |
| SC-07 | Child Context | Hiển thị thông tin tương ứng với trẻ đang chọn |
| SC-08 | Last Selected Child | Ghi nhớ trẻ được chọn gần nhất |
| SC-09 | Child Status | Điều kiện lựa chọn theo trạng thái ghi danh |
| SC-10 | Access Restriction | Giới hạn thông tin theo quyền Guardian |
| SC-11 | Notification Context | Chuyển trẻ khi mở thông báo; chờ xác nhận backlog |
| SC-12 | Exception Handling | Không có trẻ hợp lệ, mất quyền, không thể xem thông tin |

### 5. Out of Scope

Tạo/chỉnh sửa hồ sơ trẻ, tạo Guardian, liên kết/gỡ liên kết Guardian–Child, mời phụ huynh, đăng nhập/kích hoạt, chuyển Centre/lớp, tạm nghỉ/nghỉ học/tốt nghiệp, quản lý Attendance, Routines, Fees/Billing, tạo và gửi Notifications, cấu hình Roles & Permissions.

### 6. Review Functional Requirements hiện tại

| FR | Nội dung | Đánh giá lần đầu |
|---|---|---|
| FR-001 | Hiển thị Child Card trên Home | Đạt |
| FR-002 | Danh sách trẻ liên kết ở mọi Brand, Centre, quốc gia | Làm rõ điều kiện hợp lệ |
| FR-003 | Chuyển toàn bộ app sang trẻ được chọn | Giới hạn phạm vi |
| FR-004 | Ghi nhớ trẻ gần nhất | Xác nhận chính sách |
| FR-005 | Chuyển trẻ khi mở thông báo | Làm rõ ngoại lệ |

FR-002: FR ghi mọi trẻ liên kết nhưng BR-005 loại Withdrawn và Graduated. Đề xuất: hiển thị trẻ được liên kết và đáp ứng điều kiện lựa chọn theo trạng thái ghi danh.

FR-003: "Mọi màn hình" quá rộng. Child Profile, Attendance, Routines, Learning, thông tin lớp theo trẻ; Guardian Profile và Account Settings không theo trẻ; Notifications tùy đối tượng; Fees/Invoice cần xác nhận. Đề xuất: các chức năng có phạm vi theo trẻ hiển thị thông tin của trẻ được chọn; chức năng cấp Guardian không thay đổi.

FR-004: FRS hiện quy định mở lại app giữ trẻ gần nhất; đăng xuất rồi đăng nhập lại chọn trẻ đầu tiên; thiết bị mới chọn mặc định nếu chưa có lựa chọn; trẻ gần nhất không hợp lệ chọn trẻ hợp lệ đầu tiên; không còn trẻ hợp lệ chưa quy định.

FR-005: Thông báo thuộc trẻ hiện tại giữ nguyên; trẻ khác được phép xem thì chuyển sang trẻ đó; thông báo chung giữ trẻ nếu áp dụng; không còn quyền thì không mở nội dung; nội dung không khả dụng cần thông báo; Centre khác cần làm rõ. Không đặc tả tạo/phân phối Notification.

### 7. Business Rules theo trạng thái trẻ

Theo Children & Families SRS: BR-CHF-006 (trạng thái do Joining & Leaving quản lý), BR-CHF-014 (Guardian có thể liên kết nhiều trẻ; unlink không xóa hồ sơ Guardian), BR-CHF-007 (trẻ nghỉ/tốt nghiệp vẫn tìm được trên SMS).

| Guardian liên kết | Trạng thái | Switcher theo FRS nháp |
|---|---|---|
| Có | Enrolled | Có |
| Có | Temporary Withdrawal | Có |
| Có | Withdrawn | Không |
| Có | Graduated | Không |
| Không | Bất kỳ | Không |

Không xuất hiện trong Switcher không đồng nghĩa mất quyền xem lịch sử. Ví dụ, trẻ tốt nghiệp vẫn còn hóa đơn chưa thanh toán: phụ huynh sẽ truy cập thế nào? Cần xác nhận.

### 8. Review file BBA-729_Review_BBA-145.md

Các nhóm vấn đề đã được nêu trong lần review đầu (diễn giải của trợ lý):
- RV-01: Thu hồi quyền xem khi đang sử dụng app.
- RV-02: Không có trẻ hợp lệ.
- RV-03: Vị trí thao tác chuyển trẻ.
- RV-04: Ghi nhớ lựa chọn khi đăng xuất/đổi thiết bị.
- RV-05: Thông báo/nội dung không còn được phép xem.
- RV-06: Chuyển Centre, nhiều ghi danh, xem lịch sử.
- RV-07: Thứ tự danh sách và đảm bảo đúng trẻ.

Chuyển ngôn ngữ kỹ thuật về hành vi nghiệp vụ: quyền xem đúng phạm vi; không hiển thị trẻ đã mất quyền; thông tin luôn thuộc trẻ đang chọn; thông báo xác định được trẻ và nội dung liên quan; quy tắc ghi nhớ và màn hình sau chuyển trẻ. Không đặc tả cơ chế thực hiện.

### 9. Business Flow đề xuất

Guardian mở Parents App → xác định danh sách trẻ hợp lệ:
- 0 trẻ: trạng thái không có trẻ hợp lệ.
- 1 trẻ: tự chọn trẻ duy nhất.
- 2+ trẻ: hiển thị trẻ gần nhất/mặc định, cho phép lựa chọn.
- Kiểm tra còn quyền xem trẻ; nếu không, chọn trẻ hợp lệ hoặc trạng thái trống.
- Hiển thị đúng trẻ; ghi nhớ lựa chọn nếu chính sách được xác nhận.

### 10. Acceptance Criteria đề xuất lần đầu

| ID | Given | When | Then |
|---|---|---|---|
| AC-R01 | Đang xem Emma | Quyền xem bị thu hồi và có hiệu lực | Không còn xem Emma |
| AC-R02 | Không có trẻ hợp lệ | Mở app | Hiển thị trạng thái không có trẻ hợp lệ |
| AC-R03 | Đang xem Emma | Chọn Sophia | Các chức năng theo trẻ hiện Sophia |
| AC-R04 | Đang xem Emma | Mở thông báo trẻ không còn quyền | Không hiển thị nội dung |
| AC-R05 | Sarah đăng xuất | David đăng nhập | Chỉ hiện trẻ thuộc David |
| AC-R06 | Xem Attendance Emma | Chọn Sophia, dữ liệu không khả dụng | Không hiện Attendance Emma thay thế |
| AC-R07 | Một trẻ học, một trẻ tạm nghỉ | Mở Switcher | Hiển thị hai trẻ theo trạng thái |
| AC-R08 | Trẻ đang chọn không còn hợp lệ | Mở lại app | Chọn trẻ hợp lệ mặc định hoặc trạng thái trống |
| AC-R09 | Thông báo không còn khả dụng | Mở thông báo | Hiện thông báo phù hợp |
| AC-R10 | Xem Account Settings | Đổi trẻ nếu có thể | Thông tin Guardian không đổi |

AC mới cần xác nhận nghiệp vụ trước nghiệm thu.

### 11. Open Questions

| ID | Vấn đề | Câu hỏi |
|---|---|---|
| OQ-01 | Lịch sử | Trẻ Withdrawn/Graduated có xem lại báo cáo, hóa đơn không? |
| OQ-02 | Không có trẻ hợp lệ | Guardian còn dùng được chức năng nào? |
| OQ-03 | Vị trí Switcher | Chỉ ở Home hay màn khác? |
| OQ-04 | Ghi nhớ | Đăng xuất/đổi thiết bị có giữ lựa chọn? |
| OQ-05 | Chuyển Centre | Xem được thông tin Centre cũ/mới nào? |
| OQ-06 | Nhiều ghi danh | Hiển thị Centre/lớp nào khi nhiều enrolment? |
| OQ-07 | Notifications | Tự chuyển trẻ có thuộc Sprint 5 không? |
| OQ-08 | Fees | Theo trẻ, Guardian hay gia đình? |
| OQ-09 | Temporary Withdrawal | Có xem lịch sử Attendance/Routines/Learning? |
| OQ-10 | Thứ tự | Trẻ đang học trước, ngày sinh tăng dần? Trùng ngày sinh xử lý thế nào? |

### 12. Scope đề xuất lần đầu

**In Scope:** Hiển thị trẻ đang chọn; danh sách trẻ liên kết đủ điều kiện; chuyển trẻ cùng/khác Brand, Centre, quốc gia; thông tin theo trẻ; ghi nhớ lựa chọn và mặc định; một hoặc không có trẻ hợp lệ; thay đổi trạng thái/quyền xem; giới hạn quyền; chuyển trẻ từ thông báo tùy BBA xác nhận.

**Out of Scope:** Quản lý hồ sơ trẻ/Guardian/liên kết, tài khoản, ghi danh/lớp/Centre/trạng thái, nội dung Attendance/Routines/Learning/Fees, tạo/cấu hình/gửi thông báo, cấu hình vai trò quyền.

**Business Dependencies:** Children & Families, Enrolment & Class Management, Joining & Leaving, Account Management, Notifications. Chuyển trẻ không thay đổi hồ sơ, liên kết, ghi danh; không làm thay đổi chức năng cấp Guardian.

### 13. Kết luận lần đầu

REVISE: mục tiêu và chức năng chính đạt; cần bổ sung ranh giới, BR, validation, AC, Assumptions/Open Questions; loại mô tả kỹ thuật. Đề xuất giữ hai User Story hiện có ở thời điểm review lần đầu. Chưa kiểm chứng ticket Plane, Q&A khách hàng hoặc Prototype. Chưa chỉnh sửa FRS gốc.

**Lưu ý:** Phần trao đổi tiếp theo điều chỉnh phân loại scope của lần review này; không coi mọi mục In Scope ở trên là yêu cầu khách hàng đã xác nhận.

## 03 — Người dùng (10:36)

> Hiện tại, khi tao đọc đến phần "6. Review các FR hiện tại". Tao có thấy mày có list ra danh sách các chức năng. Tuy nhiên, FR-002 và FR-003 và FR-004 và FR-005 tao đọc chưa hiểu lắm. Mày có thể mô tả rõ thêm về cái này được không ? và kèm theo thông tin này mày lấy từ đâu ? Hay scope chỉ nằm trong phạm vi về việc phụ huynh xem được danh sách con của mình trên điện thoại và xem thông tin chi tiết của trẻ. 
> Ngoài ra, nếu được mày hãy ghi lịch sử chat từ nảy đến giờ lên Git hub. Tạo 1 folder chứa cuộc trò chuyện của tao và mày. Lưu dưới dạng MD nhé

## 04 — Trợ lý (10:36) — Làm rõ phạm vi và điều chỉnh khuyến nghị

Cách hiểu của người dùng đúng với nghiệp vụ cốt lõi: xem danh sách con, lựa chọn một trẻ và xem thông tin tương ứng. Phân biệt Scope ticket gốc, Scope FRS nháp và đề xuất của BA.

### 1. Nguồn của FR

FR-002 đến FR-005 đã tồn tại trong Google Docs Sprint 5 và FRS GitHub v0.1, 26/11/2026, trạng thái Bản nháp chờ xác nhận. Không do trợ lý tự tạo trong lần review. Sự xuất hiện trong FRS không đồng nghĩa khách hàng đã xác nhận.

| FR | Vị trí |
|---|---|
| FR-001 / FR-002 / FR-003 | Mục 6.1, US-001 |
| FR-004 / FR-005 | Mục 6.2, US-002 |

### 2. Giải thích từng FR

#### FR-002 – Hiển thị danh sách con

Nguyên văn: “Hệ thống phải hiển thị danh sách mọi trẻ được liên kết với tài khoản phụ huynh khi phụ huynh chạm Child card, ở mọi Brand, Centre và quốc gia.”

Ví dụ: Sarah có Emma, Sophia, Lucas; một tài khoản có thể xem danh sách ba trẻ. Các trường Brand, Centre, quốc gia minh họa theo tài liệu. Core Scope là xem danh sách trẻ; Cross Brand/Centre/Country cần đối chiếu backlog gốc.

#### FR-003 – Xem thông tin trẻ được chọn

Nguyên văn: “Hệ thống phải chuyển toàn bộ app sang trẻ được chọn: mọi màn hình chỉ hiển thị dữ liệu của trẻ đó.”

Ví dụ: chọn Emma thì hiển thị Emma; chọn Sophia thì hiện Sophia. Attendance/Routines của trẻ được chọn tương ứng. Dữ liệu demo là giả lập.

Child Switcher: chọn trẻ nào, xác định trẻ được theo dõi. Child Profile: quy định trường thông tin chi tiết của trẻ. BBA-145 chịu trách nhiệm chọn/chuyển trẻ; nội dung từng màn hình thuộc chức năng tương ứng. Core Scope là xem đúng thông tin trẻ; không mặc định mọi màn hình đều theo trẻ.

#### FR-004 – Ghi nhớ trẻ được chọn gần nhất

Nguyên văn: “Hệ thống phải ghi nhớ trẻ được chọn gần nhất theo tài khoản trên thiết bị và hiển thị trẻ đó khi phụ huynh mở lại app.”

Ví dụ: 08:00 xem Emma; 08:05 chuyển Sophia; 08:10 đóng app không đăng xuất; 17:00 mở lại hiện Sophia. Đây là tiện ích trải nghiệm, không cần thiết để hoàn thành Child Switcher cơ bản. Chờ xác nhận nếu backlog không đề cập.

#### FR-005 – Tự chuyển trẻ từ thông báo

Nguyên văn: “Khi phụ huynh mở một thông báo về một trẻ, hệ thống phải chuyển sang trẻ đó trước khi mở bản ghi của thông báo.”

Ví dụ: đang xem Emma, nhận thông báo Sophia checked in. Chạm thông báo thì chuyển sang Sophia và mở điểm danh tương ứng. Child Switcher cơ bản vẫn hoạt động nếu không có FR này. Đây là nghiệp vụ liên quan Notifications; chờ xác nhận.

### 3. Phân loại điều chỉnh

| FR | Phân loại đề xuất |
|---|---|
| FR-001 – Hiển thị trẻ đang chọn | Core Scope |
| FR-002 – Xem danh sách con | Core Scope |
| FR-003 – Chọn và xem thông tin tương ứng | Core Scope |
| FR-004 – Ghi nhớ trẻ gần nhất | Pending Confirmation |
| FR-005 – Tự chuyển trẻ từ thông báo | Pending Confirmation |

Core Scope: danh sách trẻ liên kết; lựa chọn trẻ; xem thông tin tương ứng; không xem trẻ ngoài quyền.
Pending: Cross Brand/Centre/Country; ghi nhớ; tự chuyển từ Notification; chính sách trẻ tạm nghỉ/nghỉ học/tốt nghiệp.
Out of Scope: quản lý hồ sơ/liên kết; đặc tả chi tiết các module Attendance, Routines, Learning, Fees; quản lý/gửi Notification.

Không mặc định FR-004 và FR-005 bắt buộc chỉ vì đã có trong bản nháp. Điều chỉnh so với lần review đầu.

### 4. User Story đề xuất (nếu backlog chỉ yêu cầu danh sách và lựa chọn trẻ)

**US-001 – View and Switch Child**

**As a** Parent / Guardian,

**I want to** view the list of children linked to my account and select a child,

**So that** I can view the relevant information of each of my children on the Parents App.

Functional Requirements:
- FR-001 – View Selected Child: Hiển thị thông tin trẻ đang chọn.
- FR-002 – View Child List: Cho phép xem danh sách trẻ liên kết với tài khoản.
- FR-003 – Switch Child: Lựa chọn trẻ trong danh sách và xem thông tin tương ứng.

US-002 có thể giữ lại ở mục Pending Confirmation thay vì xóa hẳn. Chưa tìm được backlog gốc BBA-145/BBA-729 qua GitHub, nên chưa thể kết luận FR-004/FR-005 do khách hàng yêu cầu hay BA bổ sung.

### 5. Lưu trữ

Repository được kiểm tra ở chế độ Public. Lưu trên nhánh riêng docs/bba-chat-history, không thay đổi main hoặc FRS gốc. Bản ghi đã lược bỏ đường dẫn tài liệu nội bộ và chuyển các thành phần tương tác thành văn bản. Việc phân loại ở mục 04 là khuyến nghị BA mới nhất, chưa phải phạm vi được khách hàng phê duyệt.
