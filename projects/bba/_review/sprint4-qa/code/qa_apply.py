# Áp câu trả lời trong file "BBA_SMS_S4 Tổng hợp câu hỏi phản hồi" vào các FRD nháp BBA-68..79 (trừ BBA-71 viết lại riêng).
import sys, re, os
D = sys.argv[1]
log = []

def load(n):
    p = f'{D}/{n}'; return p, open(p, encoding='utf-8').read()

def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:80])
    return s.replace(a, b)

def after_row(s, key, rows):
    """insert rows after the table row starting with '| key '"""
    m = re.search(r'^\| ' + re.escape(key) + r'[ |*].*$', s, flags=re.M)
    assert m, key
    return s[:m.end()] + '\n' + '\n'.join(rows) + s[m.end():]

def header(s, items):
    block = '\n**Cập nhật theo file câu hỏi phản hồi (BBA_SMS_S4, 13/11/2026)**\n' + '\n'.join(f'- {x}' for x in items) + '\n'
    i = s.index('\n---\n')
    return s[:i] + block + s[i:]

# ---------------- BBA-68 ----------------
p, s = load('BBA-68_Medical_Alert_Banner_US_Draft.md')
s = header(s, [
    'Cảnh báo sinh tự động (Q-69-02); nguồn Health + Allergies trên SMS và Parents App (Q-69-03) — khớp.',
    'Hiện **không có vai trò nào thiếu quyền Health**; HQ xem Health ở mọi Centre (Q-69-05); biểu tượng cảnh báo ai cũng thấy (Q-66-12) → FR-012 chỉ là cấu hình dự phòng; đóng OQ-MAB-04.',
    'Thứ tự, độ dài, cách mở toàn bộ cảnh báo: DOTB tự quyết (Q-69-06) → giữ FR-003, FR-010.',
    'Q-69-08 (09/11) nói đồng bộ ngay, không duyệt — **mâu thuẫn** với Plane BBA-1058 (13/11); bản nháp giữ theo Plane, ghi ở OQ-MAB-09.',
    'Định nghĩa critical (Q-69-01): không sửa, theo yêu cầu trước của user.'])
s, n = re.subn(r'^\| FR-012 \| (.*?) \|$', lambda m: f'| FR-012 *(sửa)* | {m.group(1)} Hiện BBA không có vai trò nào thiếu quyền Health (Q-69-05); quy tắc này chỉ dùng khi có cấu hình như vậy về sau. |', s, flags=re.M)
assert n == 1
s, n = re.subn(r'^(\| OQ-MAB-04 \| .*?) \| ([^|]+) \|$', lambda m: f'{m.group(1)} → **Đã trả lời:** mọi người thấy biểu tượng cảnh báo (Q-66-12); hiện không có vai trò nào thiếu quyền Health (Q-69-05). | Đã đóng |', s, flags=re.M)
assert n == 1
s = rep(s, 'sheet Clarification 11/11 — thay đổi của phụ huynh đồng bộ ngay, không cần duyệt', 'sheet Clarification / file câu hỏi Q-69-08 (phản hồi 09/11) — thay đổi của phụ huynh đồng bộ ngay, không cần duyệt')
open(p, 'w', encoding='utf-8').write(s); log.append('68 ok')

# ---------------- BBA-69 ----------------
p, s = load('BBA-69_Allergies_List_US_Draft.md')
s = header(s, [
    'Thang chính thức trên form BBA: Mild, Moderate, **Life Threatening**; Life Threatening lên đầu (Q-70-03) → giữ nhãn Severe trên giao diện, ghi tương ứng.',
    'Không giới hạn số dị ứng / bệnh của một trẻ (Q-70-02) → BR-005.',
    '**Chưa khai báo khác với đã khai báo không dị ứng** (Q-70-09) → FR-012.',
    'DOTB tự quyết: mô hình dữ liệu (Q-70-01) → giữ chữ tự do + mức độ; sắp xếp (Q-70-04) → mỗi trẻ một dòng theo mức cao nhất; export / audit (Q-70-11) → không lưu nhật ký.',
    'Chưa phản hồi: cột Reaction / Action Plan / EpiPen (Q-70-05), condition chung danh sách (Q-70-06), kênh cho bếp (Q-70-07), đồng bộ (Q-70-12).'])
s = rep(s, '| FR-002 | Thứ tự mặc định: trẻ có mức nặng nhất ở trên cùng (Severe, rồi Moderate, rồi Mild)', '| FR-002 *(sửa)* | Thứ tự mặc định: trẻ có mức nặng nhất ở trên cùng (Severe — tương ứng "Life Threatening" trên form của BBA — rồi Moderate, rồi Mild)')
s = after_row(s, 'FR-011', ['| FR-012 *(mới)* | Trẻ chưa khai Health record ("chưa cung cấp") được phân biệt với trẻ đã khai không có dị ứng: cuối danh sách có nhóm "Health information not provided" để Centre liên hệ phụ huynh. Trẻ chưa sinh không nằm trong nhóm này (Q-70-09). Cách hiển thị do DOTB quyết định. |'])
s = after_row(s, 'BR-004', ['| BR-005 *(mới)* | Một trẻ không bị giới hạn số dị ứng hoặc bệnh (Q-70-02). |'])
s = after_row(s, 'AC-012', ['| AC-013 *(mới)* | phụ huynh của Mia chưa khai Health record | Centre Director mở danh sách toàn Centre | Mia ở nhóm "Health information not provided", không nằm trong nhóm dị ứng | FR-012 |'])
s = rep(s, '| OQ-01 | Phản ứng, cách xử trí, nơi để thuốc khẩn cấp có thành trường riêng trong Health record không? (SRS Teacher App liệt kê "reaction, what to do".) | Mở |',
          '| OQ-01 | Phản ứng, cách xử trí, nơi để thuốc khẩn cấp có thành trường riêng không? (SRS Teacher App liệt kê "reaction, what to do".) | Mở — BBA chưa trả lời (Q-70-05); DOTB tự quyết mô hình dữ liệu (Q-70-01) → tạm giữ chữ tự do |')
