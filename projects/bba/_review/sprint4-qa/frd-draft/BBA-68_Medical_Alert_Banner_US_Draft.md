# [Nháp] BBA-68 3.1 Medical Alert Banner — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.2, đã cập nhật theo sheet Clarification 11/11) + **câu trả lời mới của BBA trên Plane BBA-1058 (13/11/2026)** + SRS Children & Families + prototype SMS (tab Health).
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)*. Wireframe: `by-frd/BBA-68/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. **Thay đổi sức khoẻ của phụ huynh chỉ có hiệu lực sau khi Centre Director hoặc School Admin hoàn tất đánh giá** (BBA-1058 Q1, 13/11). Bản Drive (theo sheet 11/11) ghi "đồng bộ ngay, không cần duyệt" → **hai câu trả lời của BBA mâu thuẫn**, bản nháp theo câu mới hơn, chờ xác nhận ở OQ-MAB-09.
2. Trong lúc chờ đánh giá: cảnh báo giữ nội dung đã xác nhận gần nhất; hồ sơ trẻ có dòng "Update from the family waiting for assessment" (FR-030, giả định AS-MAB-01).
3. Phụ huynh chưa ký đồng ý cho hiện trên danh sách y tế thì dữ liệu không hiện trong hồ sơ trẻ (BBA-1058 Q2) — phạm vi chưa rõ, OQ-MAB-11.
4. Chỉ US-001 thay đổi; **US-002 đến US-005 giữ nguyên** bản trên Drive (chép bên dưới để đọc đủ).

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Cảnh báo sinh tự động (Q-69-02); nguồn Health + Allergies trên SMS và Parents App (Q-69-03) — khớp.
- Hiện **không có vai trò nào thiếu quyền Health**; HQ xem Health ở mọi Centre (Q-69-05); biểu tượng cảnh báo ai cũng thấy (Q-66-12) → FR-012 chỉ là cấu hình dự phòng; đóng OQ-MAB-04.
- Thứ tự, độ dài, cách mở toàn bộ cảnh báo: DOTB tự quyết (Q-69-06) → giữ FR-003, FR-010.
- Q-69-08 (09/11) nói đồng bộ ngay, không duyệt — **mâu thuẫn** với Plane BBA-1058 (13/11); bản nháp giữ theo Plane, ghi ở OQ-MAB-09.
- Định nghĩa critical (Q-69-01): không sửa, theo yêu cầu trước của user.

---

## US-001 - Quy tắc cảnh báo y tế từ Health record

#### User Story

Là Centre Director, tôi muốn hệ thống tự xác định trẻ nào cần red banner và trẻ nào chỉ cần biểu tượng cảnh báo theo đúng Health record phụ huynh khai và đã được Centre đánh giá, để mọi màn hình cảnh báo giống nhau và không phụ thuộc vào việc nhân viên tự nhớ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 | Hệ thống tính mức cảnh báo của mỗi trẻ từ Health record: **Severe** khi trẻ có ít nhất một dị ứng mức Severe (mức cao nhất của thang mức độ); **Medical** khi trẻ có dị ứng mức khác, skin condition, respiratory condition, medical history hoặc nhu cầu ăn uống (diet) và không có dị ứng Severe; **None** khi Health record không có mục nào. Mức cao nhất theo form BBA là Life Threatening; dị ứng Life Threatening được xếp mức Severe. |
| FR-002 | Dị ứng chưa chọn mức độ được tính như Severe và ghi "Severity not set" cho tới khi phụ huynh chọn mức độ. |
| FR-003 | Nội dung cảnh báo lấy nguyên văn chữ phụ huynh ghi, theo thứ tự: dị ứng Severe, dị ứng khác, respiratory, skin, medical history, diet; các mục cách nhau bằng dấu chấm giữa ( · ). |
| FR-004 | Note from staff không làm thay đổi mức cảnh báo; Note from staff chỉ hiện trong cửa sổ chi tiết (US-004) và tab Health. |
| FR-005 *(sửa)* | Mức cảnh báo và nội dung được tính lại khi Centre Director hoặc School Admin hoàn tất đánh giá thay đổi của phụ huynh. Trước khi hoàn tất, mọi màn hình dùng Health record đã xác nhận gần nhất. Màn hình đang mở hiển thị mức mới khi người dùng mở lại hoặc làm mới màn. |
| FR-006 *(sửa)* | Khi phụ huynh gửi thay đổi Health record: Centre Director, School Admin và giáo viên lớp của trẻ nhận thông báo trong app "Health update from the family waiting for assessment" kèm tên trẻ. Khi đánh giá hoàn tất và mức cảnh báo đổi (bắt đầu có cảnh báo; đổi giữa Medical và Severe; không còn cảnh báo; nội dung Severe đổi), Centre Director và giáo viên chủ nhiệm nhận thông báo ghi tên trẻ, mức mới, nội dung ngắn, ví dụ: "Ethan Lim: Severe — Allergic to shellfish and nuts, including peanuts. Assessed on 24/11/2026." |
| FR-007 | Trẻ chưa có Health record (phụ huynh chưa hoàn tất phần thông tin bắt buộc của hồ sơ nhập học (Part A), hoặc trẻ chưa sinh) có mức None và hồ sơ trẻ ghi "Health record not completed by the family" với vai trò được xem chi tiết y tế. |
| FR-030 *(mới)* | Khi có thay đổi của phụ huynh chưa được đánh giá, phần đầu hồ sơ trẻ hiện dòng "Update from the family waiting for assessment" kèm nội dung thay đổi, người gửi, thời điểm; Centre Director và School Admin có nút "Open assessment". Hoàn tất đánh giá thì dòng này biến mất và thay đổi có hiệu lực. |
| FR-031 *(mới)* | Trẻ mà phụ huynh chưa ký đồng ý cho hiện tên và ảnh trên danh sách y tế (Medical Care Assessment Checklist) không hiện dữ liệu sức khoẻ trên hồ sơ trẻ (phạm vi chờ OQ-MAB-11). |

#### Functional Flow - Main (Luồng chính)

1. *(sửa)* Phụ huynh lưu Health record trong Parents App, chọn mức độ cho từng dị ứng; thay đổi ở trạng thái chờ đánh giá; Centre Director, School Admin, giáo viên lớp nhận thông báo (FR-006, FR-030).
2. *(mới)* Centre Director hoặc School Admin mở đánh giá, hoàn tất Medical Care Assessment với phụ huynh (FR-030).
3. Hệ thống tính mức cảnh báo (FR-001, FR-002) và nội dung cảnh báo (FR-003) từ bản đã đánh giá (FR-005).
4. Hệ thống hiển thị red banner hoặc biểu tượng cảnh báo trên các màn của US-002 đến US-005.
5. Nếu mức hoặc nội dung Severe đổi, hệ thống gửi thông báo (FR-006).

#### Functional Flow - Alternative (Luồng thay thế)

1. Phụ huynh xoá hết dị ứng và bệnh: sau đánh giá, mức về None, banner và biểu tượng biến mất, thông báo được gửi (FR-001, FR-006).
2. Phụ huynh hạ mức dị ứng từ Severe xuống Moderate: sau đánh giá, banner biến mất, biểu tượng chuyển sang Medical (FR-001, FR-006).
3. Nhân viên thêm Note from staff: mức cảnh báo không đổi (FR-004).
4. *(mới)* Thay đổi đang chờ đánh giá: cảnh báo giữ bản đã xác nhận gần nhất; hồ sơ có dòng chờ đánh giá (FR-005, FR-030).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Dị ứng không có mức độ: tính như Severe, ghi "Severity not set" (FR-002; VAL-001).
2. Trẻ chưa có Health record: mức None, hồ sơ ghi "Health record not completed by the family" (FR-007).
3. *(mới)* Phụ huynh chưa ký đồng ý cho hiện trên danh sách y tế: không hiện dữ liệu sức khoẻ (FR-031).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 *(sửa)* | Phụ huynh là nguồn duy nhất của Health record; nhân viên không sửa chữ phụ huynh ghi, chỉ thêm Note from staff; Note from staff phụ huynh không thấy. Thay đổi của phụ huynh chỉ có hiệu lực sau khi Centre Director hoặc School Admin hoàn tất đánh giá. |
| BR-002 | Red banner chỉ dành cho mức Severe; mọi tình trạng khác chỉ có biểu tượng cảnh báo, để giáo viên không bị quá nhiều cảnh báo đỏ. |
| BR-003 | Khi thiếu thông tin mức độ, hệ thống chọn mức an toàn hơn (Severe). |
| BR-004 | Một trẻ chỉ có một mức cảnh báo; mọi màn hình dùng cùng mức và cùng nội dung. |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Dị ứng không có mức độ. | Tính như Severe; banner thêm dòng "Severity not set — treated as severe until the family chooses a severity." |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Mức cảnh báo | Giá trị tính | Có | None | VAL-001. | Severe / Medical / None (FR-001). |
| Nội dung cảnh báo | Chữ | Khi có | — | — | Nguyên văn chữ phụ huynh, các mục cách nhau bằng dấu chấm giữa (FR-003). |
| Dòng chờ đánh giá *(mới)* | Khối viền đứt dưới banner | Khi có thay đổi chưa đánh giá | — | — | "Update from the family waiting for assessment" + Open assessment (FR-030). |
| Thông báo | Thông báo trong app | Có | — | — | FR-006. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 | Hệ thống đọc từ Health record đã đánh giá: từng dị ứng (nội dung, mức độ), skin, respiratory, medical history, diet, người cập nhật, ngày cập nhật. Không lưu bản sao nội dung cảnh báo. |
| DATA-002 | Mỗi lần mức cảnh báo đổi được ghi lịch sử của trẻ: mức cũ, mức mới, do thay đổi nào của Health record, thời điểm, người nhận thông báo. |
| DATA-007 *(mới)* | Mỗi thay đổi của phụ huynh lưu: nội dung thay đổi, phụ huynh gửi, thời điểm gửi, người hoàn tất đánh giá, thời điểm hoàn tất. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | Ethan có dị ứng "shellfish and nuts… EpiPen on file" mức Severe đã được đánh giá | hệ thống tính mức cảnh báo | mức là Severe; nội dung theo thứ tự dị ứng Severe, respiratory, skin, các mục cách nhau bằng dấu chấm giữa ( · ) | FR-001; FR-003; BR-002 |
| AC-002 | Rayyan chỉ có respiratory "Asthma…" | hệ thống tính mức cảnh báo | mức là Medical, không có banner | FR-001; BR-002 |
| AC-003 | Caleb có dị ứng trứng chưa chọn mức độ | hệ thống tính mức cảnh báo | mức là Severe và banner có dòng "Severity not set — treated as severe until the family chooses a severity." | FR-002; BR-003; VAL-001 |
| AC-004 *(sửa)* | Ethan đang mức Severe | phụ huynh đổi dị ứng xuống Moderate; Centre Director hoàn tất đánh giá ngày 24/11 | trước đánh giá Ethan vẫn Severe và có dòng chờ đánh giá; sau đánh giá mức là Medical, Centre Director và giáo viên lớp nhận thông báo, lịch sử ghi mức cũ và mới, mọi màn cùng hiện Medical | FR-005; FR-006; FR-030; BR-004; DATA-002 |
| AC-005 | Ethan đang mức Severe | giáo viên thêm Note from staff | mức vẫn là Severe | FR-004; BR-001 |
| AC-006 | trẻ mới, phụ huynh chưa hoàn tất phần thông tin bắt buộc của hồ sơ nhập học | Centre Director mở hồ sơ trẻ | không có banner, không có biểu tượng cảnh báo, hồ sơ ghi "Health record not completed by the family" | FR-007 |
| AC-007 *(sửa)* | Noah chưa có mục y tế | phụ huynh thêm dị ứng mức Severe | Centre Director, School Admin, giáo viên lớp nhận thông báo chờ đánh giá; sau khi đánh giá, Noah có red banner và Centre Director nhận thông báo "Noah Tan: Severe — …" | FR-005; FR-006 |
| AC-032 *(mới)* | phụ huynh của Ethan thêm "Egg" lúc 23/11/2026 18:42 | School Admin mở hồ sơ Ethan | banner giữ nội dung cũ; dưới banner có "Update from the family waiting for assessment" với nội dung "Egg", người gửi, thời điểm và nút Open assessment | FR-030; DATA-007 |
| AC-033 *(mới)* | phụ huynh của Caleb chưa ký đồng ý cho hiện trên danh sách y tế | giáo viên mở hồ sơ Caleb | không hiện dữ liệu sức khoẻ (theo phạm vi chốt ở OQ-MAB-11) | FR-031 |

#### Dependencies (Phụ thuộc)

Health record (Parents App, BR-CHF-021 đến BR-CHF-029); Medical Care Assessment (bước đánh giá của Centre — OQ-MAB-12); thang mức độ dị ứng do HQ Admin cấu hình (BR-CHF-022); dịch vụ thông báo.

---

> **US-002 đến US-005 — giữ nguyên bản trên Drive** (chép lại để đọc đủ).

## US-002 - Red banner trên hồ sơ trẻ

#### User Story

Là giáo viên, tôi muốn mở hồ sơ trẻ ở bất kỳ tab nào cũng thấy ngay dải đỏ ghi dị ứng nghiêm trọng của trẻ, để không bỏ sót khi xử lý việc khác của trẻ.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-008 | Trẻ mức Severe có red banner ngay dưới dòng tên / status / Centre của hồ sơ trẻ, trên các thẻ tóm tắt; banner hiện trên mọi tab (Overview, Enrolment, Enrichment, Guardians, Attendance, Finance, Health, Communication, Documents, History). |
| FR-009 | Banner gồm: biểu tượng ⚠, tiêu đề "Severe allergy", nội dung dị ứng Severe (FR-003); dòng "Also:" liệt kê các mục khác (dị ứng khác, respiratory, skin, medical history, diet); dòng "Updated by the family on" kèm ngày phụ huynh cập nhật (ví dụ "Updated by the family on 2026-09-18"); liên kết "Open Health". |
| FR-010 | Nội dung banner hiển thị tối đa 2 dòng; dài hơn thì có "Show more" mở toàn bộ ngay trong banner. |
| FR-011 | Banner không có nút đóng; người dùng không ẩn được banner. |
| FR-012 *(sửa)* | Vai trò được cấu hình ẩn chi tiết y tế không thấy banner; phần đầu hồ sơ chỉ có biểu tượng ⚠ cạnh tên với chú thích "Medical alert on file". Hiện BBA không có vai trò nào thiếu quyền Health (Q-69-05); quy tắc này chỉ dùng khi có cấu hình như vậy về sau. |
| FR-013 | Trẻ mức Medical không có banner; phần đầu hồ sơ có biểu tượng cảnh báo cạnh tên; chi tiết ở thẻ Medical alert của tab Overview (FRD 3.1 Child Record Overview) và tab Health. |
| FR-014 | Banner vẫn hiện trên hồ sơ trẻ đã Withdrawn, Graduated hoặc Temporary withdrawal. |

#### Functional Flow - Main (Luồng chính)

1. Người dùng mở hồ sơ trẻ mức Severe.
2. Hệ thống hiển thị red banner dưới phần đầu hồ sơ (FR-008, FR-009).
3. Người dùng chuyển tab; banner giữ nguyên (FR-008).
4. Người dùng chọn "Open Health" để xem đủ Health record.

#### Functional Flow - Alternative (Luồng thay thế)

1. Nội dung dài: người dùng chọn "Show more" (FR-010).
2. Trẻ mức Medical: không banner, có biểu tượng cảnh báo (FR-013).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò được cấu hình ẩn chi tiết y tế: chỉ biểu tượng ⚠ (FR-012; VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-005 | Cảnh báo Severe luôn hiển thị và không tắt được trên hồ sơ trẻ. |
| BR-006 | Mặc định mọi vai trò thấy nội dung y tế trong phạm vi của mình; vai trò bị cấu hình ẩn chỉ thấy biểu tượng (BR-CHF-025). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-002 | Vai trò không có quyền xem chi tiết y tế mở hồ sơ trẻ có cảnh báo. | Không hiển thị banner và nội dung; chỉ biểu tượng ⚠ "Medical alert on file". |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-01 - Child record — red banner |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Red banner | Banner (đỏ) | Khi mức Severe | Hiện | VAL-002. | FR-008; FR-009; không có nút đóng (FR-011). |
| Severe allergy | Chữ | Có | Nội dung dị ứng Severe | — | FR-003. |
| Also: | Chữ | Khi có | Các mục khác, cách nhau bằng dấu chấm giữa | — | FR-009. |
| Show more | Liên kết | Khi nội dung quá 2 dòng | — | — | FR-010. |
| Updated by the family on | Chữ | Có | Ngày cập nhật Health record | — | — |
| Open Health | Liên kết | Có | — | — | Mở tab Health. |
| Biểu tượng ⚠ cạnh tên | Biểu tượng | Khi mức Severe / Medical | Đỏ (Severe), viền (Medical) | — | Chú thích khi rê chuột: nội dung (vai trò được phép) hoặc "Medical alert on file". |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-003 | Banner đọc mức cảnh báo, nội dung và ngày cập nhật của US-001; không lưu lại mỗi lần banner hiển thị. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-008 | Ethan mức Severe | Teacher lớp Sunbeams mở hồ sơ Ethan | red banner "Severe allergy: Allergic to shellfish and nuts, including peanuts. EpiPen on file." hiện dưới phần đầu hồ sơ, có "Also:" eczema và asthma, "Updated by the family on 2026-09-18" và "Open Health" | FR-008; FR-009 |
| AC-009 | hồ sơ Ethan đang mở ở tab Overview | Teacher chọn tab Attendance | banner vẫn hiện ở vị trí cũ | FR-008; BR-005 |
| AC-010 | banner đang hiện | người dùng tìm cách đóng banner | không có nút đóng | FR-011; BR-005 |
| AC-011 | Người dùng có vai trò được cấu hình ẩn chi tiết y tế | Người dùng có vai trò được cấu hình ẩn chi tiết y tế mở hồ sơ Ethan | không có banner; cạnh tên có biểu tượng ⚠ với chú thích "Medical alert on file" | FR-012; BR-006; VAL-002 |
| AC-012 | Rayyan mức Medical | Centre Director mở hồ sơ Rayyan | không có banner; cạnh tên có biểu tượng cảnh báo | FR-013 |
| AC-013 | trẻ mức Severe có nội dung dài hơn 2 dòng | người dùng chọn "Show more" | banner hiện toàn bộ nội dung | FR-010 |
| AC-014 | trẻ mức Severe đã Withdrawn | Centre Director mở hồ sơ | banner vẫn hiện | FR-014 |

#### Dependencies (Phụ thuộc)

US-001; FRD 3.1 Child Record Overview (phần đầu hồ sơ, thẻ Medical alert); Roles & permissions (quyền xem chi tiết y tế).

## US-003 - Cột Medical trên danh sách trẻ và danh sách lớp

#### User Story

Là Centre Director, tôi muốn danh sách trẻ và danh sách lớp có cột Medical và bộ lọc theo cảnh báo, để biết ngay lớp nào có trẻ dị ứng nặng và lấy danh sách khi cần.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-015 | Danh sách trẻ (menu Children & families, mục Children) có cột Medical: biểu tượng ⚠ đỏ đặc cho mức Severe, biểu tượng ⚠ viền cho mức Medical, "—" cho mức None. |
| FR-016 | Rê chuột hoặc chạm vào biểu tượng hiện chú thích: nội dung cảnh báo (FR-003) với vai trò được xem chi tiết y tế; "Medical alert on file" với vai trò được cấu hình ẩn chi tiết y tế. |
| FR-017 | Bộ lọc "Medical alert": Any, Has a medical alert (Severe và Medical), Severe allergy, No medical alert; kết hợp với các bộ lọc khác. Vai trò được cấu hình ẩn chi tiết y tế không thấy bộ lọc này. |
| FR-018 | Xuất danh sách trẻ ghi cột Medical bằng "Severe", "Yes" hoặc "No", không ghi nội dung y tế; hệ thống lưu lại người xuất và thời điểm xuất. |
| FR-019 | Tab Children của từng lớp (menu Classes, mở lớp, tab Children) có biểu tượng cảnh báo cạnh tên mỗi trẻ (như FR-015) và một dòng tóm tắt cho biết lớp có bao nhiêu trẻ có cảnh báo và bao nhiêu trẻ mức Severe, ví dụ "2 children with a medical alert · 1 severe" (2 trẻ có cảnh báo, trong đó 1 trẻ mức Severe). Dòng này có liên kết "Allergy list for this class" mở danh sách Health & allergies của lớp đó. |
| FR-020 | Trẻ chuyển lớp: biểu tượng cảnh báo hiện ở lớp mới kể từ ngày việc chuyển lớp có hiệu lực. |

#### Functional Flow - Main (Luồng chính)

1. Centre Director mở danh sách trẻ; cột Medical hiển thị theo mức (FR-015).
2. Centre Director chọn bộ lọc "Severe allergy" (FR-017).
3. Centre Director rê chuột lên biểu tượng để đọc nội dung (FR-016).
4. Centre Director xuất danh sách (FR-018).

#### Functional Flow - Alternative (Luồng thay thế)

1. Giáo viên mở tab Children của lớp: thấy biểu tượng cảnh báo và dòng tóm tắt, chọn "Allergy list for this class" (FR-019).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò được cấu hình ẩn chi tiết y tế: chú thích "Medical alert on file", không có bộ lọc Medical alert (FR-016, FR-017; VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-007 | Trẻ có cảnh báo có biểu tượng ở mọi nơi tên trẻ xuất hiện trong danh sách (BR-CHF-024). |
| BR-008 | File xuất không chứa nội dung y tế; mọi lần xuất đều được lưu lại (ai xuất, lúc nào). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-003 | Lọc "Severe allergy" không có trẻ nào. | Danh sách trống với dòng "No children with a severe allergy match these filters." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-02 - Children list — cột Medical |  |
| SCR-03 - Class — tab Children |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Cột Medical | Biểu tượng | Có | "—" | — | FR-015; FR-016. |
| Medical alert | Bộ lọc | Không | Any | VAL-003. | FR-017. |
| Export | Nút | Theo quyền | — | — | FR-018. |
| Dòng tóm tắt lớp | Text + link | Khi lớp có trẻ có cảnh báo | — | — | FR-019. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-004 | Mỗi lần xuất được lưu lại: người xuất, thời điểm, bộ lọc, số dòng. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-015 | Ethan Severe, Rayyan Medical, Adam None | HQ Admin mở danh sách trẻ | cột Medical: Ethan ⚠ đỏ đặc, Rayyan ⚠ viền, Adam "—" | FR-015; BR-007 |
| AC-016 | Centre Director Small Wonder Tampines | chọn Medical alert = Severe allergy | chỉ trẻ mức Severe của Centre hiện | FR-017 |
| AC-017 | Người dùng có vai trò được cấu hình ẩn chi tiết y tế mở danh sách trẻ | rê chuột lên biểu tượng của Ethan | chú thích "Medical alert on file"; không có bộ lọc Medical alert | FR-016; FR-017; VAL-002 |
| AC-018 | Centre Director xuất danh sách 19 trẻ | mở file xuất | cột Medical chỉ có "Severe", "Yes", "No"; hệ thống lưu lại người xuất và thời điểm xuất | FR-018; BR-008; DATA-004 |
| AC-019 | lớp Sunbeams có Ethan (Severe) và Noah (Medical) | Teacher mở tab Children của lớp Sunbeams | dòng "2 children with a medical alert · 1 severe" và liên kết "Allergy list for this class" | FR-019 |
| AC-020 | Caleb chuyển từ Bumblebees sang Sunbeams từ 2026-10-01 | ngày 2026-10-01 Teacher mở tab Children của lớp Sunbeams | Caleb có biểu tượng cảnh báo trong lớp Sunbeams | FR-020 |
| AC-021 | không trẻ nào mức Severe ở Centre đang lọc | chọn Severe allergy | danh sách trống với "No children with a severe allergy match these filters." | VAL-003 |

#### Dependencies (Phụ thuộc)

US-001; danh sách trẻ và Classes (FRD 3.1 Children & Families); Health & allergies (danh sách theo lớp).

## US-004 - Cảnh báo trên màn điểm danh

#### User Story

Là giáo viên, khi điểm danh lớp mỗi sáng tôi muốn thấy cảnh báo cạnh tên trẻ và mở chi tiết ngay tại chỗ, để biết hôm nay lớp có những trẻ nào cần lưu ý.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-021 | Màn điểm danh (menu Daily operations, tab Class attendance) có nhãn cạnh tên trẻ: "⚠ Severe" (đỏ) cho mức Severe, "⚠ Medical" (viền) cho mức Medical. |
| FR-022 | Chọn nhãn mở cửa sổ chi tiết: Allergies (kèm mức độ), Respiratory, Skin, Medical history, Diet, Note from staff, dòng "Written by the family in the Parent app · last updated" kèm ngày phụ huynh cập nhật (ví dụ "… · last updated 18 Sep 2026") và liên kết "Open Health". |
| FR-023 | Phía trên bảng điểm danh có một dòng tóm tắt cho biết lớp đang xem có bao nhiêu trẻ có cảnh báo và bao nhiêu trẻ mức Severe, ví dụ "2 children with a medical alert in Sunbeams · 1 severe" (lớp Sunbeams có 2 trẻ có cảnh báo, trong đó 1 trẻ mức Severe). Chọn dòng này thì bảng chỉ còn các trẻ có cảnh báo. |
| FR-024 | Hàng của trẻ mức Severe có vạch đỏ ở mép trái. |
| FR-025 | Trẻ Temporary withdrawal không có trên bảng điểm danh nên không có cảnh báo trên màn này; cảnh báo vẫn ở hồ sơ trẻ. |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Class attendance của lớp mình.
2. Hệ thống hiển thị nhãn và dòng tóm tắt (FR-021, FR-023, FR-024).
3. Giáo viên chọn nhãn để đọc chi tiết (FR-022).

#### Functional Flow - Alternative (Luồng thay thế)

1. Giáo viên chọn dòng tóm tắt để lọc trẻ có cảnh báo (FR-023).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Vai trò không được xem chi tiết y tế mở được màn điểm danh: nhãn không mở cửa sổ chi tiết, chú thích "Medical alert on file" (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-009 | Màn điểm danh dùng cùng mức cảnh báo và nội dung với hồ sơ trẻ (BR-004). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-004 | Lớp không có trẻ nào có cảnh báo. | Không hiện dòng tóm tắt. |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-04 - Class attendance |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Nhãn ⚠ Severe / ⚠ Medical | Nhãn | Khi có cảnh báo | — | VAL-002. | Mở cửa sổ chi tiết (FR-022). |
| Cửa sổ chi tiết | Cửa sổ nhỏ | — | Đóng | — | FR-022. |
| Dòng tóm tắt lớp | Liên kết | Khi lớp có cảnh báo | — | VAL-004. | Lọc bảng (FR-023). |
| Vạch đỏ hàng Severe | Đánh dấu hàng | Khi mức Severe | — | — | FR-024. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-005 | Cửa sổ chi tiết đọc Health record và Note from staff hiện hành của trẻ. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-022 | lớp Sunbeams có Ethan (Severe) và Noah (Medical) | Teacher mở Class attendance | Ethan có nhãn "⚠ Severe" và vạch đỏ; Noah có nhãn "⚠ Medical"; dòng "2 children with a medical alert in Sunbeams · 1 severe"; nhãn dùng cùng mức với hồ sơ trẻ | FR-021; FR-023; FR-024; BR-009 |
| AC-023 | Ethan có Note from staff về phản ứng với bánh quy | Teacher chọn nhãn của Ethan | cửa sổ hiện Allergies (Severe), Respiratory, Skin, Medical history "—", Note from staff và "Written by the family in the Parent app · last updated 18 Sep 2026" | FR-022 |
| AC-024 | dòng tóm tắt đang hiện | Teacher chọn dòng tóm tắt | bảng chỉ còn Ethan và Noah | FR-023 |
| AC-025 | lớp không có trẻ có cảnh báo | Teacher mở Class attendance | không có dòng tóm tắt | VAL-004 |
| AC-026 | 2 trẻ đang Temporary withdrawal | Teacher mở Class attendance | 2 trẻ này không có trên bảng; hồ sơ của trẻ vẫn có banner nếu mức Severe | FR-025; FR-014 |

#### Dependencies (Phụ thuộc)

US-001; màn điểm danh Class attendance (FRD 3.2 Daily Operations).

## US-005 - Cảnh báo trên Teacher App

#### User Story

Là giáo viên dùng Teacher App, tôi muốn danh sách học sinh đánh dấu trẻ có dị ứng nặng và hồ sơ trẻ có dải đỏ ở trên cùng, để thấy cảnh báo cả khi không ngồi máy tính.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-026 | Student list có nhãn dưới tên trẻ: "⚠ Severe allergy" (đỏ) cho mức Severe, "Medical" (viền) cho mức Medical; trẻ None không có nhãn. |
| FR-027 | Hồ sơ trẻ trong Teacher App có red banner ở trên cùng, trên phần Health record, với nội dung như FR-009 (Severe allergy, Also:, ngày cập nhật); banner không đóng được. |
| FR-028 | Trên mọi danh sách trẻ trong Teacher App (Student list, Routines, Allergies), trẻ có cảnh báo có biểu tượng cạnh tên (BR-TCH-014). |
| FR-029 | Teacher App chỉ hiển thị trẻ các lớp giáo viên được phân công; giáo viên đổi lớp thì thấy cảnh báo của trẻ lớp mới từ ngày được phân công. |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Student list; hệ thống hiển thị nhãn theo mức (FR-026).
2. Giáo viên chạm vào trẻ có nhãn "Severe allergy"; hồ sơ trẻ có red banner ở trên cùng (FR-027).

#### Functional Flow - Alternative (Luồng thay thế)

1. Giáo viên mở Routines: trẻ có cảnh báo có biểu tượng cạnh tên (FR-028).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Trẻ không thuộc lớp của giáo viên: không có trong danh sách (FR-029).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-010 | Teacher App dùng cùng mức cảnh báo, nội dung và màu với SMS web (BR-004); Health record chỉ đọc trong Teacher App (BR-TCH-011). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-005 | Giáo viên mở hồ sơ trẻ không thuộc lớp mình qua đường dẫn. | Không mở; hiện "This child is not in your classes." |

#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-05 - Teacher App — Student list |  |
| SCR-06 - Teacher App — Child profile |  |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Nhãn Severe allergy / Medical | Nhãn | Khi có cảnh báo | — | — | FR-026. |
| Red banner (Teacher App) | Banner (đỏ) | Khi mức Severe | Hiện | — | FR-027; không đóng được. |
| Biểu tượng cạnh tên | Biểu tượng | Khi có cảnh báo | — | — | FR-028. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-006 | Teacher App đọc mức cảnh báo và nội dung của US-001 theo lớp được phân công của giáo viên. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-027 | Nursery 2 có Chloe (dị ứng hạt, Severe) và Hana (dị ứng mức Mild) | giáo viên mở Student list | Chloe có nhãn "⚠ Severe allergy", Hana có nhãn "Medical", trẻ khác không có nhãn | FR-026 |
| AC-028 | Chloe mức Severe | giáo viên mở hồ sơ Chloe | red banner ở trên cùng: "Severe allergy: Allergic to peanuts and all tree nuts… EpiPen on file with the centre nurse.", "Also:" asthma, ngày cập nhật | FR-027; BR-010 |
| AC-029 | Chloe mức Severe | giáo viên mở Routines | Chloe có biểu tượng cạnh tên | FR-028 |
| AC-030 | giáo viên được phân công thêm lớp K1 Blue từ hôm nay | giáo viên mở Student list | trẻ lớp K1 Blue hiện kèm nhãn theo mức | FR-029 |
| AC-031 | trẻ không thuộc lớp của giáo viên | giáo viên mở hồ sơ trẻ qua đường dẫn | hiện "This child is not in your classes." | VAL-005 |

#### Dependencies (Phụ thuộc)

US-001; Teacher App (Student list, child profile, Routines, Allergies).

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Ưu tiên |
|---|---|---|
| OQ-MAB-01 | Red banner chỉ cho dị ứng mức Severe (BR-002)? Có cần banner cho bệnh không có mức độ (ví dụ co giật do sốt, hen cần inhaler) không? | Cao |
| OQ-MAB-02 | Dị ứng chưa chọn mức độ tính như Severe (FR-002) — đồng ý? | Cao |
| OQ-MAB-03 | Diet (ví dụ không ăn thịt heo, ăn chay) chỉ là biểu tượng cảnh báo, hay cần banner riêng khi liên quan tôn giáo / y tế? | Trung bình |
| OQ-MAB-04 | Prototype không cho HQ Finance thấy gì (không biểu tượng); SRS cho thấy biểu tượng (BR-CHF-025). Chốt hành vi cho vai trò không được xem chi tiết y tế. → **Đã trả lời:** mọi người thấy biểu tượng cảnh báo (Q-66-12); hiện không có vai trò nào thiếu quyền Health (Q-69-05). | Đã đóng |
| OQ-MAB-05 | Centre Director có được tự đánh dấu một trẻ là Severe (ví dụ sau sự cố ở Centre) khi phụ huynh chưa cập nhật, hay mọi thay đổi phải qua phụ huynh? | Cao |
| OQ-MAB-06 | Ai nhận thông báo khi cảnh báo đổi: chỉ Centre Director, School Admin, giáo viên lớp (FR-006) hay thêm bếp / HQ Safeguarding? | Trung bình |
| OQ-MAB-07 | Hồ sơ trẻ chưa có Health record có cần cảnh báo riêng (ví dụ "Health record not completed") trên danh sách và màn điểm danh không, hay chỉ trên hồ sơ trẻ (FR-007)? | Trung bình |
| OQ-MAB-08 | Giáo viên dạy thay / giáo viên Enrichment có thấy banner của trẻ không thuộc lớp chính của mình không? | Thấp |
| OQ-MAB-09 *(mới)* | **Hai câu trả lời của BBA mâu thuẫn:** sheet Clarification / file câu hỏi Q-69-08 (phản hồi 09/11) — thay đổi của phụ huynh đồng bộ ngay, không cần duyệt; Plane BBA-1058 (13/11) — chỉ có hiệu lực sau khi CD / Admin hoàn tất đánh giá. Bản nháp theo câu mới hơn; BBA xác nhận. | Cao |
| OQ-MAB-10 *(mới)* | Trong lúc chờ đánh giá, giáo viên thấy nội dung cũ, mới hay cả hai? Phụ huynh **thêm** dị ứng mới mà phải chờ đánh giá có rủi ro an toàn. | Cao |
| OQ-MAB-11 *(mới)* | "Chưa ký thì dữ liệu không hiện trong hồ sơ trẻ" (BBA-1058 Q2) áp cho toàn bộ thông tin sức khoẻ hay chỉ tên / ảnh trên danh sách in? | Cao |
| OQ-MAB-12 *(mới)* | Màn / bước Medical Care Assessment và việc đánh giá lại mỗi 6 tháng (nhắc trước 1 tháng — BBA-1058, BBA-490) thuộc ticket nào? | Trung bình |
| AS-MAB-01 *(mới)* | Trong lúc chờ đánh giá, cảnh báo giữ nội dung đã xác nhận gần nhất; dòng chờ đánh giá hiện cho mọi vai trò được xem chi tiết y tế. | Chờ OQ-MAB-10 |
