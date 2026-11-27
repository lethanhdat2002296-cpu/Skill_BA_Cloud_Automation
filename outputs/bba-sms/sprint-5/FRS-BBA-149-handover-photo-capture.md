# Functional Requirements Specification — Handover Photo Capture

**Dự án:** Busy Bees Asia SMS · **Module:** Attendance App (gate iPad) — Kiosk · **Tính năng:** BBA-149 Handover photo capture  
**Mã tài liệu:** FRD-4.4.1.03_Handover_Photo_Capture · **Sprint:** 5 · **Phiên bản:** 0.2 · **Trạng thái:** Bản nháp chờ xác nhận · **Ngày:** 27/11/2026  
**Người soạn:** Business Analysis · **Người review:** HaiNguyen · **Người duyệt:** HaiNguyen

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 26/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 27/11/2026 | Business Analysis | Check-in / check-out xe bus làm từng trẻ (Q-75-10); thời gian lưu ảnh chuyển thành câu hỏi mở (Q-75-12); thêm Câu hỏi mở. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu. Đã đối chiếu bảng câu hỏi Sprint 4; 1 câu hỏi mở ở mục 7.

## 2. Mục đích và bối cảnh

Tài liệu đặc tả việc chụp ảnh bàn giao trên Attendance App (iPad dùng chung tại cổng): mỗi lần check-in và check-out, nhân viên chụp ảnh trẻ cùng người đưa / người đón. Ảnh được lưu cùng bản ghi điểm danh, đồng bộ lên SMS, gửi kèm thông báo check-in cho phụ huynh và hiển thị trên SMS (BBA-73) để đối chiếu.

iPad đăng nhập bằng tài khoản Centre, không ghi tên nhân viên bấm nút. Mọi bản ghi được lưu trên iPad trước rồi đồng bộ khi có mạng.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Chụp ảnh bàn giao bắt buộc khi check-in và check-out; xem lại, chụp lại; đổi camera; nén ảnh và xoá vị trí; lưu trên iPad và đồng bộ cùng bản ghi; sửa ảnh của bản ghi chưa đồng bộ; xoá bản sao trên iPad sau khi đồng bộ; ảnh trong thông báo check-in và màn Attendance của phụ huynh. | Chọn người đưa / người đón (BBA-150); nhập nhiệt độ (BBA-151); xem, xuất ảnh trên SMS (BBA-73); huỷ bản ghi đã đồng bộ (void request); ảnh routine (BBA-148); nhận diện khuôn mặt; check-in bằng QR / RFID. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Nhân viên tại cổng | Trẻ của Centre theo phạm vi iPad (level, lớp). | Chụp, chụp lại ảnh bàn giao; lưu check-in / check-out. |
| Phụ huynh (Guardian) | Trẻ liên kết với tài khoản. | Nhận ảnh trong thông báo check-in; xem ảnh ở Attendance (Parents App). |
| System | Bản ghi điểm danh và ảnh bàn giao. | Nén, lưu ảnh trên iPad; đồng bộ; lưu trữ ảnh; cung cấp ảnh cho SMS và Parents App theo quyền. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-149 gồm hai User Story trên Attendance App, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| Kiosk | Chụp ảnh bàn giao | Chụp ảnh bắt buộc khi check-in và check-out; xem lại, chụp lại. | BBA-149: US-001 |
| Kiosk | Lưu và đồng bộ ảnh | Lưu ảnh trên iPad, đồng bộ cùng bản ghi, sửa trước khi đồng bộ, gửi ảnh cho phụ huynh. | BBA-149: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-149: US-001 - Chụp ảnh bàn giao

#### User Story