s = rep(s, '| OQ-03 | Bếp dùng bản in hay có tài khoản xem trên máy? | Mở |', '| OQ-03 | Bếp dùng bản in hay có tài khoản xem trên máy; được xem dữ liệu nhận dạng nào? | Mở — BBA chưa trả lời (Q-70-07) |')
s = rep(s, '| AS-04 *(mới)* | Bản in chỉ ghi ngày giờ in, không ghi tên người in. | Chờ xác nhận |',
          '| AS-04 *(mới)* | Bản in chỉ ghi ngày giờ in, không ghi tên người in. | DOTB quyết định (Q-70-11) |\n| OQ-06 *(mới)* | Thang mức độ có cần cấu hình theo brand / Centre ngay Phase 1 không? BBA nói form "có thể" tuỳ theo brand / Centre (Q-70-03). | Mở |\n| OQ-07 *(mới)* | Skin, respiratory, medical history nằm chung danh sách dị ứng hay nhóm riêng? FRD đang để nhóm riêng (SRS BR-TCH-015). | Mở — BBA chưa trả lời (Q-70-06) |')
open(p, 'w', encoding='utf-8').write(s); log.append('69 ok')

# ---------------- BBA-70 ----------------
p, s = load('BBA-70_Growth_US_Draft.md')
s = header(s, [
    'Term **do HQ đặt theo brand, Centre không sửa**; 4 term, năm học bắt đầu 1/1, ngày term đổi theo năm (vd Schoolhouse T1 2/1–15/3, Agape T1 2/1–10/3); nhắc giữa tháng cuối mỗi term (Q-71-03) → FR-001, FR-011.',
    'Mọi trẻ trong lớp (Q-71-06); một lần mỗi term và có **Measurement history** (Q-71-07) → FR-012; Change record có "Updated By" (Q-71-08); đơn vị cm, kg (Q-71-05).',
    'Teacher thao tác lớp mình; Centre Director và School Admin mọi trẻ (Q-71-10) → BR-005.',
    'Lưu cả lớp khi có dòng lỗi: DOTB tự quyết (Q-71-09) → lưu các dòng hợp lệ.',
    '**Mâu thuẫn:** Q-71-02 (09/11) bỏ cả BMI và percentile, "chỉ cần height + weight" ↔ Plane BBA-1059 (13/11) gửi chuẩn biểu đồ → giữ biểu đồ theo Plane, OQ-07.'])
s = rep(s, 'Kỳ đo theo lịch của brand: 4 kỳ một năm (Term 1–4); Brighton theo 2 học kỳ (Semester 1–2). |',
          'Kỳ đo theo lịch term của brand do HQ đặt (Centre không sửa): 4 term một năm, năm học bắt đầu 1/1, ngày term đổi theo từng năm (Q-71-03); Brighton đo theo 2 học kỳ (Semester 1–2) (BBA-529). |')
s = rep(s, '| FR-003 | "Save the whole class" lưu một lần mọi dòng đã nhập đủ cả chiều cao và cân nặng; dòng để trống không được lưu và vẫn là "Not recorded yet" trong kỳ. Số đo có hiệu lực ngay, không cần duyệt. |',
          '| FR-003 *(sửa)* | "Save the whole class" lưu một lần mọi dòng đã nhập đủ cả chiều cao và cân nặng; dòng để trống không được lưu và vẫn là "Not recorded yet" trong kỳ; dòng lỗi không chặn các dòng hợp lệ (DOTB quyết định, Q-71-09). Số đo có hiệu lực ngay, không cần duyệt. |')
s = rep(s, 'vào giữa tháng cuối mỗi quý (tháng 3, 6, 9, 12) cho mọi brand, kể cả Brighton. |', 'vào giữa tháng cuối mỗi term (tháng 3, 6, 9, 12) cho mọi brand, kể cả Brighton (Q-71-03, BBA-529). |')
s = after_row(s, 'FR-011', ['| FR-012 *(mới)* | Hồ sơ trẻ có "Measurement history": mọi lần đo theo ngày đo (term, ngày đo, chiều cao, cân nặng, người nhập) (Q-71-07). |'])
s = rep(s, '| BR-005 *(mới)* | Thêm, sửa và xoá số đo là một quyền chung; mặc định giao cho Centre Director, School Admin và mọi Teacher. |',
          '| BR-005 *(mới)* | Thêm, sửa và xoá số đo là một quyền chung (BBA-1059); Teacher thao tác trên lớp mình, Centre Director và School Admin trên mọi trẻ của Centre (Q-71-10). |')
