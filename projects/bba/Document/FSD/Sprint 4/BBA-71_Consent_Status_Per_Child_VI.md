# BBA-71 Consent status per child & send consent request (Tiếng Việt)

| Thuộc tính | Giá trị |
|---|---|
| Dự án | Busy Bees Asia SMS |
| Module | Children & Families — Documents & consents |
| Tính năng | Consent status per child & send consent request |
| Mã ticket | BBA-71 |
| Mã WBS | 3.1.4.01 |
| Mã tài liệu | FRD-BBA-71 |
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
| 0.1 | 10/11/2026 | Business Analysis | Bản đầu cho ticket BBA-71: quy tắc nghiệp vụ, trường hợp đặc biệt và tiêu chí nghiệm thu để chốt với vận hành Centre (Centre Director) và HQ Ops. | HaiNguyen |

**Mức sẵn sàng:** Đã đặc tả bảng trạng thái consent của từng trẻ, gửi và nhắc phụ huynh, ghi nhận câu trả lời, phiên bản và hết hạn. 5 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.

## 2. Mục tiêu và bối cảnh

Centre cần biết với từng trẻ: phụ huynh đã đồng ý những gì (ví dụ cho phép dùng ảnh của trẻ, cho trẻ đi tham quan), chưa trả lời những gì, và gửi hoặc nhắc lại ngay từ hồ sơ trẻ. Mỗi câu trả lời được lưu kèm phụ huynh nào trả lời, ngày nào, qua kênh nào.

Mục tiêu đo được: từ hồ sơ trẻ, nhân viên thấy trạng thái của mọi loại consent trong một bảng và gửi lại yêu cầu bằng một thao tác.

## 3. Phạm vi

| Trong phạm vi | Ngoài phạm vi |
|---|---|
| Bảng consent của từng trẻ: loại consent, phiên bản, trạng thái, ngày gửi, số lần nhắc, ngày trả lời, người trả lời, kênh trả lời. Gửi yêu cầu, nhắc lại, gửi lại khi đã hết hạn hoặc phụ huynh không đồng ý. Ghi nhận câu trả lời và việc rút lại consent. | Soạn biểu mẫu consent và gửi cho cả lớp / Centre (Communication › Surveys & consents). Khảo sát có thu phí. |

## 4. Tác nhân, vai trò và quyền truy cập

| Tác nhân | Phạm vi | Quyền / Trách nhiệm |
|---|---|---|
| Centre Director, School Admin | Centre của mình. | Xem; gửi, nhắc, gửi lại yêu cầu consent (theo quyền, mặc định bật cho Centre Director). |
| Teacher | Lớp của mình. | Xem trạng thái consent của trẻ lớp mình. |
| HQ Admin | Mọi Centre. | Mọi quyền. |
| Phụ huynh / người giám hộ | Con mình. | Đồng ý hoặc không đồng ý, ký khi biểu mẫu yêu cầu; rút lại consent khi biểu mẫu cho phép. |
| Hệ thống | Toàn hệ thống. | Gửi yêu cầu, đếm số lần nhắc, chuyển trạng thái hết hạn, lưu lịch sử. |

## 5. Tổng quan tính năng

| Khu vực | Chức năng | User Story |
|---|---|---|
| Hồ sơ trẻ › Documents & consents | Trạng thái consent của trẻ, gửi và nhắc yêu cầu. | US-001 |

## 6. Yêu cầu chức năng

### 6.1 US-001 - Trạng thái consent của từng trẻ và gửi yêu cầu

#### User Story

