# Functional Requirements Specification — Child Switcher

**Dự án:** Busy Bees Asia SMS · **Module:** Parents App — Account & home · **Tính năng:** BBA-145 Child switcher  
**Mã tài liệu:** FRD-4.1.1.01_Child_Switcher · **Sprint:** 5 · **Phiên bản:** 0.1 · **Trạng thái:** Bản nháp chờ xác nhận · **Ngày:** 26/11/2026  
**Người soạn:** Business Analysis · **Người review:** HaiNguyen · **Người duyệt:** HaiNguyen

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 26/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu.

## 2. Mục đích và bối cảnh

Tài liệu đặc tả chức năng chuyển trẻ (Child switcher) trên Parents App: phụ huynh có nhiều con xem danh sách trẻ được liên kết với tài khoản của mình, ở mọi Brand, Centre và quốc gia, chọn một trẻ, và mọi màn hình của app hiển thị dữ liệu của đúng trẻ đó.

App ghi nhớ trẻ được chọn gần nhất để lần mở sau hiển thị đúng trẻ. Khi phụ huynh mở một thông báo, app tự chuyển sang trẻ mà thông báo đề cập rồi mới mở bản ghi. Liên kết giữa phụ huynh và trẻ được quản lý trên SMS (Children & Families); Parents App chỉ đọc liên kết này.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách trẻ liên kết với tài khoản phụ huynh; thẻ trẻ (Child card) trên Home; chọn trẻ và tải lại toàn bộ màn hình theo trẻ được chọn; ghi nhớ trẻ chọn gần nhất; tự chuyển trẻ khi mở thông báo; hiển thị trẻ đang tạm nghỉ. | Tạo, sửa, gỡ liên kết phụ huynh – trẻ (Children & Families trên SMS); đăng nhập, kích hoạt tài khoản (Account & sign-in); nội dung các màn hình Home, Attendance, Routines, Fees… (đặc tả riêng); xem hồ sơ trẻ chi tiết (Child profile); ứng dụng cho tài khoản không phải phụ huynh. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Phụ huynh (Guardian) | Các trẻ được liên kết với tài khoản của mình. | Xem danh sách trẻ, chọn trẻ, xem dữ liệu của trẻ đang chọn. |
| System | Liên kết phụ huynh – trẻ, ghi danh và lớp của trẻ. | Cung cấp danh sách trẻ theo tài khoản; chỉ trả dữ liệu của trẻ thuộc tài khoản; ghi nhớ trẻ chọn gần nhất; gắn mã trẻ vào thông báo. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-145 gồm hai User Story trên Parents App, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| Account & home | Chọn trẻ | Xem danh sách trẻ liên kết và chuyển sang trẻ khác; mọi màn hình hiển thị dữ liệu của trẻ được chọn. | BBA-145: US-001 |
| Account & home | Ghi nhớ trẻ và mở từ thông báo | Mở app hiển thị trẻ chọn gần nhất; mở thông báo thì app chuyển sang đúng trẻ. | BBA-145: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-145: US-001 - Chọn trẻ

#### User Story

Là phụ huynh có nhiều con học tại Busy Bees, tôi muốn chọn từng con trên app, để xem đúng thông tin của trẻ đó mà không lẫn với trẻ khác.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải hiển thị thẻ trẻ (Child card) của trẻ đang chọn ở đầu màn hình Home. |
| FR-002 | Hệ thống phải hiển thị danh sách mọi trẻ được liên kết với tài khoản phụ huynh khi phụ huynh chạm Child card, ở mọi Brand, Centre và quốc gia. |
| FR-003 | Hệ thống phải chuyển toàn bộ app sang trẻ được chọn: mọi màn hình chỉ hiển thị dữ liệu của trẻ đó. |

#### Functional Flow - Main (Luồng chính)

1. Phụ huynh mở app. Home hiển thị Child card của trẻ đang chọn (FR-001).
2. Phụ huynh chạm Child card. Hệ thống mở danh sách trẻ (Child picker) với các trẻ được liên kết (FR-002).
3. Phụ huynh chọn một trẻ. Hệ thống đóng danh sách, xoá dữ liệu đang hiển thị của trẻ trước và tải lại màn hình hiện tại theo trẻ vừa chọn (FR-003).

#### Functional Flow - Alternative (Luồng thay thế)

