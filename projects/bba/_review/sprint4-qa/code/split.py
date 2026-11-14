# Tách brainstorm + wireframe BBA-68..79 thành từng FRD (mỗi ticket một thư mục).
import re, json, os, sys
R = sys.argv[1]
md = open(f'{R}/BBA-68-79_brainstorm.md', encoding='utf-8').read().split('\n')
html = open(f'{R}/BBA-68-79_wireframes.html', encoding='utf-8').read()

qa_md = open(f'{R}/BBA-66-79_brainstorm_QA.md', encoding='utf-8').read().split('\n')
QA = {}
for _i, _l in enumerate(qa_md):
    _m = re.match(r'^### BBA-(\d+) ', _l)
    if _m:
        _j = next((k for k in range(_i + 1, len(qa_md)) if qa_md[k].startswith('### BBA-') or qa_md[k].startswith('## ')), len(qa_md))
        QA[int(_m.group(1))] = qa_md[_i:_j]
TITLES = {68: 'Medical alert banner', 69: 'Allergies list', 70: 'Growth — height & weight', 71: 'Consent status per child',
          72: 'Bulk class promotion', 73: 'Handover recording', 74: 'Temperature readings', 75: 'Late flag (internal)',
          76: 'Centre-brand overview today', 77: 'Attendance correction', 78: 'Daily routines (web)', 79: 'Staff clock-in / out'}
# screen id -> states kept (None = all)
WF = {68: {'b68-1': None, 'b68-2': None}, 69: {'b69': None}, 70: {'b70-1': None, 'b70-2': None, 'b70-3': None},
      71: {'b71-1': None, 'b71-2': None}, 72: {'b72': None},
      73: {'b73': ['default', 'checkin', 'checkinerr', 'checkout', 'blocked', 'bus', 'busin', 'busout', 'offline']}, 74: {'b73': ['default', 'checkin', 'reading'], 'b75': None},
      75: {'b73': ['default'], 'b75': None}, 76: {'b76': None}, 77: {'b73': ['default', 'void']},
      78: {'b78': None}, 79: {'b79-1': None, 'b79-2': None}}

def block(start_pat, stop_pat):
    i = next(k for k, l in enumerate(md) if re.match(start_pat, l))
    j = next((k for k in range(i + 1, len(md)) if re.match(stop_pat, md[k])), len(md))
    return md[i:j]

head = md[:md.index('---')]                      # nguồn đã đọc
roles = block(r'^## 3\.', r'^## 4\.')
aq_head = block(r'^## Assumptions', r'^## Tóm tắt')[:4]
aq_rows = [l for l in block(r'^## Assumptions', r'^## Tóm tắt') if l.startswith('| ') and ('OQ-' in l or 'AS-' in l)]
chg_rows = [l for l in block(r'^## Tóm tắt', r'(?!)') if l.startswith('| ')][1:]
data = block(r'^## 6\.', r'^## 7\.')
risk = block(r'^## 7\.', r'^## Đề xuất')
prop = block(r'^## Đề xuất', r'^## Assumptions')

index = ['# BBA-68 đến BBA-79 — tách theo từng FRD', '', '> Bản nháp để review, chưa đưa lên Drive / Git. Mỗi thư mục: `brainstorm.md` (đối chiếu nguồn, lệch với FRD, câu hỏi mở) và `wireframe.html` (chỉ các màn của ticket đó).', '',
         '| Ticket | FRD | Thay đổi đề xuất | Câu hỏi mở | Màn wireframe |', '|---|---|---|---|---|']
for t in range(68, 80):
    d = f'{R}/by-frd/BBA-{t}'
    os.makedirs(d, exist_ok=True)
    sec = block(rf'^### BBA-{t} ', r'^(### BBA-|## 6\.)')
    mine = [l for l in aq_rows if re.search(rf'\| ([0-9, ]*\b{t}\b[0-9, ]*|chung) \|', l)]
    change = next((l for l in chg_rows if l.startswith(f'| {t} ')), '')
    tag = {68: 'BBA-68', 69: 'BBA-69', 70: 'BBA-70', 79: 'BBA-79'}.get(t, f'BBA-{t}')
    props = [l for l in prop if l.startswith(f'- {tag}:')]
    rel_risk = [l for l in risk[:4]] + [l for l in risk if l.startswith('| ') and (
        (t in (68, 69) and 'An toàn trẻ' in l) or (t == 79 and ('Phạm vi' in l or 'Dữ liệu cá nhân' in l)) or (t == 77 and 'Trợ cấp' in l))]
    out = [f'# Brainstorm — BBA-{t} {TITLES[t]}', ''] + head[2:] + ['', '---', ''] + [l.replace('### ', '## ') for l in sec]
    out[2:2] = ['## Cập nhật theo file câu hỏi phản hồi (13/11/2026)', '', '> Nguồn: `../../BBA-66-79_brainstorm_QA.md`. Phần này thắng phần phân tích cũ bên dưới khi mâu thuẫn.', ''] + [l.replace('### ', '### ') for l in QA.get(t, [])] + ['', '---', '']
    if change:
        out += ['', '## Thay đổi đề xuất cho FRD', '', '| FRD | Thay đổi chính |', '|---|---|', change]
    if props:
        out += ['', '## Đề xuất của BA (chưa phải yêu cầu)', ''] + props
    if len(rel_risk) > 4:
        out += [''] + rel_risk
    out += ['', '## Assumptions & Open Questions', ''] + aq_head[2:4] + mine
    out += ['', '## Vai trò liên quan (chung cho nhóm BBA-68..79)', ''] + roles[2:]
    open(f'{d}/brainstorm.md', 'w', encoding='utf-8').write('\n'.join(out).rstrip() + '\n')
    # wireframe: keep only this ticket's screens / states
    filt = json.dumps(WF[t])
    h = html.replace('const SCREENS = [', 'let SCREENS = [', 1)
    h = h.replace('\nlet current = {', f'\nconst ONLY = {filt};\nSCREENS = SCREENS.filter(s => s.id in ONLY).map(s => ONLY[s.id] ? Object.assign({{}}, s, {{ states: s.states.filter(x => ONLY[s.id].includes(x[0])) }}) : s);\nlet current = {{', 1)
    h = h.replace('<title>BBA-68 to BBA-79 wireframes</title>', f'<title>BBA-{t} wireframe</title>', 1)
    h = h.replace('<h1>Wireframe — Health, Consent, Promotion, Daily operations</h1>', f'<h1>Wireframe — BBA-{t} {TITLES[t]}</h1>', 1)
    open(f'{d}/wireframe.html', 'w', encoding='utf-8').write(h)
    n_scr = len(WF[t]); n_oq = len([l for l in mine if '| chung |' not in l])
    index.append(f'| BBA-{t} | {TITLES[t]} | {change.split("|")[2].strip() if change else "—"} | {n_oq} | {", ".join(WF[t])} |')
open(f'{R}/by-frd/README.md', 'w', encoding='utf-8').write('\n'.join(index) + '\n')
print('ok')
