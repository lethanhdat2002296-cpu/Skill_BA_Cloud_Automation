import re, sys, shutil
from PIL import Image
S, P = sys.argv[1], sys.argv[2]
F = f'{P}/Document/FSD/Sprint 4/BBA-71_Consent_Status_Per_Child_VI.md'
old = open(F, encoding='utf-8').read()
d = open(f'{S}/frd-draft/BBA-71_Consent_US_Draft.md', encoding='utf-8').read()
def rep(s, a, b):
    assert s.count(a) == 1, a[:70]; return s.replace(a, b)
us = d[d.index('#### User Story'):d.index('\n---\n\n## Câu hỏi mở')].rstrip() + '\n'
us = '\n'.join(l for l in us.split('\n') if '*(bỏ)*' not in l)
us = re.sub(r' \*\((?:sửa|mới)[^)]*\)\*', '', us)
us = re.sub(r'^(\d+\.) \*\((?:sửa|mới)\)\* ', r'\1 ', us, flags=re.M)
assert '*(' not in us and '~~' not in us, re.findall(r'.{40}\*\(.{20}', us)
UIREF = '''#### UI Reference (Tham chiếu giao diện)

| Mã màn hình / Phiên bản | Tham chiếu / Link |
|---|---|
| SCR-01 - Child record — Consents | Wireframe: `Diagram/Wireframe/consent-status-sprint4.html` (Tab Consents) |
| SCR-02 - Surveys & consents — danh sách consent | Wireframe: `Diagram/Wireframe/consent-status-sprint4.html` (Danh sách consent · Chưa trả lời) |
| SCR-03 - New consent | Wireframe: `Diagram/Wireframe/consent-status-sprint4.html` (Tạo consent) |
| SCR-04 - Publish new version | Wireframe: `Diagram/Wireframe/consent-status-sprint4.html` (Phiên bản mới) |
| SCR-05 - Consent compliance | Wireframe: `Diagram/Wireframe/consent-status-sprint4.html` |

![SCR-01 Child record — Consents](../../../Diagram/Wireframe/png/SCR-01-child-consents.png)

![SCR-02 Surveys & consents — danh sách consent](../../../Diagram/Wireframe/png/SCR-02-consent-list.png)

![SCR-03 New consent](../../../Diagram/Wireframe/png/SCR-03-new-consent.png)

![SCR-04 Publish new version](../../../Diagram/Wireframe/png/SCR-04-consent-new-version.png)

![SCR-05 Consent compliance](../../../Diagram/Wireframe/png/SCR-05-consent-compliance.png)

'''
us = rep(us, '#### UI Components / Field Specification', UIREF + '#### UI Components / Field Specification')