1. Phụ huynh chỉ có một trẻ: Child card không có biểu tượng chuyển và chạm vào không mở danh sách (BR-004).
2. Phụ huynh chọn lại đúng trẻ đang chọn: hệ thống đóng danh sách, không tải lại dữ liệu.
3. Trẻ được chọn đang tạm nghỉ (Temporary Withdrawal): app chuyển sang trẻ; các màn hình điểm danh, routine và lớp hiển thị trạng thái trống “Not attending at the moment” (BR-005).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không tải được danh sách trẻ: hiển thị “Couldn't load your children. Try again.” và nút Try again; giữ trẻ đang chọn.
2. Không tải được dữ liệu của trẻ vừa chọn: màn hình hiển thị lỗi theo hành vi chuẩn; không hiển thị dữ liệu của trẻ trước.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Danh sách chỉ gồm trẻ được liên kết với tài khoản phụ huynh đang đăng nhập. Không màn hình nào hiển thị tên, ảnh hay bản ghi của trẻ không thuộc tài khoản. |
| BR-002 | Mỗi dòng trong danh sách gồm: ảnh trẻ (không có ảnh thì hiển thị chữ cái đầu của tên), tên gọi và họ, Brand, Centre, lớp chính, quốc gia; trẻ đang chọn có dấu ✓. |
| BR-003 | Thứ tự danh sách: trẻ đang theo học trước, sau đó theo ngày sinh tăng dần. |
| BR-004 | Phụ huynh có một trẻ: Child card không mở danh sách. |
| BR-005 | Trẻ đang tạm nghỉ vẫn có trong danh sách với nhãn “Temporarily withdrawn”. Trẻ đã nghỉ học hẳn (Withdrawn) hoặc đã tốt nghiệp không có trong danh sách. |
| BR-006 | Sau khi chuyển trẻ, không màn hình nào còn dữ liệu của trẻ trước. Yêu cầu dữ liệu của trẻ trước đang chạy bị huỷ; kết quả trả về muộn bị bỏ qua. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | App yêu cầu dữ liệu của trẻ không liên kết với tài khoản. | Không cung cấp dữ liệu; app hiển thị lỗi theo hành vi chuẩn. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-145: UI-US-001 - Home: Child card | https://bba-parents.lovable.app/ |
| BBA-145: UI-US-001 - Child picker | https://bba-parents.lovable.app/children |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Child card | Thẻ / thao tác | — | Trẻ đang chọn | FR-001;BR-004 | Hiển thị ảnh, tên, Centre, lớp của trẻ đang chọn; chạm để mở Child picker khi có từ hai trẻ. |
| Child picker | Bottom sheet | — | Đóng | FR-002;BR-001 | Danh sách trẻ liên kết với tài khoản. |
| Dòng trẻ | Danh sách chọn | — | Trẻ đang chọn có dấu ✓ | BR-002;BR-003 | Ảnh / chữ cái đầu, tên, Brand, Centre, lớp, quốc gia; chạm để chọn trẻ. |
| Nhãn Temporarily withdrawn | Nhãn | — | Ẩn | BR-005 | Hiện ở dòng trẻ đang tạm nghỉ. |
| Đang tải | Trạng thái | — | Khung xương danh sách | — | Hiện trong khi tải danh sách. |
| Try again | Thao tác | — | Ẩn | — | Hiện khi không tải được danh sách; tải lại. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Đọc liên kết phụ huynh – trẻ và thông tin hiển thị (ảnh, tên, Brand, Centre, lớp, quốc gia, trạng thái ghi danh) từ SMS. Chọn trẻ không tạo hay thay đổi dữ liệu trên SMS. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Sarah có Emma (Small Wonder Tampines, Singapore) và Sophia (Brighton Montessori Mont Kiara, Malaysia) | Sarah chạm Child card | danh sách hiện Emma và Sophia với Brand, Centre, lớp, quốc gia; Emma có dấu ✓ | FR-002;BR-001;BR-002 |
| AC-002 | Sarah đang xem Routines của Emma | Sarah chọn Sophia | màn Routines tải lại và chỉ hiện dữ liệu của Sophia | FR-003;BR-006 |
| AC-003 | David chỉ có một trẻ | David chạm Child card | danh sách không mở | BR-004 |
| AC-004 | Zoe của Sarah đang tạm nghỉ | Sarah mở danh sách và chọn Zoe | Zoe có nhãn Temporarily withdrawn; màn Attendance hiện “Not attending at the moment” | BR-005 |
| AC-005 | Mia đã tốt nghiệp, Emma đang học | Sarah mở danh sách | chỉ có Emma | BR-005 |
| AC-006 | Mất kết nối mạng | Sarah chạm Child card | hiện “Couldn't load your children. Try again.” và nút Try again; vẫn giữ Emma | FR-002 |

#### Dependencies (Phụ thuộc)

Liên kết phụ huynh – trẻ, trạng thái ghi danh (Children & Families); Temporary Withdrawal (Joining & leaving); đăng nhập Parents App.

### 6.2 BBA-145: US-002 - Ghi nhớ trẻ và mở từ thông báo

#### User Story

Là phụ huynh, tôi muốn app mở đúng trẻ tôi xem gần nhất và mở đúng trẻ khi tôi chạm một thông báo, để không phải chọn lại mỗi lần.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Hệ thống phải ghi nhớ trẻ được chọn gần nhất theo tài khoản trên thiết bị và hiển thị trẻ đó khi phụ huynh mở lại app. |
| FR-005 | Khi phụ huynh mở một thông báo về một trẻ, hệ thống phải chuyển sang trẻ đó trước khi mở bản ghi của thông báo. |

