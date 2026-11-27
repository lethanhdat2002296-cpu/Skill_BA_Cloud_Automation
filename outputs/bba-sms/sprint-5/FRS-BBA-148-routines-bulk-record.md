# Functional Requirements Specification — Routines – Bulk Record

**Dự án:** Busy Bees Asia SMS · **Module:** Teacher App — Teaching day · **Tính năng:** BBA-148 Routines – bulk record  
**Mã tài liệu:** FRD-4.2.1.04_Routines_Bulk_Record · **Sprint:** 5 · **Phiên bản:** 0.2 · **Trạng thái:** Bản nháp chờ xác nhận · **Ngày:** 27/11/2026  
**Người soạn:** Business Analysis · **Người review:** HaiNguyen · **Người duyệt:** HaiNguyen

## 1. Kiểm soát tài liệu

| Phiên bản | Ngày | Tác giả | Tóm tắt thay đổi | Duyệt |
|---|---|---|---|---|
| 0.1 | 26/11/2026 | Business Analysis | Khởi tạo | HaiNguyen |
| 0.2 | 27/11/2026 | Business Analysis | Bỏ Mood (Q-86-01, BBA-78); đồng bộ thông báo lỗi với BBA-78; thêm “Shown to parents”, sửa lùi ngày trên web, điều chỉnh trước / sau khi lưu; thêm Câu hỏi mở. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả đủ User Story, FR, quy tắc, kiểm tra, dữ liệu, tiêu chí nghiệm thu. Đã đối chiếu BBA-78 và bảng câu hỏi Sprint 4; 2 câu hỏi mở ở mục 7.

## 2. Mục đích và bối cảnh

Tài liệu đặc tả chức năng ghi routine trên Teacher App: giáo viên xem tình trạng routine của lớp trong ngày, ghi một routine (bữa ăn, bình sữa, giấc ngủ, thay tã / đi vệ sinh) cho cả lớp bằng một lần nhập rồi điều chỉnh riêng từng trẻ, sửa hoặc xoá routine đã ghi, và đọc Note from home của phụ huynh.

Mỗi trẻ được chọn nhận một routine riêng; phụ huynh chỉ thấy routine của con mình trên Parents App (BBA-146). Teacher App không điểm danh: danh sách trẻ có mặt lấy từ check-in tại cổng (Attendance App) hoặc SMS.

## 3. Phạm vi và ranh giới phase

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Tổng quan routine của lớp trong ngày; trẻ chưa có routine và thiếu routine bắt buộc; ghi routine cho cả lớp và điều chỉnh từng trẻ; giờ ngủ mặc định của lớp; đánh thức nhiều trẻ; sửa, xoá routine trong ngày; xem ngày của một trẻ; đọc Note from home; lưu lại khi mất mạng giữa chừng. | Điểm danh, nhiệt độ (Attendance App); xem routine của phụ huynh (BBA-146); cấu hình routine bắt buộc theo level, cài đặt “Shown to parents” và danh mục món ăn (SMS, BBA-78); báo cáo routine (SMS); ghi tắm; sửa routine của ngày trước (làm trên SMS web theo BBA-78). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Giáo viên (Teacher) | Lớp được phân công. | Xem, ghi, sửa, xoá routine trong ngày; đặt giờ ngủ mặc định của lớp; đọc Note from home. |
| Senior Teacher | Lớp được phân công. | Như Teacher. |
| System | Routine, lớp, phân công giáo viên, điểm danh trong ngày, Note from home. | Cung cấp danh sách trẻ có mặt; tạo một routine cho mỗi trẻ; tính thời gian từ lần ghi gần nhất và thời lượng ngủ; ghi lịch sử; cung cấp routine cho Parents App. |

## 5. Tổng quan tính năng và phân rã chức năng

BBA-148 gồm ba User Story trên Teacher App, đặc tả ở mục 6.

| Module | Tính năng | Mô tả | User Story |
|---|---|---|---|
| Teaching day | Tổng quan routine của lớp | Trẻ có mặt, routine đã ghi, trẻ chưa ghi, routine bắt buộc còn thiếu, Note from home chưa đọc. | BBA-148: US-001 |
| Teaching day | Ghi routine cho cả lớp | Nhập một lần, áp dụng cho nhiều trẻ, điều chỉnh từng trẻ; mỗi trẻ một routine. | BBA-148: US-002 |
| Teaching day | Sửa, xoá routine và đọc Note from home | Ngày của một trẻ: sửa, xoá routine trong ngày; đọc Note from home. | BBA-148: US-003 |