head = old[:old.index('#### User Story')]
R = [
('| Phiên bản | 0.1 |', '| Phiên bản | 0.2 |'), ('| Ngày | 10/11/2026 |', '| Ngày | 13/11/2026 |'),
('HQ Ops. | HaiNguyen |\n', 'HQ Ops. | HaiNguyen |\n| 0.2 | 13/11/2026 | Business Analysis | Cập nhật theo câu trả lời của BBA (file câu hỏi phản hồi Sprint 4 Q-73; Plane BBA-488, BBA-492) và file "Consent Types" (đính kèm BBA-488): Centre Director tạo và gửi consent theo lớp hoặc cả Centre, luôn kèm Announcement có link, email chỉ gửi khi chọn; loại và vòng đời consent (thu một lần lúc nhập học / theo sự kiện / Crossroad gia hạn hằng năm); nhiều consent cùng loại mỗi cái gắn một sự kiện; người nhận cả hai phụ huynh hoặc chỉ người liên hệ chính; tick checklist học sinh; thẻ "x of y families answered"; tuỳ chọn đồng ý lại khi có phiên bản mới; Consent compliance. Sửa FR-001, FR-003, FR-004, FR-005, FR-007, FR-009, BR-004, VAL-001, DATA-001, AC-001, AC-003, AC-004, AC-006 đến AC-008, AC-010; thêm FR-012 đến FR-014, BR-006, BR-007, VAL-004, AC-015 đến AC-019, OQ-06 đến OQ-10, AS-05; bỏ AS-02, AS-04 (mã cũ không dùng lại); thêm wireframe SCR-01 đến SCR-05 và mục 9 Tài liệu tham khảo. | HaiNguyen |\n'),
('**Mức sẵn sàng:** Đã đặc tả bảng trạng thái consent của từng trẻ, gửi và nhắc phụ huynh, ghi nhận câu trả lời, phiên bản và hết hạn. 5 câu hỏi mở ở mục 7 cần Centre Director / HQ Ops chốt.',
 '**Mức sẵn sàng:** Đã đặc tả tạo và gửi consent theo lớp / Centre, trạng thái consent của từng trẻ, nhắc và gửi lại, ghi nhận câu trả lời, phiên bản, vòng đời theo loại, thẻ tỷ lệ trả lời và Consent compliance; có wireframe. 6 câu hỏi mở ở mục 7 cần BBA chốt (OQ-04, OQ-05, OQ-07 đến OQ-10).'),
('Centre cần biết với từng trẻ: phụ huynh đã đồng ý những gì (ví dụ cho phép dùng ảnh của trẻ, cho trẻ đi tham quan), chưa trả lời những gì, và gửi hoặc nhắc lại ngay từ hồ sơ trẻ. Mỗi câu trả lời được lưu kèm phụ huynh nào trả lời, ngày nào, qua kênh nào.',
 'Centre cần biết với từng trẻ: phụ huynh đã đồng ý những gì (ví dụ cho phép dùng ảnh của trẻ, cho trẻ đi tham quan), chưa trả lời những gì, và nhắc lại ngay từ hồ sơ trẻ. Privacy policy, Medical authorisation và Media release được thu một lần lúc nhập học; các consent theo sự kiện (Field trip, Ad hoc) và Crossroad do Centre Director tạo ở Surveys & consents và gửi cho lớp hoặc cả Centre kèm Announcement. Mỗi câu trả lời được lưu kèm phụ huynh nào trả lời, ngày nào, qua kênh nào.'),
('Mục tiêu đo được: từ hồ sơ trẻ, nhân viên thấy trạng thái của mọi loại consent trong một bảng và gửi lại yêu cầu bằng một thao tác.',
 'Mục tiêu đo được: từ hồ sơ trẻ, nhân viên thấy trạng thái của mọi consent trong một bảng và nhắc hoặc gửi lại bằng một thao tác; với mỗi consent đã gửi, Centre Director thấy ngay bao nhiêu gia đình đã trả lời.'),
('| Bảng consent của từng trẻ: loại consent, phiên bản, trạng thái, ngày gửi, số lần nhắc, ngày trả lời, người trả lời, kênh trả lời. Gửi yêu cầu, nhắc lại, gửi lại khi đã hết hạn hoặc phụ huynh không đồng ý. Ghi nhận câu trả lời và việc rút lại consent. | Soạn biểu mẫu consent và gửi cho cả lớp / Centre (Communication › Surveys & consents). Khảo sát có thu phí. |',
 '| Bảng consent của từng trẻ: loại, sự kiện, phiên bản, trạng thái, câu trả lời hoặc lần nhắc gần nhất, ngày đóng. Tạo consent và gửi cho lớp hoặc cả Centre (Surveys & consents), kèm Announcement; tuỳ chọn gửi email. Nhắc, gửi lại khi hết hạn hoặc phụ huynh không đồng ý. Thẻ "x of y families answered". Công bố phiên bản mới. Ghi nhận câu trả lời, rút lại consent, tick checklist học sinh. Consent compliance. | Khảo sát (Survey) và khảo sát có thu phí. Nội dung consent thu lúc nhập học trong registration form (Enrolment). Chặn gắn tên trẻ trong ảnh (Teacher App, theo BR-005). |'),
('| Centre Director, School Admin | Centre của mình. | Xem; gửi, nhắc, gửi lại yêu cầu consent (theo quyền, mặc định bật cho Centre Director). |',
 '| Centre Director | Centre của mình. | Tạo và gửi consent cho các lớp hoặc cả Centre; xem, nhắc, gửi lại; xem Consent compliance. |\n| School Admin | Centre của mình. | Như Centre Director khi được cấp quyền (Roles & permissions). |'),
('| Teacher | Lớp của mình. | Xem trạng thái consent của trẻ lớp mình. |', '| Teacher | Lớp của mình. | Chỉ xem trạng thái consent của trẻ lớp mình. |'),
('| HQ Admin | Mọi Centre. | Mọi quyền. |', '| HQ Admin | Mọi Centre. | Mọi quyền; công bố phiên bản mới của consent. |\n| HQ Marketing | Mọi Centre. | Nhận thông báo khi phụ huynh rút lại Media release. |'),
('| Hệ thống | Toàn hệ thống. | Gửi yêu cầu, đếm số lần nhắc, chuyển trạng thái hết hạn, lưu lịch sử. |',
 '| Hệ thống | Toàn hệ thống. | Tạo Announcement kèm link, tự nhắc 1 ngày trước ngày đóng, đếm số lần nhắc, chuyển Expired, tick checklist học sinh, lưu lịch sử. |'),
('| Hồ sơ trẻ › Documents & consents | Trạng thái consent của trẻ, gửi và nhắc yêu cầu. | US-001 |',
 '| Hồ sơ trẻ › Documents › Consents | Trạng thái consent của trẻ, nhắc, gửi lại, lịch sử. | US-001 |\n| Communication › Surveys & consents | Tạo và gửi consent, thẻ "x of y families answered", công bố phiên bản mới. | US-001 |\n| Daily operations › Safety overview › Consent compliance | Trẻ còn thiếu consent theo Centre, lớp. | US-001 |'),
]
for a, b in R: head = rep(head, a, b)

