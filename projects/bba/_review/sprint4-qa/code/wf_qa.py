import sys
R = sys.argv[1]
p = R + '/wf_body.html'
s = open(p, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:80])
    s = s.replace(a, b)
def block(start, end, new):
    """replace from start marker (inclusive) to end marker (exclusive)"""
    global s
    i = s.index(start); j = s.index(end, i)
    s = s[:i] + new + s[j:]

# ---------- BBA-71 Consents ----------
block('const CONS = [', '/* ===================== BBA-72', r'''const CONS = [["Media release", "—", "v2 · 01/09/2026", '<span class="tag solid">Agreed</span>', "Serena Lim · registration form · 05/01/2026", "—"],
  ["Field trip / learning journey", "Singapore Zoo", "v1 · 18/11/2026", '<span class="tag dash">Waiting on the parent</span>', "Sent 18/11/2026 · reminded 1 time", "28/11/2026"],
  ["Field trip / learning journey", "Science Centre", "v1 · 20/11/2026", '<span class="tag dash">Waiting on the parent</span>', "Sent 20/11/2026", "05/12/2026"],
  ["Medical authorisation", "—", "v1 · 01/01/2026", '<span class="tag solid">Agreed</span>', "Serena Lim · registration form · 05/01/2026", "—"],
  ["Privacy policy", "—", "v3 · 15/11/2026", '<span class="tag">Not sent</span>', "New version — agree again", "—"]];
function consentTab(o) {
  o = o || {};
  const body = childHeader({ level: "severe" })
    + `<div class="ph2"><div><b style="font-size:15px">Consents</b><p>Answers from the family. Consents are created in Communication › Surveys & consents.${A(1)}</p></div><div class="row"><span class="btn">Open Surveys & consents</span></div></div>`
    + table(["Consent", "Event" + A(3), "!Version", "!Status" + A(2), "!Answer / last action", "!Closing date", "!"], CONS.map(c => tr([c[0], c[1], c[2], c[3], c[4], c[5], c[3].includes("Waiting") ? '<span class="btn sm">Remind</span>' : c[3].includes("Not sent") ? '<span class="btn sm">Send request</span>' : '<span class="lnk">History</span>'])));
  return body;
}
function consentNewVersion() {
  return overlay("Publish new version — Privacy policy", `${fl("Summary of changes", "Added the Data Protection Officer contact: DPO@busybeesasia.com", { req: 1, ta: 1 })}
    <div class="radio"><div class="on"><i></i><span><b>Ask families to agree again</b><br><span style="color:var(--muted)">Every child goes back to "Not sent" for v3.</span></span></div>
    <div><i></i><span><b>Keep current answers</b><br><span style="color:var(--muted)">Small wording fix. Answers to v2 still count.</span></span></div></div>
    <div class="alert"><span class="anno">1</span><span>The choice is made per update, as BBA asked (BBA-488). Old answers stay in History.</span></div>`, '<span class="btn">Cancel</span><span class="btn primary">Publish</span>', 560);
}
function consentNew() {
  return overlay("New consent", `${grid2(fl("Type", "Field trip / learning journey", { sel: 1, req: 1, hint: "Crossroad only for Singapore centres without an outdoor area" }), fl("Event", "Singapore Zoo", { req: 1 }))}
    ${fl("Content", "Learning journey to Singapore Zoo on 28/11/2026, 09:00–12:00. Transport by school bus.", { req: 1, ta: 1 })}
    ${grid2(fl("Closing date", "28/11/2026", { req: 1 }), `<div class="field"><label>Audience <span class="req">*</span></label><div class="radio"><div class="on"><i></i>Classes${A(1)}</div><div><i></i>Whole centre</div></div></div>`)}
    <div class="field"><label>Classes <span class="req">*</span></label><div class="chips"><span class="on">☑ N2 · Sunbeams</span><span class="on">☑ K1 · Honeycombs</span><span>☐ N1 · Acorns</span></div></div>
    <div class="row" style="gap:10px"><span class="toggle"></span><span>Also send by email${A(2)}</span></div>
    <div class="alert"><span>Sending posts an Announcement with a link to this consent. Each child in the audience starts at "Waiting on the parent".</span></div>`, '<span class="btn">Cancel</span><span class="btn primary">Send</span>', 620);
}
function surveysList(o) {
  o = o || {};
  const f = [["Singapore Zoo", "Field trip / learning journey", "N2 · Sunbeams, K1 · Honeycombs", "28/11/2026", "28 of 34"], ["Science Centre", "Field trip / learning journey", "N2 · Sunbeams", "05/12/2026", "9 of 17"], ["Crossroad 2027", "Crossroad", "Whole centre", "15/01/2027", "0 of 72"]];
  const cards = `<div class="cnt" style="grid-template-columns:repeat(3,minmax(0,1fr))">${f.map((x, i) => `<div${o.unanswered && i === 0 ? ' style="border-color:var(--ink)"' : ""}><b>${x[4]}</b>families answered · ${x[0]}${i === 0 ? A(1) : ""}</div>`).join("")}</div>`;
  const top = head("Surveys & consents", "Consents sent to families. Answers show on each child's record.", '<span class="btn primary">+ New consent</span>')
    + utabs([["Surveys"], ["Consents", 3]], 1) + cards;
  if (o.unanswered) {
    const k = [["Noah Tan", "N2 · Sunbeams", "Sent 18/11/2026 · reminded 1 time"], ["Chloe Lim Xin Yi", "N2 · Sunbeams", "Sent 18/11/2026"], ["Lucas Koh", "K1 · Honeycombs", "Sent 18/11/2026"]];
    return top + `<div class="crumb">Singapore Zoo › <b>Not answered (6)</b></div>` + tb("Search child", 6) + flt("All classes", "Not answered")
      + table(["Child", "Class", "!Last action", "!"], k.map(x => tr([`<span class="lnk">${x[0]}</span>`, x[1], x[2], '<span class="btn sm">Remind</span>']))) + pager(6);
  }
  return top + tb("Search consent", 3) + flt("Small Wonder Tampines", "All types", "All classes", "Any status", "Any closing date")
    + table(["Consent", "Type", "Audience", "!Closing date", "!Answered"], f.map(x => tr([x[0], x[1], x[2], x[3], x[4]]))) + pager(3);
}
function consentCompliance() {
  const r = [["Ethan Lim", "N2 · Sunbeams", "—", "Singapore Zoo, Science Centre", "—"], ["Noah Tan", "N2 · Sunbeams", "—", "Singapore Zoo", "Media release"], ["Mia Wong", "Playgroup · Bumblebees", "Privacy policy", "—", "—"], ["Caleb Ho", "Playgroup · Bumblebees", "Privacy policy", "—", "—"]];
  return head("Consent compliance", "Children with a consent outstanding. Read from each child's consents.", '<span class="btn">⤓ Export (4)</span>')
    + utabs([["Today by centre"], ["Drills"], ["Consent compliance", 4]], 2) + tb("Search child", 4) + flt("Small Wonder Tampines", "All classes", "All consents", "Enrolled", "Any status")
    + table(["Child", "Class", "!Not sent", "!Waiting on the parent", "!Declined or withdrawn" + A(1)], r.map(x => tr([`<span class="lnk">${x[0]}</span>`, x[1], x[2], x[3], x[4]]))) + pager(4);
}

''')