s = rep(s, '| OQ-06 *(mới)* | Nhắc gửi cho ai (Centre Director, School Admin, giáo viên lớp) và qua kênh nào? | Mở |',
          '| OQ-06 *(mới)* | Nhắc gửi cho ai (Centre Director, School Admin, giáo viên lớp) và qua kênh nào? | Mở |\n| OQ-07 *(mới)* | Có biểu đồ tăng trưởng không? File câu hỏi Q-71-02 (09/11): bỏ BMI và percentile, chỉ cần height + weight; Plane BBA-1059 (13/11): gửi chuẩn biểu đồ SG / MY. Bản nháp theo Plane. | Mở — cao |')
s = rep(s, '| OQ-03 | Khoảng hợp lệ chiều cao, cân nặng theo độ tuổi. | Mở |', '| OQ-03 | Khoảng hợp lệ và số chữ số thập phân. | Mở — BBA mới chốt đơn vị cm, kg (Q-71-05); DOTB có thể tự đặt |')
open(p, 'w', encoding='utf-8').write(s); log.append('70 ok')

# ---------------- BBA-72 ----------------
p, s = load('BBA-72_Bulk_Class_Promotion_US_Draft.md')
s = header(s, [
    'Ticket này là **annual promotion** (cuối năm, cả lớp lên level kế). Infant promotion (từng trẻ, 18 tháng tuổi) và class change (đổi lớp cùng level) là luồng khác; **K2 graduation là mass withdrawal**, chỉ K2 rời vào tháng 12 (Q-74-01, Q-74-06) → BR-007, đóng OQ-05.',
    'Chỉ trong cùng Centre; khác Centre / brand là Transfer (Q-74-02) → BR-006.',
    'Chọn cả cohort, bỏ tick ngoại lệ; trẻ ở lại giữ lớp hoặc chuyển lớp khác cùng level (Q-74-03) → FR-003.',
    'Capacity linh hoạt, CD cấu hình sĩ số từng lớp (Q-74-08); hoá đơn đã phát hành sửa bằng credit note (Q-74-09) — khớp.',
    'Lên lớp → thread trao đổi mới cho lớp mới, thread cũ chỉ đọc (Q-74-10) → FR-005.',
    'DOTB tự quyết: preview, lỗi từng phần, chạy lại (Q-74-11, 12, 13).',
    'Ngày hiệu lực mặc định: dùng ngày bắt đầu Term 1 năm sau theo lịch brand (Q-71-03, Q-74-07) — giả định AS-01.'])
s = rep(s, '| FR-003 | Người dùng bỏ chọn trẻ học lại (ở lại level cũ) và đổi lớp đích cho từng trẻ khi cần. |',
          '| FR-003 *(sửa)* | Người dùng bỏ chọn trẻ ngoại lệ (học lại, rút, gia hạn) và đổi lớp đích cho từng trẻ khi cần; trẻ bị bỏ chọn giữ lớp cũ hoặc được chuyển sang lớp khác cùng level bằng luồng class change (Q-74-03). |')
s = rep(s, 'đưa trẻ vào danh sách điểm danh của lớp đích; chuyển trẻ từ nhóm trao đổi của lớp cũ sang lớp mới. |',
          'đưa trẻ vào danh sách điểm danh của lớp đích; tạo thread trao đổi mới cho lớp mới, thread lớp cũ chuyển chỉ đọc và giữ tới khi trẻ rời trường (Q-74-10). |')
s = rep(s, '| FR-005 | "Confirm move"', '| FR-005 *(sửa)* | "Confirm move"')
s = rep(s, 'trẻ của lớp này đi qua Joining & leaving › Graduation (chờ OQ-05). |', 'K2 tốt nghiệp đi qua Joining & leaving › Graduation (mass withdrawal, reason graduation, chỉ K2 rời vào tháng 12) (Q-74-01). |')
s = after_row(s, 'BR-005', ['| BR-006 *(mới)* | Chỉ chuyển trong cùng Centre; khác Centre hoặc khác brand đi luồng Transfer (Q-74-02). |',
                             '| BR-007 *(mới)* | Màn này chỉ dùng cho annual promotion; Infant promotion và class change là luồng riêng (Q-74-01). |'])
s = after_row(s, 'AC-013', ['| AC-014 *(mới)* | 14 trẻ đã chuyển sang Honeycombs từ 04/01/2027 | phụ huynh của một trẻ mở Messages ngày 05/01/2027 | thấy thread lớp Honeycombs mới; thread Sunbeams chỉ đọc | FR-005 |'])
s = rep(s, '| OQ-02 | Ngày đầu năm học mới của mỗi quốc gia / brand? | BBA đã gửi file term dates 2027 (BBA-489) — cần file |',
          '| OQ-02 | Ngày hiệu lực mặc định, có cho lên lịch và huỷ trước ngày hiệu lực không? | Mở — Q-74-07 mới có bối cảnh (năm học 1–12, lập lớp tháng 11–12); ngày term theo file BBA-489 |')
