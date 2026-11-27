# Functional Requirements Specification — Gate Temperature Entry

**Dự án:** Busy Bees Asia SMS · **Module:** Attendance App (gate iPad) — Kiosk · **Tính năng:** BBA-151 Gate temperature entry  
**Mã tài liệu:** FRD-4.4.1.05_Gate_Temperature_Entry · **Sprint:** 5 · **Phiên bản:** 0.2 · **Trạng thái:** Bản nháp chờ xác nhận · **Ngày:** 27/11/2026  
**Người soạn:** Business Analysis · **Người review:** HaiNguyen · **Người duyệt:** HaiNguyen

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 26/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 27/11/2026 | Business Analysis | Bỏ mô tả kết nối thiết bị đo; thêm nút chọn nhanh 36.3–36.7 (Q-76-05); Round bắt buộc cấu hình theo Centre (Q-81-02); check-in xe bus từng trẻ (Q-75-10); thêm Câu hỏi mở. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu. Đã đối chiếu bảng câu hỏi Sprint 4; 2 câu hỏi mở ở mục 7.

## 2. Mục đích và bối cảnh

Tài liệu đặc tả việc nhập nhiệt độ của trẻ trên Attendance App (iPad tại cổng): nhập nhiệt độ bắt buộc khi check-in, thêm lần đo trong ngày, cảnh báo khi nhiệt độ từ ngưỡng sốt trở lên, và đồng bộ lần đo vào ngày của trẻ trên SMS.

Lần đo trên iPad là nguồn dữ liệu cho tab Temperature trên SMS (BBA-74). Round, khoảng giá trị và Measurement method dùng đúng quy tắc của BBA-74.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Nhiệt độ bắt buộc khi check-in (Round On arrival); thêm lần đo Before nap, After nap, Before pickup, Extra; chọn giá trị bằng bộ chọn, nút chọn nhanh hoặc Enter manually; giá trị tự điền từ thiết bị đo được phép sửa; tô đỏ và cảnh báo nhiệt độ từ ngưỡng sốt; xem các lần đo trong ngày; lưu trên iPad và đồng bộ. | Quản lý lần đo trên SMS (BBA-74); nhiệt độ nhân viên khi chấm công (Staff attendance); cấu hình ngưỡng sốt và Round bắt buộc (SMS); kết nối, ghép nối và giao tiếp với thiết bị đo (không mô tả trong FRD này); phụ huynh xem nhiệt độ (Parents App Attendance); đo nhiệt độ trên Teacher App (đã huỷ, BBA-147); đơn vị °F. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Nhân viên tại cổng | Trẻ của Centre theo phạm vi iPad. | Nhập nhiệt độ khi check-in; thêm lần đo trong ngày. |
| Giáo viên chủ nhiệm, Centre Director | Lớp / Centre của trẻ. | Nhận cảnh báo nhiệt độ từ ngưỡng sốt. |
| System | Lần đo nhiệt độ, ngưỡng sốt theo quốc gia, bản ghi điểm danh. | Kiểm tra dữ liệu; tô đỏ và gửi cảnh báo; lưu trên iPad và đồng bộ lên SMS. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-151 gồm hai User Story trên Attendance App, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| Kiosk | Nhiệt độ khi check-in | Nhập nhiệt độ bắt buộc khi check-in; cảnh báo sốt. | BBA-151: US-001 |
| Kiosk | Thêm lần đo trong ngày | Thêm lần đo theo Round; xem các lần đo trong ngày của trẻ. | BBA-151: US-002 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-151: US-001 - Nhiệt độ khi check-in

#### User Story

Là nhân viên tại cổng, tôi muốn ghi nhiệt độ mỗi trẻ khi nhận trẻ và được báo ngay khi trẻ sốt, để Centre xử lý kịp thời.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải yêu cầu một lần đo nhiệt độ cho mỗi lần check-in; lần đo này có Round = On arrival. |
| FR-002 | Hệ thống phải cho nhập nhiệt độ bằng bộ chọn, nút chọn nhanh 36.3–36.7 °C hoặc Enter manually; giá trị được điền tự động từ thiết bị đo vẫn sửa được (Q-76-05, Q-76-06). |
| FR-003 | Lần đo từ ngưỡng sốt trở lên phải được tô đỏ và gửi cảnh báo cho giáo viên chủ nhiệm và Centre Director. |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên mở Check in của trẻ. Ô Temperature hiển thị bộ chọn với giá trị mặc định 36.5 °C và các nút chọn nhanh 36.3, 36.4, 36.5, 36.6, 36.7 (FR-001; FR-002).
2. Nhân viên đo trẻ và chọn giá trị trên nút chọn nhanh, bộ chọn, hoặc chọn Enter manually và nhập. Centre có thiết bị đo thì giá trị được điền sẵn (Measurement method = Device) (FR-002).
3. Nhân viên chọn người đưa (BBA-150), chụp ảnh (BBA-149) và Save. Hệ thống kiểm tra (VAL-001, VAL-002) và lưu lần đo cùng bản ghi check-in.

