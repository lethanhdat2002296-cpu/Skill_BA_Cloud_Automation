# BBA-73 Handover recording (dropped off by / picked up by) (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Daily Operations — Attendance |
| Tính năng | Handover recording (dropped off by / picked up by) |
| Mã ticket | BBA-73 |
| Mã WBS | 3.2.1.01 |
| Mã tài liệu | FRD-BBA-73 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-73: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả việc ghi người đưa trẻ đến và người đón trẻ về, kiểm tra người đón theo danh sách đã duyệt và trường hợp người đón không có trong danh sách. 4 câu hỏi mở ở mục 7, trong đó OQ-01 cần chốt trước khi phát triển.

## 2. Mục tiêu và bối cảnh

Mỗi lần nhận trẻ buổi sáng và trả trẻ buổi chiều, Centre phải biết ai đưa trẻ đến, ai đón trẻ về và lúc mấy giờ. Khi trả trẻ, nhân viên phải chắc chắn người đón có trong danh sách người được phép đón mà phụ huynh đã đăng ký và Centre đã duyệt.

Mục tiêu đo được: 100% lượt nhận và trả trẻ có ghi người đưa / người đón và giờ; không lượt trả trẻ nào cho người ngoài danh sách được lưu mà không có xác nhận của Centre Director.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Ghi người đưa trẻ đến khi nhận trẻ: phụ huynh, người được phép đón trong danh sách, hoặc "Other" kèm ghi chú. Ghi người đón khi trả trẻ, chọn từ danh sách người được phép đón đã duyệt. Hiện ảnh và giấy tờ của người đón để đối chiếu. Xử lý người đón không có trong danh sách. Giờ nhận và giờ trả. | Phụ huynh thêm người được phép đón trong Parents App và Centre duyệt (Children & Families). Ghi phí đón muộn. Nhận diện khuôn mặt, quét mã. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Centre Admin / School Admin, Teacher | Centre / lớp của mình. | Nhận và trả trẻ, ghi người đưa / người đón trên SMS web hoặc ứng dụng điểm danh ở cổng. |
| Centre Director | Centre của mình. | Như trên; xử lý trường hợp người đón không có trong danh sách (OQ-01). |
| Phụ huynh (Parents App) | Con mình. | Nhận thông báo khi con được nhận và được đón. |
| Hệ thống | Toàn hệ thống. | Lấy danh sách người được phép đón, kiểm tra người đón, lưu giờ và người thực hiện. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Daily operations › Class attendance | Ghi người đưa và người đón khi nhận / trả trẻ. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Ghi người đưa trẻ đến và người đón trẻ về

#### User Story

Là nhân viên ở cổng, khi nhận và trả trẻ tôi muốn chọn nhanh người đưa / người đón từ danh sách của trẻ và được hệ thống chặn nếu người đón không có trong danh sách, để trẻ chỉ được giao cho đúng người.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Khi nhận trẻ, nhân viên chọn người đưa trẻ đến từ danh sách gồm phụ huynh và người được phép đón đã duyệt của trẻ, hoặc chọn "Other" và nhập ghi chú bắt buộc (họ tên và quan hệ với trẻ). |
| FR-002 | Khi trả trẻ, nhân viên chọn người đón từ danh sách người được phép đón đã duyệt (gồm cả phụ huynh). Mỗi người hiện ảnh, họ tên, quan hệ với trẻ và 4 ký tự cuối của số giấy tờ để nhân viên đối chiếu. |
| FR-003 | Người phụ huynh đã thêm nhưng Centre chưa duyệt hiện với chữ "Pending approval" và không chọn được khi trả trẻ. |
| FR-004 | Khi người đến đón không có trong danh sách, nhân viên chọn "Not on the list"; hệ thống không cho trả trẻ và hiện hướng dẫn "Do not release the child. Call the parent and the Centre Director." |
| FR-005 | Giờ nhận và giờ trả mặc định là giờ hiện tại; nhân viên sửa được trong cùng ngày; giờ trả không được trước giờ nhận. |
| FR-006 | Bảng điểm danh của lớp có cột "Dropped off by" và "Picked up by" ghi tên người và giờ. |
| FR-007 | Thông báo nhận trẻ và trả trẻ gửi cho phụ huynh ghi tên người đưa / người đón và giờ. |
| FR-008 | Trẻ đi xe đưa đón được nhận cả nhóm; người đưa ghi là tên tuyến xe. Khi trả, mỗi trẻ được trả riêng và vẫn phải chọn người đón theo FR-002. |
| FR-009 | Mỗi lượt nhận / trả lưu người đưa / người đón, giờ, ghi chú, nhân viên thực hiện và thiết bị dùng (SMS web hoặc ứng dụng điểm danh). |

#### Functional Flow - Main (Luồng chính)