## 6. Yêu cầu chức năng theo User Story

### 6.1 BBA-148: US-001 - Tổng quan routine của lớp

#### User Story

Là giáo viên, tôi muốn thấy trong lớp trẻ nào đã có, trẻ nào chưa có routine hôm nay, để không bỏ sót trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống phải hiển thị danh sách trẻ đã check-in hôm nay của lớp đang chọn, kèm routine đã ghi của từng trẻ. |
| FR-002 | Hệ thống phải đánh dấu trẻ chưa có routine nào (To do) và trẻ thiếu routine bắt buộc theo level. |
| FR-003 | Hệ thống phải hiển thị thời gian từ lần ghi gần nhất của Meal, Bottle và Nappy / toilet cho từng trẻ. |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Routines. Hệ thống hiển thị lớp đang chọn ở bộ chuyển lớp (một lớp hoặc All my classes).
2. Hệ thống hiển thị số trẻ có mặt, số trẻ To do và danh sách trẻ đã check-in hôm nay, mỗi trẻ kèm biểu tượng routine đã ghi (FR-001; FR-002).
3. Giáo viên xem cảnh báo thiếu routine bắt buộc và thời gian từ lần ghi gần nhất (FR-003), chọn một trẻ để mở ngày của trẻ (US-003) hoặc chọn Record for the class (US-002).

#### Functional Flow - Alternative (Luồng thay thế)

1. All my classes: danh sách nhóm theo lớp; mỗi lớp có số trẻ có mặt và số To do.
2. Trẻ đã check-out: vẫn hiển thị với nhãn “Gone home” để sửa routine trong ngày.
3. Lớp chưa có trẻ check-in: hiển thị “No children checked in yet.”

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Không tải được dữ liệu: báo lỗi theo hành vi chuẩn, nút Try again.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-001 | Giáo viên chỉ thấy lớp được phân công. Danh sách gồm trẻ có check-in hôm nay; trẻ đang tạm nghỉ không hiển thị. |
| BR-002 | Trẻ To do: chưa có routine nào hôm nay. Routine bắt buộc theo level do HQ cấu hình (mặc định Infant và Playgroup: Lunch, Nap, Nappy / toilet); thiếu thì hiện “Missing: <routine>”. |
| BR-003 | Thời gian từ lần ghi gần nhất do hệ thống tính, ví dụ “3h 10m since the last bottle”; không nhập tay. |
| BR-004 | Trẻ có allergy hoặc bệnh lý có biểu tượng y tế cạnh tên. Trẻ có Note from home chưa đọc có dấu đánh dấu (US-003). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-001 | Yêu cầu dữ liệu của lớp không được phân công. | Không cung cấp dữ liệu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-148: UI-US-001 - Routines: tổng quan lớp | https://bba-teacher.lovable.app/routines |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Bộ chuyển lớp | Chọn | Có | Lựa chọn gần nhất | BR-001 | Một lớp hoặc All my classes. |
| Số trẻ có mặt / To do | Hiển thị | — | Theo lớp | FR-002;BR-002 | Ví dụ “10 here · 3 to do”. |
| Dòng trẻ | Danh sách | — | Trẻ đã check-in | FR-001;BR-004 | Ảnh, tên, biểu tượng y tế, biểu tượng routine đã ghi, dấu Note from home chưa đọc. |
| Missing | Nhãn | — | Ẩn | FR-002;BR-002 | “Missing: Lunch, Nap”. |
| Thời gian từ lần ghi gần nhất | Hiển thị | — | Theo trẻ | FR-003;BR-003 | Meal, Bottle, Nappy / toilet. |
| Gone home | Nhãn | — | Ẩn | — | Hiện khi trẻ đã check-out. |
| Record for the class | Thao tác | — | Luôn hiện | — | Mở luồng ghi cho cả lớp (US-002). |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Đọc phân công lớp, danh sách check-in / check-out hôm nay, cấu hình routine bắt buộc theo level, routine đã ghi và trạng thái đọc Note from home. Xem tổng quan không tạo dữ liệu. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-001 | Lớp Infant A có 12 trẻ, 10 trẻ đã check-in, chưa có routine | cô Priya mở Routines | hiện 10 trẻ và “10 here · 10 to do” | FR-001;FR-002 |
| AC-002 | Mia (Infant) đã có Lunch, chưa có Nap và Nappy / toilet | cô Priya xem dòng của Mia | hiện “Missing: Nap, Nappy / toilet” | FR-002;BR-002 |
| AC-003 | Bottle gần nhất của Leo lúc 09:00, hiện tại 12:10 | cô Priya xem dòng của Leo | hiện “3h 10m since the last bottle” | FR-003;BR-003 |
| AC-004 | Cô Priya dạy Nursery 2 và K1 Blue | cô chọn All my classes | danh sách nhóm theo hai lớp | BR-001 |
| AC-005 | Noah đã check-out lúc 15:00 | cô Priya xem danh sách | Noah có nhãn Gone home | FR-001 |