#### Functional Flow - Alternative (Luồng thay thế)

1. Nhiệt độ từ ngưỡng sốt trở lên: ô Temperature tô đỏ; khi Save, hệ thống hỏi xác nhận theo BR-005; nhân viên chọn Save and alert thì lưu và gửi cảnh báo (FR-003).
2. Nhân viên sửa giá trị được điền sẵn từ thiết bị: Measurement method đổi thành Manual (Q-76-06).
3. Trẻ đi xe bus: lọc theo xe để gom danh sách; mỗi trẻ check-in và nhập nhiệt độ riêng (Q-75-10).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Giá trị không hợp lệ: báo lỗi tại trường, không lưu (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Mỗi check-in có đúng một lần đo Round = On arrival. Không có nhiệt độ thì không lưu check-in. |
| BR-002 | Temperature nhận 36.0–40.0 °C, bước 0.1 (thang không cần dưới 36, phải lên được 39–40, Q-76-05). Bộ chọn mặc định 36.5 °C; nút chọn nhanh 36.3–36.7. Measurement method: Device khi giá trị được điền từ thiết bị đo và không sửa; Manual trong trường hợp khác. |
| BR-003 | Ngưỡng sốt cấu hình theo quốc gia trên SMS, mặc định 37.5 °C (chờ OQ-01); iPad chỉ đọc. Lần đo từ ngưỡng trở lên tô đỏ trên form, thẻ trẻ và ngày của trẻ. |
| BR-004 | Cảnh báo sốt gửi giáo viên chủ nhiệm (push Teacher App) và Centre Director (in-app SMS, Centre Director App) khi lần đo tới SMS; gồm tên trẻ, lớp, nhiệt độ, Round, thời điểm. |
| BR-005 | Lưu lần đo từ ngưỡng sốt cần xác nhận: “<giá trị>°C is at or above <ngưỡng>°C. Save and alert the class teacher and Centre Director?” với Save and alert / Check again. |
| BR-006 | Màu đỏ chỉ dùng cho nhiệt độ từ ngưỡng sốt (cùng lỗi đồng bộ theo Attendance App). |
| BR-007 | Time của lần đo là giờ check-in. Không ghi, không hiển thị nhân viên đo. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Chưa có nhiệt độ khi Save check-in. | Nút Save không dùng được; ô Temperature hiện “Temperature required”. |
| VAL-002 | Nhiệt độ không phải số, ngoài 36.0–40.0 °C hoặc không theo bước 0.1. | Báo “Check the temperature: 36.0–40.0°C, step 0.1.” và không lưu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-151: UI-US-001 - Check in (Temperature) | https://bba-attendance-visitor.lovable.app/ |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Temperature | Bộ chọn số | Có | 36.5 °C | FR-001;BR-002;VAL-001 | Chọn 36.0–40.0, bước 0.1; tô đỏ khi từ ngưỡng sốt. |
| Nút chọn nhanh | Chip | — | 36.3 / 36.4 / 36.5 / 36.6 / 36.7 | FR-002;BR-002 | Chạm để chọn giá trị. |
| Enter manually | Thao tác / ô số | — | Ẩn | VAL-002 | Nhập tay giá trị. |
| Measurement method | Hiển thị | — | Manual | BR-002 | Device / Manual, do hệ thống xác định. |
| Xác nhận sốt | Hộp thoại | — | Ẩn | BR-005 | Save and alert / Check again. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Lưu lần đo là một bản ghi riêng gắn với trẻ và bản ghi check-in: Round On arrival, Temperature, Time, Measurement method, nguồn ghi Attendance App, Centre, lớp. Đồng bộ vào tab Temperature của SMS (BBA-74). |
| DATA-002 | Lưu cảnh báo sốt đã gửi: lần đo, người nhận, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Nhân viên mở Check in cho Mia | nhân viên chưa nhập nhiệt độ | Save không dùng được; ô Temperature hiện “Temperature required” | FR-001;VAL-001 |
| AC-002 | Centre có thiết bị đo; giá trị 36.6 được điền sẵn cho Mia | nhân viên giữ nguyên và Save | lần đo 36.6, Measurement method Device | FR-002;BR-002 |
| AC-003 | Như AC-002 | nhân viên sửa thành 36.7 | Measurement method thành Manual | BR-002 |
| AC-004 | Ngưỡng sốt 37.5 °C | nhân viên nhập 37.8 cho Noah và Save | ô tô đỏ; hỏi xác nhận; chọn Save and alert thì lưu; giáo viên chủ nhiệm và Centre Director nhận cảnh báo khi lần đo tới SMS | FR-003;BR-003;BR-004;BR-005 |
| AC-005 | Nhân viên nhập tay 3.6 | nhân viên chọn Save | báo “Check the temperature: 36.0–40.0°C, step 0.1.”, không lưu | VAL-002 |
| AC-006 | iPad mất mạng | nhân viên check-in Noah với 38.0 | ô tô đỏ ngay trên iPad; cảnh báo gửi khi lần đo tới SMS | BR-003;BR-004 |
| AC-007 | Mia check-in lúc 08:10 với 36.6 | lần đo tới SMS | tab Temperature trên SMS có lần đo On arrival 36.6 lúc 08:10 | DATA-001;BR-007 |
| AC-014 | Nhân viên mở Check in cho Leo | nhân viên chạm nút 36.4 | ô Temperature là 36.4, Measurement method Manual | FR-002;BR-002 |

#### Dependencies (Phụ thuộc)

Check-in (Attendance App); BBA-149; BBA-150; ngưỡng sốt theo quốc gia (SMS); tab Temperature (BBA-74); thông báo Teacher App và Centre Director App.

### 6.2 BBA-151: US-002 - Thêm lần đo trong ngày

#### User Story

Là nhân viên, tôi muốn thêm các lần đo nhiệt độ trong ngày cho trẻ, để đủ số lần đo Centre yêu cầu và theo dõi khi trẻ có dấu hiệu bất thường.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Hệ thống phải cho thêm lần đo cho trẻ đã check-in hôm nay với Round: Before nap, After nap, Before pickup, Extra. |
| FR-005 | Round = Extra phải có lý do đo thêm. |
| FR-006 | Hệ thống phải hiển thị mọi lần đo trong ngày của trẻ theo thời gian; Centre có cấu hình Round bắt buộc thì hiển thị số Round bắt buộc đã có (x of N). |

#### Functional Flow - Main (Luồng chính)

1. Nhân viên chọn trẻ rồi Add temperature reading.
2. Nhân viên chọn Round, nhập nhiệt độ như US-001, Time mặc định là thời điểm hiện tại (FR-004).
3. Nhân viên chọn Save. Hệ thống kiểm tra (VAL-002 đến VAL-005), lưu lần đo trên iPad và đồng bộ.
4. Ngày của trẻ hiển thị mọi lần đo theo giờ với Round, nhiệt độ, Measurement method; Centre có Round bắt buộc thì hiển thị “x of N” (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Round = Extra: nhân viên nhập lý do, ví dụ “Child felt warm” (FR-005).
2. Nhiệt độ từ ngưỡng sốt: xác nhận và cảnh báo như US-001 (BR-003 đến BR-005).
3. Lần đo chưa đồng bộ nhập sai: nhân viên chọn Fix a mistake, sửa và lưu; lịch sử sửa được giữ.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ chưa check-in hoặc đã check-out: không có Add temperature reading (VAL-005).
2. Lần đo đã đồng bộ: không sửa trên iPad; sửa trên SMS theo BBA-74.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-008 | Round: On arrival (tự động khi check-in), Before nap, After nap, Before pickup, Extra. Round bắt buộc cấu hình theo Centre trên SMS: Centre đo 3 lần dùng On arrival, After nap, Before pickup (Q-81-02); Centre không cấu hình thì chỉ On arrival bắt buộc. “x of N” đếm số Round bắt buộc đã có lần đo. |
| BR-009 | Không giới hạn số lần đo trong ngày; mỗi lần đo một bản ghi, kể cả cùng Round. |
| BR-010 | Time không trước giờ check-in và không sau thời điểm hiện tại; chỉ thêm cho trẻ đã check-in và chưa check-out hôm nay. |
| BR-011 | Lần đo chưa đồng bộ được sửa trên iPad; mỗi lần sửa lưu giá trị cũ, mới, thời điểm. Lần đo đã đồng bộ không sửa trên iPad. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-003 | Chưa chọn Round. | Báo trường bắt buộc, không lưu. |
| VAL-004 | Round = Extra và lý do trống. | Báo “Enter why this extra reading was taken.”, không lưu. |
| VAL-005 | Trẻ chưa check-in / đã check-out hoặc Time ngoài khoảng ở BR-010. | Báo “Check the time: not before check-in or after now.” hoặc không hiện thao tác thêm; không lưu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-151: UI-US-002 - Add temperature reading | https://bba-attendance-visitor.lovable.app/ |
| BBA-151: UI-US-002 - Ngày của trẻ (Temperature readings) | https://bba-attendance-visitor.lovable.app/ |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Add temperature reading | Thao tác | — | Chỉ trẻ đã check-in, chưa check-out | FR-004;VAL-005 | Mở form thêm lần đo. |
| Round | Chọn | Có | Trống | VAL-003;BR-008 | Before nap / After nap / Before pickup / Extra. |
| Temperature | Bộ chọn số | Có | 36.5 °C | VAL-002;BR-002 | Như US-001. |
| Time | Giờ | Có | Thời điểm hiện tại | VAL-005;BR-010 | Giờ đo. |
| Lý do đo thêm | Ô nhập | Khi Round = Extra | Ẩn | VAL-004 | Tối đa 200 ký tự. |
| Save / Cancel | Thao tác | — | — | VAL-002 đến VAL-005 | Lưu hoặc đóng không lưu. |
| Temperature readings | Danh sách | — | Theo giờ | FR-006;BR-009 | Round, nhiệt độ (đỏ khi sốt), Time, Measurement method, lý do. |
| x of N | Hiển thị | — | Ẩn khi Centre không cấu hình Round bắt buộc | FR-006;BR-008 | Số Round bắt buộc đã có lần đo. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Lưu mỗi lần đo một bản ghi: trẻ, Round, Temperature, Time, Measurement method, lý do đo thêm, nguồn Attendance App; đồng bộ vào tab Temperature của SMS (BBA-74). Lưu lịch sử sửa trước đồng bộ theo BR-011. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-008 | Centre của Mia cấu hình 3 Round bắt buộc; Mia có On arrival 36.6 và After nap 36.8 | nhân viên xem ngày của Mia | hiện 2 lần đo theo giờ và “2 of 3” | FR-006;BR-008 |
| AC-009 | Mia có 3 lần đo | nhân viên thêm Extra 37.8, lý do “Child felt warm”, chọn Save and alert | hiện 4 lần đo, lần thứ tư tô đỏ; giáo viên chủ nhiệm và Centre Director nhận cảnh báo | FR-004;FR-005;BR-004;BR-009 |
| AC-010 | Round = Extra, lý do trống | nhân viên chọn Save | báo “Enter why this extra reading was taken.”, không lưu | VAL-004 |
| AC-011 | Leo check-in lúc 08:30 | nhân viên thêm lần đo với Time 08:00 | báo “Check the time: not before check-in or after now.”, không lưu | VAL-005;BR-010 |
| AC-012 | Ava đã check-out | nhân viên mở Ava | không có Add temperature reading | VAL-005 |
| AC-013 | Lần đo Before nap của Noah chưa đồng bộ, nhập 36.0 thay vì 36.9 | nhân viên chọn Fix a mistake và sửa 36.9 | lần đo là 36.9; lịch sử có lần sửa | BR-011 |
| AC-015 | Centre của Leo không cấu hình Round bắt buộc; Leo có On arrival 36.5 | nhân viên xem ngày của Leo | hiện 1 lần đo, không có “x of N” | FR-006;BR-008 |

#### Dependencies (Phụ thuộc)

US-001; check-in / check-out (Attendance App); tab Temperature (BBA-74). Cấu hình Round bắt buộc theo Centre (SMS).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Nguồn | Giả định đang dùng | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Ngưỡng sốt bao nhiêu; có khác nhau giữa các quốc gia không? | Chưa có trong bảng câu hỏi Sprint 4 | 37.5 °C cho mọi quốc gia, cấu hình được trên SMS (BR-003). |  |
| OQ-02 | Nhập tay ngoài 36.0–40.0 °C thì cảnh báo cho lưu hay chặn? | Q-76-05 | Chặn, báo lỗi theo VAL-002. |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Lần đo (Reading) | Một lần đo nhiệt độ của trẻ; mỗi lần đo một bản ghi. |
| Round | Thời điểm đo: On arrival, Before nap, After nap, Before pickup, Extra. |
| Round bắt buộc | Round Centre yêu cầu đo mỗi ngày, cấu hình theo Centre; Centre đo 3 lần: On arrival, After nap, Before pickup. |
| Measurement method | Device (giá trị điền từ thiết bị đo, không sửa) hoặc Manual. |
| Ngưỡng sốt | Nhiệt độ cấu hình theo quốc gia (mặc định 37.5 °C); từ ngưỡng trở lên tô đỏ và cảnh báo. |
