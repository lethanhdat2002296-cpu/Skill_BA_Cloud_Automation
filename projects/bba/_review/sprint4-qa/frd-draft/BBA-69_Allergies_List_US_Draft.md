# [Nháp] BBA-69 Allergies list (most severe first) — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + câu trả lời của BBA (Plane BBA-1058) + SRS Children & Families, Teacher App + prototype SMS `/records/allergies`.
> Nhãn: *(mới)* thêm mới · *(sửa)* đổi nội dung · *(bỏ)* đề xuất bỏ (giữ mã, không dùng lại).
> Wireframe: `by-frd/BBA-69/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. Teacher được in và xuất; **không lưu nhật ký** ai in / xuất (BBA-1058 Q2).
2. ~~Bỏ các cột riêng "phản ứng, cách xử trí, nơi để EpiPen"~~ → **đổi lại**: form của BBA có trường riêng Symptoms, Steps to follow, Medication for immediate administration (Appendix 1, đính kèm BBA-1058) → tách cột. Nơi để EpiPen vẫn không có (OQ-02).
3. Trẻ mà phụ huynh chưa ký đồng ý cho hiện trên danh sách y tế thì không có trong danh sách (BBA-1058 Q2).

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Thang chính thức trên form BBA: Mild, Moderate, **Life Threatening**; Life Threatening lên đầu (Q-70-03) → giữ nhãn Severe trên giao diện, ghi tương ứng.
- Không giới hạn số dị ứng / bệnh của một trẻ (Q-70-02) → BR-005.
- **Chưa khai báo khác với đã khai báo không dị ứng** (Q-70-09) → FR-012.
- DOTB tự quyết: mô hình dữ liệu (Q-70-01) → giữ chữ tự do + mức độ; sắp xếp (Q-70-04) → mỗi trẻ một dòng theo mức cao nhất; export / audit (Q-70-11) → không lưu nhật ký.
- Chưa phản hồi: cột Reaction / Action Plan / EpiPen (Q-70-05), condition chung danh sách (Q-70-06), kênh cho bếp (Q-70-07), đồng bộ (Q-70-12).

**Cập nhật theo tệp đính kèm Plane BBA-1058 (Appendix 1 Medical Care Assessment Checklist, Appendix 3 Medical Care Assessment Review 2025)**
- Form của BBA có sẵn các trường có cấu trúc (Appendix 1 tr. 1–2): Type of Allergies (Food, Environmental, Medication, Insect, Medical Condition), Allergens, Severity (Mild, Moderate, Life Threatening), Symptoms of Allergic Reactions, Conditions under which certain allergens are tolerable, Can the child have foods with traces of eggs / nuts, Menu modifications, Steps to follow in the event of an allergic reaction, Medication for immediate administration, Medication Held On Site Form → **thay "From the family" (chữ tự do) bằng các cột theo form** (FR-001, FR-004, FR-007); OQ-01 trả lời phần lớn.
- Tên danh sách trên form: "Medical Overview / Medical Health Alert List"; phụ huynh đồng ý hiện **tên và ảnh** (Appendix 1 tr. 3) → FR-011, bản in có ảnh.
- Đánh giá lại mỗi 6 tháng hoặc khi có thay đổi, có "Date of Next Review" (Appendix 3); BBA chốt theo dõi trong hệ thống, nhắc trước 1 tháng (BBA-1058 Q1) → FR-013.
- Thay đổi của phụ huynh chỉ áp dụng sau khi CD / Admin hoàn tất đánh giá (BBA-1058 Q1) → FR-014.

---

## US-001 - Danh sách dị ứng, trẻ nặng nhất lên đầu

#### User Story

Là giáo viên, tôi muốn xem và in danh sách dị ứng của lớp mình, trẻ bị nặng nhất ở trên cùng, để tôi và bếp biết ngay trẻ nào cần tránh món gì.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(sửa)* | Danh sách có một dòng cho mỗi trẻ có ít nhất một dị ứng, theo các trường của Medical Care Assessment Checklist (Appendix 1): ảnh và tên trẻ, lớp, "Note from staff"; loại (Food, Environmental, Medication, Insect) và các chất gây dị ứng, mỗi chất kèm mức độ (Mild / Moderate / Severe); Symptoms; Can tolerate (điều kiện dung nạp) kèm "Traces · Eggs: Yes/No · Nuts: Yes/No"; Emergency action plan (các bước xử trí) kèm thuốc dùng ngay và trạng thái Medication Held On Site Form; Next review (FR-013). |
| FR-002 *(sửa)* | Thứ tự mặc định: trẻ có mức nặng nhất ở trên cùng (Severe — tương ứng "Life Threatening" trên form của BBA — rồi Moderate, rồi Mild); cùng mức thì xếp theo lớp, rồi theo tên trẻ. Dị ứng chưa chọn mức độ được xếp cùng nhóm Severe và ghi "Severity not set". |
| FR-003 *(sửa)* | Bên dưới danh sách dị ứng có phần riêng "Other conditions and diet" cho trẻ không có dị ứng nhưng có Medical Condition, Medical Conditions & History (Appendix 1 tr. 1) hoặc chế độ ăn đặc biệt; mỗi dòng có loại, mô tả, kế hoạch xử trí, Next review. |
| FR-004 *(sửa)* | Tìm theo tên trẻ hoặc chất gây dị ứng; lọc theo Centre, lớp, mức độ, loại (Food, Environmental, Medication, Insect, Medical condition — theo Appendix 1) và hạn đánh giá lại (Any, Due within 1 month, Overdue); các bộ lọc dùng kết hợp được. |
| FR-005 | Giáo viên mở danh sách thì mặc định lọc theo lớp của mình; Centre Director và School Admin mặc định thấy toàn Centre. |
| FR-006 *(bỏ)* | ~~Ô "Chưa có thông tin" màu đỏ cho trẻ Severe thiếu phản ứng / cách xử trí / nơi để thuốc.~~ Lý do: không có trường riêng (xem OQ-01). |
| FR-007 *(sửa)* | "Print for the kitchen" in "Medical Health Alert List" theo bộ lọc đang chọn (một lớp hoặc cả Centre); đầu trang ghi tên Centre, lớp, ngày giờ in (ví dụ "Printed 24/11/2026 08:15") và số trẻ; cột: Photo, Child, Type · allergen · severity, Can tolerate, Traces of eggs / nuts, Emergency action plan (chờ OQ-04). |
| FR-008 *(sửa)* | "Export" xuất danh sách theo bộ lọc đang chọn ra Excel. Hệ thống không lưu nhật ký in / xuất. |
| FR-009 | Chọn tên trẻ mở tab Health trong hồ sơ trẻ. |
| FR-010 | Danh sách chỉ gồm trẻ đang đi học; trẻ đang tạm nghỉ, đã thôi học hoặc đã tốt nghiệp không có trong danh sách. |
| FR-011 *(mới)* | Trẻ mà phụ huynh chưa ký đồng ý cho hiện tên và ảnh trên danh sách y tế (Medical Care Assessment Checklist) không có trong danh sách và bản in. |
| FR-012 *(mới)* | Trẻ chưa khai Health record ("chưa cung cấp") được phân biệt với trẻ đã khai không có dị ứng: cuối danh sách có nhóm "Health information not provided" để Centre liên hệ phụ huynh. Trẻ chưa sinh không nằm trong nhóm này (Q-70-09). Cách hiển thị do DOTB quyết định. |
| FR-013 *(mới)* | Cột "Next review" hiện Date of Next Review của lần đánh giá gần nhất (mỗi 6 tháng — Appendix 3); từ 1 tháng trước ngày đó hiện "Due in …" (lúc hệ thống nhắc và gửi form đánh giá lại cho phụ huynh — BBA-1058 Q1); qua ngày đó chưa đánh giá hiện "Overdue". |
| FR-014 *(mới)* | Khi phụ huynh sửa thông tin sức khoẻ trong Parents App, danh sách và bản in giữ thông tin đã được xác nhận gần nhất và gắn nhãn "Awaiting assessment" cho tới khi CD / Admin hoàn tất đánh giá (BBA-1058 Q1). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Children & families › Health & allergies; danh sách mặc định lọc theo lớp của mình (FR-005).
2. Hệ thống hiển thị trẻ có dị ứng, trẻ nặng nhất lên đầu (FR-001, FR-002), và phần "Other conditions and diet" (FR-003).
3. Giáo viên chọn "Print for the kitchen" và đưa bản in cho bếp (FR-007).

#### Functional Flow - Alternative (Luồng thay thế)

1. *(sửa)* Centre Director lọc toàn Centre theo mức Severe để rà soát (FR-004).
2. Centre Director, School Admin hoặc giáo viên xuất danh sách ra Excel (FR-008).
3. Người dùng chọn tên trẻ để xem đủ Health record (FR-009).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Bộ lọc không có trẻ nào: hiện thông báo trống (VAL-001).
2. Vai trò không được xem chi tiết y tế: không mở được danh sách (VAL-002).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 *(sửa)* | Phụ huynh khai thông tin dị ứng (Medical Care Assessment); Centre Director hoặc Senior Staff kiểm tra và xác nhận (Appendix 1 tr. 3, BBA-1058 Q1). Danh sách chỉ đọc; nhân viên chỉ thêm "Note from staff" ở tab Health. |
| BR-002 | Trẻ nặng nhất luôn ở trên cùng; dị ứng chưa chọn mức độ được coi như Severe. |
| BR-003 *(sửa)* | Bản in luôn ghi ngày giờ in, để bếp biết bản nào là bản mới nhất. |
| BR-004 *(sửa)* | Centre Director, School Admin và Teacher được xem, in và xuất danh sách; không lưu nhật ký in / xuất. |
| BR-005 *(mới)* | Một trẻ không bị giới hạn số dị ứng hoặc bệnh (Q-70-02). |
| BR-006 *(mới)* | Mỗi Medical Care Assessment được đánh giá lại tối đa 6 tháng một lần, hoặc sớm hơn khi có thay đổi / sự cố (Appendix 3). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Bộ lọc không có trẻ nào. | Hiện "No children with allergies match these filters."; nút in và xuất file bị mờ. |
| VAL-002 | Người dùng không có quyền xem chi tiết y tế mở danh sách. | Không có mục Health & allergies trong menu; mở bằng đường dẫn thì hiện "You do not have access to medical details." |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Tìm kiếm | Ô nhập | Không | Trống | — | Tên trẻ, chất gây dị ứng. |
| Centre, Class, Severity, Type, Review *(sửa)* | Bộ lọc | Không | Theo vai trò (FR-005) | VAL-001. | FR-004. |
| Danh sách dị ứng *(sửa)* | Bảng | Có | Nặng nhất lên đầu | — | Cột: Child (kèm Note from staff), Type · allergen · severity, Symptoms, Can tolerate, Emergency action plan · medication, Next review (FR-001; FR-002; FR-013). |
| Awaiting assessment *(mới)* | Nhãn dưới tên trẻ | Khi có | — | — | FR-014. |
| Health information not provided *(mới)* | Nhóm cuối danh sách | Khi có | — | — | Kèm "Contact the family" (FR-012). |
| Other conditions and diet | Bảng | Khi có | — | — | FR-003. |
| Print for the kitchen | Nút | Có | — | VAL-001. | FR-007. |
| Export | Nút | Có | — | VAL-001. | FR-008. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 *(sửa)* | Danh sách đọc từ Medical Care Assessment đã xác nhận: loại, chất gây dị ứng, mức độ, triệu chứng, điều kiện dung nạp, traces of eggs / nuts, menu modifications, các bước xử trí, thuốc dùng ngay, Medication Held On Site Form, bệnh và tiền sử, đồng ý hiện tên và ảnh, người xác nhận và ngày; "Note from staff". |
| DATA-003 *(mới)* | Mỗi lần đánh giá lại lưu: số thứ tự, Date of Review, Date of Next Review, còn phù hợp không, có thay đổi không, thuốc còn hạn tới lần đánh giá sau không, người đánh giá, xác nhận của phụ huynh (Appendix 3). |
| DATA-002 *(bỏ)* | ~~Lưu nhật ký mỗi lần in và xuất file.~~ Lý do: BBA không cần (BBA-1058 Q2). |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Sunbeams có Ethan (hải sản và hạt, Severe) và một trẻ dị ứng trứng mức Mild | giáo viên lớp Sunbeams mở danh sách | Ethan ở dòng đầu, trẻ dị ứng trứng ở dưới; mỗi chất gây dị ứng ghi kèm mức độ | FR-001; FR-002; BR-002 |
| AC-002 | một trẻ dị ứng trứng chưa chọn mức độ | danh sách hiển thị | trẻ nằm trong nhóm Severe và ghi "Severity not set" | FR-002; BR-002 |
| AC-003 | Rayyan chỉ có hen suyễn, không có dị ứng | danh sách hiển thị | Rayyan nằm ở phần "Other conditions and diet" | FR-003 |
| AC-004 *(bỏ)* | ~~Ethan Severe chưa có cách xử trí → "Chưa có thông tin"~~ | | | ~~FR-006~~ |
| AC-005 *(sửa)* | giáo viên đang lọc lớp Sunbeams | giáo viên chọn "Print for the kitchen" | bản in chỉ có trẻ lớp Sunbeams, đầu trang ghi Centre, lớp, ngày giờ in và số trẻ | FR-007; BR-003 |
| AC-006 *(sửa)* | giáo viên lọc lớp Sunbeams | giáo viên chọn Export | file Excel có đúng các trẻ đang hiện; không có bản ghi nhật ký xuất | FR-008; BR-004 |
| AC-007 | giáo viên lớp Sunbeams | giáo viên mở danh sách | bộ lọc lớp mặc định là Sunbeams | FR-005 |
| AC-008 | một trẻ dị ứng đang tạm nghỉ | Centre Director mở danh sách toàn Centre | trẻ đó không có trong danh sách | FR-010 |
| AC-009 | HQ Finance không được xem chi tiết y tế | HQ Finance mở đường dẫn danh sách | hiện "You do not have access to medical details." | VAL-002; BR-004 |
| AC-010 | lớp không có trẻ dị ứng | giáo viên mở danh sách | hiện "No children with allergies match these filters."; nút in và xuất file bị mờ | VAL-001 |
| AC-011 | đang xem danh sách | giáo viên chọn tên Ethan | mở tab Health trong hồ sơ Ethan | FR-009; BR-001 |
| AC-012 *(mới)* | phụ huynh của Caleb chưa ký đồng ý cho hiện trên danh sách y tế | giáo viên mở danh sách và in cho bếp | Caleb không có trong danh sách và bản in | FR-011 |
| AC-013 *(mới)* | phụ huynh của Mia chưa khai Health record | Centre Director mở danh sách toàn Centre | Mia ở nhóm "Health information not provided", không nằm trong nhóm dị ứng | FR-012 |
| AC-014 *(mới)* | lần đánh giá gần nhất của Sophia có Date of Next Review 16/12/2026; hôm nay 24/11/2026 | Centre Director mở danh sách | Next review của Sophia ghi "16/12/2026 · Due in 3 weeks" | FR-013 |
| AC-015 *(mới)* | Next review của Lucas là 02/11/2026, chưa đánh giá lại | Centre Director lọc Review: Overdue | Lucas có trong kết quả, nhãn "Overdue" | FR-004; FR-013 |
| AC-016 *(mới)* | mẹ của Ethan sửa triệu chứng trong Parents App, CD chưa đánh giá | giáo viên mở danh sách | dòng Ethan vẫn hiện triệu chứng đã xác nhận, có nhãn "Awaiting assessment" | FR-014 |

#### Dependencies (Phụ thuộc)

Health record (phụ huynh khai trong Parents App, CD / Admin hoàn tất đánh giá — BBA-68); quyền xem chi tiết y tế (Roles & permissions); hồ sơ trẻ.

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái |
|---|---|---|
| OQ-01 *(sửa)* | Phản ứng, cách xử trí, nơi để thuốc khẩn cấp có thành trường riêng không? | **Trả lời phần lớn** bằng form của BBA (Appendix 1): Symptoms, Steps to follow, Medication for immediate administration là trường riêng → đã tách cột. Nơi để thuốc không có trên form → OQ-02 |
| OQ-02 *(sửa)* | Nơi để thuốc khẩn cấp có cần ghi không, ai ghi? Form chỉ có "Medication Held On Site Form Has Been Completed? Yes / Not Applicable" (Appendix 1 tr. 2). | Mở |
| OQ-03 | Bếp dùng bản in hay có tài khoản xem trên máy; được xem dữ liệu nhận dạng nào? | Mở — BBA chưa trả lời (Q-70-07) |
| OQ-04 *(sửa)* | Bản in cho bếp: DOTB đề xuất Photo, Child, Type · allergen · severity, Can tolerate, Traces of eggs / nuts, Emergency action plan (theo Appendix 1). Có cần thêm Menu modifications không? | Mở — chờ BBA xác nhận |
| OQ-05 *(mới)* | "Chưa ký thì không hiện" áp cho toàn bộ thông tin sức khoẻ (giáo viên cũng không thấy) hay chỉ tên / ảnh trên bản in? Ẩn toàn bộ có rủi ro an toàn. | Mở — cao |
| AS-01 | Bếp nhận bản in do Centre đưa. | Chờ OQ-03 |
| AS-04 *(mới)* | Bản in chỉ ghi ngày giờ in, không ghi tên người in. | DOTB quyết định (Q-70-11) |
| OQ-06 *(mới)* | Thang mức độ có cần cấu hình theo brand / Centre ngay Phase 1 không? BBA nói form "có thể" tuỳ theo brand / Centre (Q-70-03). | Mở |
| OQ-07 *(sửa)* | Medical condition, medical history nằm chung danh sách dị ứng hay nhóm riêng? Form vừa có "Medical Condition" trong Type of Allergies, vừa có mục "Medical Conditions & History" riêng (Appendix 1 tr. 1). FRD đang để nhóm riêng. | Mở — BBA chưa trả lời (Q-70-06) |
| OQ-08 *(mới)* | Can tolerate, traces of eggs / nuts, menu modifications do phụ huynh khai trong Parents App hay Centre ghi khi đánh giá ("Menu reviewed with parents")? | Mở |
| OQ-09 *(mới)* | Tên màn hình dùng "Allergies & conditions" hay theo form của BBA "Medical Health Alert List"? Wireframe đang để tên form làm phụ đề và tiêu đề bản in. | Mở — thấp |