1. Buổi sáng, nhân viên chọn trẻ, chọn người đưa (FR-001), lưu giờ nhận (FR-005).
2. Buổi chiều, nhân viên chọn trẻ, chọn người đón, đối chiếu ảnh và giấy tờ (FR-002), lưu giờ trả (FR-005).
3. Phụ huynh nhận thông báo có tên người đưa / người đón (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. Người đưa không có trong danh sách: chọn "Other" và ghi chú (FR-001).
2. Trẻ đi xe: nhận theo tuyến xe, trả từng trẻ (FR-008).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Người đón không có trong danh sách: không trả trẻ, gọi phụ huynh và Centre Director (FR-004; VAL-002).
2. Người đón đang chờ duyệt: không chọn được (FR-003).
3. Giờ trả trước giờ nhận: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Trẻ chỉ được trả cho người có trong danh sách người được phép đón đã duyệt. |
| BR-002 | Người mới phải được phụ huynh thêm trong Parents App và Centre duyệt trước khi đón trẻ. |
| BR-003 | Người đưa trẻ đến được ghi theo người thật sự đưa trẻ, không phải nhân viên bấm nút. |
| BR-004 | Lượt nhận / trả đã lưu không bị xoá; sửa giờ hoặc người phải có lý do (BBA-77). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chọn "Other" khi nhận trẻ nhưng không nhập ghi chú. | Không lưu; hiện "Enter the name and relationship of the adult." |
| VAL-002 | Chọn "Not on the list" khi trả trẻ. | Không lưu lượt trả; hiện "Do not release the child. Call the parent and the Centre Director." |
| VAL-003 | Giờ trả trước giờ nhận, hoặc giờ sau thời điểm hiện tại. | Không lưu; hiện "Check the time." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Class attendance — nhận / trả trẻ | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Người đưa trẻ đến | Danh sách chọn | Có | Trống | VAL-001. | Phụ huynh, người được phép đón, "Other". |
| Ghi chú (Other) | Ô nhập | Khi chọn Other | Trống | VAL-001. | — |
| Người đón | Danh sách chọn có ảnh | Có | Trống | VAL-002. | Chỉ người đã duyệt; có "Not on the list". |
| Giờ nhận / giờ trả | Giờ | Có | Giờ hiện tại | VAL-003. | — |
| Dropped off by, Picked up by | Cột bảng | — | — | — | FR-006. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi lượt nhận / trả lưu: trẻ, loại (nhận / trả), người đưa hoặc người đón, ghi chú, giờ, nhân viên thực hiện, thiết bị. |
| DATA-002 | Mỗi lần chọn "Not on the list" được lưu: trẻ, giờ, nhân viên, để Centre Director xem lại. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | bà ngoại của Ethan có trong danh sách người được phép đón | nhân viên nhận Ethan và chọn bà ngoại | lượt nhận lưu "bà ngoại" và giờ hiện tại; cột Dropped off by hiện tên bà và giờ | FR-001; FR-005; FR-006 |
| AC-002 | hàng xóm đưa trẻ đến, không có trong danh sách | nhân viên chọn "Other" và ghi "Mrs Tan, neighbour" | lượt nhận được lưu kèm ghi chú | FR-001; BR-003 |
| AC-003 | nhân viên chọn "Other" nhưng để trống ghi chú | chọn lưu | không lưu, hiện "Enter the name and relationship of the adult." | VAL-001 |
| AC-004 | chú của trẻ có trong danh sách đã duyệt | nhân viên trả trẻ | danh sách hiện ảnh, họ tên, quan hệ, 4 ký tự cuối giấy tờ của chú; chọn chú thì lượt trả được lưu | FR-002; BR-001 |
| AC-005 | người đến đón không có trong danh sách | nhân viên chọn "Not on the list" | không trả trẻ; hiện "Do not release the child. Call the parent and the Centre Director."; hệ thống lưu lại lần này | FR-004; VAL-002; DATA-002 |
| AC-006 | phụ huynh vừa thêm cô của trẻ, Centre chưa duyệt | nhân viên mở danh sách người đón | cô của trẻ hiện "Pending approval" và không chọn được | FR-003; BR-002 |
| AC-007 | trẻ được nhận lúc 08:12 | nhân viên sửa giờ trả thành 07:50 | không lưu, hiện "Check the time." | FR-005; VAL-003 |
| AC-008 | bố đón trẻ lúc 17:40 | lượt trả được lưu | phụ huynh nhận thông báo có tên người bố và giờ 17:40 | FR-007 |
| AC-009 | 6 trẻ đi xe tuyến A đến trường | nhân viên nhận cả xe | 6 lượt nhận ghi người đưa là "tuyến A" | FR-008 |
| AC-010 | lượt nhận lưu trên ứng dụng điểm danh ở cổng | Centre Director xem lịch sử | thấy người đưa, giờ, nhân viên, thiết bị | FR-009; DATA-001; BR-004 |

#### Dependencies (Phụ thuộc)

Danh sách người được phép đón (Children & Families); ứng dụng điểm danh ở cổng; thông báo trong Parents App; sửa điểm danh có lý do (BBA-77).

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Khi người đón không có trong danh sách, có cho Centre Director trả trẻ sau khi gọi điện xác nhận với phụ huynh (ghi lại tên người xác nhận) không, hay tuyệt đối không trả? | Centre Director / HQ Ops | Cao |  |
| OQ-02 | Khi nhận trẻ, người đưa có bắt buộc là người trong danh sách không, hay "Other" luôn được phép? | Centre Director / HQ Ops | Trung bình |  |
| OQ-03 | Thông báo cho phụ huynh có cần ghi tên người đưa / người đón không? | Centre Director / HQ Ops | Thấp |  |
| OQ-04 | Trẻ đi xe về nhà: người đón ghi là tài xế / người phụ trách xe hay phụ huynh ở điểm trả? | Centre Director / HQ Ops | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Hệ thống chặn trả trẻ cho người ngoài danh sách, không chỉ cảnh báo. | FR-004; BR-001 — chờ OQ-01 |
| AS-02 | "Other" chỉ dùng khi nhận trẻ, không dùng khi trả trẻ. | FR-001 — chờ OQ-02 |
| AS-03 | Thông báo cho phụ huynh có tên người đưa / người đón. | FR-007 — chờ OQ-03 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Danh sách người được phép đón | Những người phụ huynh đăng ký trong Parents App (ảnh, họ tên, quan hệ, số giấy tờ, số điện thoại) và Centre đã duyệt. |
| Ứng dụng điểm danh | Ứng dụng trên máy tính bảng ở cổng Centre dùng để nhận và trả trẻ. |