#### Dependencies (Phụ thuộc)

Phân công lớp (SMS); check-in / check-out (Attendance App, BBA-149/150); cấu hình routine bắt buộc (SMS); hồ sơ sức khoẻ của trẻ.

### 6.2 BBA-148: US-002 - Ghi routine cho cả lớp

#### User Story

Là giáo viên, tôi muốn ghi một routine cho cả lớp trong vài thao tác rồi chỉnh riêng trẻ khác biệt, để ghi nhanh mà vẫn đúng từng trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-004 | Hệ thống phải cho chọn loại routine, nhập form một lần và áp dụng cho nhiều trẻ của lớp. |
| FR-005 | Hệ thống phải chọn sẵn mọi trẻ đã check-in và chưa check-out; giáo viên bỏ chọn trẻ không áp dụng và chỉnh giá trị riêng cho từng trẻ. |
| FR-006 | Khi lưu, hệ thống phải tạo một routine riêng cho mỗi trẻ được chọn, ghi giáo viên đăng nhập là người ghi. |
| FR-007 | Hệ thống phải cho đặt giờ ngủ mặc định của lớp và đánh thức (ghi giờ kết thúc ngủ) cho nhiều trẻ cùng lúc. |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên chọn Record for the class rồi chọn loại: Meal, Bottle, Nap, Nappy / toilet (FR-004).
2. Giáo viên nhập form theo BR-006 một lần.
3. Hệ thống hiển thị danh sách trẻ đã check-in và chưa check-out, tất cả được chọn sẵn (FR-005). Giáo viên bỏ chọn trẻ không áp dụng, chỉnh giá trị trên dòng của trẻ khác biệt hoặc mở form đầy đủ cho trẻ đó.
4. Giáo viên chọn Save (N children). Hệ thống kiểm tra (VAL-002 đến VAL-006), tạo một routine cho mỗi trẻ (FR-006), hiển thị “<Routine> saved for N children” và quay lại tổng quan.

#### Functional Flow - Alternative (Luồng thay thế)

