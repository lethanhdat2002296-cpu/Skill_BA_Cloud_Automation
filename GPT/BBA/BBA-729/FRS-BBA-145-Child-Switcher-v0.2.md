# Functional Requirements Specification — Child Switcher

**Dự án:** Busy Bees Asia SMS  
**Module:** Parents App — Account & Home  
**Tính năng:** BBA-145 — Child Switcher | **Task BA:** BBA-729  
**Mã tài liệu:** FRD-4.1.1.01_Child_Switcher | **Sprint:** 5  
**Phiên bản:** 0.2 | **Trạng thái:** Bản nháp chờ review | **Ngày:** 28/11/2026  
**Người soạn:** Business Analysis | **Người review:** HaiNguyen | **Người duyệt:** HaiNguyen (chưa duyệt)

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 26/11/2026 | Business Analysis | Khởi tạo | Chưa xác nhận |
| 0.2 | 28/11/2026 | Business Analysis / GPT | Giữ FR-002, FR-003; loại FR-001, FR-004, FR-005 và US-002 khỏi đặc tả độc lập; cập nhật các nội dung liên quan | Chờ review |

Mức sẵn sàng: Bản nháp đặc tả nghiệp vụ theo phạm vi đã thống nhất với BA; các chính sách chưa xác nhận được liệt kê tại mục 7. Chưa đối chiếu được ticket backlog gốc.

## 2. Mục đích và bối cảnh

Chức năng Child Switcher cho phép phụ huynh xem danh sách trẻ của mình trên Parents App và lựa chọn từng trẻ để theo dõi thông tin tương ứng, không nhầm lẫn giữa các trẻ.

Mối quan hệ giữa phụ huynh và trẻ được quản lý tại Children & Families trên SMS. Child Switcher sử dụng thông tin này để xác định phạm vi trẻ mà phụ huynh được phép xem; việc lựa chọn trẻ không thay đổi hồ sơ của trẻ hoặc phụ huynh.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Hiển thị danh sách trẻ của phụ huynh. | Tạo, sửa, gỡ liên kết phụ huynh – trẻ; quản lý hồ sơ trẻ và Guardian trên SMS. |
| Lựa chọn và chuyển đổi giữa các trẻ để xem thông tin tương ứng. | Đăng nhập, kích hoạt và quản lý tài khoản Parents App. |
| Kiểm soát phạm vi trẻ mà phụ huynh được phép theo dõi. | Quản lý ghi danh, chuyển Centre, phân lớp và thay đổi trạng thái của trẻ. |
| Xử lý trường hợp không có trẻ, chỉ có một trẻ hoặc không thể xem thông tin trẻ. | Đặc tả nội dung chi tiết Child Profile, Home, Attendance, Routines, Learning, Fees và các chức năng khác; quản lý và gửi thông báo. |

Child Card không phải một yêu cầu nghiệp vụ độc lập. Ghi nhớ trẻ được chọn gần nhất và chuyển trẻ khi mở thông báo là hành vi mặc định của ứng dụng theo thống nhất với BA, không đặc tả thành FR/US riêng trong tài liệu này. Việc loại bỏ các FR tương ứng không có nghĩa là yêu cầu bỏ các hành vi đó khỏi ứng dụng.

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Phụ huynh (Guardian) | Các trẻ mà tài khoản phụ huynh được phép theo dõi. | Xem danh sách trẻ; lựa chọn và xem thông tin tương ứng của trẻ. |
| System | Thông tin trẻ và mối quan hệ phụ huynh – trẻ trên SMS. | Hiển thị danh sách trẻ đúng phạm vi quyền của phụ huynh; hiển thị thông tin đúng trẻ được chọn; không cho xem trẻ ngoài phạm vi quyền. |

## 5. Tổng quan tính năng và phân rã chức năng

| Module | Tính năng | Mô tả | User Story | FR |
|---|---|---|---|---|
| Account & Home | Child Switcher | Xem danh sách trẻ của phụ huynh và lựa chọn trẻ để theo dõi thông tin. | BBA-145: US-001 | FR-002, FR-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-145: US-001 — Xem danh sách và chuyển đổi trẻ

#### User Story