# ---------- BBA-72 ----------
rep('{ req: 1, hint: "First day of the 2027 school year" + A(2) }', '{ req: 1, hint: "Start of Term 1, 2027 (brand term calendar)" + A(2) }')
rep('3 of 4 children selected · untick a child who repeats the level${A(3)}</span>',
    '3 of 4 children selected · untick a child who repeats the level, withdraws or extends${A(3)}<br>Moved children join the K1 · Honeycombs class thread; the N2 · Sunbeams thread becomes read-only.${A(4)}</span>')

# ---------- BBA-73/74/75 attendance ----------
rep('"36.8 · Before nap · 12:40"', '"36.8 · After nap · 14:40"')
rep('"36.7 · Before nap"', '"36.7 · After nap"')
rep('["NT", "Noah Tan", "N2 · 4y 10m", "", "Present", "09:34", "—", "Someone else: Ahmad · Driver"',
    '["NT", "Noah Tan", "N2 · 4y 10m", "", "Present", "09:34", "—", "Someone else: Ahmad · Family driver"')
rep('''  return head("Class attendance", "The gate records arrival and departure; staff correct and void here.", '<span class="btn">⤓ Export</span>')''',
    '''  if (o.bus) return head("Class attendance", "Bus 2 · Tampines North — children on this bus. Each child is signed in on their own, with a photo.", '<span class="btn">⤓ Export</span>')
    + utabs([["Class attendance"], ["Overview by centre"], ["Late arrival", 1], ["Void log"]], 0)
    + tb("Search child", 2) + flt("Small Wonder Tampines", "All classes", "Today · 24/11/2026", ["Bus 2 · Tampines North"], "Any status")
    + table(["Child", "!Class", "!Status", "!Handover", "!"], [tr([who("CL", "Chloe Lim Xin Yi", "N2 · 4y"), "N2 · Sunbeams", '<span class="tag">Not signed in</span>', '<small style="margin:0">Dropped off by</small>Bus driver · Bus 2' + A(1), '<span class="btn sm">Sign in</span>']),
      tr([who("LK", "Lucas Koh", "K1 · 5y 6m"), "K1 · Honeycombs", '<span class="tag solid">Present</span>', '<small style="margin:0">Dropped off by</small>Bus driver · Bus 2<small>📷 Photo · 08:05</small>', '<span class="act">⋯</span>'])]);
  return head("Class attendance", "The gate records arrival and departure; staff correct and void here.", '<span class="btn">⤓ Export</span>')''')
