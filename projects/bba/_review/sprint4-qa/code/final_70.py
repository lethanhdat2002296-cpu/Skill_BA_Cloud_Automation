import re, sys, shutil
from PIL import Image
S, P = sys.argv[1], sys.argv[2]
F = f'{P}/Document/FSD/Sprint 4/BBA-70_Growth_Termly_Height_Weight_VI.md'
old = open(F, encoding='utf-8').read()
d = open(f'{S}/frd-draft/BBA-70_Growth_US_Draft.md', encoding='utf-8').read()
def rep(s, a, b):
    assert s.count(a) == 1, a[:70]; return s.replace(a, b)
us = d[d.index('#### User Story'):d.index('\n---\n\n## Câu hỏi mở')].rstrip() + '\n'
us = '\n'.join(l for l in us.split('\n') if '*(bỏ)*' not in l)
us = re.sub(r' \*\((?:sửa|mới)[^)]*\)\*', '', us)
us = re.sub(r'^(\d+\.) \*\((?:sửa|mới)\)\* ', r'\1 ', us, flags=re.M)
assert '*(' not in us and '~~' not in us
us = rep(us, 'Danh sách lớp và trẻ (gồm trẻ tạm nghỉ); hồ sơ trẻ (ngày sinh, giới tính); Parents App (Health & growth); lịch kỳ đo theo brand; chuẩn biểu đồ Singapore / Malaysia.',
         'Danh sách lớp và trẻ (gồm trẻ vắng và tạm nghỉ); hồ sơ trẻ (ngày sinh, giới tính, IC / BC No., chương trình học); quy tắc che số giấy tờ theo vai trò (BBA-66); Parents App (Health & growth); lịch term theo brand (HQ Admin); chuẩn biểu đồ Singapore / Malaysia; thông báo nhắc.')
UIREF = '''#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-01 - Height & weight — nhập theo lớp | Wireframe: `Diagram/Wireframe/growth-height-weight-sprint4.html` (Nhập · Đã lưu · Xoá số đo) |
| SCR-02 - Height & weight — Year view, Export | Wireframe: `Diagram/Wireframe/growth-height-weight-sprint4.html` (Xem cả năm · Export) |
| SCR-03 - Child record — Health › Growth | Wireframe: `Diagram/Wireframe/growth-height-weight-sprint4.html` |
| SCR-04 - Height & weight completion | Wireframe: `Diagram/Wireframe/growth-height-weight-sprint4.html` |

![SCR-01 Height & weight — nhập theo lớp](../../../Diagram/Wireframe/png/SCR-01-growth-entry.png)

![SCR-02 Height & weight — Year view](../../../Diagram/Wireframe/png/SCR-02-growth-year.png)

![SCR-03 Child record — Health › Growth](../../../Diagram/Wireframe/png/SCR-03-child-growth.png)

![SCR-04 Height & weight completion](../../../Diagram/Wireframe/png/SCR-04-growth-completion.png)

'''
us = rep(us, '#### UI Components / Field Specification', UIREF + '#### UI Components / Field Specification')