#### Functional Flow - Main (Luồng chính)

1. Phụ huynh chọn một trẻ (US-001). Hệ thống lưu trẻ đó là trẻ chọn gần nhất (FR-004).
2. Phụ huynh đóng rồi mở lại app. Home hiển thị trẻ chọn gần nhất.
3. Phụ huynh chạm một thông báo về trẻ khác trẻ đang chọn. Hệ thống chuyển sang trẻ của thông báo, rồi mở bản ghi mà thông báo đề cập (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Lần đầu đăng nhập trên thiết bị: hiển thị trẻ đầu tiên theo thứ tự ở BR-003.
2. Thông báo về đúng trẻ đang chọn: mở bản ghi, không chuyển trẻ.
3. Thông báo áp dụng cho nhiều trẻ (ví dụ thông báo chung của Centre): mở bản ghi, giữ trẻ đang chọn.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chọn gần nhất không còn liên kết với tài khoản: hiển thị trẻ đầu tiên theo BR-003 (BR-007).
2. Thông báo về trẻ không còn liên kết với tài khoản: mở Home với trẻ đang chọn và hiển thị “This item is no longer available.”

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-007 | Trẻ chọn gần nhất được lưu theo tài khoản và thiết bị. Khi trẻ đó không còn trong danh sách (BR-005), app dùng trẻ đầu tiên theo BR-003. |
| BR-008 | Mỗi thông báo về một trẻ mang mã trẻ và mã bản ghi. Mở thông báo thì app chuyển trẻ (nếu khác trẻ đang chọn) rồi mở bản ghi; trẻ chọn gần nhất được cập nhật theo trẻ của thông báo. |
| BR-009 | Đăng xuất xoá trẻ chọn gần nhất trên thiết bị. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-002 | Thông báo mang mã trẻ không liên kết với tài khoản. | Không mở bản ghi; hiển thị “This item is no longer available.” |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-145: UI-US-002 - Home khi mở lại app | https://bba-parents.lovable.app/ |
| BBA-145: UI-US-002 - Mở từ Notifications | https://bba-parents.lovable.app/notifications |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Child card | Thẻ / thao tác | — | Trẻ chọn gần nhất | FR-004;BR-007 | Hiển thị trẻ chọn gần nhất khi mở app. |
| Thông báo đẩy / mục trong Notifications | Thao tác | — | Theo thông báo | FR-005;BR-008 | Chuyển sang trẻ của thông báo rồi mở bản ghi. |
| This item is no longer available. | Thông báo ngắn | — | Ẩn | VAL-002 | Hiện khi bản ghi thuộc trẻ không còn liên kết. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Lưu mã trẻ chọn gần nhất trên thiết bị theo tài khoản; xoá khi đăng xuất. Không lưu lên SMS. |
| DATA-003 | Thông báo gửi tới Parents App mang mã trẻ và mã bản ghi để mở đúng nội dung. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-007 | Sarah chọn Sophia rồi đóng app | Sarah mở lại app | Home hiện Sophia | FR-004;BR-007 |
| AC-008 | Sarah đang xem Emma | Sarah chạm thông báo “Sophia checked in” | app chuyển sang Sophia và mở bản ghi check-in của Sophia | FR-005;BR-008 |
| AC-009 | Sarah đang xem Emma | Sarah chạm thông báo đóng cửa Centre gửi cho cả hai trẻ | mở thông báo, vẫn giữ Emma | BR-008 |
| AC-010 | Trẻ chọn gần nhất là Mia, Mia đã tốt nghiệp | Sarah mở app | Home hiện trẻ đầu tiên theo thứ tự danh sách | BR-007 |
| AC-011 | Sarah đăng xuất rồi đăng nhập lại trên cùng thiết bị | app mở Home | hiện trẻ đầu tiên theo thứ tự danh sách | BR-009 |
| AC-012 | Thông báo về Mia, Mia không còn liên kết với tài khoản | Sarah chạm thông báo | mở Home với trẻ đang chọn và hiện “This item is no longer available.” | VAL-002 |

#### Dependencies (Phụ thuộc)

US-001; Notifications (Parents App); các màn hình nhận thông báo (Attendance, Routines, Fees…).

## 7. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Phụ huynh (Guardian) | Người giám hộ có tài khoản Parents App; mỗi người giám hộ một tài khoản. |
| Trẻ liên kết | Trẻ được gắn với tài khoản phụ huynh trên SMS (Children & Families). |
| Child card | Thẻ hiển thị trẻ đang chọn ở đầu Home. |
| Child picker | Danh sách trẻ để chọn, mở từ Child card. |
| Trẻ chọn gần nhất | Trẻ phụ huynh chọn lần cuối trên thiết bị; app hiển thị khi mở lại. |
