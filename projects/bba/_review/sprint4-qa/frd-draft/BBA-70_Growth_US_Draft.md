# [Nháp] BBA-70 Growth – termly height & weight entry by class — User Story

> Nháp để review, **chưa đưa lên Drive / Git**. Dựa trên FRD trên Drive (v0.1) + câu trả lời của BBA (Plane BBA-529, BBA-1059, BBA-524) + SRS Children & Families + prototype SMS tab Growth, Teacher app `/growth`.
> Nhãn: *(mới)* · *(sửa)* · *(bỏ)* (giữ mã, không dùng lại). Wireframe: `by-frd/BBA-70/wireframe.html`.

**Thay đổi chính so với bản trên Drive**
1. **Bỏ BMI** (BBA đã bỏ ở buổi review Parent App 16/09 — BBA-1059).
2. Biểu đồ: Singapore theo nghiên cứu nhân trắc của Singapore National Healthcare Group Polyclinics; Malaysia theo Child Health Record Book (BBA-1059 Q1).
3. Lịch đo: 4 kỳ / năm; riêng Brighton theo 2 học kỳ; nhắc giữa tháng cuối mỗi quý cho mọi brand (BBA-529).
4. Trẻ vắng và trẻ tạm nghỉ vẫn có trên màn nhập, tách nhóm riêng (Q2); được **xoá** số đo, một quyền chung thêm / sửa / xoá (Q3); phụ huynh thấy ngay (Q4).
5. Báo cáo HQ chỉ cần trạng thái hoàn thành; người dùng CD, Admin, Cluster Head (Q5).

**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**
- Term **do HQ đặt theo brand, Centre không sửa**; 4 term, năm học bắt đầu 1/1, ngày term đổi theo năm (vd Schoolhouse T1 2/1–15/3, Agape T1 2/1–10/3); nhắc giữa tháng cuối mỗi term (Q-71-03) → FR-001, FR-011.
- Mọi trẻ trong lớp (Q-71-06); một lần mỗi term và có **Measurement history** (Q-71-07) → FR-012; Change record có "Updated By" (Q-71-08); đơn vị cm, kg (Q-71-05).
- Teacher thao tác lớp mình; Centre Director và School Admin mọi trẻ (Q-71-10) → BR-005.
- Lưu cả lớp khi có dòng lỗi: DOTB tự quyết (Q-71-09) → lưu các dòng hợp lệ.
- **Mâu thuẫn:** Q-71-02 (09/11) bỏ cả BMI và percentile, "chỉ cần height + weight" ↔ Plane BBA-1059 (13/11) gửi chuẩn biểu đồ → giữ biểu đồ theo Plane, OQ-07.

**Cập nhật theo tệp đính kèm Plane BBA-529 và BBA-1059**
- File mẫu export của Taidii "Quarterly Heights & Weight Report" (BBA-529, `Student_quarterly_height_weight_2026-sample.xlsx`): mỗi lớp một năm; đầu file ghi Centre, Class, Year, Generated on; cột No., Name, Birthdate, IC/BC No., Program Type, Term 1–4 mỗi kỳ Height cm / Weight kg → thêm **Year view** và **Export** cùng bố cục (FR-013). BBA hỏi để "màn mới, báo cáo HQ và chuyển dữ liệu khớp với những gì đang giữ".
- File mẫu là của Brighton Montessori Frankel (đo theo học kỳ) nhưng vẫn có cột Term 1–4, số đo là số nguyên (94 cm, 13 kg) → OQ-08, OQ-03.
- Ảnh Taidii Parents App: biểu đồ chiều cao theo tuổi với 3 đường 3rd / 50th / 97th, ghi "plotted according to WHO standards"; BBA chọn chuẩn Singapore (NHG Polyclinics) và Malaysia (Child Health Record Book) (BBA-1059 Q1) → FR-004, wireframe biểu đồ trên hồ sơ trẻ; có hiện đường percentile hay không vẫn chờ OQ-07.
- Taidii Center Staff Role permissions, dòng 14 "Update Height and Weight": CD/ACD/Admin và Teachers → khớp BR-005.
- File "Centre Terms Setup.xlsx" (BBA-489): ngày bắt đầu Term 1–4 năm 2027 theo từng brand; **Brighton Montessori cũng có 4 term** (1/1, 1/4, 1/7, 1/10) → kỳ đo là Term 1–4 cho mọi brand; Brighton đo theo học kỳ, tức đo ở 2 trong 4 term (OQ-08) → sửa FR-001, AC-013; OQ-01 đã có dữ liệu.
- Parent App Requirements (30/07/2026) mục 19: Height, Weight, Growth tracking/history → khớp FR-008, FR-012; mục 19b "Health observations" → OQ-09.

