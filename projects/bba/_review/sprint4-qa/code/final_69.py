import re, sys, shutil
from PIL import Image
S, P = sys.argv[1], sys.argv[2]   # scratch review dir, projects/bba dir
F = f'{P}/Document/FSD/Sprint 4/BBA-69_Allergies_List_VI.md'
old = open(F, encoding='utf-8').read()
d = open(f'{S}/frd-draft/BBA-69_Allergies_List_US_Draft.md', encoding='utf-8').read()

us = d[d.index('#### User Story'):d.index('\n---\n\n## Câu hỏi mở')].rstrip() + '\n'
us = '\n'.join(l for l in us.split('\n') if '*(bỏ)*' not in l)
us = re.sub(r' \*\((?:sửa|mới)[^)]*\)\*', '', us)
us = re.sub(r'^(\d+\.) \*\((?:sửa|mới)\)\* ', r'\1 ', us, flags=re.M)
assert '*(' not in us and '~~' not in us, re.findall(r'.{30}\*\(.{20}', us)
def rep(s, a, b):
    assert s.count(a) == 1, a[:60]; return s.replace(a, b)
us = rep(us, ' Cách hiển thị do DOTB quyết định.', ' Mỗi dòng có "Contact the family".')
us = rep(us, 'Health record (phụ huynh khai trong Parents App, CD / Admin hoàn tất đánh giá — BBA-68); quyền xem chi tiết y tế (Roles & permissions); hồ sơ trẻ.',
         'Medical Care Assessment (phụ huynh khai trong Parents App, Centre Director / Admin hoàn tất đánh giá — BBA-68); đánh giá lại 6 tháng (BBA-68); quyền xem chi tiết y tế (Roles & permissions); hồ sơ trẻ; BBA-68 (quy tắc mức cảnh báo).')
UIREF = '''#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-01 - Allergies & conditions (Medical Health Alert List) | Wireframe: `Diagram/Wireframe/allergies-list-sprint4.html` |
| SCR-02 - Print for the kitchen | Wireframe: `Diagram/Wireframe/allergies-list-sprint4.html` (trạng thái "Bản in cho bếp") |

![SCR-01 Allergies & conditions — toàn Centre](../../../Diagram/Wireframe/png/SCR-01-allergies-list.png)

![SCR-01 Allergies & conditions — lọc một lớp](../../../Diagram/Wireframe/png/SCR-01-allergies-list--class.png)

![SCR-02 Print for the kitchen](../../../Diagram/Wireframe/png/SCR-02-kitchen-print.png)

'''
us = rep(us, '#### UI Components / Field Specification', UIREF + '#### UI Components / Field Specification')

head = old[:old.index('#### User Story')]
head = rep(head, '| Phiên bản | 0.1 |', '| Phiên bản | 0.2 |')
head = rep(head, '| Ngày | 10/11/2026 |', '| Ngày | 13/11/2026 |')
head = rep(head, '| HaiNguyen |\n\n**Mức sẵn sàng:**', '''| HaiNguyen |
| 0.2 | 13/11/2026 | Business Analysis | Cập nhật theo câu trả lời của BBA (Plane BBA-1058, file câu hỏi phản hồi Sprint 4) và form Medical Care Assessment Checklist / Review (đính kèm BBA-1058): cột theo các trường của form (loại, triệu chứng, điều kiện dung nạp, vết trứng / hạt, kế hoạch xử trí, thuốc); Teacher được in / xuất, không lưu nhật ký in / xuất; chỉ hiện trẻ có phụ huynh đồng ý hiện tên và ảnh; theo dõi hạn đánh giá lại 6 tháng; giữ thông tin đã xác nhận khi phụ huynh sửa; nhóm "Health information not provided". Sửa FR-001 đến FR-004, FR-007, FR-008, BR-001, BR-003, BR-004, DATA-001; thêm FR-011 đến FR-014, BR-005, BR-006, DATA-003, AC-012 đến AC-016, OQ-05 đến OQ-09, AS-04; bỏ FR-006, DATA-002, AC-004 (không dùng lại mã); thêm wireframe SCR-01, SCR-02. | HaiNguyen |

**Mức sẵn sàng:**''')
head = rep(head, '**Mức sẵn sàng:** Đã đặc tả danh sách dị ứng theo Centre / lớp, thứ tự theo mức độ, lọc, in cho bếp, xuất file và quyền xem. 4 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.',
 '**Mức sẵn sàng:** Đã đặc tả danh sách dị ứng theo Centre / lớp theo các trường của form Medical Care Assessment, thứ tự theo mức độ, hạn đánh giá lại, lọc, in cho bếp, xuất file và quyền xem; có wireframe. 8 câu hỏi mở ở mục 7 cần BBA chốt.')