s = rep(s, '| OQ-03 | Trẻ đang tạm nghỉ có được chuyển cùng lớp không? | Mở |', '| OQ-03 | Trẻ đang tạm nghỉ (tối đa 3 tháng, vẫn trong hệ thống) có được chuyển cùng lớp không; trạng thái nào đủ điều kiện? | Mở — Q-74-06 chưa nói |')
s = rep(s, '| OQ-04 | Phụ huynh có nhận thông báo khi con được lên lớp không? | Mở |', '| OQ-04 | Phụ huynh / giáo viên có nhận thông báo khi lên lớp không; lớp cũ tự đóng hay đóng tay? | Mở — Q-74-15 chưa trả lời phần này |')
s = rep(s, '| OQ-05 *(sửa)* | Trẻ K2 cuối năm xử lý ở Joining & leaving › Graduation (prototype đã có) — BBA xác nhận? | Chờ xác nhận |',
          '| OQ-05 | Trẻ K2 cuối năm xử lý ở đâu? | **Đã chốt:** mass graduation qua withdrawal (Q-74-01) |\n| OQ-06 *(mới)* | Biểu phí level mới áp từ ngày hiệu lực hay từ đầu tháng sau? | Mở (Q-74-09) |\n| OQ-07 *(mới)* | Danh sách điểm danh chuyển ngay khi xác nhận hay tại ngày hiệu lực? | Mở (Q-74-10) |')
s = rep(s, '| AS-01 | Ngày hiệu lực mặc định là ngày đầu năm học mới. | Chờ OQ-02 |', '| AS-01 *(sửa)* | Ngày hiệu lực mặc định là ngày bắt đầu Term 1 năm sau theo lịch term của brand (Q-71-03). | Chờ OQ-02 |')
open(p, 'w', encoding='utf-8').write(s); log.append('72 ok')

# ---------------- BBA-73 ----------------
p, s = load('BBA-73_Handover_US_Draft.md')
s = header(s, [
    'Check-out chỉ người đã duyệt, **không có override**; người lạ → Centre gọi phụ huynh, phụ huynh điền đủ thông tin ngay rồi người đó mới được đón (Q-75-02, Q-75-04) → FR-004.',
    'Xe đưa đón: bộ lọc theo xe chỉ để gom; **nhận / trả từng trẻ, ảnh riêng**; người giao là tài xế, người nhận về là phụ xe của công ty xe (Q-75-10) → FR-008.',
    'Parents App hiện ảnh lúc giao nhận (Q-81-02) → FR-010.',
    'Ô nhập tay ở check-in: DOTB tự quyết (Q-75-02) → chỉ hiện khi chọn "Someone else".'])
s = rep(s, '| FR-004 | Khi người đến đón không có trong danh sách, nhân viên chọn "Not on the list"; hệ thống không cho trả trẻ và hiện hướng dẫn "Do not release the child. Call the parent and the Centre Director." |',
          '| FR-004 *(sửa)* | Khi người đến đón không có trong danh sách, nhân viên chọn "Not on the list"; hệ thống không cho trả trẻ và hiện hướng dẫn "Do not release the child. Call the parent to add this person in the Parents App. The person can collect the child once approved." Không có cơ chế override (Q-75-04). |')
s = rep(s, '| FR-008 | Trẻ đi xe đưa đón được nhận cả nhóm; người đưa ghi là tên tuyến xe. Khi trả, mỗi trẻ được trả riêng và vẫn phải chọn người đón theo FR-002. |',
          '| FR-008 *(sửa)* | Bộ lọc theo tuyến xe gom trẻ của một xe vào một danh sách; nhận và trả vẫn làm từng trẻ, mỗi trẻ một bản ghi và ảnh riêng. Lúc xe đến, người giao là tài xế; lúc xe về, người nhận là phụ xe của công ty xe (Q-75-10). |')
s = after_row(s, 'FR-009', ['| FR-010 *(mới)* | Mỗi lượt nhận / trả chụp ảnh trẻ cùng người giao / nhận; Parents App hiện ảnh này để phụ huynh thấy ai đưa / đón (Q-75-10, Q-81-02; SRS Daily Operations "Check out: time, photo and the person collecting"). |'])
s = rep(s, '| Time | Giờ | Có | Giờ hiện tại | VAL-003. | — |', '| Time | Giờ | Có | Giờ hiện tại | VAL-003. | — |\n| Photo *(mới)* | Chụp ảnh | Có | — | — | FR-010. |\n| Bus route *(mới)* | Bộ lọc | Không | All | — | Gom trẻ của một xe (FR-008). |')
s = rep(s, '| DATA-001 *(sửa)* | Mỗi lượt nhận / trả lưu: trẻ, loại (nhận / trả), người đưa hoặc người đón (hoặc tên và quan hệ khi Someone else), giờ, nhân viên thực hiện, thiết bị. |',
          '| DATA-001 *(sửa)* | Mỗi lượt nhận / trả lưu: trẻ, loại (nhận / trả), người đưa hoặc người đón (hoặc tên và quan hệ khi Someone else), ảnh, giờ, nhân viên thực hiện, thiết bị. |')
s = rep(s, '| AC-009 | 6 trẻ đi xe tuyến A đến trường | nhân viên nhận cả xe | 6 lượt nhận ghi người đưa là "tuyến A" | FR-008 |',
          '| AC-009 *(sửa)* | 6 trẻ đi xe tuyến A đến trường | nhân viên lọc tuyến A và nhận từng trẻ | 6 bản ghi riêng, mỗi bản ghi có ảnh của trẻ, người đưa là tài xế tuyến A | FR-008 |')