rep('flt("Small Wonder Tampines", ["N2 · Sunbeams"], "Today · 24/11/2026", "Any status", "Any temperature")',
    'flt("Small Wonder Tampines", ["N2 · Sunbeams"], "Today · 24/11/2026", "All bus routes", "Any temperature")')

TEMP_PICK = '''<div class="field"><label>Temperature <span class="req">*</span></label><div class="chips"><span>36.3</span><span>36.4</span><span class="on">36.5</span><span>36.6</span><span>36.7</span><span>Enter manually</span></div><span class="hint">Picker 36.0–40.0 °C, step 0.1. A Bluetooth thermometer fills it in; staff can change it.${A(%d)}</span></div>'''
block('function checkIn() {', 'function checkOut(block) {', '''function checkIn(o) {
  o = o || {};
  if (o.bus) return overlay("Sign in — Chloe Lim Xin Yi", `${fl("Time", "08:07", { req: 1, hint: "Defaults to now" })}
    ''' + TEMP_PICK % 2 + '''
    <div class="field"><label>Brought by <span class="req">*</span></label><div class="radio"><div><i></i>Mr Lim · Father</div><div><i></i>Mrs Lim · Mother</div><div class="on"><i></i>Bus driver · Bus 2 · Tampines North${A(1)}</div><div><i></i>Someone else</div></div></div>
    <div class="cam">📷 Photo of the child with the bus driver — required${A(3)}</div>`, '<span class="btn">Cancel</span><span class="btn primary">Sign in</span>', 580);
  return overlay("Sign in — Noah Tan", `${fl("Time", "09:34", { req: 1, hint: "Defaults to now" })}
    ''' + TEMP_PICK % 2 + '''
    <div class="field"><label>Brought by <span class="req">*</span></label><div class="radio">
      <div><i></i>Mr Tan · Father</div><div><i></i>Mrs Tan · Mother</div><div><i></i>Mdm Lee · Grandmother (authorised pickup)</div><div class="on"><i></i>Someone else${A(1)}</div></div></div>
    ${grid2(fl("Name", "Ahmad", { req: 1 }), fl("Relationship", "Family driver", { req: 1 }))}
    <div class="cam">📷 Photo of the child with the person — required${A(3)}</div>`, '<span class="btn">Cancel</span><span class="btn primary">Sign in</span>', 580);
}
''')
rep('''      <div class="${block ? "on" : ""}"><i></i>Not on the list</div></div></div>
    ${block ? `<div class="alert strong"><b>⚠ Do not release the child.</b><span>Call the parent and the Centre Director. Only a person on the approved pickup list can collect the child; one-time pickup persons are not supported.${A(2)}</span></div>` : ""}`,''',
    '''      <div class="${block ? "on" : ""}"><i></i>Not on the list</div></div></div>
    ${block ? `<div class="alert strong"><b>⚠ Do not release the child.</b><span>Call the parent to add this person in the Parents App. The person can collect the child once approved.${A(2)}</span></div>` : `<div class="cam">📷 Photo of the child with the person collecting — required${A(3)}</div>`}`,''')