tail = """## 7. Câu hỏi mở

| Mã câu hỏi | Quyết định cần có | Người quyết định | Ưu tiên | Quyết định của BBA |
|---|---|---|---|---|
| OQ-01 | Danh sách loại consent và nội dung từng loại; có khác theo brand không? | Centre Director / HQ Ops | Cao | Loại: Privacy policy, Medical authorisation, Media release (thu lúc nhập học), Field trip / learning journey, Ad hoc (theo sự kiện), Crossroad (Q-73-04). Nội dung: file "Consent Types" (BBA-488) — Privacy Policy, Media Consent, Medical, Outing, Accuracy of Information, "Initial setup for all brands". Xem OQ-10. |
| OQ-02 | "Expired" nghĩa là gì; thời hạn hiệu lực của từng loại? | Centre Director / HQ Ops | Cao | Theo vòng đời từng loại (Q-73-12) → FR-007. |
| OQ-03 | Khi consent có phiên bản mới, có cần đồng ý lại không? | Business Owner | Cao | Tuỳ từng lần cập nhật (BBA-488) → FR-006. |
| OQ-04 | Nhắc thủ công hay tự động; giới hạn số lần và khoảng cách? | Centre Director / HQ Ops | Thấp |  |
| OQ-05 | Phụ huynh trả lời qua email có cần ký không? | Business Owner | Trung bình | Email chỉ là kênh báo kèm, phụ huynh trả lời trong app (Q-73-08); câu hỏi còn mở nếu sau này cho trả lời qua email. |
| OQ-06 | Gửi consent ở đâu, ai gửi? | Centre Director / HQ Ops | Cao | Centre Director gửi theo lớp hoặc cả Centre ở Surveys & consents (Q-73-04); hồ sơ trẻ chỉ xem, nhắc, gửi lại. |
| OQ-07 | Consent gửi sau (Field trip, Ad hoc, Crossroad) cần một hay cả hai phụ huynh đồng ý? Form đăng ký cần 2 chữ ký. | Business Owner | Cao |  |
| OQ-08 | Gia hạn Crossroad đầu năm học do hệ thống tạo tự động hay Centre tạo tay? | Centre Director / HQ Ops | Trung bình |  |
| OQ-09 | Ai đánh dấu Centre "không có sân ngoài trời" và đánh dấu ở đâu? | HQ Ops | Trung bình |  |
| OQ-10 | File "Consent Types" có "Accuracy of Information" và "Outing" (thu lúc nhập học); FRD chưa có Accuracy of Information và dùng Field trip theo sự kiện. "Accuracy of Information" có là một loại consent không? "Outing" thu lúc nhập học khác Field trip theo sự kiện thế nào? | Centre Director / HQ Ops | Trung bình |  |

### Giả định của BA (cần xác nhận cùng mục 7)

| Mã | Giả định | Dùng ở |
|---|---|---|
| AS-01 | Có trạng thái Withdrawn cho consent phụ huynh đã rút lại. | FR-002; FR-009 |
| AS-03 | Expired là qua ngày đóng (Field trip, Ad hoc) hoặc hết năm học (Crossroad). | FR-007 — theo Q-73-12 |
| AS-05 | Bảng Consents nằm ở tab Documents của hồ sơ trẻ; SRS Children & Families liệt kê tab Consents riêng. | FR-001 — chờ xác nhận |

Bằng chứng lưu (Q-73-15) và cách đếm lần nhắc (Q-73-10) do DOTB quyết định, theo DATA-002 và FR-004.

## 8. Phụ lục

### Phụ lục A. Thuật ngữ

| Thuật ngữ | Định nghĩa trong FRD này |
|---|---|
| Consent | Sự đồng ý của phụ huynh cho một việc cụ thể, ví dụ cho phép dùng ảnh của trẻ hoặc cho trẻ đi tham quan. |
| Phiên bản | Lần sửa nội dung của một consent; người công bố chọn có yêu cầu đồng ý lại hay không. |
| Ngày đóng (Closing date) | Hạn trả lời của consent theo sự kiện; qua ngày này dòng chưa trả lời chuyển Expired. |
| Crossroad | Consent cho trẻ qua đường (road crossing), chỉ cho Centre Singapore không có sân ngoài trời, gia hạn hằng năm. |
| Consent compliance | Danh sách trẻ còn thiếu consent, đọc từ consent của từng trẻ. |
| PDPA | Luật bảo vệ dữ liệu cá nhân. |

## 9. Tài liệu tham khảo

Số trang của SRS tính theo bản Word gốc khi xuất PDF. Tệp của BBA là tệp đính kèm trên Plane.

| STT | Tài liệu | Mục | Trang | Dùng cho |
|---|---|---|---|---|
| 1 | BBA-SMS-SRS-Children-and-Families-v0.1 | §1.2 Not in Phase 1 (consent quản lý ở Communication › Surveys & consents) | 3 | Mục 3. |
| 2 | BBA-SMS-SRS-Children-and-Families-v0.1 | §4 mục 1.1 Children (View child profile — tab Consents; View consents) | 6 | FR-001; AS-05. |
| 3 | BBA-SMS-SRS-Children-and-Families-v0.1 | §5 Business rules (BR-CHF-010) | 9 | FR-001 — hồ sơ trẻ chỉ đọc consent. |
| 4 | BBA-SMS-SRS-Communication-v0.1 | §3 P6 Consent | 5 | Luồng chính; FR-003, FR-009. |
| 5 | BBA-SMS-SRS-Communication-v0.1 | §4 mục 4.2 Consents (View consent list, Create consent form, Respond, Withdraw, Edit, View consent record) | 8 | FR-003, FR-005, FR-009, FR-010, FR-012. |
| 6 | BBA-SMS-SRS-Communication-v0.1 | §5 Business rules (BR-COM-002, BR-COM-016, BR-COM-039, BR-COM-043, BR-COM-044) | 9–10 | Mục 4; FR-004, FR-005, FR-009; BR-001, BR-003. |
| 7 | BBA-SMS-SRS-Parents-App-v0.1 | §5.1 Announcements (Open linked survey); §5.4 Surveys & consents | 10–12 | FR-003, FR-005, FR-009. |
| 8 | BBA-SMS-SRS-Teacher-App-v0.1 | §5.4 Survey & consent; §5 Business rules (BR-TCH-030, BR-TCH-054) | 11, 13–14 | BR-004, BR-005. |
| 9 | BBA-SMS-SRS-Daily-Operations-v0.1 | §4.2 Safety overview (View consent gaps) | 9 | FR-011. |
| 10 | Plane — BBA-488 "BBA input: Consent types and wording" | Consent thu lúc nhập học; Media consent; đồng ý lại khi đổi nội dung | — | FR-006, FR-007; BR-005; OQ-03. |
| 11 | Plane — BBA-488, tệp đính kèm "Consent Types.xlsx" | Sheet Privacy Policy, Media Consent, Medical, Outing, Accuracy of Information | — | OQ-01, OQ-10. |
| 12 | Plane — BBA-492 "BBA input: Additional document templates" | Consent request letter không dùng, phụ huynh đã đồng ý qua registration form | — | Mục 2; BR-006. |
| 13 | BBA_SMS_S4 — Tổng hợp câu hỏi phản hồi, sheet "Tổng hợp" | Q-73-04 đến Q-73-15 | — | FR-001, FR-003, FR-005, FR-007, FR-009, FR-012 đến FR-014; BR-004 đến BR-007; OQ-04 đến OQ-09. |
| 14 | Plane — dự án BBA Phase 1, ticket BBA-71 (WBS 3.1.4.01) | Consent status per child & send consent request | — | Phạm vi tính năng. |
"""
open(F, 'w', encoding='utf-8').write(head + us + '\n' + tail)
W = f'{P}/Diagram/Wireframe'
shutil.copy(f'{S}/by-frd/BBA-71/wireframe.html', f'{W}/consent-status-sprint4.html')
for a, b in [('BBA-71-1--default', 'SCR-01-child-consents'), ('BBA-71-1--list', 'SCR-02-consent-list'), ('BBA-71-1--unanswered', 'SCR-02-consent-list--unanswered'),
             ('BBA-71-1--new', 'SCR-03-new-consent'), ('BBA-71-1--version', 'SCR-04-consent-new-version'), ('BBA-71-2--default', 'SCR-05-consent-compliance')]:
    Image.open(f'{S}/png/{a}.png').convert('RGB').quantize(colors=128, method=Image.Quantize.MEDIANCUT).save(f'{W}/png/{b}.png', optimize=True)
print('ok')