s = after_row(s, 'AC-011', ['| AC-012 *(mới)* | Ethan được bố đón lúc 17:40, nhân viên chụp ảnh | phụ huynh mở Parents App | thấy ảnh lúc giao nhận và tên người đón | FR-010 |'])
s = rep(s, '| OQ-04 | Trẻ đi xe về nhà: người đón ghi là tài xế / người phụ trách xe hay phụ huynh ở điểm trả? | Mở |',
          '| OQ-04 | Trẻ đi xe về nhà: người nhận là phụ xe của công ty xe (Q-75-10). Phụ xe có phải nằm trong danh sách người đón đã duyệt của từng trẻ không? | Mở |\n| OQ-05 *(mới)* | Ảnh và bằng chứng giao nhận lưu bao lâu, ai xem / xuất, có tự xoá không? | Mở (Q-75-12) |')
open(p, 'w', encoding='utf-8').write(s); log.append('73 ok')

# ---------------- BBA-74 ----------------
p, s = load('BBA-74_Temperature_US_Draft.md')
s = header(s, [
    'Bộ chọn: không cần dưới 36, phải lên 39–40; **mặc định 36.5, hiện sẵn dải 36.3–36.7 để bấm**; nút ghi **"Enter manually"** (Q-76-05) → FR-001.',
    'Được sửa số đọc từ nhiệt kế Bluetooth (Q-76-06) → FR-003.',
    '**Một số Centre** đo 3 lần: lúc đến, **sau ngủ trưa**, lúc về; CD có nút "add temperature" (Q-81-02) → đổi "Before nap" thành **"After nap"**; số lần bắt buộc vẫn ở OQ-06.',
    'Nhập tay ngoài khoảng: cảnh báo hay chặn chưa rõ (Q-76-05) → giữ AS-02 / OQ-04.'])
s = rep(s, '| FR-001 | "Add reading" cho mỗi trẻ: nhiệt độ (bộ chọn mặc định 36,5 °C, từ 36 đến 40 °C, bước 0,1; hoặc nhập tay), giờ (mặc định hiện tại), thời điểm: On arrival, Before nap, Before pickup, Extra. |',
          '| FR-001 *(sửa)* | "Add reading" cho mỗi trẻ: nhiệt độ (mặc định 36,5 °C; nút chọn nhanh 36,3 – 36,4 – 36,5 – 36,6 – 36,7; bộ chọn từ 36 đến 40 °C, bước 0,1; nút "Enter manually" để nhập tay), giờ (mặc định hiện tại), thời điểm: On arrival, After nap, Before pickup, Extra. |')
s = rep(s, '| FR-003 | Nhiệt kế đã kết nối với máy tính bảng tự điền nhiệt độ; nhân viên vẫn chọn thời điểm. |',
          '| FR-003 *(sửa)* | Nhiệt kế Bluetooth đã kết nối với máy tính bảng tự điền nhiệt độ; nhân viên sửa được giá trị (Q-76-06) và vẫn chọn thời điểm. |')
s = s.replace('Before nap', 'After nap')
s = after_row(s, 'FR-011', ['| FR-012 *(mới)* | Centre Director thêm lần đo cho trẻ bằng nút "Add temperature" (Q-81-02). |'])
s = rep(s, '| OQ-06 *(mới)* | Xác nhận số lần đo bắt buộc mỗi ngày là 3 (On arrival, After nap, Before pickup). SRS chỉ bắt buộc khi nhận trẻ. | Mở — cao |',
          '| OQ-06 *(mới)* | Số lần đo bắt buộc mỗi ngày: BBA nói **một số Centre** đo 3 lần (lúc đến, sau ngủ trưa, lúc về) (Q-81-02); SRS chỉ bắt buộc khi nhận trẻ. Có cần thiết lập số lần theo Centre không? | Mở — cao |')
s = rep(s, '| Temperature (°C) | Bộ chọn số / nhập tay | Có | 36,5 | VAL-001; VAL-004. | Nhiệt kế kết nối tự điền. |',
          '| Temperature (°C) *(sửa)* | Nút chọn nhanh 36,3–36,7 + bộ chọn 36–40 + "Enter manually" | Có | 36,5 | VAL-001; VAL-004. | Nhiệt kế Bluetooth tự điền, sửa được. |')
open(p, 'w', encoding='utf-8').write(s); log.append('74 ok')

# ---------------- BBA-75 ----------------
p, s = load('BBA-75_Late_Flag_US_Draft.md')
s = header(s, [
    'Giờ chốt theo Centre có **buổi sáng và buổi chiều** (vd sau 9:15 sáng, sau 12:15 chiều); tính theo **giờ ghi nhận ở cổng**, không phải giờ đồng bộ (Q-77-03) → FR-001, FR-002; OQ-01 trả lời một phần.',
    'Late không gắn tay (Q-81-02) — khớp BR-001. Bản ghi offline / backdated tự tính lại: DOTB tự quyết (Q-77-04) — khớp FR-005.',
    'Chỉ nhân viên thấy — BBA nói "ở Singapore", Malaysia chưa rõ (Q-77-05) → OQ-06.'])
s = rep(s, '| FR-001 | Mỗi Centre có một giờ chốt đến muộn (mặc định 9:15); HQ Admin đổi được ở Centre settings, mỗi lần đổi được lưu lịch sử. |',
          '| FR-001 *(sửa)* | Mỗi Centre có giờ chốt đến muộn buổi sáng (mặc định 9:15) và buổi chiều (ví dụ 12:15) (Q-77-03); HQ Admin đổi được ở Centre settings, mỗi lần đổi được lưu lịch sử. |')
