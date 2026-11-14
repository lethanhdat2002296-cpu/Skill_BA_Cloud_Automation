import sys
p = sys.argv[1] + '/wf_body.html'
s = open(p, encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:70]; s = s.replace(a, b)
# 1. entry screen: view switch + export
rep('''  return head("Height & weight", "Four terms a year (Brighton: two semesters). Every age, no approval. Entries appear immediately for the family.", `<span class="btn primary">Save the whole class${A(1)}</span>`)
    + utabs([["Allergies & conditions", 5], ["Growth"]], 1)''',
'''  return head("Height & weight", "Four terms a year (Brighton: two semesters). Every age, no approval. Entries appear immediately for the family.", `<span class="btn primary">Save the whole class${A(1)}</span>`)
    + utabs([["Allergies & conditions", 5], ["Growth"]], 1)
    + '<div class="chips" style="margin-bottom:10px"><span class="on">Enter this term</span><span>Year view</span></div>\'''')
s = s.replace("+ '<div class=\"chips\" style=\"margin-bottom:10px\"><span class=\"on\">Enter this term</span><span>Year view</span></div>\\'", "+ '<div class=\"chips\" style=\"margin-bottom:10px\"><span class=\"on\">Enter this term</span><span>Year view</span></div>'")
# 2. new functions before growthReport
NEW = r'''const YR = [["Ethan Lim", "14/02/2022", "••••482K", "N2 full day", ["104.0", "16.9"], ["105.5", "17.2"], ["107.0", "17.6"], ["108.5", "18.1"]],
  ["Aiden Tan Wei Jie", "20/01/2022", "••••115J", "N2 full day", ["91.0", "13.0"], ["92.0", "13.2"], ["93.0", "13.5"], ["", ""]],
  ["Chloe Lim Xin Yi", "02/11/2022", "••••907C", "N2 half day AM", ["93.0", "14.1"], ["94.0", "14.4"], ["95.0", "14.7"], ["96.5", "15.0"]],
  ["Noah Tan", "18/01/2022", "••••330F", "N2 full day", ["", ""], ["", ""], ["", ""], ["", ""]],
  ["Olivia Wong Mei Ling", "05/12/2022", "••••761H", "N2 full day", ["94.5", "13.6"], ["96.0", "13.9"], ["98.0", "14.1"], ["", ""]],
  ["Sofia D'Cruz", "21/02/2022", "••••204B", "N2 full day", ["99.0", "14.8"], ["100.0", "15.0"], ["101.0", "15.2"], ["", ""]]];
function growthYear() {
  const c = (v) => v ? v : '<span style="color:var(--muted)">—</span>';
  const th = `<tr><th rowspan="2">No.</th><th rowspan="2">Child</th><th rowspan="2">Birthdate</th><th rowspan="2">IC / BC No.${A(2)}</th><th rowspan="2">Programme</th>${[1, 2, 3, 4].map(t => `<th colspan="2" style="text-align:center">Term ${t}</th>`).join("")}</tr><tr>${[1, 2, 3, 4].map(() => "<th>Height cm</th><th>Weight kg</th>").join("")}</tr>`;
  const rows = YR.map((r, i) => `<tr><td>${i + 1}</td><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td>${[4, 5, 6, 7].map(k => `<td>${c(r[k][0])}</td><td>${c(r[k][1])}</td>`).join("")}</tr>`).join("");
  return head("Height & weight", "Year view · one row per child, Term 1 to Term 4 — the same layout as the Quarterly Heights & Weight Report kept today.", `<span class="btn">⤓ Export (Excel)${A(1)}</span>`)
    + utabs([["Allergies & conditions", 5], ["Growth"]], 1)
    + '<div class="chips" style="margin-bottom:10px"><span>Enter this term</span><span class="on">Year view</span></div>'
    + `<div class="flt" style="grid-template-columns:repeat(3,minmax(0,1fr))">${sel("Small Wonder Tampines")}${sel("N2 · Sunbeams", 1)}${sel("Year 2026", 1)}</div>`
    + `<div class="tbl"><table class="t">${th}${rows}</table></div>`
    + `<div class="alert"><span>Brighton Montessori measures by semester; the Taidii export of a Brighton centre still shows Term 1 to Term 4 columns.${A(3)}</span></div>`;
}
function growthChart() {
  const X = (m) => 40 + (m - 24) * 7.5, Y = (cm) => 230 - (cm - 80) * 4;   // 24–72 months, 80–130 cm
  const line = (pts) => pts.map((q, i) => `${i ? "L" : "M"}${X(q[0]).toFixed(1)} ${Y(q[1]).toFixed(1)}`).join(" ");
  const p3 = [[24, 81], [36, 89], [48, 96], [60, 102], [72, 108]], p50 = [[24, 87], [36, 95], [48, 103], [60, 110], [72, 116]], p97 = [[24, 93], [36, 102], [48, 110], [60, 118], [72, 124]];
  const kid = [[48, 104.0], [51, 105.5], [54, 107.0], [57, 108.5]];
  const lab = (pts, t) => `<text x="${X(72) + 6}" y="${Y(pts[4][1]) + 4}" font-size="11" fill="currentColor">${t}</text>`;
  return `<svg viewBox="0 0 470 260" width="100%" style="max-width:520px;color:var(--muted)" role="img" aria-label="Height for age">
    ${[80, 90, 100, 110, 120, 130].map(v => `<line x1="40" x2="400" y1="${Y(v)}" y2="${Y(v)}" stroke="var(--line)" stroke-dasharray="3 3"/><text x="8" y="${Y(v) + 4}" font-size="11" fill="currentColor">${v}</text>`).join("")}
    ${[24, 36, 48, 60, 72].map(m => `<text x="${X(m) - 10}" y="250" font-size="11" fill="currentColor">${m / 12}y</text>`).join("")}
    <path d="${line(p97)} ${line(p3.slice().reverse()).replace("M", "L")} Z" fill="var(--fill)"/>
    <path d="${line(p3)}" fill="none" stroke="var(--muted)"/><path d="${line(p50)}" fill="none" stroke="var(--muted)" stroke-dasharray="5 3"/><path d="${line(p97)}" fill="none" stroke="var(--muted)"/>
    ${lab(p97, "97th")}${lab(p50, "50th")}${lab(p3, "3rd")}
    <path d="${line(kid)}" fill="none" stroke="var(--ink)" stroke-width="2"/>${kid.map(q => `<circle cx="${X(q[0])}" cy="${Y(q[1])}" r="4" fill="var(--ink)"/>`).join("")}
  </svg>`;
}
function growthChild() {
  const h = [["Term 4 · 2026", "24/11/2026", "108.5", "18.1", "+1.5 cm · +0.5 kg", "Aisyah Rahman · Teacher · class entry"], ["Term 3 · 2026", "14/08/2026", "107.0", "17.6", "+1.5 cm · +0.4 kg", "Aisyah Rahman · Teacher · class entry"], ["Term 2 · 2026", "12/05/2026", "105.5", "17.2", "+1.5 cm · +0.3 kg", "Grace Tan · Centre Director · child record"], ["Term 1 · 2026", "10/02/2026", "104.0", "16.9", "—", "Aisyah Rahman · Teacher · class entry"]];
  return childHeader({ level: "severe" })
    + '<div class="chips" style="margin:4px 0 10px"><span>Allergies & conditions</span><span class="on">Growth</span></div>'
    + `<div class="ph2"><div><b style="font-size:15px">Growth</b><p>Shown to the family in the Parents App as soon as it is saved.${A(1)}</p></div><div class="row"><span class="btn primary">+ Add measurement${A(2)}</span></div></div>`
    + `<div class="card" style="padding:14px 16px;margin-bottom:12px"><div class="row between"><b>Height for age</b><div class="chips"><span class="on">Height</span><span>Weight</span></div></div>${growthChart()}
       <div style="font-size:12px;color:var(--muted)">Plotted against the Singapore reference (National Healthcare Group Polyclinics anthropometric study). Malaysia centres use the Child Health Record Book. No BMI.${A(3)}</div></div>`
    + table(["Term", "Date measured", "!Height (cm)", "!Weight (kg)", "!Change since last term" + A(4), "!Recorded by", "!"], h.map(x => tr([x[0], x[1], x[2], x[3], x[4], x[5], '<span class="lnk">Edit</span> · <span class="lnk">Delete</span>'])))
    + `<div class="total">Measurement history · 4 measurements${A(5)}</div>`;
}
'''
rep('function growthReport() {', NEW + 'function growthReport() {')
rep('''  return head("Height & weight completion", "Children measured this term, by centre and class.", '<span class="btn">⤓ Export (4)</span>')''',
    '''  return head("Height & weight completion", "Children measured this term, by centre and class. Completion status only, no growth statistics.", '<span class="btn">⤓ Export (4)</span>')''')