1. Nap: giờ bắt đầu mặc định theo giờ ngủ mặc định của lớp; để trống giờ kết thúc thì trẻ hiển thị “Sleeping”. Giáo viên chọn Wake up, chọn các trẻ đang ngủ và lưu: giờ kết thúc = thời điểm hiện tại (FR-007).
2. Ghi cho một trẻ (từ ngày của trẻ, US-003): form như trên, không có bước chọn trẻ; được thêm ảnh.
3. Sau khi lưu, trẻ khác biệt được chỉnh riêng ở ngày của trẻ (US-003); điều chỉnh làm được cả trước và sau khi lưu (Q-86-04).
4. Giáo viên chọn Cancel: không lưu.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Mất mạng khi lưu: routine đã lưu giữ nguyên; app liệt kê trẻ chưa lưu và nút Retry; Retry không tạo routine trùng (BR-009).
2. Dữ liệu không hợp lệ: báo lỗi tại trường, không lưu (VAL-002 đến VAL-006).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-005 | Mỗi trẻ được chọn nhận một routine riêng, chỉ phụ huynh của trẻ đó thấy. “Logged by” là giáo viên đăng nhập, không đổi được. |
| BR-006 | Phase 1 có 4 loại routine (Q-86-01, BBA-78). Trường theo loại: Meal – Time, Meal type (Breakfast / Morning snack / Lunch / Afternoon snack / Late snack), Amount eaten (All / Most / Some / None), Meal items; Bottle – Time, ml prepared, ml drunk; Nap – Start time, End time, Quality (Slept well / Disrupted sleep); Nappy / toilet – Time, Kind (Diaper / Potty / Accident), Result (Wet / BM / Dry). Mọi loại có Note (tuỳ chọn). |
| BR-007 | Time mặc định là thời điểm hiện tại, không sau thời điểm hiện tại và không trước giờ check-in của trẻ. Thời lượng ngủ = End time − Start time, do hệ thống tính. |
| BR-008 | Ảnh chỉ thêm khi ghi cho một trẻ; app báo “This photo will also appear in the child's album in the Parents App.” |
| BR-009 | Lưu theo từng trẻ: trẻ lưu thành công giữ nguyên khi trẻ khác lỗi. Mỗi lần lưu có mã để Retry không tạo routine trùng. |
| BR-010 | Giờ ngủ mặc định đặt theo lớp (ví dụ 12:00–14:00); mọi giáo viên của lớp sửa được. |
| BR-011 | Không ghi tắm (showering). |
| BR-016 | Giáo viên ghi được mọi loại routine, kể cả loại đang tắt “Shown to parents”; loại bị tắt không hiện cho phụ huynh (BBA-78 FR-007, BR-004). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-002 | Không trẻ nào được chọn. | Nút Save không dùng được; hiện “Select at least one child”. |
| VAL-003 | Thiếu trường bắt buộc theo loại (Meal type, Amount eaten, ml drunk, Start time, Kind, Result). | Báo trường bắt buộc, không lưu. |
| VAL-004 | End time không sau Start time. | Báo “The nap end time must be after the start time.”, không lưu (giống BBA-78 VAL-001). |
| VAL-005 | ml drunk lớn hơn ml prepared; hoặc ml ngoài 0–500. | Báo “Amount drunk cannot be more than amount prepared.” (giống BBA-78 VAL-002) hoặc “Enter an amount from 0 to 500 ml.”, không lưu. |
| VAL-006 | Time sau thời điểm hiện tại hoặc trước giờ check-in của trẻ. | Báo “Check the time: not before check-in or after now.”, không lưu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-148: UI-US-002 - Chọn loại routine | https://bba-teacher.lovable.app/routines |
| BBA-148: UI-US-002 - Form routine | https://bba-teacher.lovable.app/routines |
| BBA-148: UI-US-002 - Chọn trẻ và điều chỉnh | https://bba-teacher.lovable.app/routines |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Loại routine | Chọn | Có | — | FR-004 | Meal / Bottle / Nap / Nappy / toilet. |
| Time / Start time | Giờ | Có | Thời điểm hiện tại; Nap theo giờ ngủ mặc định | VAL-006;BR-007;BR-010 | Giờ của routine. |
| End time | Giờ | Không | Trống | VAL-004 | Trống = Sleeping. |
| Meal type / Amount eaten | Chọn | Có (Meal) | — | VAL-003 | Theo BR-006; Amount chỉnh được theo từng trẻ. |
| Meal items | Ô nhập | Không | Trống | — | Tối đa 200 ký tự. |
| ml prepared / ml drunk | Ô số | ml drunk: Có (Bottle) | Trống | VAL-003;VAL-005 | Số nguyên 0–500. |
| Quality | Chọn | Không | Trống | — | Slept well / Disrupted sleep. |
| Kind / Result | Chọn | Có (Nappy / toilet) | — | VAL-003 | Diaper / Potty / Accident; Wet / BM / Dry. |
| Note | Ô nhập | Không | Trống | — | Tối đa 500 ký tự; phụ huynh đọc được. |
| Photo | Ảnh | Không | Chỉ khi ghi cho một trẻ | BR-008 | Chụp hoặc chọn từ thư viện. |
| Danh sách trẻ | Danh sách chọn | Có | Mọi trẻ đã check-in, chưa check-out được chọn | FR-005;VAL-002 | Bỏ chọn; chỉnh giá trị trên dòng; mở form đầy đủ. |
| Save (N children) / Cancel | Thao tác | — | Save mờ khi không có trẻ | VAL-002 đến VAL-006 | Lưu một routine cho mỗi trẻ; Cancel đóng không lưu. |
| Wake up | Thao tác | — | Hiện khi có trẻ Sleeping | FR-007 | Ghi End time = hiện tại cho các trẻ được chọn. |
| Retry | Thao tác | — | Ẩn | BR-009 | Lưu lại cho trẻ chưa lưu. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-002 | Lưu mỗi routine một bản ghi: trẻ, lớp, loại, các trường theo BR-006, ghi chú, ảnh, người ghi, thời điểm ghi, mã lần lưu. |
| DATA-003 | Lưu giờ ngủ mặc định theo lớp và người cập nhật gần nhất. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-006 | Infant A có 10 trẻ đã check-in | cô Priya ghi Lunch “All” cho cả lớp, đổi Mia thành “Some” rồi Save | 9 trẻ có Lunch All, Mia có Some; mỗi routine “Logged by Priya”; mỗi phụ huynh chỉ thấy routine của con mình | FR-004;FR-005;FR-006;BR-005 |
| AC-007 | Form Nap có Start 13:00 | giáo viên nhập End 12:30 và Save | báo “The nap end time must be after the start time.”, không lưu | VAL-004 |
| AC-008 | Form Bottle | giáo viên để trống ml drunk và Save | báo trường bắt buộc, không lưu | VAL-003 |
| AC-009 | Giáo viên bỏ chọn tất cả trẻ | giáo viên xem nút Save | Save không dùng được, hiện “Select at least one child” | VAL-002 |
| AC-010 | Lưu Lunch cho 10 trẻ, 3 trẻ lỗi do mất mạng | giáo viên chọn Retry khi có mạng | 3 routine còn lại được tạo; mỗi trẻ có đúng một Lunch | BR-009 |
| AC-011 | Giờ ngủ mặc định của lớp là 12:00–14:00 | giáo viên ghi Nap cho cả lớp | Start time mặc định 12:00 | FR-007;BR-010 |
| AC-012 | 5 trẻ đang Sleeping | giáo viên chọn Wake up lúc 14:05 cho cả 5 trẻ | 5 Nap có End time 14:05 và thời lượng được tính | FR-007;BR-007 |
| AC-013 | Leo check-in lúc 08:30 | giáo viên ghi Meal cho Leo lúc 08:00 | báo “Check the time: not before check-in or after now.”, không lưu | VAL-006 |
| AC-019 | HQ Admin tắt “Nappy & toilet” cho phụ huynh | giáo viên ghi Nappy cho Mia | lưu thành công; phụ huynh của Mia không thấy mục này | BR-016 |
| AC-020 | Bottle có ml prepared 150 | giáo viên nhập ml drunk 180 và Save | báo “Amount drunk cannot be more than amount prepared.”, không lưu | VAL-005 |