s = rep(s, '| FR-002 | Khi trẻ được nhận sau giờ chốt, hệ thống tự gắn dấu "Late" cho lượt nhận đó; nhận đúng giờ chốt không bị tính muộn. |',
          '| FR-002 *(sửa)* | Khi trẻ được nhận sau giờ chốt của buổi tương ứng (OQ-05), hệ thống tự gắn dấu "Late" cho lượt nhận đó; so sánh bằng giờ ghi nhận ở cổng, không phải giờ đồng bộ (Q-77-03); nhận đúng giờ chốt không bị tính muộn. |')
s = rep(s, '| Late arrival cut-off *(sửa tên)* | Giờ, ở Centre settings | Có | 09:15 | VAL-001. | Thiết lập theo Centre (FR-001). |',
          '| Late arrival cut-off — morning *(sửa)* | Giờ, ở Centre settings | Có | 09:15 | VAL-001. | Thiết lập theo Centre (FR-001). |\n| Late arrival cut-off — afternoon *(mới)* | Giờ, ở Centre settings | Có | 12:15 (ví dụ của BBA) | VAL-001. | Thiết lập theo Centre (FR-001). |')
s = after_row(s, 'AC-007', ['| AC-008 *(mới)* | giờ chốt buổi chiều của Centre là 12:15 | trẻ học buổi chiều được nhận lúc 12:30 | bảng điểm danh hiện "12:30 · Late (staff only)" | FR-001; FR-002 |'])
s = rep(s, '| OQ-01 | Trẻ học buổi chiều (Half Day PM) dùng giờ chốt riêng hay không tính đến muộn? | Mở — cao |',
          '| OQ-01 | Trẻ học buổi chiều dùng giờ chốt riêng? | **Đã trả lời:** có giờ chốt buổi chiều, vd 12:15 (Q-77-03) |\n| OQ-05 *(mới)* | Chọn giờ chốt nào cho một lượt nhận: theo buổi học của trẻ (AM / PM / Full day) hay theo khung giờ lượt nhận? | Mở |\n| OQ-06 *(mới)* | Malaysia: phụ huynh có thấy dấu Late không? BBA chỉ nói "ở Singapore" (Q-77-05). | Mở |')
s = rep(s, '| AS-02 | Một giờ chốt chung cho mọi trẻ của Centre. | Chờ OQ-01 |', '| AS-02 *(sửa)* | Hai giờ chốt (sáng, chiều) cho mọi trẻ của Centre. | Chờ OQ-05 |')
open(p, 'w', encoding='utf-8').write(s); log.append('75 ok')

# ---------------- BBA-76 ----------------
p, s = load('BBA-76_Overview_Today_US_Draft.md')
s = header(s, [
    'Temporary withdrawal: không điểm danh, không tính enrolment number, vẫn trong student list (có tag), ẩn khỏi Attendance app (Q-80-01, Q-80-03) — khớp FR-002.',
    'Điểm danh gắn với **bản ghi enrolment**, không gắn hồ sơ trẻ (Q-80-03) → DATA-001.',
    '"Today" theo Centre hay người xem như nhau vì SG, MY cùng UTC+8 (Q-80-08) → BR-002.',
    'iPad offline: DOTB tự quyết (Q-80-05).',
    'Còn mở: nghỉ phép có trừ khỏi expected (Q-80-03), realtime (Q-80-04), drill-down (Q-80-07), 3 stream (Q-80-09), export (Q-80-11).'])
s = rep(s, '| BR-002 | Số liệu tính theo điểm danh hôm nay; lượt đã huỷ không được tính. |', '| BR-002 *(sửa)* | Số liệu tính theo điểm danh hôm nay (ngày theo giờ UTC+8 của Singapore và Malaysia, Q-80-08); lượt đã huỷ không được tính. |')
s = rep(s, '| DATA-001 | Bảng đọc điểm danh hôm nay, lịch học, nghỉ phép đã duyệt và trạng thái tạm nghỉ của trẻ; không lưu dữ liệu mới. |',
          '| DATA-001 *(sửa)* | Bảng đọc điểm danh hôm nay (gắn với bản ghi enrolment, Q-80-03), lịch học, nghỉ phép đã duyệt và trạng thái tạm nghỉ của trẻ; không lưu dữ liệu mới. |')
s = rep(s, '| OQ-02 | Số liệu cần tự làm mới sau bao nhiêu phút, hay chỉ khi bấm Refresh? | Mở |',
          '| OQ-02 | Số liệu cần realtime hay theo chu kỳ; độ trễ chấp nhận được? | Mở — BBA chưa trả lời (Q-80-04) |\n| OQ-04 *(mới)* | Trẻ có nhiều stream (Main, Early Intervention, Enrichment) được đếm thế nào trên bảng? | Mở (Q-80-09) |\n| OQ-05 *(mới)* | Drill-down có mức Country / cluster không; giữ bộ lọc nào khi mở xuống? | Mở (Q-80-07) |\n| OQ-06 *(mới)* | Có cần xuất bảng; thời gian tải cho toàn bộ brand / country? | Mở (Q-80-11) |')
s = rep(s, '| OQ-01 | "Expected" có trừ trẻ bị đánh vắng bằng tay trong ngày không? | Mở |', '| OQ-01 | "Expected" có trừ trẻ nghỉ phép đã duyệt và trẻ bị đánh vắng bằng tay không? | Mở — Q-80-03 chưa nói thẳng |')
open(p, 'w', encoding='utf-8').write(s); log.append('76 ok')