Là phụ huynh có con đang theo học tại Busy Bees, tôi muốn xem danh sách các con của mình và lựa chọn từng trẻ để theo dõi thông tin tương ứng trên Parents App.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Tên chức năng | Yêu cầu chức năng |
|---|---|---|
| FR-002 | Hiển thị danh sách trẻ của phụ huynh (View Children List) | Hệ thống phải hiển thị danh sách trẻ mà phụ huynh được phép theo dõi trên Parents App. |
| FR-003 | Chuyển đổi trẻ (Switch Child) | Hệ thống phải cho phép phụ huynh lựa chọn và chuyển đổi giữa các trẻ trong danh sách để xem thông tin tương ứng của từng trẻ. |

#### Functional Flow — Main (Luồng chính)

Điều kiện trước: Phụ huynh có tài khoản Parents App hợp lệ và được phép theo dõi ít nhất một trẻ.

1. Phụ huynh truy cập chức năng xem danh sách trẻ.
2. Hệ thống hiển thị danh sách trẻ của phụ huynh (FR-002).
3. Phụ huynh lựa chọn trẻ muốn theo dõi trong danh sách (FR-003).
4. Hệ thống hiển thị thông tin tương ứng với trẻ được chọn tại các chức năng có phạm vi theo trẻ (BR-006).
5. Khi phụ huynh lựa chọn trẻ khác, thông tin hiển thị chuyển sang trẻ vừa chọn (FR-003).

Kết quả: Phụ huynh xem đúng thông tin của trẻ được chọn, trong phạm vi quyền của mình.

#### Functional Flow — Alternative (Luồng thay thế)

| ID | Tình huống | Kết quả |
|---|---|---|
| ALT-01 | Phụ huynh chỉ có một trẻ được phép theo dõi. | Phụ huynh xem được thông tin của trẻ đó mà không cần chuyển đổi giữa các trẻ. |
| ALT-02 | Phụ huynh chọn lại trẻ đang theo dõi. | Tiếp tục hiển thị thông tin của trẻ đó. |

#### Functional Flow — Exception (Luồng ngoại lệ)

| ID | Tình huống | Kết quả |
|---|---|---|
| EX-01 | Phụ huynh không có trẻ nào được phép theo dõi. | Thông báo không có trẻ để theo dõi; không hiển thị thông tin của trẻ khác. Các chức năng cấp tài khoản do đặc tả tương ứng quyết định. |
| EX-02 | Phụ huynh chọn hoặc truy cập thông tin của trẻ không còn thuộc phạm vi quyền. | Không cho xem thông tin trẻ đó; phụ huynh được thông báo và có thể xem danh sách trẻ còn được phép theo dõi (VAL-001). |
| EX-03 | Không thể hiển thị danh sách trẻ. | Thông báo không thể xem danh sách và cho phép thử lại. |
| EX-04 | Không thể hiển thị thông tin của trẻ vừa chọn. | Thông báo không thể xem thông tin của trẻ vừa chọn; không hiển thị thông tin của trẻ trước dưới tên trẻ mới. |

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc | FR liên quan |
|---|---|---|
| BR-001 | Phụ huynh chỉ được xem danh sách và thông tin của các trẻ mà mình có quyền theo dõi. | FR-002, FR-003 |
| BR-002 | Phụ huynh có thể theo dõi nhiều trẻ trên cùng một tài khoản. Danh sách hiển thị tên trẻ để phụ huynh nhận biết và lựa chọn; các thông tin nhận diện bổ sung cần xác nhận tại OQ-04. | FR-002 |
| BR-006 | Thông tin tại các chức năng có phạm vi theo trẻ phải tương ứng với trẻ đang được chọn. Việc chuyển trẻ không làm thay đổi thông tin thuộc phạm vi tài khoản phụ huynh. | FR-003 |
| BR-010 | Việc lựa chọn hoặc chuyển đổi trẻ không làm thay đổi hồ sơ trẻ, hồ sơ phụ huynh hoặc mối quan hệ giữa phụ huynh và trẻ. | FR-003 |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống | BR liên quan |
|---|---|---|---|
| VAL-001 | Trẻ được chọn không thuộc phạm vi quyền của phụ huynh hoặc quyền theo dõi trẻ đã bị thu hồi và có hiệu lực. | Không hiển thị thông tin của trẻ đó; thông báo phụ huynh không có quyền xem thông tin này. | BR-001 |

#### UI Reference (Tham chiếu giao diện)