head = old[:old.index('#### User Story')]
R = [
('| Phiên bản | 0.1 |', '| Phiên bản | 0.2 |'), ('| Ngày | 10/11/2026 |', '| Ngày | 13/11/2026 |'),
('HQ Ops. | HaiNguyen |\n', 'HQ Ops. | HaiNguyen |\n| 0.2 | 13/11/2026 | Business Analysis | Cập nhật theo câu trả lời của BBA (Plane BBA-529, BBA-1059, BBA-489, BBA-524; file câu hỏi phản hồi Sprint 4) và tệp đính kèm (file export "Quarterly Heights & Weight Report" của Taidii, bảng quyền Taidii, Parent App Requirements, Centre Terms Setup): bỏ BMI; biểu đồ theo chuẩn Singapore / Malaysia; Term 1–4 theo lịch term của brand do HQ đặt; trẻ vắng và tạm nghỉ ở nhóm riêng; lưu cả lớp không bị dòng lỗi chặn; xoá số đo; nhắc giữa tháng cuối mỗi term; báo cáo completion chỉ có trạng thái hoàn thành; Measurement history và biểu đồ trên hồ sơ trẻ; Year view và Export theo bố cục Taidii. Sửa FR-001 đến FR-004, FR-008, FR-009, BR-003, DATA-001, AC-001, AC-002, AC-007, AC-009; thêm FR-010 đến FR-013, BR-005, DATA-003, AC-011 đến AC-017, OQ-06 đến OQ-09, AS-05, AS-06; thêm wireframe SCR-01 đến SCR-04 và mục 9 Tài liệu tham khảo. | HaiNguyen |\n'),
('**Mức sẵn sàng:** Đã đặc tả màn nhập chiều cao, cân nặng theo lớp mỗi kỳ, cách tính BMI, cảnh báo số liệu bất thường, phụ huynh xem kết quả và báo cáo theo dõi cho HQ. 5 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.',
 '**Mức sẵn sàng:** Đã đặc tả màn nhập chiều cao, cân nặng theo lớp mỗi term, xem cả năm và xuất Excel, biểu đồ và lịch sử đo trên hồ sơ trẻ, xoá số đo, nhắc nhập, cảnh báo số liệu bất thường, phụ huynh xem ngay và báo cáo completion; có wireframe. 5 câu hỏi mở ở mục 7 cần BBA chốt (OQ-03, OQ-06 đến OQ-09).'),
('Mỗi kỳ, giáo viên đo chiều cao và cân nặng của trẻ trong lớp và ghi vào hệ thống một lần cho cả lớp. Hệ thống tự tính chỉ số BMI và vị trí trên biểu đồ tăng trưởng; phụ huynh xem được trong Parents App; HQ theo dõi Centre nào đã đo đủ.',
 'Mỗi term, giáo viên đo chiều cao và cân nặng của trẻ trong lớp và ghi vào hệ thống một lần cho cả lớp, thay cho báo cáo "Quarterly Heights & Weight Report" đang giữ trên Taidii. Hệ thống vẽ biểu đồ tăng trưởng theo chuẩn Singapore / Malaysia (không tính BMI); phụ huynh xem ngay trong Parents App; Centre Director, School Admin và Cluster Head theo dõi lớp nào đã đo đủ, vì nhiều Centre quên nhập khiến portfolio bị trống (BBA-1059 Q5).'),
('| Màn nhập theo lớp và kỳ đo: chiều cao, cân nặng, ngày đo. Tính BMI và vị trí trên biểu đồ tăng trưởng. Cảnh báo số liệu bất thường. Nhập cho một trẻ từ hồ sơ trẻ. Biểu đồ tăng trưởng trên hồ sơ trẻ và trong Parents App. Báo cáo theo dõi việc đo cho HQ. | Thiết bị đo kết nối tự động. Nhận xét dinh dưỡng, tư vấn sức khoẻ. Danh sách dị ứng (BBA-69). |',
 '| Màn nhập theo lớp và term: chiều cao, cân nặng, ngày đo; trẻ vắng và tạm nghỉ ở nhóm riêng. Year view theo năm và xuất Excel. Vị trí trên biểu đồ tăng trưởng. Cảnh báo số liệu bất thường. Nhập cho một trẻ từ hồ sơ trẻ. Xoá số đo. Biểu đồ và Measurement history trên hồ sơ trẻ và trong Parents App. Nhắc nhập giữa tháng cuối mỗi term. Báo cáo completion. | BMI (SRS Children & Families §1.2). Thống kê tăng trưởng trong báo cáo (BBA-1059 Q5). Thiết bị đo kết nối tự động. Nhận xét dinh dưỡng, tư vấn sức khoẻ. Danh sách dị ứng (BBA-69). |'),
('| Teacher / Senior Teacher | Lớp của mình. | Nhập và sửa số đo của trẻ lớp mình. |', '| Teacher / Senior Teacher | Lớp của mình. | Nhập, sửa, xoá số đo của trẻ lớp mình; xem cả năm, xuất Excel. |'),
('| Centre Director, School Admin | Centre của mình. | Nhập, sửa số đo; theo dõi lớp nào chưa đo. |', '| Centre Director, School Admin | Centre của mình. | Nhập, sửa, xoá số đo của mọi trẻ; xem báo cáo completion. |'),
('| HQ Admin | Mọi Centre. | Cấu hình kỳ đo; xem báo cáo theo dõi. |', '| HQ Admin | Mọi Centre. | Thiết lập lịch term theo brand. |'),
('| HQ Ops (District Manager, Operations Manager) | Các Centre mình phụ trách. | Xem báo cáo theo dõi. |', '| Cluster Head (trước đây District Manager — BBA-524) | Các Centre mình phụ trách. | Xem báo cáo completion. |'),
('| Phụ huynh (Parents App) | Con mình. | Xem số đo và biểu đồ tăng trưởng. |', '| Phụ huynh (Parents App) | Con mình. | Xem số đo, biểu đồ tăng trưởng và lịch sử đo ngay khi lưu. |'),
('| Hệ thống | Toàn hệ thống. | Tính tuổi, BMI, vị trí trên biểu đồ; lưu lịch sử. |', '| Hệ thống | Toàn hệ thống. | Tính tuổi, vị trí trên biểu đồ; nhắc nhập giữa tháng cuối mỗi term; lưu lịch sử. |'),
('| Health & allergies › Growth | Nhập số đo theo lớp và kỳ, biểu đồ tăng trưởng, báo cáo theo dõi. | US-001 |',
 '| Health & allergies › Growth | Nhập số đo theo lớp và term, Year view, xuất Excel. | US-001 |\n| Child record › Health › Growth | Biểu đồ tăng trưởng, Measurement history, nhập cho một trẻ. | US-001 |\n| Reports › Height & weight completion | Trạng thái hoàn thành theo Centre, lớp, term. | US-001 |'),
]
for a, b in R: head = rep(head, a, b)