# ---------------- BBA-77 ----------------
p, s = load('BBA-77_Attendance_Correction_US_Draft.md')
s = header(s, [
    '**Check-in nhầm phải Void (gỡ)**, không dùng check-out để thay (Q-81-01) → FR-010; OQ-04 trả lời một phần.',
    'Ai cũng gửi yêu cầu; Admin, CD, Senior Teacher được chỉ định duyệt, chính họ void không cần duyệt (Q-81-03, Q-75-08) — khớp FR-010, FR-011.',
    'Void check-in đổi trạng thái đủ điều kiện subsidy và cảnh báo ngày 18; e-Form 1 gửi ECDA ngày có điểm danh thật đầu tiên, lô 12:00 trưa (Q-81-07) → FR-007.',
    'Audit trail bắt buộc ở Singapore (Q-81-05) — khớp BR-002.',
    'Chưa đồng bộ sửa trên iPad, đã đồng bộ void trên web: DOTB tự quyết (Q-81-10) — khớp BR-005.'])
s = rep(s, '| FR-007 | Ngày đã sửa hoặc huỷ được tính lại trong báo cáo điểm danh, bảng tổng hợp và danh sách trẻ chưa có ngày đi học trong tháng. |',
          '| FR-007 *(sửa)* | Ngày đã sửa hoặc huỷ được tính lại trong báo cáo điểm danh, bảng tổng hợp, trạng thái đủ điều kiện subsidy và danh sách trẻ chưa có ngày đi học trong tháng (kiểm tra ngày 18) (Q-81-07). |')
s = rep(s, 'Lượt bị huỷ không được tính vào điểm danh; nhân viên ghi lại lượt đúng như bình thường. |', 'Lượt bị huỷ không được tính vào điểm danh; nhân viên ghi lại lượt đúng như bình thường. Check-in nhầm phải huỷ, không dùng check-out để thay (Q-81-01). |')
s = rep(s, '| OQ-04 *(mới)* | SMS web cho **sửa trực tiếp** (Correct: giờ, trạng thái, người) hay **chỉ huỷ rồi ghi lại** (Void, như SRS và prototype)? | Mở — cao |',
          '| OQ-04 *(mới)* | Check-in nhầm cả lượt → **Void** (đã chốt, Q-81-01). Còn sai giờ / người (lượt đúng nhưng ghi sai) thì sửa trực tiếp (Correct) hay cũng Void rồi ghi lại? | Mở — cao |\n| OQ-05 *(mới)* | Trường nào được sửa: giờ, người giao / nhận, ảnh, nhiệt độ, trạng thái nghỉ? | Mở (Q-81-02) |\n| OQ-06 *(mới)* | Phụ huynh có được báo khi lượt nhận / trả đã gửi bị sửa hoặc huỷ không? | Mở (Q-81-08) |\n| OQ-07 *(mới)* | Huỷ check-in sau 12:00 (e-Form 1 đã gửi ECDA) thì xử lý thế nào? | Mở (Q-81-07, Q-81-09) |')
s = rep(s, '| OQ-02 | Được sửa / huỷ lùi về tối đa bao nhiêu ngày? | Mở — cao |', '| OQ-02 | Sau mốc nào điểm danh bị khoá: cuối ngày, chốt tháng, sau khi gửi subsidy? | Mở — cao (Q-81-09) |')
s = rep(s, '| OQ-03 | Sửa ngày đã gửi báo cáo trợ cấp (e-Form 1) thì có cần thêm bước gì không? | Mở |', '| OQ-03 | Có danh mục lý do (reason code) ngoài ô nhập tự do không? | Mở (Q-81-05) |')
open(p, 'w', encoding='utf-8').write(s); log.append('77 ok')

# ---------------- BBA-78 ----------------
p, s = load('BBA-78_Daily_Routines_US_Draft.md')
s = rep(s, '1. Thêm **Mood** (có trong SRS CD app và prototype).', '1. ~~Thêm Mood~~ → **bỏ lại**: BBA chốt 4 loại theo Taidii (Q-86-01). Mood chuyển sang OQ-05.')
s = header(s, [
    'Danh mục: Taidii và file export của BBA có **4 loại: Bottle, Food, Nap, Potty** (Q-86-01) → FR-001 bỏ Mood.',
    'Trường dữ liệu dùng lại như Taidii (Q-86-02); lỗi từng phần khi ghi cả lớp: DOTB tự quyết (Q-86-05).',
    'Ghi cả lớp: chỉnh ngoại lệ "cả 2" — trước và sau khi lưu (Q-86-04) → FR-003.',
    'Thông báo theo category, có Routines, phụ huynh chọn category muốn nhận (Q-86-09) → FR-012.',
    'Chưa phản hồi: backdated / future (Q-86-06), cài đặt hiện cho phụ huynh (Q-86-08), ghi chú từ gia đình (Q-86-10).'])
s = rep(s, 'mỗi trẻ một dòng gồm: Meal (All / Most / Some / None cho từng bữa, món ăn), sữa (ml pha, ml uống), Nap (giờ bắt đầu, giờ kết thúc, thời gian ngủ, chất lượng), Nappy and toilet (Diaper, Potty, Accident; Wet, BM, Dry), **Mood**, ghi chú từ gia đình. |',
          'mỗi trẻ một dòng gồm 4 loại theo Taidii (Q-86-01, Q-86-02): Food (bữa, All / Most / Some / None, món ăn), Bottle (ml pha, ml uống), Nap (giờ bắt đầu, giờ kết thúc, thời gian ngủ, chất lượng), Potty (Diaper, Potty, Accident; Wet, BM, Dry); ghi chú từ gia đình. |')