Là nhân viên tại cổng, tôi muốn chụp ảnh trẻ cùng người đưa / người đón mỗi lần nhận và trả trẻ, để có bằng chứng bàn giao.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải yêu cầu một ảnh bàn giao cho mỗi lần check-in và mỗi lần check-out; không lưu được bản ghi khi chưa có ảnh. |
| FR-002 | Hệ thống phải mở camera toàn màn hình với chụp, đổi camera trước / sau, chụp lại và dùng ảnh. |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên mở Check in (hoặc Check out) của trẻ. Màn hình có ô Photo trống.
2. Nhân viên chạm ô Photo. Hệ thống mở camera toàn màn hình, mặc định camera sau (FR-002).
3. Nhân viên chụp. Hệ thống hiển thị ảnh vừa chụp với Retake và Use photo.
4. Nhân viên chọn Use photo. Ảnh thu nhỏ hiển thị trong ô Photo; Save dùng được khi các trường khác hợp lệ (FR-001).

#### Functional Flow - Alternative (Luồng thay thế)

1. Nhân viên chọn Retake: chụp lại; chỉ ảnh cuối cùng được dùng.
2. Nhân viên đổi sang camera trước khi người lớn và trẻ đứng phía màn hình.
3. Trẻ đi xe bus: nhân viên lọc theo xe để gom trẻ của một xe vào danh sách; check-in, check-out vẫn làm từng trẻ, mỗi trẻ một bản ghi và một ảnh chụp cùng tài xế / phụ xe (BR-004; Q-75-10).
4. Nhân viên đóng camera khi chưa chụp: quay lại form, ô Photo vẫn trống.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Ứng dụng không có quyền dùng camera: hiển thị “Camera access is off. Turn it on in Settings › BBA Attendance.” và nút Open Settings; không lưu được bản ghi (BR-003).
2. Camera lỗi: hiển thị “The camera isn't working. Restart the iPad or contact the Centre Admin.”; không lưu được bản ghi.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi check-in và mỗi check-out có đúng một ảnh bàn giao. Không có ảnh thì không lưu. |
| BR-002 | Ảnh chụp trực tiếp từ camera của iPad; không chọn ảnh có sẵn trong thư viện. |
| BR-003 | Không có ngoại lệ lưu bản ghi không ảnh trên iPad. Khi camera không dùng được, Centre ghi điểm danh trên SMS theo BBA-73 US-002. |
| BR-004 | Lọc theo xe bus chỉ để gom danh sách. Không có bản ghi chung cho cả xe: mỗi trẻ một bản ghi check-in / check-out và một ảnh riêng (Q-75-10). |
| BR-005 | Ảnh không hiển thị trên màn hình chờ (idle cover) và màn hình khách (visitor). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Chưa có ảnh khi chọn Save. | Nút Save không dùng được; ô Photo hiện “Photo required”. |
| VAL-002 | Ứng dụng không có quyền camera. | Hiện hướng dẫn bật quyền; không lưu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-149: UI-US-001 - Check in (ô Photo) | https://bba-attendance-visitor.lovable.app/ |
| BBA-149: UI-US-001 - Check out (ô Photo) | https://bba-attendance-visitor.lovable.app/ |
| BBA-149: UI-US-001 - Camera toàn màn hình | https://bba-attendance-visitor.lovable.app/ |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Photo | Ô ảnh / thao tác | Có | Trống; “Photo required” | FR-001;VAL-001 | Chạm để mở camera; hiện ảnh thu nhỏ khi đã chụp. |
| Shutter | Thao tác | — | — | FR-002 | Chụp ảnh. |
| Switch camera | Thao tác | — | Camera sau | FR-002 | Đổi camera trước / sau. |
| Retake / Use photo | Thao tác | — | Sau khi chụp | FR-002 | Chụp lại hoặc dùng ảnh. |
| Close | Thao tác | — | — | — | Đóng camera, không đổi ảnh hiện có. |
| Thông báo quyền camera | Thông điệp | — | Ẩn | VAL-002;BR-003 | Hướng dẫn và Open Settings. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Ảnh gắn với một bản ghi check-in hoặc check-out: mã bản ghi, loại (check-in / check-out), thời điểm chụp. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Nhân viên mở Check in cho Mia, chưa chụp ảnh | nhân viên xem nút Save | Save không dùng được; ô Photo hiện “Photo required” | FR-001;VAL-001 |
| AC-002 | Nhân viên đã chụp ảnh thứ nhất | nhân viên chọn Retake, chụp lại và Use photo | chỉ ảnh thứ hai gắn với bản ghi | FR-002 |
| AC-003 | Quyền camera của app đang tắt | nhân viên chạm ô Photo | hiện “Camera access is off. Turn it on in Settings › BBA Attendance.” và Open Settings; không lưu được | VAL-002;BR-003 |
| AC-004 | Bus A có 7 trẻ; nhân viên lọc theo Bus A | nhân viên check-in từng trẻ | mỗi trẻ có một bản ghi và một ảnh riêng; không có thao tác lưu chung cho cả xe | BR-004 |
| AC-005 | iPad chuyển sang màn hình chờ sau 2 phút không thao tác | màn hình chờ hiển thị | không có ảnh, tên trẻ | BR-005 |