head = rep(head, 'Nội dung lấy từ Health record do phụ huynh khai; nhân viên không gõ lại.',
 'Nội dung lấy từ Medical Care Assessment do phụ huynh khai và Centre Director / Senior Staff xác nhận; nhân viên không gõ lại. Trên form của BBA, danh sách này gọi là "Medical Overview / Medical Health Alert List".')
head = rep(head, '| Danh sách dị ứng theo Centre và lớp, trẻ nặng nhất lên đầu. Các cột: trẻ, lớp, chất gây dị ứng, mức độ, phản ứng, cách xử trí, nơi để thuốc khẩn cấp (EpiPen), ghi chú của nhân viên, ngày phụ huynh cập nhật. Phần riêng cho trẻ chỉ có bệnh hoặc chế độ ăn đặc biệt. Tìm kiếm, lọc, in cho bếp, xuất file. Quyền xem theo vai trò. | Phụ huynh nhập và sửa Health record (Parents App). Cảnh báo đỏ trên hồ sơ trẻ và các danh sách khác (BBA-68). Biểu đồ tăng trưởng (BBA-70). Khai báo và ghi nhận cho trẻ uống thuốc. |',
 '| Danh sách dị ứng theo Centre và lớp, trẻ nặng nhất lên đầu. Các cột theo form Medical Care Assessment Checklist: trẻ (ảnh), lớp, loại, chất gây dị ứng, mức độ, triệu chứng, điều kiện dung nạp, vết trứng / hạt, kế hoạch xử trí và thuốc dùng ngay, hạn đánh giá lại, ghi chú của nhân viên. Phần riêng cho trẻ chỉ có bệnh hoặc chế độ ăn đặc biệt; nhóm trẻ chưa khai thông tin sức khoẻ. Tìm kiếm, lọc, in cho bếp, xuất file. Quyền xem theo vai trò. | Phụ huynh nhập và sửa Medical Care Assessment (Parents App); quy trình đánh giá và đánh giá lại 6 tháng (BBA-68). Cảnh báo đỏ trên hồ sơ trẻ và các danh sách khác (BBA-68). Biểu đồ tăng trưởng (BBA-70). Khai báo và ghi nhận cho trẻ uống thuốc. |')
head = rep(head, '| Teacher / Senior Teacher | Lớp của mình. | Xem danh sách lớp mình, in cho bếp. |', '| Teacher / Senior Teacher | Lớp của mình. | Xem danh sách lớp mình, in cho bếp, xuất file. |')
head = rep(head, '| Phụ huynh (Parents App) | Con mình. | Nguồn duy nhất của thông tin dị ứng. |', '| Phụ huynh (Parents App) | Con mình. | Khai thông tin dị ứng; đồng ý cho hiện tên và ảnh trên Medical Health Alert List. |')
head = rep(head, '| Hệ thống | Toàn hệ thống. | Sắp xếp theo mức độ, ghi thời điểm in, lưu lại các lần xuất file. |', '| Hệ thống | Toàn hệ thống. | Sắp xếp theo mức độ, ghi thời điểm in, tính hạn đánh giá lại. |')
head = rep(head, 'Quy tắc chung: chỉ vai trò được phép xem chi tiết y tế mới mở được danh sách này (mặc định Centre Director, Teacher, School Admin, HQ Admin); mọi lần xuất file được lưu lại (ai xuất, lúc nào).',
 'Quy tắc chung: chỉ vai trò được phép xem chi tiết y tế mới mở được danh sách này (mặc định Centre Director, Teacher, School Admin, HQ Admin); không lưu nhật ký in / xuất (BBA-1058 Q2).')
head = rep(head, '| Children & families › Health & allergies | Danh sách dị ứng theo Centre / lớp, in cho bếp, xuất file. | US-001 |', '| Children & families › Health & allergies | Danh sách dị ứng theo Centre / lớp (Medical Health Alert List), in cho bếp, xuất file. | US-001 |')
us = rep(us, 'để tôi và bếp biết ngay trẻ nào cần tránh món gì.', 'để tôi và bếp biết ngay trẻ nào cần tránh món gì và xử lý ra sao khi trẻ có phản ứng.')