| Mã tham chiếu | Nội dung | Ghi chú |
|---|---|---|
| BBA-145: UI-US-001 | Danh sách trẻ của phụ huynh và thao tác lựa chọn trẻ | Prototype Parents App: /children theo FRS v0.1. Chưa kiểm chứng giao diện thực tế. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Hành vi | FR liên quan |
|---|---|---|---|
| Danh sách trẻ | Danh sách | Hiển thị các trẻ thuộc phạm vi quyền của phụ huynh. | FR-002 |
| Tên trẻ | Thông tin hiển thị | Nhận biết trẻ trong danh sách. | FR-002 |
| Lựa chọn trẻ | Thao tác | Cho phép chọn trẻ để xem thông tin tương ứng. | FR-003 |

Không quy định Child Card, Bottom Sheet, vị trí nút hoặc kiểu hiển thị cụ thể. Các trường thông tin bổ sung và cách phân biệt trẻ trùng tên cần xác nhận tại OQ-04.

#### Data and Audit (Dữ liệu và audit — mức nghiệp vụ)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Danh sách sử dụng thông tin trẻ và mối quan hệ phụ huynh – trẻ được quản lý trên SMS. Việc lựa chọn trẻ không tạo mới hay thay đổi hồ sơ trên SMS. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Sarah được phép theo dõi Emma và Sophia; Noah không thuộc phạm vi quyền của Sarah. | Sarah xem danh sách trẻ. | Danh sách hiển thị Emma và Sophia, không hiển thị Noah. | FR-002; BR-001; BR-002 |
| AC-002 | Sarah đang xem thông tin Emma và được phép theo dõi Sophia. | Sarah chọn Sophia. | Các chức năng theo trẻ hiển thị thông tin Sophia, không hiển thị thông tin Emma dưới tên Sophia. | FR-003; BR-006 |
| AC-003 | David chỉ được phép theo dõi một trẻ là Lucas. | David truy cập chức năng theo dõi trẻ. | David xem được thông tin Lucas mà không cần chuyển đổi trẻ. | FR-002; FR-003; ALT-01 |
| AC-006 | Danh sách trẻ không thể hiển thị. | Sarah truy cập danh sách. | Hệ thống thông báo không thể xem danh sách và cho phép thử lại. | FR-002; EX-03 |
| AC-013 | Sarah không được phép theo dõi Noah. | Sarah truy cập thông tin Noah. | Hệ thống không hiển thị thông tin Noah và thông báo không có quyền xem. | FR-003; BR-001; VAL-001 |
| AC-014 | Sarah không có trẻ nào được phép theo dõi. | Sarah truy cập danh sách trẻ. | Hệ thống thông báo không có trẻ để theo dõi; không hiển thị thông tin của trẻ khác. | FR-002; BR-001; EX-01 |
| AC-015 | Sarah được phép theo dõi Emma và Sophia nhưng thông tin Sophia không thể hiển thị. | Sarah chọn Sophia. | Hệ thống thông báo không thể xem thông tin Sophia; không hiển thị thông tin Emma dưới tên Sophia. | FR-003; BR-006; EX-04 |
| AC-016 | Sarah đang xem Emma và quyền theo dõi Emma bị thu hồi, đã có hiệu lực. | Sarah truy cập lại thông tin Emma. | Hệ thống không hiển thị thông tin Emma; Emma không còn xuất hiện trong danh sách trẻ được phép theo dõi. | FR-002; FR-003; BR-001; VAL-001; EX-02 |
| AC-017 | Sarah có hai trẻ được phép theo dõi. | Sarah chuyển từ Emma sang Sophia. | Hồ sơ trẻ, hồ sơ phụ huynh, mối quan hệ phụ huynh – trẻ và thông tin cấp tài khoản không thay đổi. | FR-003; BR-006; BR-010 |

Các tên trẻ và phụ huynh trong AC là dữ liệu minh họa. Các AC cho trường hợp một trẻ, không có trẻ và thu hồi quyền là đề xuất BA cần review; không quy định phương thức kỹ thuật thực hiện.

#### Dependencies (Phụ thuộc)

| Phân hệ | Phụ thuộc nghiệp vụ |
|---|---|
| Children & Families | Thông tin trẻ và mối quan hệ phụ huynh – trẻ. |
| Account & Sign-in | Tài khoản và phạm vi truy cập của phụ huynh. |
| Joining & Leaving / Enrolment | Trạng thái ghi danh, Centre và lớp nếu chính sách hiển thị được xác nhận. |
| Các chức năng theo trẻ trên Parents App | Hiển thị nội dung của trẻ được chọn; nội dung chi tiết do FRS riêng quy định. |

