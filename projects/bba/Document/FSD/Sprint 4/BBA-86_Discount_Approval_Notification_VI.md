# BBA-86 Rebate & discount – approve / reject + in-app result notification (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Fees & Payments — Settings › Items, discounts & general |
| Tính năng | Rebate & discount – approve / reject + in-app result notification |
| Mã ticket | BBA-86 |
| Mã WBS | 3.6.8.03 |
| Mã tài liệu | FRD-BBA-86 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-86: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với BBA Finance. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc duyệt / từ chối đơn giảm giá (Pending, Approved, Rejected) theo tuyến duyệt, áp giảm giá sau khi duyệt và thông báo kết quả cho người gửi trong app. 2 câu hỏi mở ở mục 7 cần BBA Finance chốt.

## 2. Mục tiêu và bối cảnh

Centre gửi đơn xin giảm giá (rebate / discount) cho một trẻ. Đơn đi qua Centre Director rồi Finance theo tuyến duyệt; mỗi cấp duyệt hoặc từ chối có lý do. Người gửi luôn biết kết quả qua thông báo trong app; giảm giá chỉ được áp vào lịch phí sau khi được duyệt.

Mục tiêu đo được: 100% đơn có kết quả được báo cho người gửi; 0 giảm giá được áp khi chưa duyệt xong.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Danh sách đơn giảm giá theo trạng thái Pending, Approved, Rejected. Duyệt, từ chối có lý do, theo tuyến duyệt. Áp giảm giá đã duyệt vào lịch phí của trẻ. Thông báo kết quả cho người gửi. Lịch sử. | Tạo loại giảm giá và mã khuyến mãi. Giảm giá duyệt sẵn (theo chiến dịch / mã khuyến mãi) — không cần duyệt. Thiết lập tuyến duyệt (Administration). |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Centre Admin / School Admin, Centre Director (người gửi) | Centre của mình. | Gửi đơn giảm giá cho trẻ; nhận kết quả. |
| Centre Director (cấp 1) | Centre của mình. | Duyệt / từ chối theo tuyến duyệt. |
| HQ Finance (cấp 2) | Quốc gia / pháp nhân. | Duyệt / từ chối theo tuyến duyệt. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Hệ thống | Toàn hệ thống. | Chuyển đơn theo tuyến, áp giảm giá, gửi thông báo, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Finance approvals › Discount | Duyệt đơn giảm giá và thông báo kết quả. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Duyệt đơn giảm giá và báo kết quả

#### User Story

Là Centre Admin, tôi muốn đơn giảm giá tôi gửi cho trẻ được duyệt theo đúng tuyến và tôi nhận thông báo kết quả, để báo lại cho phụ huynh mà không phải hỏi Finance.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Đơn giảm giá gồm: trẻ, loại giảm giá, số tiền hoặc phần trăm, ngày bắt đầu, ngày kết thúc, lý do, tệp đính kèm (không bắt buộc), người gửi; trạng thái Pending khi gửi. |
| FR-002 | Đơn đi theo tuyến duyệt đã cấu hình cho loại "Discount" (mặc định Centre Director rồi Finance); cấp 2 chỉ mở sau khi cấp 1 duyệt. |
| FR-003 | Người duyệt chọn Approve hoặc Reject; Reject bắt buộc lý do. Đơn bị từ chối ở bất kỳ cấp nào chuyển Rejected và kết thúc. |
| FR-004 | Khi cấp cuối duyệt, đơn chuyển Approved và giảm giá được áp vào lịch phí của trẻ từ ngày bắt đầu đến ngày kết thúc. |
| FR-005 | Người gửi nhận thông báo trong app khi đơn được duyệt hoặc bị từ chối: tên trẻ, loại giảm giá, kết quả, lý do (khi từ chối), người quyết định. |
| FR-006 | Danh sách đơn giảm giá: trẻ, Centre, loại, số tiền / %, ngày bắt đầu – kết thúc, người gửi, ngày gửi, trạng thái, cấp đang chờ; lọc theo trạng thái, Centre; tìm theo tên trẻ. |
| FR-007 | Người đã duyệt cấp 1 không duyệt cấp 2 của cùng đơn. |
| FR-008 | Lịch sử đơn: gửi, từng cấp duyệt / từ chối, lý do, người, thời điểm. |

#### Functional Flow - Main (Luồng chính)