#### Dependencies (Phụ thuộc)

Check-in / check-out của Attendance App; chọn người đưa / đón (BBA-150); nhiệt độ (BBA-151); BBA-73 US-002 (ghi trên SMS).

### 6.2 BBA-149: US-002 - Lưu và đồng bộ ảnh

#### User Story

Là Centre, tôi muốn ảnh bàn giao được lưu ngay cả khi mất mạng và tới SMS cùng bản ghi, để không mất bằng chứng và phụ huynh nhận ảnh khi con được nhận.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-003 | Hệ thống phải nén ảnh và xoá thông tin vị trí trước khi lưu. |
| FR-004 | Hệ thống phải lưu ảnh trên iPad cùng bản ghi trước, rồi đồng bộ cùng bản ghi lên SMS khi có mạng; xoá bản sao trên iPad sau khi đồng bộ thành công. |
| FR-005 | Hệ thống phải cho chụp lại ảnh của bản ghi chưa đồng bộ (Fix a mistake) và khoá ảnh của bản ghi đã đồng bộ. |
| FR-006 | Hệ thống phải gửi ảnh check-in trong thông báo check-in cho phụ huynh và hiển thị ảnh check-in, check-out ở Attendance của Parents App. |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên chọn Save. Hệ thống nén ảnh, xoá vị trí (FR-003) và lưu bản ghi cùng ảnh trên iPad với trạng thái Not synced (FR-004).
2. Khi có mạng, hệ thống đồng bộ bản ghi cùng ảnh lên SMS; trạng thái thành Synced và bản sao ảnh trên iPad bị xoá.
3. Khi bản ghi tới SMS, phụ huynh nhận thông báo check-in kèm giờ và ảnh (FR-006); ảnh hiển thị ở Attendance của Parents App và trên SMS (BBA-73).

#### Functional Flow - Alternative (Luồng thay thế)