tail = """## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Các term trong năm học bắt đầu và kết thúc ngày nào, theo từng brand? | HQ Ops | Cao | File "Centre Terms Setup.xlsx" (BBA-489): ngày bắt đầu Term 1–4 năm 2027 của từng brand; term do HQ đặt theo brand, Centre không sửa (Q-71-03). Ngày kết thúc theo AS-06. |
| OQ-02 | Biểu đồ tăng trưởng dùng chuẩn nào? | HQ Ops | Cao | Singapore: nghiên cứu nhân trắc của Singapore National Healthcare Group Polyclinics; Malaysia: Child Health Record Book (BBA-1059 Q1). |
| OQ-03 | Khoảng hợp lệ của chiều cao, cân nặng và số chữ số thập phân? | HQ Ops | Trung bình | Một phần: đơn vị cm, kg (Q-71-05). File mẫu Taidii ghi số nguyên (94 cm, 13 kg). Khoảng hợp lệ chưa chốt. |
| OQ-04 | Báo cáo theo dõi cần thêm gì ngoài số trẻ đã đo / chưa đo? | HQ Ops | Trung bình | Chỉ trạng thái hoàn thành; người dùng ban đầu: Centre Director, School Admin, Cluster Head (BBA-1059 Q5). |
| OQ-05 | Có nhắc khi gần hết term mà lớp chưa đo đủ không? | Centre Director / HQ Ops | Thấp | Nhắc giữa tháng cuối mỗi term (tháng 3, 6, 9, 12) cho mọi brand, kể cả Brighton (BBA-529, Q-71-03). |
| OQ-06 | Nhắc gửi cho ai (Centre Director, School Admin, giáo viên lớp) và qua kênh nào? | Centre Director / HQ Ops | Trung bình |  |
| OQ-07 | Có biểu đồ tăng trưởng không, có hiện đường percentile không? Q-71-02 (09/11): bỏ BMI và percentile, chỉ cần height + weight. BBA-1059 Q1 (13/11): gửi chuẩn biểu đồ Singapore / Malaysia. SRS Children & Families §4 mục 1.3: "View growth chart — height and weight against percentile curves". Taidii hiện vẽ 3 đường 3rd / 50th / 97th. FRD và wireframe đang theo BBA-1059. | HQ Ops | Cao |  |
| OQ-08 | Brighton Montessori đo theo học kỳ nhưng dùng Term 1–4 (Centre Terms Setup; file export Taidii). Brighton đo ở term nào? Báo cáo completion có bỏ qua các term Brighton không đo không? | HQ Ops | Trung bình |  |
| OQ-09 | "Health observations" (Parent App Requirements mục 19b) thuộc tính năng nào, có trong BBA-70 không? | HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | HQ Admin thiết lập lịch term theo brand. | FR-001 — đã xác nhận (Q-71-03) |
| AS-02 | Khoảng hợp lệ tạm thời: chiều cao 40–150 cm, cân nặng 2–50 kg, cho tới khi BBA chốt. | VAL-001 — chờ OQ-03 |
| AS-03 | Chiều cao và cân nặng nhập 1 chữ số thập phân. | FR-002 — chờ OQ-03 |
| AS-04 | Báo cáo completion đếm số trẻ đã đo / chưa đo theo term. | FR-009 — đã xác nhận (BBA-1059 Q5) |
| AS-05 | "Giữa tháng" là ngày 15. | FR-011 |
| AS-06 | Ngày kết thúc một term là ngày trước ngày bắt đầu term sau; Term 4 kết thúc 31/12. | FR-001 — OQ-01 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Term (kỳ đo) | Một trong 4 term của năm học (1/1–31/12) theo lịch term của brand do HQ đặt; Centre đo chiều cao, cân nặng cho trẻ một lần mỗi term. |
| Year view | Bảng một lớp, một năm: mỗi trẻ một dòng, Height cm / Weight kg của Term 1 đến Term 4 — cùng bố cục báo cáo "Quarterly Heights & Weight Report" của Taidii. |
| Measurement history | Danh sách mọi lần đo của một trẻ theo ngày đo, kèm người nhập. |
| Biểu đồ tăng trưởng | Biểu đồ so sánh chiều cao, cân nặng của trẻ với trẻ cùng tuổi, cùng giới tính, theo chuẩn Singapore (NHG Polyclinics) hoặc Malaysia (Child Health Record Book). |
| BMI | Chỉ số khối cơ thể; không dùng trong Phase 1 (SRS Children & Families §1.2). |
| Cluster Head | Tên mới của District Manager, cho cả Singapore và Malaysia (BBA-524). |

## 9. Tài liệu tham khảo

Số trang của SRS tính theo bản Word gốc khi xuất PDF. Tệp của BBA là tệp đính kèm trên Plane.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | BBA-SMS-SRS-Children-and-Families-v0.1 | §1.1 In scope; §1.2 Not in Phase 1 (BMI) | 3 | Mục 3 — phạm vi, bỏ BMI. |
| 2 | BBA-SMS-SRS-Children-and-Families-v0.1 | §3 P7 Height and weight | 5 | Luồng chính; FR-002, FR-003, FR-004. |
| 3 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.3 Health & allergies (Record height and weight, Bulk record height and weight, View growth chart) | 7 | FR-001, FR-004, FR-007; OQ-07. |
| 4 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Business rules › Health and allergies (BR-CHF-026) | 9 | BR-001 — ghi trực tiếp, không cần duyệt. |
| 5 | BBA-SMS-SRS-Children-and-Families-v0.1 | §8 Acceptance criteria (AC-CHF-011 Bulk height and weight) | 12 | AC-001. |
| 6 | BBA-SMS-SRS-Parents-App-v0.1 | §4.1 Health (View height and weight, View measurement history) | 9 | FR-008, FR-012, BR-004. |
| 7 | Plane — BBA-1059 "BBA input: Height and weight – growth chart, absent children, deleting, parent view, HQ report" | Q1 chuẩn biểu đồ; Q2 trẻ vắng / tạm nghỉ; Q3 xoá số đo, một quyền chung; Q4 phụ huynh thấy ngay; Q5 báo cáo completion | — | FR-002, FR-004, FR-008, FR-009, FR-010, BR-005; OQ-02, OQ-04. |
| 8 | Plane — BBA-1059, tệp đính kèm "Taidii - Center Staff Role permissions.xlsx" | Sheet "Center Staff Role", dòng 14 "Update Height and Weight" | — | BR-005. |
| 9 | Plane — BBA-1059, tệp đính kèm "Parent App Requirements Provided to DotB (30 July 2026).pdf" | Mục 19 Child Health Records | 3–4 | FR-008, FR-012; OQ-09. |
| 10 | Plane — BBA-1059, ảnh Taidii Parents App "Height & Weight" | Biểu đồ chiều cao theo tuổi, 3 đường 3rd / 50th / 97th, chuẩn WHO | — | FR-004; OQ-07. |
| 11 | Plane — BBA-529 "BBA input: Height and weight records today" | Lịch đo theo brand (Brighton theo học kỳ), nhắc giữa tháng cuối quý cho mọi brand | — | FR-001, FR-011; OQ-05, OQ-08. |
| 12 | Plane — BBA-529, tệp đính kèm "Student_quarterly_height_weight_2026-sample.xlsx" | Quarterly Heights & Weight Report (Brighton Montessori Frankel, Class N2) | — | FR-013; OQ-03, OQ-08. |
| 13 | Plane — BBA-489, tệp đính kèm "Centre Terms Setup.xlsx" | Sheet "Term Setup" (ngày bắt đầu Term 1–4 năm 2027 theo brand) | — | FR-001; OQ-01, OQ-08; AS-06. |
| 14 | Plane — BBA-524 "BBA input: Approval matrix" | District Manager đổi tên thành Cluster Head | — | Mục 4. |
| 15 | BBA_SMS_S4 — Tổng hợp câu hỏi phản hồi, sheet "Tổng hợp" | Đã chốt: Q-71-02, Q-71-03, Q-71-06, Q-71-07, Q-71-10 · Một phần: Q-71-05, Q-71-08 · DOTB quyết định: Q-71-09 · Chưa phản hồi: Q-71-04, Q-71-11, Q-71-12 | — | FR-001, FR-002, FR-003, FR-011, FR-012, BR-005; OQ-03, OQ-07. |
| 16 | Plane — dự án BBA Phase 1, ticket BBA-70 (WBS 3.1.3.03) | Growth – termly height & weight entry by class | — | Phạm vi tính năng. |
"""
open(F, 'w', encoding='utf-8').write(head + us + '\n' + tail)

W = f'{P}/Diagram/Wireframe'
shutil.copy(f'{S}/by-frd/BBA-70/wireframe.html', f'{W}/growth-height-weight-sprint4.html')
for a, b in [('BBA-70-1--default', 'SCR-01-growth-entry'), ('BBA-70-1--saved', 'SCR-01-growth-entry--saved'), ('BBA-70-1--delete', 'SCR-01-growth-entry--delete'),
             ('BBA-70-1--year', 'SCR-02-growth-year'), ('BBA-70-3--default', 'SCR-03-child-growth'), ('BBA-70-2--default', 'SCR-04-growth-completion')]:
    Image.open(f'{S}/png/{a}.png').convert('RGB').quantize(colors=128, method=Image.Quantize.MEDIANCUT).save(f'{W}/png/{b}.png', optimize=True)
print('ok')