## 7. Câu hỏi mở (Open Questions)

Các chính sách dưới đây xuất hiện trong bản v0.1 hoặc phát sinh khi review nhưng chưa được BA xác nhận là phạm vi bắt buộc. Không dùng làm tiêu chí nghiệm thu chính thức trước khi có quyết định.

| OQ ID | Quyết định cần có | Nguồn / Căn cứ | Đối tượng xác nhận | Ảnh hưởng |
|---|---|---|---|---|
| OQ-01 | Có cho phép xem trẻ thuộc các Brand, Centre hoặc quốc gia khác nhau trên cùng tài khoản không? | FR-002 v0.1 | BBA / HQ Ops | FR-002; FR-003 |
| OQ-02 | Trẻ Temporary Withdrawal, Withdrawn hoặc Graduated có xuất hiện trong danh sách không? Quyền xem lịch sử của các trẻ này như thế nào? | BR-005 v0.1 | BBA / HQ Ops / Finance | FR-002; FR-003 |
| OQ-03 | Danh sách trẻ có cần sắp xếp theo trạng thái ghi danh, ngày sinh hay thứ tự khác không? | BR-003 v0.1 | BBA / Product | FR-002 |
| OQ-04 | Ngoài tên trẻ, cần hiển thị ảnh, Brand, Centre, lớp chính, quốc gia hoặc thông tin nhận diện nào, đặc biệt khi trùng tên? | BR-002 v0.1 | BBA / Product | FR-002 |
| OQ-05 | Phạm vi các chức năng theo trẻ, theo gia đình và theo tài khoản (ví dụ Fees) được phân định thế nào? | FR-003 v0.1 và review BA | BBA / Product / Finance | FR-003 |

## 8. Phụ lục

### A. Thuật ngữ

| Thuật ngữ | Định nghĩa |
|---|---|
| Phụ huynh (Guardian) | Người giám hộ có tài khoản Parents App. |
| Danh sách trẻ của phụ huynh | Danh sách trẻ mà phụ huynh được phép theo dõi. |
| Trẻ đang được chọn | Trẻ mà phụ huynh đang theo dõi thông tin trên Parents App. |
| Child Switcher | Chức năng xem danh sách và lựa chọn, chuyển đổi trẻ. |

### B. Truy vết thay đổi từ v0.1

| Nhóm | Giữ / điều chỉnh | Loại khỏi đặc tả độc lập hoặc chuyển chờ xác nhận |
|---|---|---|
| US | US-001 | US-002 |
| FR | FR-002, FR-003 | FR-001, FR-004, FR-005 |
| BR | BR-001, BR-002, BR-006; bổ sung BR-010 | BR-003 → OQ-03; BR-004 → ALT-01; BR-005 → OQ-02; BR-007 đến BR-009 là hành vi mặc định |
| VAL | VAL-001 | VAL-002 thuộc luồng Notifications |
| DATA | DATA-001 | DATA-002, DATA-003 thuộc hành vi mặc định |
| AC | AC-001, AC-002, AC-003, AC-006; bổ sung AC-013 đến AC-017 | AC-004, AC-005 chờ OQ-02; AC-007 đến AC-012 không còn thuộc nghiệm thu độc lập của Child Switcher |

Giữ mã cũ cho các nội dung còn hiệu lực; không tái sử dụng mã đã loại bỏ. Các mã mới tiếp nối bản 0.1.

### C. Nguồn và giới hạn review

- FRS BBA-145 Child Switcher v0.1 (26/11/2026), Sprint 5, bản nháp chờ xác nhận.
- Children & Families SRS v0.1, BR-CHF-006, BR-CHF-007, BR-CHF-014 (ranh giới quản lý hồ sơ và trạng thái).
- Trao đổi BA – GPT ngày 28/11/2026: loại FR-001, FR-004, FR-005; đổi tên và tinh gọn FR-002; giữ FR-003; đặc tả thuần nghiệp vụ.
- Chưa đối chiếu được backlog gốc trên Plane, Q&A khách hàng và Prototype thực tế; chưa xác nhận các câu hỏi mở hoặc phê duyệt FRS.