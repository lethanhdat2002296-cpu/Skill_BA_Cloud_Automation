# BBA-78 Daily routines – view & edit (web) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Routines |
| Tính năng | Daily routines – view & edit (web) |
| Mã ticket | BBA-78 |
| Mã WBS | 3.2.3.01 |
| Mã tài liệu | FRD-BBA-78 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-78: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả màn xem và sửa sinh hoạt hằng ngày theo lớp và ngày trên SMS web, mục bắt buộc theo level, và cài đặt loại sinh hoạt nào phụ huynh được xem. 3 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

Giáo viên ghi sinh hoạt hằng ngày của trẻ (ăn, uống sữa, ngủ trưa, thay tã, đi vệ sinh). Centre Director và Centre Admin cần xem toàn lớp theo ngày trên máy tính, sửa khi ghi nhầm, biết trẻ nào còn thiếu mục bắt buộc, và quyết định loại sinh hoạt nào phụ huynh được xem trong Parents App.

Mục tiêu đo được: người dùng xem được sinh hoạt của cả lớp trong một ngày trên một màn hình; mọi lần sửa có người sửa và thời điểm.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Xem sinh hoạt theo lớp và ngày: bữa ăn, sữa, giấc ngủ, thay tã / đi vệ sinh, ghi chú từ gia đình. Ghi cho cả lớp rồi chỉnh từng trẻ. Sửa có lịch sử. Mục bắt buộc theo level và trẻ còn thiếu. Cài đặt loại sinh hoạt hiện cho phụ huynh. Xuất file. | Ghi sinh hoạt trên Teacher App. Thực đơn của bếp. Ghi nhận cho uống thuốc. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Teacher / Senior Teacher | Lớp của mình. | Ghi và sửa sinh hoạt của trẻ lớp mình. |
| Centre Director, Centre Admin / School Admin | Centre của mình. | Xem, sửa, xuất file. |
| HQ Admin | Mọi Centre. | Cài đặt mục bắt buộc và loại sinh hoạt hiện cho phụ huynh. |
| Phụ huynh (Parents App) | Con mình. | Xem sinh hoạt của con theo ngày, chỉ các loại được bật. |
| Hệ thống | Toàn hệ thống. | Tính thời gian ngủ, đánh dấu mục còn thiếu, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Daily operations › Daily routines | Xem, ghi, sửa sinh hoạt theo lớp và ngày; cài đặt hiển thị cho phụ huynh. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Xem và sửa sinh hoạt hằng ngày trên SMS web

#### User Story

Là Centre Director, tôi muốn xem sinh hoạt trong ngày của cả lớp, sửa khi giáo viên ghi nhầm và biết trẻ nào còn thiếu mục bắt buộc, để phụ huynh nhận được thông tin đầy đủ và đúng về ngày của con.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Màn Daily routines chọn lớp và ngày (mặc định hôm nay); mỗi trẻ một dòng gồm: bữa ăn (All / Most / Some / None cho từng bữa), sữa (ml pha, ml uống), giấc ngủ (giờ bắt đầu, giờ kết thúc, thời gian ngủ, chất lượng), thay tã / đi vệ sinh (Diaper, Potty, Accident; Wet, BM, Dry), ghi chú từ gia đình. |
| FR-002 | Tìm theo tên trẻ; lọc theo lớp, mục còn thiếu; sắp xếp theo tên trẻ hoặc giờ ghi gần nhất. |
| FR-003 | "Record for the class" ghi một mục cho mọi trẻ trong lớp cùng lúc, sau đó người dùng chỉnh riêng từng trẻ khác đi. |
| FR-004 | Thời gian ngủ do hệ thống tính từ giờ bắt đầu và giờ kết thúc. |
| FR-005 | Sửa một mục: đổi giờ hoặc chi tiết; lịch sử lưu giá trị cũ, giá trị mới, người sửa, thời điểm. |
| FR-006 | Mục bắt buộc được đặt theo level (mặc định Infant và Playgroup); trẻ còn thiếu mục bắt buộc trong ngày hiện chữ "Missing" kèm tên mục. |
| FR-007 | Cài đặt "Shown to parents": với mỗi loại sinh hoạt (bữa ăn, sữa, giấc ngủ, thay tã / đi vệ sinh) có bật / tắt hiện cho phụ huynh; loại bị tắt vẫn được ghi nhưng không hiện trong Parents App. |
| FR-008 | Phụ huynh chỉ thấy sinh hoạt của con mình, theo ngày, và chỉ các loại đang bật. Sửa một mục đã hiện cho phụ huynh thì phụ huynh thấy giá trị mới. |
| FR-009 | Xuất sinh hoạt theo khoảng ngày và lớp ra Excel. |
| FR-010 | Chỉ sửa được sinh hoạt trong giới hạn số ngày cho phép (AS-02); ngày sau hôm nay không ghi được. |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở Daily routines, chọn lớp và ngày (FR-001).
2. Centre Director lọc "mục còn thiếu", thấy trẻ thiếu giấc ngủ (FR-002, FR-006).
3. Centre Director nhắc giáo viên ghi bổ sung; giáo viên ghi trên màn này hoặc Teacher App.

#### Functional Flow - Alternative (Luồng thay thế)