tail = """## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Phản ứng, cách xử trí và nơi để thuốc khẩn cấp có thành trường riêng không? | Centre Director / HQ Ops | Cao | Form Medical Care Assessment Checklist có trường riêng Symptoms, Steps to follow, Medication for immediate administration → đã tách cột. Nơi để thuốc chuyển sang OQ-02. |
| OQ-02 | Nơi để thuốc khẩn cấp có cần ghi không, ai ghi? Form chỉ có "Medication Held On Site Form Has Been Completed? Yes / Not Applicable". | Centre Director / HQ Ops | Cao |  |
| OQ-03 | Bếp dùng bản in hay có tài khoản xem trên máy; được xem dữ liệu nhận dạng nào? | Centre Director / HQ Ops | Trung bình |  |
| OQ-04 | Bản in cho bếp dùng các cột Photo, Child, Type · allergen · severity, Can tolerate, Traces of eggs / nuts, Emergency action plan; có cần thêm Menu modifications không? | Centre Director / HQ Ops | Thấp |  |
| OQ-05 | "Chưa ký đồng ý thì không hiện" áp cho toàn bộ thông tin sức khoẻ (giáo viên cũng không thấy) hay chỉ tên / ảnh trên danh sách và bản in? Ẩn toàn bộ có rủi ro an toàn. | Centre Director / HQ Ops | Cao |  |
| OQ-06 | Thang mức độ có cần cấu hình theo brand / Centre ngay Phase 1 không? | HQ Ops | Trung bình |  |
| OQ-07 | Medical condition, medical history nằm chung danh sách dị ứng hay nhóm riêng? Form vừa có "Medical Condition" trong Type of Allergies, vừa có mục "Medical Conditions & History" riêng. FRD đang để nhóm riêng. | Centre Director / HQ Ops | Trung bình |  |
| OQ-08 | Can tolerate, traces of eggs / nuts, menu modifications do phụ huynh khai trong Parents App hay Centre ghi khi đánh giá ("Menu reviewed with parents")? | Centre Director / HQ Ops | Trung bình |  |
| OQ-09 | Tên màn hình dùng "Allergies & conditions" hay theo form "Medical Health Alert List"? | HQ Ops | Thấp |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Bếp nhận bản in do Centre đưa; nhân viên bếp không có tài khoản. | Mục 4 — chờ OQ-03 |
| AS-02 | Mỗi trẻ một dòng; trẻ có nhiều dị ứng thì liệt kê các chất trong cùng dòng. | FR-001 |
| AS-03 | Trẻ đang tạm nghỉ không có trong danh sách vì không đến trường. | FR-010 |
| AS-04 | Bản in chỉ ghi ngày giờ in, không ghi tên người in. | FR-007; BR-003 |

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Medical Care Assessment | Form thông tin sức khoẻ của trẻ (Medical Care Assessment Checklist): loại dị ứng, chất gây dị ứng, mức độ, triệu chứng, điều kiện dung nạp, yêu cầu chăm sóc hằng ngày, kế hoạch xử trí, thuốc, bác sĩ, đồng ý của phụ huynh. Phụ huynh khai, Centre Director hoặc Senior Staff kiểm tra và xác nhận. |
| Medical Health Alert List | Tên danh sách y tế trên form của BBA ("Medical Overview / Medical Health Alert List"); trong hệ thống là màn Allergies & conditions. |
| Mức độ dị ứng | Mild (nhẹ), Moderate (vừa), Severe (nặng — tương ứng "Life Threatening" trên form của BBA). |
| Next review | Ngày đánh giá lại Medical Care Assessment (Date of Next Review), tối đa 6 tháng sau lần đánh giá gần nhất. |
| Can tolerate | Điều kiện trẻ vẫn dùng được chất gây dị ứng (ví dụ ăn được bánh nướng có trứng nhưng không ăn trứng luộc). |
| EpiPen | Bút tiêm adrenaline dùng khi trẻ bị sốc phản vệ. |
| Ghi chú của nhân viên | Ghi chú do nhân viên Centre thêm ở tab Health, tách khỏi thông tin phụ huynh khai. |
"""
open(F, 'w', encoding='utf-8').write(head + us + '\n' + tail)

# wireframe + PNG
shutil.copy(f'{S}/by-frd/BBA-69/wireframe.html', f'{P}/Diagram/Wireframe/allergies-list-sprint4.html')
for a, b in [('BBA-69--default', 'SCR-01-allergies-list'), ('BBA-69--class', 'SCR-01-allergies-list--class'), ('BBA-69--print', 'SCR-02-kitchen-print')]:
    im = Image.open(f'{S}/png/{a}.png').convert('RGB').quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    im.save(f'{P}/Diagram/Wireframe/png/{b}.png', optimize=True)
print('ok')