# 3. screens
rep('''     ["delete", "Xoá số đo", () => shell("health", "Health & allergies › <b>Growth</b>", growthEntry({ saved: 1 }) + growthDelete(), W.t)]],''',
'''     ["delete", "Xoá số đo", () => shell("health", "Health & allergies › <b>Growth</b>", growthEntry({ saved: 1 }) + growthDelete(), W.t)],
     ["year", "Xem cả năm · Export", () => shell("health", "Health & allergies › <b>Growth</b>", growthYear(), W.t)]],''')
rep('''      saved: [], delete: [[], [], [], ["Một quyền chung thêm / sửa / xoá; hiện giao CD, Admin, mọi Teacher.", "Plane BBA-1059 Q3"]] }),''',
'''      saved: [], delete: [[], [], [], ["Một quyền chung thêm / sửa / xoá; hiện giao CD, Admin, mọi Teacher (Taidii: \\"Update Height and Weight\\" cho CD/ACD/Admin và Teachers).", "Plane BBA-1059 Q3 · Taidii Center Staff Role permissions, dòng 14"]],
      year: [["Bảng cả năm và file Excel theo đúng bố cục \\"Quarterly Heights & Weight Report\\" của Taidii: No., Name, Birthdate, IC/BC No., Program Type, Term 1–4 mỗi kỳ Height cm / Weight kg; đầu file ghi Centre, Class, Year, Generated on.", "Plane BBA-529 — file mẫu Student_quarterly_height_weight_2026-sample.xlsx · FR-013"], ["Số giấy tờ che theo vai trò như hồ sơ trẻ.", "BBA-66"], ["File mẫu của Brighton (đo theo học kỳ) vẫn có cột Term 1–4 → hỏi lại cách hiện Brighton.", "Plane BBA-529 · OQ-08"]] }),
  S("b70-3", "BBA-70 · 3", "Child record — Growth", "Biểu đồ và Measurement history trên hồ sơ trẻ — BBA-1059 Q1, Q4",
    [["default", "Tab Health · Growth", () => shell("children", "All children › <b>Ethan Lim</b>", growthChild(), W.cd, childTabs(6))]],
    { default: [["Phụ huynh thấy ngay khi lưu.", "Plane BBA-1059 Q4 · FR-008"], ["Nhập riêng một trẻ từ hồ sơ.", "FR-007"], ["Biểu đồ theo tuổi: Singapore theo nghiên cứu nhân trắc của NHG Polyclinics, Malaysia theo Child Health Record Book; Taidii hiện vẽ theo WHO với 3 đường 3rd / 50th / 97th. Đường cong trên wireframe chỉ minh hoạ. Có hiện đường percentile hay không còn chờ OQ-07 (Q-71-02 bỏ percentile).", "Plane BBA-1059 Q1 · ảnh Taidii Parents App · OQ-07"], ["Thay đổi so với kỳ trước.", "Q-71-11 · FR-012"], ["Mọi lần đo theo ngày đo, người nhập.", "Q-71-07 · Q-71-08 · FR-012"]] }),''')
rep('''    { default: [["Chỉ trạng thái hoàn thành theo Centre, lớp, kỳ; người dùng CD, Admin, Cluster Head.", "Plane BBA-1059 Q5 · BBA-524"]] }),''',
    '''    { default: [["Chỉ trạng thái hoàn thành theo Centre, lớp, kỳ; người dùng ban đầu: CD, Admin, Cluster Head.", "Plane BBA-1059 Q5 · FR-009"]] }),''')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