1. Ghi bữa trưa cho cả lớp rồi chỉnh trẻ ăn ít (FR-003).
2. Sửa giờ ngủ ghi nhầm (FR-004, FR-005).
3. HQ Admin tắt loại "thay tã / đi vệ sinh" khỏi Parents App cho một level (FR-007).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Giờ kết thúc ngủ trước giờ bắt đầu: không lưu (VAL-001).
2. Sữa uống nhiều hơn sữa pha: không lưu (VAL-002).
3. Ngày ngoài giới hạn sửa: chỉ xem (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Mỗi mục ghi lưu người ghi; mỗi lần sửa lưu người sửa. |
| BR-002 | Phụ huynh chỉ thấy sinh hoạt của con mình. |
| BR-003 | Mục bắt buộc theo level; trẻ thiếu mục bắt buộc được đánh dấu trên màn lớp. |
| BR-004 | Tắt hiện cho phụ huynh không xoá dữ liệu; bật lại thì phụ huynh thấy lại. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Giờ kết thúc ngủ trước giờ bắt đầu. | Không lưu; hiện "The nap end time must be after the start time." |
| VAL-002 | Lượng sữa uống lớn hơn lượng sữa pha. | Không lưu; hiện "Amount drunk cannot be more than amount prepared." |
| VAL-003 | Ngày sau hôm nay hoặc ngoài giới hạn sửa. | Chỉ xem; không có nút ghi và sửa. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Daily routines — theo lớp và ngày | Chưa có wireframe trong đợt này. |
| SCR-02 - Cài đặt "Shown to parents" | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Lớp, ngày | Danh sách chọn, ngày | Có | Lớp của người dùng, hôm nay | VAL-003. | — |
| Bảng sinh hoạt | Bảng | Có | Mỗi trẻ một dòng | — | FR-001; FR-006. |
| Record for the class | Nút | Theo quyền | — | — | FR-003. |
| Giờ bắt đầu / kết thúc ngủ | Giờ | Khi ghi giấc ngủ | — | VAL-001. | Tính thời gian ngủ (FR-004). |
| Sữa pha / sữa uống (ml) | Số | Khi ghi sữa | — | VAL-002. | — |
| Shown to parents | Bật / tắt theo loại | Có | Bật | — | FR-007. |
| Export | Nút | Theo quyền | — | — | FR-009. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi mục sinh hoạt lưu: trẻ, ngày, loại, chi tiết, giờ, người ghi, thời điểm ghi. |
| DATA-002 | Mỗi lần sửa lưu giá trị cũ, giá trị mới, người sửa, thời điểm; mỗi lần đổi cài đặt hiển thị lưu người đổi và thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Bumblebees hôm nay có 16 trẻ | Centre Director mở Daily routines | mỗi trẻ một dòng với bữa ăn, sữa, giấc ngủ, thay tã, ghi chú từ gia đình | FR-001 |
| AC-002 | giáo viên ghi bữa trưa "All" cho cả lớp | giáo viên chỉnh Caleb thành "Some" | 15 trẻ "All", Caleb "Some" | FR-003 |
| AC-003 | giờ ngủ 13:00 đến 14:30 | lưu | thời gian ngủ hiện 1 giờ 30 phút | FR-004 |
| AC-004 | Centre Admin sửa giờ ngủ từ 13:00 thành 13:15 | lưu | lịch sử ghi 13:00 → 13:15, người sửa, thời điểm | FR-005; BR-001; DATA-002 |
| AC-005 | Playgroup bắt buộc ghi giấc ngủ, 2 trẻ chưa có | Centre Director lọc mục còn thiếu | 2 trẻ hiện "Missing: Nap" | FR-002; FR-006; BR-003 |
| AC-006 | HQ Admin tắt "Nappy and toilet" cho phụ huynh | phụ huynh mở sinh hoạt của con | không thấy mục thay tã; giáo viên vẫn ghi được | FR-007; BR-004 |
| AC-007 | phụ huynh của Caleb mở Parents App | xem sinh hoạt hôm nay | chỉ thấy sinh hoạt của Caleb | FR-008; BR-002 |
| AC-008 | giờ kết thúc ngủ 12:50, bắt đầu 13:00 | lưu | không lưu, hiện "The nap end time must be after the start time." | VAL-001 |
| AC-009 | sữa pha 150 ml | nhập sữa uống 180 ml | không lưu, hiện "Amount drunk cannot be more than amount prepared." | VAL-002 |
| AC-010 | ngày ngoài giới hạn sửa | Centre Admin mở ngày đó | chỉ xem, không có nút ghi và sửa | FR-010; VAL-003 |
| AC-011 | Centre Admin chọn lớp Bumblebees, tuần trước | chọn Export | file Excel có sinh hoạt của lớp trong tuần đó | FR-009 |

#### Dependencies (Phụ thuộc)

Teacher App (ghi sinh hoạt); ghi chú từ gia đình (Parents App); danh sách lớp; Parents App (xem sinh hoạt).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Cài đặt "Shown to parents" đặt theo level, theo Centre hay toàn brand; ai được đổi? | Centre Director / HQ Ops | Cao |  |
| OQ-02 | Được sửa sinh hoạt lùi về tối đa bao nhiêu ngày? | Centre Director / HQ Ops | Trung bình |  |
| OQ-03 | Phụ huynh có nhận thông báo khi một mục đã xem bị sửa không? | Centre Director / HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | HQ Admin đặt "Shown to parents" theo level. | FR-007 — chờ OQ-01 |
| AS-02 | Sửa được sinh hoạt trong 7 ngày gần nhất. | FR-010 — chờ OQ-02 |
| AS-03 | Sửa mục đã hiện cho phụ huynh không gửi thông báo. | FR-008 — chờ OQ-03 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Sinh hoạt hằng ngày | Bữa ăn, sữa, giấc ngủ, thay tã / đi vệ sinh của trẻ trong ngày. |
| Mục bắt buộc | Loại sinh hoạt giáo viên phải ghi mỗi ngày cho trẻ ở một level. |
| Diaper / Potty / Accident | Thay tã / đi bô / tè dầm; Wet / BM / Dry: ướt / đi nặng / khô. |