Là Centre Director, tôi muốn thấy trạng thái từng loại consent của một trẻ và gửi hoặc nhắc phụ huynh ngay tại hồ sơ trẻ, để trước mỗi hoạt động (chụp ảnh, tham quan) tôi biết chắc phụ huynh đã đồng ý.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hồ sơ trẻ có bảng consent, mỗi dòng một loại consent đang dùng: tên, phiên bản, trạng thái, ngày gửi, hạn trả lời, số lần nhắc, ngày trả lời, người trả lời, kênh trả lời (Parents App hoặc email). |
| FR-002 | Trạng thái của mỗi dòng là một trong: Not sent (chưa gửi), Awaiting reply (đã gửi, chờ trả lời), Agreed (đồng ý), Declined (không đồng ý), Expired (hết hạn), Withdrawn (phụ huynh đã rút lại). |
| FR-003 | "Send request" ở dòng Not sent gửi yêu cầu cho phụ huynh của trẻ: phụ huynh có tài khoản Parents App nhận thông báo trong app; phụ huynh chưa có tài khoản nhận email có đường dẫn trả lời. Trạng thái chuyển sang Awaiting reply. |
| FR-004 | "Remind" ở dòng Awaiting reply gửi lại thông báo, tăng số lần nhắc thêm 1 và ghi ngày nhắc. Hệ thống tự nhắc 1 ngày trước hạn trả lời; lần nhắc tự động cũng được đếm. |
| FR-005 | Khi một phụ huynh trả lời, hệ thống lưu câu trả lời, chữ ký (nếu biểu mẫu yêu cầu), tên phụ huynh, ngày giờ và kênh; mỗi trẻ chỉ cần một câu trả lời cho mỗi phiên bản. |
| FR-006 | Khi nội dung consent được đổi thành phiên bản mới, dòng của trẻ hiện phiên bản mới với trạng thái Not sent; câu trả lời cho phiên bản cũ vẫn xem được trong lịch sử. |
| FR-007 | Dòng Agreed chuyển sang Expired khi consent hết thời hạn hiệu lực; dòng Awaiting reply chuyển sang Expired khi quá hạn trả lời mà chưa có câu trả lời. |
| FR-008 | "Send again" ở dòng Declined hoặc Expired tạo một yêu cầu mới với hạn trả lời mới; câu trả lời cũ giữ trong lịch sử. |
| FR-009 | Khi phụ huynh rút lại consent (biểu mẫu cho phép rút), dòng chuyển sang Withdrawn; câu đồng ý ban đầu và việc rút lại đều được giữ; người tạo biểu mẫu và Centre Director nhận thông báo. |
| FR-010 | Chọn một dòng mở lịch sử của loại consent đó: mọi lần gửi, nhắc, trả lời, rút lại, kèm ngày giờ và người thực hiện. |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở hồ sơ trẻ, xem bảng consent (FR-001, FR-002).
2. Ở dòng Not sent, Centre Director chọn Send request (FR-003).
3. Phụ huynh trả lời trong Parents App; hệ thống lưu câu trả lời (FR-005).

#### Functional Flow - Alternative (Luồng thay thế)