block('function addReading() {', 'function voidRec() {', '''function addReading() {
  return overlay("Add a temperature reading — Aiden Tan Wei Jie", `${grid2(fl("Temperature", "37.9 °C", { req: 1, hint: "Entered manually · at or above 37.5 °C is a fever" + A(1) }), fl("Time", "15:40", { req: 1 }))}
    <div class="field"><label>When <span class="req">*</span></label><div class="chips"><span>On arrival</span><span>After nap</span><span class="on">Before pickup</span><span>Extra</span></div></div>
    <div class="alert strong"><b>⚠ Fever</b><span>Saving notifies the class teacher and the Centre Director.</span></div>`, '<span class="btn">Cancel</span><span class="btn primary">Save reading</span>', 540);
}
''')
rep('''tr(["Late arrival cut-off" + A(1), "<b>09:15</b>", "Centre · default", '<span class="btn sm">Change</span>']), ''',
    '''tr(["Late arrival cut-off — morning" + A(1), "<b>09:15</b>", "Centre · default", '<span class="btn sm">Change</span>']), tr(["Late arrival cut-off — afternoon", "<b>12:15</b>", "Centre", '<span class="btn sm">Change</span>']), ''')

# ---------- BBA-78 routines ----------
block('function routines(o) {', '/* ===================== BBA-79', '''function routines(o) {
  o = o || {};
  const r = [["Mia Wong", "Lunch · All<small>Chicken rice, broccoli · 11:50 · Aisyah Rahman · Teacher app</small>", "—", "13:00–14:30 · 1h 30m<small>Slept well</small>", "Diaper · Wet<small>10:15</small>", "Note from home"],
    ["Caleb Ho", `<span class="tag dash">Missing: Lunch</span>${A(2)}`, "150 ml made · 120 ml drunk<small>10:00</small>", "13:10–14:20 · 1h 10m", "Diaper · Dry<small>10:20</small>", ""]];
  const body = head("Daily routines", "Playgroup · Bumblebees · Small Wonder Tampines · Today", `<span class="btn">Parent view</span><span class="btn">⤓ Export (2)</span><span class="btn primary">Record for the whole class${A(1)}</span>`)
    + tb("Search child", 2, '<span class="tot">Required every day for <b>Infant</b> <b>Playgroup</b></span>') + flt("Small Wonder Tampines", ["Playgroup · Bumblebees"], "Today · 24/11/2026", "All children", "Recorded in: all apps")
    + table(["Child", "!Food" + A(3), "!Bottle", "!Nap", "!Potty", "!"], r.map(x => tr([x[0] + (x[5] ? `<small>📝 ${x[5]}</small>` : ""), x[1], x[2], x[3], x[4], '<span class="lnk">Change time</span>'])));
  if (!o.dialog) return body;
  return body + overlay("Record for the whole class — Food", `<div class="field"><label>Type <span class="req">*</span></label><div class="chips"><span class="on">Food</span><span>Bottle</span><span>Nap</span><span>Potty</span></div></div>
    ${grid2(fl("Meal", "Lunch", { sel: 1, req: 1 }), fl("Time", "11:50", { req: 1 }))}
    ${fl("Menu", "Chicken rice, steamed broccoli, orange slices")}
    <div class="field"><label>Amount eaten</label><div class="chips"><span class="on">All</span><span>Most</span><span>Some</span><span>None</span></div></div>
    <div class="field"><label>Children (checked in today)</label><div class="chips"><span class="on">☑ Mia Wong</span><span>☐ Caleb Ho</span></div><span class="hint">Untick a child to leave them out; change one child afterwards on the class view.${A(1)}</span></div>`, '<span class="btn">Cancel</span><span class="btn primary">Save for 1 child</span>', 600);
}

''')