---

## US-001 - Nhập chiều cao, cân nặng theo lớp mỗi kỳ

#### User Story

Là giáo viên, tôi muốn nhập chiều cao và cân nặng của cả lớp trên một màn hình và lưu một lần, để không phải mở từng hồ sơ trẻ và phụ huynh thấy ngay sự phát triển của con.

#### Functional Requirements (Yêu cầu chức năng)

| FR ID | Yêu cầu chức năng |
|---|---|
| FR-001 *(sửa)* | Màn "Height & weight" cho chọn lớp, kỳ đo và ngày đo (mặc định hôm nay, không được sau hôm nay). Kỳ đo là Term 1–4 theo lịch term của brand do HQ đặt (Centre không sửa): năm học bắt đầu 1/1, ngày term đổi theo từng năm (Q-71-03; Centre Terms Setup — BBA-489). Brighton Montessori cũng dùng Term 1–4 nhưng đo theo học kỳ, tức đo ở 2 trong 4 term (BBA-529; term nào chờ OQ-08). |
| FR-002 *(sửa)* | Bảng chia 2 nhóm: "Present today" và "Absent today · Temporary withdrawal". Mỗi trẻ một dòng: tên, tuổi (năm và tháng tại ngày đo), số đo lần trước (chiều cao, cân nặng, ngày đo), ô nhập chiều cao (cm) và cân nặng (kg). Trẻ nhóm thứ hai để trống được và nhập sau trong cùng kỳ. |
| FR-003 *(sửa)* | "Save the whole class" lưu một lần mọi dòng đã nhập đủ cả chiều cao và cân nặng; dòng để trống không được lưu và vẫn là "Not recorded yet" trong kỳ; dòng lỗi không chặn các dòng hợp lệ (DOTB quyết định, Q-71-09). Số đo có hiệu lực ngay, không cần duyệt. |
| FR-004 *(sửa)* | Hệ thống tính vị trí của trẻ trên biểu đồ tăng trưởng theo tuổi và giới tính: Centre Singapore dùng chuẩn nhân trắc của Singapore National Healthcare Group Polyclinics; Centre Malaysia dùng Child Health Record Book. Không tính BMI. |
| FR-005 | Số đo ngoài khoảng hợp lệ bị chặn (VAL-001). Chiều cao thấp hơn lần đo trước hiện cảnh báo "Height is lower than the last measurement. Check before saving."; người dùng vẫn lưu được. |
| FR-006 | Một trẻ chỉ có một số đo cho mỗi kỳ; nhập lại trong cùng kỳ thì số mới thay số cũ, số cũ giữ trong lịch sử kèm người sửa và thời điểm. |
| FR-007 | Từ hồ sơ trẻ, người dùng có quyền nhập được số đo cho riêng một trẻ, bất kỳ ngày nào, cho trẻ ở mọi độ tuổi. |
| FR-008 *(sửa)* | Hồ sơ trẻ và mục Health & growth trong Parents App hiển thị chiều cao, cân nặng, ngày đo và biểu đồ tăng trưởng; số đo mới hiện cho phụ huynh ngay sau khi lưu. |
| FR-009 *(sửa)* | Báo cáo "Height & weight completion" theo Centre, lớp và kỳ đo: số trẻ, số trẻ đã đo, tỷ lệ hoàn thành; lọc theo Centre và kỳ đo; xuất ra Excel. Không có thống kê tăng trưởng. Người dùng ban đầu: Centre Director, School Admin, Cluster Head (BBA-1059 Q5). |
| FR-010 *(mới)* | "Delete" ở một số đo đã lưu mở hộp xác nhận "Delete this measurement?"; xoá thì phụ huynh không còn thấy số đo đó; lịch sử ghi việc xoá, người xoá, thời điểm. |
| FR-011 *(mới)* | Hệ thống gửi nhắc nhập chiều cao, cân nặng vào giữa tháng cuối mỗi term (tháng 3, 6, 9, 12) cho mọi brand, kể cả Brighton (Q-71-03, BBA-529). |
| FR-012 *(mới)* | Hồ sơ trẻ, tab Health › Growth có biểu đồ chiều cao / cân nặng theo tuổi (FR-004) và "Measurement history": mọi lần đo theo ngày đo — term, ngày đo, chiều cao, cân nặng, thay đổi so với kỳ trước, người nhập và nơi nhập (class entry / child record); mỗi dòng có Edit, Delete theo quyền (Q-71-07, Q-71-08, Q-71-11). |
| FR-013 *(mới)* | Màn Height & weight có "Year view" cho một lớp và một năm: mỗi trẻ một dòng gồm No., tên, ngày sinh, IC / BC No. (che theo vai trò như hồ sơ trẻ — BBA-66), chương trình học, và Height cm / Weight kg của Term 1 đến Term 4; "Export (Excel)" xuất đúng bố cục này, đầu file ghi Centre, Class, Year, Generated on — giống báo cáo "Quarterly Heights & Weight Report" của Taidii (BBA-529). |