1. Bản ghi Not synced bị sai ảnh: nhân viên chọn Fix a mistake, chụp lại và lưu; lịch sử sửa được giữ (FR-005).
2. Mất mạng nhiều giờ: bản ghi và ảnh nằm trong Sync queue; đồng bộ tự động khi có mạng hoặc khi nhân viên chọn Sync.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Đồng bộ lỗi: bản ghi hiện Sync error kèm lý do; nhân viên chọn Retry cho bản ghi đó.
2. Bản ghi đã Synced: không có thao tác đổi ảnh; sai thì gửi void request theo đặc tả Attendance App.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-006 | Ảnh lưu dạng JPEG, cạnh dài tối đa 1600 px, dung lượng tối đa 500 KB sau nén; không giữ thông tin vị trí (GPS). |
| BR-007 | Ảnh trên iPad chỉ nằm trong vùng lưu của app, không lưu vào thư viện ảnh của iPad, và bị xoá sau khi đồng bộ thành công. |
| BR-008 | Ảnh lưu trên SMS cùng bản ghi điểm danh. Thời gian lưu ảnh, người được xem / xuất ảnh và việc tự xoá khi hết hạn chờ BBA trả lời (OQ-01, Q-75-12); đến khi có quyết định, ảnh lưu theo bản ghi điểm danh. Truy cập ảnh qua đường dẫn có thời hạn tối đa 15 phút. |
| BR-009 | Thông báo check-in gửi khi bản ghi tới SMS, kèm giờ check-in thực tế và ảnh. Ảnh check-out hiển thị ở Attendance của Parents App; thông báo check-out nêu người đón (BBA-150). |
| BR-010 | Bản ghi Not synced được chụp lại ảnh; mỗi lần sửa lưu giá trị cũ, mới, thời điểm. Bản ghi Synced không đổi được ảnh trên iPad. |
| BR-011 | Không đăng xuất iPad khi còn bản ghi Not synced. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Ảnh sau nén vẫn lớn hơn 500 KB. | Hệ thống nén thêm đến khi đạt; không báo lỗi cho nhân viên. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-149: UI-US-002 - Sync queue | https://bba-attendance-visitor.lovable.app/queue |
| BBA-149: UI-US-002 - Ngày của trẻ (Fix a mistake) | https://bba-attendance-visitor.lovable.app/ |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Trạng thái đồng bộ | Nhãn | — | Not synced sau khi lưu | FR-004 | Synced / Not synced / Sync error. |
| Fix a mistake | Thao tác | — | Chỉ bản ghi Not synced | FR-005;BR-010 | Chụp lại ảnh và các trường khác. |
| Sync (n) | Thao tác | — | Số bản ghi chờ | FR-004 | Đồng bộ ngay. |
| Retry | Thao tác | — | Chỉ dòng Sync error | — | Đồng bộ lại bản ghi. |
| Ảnh trong thông báo | Hiển thị (Parents App) | — | — | FR-006;BR-009 | Ảnh check-in trong thông báo. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Lưu ảnh cùng bản ghi điểm danh trên SMS: ảnh, loại, thời điểm chụp, Centre, nguồn (Attendance App). Không lưu tên nhân viên chụp. |
| DATA-003 | Lưu lịch sử sửa ảnh của bản ghi trước đồng bộ theo BR-010. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-006 | iPad mất mạng | nhân viên check-in Mia có ảnh | bản ghi hiện Not synced; khi có mạng, bản ghi và ảnh đồng bộ, trạng thái Synced, bản sao trên iPad bị xoá | FR-004;BR-007 |
| AC-007 | Ảnh gốc 4 MB, có thông tin vị trí | ảnh được lưu | ảnh trên SMS ≤ 500 KB, cạnh dài ≤ 1600 px, không có vị trí | FR-003;BR-006 |
| AC-008 | Check-in của Mia lúc 08:10 tới SMS lúc 08:40 | bản ghi tới SMS | phụ huynh nhận thông báo check-in với giờ 08:10 và ảnh | FR-006;BR-009 |
| AC-009 | Check-in của Noah Not synced, ảnh chụp nhầm trẻ | nhân viên chọn Fix a mistake và chụp lại | bản ghi dùng ảnh mới; lịch sử có lần sửa | FR-005;BR-010 |
| AC-010 | Check-in của Liam đã Synced | nhân viên mở bản ghi | không có thao tác đổi ảnh | FR-005;BR-010 |
| AC-011 | Còn 3 bản ghi Not synced | Centre Admin chọn đăng xuất iPad | không cho đăng xuất | BR-011 |

#### Dependencies (Phụ thuộc)

US-001; Sync queue và void request (Attendance App); thông báo Parents App; hiển thị trên SMS (BBA-73).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Nguồn | Giả định đang dùng | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Ảnh bàn giao lưu bao lâu, ai được xem / xuất, hết hạn có tự xoá không? | Q-75-12 (P0) | Lưu theo bản ghi điểm danh; Centre và HQ xem theo quyền trên SMS; không tự xoá (BR-008). |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Ảnh bàn giao (Handover photo) | Ảnh trẻ cùng người đưa / người đón, chụp lúc check-in / check-out. |
| iPad tại cổng | iPad dùng chung đăng nhập bằng tài khoản Centre, chạy Attendance App. |
| Not synced / Synced / Sync error | Trạng thái đồng bộ của bản ghi trên iPad. |
| Fix a mistake | Sửa bản ghi chưa đồng bộ trên iPad. |
| Void request | Yêu cầu huỷ bản ghi đã đồng bộ, duyệt trên SMS. |
