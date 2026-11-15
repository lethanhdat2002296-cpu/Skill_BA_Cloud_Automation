# [Nháp] BBA-66 Child Record Overview — FR rút gọn

> Nháp để review, **chưa đưa lên Drive / Git**. Gốc: bản Drive `15Z5jLzL…` (v0.3, user sửa 14/11/2026).
> Nguyên tắc (theo góp ý của chị Hải): FR chỉ nói **hệ thống làm gì**, một câu; chi tiết quy tắc chuyển sang **Business Rules**; những thứ cơ bản (thứ tự tab, ô trống hiện "—", định dạng ngày / tuổi, câu ghi chú dưới trường) **bỏ khỏi FR** — đã có ở UI Components và wireframe.
> Mã giữ nguyên để truy vết; mã bỏ **không dùng lại**.

## US-001 — Header hồ sơ trẻ

| FR ID | Yêu cầu chức năng (nháp mới) | So với bản hiện tại |
|---|---|---|
| FR-001 | Header hiển thị họ tên, lớp và biểu tượng cảnh báo y tế của trẻ, kèm nút Actions. | Rút gọn; ví dụ lớp và "—" chuyển sang UI Components. |
| FR-002 | Hiển thị biểu tượng cảnh báo y tế cạnh tên khi trẻ có dị ứng hoặc bệnh. | Rút gọn; ai thấy biểu tượng / chi tiết → BR-012. |
| ~~FR-003~~ | — | **Bỏ** — thứ tự tab là cơ bản, thể hiện ở wireframe. |
| FR-004 | Người dùng có quyền cập nhật ảnh của trẻ. | Viết lại cho rõ. **Mâu thuẫn:** mục 3 ghi "Tải và đổi ảnh trẻ" là ngoài phạm vi → chọn giữ FR (và sửa mục 3) hoặc bỏ FR. |

**BR mới:** BR-012 — Biểu tượng cảnh báo y tế hiện với mọi vai trò xem được hồ sơ; chi tiết tình trạng chỉ xem ở tab Health với vai trò được phép (BR-CHF-024, BR-CHF-025).

## US-002 — Thông tin tổng quan của trẻ (Identity)

| FR ID | Yêu cầu chức năng (nháp mới) | So với bản hiện tại |
|---|---|---|
| FR-005 | Tab Overview hiển thị thông tin định danh và thông tin quản trị hồ sơ của trẻ (danh sách trường ở UI Components). | Rút gọn; bỏ liệt kê 11 trường. |
| ~~FR-006~~ | — | **Bỏ** — "in tên IC trên hoá đơn" đã là BR-005; câu ghi chú nằm ở UI Components. |
| ~~FR-007~~ | — | **Bỏ** — ngày sinh kèm tuổi là định dạng hiển thị → UI Components. |
| ~~FR-008~~ | — | **Bỏ** — câu ghi chú → UI Components; ý nghĩa đã là BR-003. |
| ~~FR-009~~ | — | **Chuyển** thành BR-013. |
| FR-010 | Payment method chỉ đọc, lấy từ Fees & Payments. | Rút gọn; câu ghi chú → UI Components. |
| ~~FR-011~~ | — | **Bỏ** — đã là BR-004 (phương thức theo quốc gia). |
| ~~FR-012~~ | — | **Bỏ** — ô trống hiện "—" là quy ước chung. |
| FR-013 | Hồ sơ tạo từ Lead nhận sẵn các trường Lead có; trường còn thiếu được bổ sung trên hồ sơ trẻ. | Rút gọn; bảng chép trường → BR-014, nguồn tạo → DATA-005. Bỏ câu "Owner trên header" (header không còn Owner). |

**BR mới:**
- BR-013 — Citizenship chọn trong danh mục theo quốc gia của Centre; Singapore: Singapore Citizen, Singapore PR, Foreigner (Malaysia chờ OQ-OVW-05).
- BR-014 — Khi tạo từ Lead, hệ thống chép một lần: tên trẻ → Name; Date of birth; Gender; Nationality; Parent / Guardian → primary contact ở tab Guardians.

## US-003 — Che số giấy tờ định danh theo vai trò

| FR ID | Yêu cầu chức năng (nháp mới) | So với bản hiện tại |
|---|---|---|
| FR-014 | Số giấy tờ định danh hiển thị theo quyền protected field của vai trò: đầy đủ, che hoặc ẩn. | Rút gọn. |
| ~~FR-015~~ | — | **Bỏ** — mặc định theo từng vai trò trái với nguyên tắc mục 4 (quyền do Roles & permissions cấu hình). |
| FR-016 | Dạng che có nút Show để xem số đầy đủ một lần; mỗi lần xem đầy đủ được ghi vào History. | Gộp FR-016 và FR-017; định dạng "•••••011B" → UI Components; nội dung log → BR-007, DATA-003. |
| ~~FR-017~~ | — | **Gộp** vào FR-016. |
| ~~FR-018~~ | — | **Bỏ** — đã là BR-006 (ẩn NRIC cả trong tệp xuất). |

## US-004 — Sửa thông tin định danh

| FR ID | Yêu cầu chức năng (nháp mới) | So với bản hiện tại |
|---|---|---|
| FR-019 | Người dùng có quyền sửa thông tin định danh của trẻ qua "Edit identity", kèm ngày hiệu lực, người duyệt và tệp đính kèm (tuỳ chọn). | Rút gọn; danh sách trường → UI Components. |
| ~~FR-020~~ | — | **Bỏ** — danh sách vai trò được sửa thuộc Roles & permissions (mục 4). |
| FR-021 | Mỗi lần lưu tạo một change record, hiển thị trong History. | Rút gọn; nội dung change record đã là BR-008, DATA-004. |
| FR-022 | Đổi Citizenship hiện cảnh báo ảnh hưởng học phí và trợ cấp từ ngày hiệu lực. | Rút gọn; câu chữ cảnh báo → UI Components. |
| FR-023 | Cảnh báo (không chặn) khi tên và ngày sinh trùng với trẻ khác. | Rút gọn; đã có BR-009. |
| FR-024 | Mở "Edit identity" khi hồ sơ còn trường trống thì cảnh báo và đánh dấu các trường còn thiếu. | Rút gọn; câu chữ cảnh báo → UI Components. |
| ~~FR-025~~ | — | **Bỏ** — "chỉ đi một chiều Lead → hồ sơ trẻ" đã là BR-010. |

## Tổng kết

| | Trước | Sau |
|---|---|---|
| Số FR | 25 | 13 (FR-001, 002, 004, 005, 010, 013, 014, 016, 019, 021, 022, 023, 024) |
| BR mới | — | BR-012, BR-013, BR-014 |

**Việc kéo theo khi chốt bản này** (chưa làm):
- Gắn lại Linked Rule của các AC đang trỏ vào FR bị bỏ (vd AC-009 → UI Components / bỏ AC; AC-011 → BR-013; AC-014 → bỏ tham chiếu FR-015; AC-017, AC-020 → FR-014 / BR-006; AC-023 → Roles & permissions).
- Đưa các câu ghi chú, định dạng vào cột Hành vi của UI Components.
- Mục 4: bỏ dòng Teacher cho đúng mẫu chung.