s = rep(s, '| FR-003 | "Record for the whole class" ghi một mục cho mọi trẻ đã đến trong ngày cùng lúc, sau đó người dùng chỉnh riêng từng trẻ khác đi. |',
          '| FR-003 *(sửa)* | "Record for the whole class" ghi một mục cho nhiều trẻ cùng lúc; người dùng bỏ chọn trẻ ngoại lệ trước khi lưu và chỉnh riêng từng trẻ sau khi lưu (Q-86-04). |')
s = rep(s, '| FR-012 *(mới)* | Phụ huynh nhận thông báo "Daily routines updated" trong app mỗi ngày một lần, khi trẻ được trả. |',
          '| FR-012 *(mới)* | Phụ huynh nhận thông báo "Daily routines updated" trong app mỗi ngày một lần, khi trẻ được trả; thông báo thuộc category Routines, phụ huynh tắt được category này (Q-86-09). |')
s = rep(s, '| Bảng sinh hoạt *(sửa)* | Bảng | Có | Mỗi trẻ một dòng | — | Cột: Child, Meal, Nap, Nappy and toilet, Mood (FR-001; FR-006; FR-011). |',
          '| Bảng sinh hoạt *(sửa)* | Bảng | Có | Mỗi trẻ một dòng | — | Cột: Child, Food, Bottle, Nap, Potty (FR-001; FR-006; FR-011). |')
s = rep(s, '| AC-001 *(sửa)* | lớp Bumblebees hôm nay có 16 trẻ | Centre Director mở Daily routines | mỗi trẻ một dòng với Meal, Nap, Nappy and toilet, Mood, ghi chú từ gia đình | FR-001 |',
          '| AC-001 *(sửa)* | lớp Bumblebees hôm nay có 16 trẻ | Centre Director mở Daily routines | mỗi trẻ một dòng với Food, Bottle, Nap, Potty, ghi chú từ gia đình | FR-001 |')
s = rep(s, '| OQ-04 *(mới)* | Có cần bật / tắt từng loại sinh hoạt cho phụ huynh không? SRS chỉ nói phụ huynh thấy routines của con theo ngày. | Mở — cao |',
          '| OQ-04 *(mới)* | Có cần bật / tắt từng loại sinh hoạt cho phụ huynh không; cấu hình theo cấp nào? SRS chỉ nói phụ huynh thấy routines của con theo ngày. | Mở — cao (Q-86-08 chưa trả lời) |\n| OQ-05 *(mới)* | Mood: SRS CD app và prototype có, Taidii và file export của BBA không có (Q-86-01). Bỏ Mood ở Phase 1? | Mở |\n| OQ-06 *(mới)* | Ghi cả lớp: trẻ vắng / nghỉ phép có được áp không? | Mở (Q-86-04 trả lời chưa rõ) |\n| OQ-07 *(mới)* | Có cho ghi routines ngày trước / ngày sau không? | Mở (Q-86-06) |\n| OQ-08 *(mới)* | Ghi chú từ gia đình có hiện trên màn lớp và gắn với ngày không? | Mở (Q-86-10) |')
s = rep(s, '| OQ-03 | Phụ huynh có nhận thông báo khi một mục đã xem bị sửa không? | Mở |', '| OQ-03 | Thêm / sửa routines sau khi trả trẻ có báo lại phụ huynh không? | Mở (Q-86-09 chưa trả lời phần này) |')
open(p, 'w', encoding='utf-8').write(s); log.append('78 ok')

# ---------------- BBA-79 ----------------
p, s = load('BBA-79_Staff_Clock_US_Draft.md')
s = header(s, [
    'Phase 1 là chấm công **tối thiểu**: nhân viên báo có mặt, đo nhiệt độ, cần báo cáo (Q-90-05) — khớp.',
    'Trong file các câu Q-90-07, 08, 09, 10 chưa phản hồi; Q-90-09 (ai sửa) đã có câu trả lời trên Plane BBA-528: CD sửa.',
    'Trùng lượt offline / web: DOTB tự quyết (Q-90-12) — không còn chấm công trên web nên không phát sinh.'])
s = rep(s, '| OQ-04 | Nhân viên làm ở nhiều Centre trong một ngày có được chấm công ở nhiều Centre không? | Mở |',
          '| OQ-04 | Nhân viên làm ở nhiều Centre trong một ngày; lượt đồng bộ trễ tính On site thế nào? | Mở (Q-90-10) |\n| OQ-08 *(mới)* | Một nhân viên có được chấm công nhiều lượt trong ngày (ca gãy) không? | Mở (Q-90-05 chưa trả lời) |\n| OQ-09 *(mới)* | Nhiệt độ vượt ngưỡng khi vào ca: chỉ cảnh báo hay chặn vào làm? | Mở (Q-90-07) — FRD đang chỉ cảnh báo và báo CD (SRS) |\n| OQ-10 *(mới)* | Quên chấm công ra: hệ thống tự đóng ca, nhắc nhân viên, hay CD sửa hôm sau? | Mở (Q-90-08) — FRD đang để CD sửa |')
open(p, 'w', encoding='utf-8').write(s); log.append('79 ok')

print('\n'.join(log))