#### Dependencies (Phụ thuộc)

US-001; Parents App hiển thị routine (BBA-146); thư viện ảnh của trẻ (Learning). Cài đặt “Shown to parents” (BBA-78).

### 6.3 BBA-148: US-003 - Sửa, xoá routine và đọc Note from home

#### User Story

Là giáo viên, tôi muốn sửa hoặc xoá routine ghi nhầm và đọc ghi chú của phụ huynh, để thông tin gửi phụ huynh luôn đúng và tôi chăm trẻ theo dặn dò của gia đình.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-008 | Hệ thống phải hiển thị ngày của một trẻ: mọi routine trong ngày theo giờ và Note from home. |
| FR-009 | Hệ thống phải cho giáo viên của lớp sửa, xoá routine trong ngày hiện tại của trẻ và ghi lịch sử. |
| FR-010 | Hệ thống phải đánh dấu Note from home chưa đọc cho đến khi giáo viên mở ngày của trẻ. |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên chọn một trẻ ở tổng quan. Hệ thống hiển thị ngày của trẻ: Note from home (nếu có) và routine theo giờ (FR-008); đánh dấu Note from home là đã đọc với giáo viên này (FR-010).
2. Giáo viên chọn một routine rồi Edit, sửa và Save. Hệ thống kiểm tra như US-002, lưu và ghi lịch sử (FR-009).
3. Giáo viên chọn Remove ở một routine và xác nhận. Hệ thống ẩn routine với phụ huynh và ghi lịch sử.

#### Functional Flow - Alternative (Luồng thay thế)