#### Functional Flow - Main (Luồng chính)

1. Giáo viên mở Growth, chọn lớp, kỳ đo và ngày đo (FR-001).
2. Hệ thống hiển thị trẻ theo 2 nhóm kèm số đo lần trước (FR-002).
3. Giáo viên nhập chiều cao, cân nặng và chọn "Save the whole class" (FR-003; VAL-001, VAL-002).
4. Hệ thống tính vị trí trên biểu đồ (FR-004) và hiện cho phụ huynh ngay (FR-008).

#### Functional Flow - Alternative (Luồng thay thế)

1. *(sửa)* Trẻ vắng hoặc tạm nghỉ: để trống ở nhóm thứ hai, nhập vào ngày khác trong kỳ (FR-002, FR-003).
2. Nhập sai: nhập lại trong cùng kỳ, số cũ vào lịch sử (FR-006).
3. Nhập cho một trẻ từ hồ sơ trẻ (FR-007).
4. *(sửa)* Centre Director, School Admin, Cluster Head xem báo cáo lớp nào chưa đo đủ (FR-009).
5. *(mới)* Xoá một số đo nhập nhầm (FR-010).
6. *(mới)* Giữa tháng cuối quý, Centre nhận nhắc nhập số đo (FR-011).
7. *(mới)* Giáo viên chuyển sang Year view để xem cả năm của lớp và xuất Excel (FR-013).
8. *(mới)* Centre Director mở hồ sơ trẻ, tab Health › Growth, xem biểu đồ và lịch sử đo (FR-012).

#### Functional Flow - Exception (Luồng ngoại lệ)

1. Số đo ngoài khoảng hợp lệ: không lưu dòng đó (VAL-001).
2. Chỉ nhập một trong hai số: không lưu dòng đó (VAL-002).
3. Ngày đo sau hôm nay: không lưu (VAL-003).

#### Business Rules (Quy tắc nghiệp vụ)

