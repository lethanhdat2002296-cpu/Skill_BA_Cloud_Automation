import sys
p = sys.argv[1] + '/wf_body.html'
s = open(p, encoding='utf-8').read()
i = s.index('const ALG = ['); j = s.index('/* ===================== BBA-70 Growth')
NEW = r'''const ALG = [
  // initials, name, class, type, [[allergen, severity]], symptoms, can tolerate, traces eggs/nuts, action plan, medication, next review, review tag, staff note, severe, awaiting
  ["EL", "Ethan Lim", "N2 · Sunbeams", "Food", [["Shellfish and nuts, including peanuts", "Severe"]], "Lip swelling, hives, difficulty breathing", "Can eat fish but not shellfish", "Eggs: Yes · Nuts: No", "Give the EpiPen, call 995, then call the mother.", "EpiPen Jr 0.15 mg · medication form ✓", "18/03/2027", "", "Reacted to a biscuit with traces of nut on 03/09.", 1, 1],
  ["SC", "Sophia Chen", "K1 · Honeycombs", "Food", [["Dairy", "Severe"]], "Vomiting, hives", "Can have butter or baked dairy (cookies, bread); no milk, cheese or yogurt", "Eggs: Yes · Nuts: Yes", "Give the auto-injector, call 995, then call the father.", "Adrenaline auto-injector · medication form ✓", "16/12/2026", "due", "", 1, 0],
  ["LK", "Lucas Koh", "K1 · Honeycombs", "Insect", [["Bee and wasp stings", "Moderate"]], "Swelling at the sting site", "—", "—", "Remove the sting, cold pack, antihistamine; call the mother.", "Antihistamine syrup 5 ml · medication form ✓", "02/11/2026", "over", "", 0, 0],
  ["CL", "Chloe Lim Xin Yi", "N2 · Sunbeams", "Medication", [["Penicillin", "Moderate"]], "Rash", "—", "—", "Tell the parent before any medicine is given.", "Not applicable", "05/04/2027", "", "", 0, 0]];
const OTHER = [
  ["RI", "Rayyan Idris", "K1 · Honeycombs", "Medical condition", "Asthma; coughing can start after outdoor play on very hot afternoons.", "Inhaler, 2 puffs; call the mother.", "21/01/2027"],
  ["NT", "Noah Tan", "N2 · Sunbeams", "Medical history", "Receives speech therapy through the Early Intervention programme.", "—", "03/03/2027"]];
const reviewCell = (d, t) => d + (t === "due" ? ` <span class="tag dash">Due in 3 weeks</span>${A(5)}` : t === "over" ? ' <span class="tag solid">Overdue</span>' : "");
function allergyList(o) {
  o = o || {};
  const kids = o.cls ? ALG.filter(a => a[2] === "N2 · Sunbeams") : ALG;
  const others = o.cls ? OTHER.filter(a => a[2] === "N2 · Sunbeams") : OTHER;
  const g = (t) => tr([t, "", "", "", "", "", ""], "grp");
  const rows = [g('<b>Allergies</b> · most severe first' + A(1))]
    .concat(kids.map(a => tr([who(a[0], a[1] + (a[14] ? ` <span class="tag dash">Family update · awaiting assessment</span>${A(4)}` : ""), a[2]) + (a[12] ? `<small>📝 ${a[12]}</small>` : ""),
      `<small style="margin:0">${a[3]}</small>` + a[4].map(x => `${x[0]} <span class="tag${x[1] === "Severe" ? " solid" : ""}">${x[1]}</span>`).join("<br>"),
      a[5], a[6] + (a[7] !== "—" ? `<small>Traces · ${a[7]}</small>` : ""), `${a[8]}<small>${a[9]}</small>`, reviewCell(a[10], a[11]), '<span class="lnk">Health</span>'], a[13] ? "sev" : "")))
    .concat([g('<b>Other conditions and diet</b>' + A(2))])
    .concat(others.map(a => tr([who(a[0], a[1], a[2]), `<small style="margin:0">${a[3]}</small>${a[4]}`, "—", "—", a[5], a[6], '<span class="lnk">Health</span>'])));
  if (!o.cls) rows.push(g('<b>Health information not provided</b>' + A(6)), tr([who("MW", "Mia Wong", "Playgroup · Bumblebees"), '<span style="color:var(--muted)">The family has not filled in the Medical Care Assessment yet.</span>', "", "", "", "—", '<span class="lnk">Contact the family</span>']));
  const n = kids.length + others.length;
  return head("Allergies & conditions", "Medical Health Alert List · from each child's Medical Care Assessment, as confirmed by the Centre.", `<span class="btn">⤓ Export (${n})${A(3)}</span><span class="btn primary">🖨 Print for the kitchen${A(3)}</span>`)
    + utabs([["Allergies & conditions", n], ["Growth"]], 0)
    + tb("Search child or allergen", n)
    + flt("Small Wonder Tampines", o.cls ? ["N2 · Sunbeams"] : "All classes", "All severities", "Type: all", "Review: any")
    + table(["Child", "!Type · allergen · severity", "!Symptoms", "!Can tolerate", "!Emergency action plan · medication", "!Next review", "!"], rows) + pager(n);
}
function kitchenPrint() {
  const k = ALG.filter(a => a[2] === "N2 · Sunbeams");
  return `<div class="print"><div class="row between"><div><h4>Medical Health Alert List — Small Wonder Tampines · N2 · Sunbeams</h4><span>Printed 24/11/2026 08:15 · ${k.length + 1} children${A(1)}</span></div><span>Page 1 of 1</span></div>
    <table class="t" style="margin-top:10px"><thead><tr><th>Photo</th><th>Child</th><th>Type · allergen · severity</th><th>Can tolerate</th><th>Traces of eggs / nuts</th><th>Emergency action plan</th></tr></thead><tbody>
    ${k.map(a => tr([`<span class="mini-av">${a[0]}</span>`, `<b>${a[1]}</b>`, `${a[3]} · ${a[4].map(x => `${x[0]} — <b>${x[1]}</b>`).join("<br>")}`, a[6], a[7], a[8]])).join("")}
    ${tr(['<span class="mini-av">NT</span>', "<b>Noah Tan</b>", "Medical history · speech therapy (Early Intervention)", "—", "—", "—"])}
    </tbody></table><p style="margin:10px 0 0;color:#555">Most severe first. Only children whose families agreed to show the name and photo on the Medical Health Alert List are printed.${A(2)}</p></div>`;
}

'''
s = s[:i] + NEW + s[j:]
old = s[s.index('  S("b69", "BBA-69"'):s.index('  S("b70-1"')]
new = '''  S("b69", "BBA-69", "Allergies & conditions", "Medical Health Alert List; in cho bếp — BBA-1058 + Appendix 1, Appendix 3",
    [["default", "Toàn Centre", () => shell("health", "Health & allergies › <b>Allergies & conditions</b>", allergyList(), W.t)],
     ["class", "Lọc 1 lớp", () => shell("health", "Health & allergies › <b>Allergies & conditions</b>", allergyList({ cls: 1 }), W.t)],
     ["print", "Bản in cho bếp", () => shell("health", "Health & allergies › <b>Print</b>", kitchenPrint(), W.t)]],
    { default: [["Cột theo form Medical Care Assessment Checklist: loại (Food, Environmental, Medication, Insect, Medical condition), chất gây dị ứng, mức độ, triệu chứng, điều kiện dung nạp, ăn được vết trứng / hạt, kế hoạch xử trí, thuốc dùng ngay. Severe → Moderate → Mild; chưa chọn mức coi như Severe.", "Appendix 1 tr. 1–2 · FR-001 · FR-002"], ["Bệnh / tiền sử không kèm dị ứng ở nhóm riêng.", "Appendix 1 tr. 1 · FR-003 · OQ-07"], ["CD, Admin, Teacher được in / xuất; không lưu nhật ký in / xuất.", "Plane BBA-1058 Q2 · FR-008"], ["Phụ huynh sửa trong app → danh sách giữ thông tin đã xác nhận, gắn nhãn chờ đánh giá cho tới khi CD / Admin hoàn tất.", "Plane BBA-1058 Q1 · FR-014"], ["Đánh giá lại mỗi 6 tháng; nhắc trước 1 tháng (gửi form cho phụ huynh); quá ngày hiện Overdue.", "Appendix 3 · Plane BBA-1058 Q1 · FR-013"], ["Trẻ chưa khai Health record ở nhóm riêng cuối danh sách.", "Q-70-09 · FR-012"]],
      class: [], print: [["Bản in ghi ngày giờ in và số trẻ.", "FR-007 · BR-003"], ["Chỉ in trẻ có phụ huynh đồng ý hiện tên và ảnh trên Medical Health Alert List.", "Appendix 1 tr. 3 · Plane BBA-1058 Q2 · FR-011"]] }),
'''
s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('ok')