# ---------- SCREENS notes / states ----------
rep('''    [["default", "Tab Consents", () => shell("children", "All children › <b>Ethan Lim</b>", consentTab(), W.cd, childTabs(8))],
     ["version", "Phiên bản mới", () => shell("consents", "Surveys & consents › <b>PDPA</b>", surveysList() + consentNewVersion(), W.hq)]],
    { default: [["Consent nằm ở tab Documents của hồ sơ trẻ (theo prototype); biểu mẫu tạo ở Surveys & consents. Gửi / nhắc ngay trên hồ sơ trẻ còn chờ chốt.", "BR-CHF-010 · Proto SMS · OQ-12"], ["Trạng thái theo prototype: Not sent · Waiting on the parent · Agreed · Declined · Withdrawn · Expired.", "Proto SMS Consent compliance"]],
      version: [["Khi sửa nội dung, người sửa chọn có yêu cầu đồng ý lại hay không.", "Plane BBA-488 · AS-04 · OQ-10"]] }),''',
    '''    [["default", "Tab Consents", () => shell("children", "All children › <b>Ethan Lim</b>", consentTab(), W.cd, childTabs(8))],
     ["list", "Danh sách consent", () => shell("consents", "Communication › <b>Surveys & consents</b>", surveysList(), W.cd)],
     ["unanswered", "Chưa trả lời", () => shell("consents", "Communication › <b>Surveys & consents</b>", surveysList({ unanswered: 1 }), W.cd)],
     ["new", "Tạo consent", () => shell("consents", "Communication › <b>Surveys & consents</b>", surveysList() + consentNew(), W.cd)],
     ["version", "Phiên bản mới", () => shell("consents", "Surveys & consents › <b>Privacy policy</b>", surveysList() + consentNewVersion(), W.hq)]],
    { default: [["Consent nằm ở tab Documents của hồ sơ trẻ; consent tạo ở Surveys & consents.", "FR-001 · BR-CHF-010"], ["Trạng thái: Not sent · Waiting on the parent · Agreed · Declined · Withdrawn · Expired.", "FR-002"], ["Nhiều consent cùng loại đang mở, mỗi cái gắn một sự kiện.", "Q-73-14 · FR-001"]],
      list: [["Thẻ \\"x of y families answered\\" mỗi consent; chọn thẻ → chỉ trẻ chưa trả lời.", "Q-73-10 · FR-012"]],
      unanswered: [["Danh sách trẻ chưa trả lời, Remind từng trẻ.", "Q-73-10 · FR-004 · FR-012"]],
      new: [["Đối tượng theo lớp hoặc cả Centre, có ngày đóng.", "Q-73-04 · FR-003"], ["Email chỉ gửi khi bật; luôn tạo Announcement kèm link.", "Q-73-08 · FR-003"]],
      version: [["Khi sửa nội dung, người sửa chọn có yêu cầu đồng ý lại hay không.", "Plane BBA-488 · FR-006"]] }),''')
rep('''    { default: [["Vượt sĩ số chỉ cảnh báo.", "FR-004 · BR-003"], ["Ngày hiệu lực mặc định đầu năm học mới — chờ BBA chốt ngày.", "AS-01 · OQ-02 (FRD)"], ["Bỏ chọn trẻ học lại; trẻ bỏ chọn ở lại lớp cũ.", "BR-CHF-048"]] }),''',
    '''    { default: [["Vượt sĩ số chỉ cảnh báo.", "FR-004 · BR-003"], ["Ngày hiệu lực mặc định: ngày bắt đầu Term 1 năm sau theo lịch brand — chờ BBA chốt.", "Q-71-03 · AS-01 · OQ-02"], ["Bỏ chọn trẻ học lại, rút, gia hạn; trẻ bỏ chọn giữ lớp hoặc chuyển lớp khác cùng level.", "Q-74-03 · FR-003"], ["Lớp mới có thread mới; thread lớp cũ chỉ đọc.", "Q-74-10 · FR-005"]] }),''')
rep('''     ["checkin", "Nhận trẻ · Someone else", () => shell("attendance", "Daily operations › <b>Class attendance</b>", attendance() + checkIn(), W.sa)],''',
    '''     ["checkin", "Nhận trẻ · Someone else", () => shell("attendance", "Daily operations › <b>Class attendance</b>", attendance() + checkIn(), W.sa)],
     ["bus", "Lọc theo xe", () => shell("attendance", "Daily operations › <b>Class attendance</b>", attendance({ bus: 1 }), W.sa)],
     ["busin", "Nhận trẻ từ xe", () => shell("attendance", "Daily operations › <b>Class attendance</b>", attendance({ bus: 1 }) + checkIn({ bus: 1 }), W.sa)],''')