| BR ID | Quy tắc nghiệp vụ |
|---|---|
| BR-001 | Số đo do nhân viên ghi trực tiếp, không cần duyệt. |
| BR-002 | Mỗi trẻ một số đo cho mỗi kỳ; số mới thay số cũ, lịch sử được giữ. |
| BR-003 *(sửa)* | Vị trí trên biểu đồ do hệ thống tính, người dùng không sửa tay. |
| BR-004 | Phụ huynh chỉ xem số đo của con mình. |
| BR-005 *(mới)* | Thêm, sửa và xoá số đo là một quyền chung (BBA-1059); Teacher thao tác trên lớp mình, Centre Director và School Admin trên mọi trẻ của Centre (Q-71-10). |

#### Validation Rules (Quy tắc kiểm tra)

| VAL ID | Điều kiện | Phản hồi hệ thống |
|---|---|---|
| VAL-001 | Chiều cao hoặc cân nặng ngoài khoảng hợp lệ (AS-02). | Dòng đó không được lưu; ô bị đánh dấu với chữ "Check this value." |
| VAL-002 | Chỉ nhập chiều cao hoặc chỉ nhập cân nặng. | Dòng đó không được lưu; ô còn trống bị đánh dấu "Enter both height and weight." |
| VAL-003 | Ngày đo sau hôm nay. | Không lưu; hiện "The measurement date cannot be in the future." |

#### UI Components / Field Specification (Thành phần giao diện)

| Trường / Điều khiển | Loại | Bắt buộc | Mặc định / Trạng thái | Kiểm tra | Hành vi |
|---|---|---|---|---|---|
| Class | Danh sách chọn | Có | Lớp đầu tiên của giáo viên | — | Giáo viên chỉ thấy lớp mình. |
| Term *(sửa)* | Danh sách chọn | Có | Term hiện tại | — | Term 1–4 theo lịch term của brand, mọi brand kể cả Brighton. |
| Date measured | Ngày | Có | Hôm nay | VAL-003. | — |
| Height (cm) | Số, 1 chữ số thập phân | Khi nhập dòng | Trống | VAL-001; VAL-002. | — |
| Weight (kg) | Số, 1 chữ số thập phân | Khi nhập dòng | Trống | VAL-001; VAL-002. | — |
| Nhóm "Absent today · Temporary withdrawal" *(mới)* | Nhóm dòng | Khi có | — | — | FR-002. |
| Save the whole class | Nút | Có | — | — | FR-003. |
| Delete *(mới)* | Nút ở số đo đã lưu | Theo quyền | — | — | FR-010. |
| Enter this term / Year view *(mới)* | Nút chuyển chế độ | Có | Enter this term | — | FR-013. |
| Year | Danh sách chọn (Year view) | Có | Năm hiện tại | — | FR-013. |
| Export (Excel) *(mới)* | Nút (Year view) | Theo quyền | — | — | FR-013. |
| Biểu đồ Height / Weight for age *(mới)* | Biểu đồ trên hồ sơ trẻ | — | Height | — | FR-004; FR-012; chờ OQ-07. |
| Measurement history *(mới)* | Bảng trên hồ sơ trẻ | — | Mới nhất lên đầu | — | FR-012. |

#### Data and Audit (Dữ liệu và audit)

| ID | Yêu cầu |
|---|---|
| DATA-001 *(sửa)* | Mỗi số đo lưu: trẻ, kỳ đo, ngày đo, chiều cao, cân nặng, vị trí trên biểu đồ, chuẩn biểu đồ dùng, người nhập, thời điểm nhập. |
| DATA-002 | Mỗi lần sửa lưu giá trị cũ, giá trị mới, người sửa và thời điểm. |
| DATA-003 *(mới)* | Mỗi lần xoá lưu số đo bị xoá, người xoá, thời điểm. |