1. Centre Admin gửi đơn giảm giá cho trẻ (FR-001).
2. Centre Director duyệt cấp 1; Finance duyệt cấp 2 (FR-002, FR-003).
3. Giảm giá được áp vào lịch phí (FR-004); Centre Admin nhận thông báo (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Bị từ chối ở cấp 1 hoặc cấp 2: đơn Rejected, người gửi nhận lý do (FR-003, FR-005).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Từ chối không có lý do: không lưu (VAL-001).
2. Ngày kết thúc trước ngày bắt đầu, hoặc phần trăm ngoài 0–100: không gửi được (VAL-002).
3. Cấp 2 mở đơn chưa qua cấp 1: không có nút duyệt (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Giảm giá cần duyệt đi qua Centre Director rồi Finance theo tuyến duyệt. |
| BR-002 | Từ chối phải có lý do; người gửi luôn được báo kết quả. |
| BR-003 | Giảm giá chỉ được áp sau khi cấp cuối duyệt. |
| BR-004 | Hai cấp của cùng đơn do hai người khác nhau duyệt. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Từ chối không có lý do. | Không lưu; hiện "Enter a reason. The requester sees it in the notification." |
| VAL-002 | Ngày kết thúc trước ngày bắt đầu; phần trăm ngoài 0–100; số tiền âm. | Không gửi được; đánh dấu ô lỗi. |
| VAL-003 | Cấp trước chưa duyệt. | Không có Approve / Reject cho cấp sau. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Finance approvals — Discount | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Loại giảm giá | Danh sách chọn | Có | — | — | Chỉ loại "Needs approval". |
| Số tiền / % | Số | Có | — | VAL-002. | — |
| Ngày bắt đầu / kết thúc | Ngày | Có | — | VAL-002. | — |
| Lý do, tệp đính kèm | Ô nhập, tệp | Lý do: có | — | — | — |
| Approve, Reject | Nút | Người duyệt cấp đang chờ | — | VAL-001; VAL-003. | FR-003. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi đơn lưu mọi trường, trạng thái, từng cấp duyệt (người, kết quả, lý do, thời điểm), tuyến duyệt đã dùng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Centre Admin gửi đơn giảm 10% từ 01/01 đến 31/03/2027 | xem danh sách | đơn ở Pending, cấp đang chờ là Centre Director | FR-001; FR-006 |
| AC-002 | Centre Director duyệt cấp 1 | Finance mở đơn | Finance có Approve / Reject | FR-002; BR-001 |
| AC-003 | Finance duyệt cấp 2 | xem lịch phí của trẻ | giảm 10% áp từ 01/01 đến 31/03/2027; đơn Approved | FR-004; BR-003 |
| AC-004 | Finance duyệt | Centre Admin mở thông báo | thấy tên trẻ, loại giảm giá, Approved, người duyệt | FR-005; BR-002 |
| AC-005 | Centre Director từ chối với lý do | Centre Admin mở thông báo | thấy Rejected và lý do; đơn kết thúc, không lên Finance | FR-003; FR-005 |
| AC-006 | từ chối không lý do | lưu | không lưu, hiện "Enter a reason. The requester sees it in the notification." | VAL-001 |
| AC-007 | đơn đang chờ cấp 1 | Finance mở đơn | không có Approve / Reject | VAL-003 |
| AC-008 | người A duyệt cấp 1 và cũng có quyền Finance | A mở đơn ở cấp 2 | không có Approve / Reject cho A | FR-007; BR-004 |
| AC-009 | ngày kết thúc 01/01, ngày bắt đầu 01/02 | gửi đơn | không gửi được, ô ngày bị đánh dấu | VAL-002 |
| AC-010 | đơn đã qua 2 cấp | mở lịch sử | thấy gửi, cấp 1, cấp 2 với người, kết quả, thời điểm | FR-008; DATA-001 |

#### Dependencies (Phụ thuộc)

Loại giảm giá (Discounts & promo codes); tuyến duyệt (Administration); Finance approvals; lịch phí (BBA-80); thông báo trong app.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | "Rebate" khác "discount" thế nào (ví dụ hoàn lại sau khi đã thu)? Có cần trạng thái hay cách áp riêng không? | BBA Finance | Cao |  |
| OQ-02 | Phụ huynh có nhận thông báo khi giảm giá được duyệt không? | BBA Finance | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Rebate và discount dùng chung luồng duyệt này. | FR-001 — chờ OQ-01 |
| AS-02 | Chỉ người gửi nhận thông báo kết quả; phụ huynh không nhận. | FR-005 — chờ OQ-02 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Giảm giá cần duyệt | Giảm giá phải qua tuyến duyệt, khác giảm giá duyệt sẵn theo chiến dịch / mã khuyến mãi. |
| Tuyến duyệt | Thiết lập ai duyệt cấp 1, cấp 2 cho từng loại yêu cầu. |