rep('''["Lần đo ≥ 37.5 °C in đậm; \\"x of 3\\" là số lần đo bắt buộc (giả định).", "BBA-74 · BR-OPS-012 · AS-05 · OQ-13"]],
      checkin: [["\\"Someone else\\" chỉ dùng khi nhận trẻ; bắt buộc tên và quan hệ.", "SRS ATT · FRD AS-02"]],''',
    '''["Lần đo ≥ 37.5 °C in đậm; \\"x of 3\\" = On arrival, After nap, Before pickup — chỉ một số Centre đo 3 lần.", "BBA-74 · Q-81-02 · AS-04 · OQ-06"]],
      checkin: [["\\"Someone else\\" chỉ dùng khi nhận trẻ; bắt buộc tên và quan hệ.", "SRS ATT · BBA-73 FR-001"], ["Nút nhanh 36.3–36.7, mặc định 36.5, \\"Enter manually\\"; số từ nhiệt kế Bluetooth sửa được.", "Q-76-05 · Q-76-06 · BBA-74 FR-001 · FR-003"], ["Chụp ảnh trẻ cùng người giao; phụ huynh thấy ảnh trong app.", "Q-75-10 · Q-81-02 · BBA-73 FR-010"]],
      bus: [["Bộ lọc theo xe chỉ để gom; nhận / trả từng trẻ, mỗi trẻ một bản ghi và ảnh.", "Q-75-10 · BBA-73 FR-008"]],
      busin: [["Xe đến: người giao là tài xế; xe về: người nhận là phụ xe của công ty xe.", "Q-75-10 · BBA-73 FR-008"], [], ["Ảnh riêng từng trẻ.", "BBA-73 FR-010"]],''')
rep('''      checkout: [["Chỉ chọn được người trong danh sách đã duyệt; người chờ duyệt không chọn được.", "BR-OPS-004 · BR-CDP-024"]],
      blocked: [["Người chờ duyệt không chọn được.", "BR-CDP-024"], ["Không có người đón một lần → chặn, không cho CD trả trẻ.", "BR-CDP-025 · BR-ATT-005"]],''',
    '''      checkout: [["Chỉ chọn được người trong danh sách đã duyệt; người chờ duyệt không chọn được.", "BR-OPS-004 · BR-CDP-024"], [], ["Chụp ảnh trẻ cùng người đón.", "BBA-73 FR-010"]],
      blocked: [["Người chờ duyệt không chọn được.", "BR-CDP-024"], ["Không override: gọi phụ huynh thêm người này trong Parents App; được duyệt mới đón.", "Q-75-02 · Q-75-04 · BBA-73 FR-004"]],''')
rep('''    { default: [["Giờ chốt theo Centre, mặc định 09:15; đổi chỉ áp từ ngày đổi.", "BR-OPS-014 · BR-ADM-040 · FRD FR-007"], ["Ngưỡng sốt theo quốc gia (SRS) — prototype iPad cho chỉnh trên máy.", "OQ-14"]] }),''',
    '''    { default: [["Giờ chốt theo Centre: sáng 09:15, chiều 12:15; so với giờ ghi nhận ở cổng; đổi chỉ áp từ ngày đổi.", "Q-77-03 · BBA-75 FR-001 · FR-002 · FR-007"], ["Ngưỡng sốt theo quốc gia (SRS) — prototype iPad cho chỉnh trên máy.", "OQ-14"]] }),''')
rep('''["Thêm cột Mood theo SRS CD app và prototype.", "SRS CDP · Proto SMS"]], class: [] }),''',
    '''["4 loại theo Taidii: Food, Bottle, Nap, Potty — bỏ Mood.", "Q-86-01 · FR-001"]], class: [["Bỏ chọn trẻ ngoại lệ trước khi lưu; chỉnh từng trẻ sau khi lưu.", "Q-86-04 · FR-003"]] }),''')
open(p, 'w', encoding='utf-8').write(s)
print('wf ok')