#### Acceptance Criteria (Tiêu chí nghiệm thu)

| AC ID | Given | When | Then | Linked Rule |
|---|---|---|---|---|
| AC-001 | lớp Nursery 1 có 18 trẻ, 17 trẻ có mặt | giáo viên nhập số đo cho 17 trẻ và chọn "Save the whole class" | 17 số đo được lưu cùng lúc, không cần duyệt; trẻ còn lại ở nhóm "Absent today" với "Not recorded yet" | FR-001; FR-002; FR-003; BR-001 |
| AC-002 *(sửa)* | Ethan (Centre Singapore, nam, 4 tuổi 9 tháng) cao 108,5 cm, nặng 18,1 kg | số đo được lưu | biểu đồ của Ethan có điểm mới theo chuẩn Singapore; không có BMI | FR-004; BR-003 |
| AC-003 | giáo viên nhập 1000 cm | chọn Save | dòng đó không được lưu, ô hiện "Check this value." | VAL-001 |
| AC-004 | giáo viên chỉ nhập chiều cao | chọn Save | dòng đó không được lưu, ô cân nặng hiện "Enter both height and weight." | VAL-002 |
| AC-005 | lần trước trẻ cao 98 cm | giáo viên nhập 96 cm | hiện cảnh báo chiều cao thấp hơn lần trước; giáo viên vẫn lưu được | FR-005 |
| AC-006 | trẻ đã có số đo kỳ này | giáo viên nhập lại số khác trong cùng kỳ | số mới thay số cũ; lịch sử ghi số cũ, người sửa, thời điểm | FR-006; BR-002; DATA-002 |
| AC-007 *(sửa)* | số đo vừa được lưu | phụ huynh mở Health & growth | thấy ngay chiều cao, cân nặng, ngày đo và điểm mới trên biểu đồ | FR-008; BR-004 |
| AC-008 | ngày đo chọn ngày mai | chọn Save | hiện "The measurement date cannot be in the future." | VAL-003 |
| AC-009 *(sửa)* | lớp N2 · Sunbeams đo 12 / 18 trẻ trong Term 4 | Cluster Head mở báo cáo completion | dòng N2 · Sunbeams hiện 18 trẻ, đã đo 12, hoàn thành 67% | FR-009 |
| AC-010 | Centre Director mở hồ sơ một trẻ | nhập số đo cho riêng trẻ đó | số đo được lưu và biểu đồ của trẻ cập nhật | FR-007 |
| AC-011 *(mới)* | Sofia đang tạm nghỉ | giáo viên mở màn nhập lớp của Sofia | Sofia ở nhóm "Absent today · Temporary withdrawal", ô nhập để trống được | FR-002 |
| AC-012 *(mới)* | số đo Term 4 của Ethan nhập nhầm | giáo viên chọn Delete và xác nhận | số đo bị xoá, phụ huynh không còn thấy; lịch sử ghi người xoá và thời điểm | FR-010; BR-005; DATA-003 |
| AC-013 *(mới)* | Centre thuộc brand Brighton Montessori, lịch 2027 bắt đầu Term 2 ngày 01/04/2027 | giáo viên mở danh sách kỳ đo ngày 10/04/2027 | danh sách có Term 1 đến Term 4 của 2027, mặc định Term 2 | FR-001 |
| AC-014 *(mới)* | ngày 15/12/2026 | hệ thống chạy nhắc | Centre nhận nhắc nhập chiều cao, cân nặng | FR-011 |
| AC-015 *(mới)* | lớp N2 · Sunbeams có số đo Term 1–4 năm 2026 | giáo viên chọn Year view, năm 2026 | mỗi trẻ một dòng với ngày sinh, IC / BC No. đã che, chương trình học và Height cm / Weight kg của 4 term; term chưa đo hiện "—" | FR-013 |
| AC-016 *(mới)* | đang ở Year view lớp N2 · Sunbeams năm 2026 | giáo viên chọn Export (Excel) | file có đầu trang Centre, Class, Year, Generated on và các cột như Year view | FR-013 |
| AC-017 *(mới)* | Ethan có số đo Term 3 (107,0 cm, 17,6 kg) và Term 4 (108,5 cm, 18,1 kg) | Centre Director mở hồ sơ Ethan, tab Health › Growth | dòng Term 4 ghi "+1.5 cm · +0.5 kg" và người nhập; biểu đồ có điểm Term 4 | FR-004; FR-012 |