1. Phụ huynh chưa trả lời: Centre Director chọn Remind; hệ thống tự nhắc 1 ngày trước hạn (FR-004).
2. Phụ huynh không đồng ý hoặc consent hết hạn: Centre Director chọn Send again (FR-007, FR-008).
3. Consent có phiên bản mới: gửi lại cho phiên bản mới (FR-006).
4. Phụ huynh rút lại consent (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ không có phụ huynh nào có tài khoản Parents App hay email: không gửi được (VAL-001).
2. Người dùng không có quyền gửi consent: không có nút gửi (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Câu trả lời ghi rõ phụ huynh nào trả lời, ngày giờ, kênh và chữ ký khi biểu mẫu yêu cầu. |
| BR-002 | Câu trả lời cho phiên bản cũ không thay cho phiên bản mới. |
| BR-003 | Câu trả lời cũ và việc rút lại không bao giờ bị xoá. |
| BR-004 | Quyền gửi consent theo Roles & permissions; mặc định bật cho HQ Admin và Centre Director, tắt cho Teacher. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Trẻ không có phụ huynh nào có tài khoản Parents App hoặc email. | Không gửi; hiện "No guardian of this child can receive the request. Add an email or invite a guardian to the Parents App." |
| VAL-002 | Người dùng không có quyền gửi consent. | Không hiển thị Send request, Remind, Send again. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình | Tham chiếu |
|---|---|
| SCR-01 - Hồ sơ trẻ — Documents & consents | Chưa có wireframe trong đợt này. |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Bảng consent | Bảng | Có | Mỗi loại consent một dòng | — | FR-001; FR-002. |
| Send request | Nút | Theo quyền | Dòng Not sent | VAL-001; VAL-002. | FR-003. |
| Remind | Nút | Theo quyền | Dòng Awaiting reply | VAL-002. | FR-004. |
| Send again | Nút | Theo quyền | Dòng Declined, Expired | VAL-001; VAL-002. | FR-008. |
| Lịch sử | Cửa sổ chi tiết | — | Đóng | — | FR-010. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Mỗi yêu cầu consent lưu: trẻ, loại consent, phiên bản, người gửi, ngày gửi, hạn trả lời, số lần nhắc và ngày nhắc, trạng thái. |
| DATA-002 | Mỗi câu trả lời lưu: câu trả lời, chữ ký, phụ huynh, ngày giờ, kênh; việc rút lại lưu thêm ngày giờ rút. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | trẻ chưa được gửi consent dùng ảnh | Centre Director chọn Send request | phụ huynh có Parents App nhận thông báo; dòng chuyển Awaiting reply, có ngày gửi | FR-001; FR-002; FR-003 |
| AC-002 | dòng đang Awaiting reply, đã nhắc 1 lần | Centre Director chọn Remind | số lần nhắc là 2 và có ngày nhắc mới | FR-004 |
| AC-003 | hạn trả lời là 20/11 | đến ngày 19/11, phụ huynh chưa trả lời | hệ thống tự nhắc và số lần nhắc tăng 1 | FR-004 |
| AC-004 | mẹ của trẻ đồng ý trong Parents App và ký | Centre Director mở bảng consent | dòng hiện Agreed, tên người mẹ, ngày giờ, kênh Parents App | FR-005; BR-001; DATA-002 |
| AC-005 | trẻ đã Agreed phiên bản 1 | consent được đổi thành phiên bản 2 | dòng hiện phiên bản 2, trạng thái Not sent; câu trả lời phiên bản 1 vẫn có trong lịch sử | FR-006; BR-002 |
| AC-006 | dòng Awaiting reply quá hạn trả lời | ngày sau hạn | dòng chuyển Expired và có nút Send again | FR-007; FR-008 |
| AC-007 | phụ huynh đã rút lại consent dùng ảnh | Centre Director mở bảng | dòng hiện Withdrawn; lịch sử có cả câu đồng ý và việc rút lại; Centre Director đã nhận thông báo | FR-009; BR-003 |
| AC-008 | trẻ không có phụ huynh nào có Parents App hay email | Centre Director chọn Send request | hiện "No guardian of this child can receive the request. …" | VAL-001 |
| AC-009 | Teacher mở hồ sơ trẻ lớp mình | xem bảng consent | thấy trạng thái, không có nút gửi | VAL-002; BR-004 |
| AC-010 | phụ huynh chưa có Parents App nhưng có email | Centre Director chọn Send request | phụ huynh nhận email có đường dẫn trả lời; câu trả lời ghi kênh Email | FR-003; FR-005 |
| AC-011 | dòng đã có 3 lần gửi và nhắc | Centre Director chọn dòng | lịch sử hiện đủ 3 lần với ngày giờ, người thực hiện | FR-010 |

#### Dependencies (Phụ thuộc)

Communication › Surveys & consents (biểu mẫu consent, hạn trả lời, cho phép rút lại); danh sách phụ huynh của trẻ; Parents App; dịch vụ email.

## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Danh sách loại consent mỗi trẻ phải có (ví dụ dùng ảnh / PDPA, tham quan, bơi…) là gì; theo brand hay chung? | Centre Director / HQ Ops | Cao |  |
| OQ-02 | "Expired" nghĩa là hết thời hạn hiệu lực của consent (ví dụ hết năm học) hay quá hạn trả lời, hay cả hai? Thời hạn hiệu lực của từng loại? | Centre Director / HQ Ops | Cao |  |
| OQ-03 | Khi consent có phiên bản mới, câu đồng ý phiên bản cũ còn hiệu lực đến khi phụ huynh trả lời phiên bản mới không? | Business Owner | Cao |  |
| OQ-04 | Có giới hạn số lần nhắc không? | Centre Director / HQ Ops | Thấp |  |
| OQ-05 | Phụ huynh trả lời qua email có cần ký không? | Business Owner | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Thêm trạng thái Withdrawn cho consent phụ huynh đã rút lại. | FR-002; FR-009 |
| AS-02 | Phụ huynh chưa có Parents App nhận yêu cầu qua email. | FR-003 |
| AS-03 | Expired dùng cho cả hai trường hợp: hết thời hạn hiệu lực và quá hạn trả lời. | FR-007 — chờ OQ-02 |
| AS-04 | Câu trả lời phiên bản cũ không thay cho phiên bản mới. | FR-006; BR-002 — chờ OQ-03 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Consent | Sự đồng ý của phụ huynh cho một việc cụ thể, ví dụ cho phép dùng ảnh của trẻ hoặc cho trẻ đi tham quan. |
| Phiên bản | Lần sửa nội dung của một loại consent; mỗi phiên bản cần câu trả lời riêng. |
| PDPA | Luật bảo vệ dữ liệu cá nhân. |