1. Giáo viên chọn Add ở ngày của trẻ: ghi routine cho một trẻ (US-002, được thêm ảnh).
2. Giáo viên huỷ xác nhận xoá: routine giữ nguyên.

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Routine thuộc ngày trước: chỉ xem, không có Edit, Remove; hiển thị “Edit past days on the SMS web.” (BR-013).
2. Không lưu được: báo lỗi theo hành vi chuẩn, giữ nội dung đang sửa.

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc |
|---|---|
| BR-012 | Mọi giáo viên được phân công lớp của trẻ được sửa, xoá routine của trẻ trong ngày hiện tại, kể cả routine giáo viên khác ghi. “Logged by” giữ nguyên; lưu thêm người sửa và thời điểm. Sửa không gửi thông báo cho phụ huynh (BBA-78 AS-03). |
| BR-013 | Routine của ngày trước chỉ xem trên Teacher App. Sửa lùi ngày (tối đa 7 ngày) làm trên SMS web theo BBA-78 FR-010. |
| BR-014 | Xoá cần xác nhận “Remove this entry? Parents will no longer see it.”. Routine đã xoá không hiện với phụ huynh, vẫn có trong lịch sử. |
| BR-015 | Note from home hiển thị dưới “From the family” kèm người viết và thời điểm; chỉ đọc. Trạng thái đã đọc tính theo từng giáo viên. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi của hệ thống |
|---|---|---|
| VAL-007 | Sửa routine với dữ liệu không hợp lệ. | Áp dụng VAL-003 đến VAL-006; không lưu. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| BBA-148: UI-US-003 - Ngày của trẻ | https://bba-teacher.lovable.app/routines |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| From the family | Khối hiển thị | — | Ẩn khi không có ghi chú | FR-010;BR-015 | Note from home, người viết, thời điểm; chỉ đọc. |
| Dòng routine | Danh sách | — | Sắp theo giờ | FR-008 | Loại, giờ, nội dung, ghi chú, ảnh, Logged by, Edited by. |
| Edit | Thao tác | — | Chỉ ngày hiện tại | FR-009;BR-012;BR-013 | Mở form sửa. |
| Remove | Thao tác | — | Chỉ ngày hiện tại | FR-009;BR-014 | Xác nhận rồi xoá. |
| Add | Thao tác | — | Chỉ ngày hiện tại | — | Ghi routine cho trẻ này. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Ghi lịch sử sửa, xoá routine: giá trị cũ / mới, người thao tác, thời điểm. Xoá là ẩn, không xoá vật lý. |
| DATA-005 | Lưu trạng thái đã đọc Note from home theo giáo viên và ghi chú. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given (Cho trước) | When (Khi) | Then (Thì) | Linked Rule |
|---|---|---|---|---|
| AC-014 | Cô Priya ghi Lunch “All” cho Mia | cô Lan (cùng lớp) sửa thành “Some” | routine hiện Some, “Logged by Priya”, “Edited by Lan <giờ>” | FR-009;BR-012 |
| AC-015 | Bottle 10:00 của Mia ghi nhầm | giáo viên Remove và xác nhận | phụ huynh không còn thấy Bottle 10:00; lịch sử có người xoá và thời điểm | FR-009;BR-014;DATA-004 |
| AC-016 | Mẹ Chloe viết “She slept late last night” | cô Priya mở Routines | dòng Chloe có dấu ghi chú chưa đọc | FR-010 |
| AC-017 | Như AC-016 | cô Priya mở ngày của Chloe | ghi chú hiện dưới From the family với người viết, thời điểm, không sửa được; dấu chưa đọc biến mất với cô Priya, vẫn còn với cô Lan | FR-010;BR-015 |
| AC-018 | Mia có routine hôm qua | giáo viên mở routine đó | chỉ xem, không có Edit, Remove | BR-013 |

#### Dependencies (Phụ thuộc)

US-001; US-002; Note from home (BBA-146); Daily routines trên SMS web (BBA-78).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Nguồn | Giả định đang dùng | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Trẻ vắng mặt hoặc nghỉ phép có được áp dụng khi ghi cho cả lớp không? | Q-86-04 | Không: danh sách chỉ gồm trẻ đã check-in, chưa check-out (FR-005). |  |
| OQ-02 | Có cho ghi routine lùi ngày hoặc cho ngày tương lai trên Teacher App không? | Q-86-06; BBA-78 OQ-02 | Không ghi ngày tương lai; ngày trước chỉ sửa trên SMS web trong 7 ngày (BR-013). |  |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Routine | Một hoạt động chăm sóc ghi cho một trẻ. Phase 1: Meal, Bottle, Nap, Nappy / toilet. |
| Record for the class | Ghi một routine cho nhiều trẻ của lớp bằng một lần nhập. |
| To do | Trẻ đã check-in nhưng chưa có routine nào trong ngày. |
| Routine bắt buộc | Routine mỗi trẻ của level cần có trong ngày, do HQ cấu hình. |
| Logged by | Giáo viên ghi routine; là người đăng nhập, không đổi được. |
| Note from home | Ghi chú phụ huynh gửi trong ngày (BBA-146). |
| Shown to parents | Cài đặt trên SMS bật / tắt từng loại routine hiện cho phụ huynh (BBA-78). |