#### Dependencies (Phụ thuộc)

Danh sách lớp và trẻ (gồm trẻ tạm nghỉ); hồ sơ trẻ (ngày sinh, giới tính); Parents App (Health & growth); lịch kỳ đo theo brand; chuẩn biểu đồ Singapore / Malaysia.

---

## Câu hỏi mở và giả định

| Mã | Nội dung | Trạng thái / Quyết định của BBA |
|---|---|---|
| OQ-01 *(sửa)* | Ngày bắt đầu và kết thúc từng kỳ của mỗi brand. | **Đã có dữ liệu:** file "Centre Terms Setup.xlsx" (BBA-489) ghi ngày bắt đầu Term 1–4 năm 2027 của từng brand; ngày kết thúc lấy trước ngày bắt đầu term sau một ngày, Term 4 hết 31/12 (AS-06) |
| OQ-02 | Chuẩn biểu đồ. | **Đã chốt:** SG — NHG Polyclinics; MY — Child Health Record Book (BBA-1059 Q1) |
| OQ-03 *(sửa)* | Khoảng hợp lệ và số chữ số thập phân. | Mở — BBA mới chốt đơn vị cm, kg (Q-71-05); file mẫu Taidii ghi số nguyên (94 cm, 13 kg) (BBA-529); DOTB có thể tự đặt |
| OQ-04 | Báo cáo HQ cần gì. | **Đã chốt:** chỉ trạng thái hoàn thành; CD, Admin, Cluster Head (BBA-1059 Q5) |
| OQ-05 | Có nhắc không. | **Đã chốt:** giữa tháng cuối mỗi quý, mọi brand (BBA-529) |
| OQ-06 *(mới)* | Nhắc gửi cho ai (Centre Director, School Admin, giáo viên lớp) và qua kênh nào? | Mở |
| OQ-07 *(sửa)* | Có biểu đồ tăng trưởng không, có hiện đường percentile (Taidii hiện 3rd / 50th / 97th) không? File câu hỏi Q-71-02 (09/11): bỏ BMI và percentile, chỉ cần height + weight; Plane BBA-1059 (13/11): gửi chuẩn biểu đồ SG / MY. Bản nháp và wireframe theo Plane. | Mở — cao |
| OQ-08 *(mới)* | Brighton đo theo học kỳ nhưng dùng Term 1–4 (Centre Terms Setup — BBA-489; file export Taidii — BBA-529). Brighton đo ở term nào (ví dụ Term 2 và Term 4)? Báo cáo completion có bỏ qua các term Brighton không đo không? | Mở |
| OQ-09 *(mới)* | "Health observations" (Parent App Requirements mục 19b) thuộc tính năng nào, có trong BBA-70 không? | Mở — thấp |
| AS-01 | HQ Admin thiết lập lịch kỳ đo. | Chờ OQ-01 |
| AS-02 | Khoảng hợp lệ tạm thời: chiều cao 40–150 cm, cân nặng 2–50 kg. | Chờ OQ-03 |
| AS-03 | Chiều cao và cân nặng nhập 1 chữ số thập phân. | — |
| AS-05 *(mới)* | "Giữa tháng" = ngày 15. | Chờ xác nhận |
| AS-06 *(mới)* | Ngày kết thúc một term là ngày trước ngày bắt đầu term sau; Term 4 kết thúc 31/12. | OQ-01 |
