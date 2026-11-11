# Brainstorm Sprint 4 — BBA (5 feature chính thức)

> Tài liệu nội bộ, không đẩy Drive. Ngày: 09/11/2026.
> Phạm vi Sprint 4 do user chốt (ảnh WBS): **2.3 Enquiry actions (state…)**, **2.8 CRM Administration**, **3.1 Children & families**, **3.2 Daily operations**, **3.6 Finance (rebuilt to Tai…)** → 5 FRD.
> Cách làm: chỉ dùng dữ kiện trong SRS của dự án (`Document/SRS/*.md`) và FRS Sprint 3 (`Document/FSD/Sprint 3/`). Mỗi dữ kiện ghi nguồn. Không có dữ kiện → `AS-xx` (giả định, cần xác nhận) hoặc `OQ-xx`. Không thêm tính năng ngoài SRS.
> Thứ tự: viết bản **tiếng Việt** trước → user duyệt → mới dịch sang tiếng Anh.
> Tên ảnh bị cắt ("state…", "rebuilt to Tai…") → tên đầy đủ hỏi ở OQ-01.

## 0. Ánh xạ feature ↔ nguồn SRS

| Feature (ảnh) | Nguồn SRS | Mục / mã WBS dùng | Đã có ở Sprint 3 (chỉ dẫn chiếu) |
|---|---|---|---|
| 2.3 Enquiry actions | `BBA_CRM_SRS_v0.1.md` | §1.1 (WBS 2.3.1.01–05, 2.3.1.09; 2.3.2.03, .05, .07, .08), §1.2, §3 P2 bước 7, P4, P6 bước 15, §4 mục 3.2–3.3, §5 BR-CRM-012, 019–022, 037–038, §6.1, §8 AC-CRM-004, 012 | BBA-43 (hiển thị Actions & SLA, Enquiry Status Catalogue §7.1), BBA-44 (Timeline) |
| 2.8 CRM Administration → Approvals | `BBA-SMS-SRS-Administration-v0.1.md` + `…-00-General-Requirements` + prototype `/organisation/approvals` | §3 P4, P5; §4 mục 2.3, 2.4, 4.1, 4.2; BR-ADM-016–023, 036, 037, 042; GEN §3.3, §4.4 | — |
| 3.1 Children & families | `BBA-SMS-SRS-Children-and-Families-v0.1.md` (+ `…-00-General-Requirements`) | xem mục 3.1 bên dưới | — |
| 3.2 Daily operations | `BBA-SMS-SRS-Daily-Operations-v0.1.md` (+ General) | xem mục 3.2 bên dưới | — |
| 3.6 Finance | `BBA-SMS-SRS-Fees-and-Payments-v0.1.md` (+ General) — SRS ghi "close each month without Taidii" (§1) khớp tên "rebuilt to Tai[dii]" | xem mục 3.6 bên dưới | — |

## Assumptions & Open Questions chung

| Mã | Nội dung | Loại | Liên quan |
|---|---|---|---|
| AS-01 | Sprint 4 chỉ gồm tính năng **Phase 1** của từng nhóm WBS; tính năng Phase 2/3 trong cùng nhóm ghi ở "Ngoài phạm vi". | AS → OQ-02 | cả 5 |
| AS-02 | Nhóm "2.3" gồm cả 2.3.1 (Enquiry actions) và 2.3.2 (Journey automation foundation) vì cùng mã 2.3. | AS → OQ-03 | 2.3 |
| OQ-01 | Tên đầy đủ của "2.3 Enquiry actions (state…)" và "3.6 Finance (rebuilt to Tai…)"; mã ticket chính thức của 5 FRD. | OQ | 2.3, 3.6 |
| OQ-02 | Sprint 4 có gồm tính năng Phase 2/3 của cùng nhóm WBS không? | OQ | cả 5 |
| OQ-03 | Nhóm 2.3 có gồm 2.3.2 Journey automation (Journey assignment, Event-key engine, Task assignment, Automated messages) không, hay để FRD khác? | OQ | 2.3 |

---

## 2.3 Enquiry actions

**1. Bối cảnh & vấn đề**
- Enquiry là bối cảnh tuyển sinh theo Centre của một Lead, sở hữu owner, status, Journey và lịch sử vận hành (nguồn: CRM SRS BR-CRM-012).
- Status chỉ đổi qua Action được phép hoặc quy trình sở hữu, không sửa trực tiếp (nguồn: BBA-43 BR-012; CRM SRS BR-CRM-021). BBA-43 dẫn chiếu "Authoritative Enquiry Action catalogue and Status mapping (BBA-55)" — chưa có tài liệu.

**2. Mục tiêu** — SRS không nêu KPI riêng cho Action. → OQ-EA-01.

**3. Người dùng** — Admissions / Customer Service (ghi Call, follow-up Journey, quản lý Visit, Waitlist), Centre Director, System (áp status, notification, audit) (nguồn: CRM SRS §2).

**4. Phạm vi**

| In scope (Phase 1) | Ngoài phạm vi | Sprint 3 / FRD khác |
|---|---|---|
| 2.3.1.01 Action framework · 2.3.1.02 Mark visited · 2.3.1.03 Log no-show · 2.3.1.04 Parent is considering · 2.3.1.05 Log follow-up · 2.3.1.09 Hold the space · Update Enquiry status (§4 mục 3.2, WBS Phase 1) · 2.3.2.03 Journey assignment resolution · 2.3.2.05 Event-key engine · 2.3.2.07 Task assignment resolution · 2.3.2.08 Automated messages | 2.3.1.06–07 Schedule for later, Transfer Centre; 2.3.2.01–02, .04, .06 Journey/Task checklist, Change Journey, Add manual Task, Task SLA (Phase 2, §1.2); View Enquiry Journey runtime / Tasks (Phase 2, §4 mục 3.2); SLA clock (BBA-43 FR-021) | Hiển thị Actions & SLA (BBA-43 US-003); Timeline (BBA-44); Visit booking, attendance (nhóm 2.4); Waitlist (nhóm 2.5); cấu hình Journey Template (FRD 2.8) |

**5. Quy trình (TO-BE theo SRS)**
1. Enquiry được gán Journey có phiên bản (Stages, Tasks) và owner (nguồn: P2 bước 7, P4 bước 10).
2. Người dùng thực hiện Action được phép theo Status, quyền và ràng buộc (nguồn: BBA-43 BR-010).
3. Action có thể đổi Status; đổi Status không sửa Journey đã lưu (nguồn: BR-CRM-021).
4. Sự kiện cấu hình hoàn tất Task tự động, không tính hai lần (nguồn: P4 bước 11, BR-CRM-019, 020, AC-CRM-004).
5. Parent is considering đề xuất ngày hành động kế tiếp = thời điểm thực hiện + 48 giờ liên tục, người dùng sửa được; không giữ chỗ (nguồn: BR-CRM-037, 038, AC-CRM-012, P6 bước 15).
- **Chưa biết:** Status đích của từng Action (OQ-EA-02); nội dung Mark visited, Log no-show, Hold the space (OQ-EA-03..05); quy tắc chọn Journey và người nhận Task (OQ-EA-06, 07); nội dung Automated messages (OQ-EA-08).

**6. Dữ liệu** — Status catalogue Phase 1 có 16 giá trị (nguồn: BBA-43 §7.1). Notification "New assigned work", "Journey Task due" (nguồn: CRM SRS §6.1). Audit: tác nhân, thời điểm, trước/sau (nguồn: BR-CRM-022).

**7. Rủi ro** — SRS chỉ có tên WBS cho Mark visited, Log no-show, Log follow-up, Hold the space, Automated messages → FRD để nhiều OQ; rủi ro dev tự hiểu khác nhau. Giảm thiểu: chốt OQ-EA-02..08 trước khi dev.

| Mã | Nội dung | Loại |
|---|---|---|
| AS-EA-01 | Mark visited → status `visited`; Parent is considering → `considering`; Log follow-up → `follow_up` (suy từ ý nghĩa status ở BBA-43 §7.1). | AS → OQ-EA-02 |
| OQ-EA-01 | Có chỉ số đo hiệu quả Action (vd. thời gian phản hồi) cho Sprint 4 không? | OQ |
| OQ-EA-02 | Bảng chuyển trạng thái chính thức: Action nào được phép ở Status nào, đổi sang Status nào (BBA-55). | OQ |
| OQ-EA-03 | Mark visited: có cập nhật Visit sang Held không, hay chỉ đổi Status Enquiry? Áp dụng khi chưa có Visit? | OQ |
| OQ-EA-04 | Log no-show: Status Enquiry sau no-show (catalogue không có status no-show); có bắt buộc Rebook không? | OQ |
| OQ-EA-05 | Hold the space: nghĩa nghiệp vụ, có giảm chỗ trống không, thời hạn giữ, cần đặt cọc không, ai được dùng. | OQ |
| OQ-EA-06 | Quy tắc chọn Journey Template cho Enquiry (theo Country, Brand, Centre, Level…?) và khi không tìm được. | OQ |
| OQ-EA-07 | Quy tắc chọn người nhận Task (owner Enquiry, vai trò, Centre?). | OQ |
| OQ-EA-08 | Automated messages: kênh (email, SMS, Zalo…), mẫu nội dung, sự kiện kích hoạt, người nhận. | OQ |
| OQ-EA-09 | Log follow-up: trường bắt buộc (ngày hành động kế tiếp, ghi chú, kênh liên hệ). | OQ |

---

## 2.8 CRM Administration — Approvals (BBA-49 đến BBA-53), đối chiếu prototype

> Phạm vi 2.8 do user chốt lại ngày 09/11/2026: **Approvals (Administration)**, 5 ticket BBA-49 đến BBA-53 (nội dung Journey Settings / Visit Slot Schedule của bản 0.1 đã bỏ).
> Nguồn: SRS SMS Administration v0.1 (§3 P4, P5; §4 mục 2.3, 2.4, 4.1, 4.2; BR-ADM-016 đến 023, 036, 037, 042), SRS SMS General Requirements v0.1 (§3.1, §3.3, §4.4) và **prototype** mà SRS ADM §1 dẫn chiếu ("Read it together with the prototype").
> Prototype khảo sát ngày 10/11/2026, đăng nhập demo HQ Admin "Daniel Yeo": `/organisation/approvals`, `/organisation/delegations`, `/approvals`, `/approvals/<id>`, `/organisation/features`, `/organisation` (Roles), `/history`. Dữ liệu là dữ liệu demo; prototype chỉ thể hiện ý đồ màn hình, quy tắc vẫn lấy SRS làm chuẩn. Prototype khác SRS → ghi OQ, không tự chọn.

**1. Bối cảnh** — Mọi yêu cầu cần duyệt đi qua một hộp duyệt; người duyệt chỉ đặt trong Approval routes (SRS GEN §3.3; BR-ADM-018). Prototype: menu chính có **My approvals** (badge số yêu cầu chờ, demo 26) tách khỏi Administration; Approval routes, Extra permissions nằm trong **Users & permissions** (tab Users, Roles, Extra permissions, Approval routes, Sign-in & security); Settings là menu riêng.

**2. Mục tiêu** — SRS không nêu KPI → giữ OQ-ADM-13 (mới).

**3. Người dùng** — HQ Admin (mọi quyền, BR-ADM-001; prototype: HQ Admin giao được extra permission cho bất kỳ ai trong 53 nhân viên và quyết định thay vai trò khác), Centre Director (giao extra permission, duyệt yêu cầu Centre), Finance, District Manager, Operations Manager, Head of Brand (người duyệt route). Danh sách vai trò duyệt trong form route: Centre Director, District Manager, Operations Manager, Head of Brand, Finance, HQ Admin (prototype). Roles demo ghi "Sample roles · ⚠ final list to confirm with BBA".

**4. Đối chiếu prototype ↔ FRD 2.8 v0.2**

| US / ticket | Prototype thể hiện | FRD v0.2 đang viết | Kết luận |
|---|---|---|---|
| US-001 BBA-49 Ma trận | Bảng 21 route: Request type, Country, Brand, Level 1 approver, Level 2 approver, Amount threshold, Edit. Lọc Request type / Country / Brand, Search, Export (21). Dấu "⚠ To confirm with BBA" trên route chưa chốt; nhãn "· can be delegated" ở cấp 1 của Attendance void, Child leave, Authorised pickup, Photos, Progress report. **History chung cuối trang**: "thời điểm · người · loại: cấp 1 → cấp 2 cũ → cấp 1 → cấp 2 mới". Nút **Add route**. | Cột "Last changed"; History từng dòng; không có dấu To confirm, không có nhãn can be delegated; không có Add route. | Sửa: bỏ cột Last changed, History chung theo màn (vẫn lọc theo route được); thêm dấu To confirm, nhãn can be delegated. Add route chuyển sang US-005. |
| US-005 BBA-53 Cấu hình | Dialog Add / Edit route: Request type, Country (All / Singapore / Malaysia), Brand (All brands + 7 brand) **đều sửa được**; Level 1 approver; Level 2 approver có lựa chọn "None — one level"; trường **"Level 2 only above this amount"** chỉ hiện khi đã chọn cấp 2, để trống = "Always both levels". Lưu là có hiệu lực ngay, ghi History; không duyệt lần hai. Prototype cho lưu cấp 1 = cấp 2 cùng vai trò (Discount CD → CD) không báo lỗi. 17 loại yêu cầu (có Portfolio). | Loại / quốc gia / brand chỉ đọc; toggle "Cần duyệt cấp 2"; VAL-009 báo lỗi ngưỡng khi chưa bật cấp 2; có Load default routes. | Sửa field spec theo dialog; ngưỡng ẩn khi cấp 2 = None (VAL-009 chỉ còn "số dương"); thêm Add route + kiểm tra trùng tổ hợp (AS); giữ Load default routes (SRS §4 mục 2.4). Cấp 1 = cấp 2 cùng vai trò → OQ (Transfer DM → DM là hợp lệ vì hai Centre). |
| US-005 route mặc định | Khác SRS ở 6 dòng: "Withdrawal · not at month end" chỉ DM 1 cấp (SRS: CD rồi DM/OM); Retention fee waiver MY: CD → OM **2 cấp** (SRS: 3 cấp); Credit note, Refund: Finance → HQ Admin, ngưỡng 1.000 (SRS: Finance, không ngưỡng); Notice period waiver ⚠; Temporary withdrawal SG ⚠. | Phụ lục A theo SRS. | Phụ lục A thêm cột "Prototype" và "Khác biệt"; OQ-ADM-01 cập nhật; thêm OQ-ADM-14. |
| US-002 BBA-50 Uỷ quyền | Màn "Extra permissions — Permissions given to one person on top of their role": Person, Permission, Granted by, From, Until ("No end date"), Status (Active / Revoked), Revoke; lọc Permission, Status; Export. Dialog **Grant**: Person, Permission, Reason, Until (optional), checkbox **"I confirm this person should hold it"**. Danh mục 6 quyền: Approve leave requests, Review class update photos, Void or delete attendance records, Assign teachers to a class, Move a class's children up, Manage users of their own centre. Revoke có hộp xác nhận "… loses it now and is told in the app". History: "Granted via Centre Director app", lý do "Covers leave approvals on the Centre Director's off days". | Có đủ grant / revoke / expire; thiếu checkbox xác nhận, hộp xác nhận Revoke, danh mục quyền, liên kết với route "can be delegated", HQ Admin cũng giao được. | Sửa: thêm danh mục quyền, checkbox, hộp xác nhận, liên kết route can be delegated ↔ quyền duyệt; HQ Admin giao mọi Centre (BR-ADM-001). Authorised pickup và Progress report được đánh "can be delegated" nhưng không có quyền tương ứng → OQ-ADM-15. OQ-ADM-03 thu hẹp: uỷ quyền = extra permission, không có uỷ quyền cả hộp duyệt trong prototype. |
| US-003 BBA-51 Tác động | Settings: danh sách thiết lập theo nhóm FEES, JOINING & LEAVING, DAILY OPERATIONS, LEARNING, COMMUNICATION; "⚠" + bộ lọc "Not yet confirmed"; mỗi thiết lập có đơn vị, "Set at: Group · default 5" (các cấp được đặt), "Mark as confirmed by BBA", Change. Bảng "Value at every centre": Centre, Value, Comes from, Set by, Override. Lọc Country / Brand / Cluster / Differs from default. Dialog **Change**: Applies to (cấp), Value, **See the impact** → "15 centres affected" + danh sách "Centre: 5 → 10 … and 7 more", Confirm. Tab **Feature switches**: mỗi tính năng bật / tắt theo brand ("Whole brand", "3 of 4 on") và từng Centre, mô tả "Off hides: …". | Tác động = số trẻ, hoá đơn, yêu cầu chờ (theo SRS); không có danh sách Centre đổi giá trị; phạm vi chưa có cấp "Group"; chưa có "Set at", "Off hides". | Sửa: tác động gồm **danh sách Centre đổi giá trị (cũ → mới)** (prototype) **và** số trẻ, hoá đơn, yêu cầu chờ (SRS BR-ADM-037) → OQ-ADM-07 cập nhật; thêm "Set at", cấp Group, "Off hides", bật theo brand / Centre. |
| US-004 BBA-52 Duyệt 2 cấp | **My approvals**: tab Waiting / Done; lọc Centre, Type, Requested by, Submitted (Done thêm Status); cột Request (loại + số), Record (đối tượng + Centre), **What happens next** (câu hậu quả "Once you approve, …"), Requested by, Submitted, Status, Decide. Trang chi tiết: badge **"Level 1 of 2"**, Request, **What approving changes**, **Rule warnings**, Supporting documents (Verified / Pending review), Approval history, Your decision (Comment, Reason required to reject, Approve, Reject). Duyệt cấp 1 → "Level 2 of 2"; history ghi "Approved · Level 1 of 2 · Centre Director · Daniel Yeo · HQ Admin" + "This decision belongs to the Centre Director · group. Approval routes · Discount." Sau khi Daniel Yeo duyệt cấp 1, trang **không còn Your decision** cho cấp 2 của chính người đó. Change log ghi "Workflow step · Pending · level 1 of 2 → Pending · level 2 of 2". Done: Approved / **Declined**, "Outcome", "Reason given". Ghi chú: hồ sơ chiều cao cân nặng, routine, cập nhật hồ sơ không cần duyệt; class update của Teacher chờ duyệt, của CD / HQ Admin đi thẳng. Duyệt tại cửa (pickup, leave, refused collections) ở màn riêng `/operations/approvals`. Ví dụ "change request": **Discount "Open house September — 15%"** (định nghĩa giảm giá cấp group do Finance gửi) đi 2 cấp. | Inbox nằm trong Administration; panel chi tiết bên phải; tab Waiting for me / All requests; cột Amount, Level; chưa có What happens next, What approving changes, Rule warnings, Comment; chưa có quy tắc một người không duyệt hai cấp; chưa có HQ Admin quyết thay. | Sửa: theo màn My approvals + trang chi tiết; thêm quy tắc người đã duyệt cấp 1 không duyệt cấp 2 (theo prototype → xác nhận OQ-ADM-09); HQ Admin quyết thay vai trò, history ghi vai trò sở hữu và route; trạng thái Declined; duyệt tại cửa ngoài phạm vi. OQ-ADM-05 bổ sung ví dụ thay đổi định nghĩa giảm giá. |

**5. Quy trình TO-BE (đã chỉnh theo prototype)**
1. HQ Admin xem ma trận route, lọc, xuất; route chưa chốt có dấu ⚠ (US-001).
2. HQ Admin thêm / sửa route trong dialog; lưu có hiệu lực ngay cho yêu cầu mới, ghi History (US-005).
3. Centre Director (hoặc HQ Admin) giao extra permission có lý do, xác nhận, hạn tuỳ chọn; người nhận dùng quyền ngay, thấy yêu cầu tương ứng trong My approvals (US-002).
4. Người dùng đổi thiết lập: chọn cấp áp dụng, giá trị → See the impact → Confirm (US-003).
5. Người yêu cầu gửi → My approvals của người duyệt cấp 1 → (cấp 2 khi route có cấp 2 và vượt ngưỡng) → Approved / Declined; mỗi bước ghi Approval history và change log (US-004).

**6. Dữ liệu** — Route (loại, quốc gia, brand, cấp 1, cấp 2, ngưỡng, trạng thái xác nhận, cho phép uỷ quyền); Extra permission (người, quyền, người giao, lý do, từ, đến, trạng thái, kênh giao: CRM / Centre Director app); Setting value (thiết lập, cấp, giá trị, nguồn, người đặt, thời điểm, đã xác nhận); Approval request + step (cấp x / y, vai trò sở hữu, người quyết, comment, lý do, route áp dụng).

**7. Rủi ro** — Prototype và SRS khác nhau ở route mặc định (6 dòng) và nội dung tác động → nếu không chốt, đội dev làm theo prototype sai SRS. Giảm thiểu: Phụ lục A ghi cả hai, OQ-ADM-01, OQ-ADM-07, OQ-ADM-14 mức Cao.

**Đề xuất của BA (chưa phải yêu cầu)** — Chặn lưu route có cấp 1 = cấp 2 cùng vai trò trừ loại yêu cầu liên quan hai Centre (Transfer); hiển thị trên dòng route số yêu cầu đang chờ khi sửa.

| Mã | Nội dung | Loại | Liên quan |
|---|---|---|---|
| AS-ADM-08 | Không lưu hai route trùng tổ hợp loại yêu cầu + quốc gia + brand; Add route với tổ hợp đã có báo lỗi. (Prototype không báo lỗi rõ.) | AS → OQ-ADM-16 | US-005 |
| AS-ADM-09 | Route "can be delegated" là route có quyền duyệt tương ứng trong danh mục extra permission (Approve leave requests ↔ Child leave, Review class update photos ↔ Photos, Void or delete attendance records ↔ Attendance void). | AS → OQ-ADM-15 | US-001, US-002 |
| OQ-ADM-13 | Chỉ số thành công cho Approvals ở Sprint 4? | OQ | chung |
| OQ-ADM-14 | Route mặc định theo SRS hay theo prototype ở 6 dòng khác nhau (Phụ lục A)? | OQ | US-005 |
| OQ-ADM-15 | Authorised pickup, Progress report có nhãn "can be delegated" nhưng không có quyền tương ứng trong danh mục extra permission: thêm quyền hay bỏ nhãn? | OQ | US-001, US-002 |
| OQ-ADM-16 | Add route trùng tổ hợp đã có: báo lỗi hay ghi đè route cũ? | OQ | US-005 |
| OQ-ADM-17 | Cho phép route có cấp 1 và cấp 2 cùng vai trò không (ngoài Transfer)? | OQ | US-005 |

---

## Quy tắc chung SMS (áp cho 3.1, 3.2, 3.6) — nguồn: SRS SMS General Requirements v0.1

- Phase 1 phục vụ Singapore và Malaysia; Vietnam không thuộc Phase 1 (§2.2). Tổ chức Country → Brand → Cluster → Centre (§2.2).
- SMS bắt đầu khi gia đình đóng booking fee; trước đó thuộc Enquiries (CRM) (§2.3).
- Quyền 3 lớp: area permission, special permission, protected field; data scope; điều không được làm thì không hiển thị (§3.1). Phê duyệt qua Approvals inbox, tối đa 2 cấp, Approval routes; từ chối bắt buộc lý do (§3.3).
- Danh sách chuẩn, bản ghi không xoá, History chỉ thêm, dữ liệu có "một nơi quản lý", thiết lập kế thừa theo cấp (§4). Không gửi SMS text / email digest ở Phase 1 (BR-GEN-014).

## 3.1 Children & families — nguồn: SRS SMS Children & Families v0.1

- **Đã biết:** đủ 6 phân hệ (Children, Families & guardians, Health & allergies, Documents, Authorised pickup, Classes), quy trình P1–P7, BR-CHF-001–050, 20 AC (nguồn: SRS C&F §1–§8). Phạm vi Phase 1 và loại trừ rõ ở §1.1, §1.2.
- **Mâu thuẫn:** lời mời Parents App gửi qua SMS (BR-CHF-019) ↔ Phase 1 không gửi SMS (BR-GEN-014) → OQ-CF-06. Tên vai trò "School Admin", "HQ Enrolment" (C&F) ↔ "Centre Admin" (General §3.2) → OQ-CF-01.
- **Chưa biết:** người duyệt change record (OQ-CF-02); trường bắt buộc sức khoẻ / người giám hộ / lớp (OQ-CF-03); chuẩn biểu đồ (OQ-CF-04); lịch tiêm chủng (OQ-CF-05); danh mục giấy tờ (OQ-CF-07); cơ chế lên playgroup 18 tháng và đề xuất lớp đích (OQ-CF-08, 09); trẻ chưa sinh khi sinh (OQ-CF-10); điều khoản người đón (OQ-CF-11).
- **Kết quả:** FRD `3.1_Children_and_Families_VI.md` — 10 US, 66 FR, 60 AC, 12 OQ.

## 3.2 Daily operations — nguồn: SRS SMS Daily Operations v0.1

- **Đã biết:** 5 nhóm (Attendance: trẻ, nhân viên, khách; Daily care: hoạt động, đơn nghỉ; Calendar và diễn tập; Safety: centre log, tổng quan an toàn; Bus services), quy trình P1–P7, BR-OPS-001–051, 13 notification, 13 báo cáo, 20 AC (nguồn: SRS OPS §1–§8). Phạm vi loại trừ rõ ở §1.2 (16 mục).
- **Chưa rõ:** vai trò "Centre Admin / School Admin" (OQ-OPS-01); Present vs Signed in (OQ-OPS-02); nhiệt kế Bluetooth (OQ-OPS-03); xung đột offline (OQ-OPS-04); e-Form 1 (OQ-OPS-05); người đưa trẻ có cần trong danh sách đón (OQ-OPS-06); khách sốt (OQ-OPS-12); huỷ đơn nghỉ (OQ-OPS-13).
- **Kết quả:** FRD `3.2_Daily_Operations_VI.md` — 14 US, 69 FR, 74 AC, 14 OQ.

## 3.6 Finance — nguồn: SRS SMS Fees & Payments v0.1

- **Đã biết:** SRS ghi mục tiêu "bill, collect, refund and close each month without Taidii" (§1) — khớp tên "Finance (rebuilt to Tai[dii])". 8 nhóm (Overview, Fee set-up, Billing, Payments & receipts, Deposits & refunds, GSII, Approvals, Reports & month-end), quy trình P1–P7, BR-FEE-001–053, 12 notification, 11 báo cáo, 20 AC (nguồn: SRS FEE §1–§8).
- **Mâu thuẫn / chưa rõ:** thời điểm tạo hoá đơn đầu tiên — "registration submitted" (BR-FEE-020) ↔ "enrolment confirmed" (P1) → OQ-FIN-02; Malaysia billing để sprint planning → OQ-FIN-01; định dạng file ngân hàng, cách nhận tiền PayNow, nguồn dòng trợ cấp → OQ-FIN-03, 04, 06.
- **Kết quả:** FRD `3.6_Finance_VI.md` — 22 US, 97 FR, 107 AC, 15 OQ.

## Tổng kết 5 FRD (bản tiếng Việt v0.1)

| FRD | US | FR | AC | OQ | AS |
|---|---|---|---|---|---|
| 2.3 Enquiry Actions | 10 | 32 | 40 | 10 | 4 |
| 2.8 CRM Administration (v0.4 — chỉ BBA-49) | 1 | 8 | 9 | 5 | 2 |
| 2.8 Approval Delegation (BBA-50, tách 10/11/2026) | 1 | 8 | 9 | 2 | 3 |
| 2.8 Impact Preview Before Change (BBA-51) | 1 | 10 | 10 | 2 | 0 |
| 2.8 Change Request with Second Approval (BBA-52) | 1 | 10 | 10 | 2 | 2 |
| 2.8 Approval Flows Configuration (BBA-53) | 1 | 5 | 7 | 7 | 3 |
| 3.1 Child Record Overview (v0.1, thêm 10/11/2026) | 6 | 35 | 38 | 13 | 9 |
| 3.1 Child Record Tabs – Read Views (v0.2, 10/11/2026) | 6 | 45 | 55 | 11 | 7 |
| 3.1 Children and Families | 10 | 66 | 60 | 12 | 2 |
| 3.2 Daily Operations | 14 | 69 | 74 | 14 | 7 |
| 3.6 Finance | 22 | 97 | 107 | 15 | 6 |

---

## 3.1 Child record — Overview (header + tab Overview), đối chiếu prototype

> Yêu cầu khách (10/11/2026): "Header and Overview tab of the child record: status, centre/class/owner, day-to-day name vs IC-registered name (used on invoices), DOB/age, gender, nationality (passport) vs citizenship (decides fee & subsidy), race, payment method (GIRO/PayNow…), masked ID, photo, class card with homeroom teacher, medical alert summary, Actions menu". Khách muốn làm rõ thông tin các tab và hỏi có cần thêm trường nào.
> Nguồn: SRS SMS Children & Families v0.1 (§1, §2, §3 P1, §4 mục 1.1, BR-CHF-001 đến 013, 017, 024, 025); SRS General (§3.1 quyền 3 lớp, §4 Personal data); SRS Administration (protected fields, BR-ADM-038); SRS Fees & Payments (BR-FEE-013, 037, 038; §4.1 GIRO accounts); SRS Joining & Leaving §1.2. Prototype `/records/child/<id>` khảo sát 10/11/2026 với vai trò HQ Admin, School Admin, Teacher (dữ liệu demo).
> Phạm vi FRD: **chỉ header và tab Overview**. Các tab khác chỉ lập danh mục để làm rõ, chi tiết thuộc FRD 3.1 Children & Families và FRD module sở hữu.

**1. Bối cảnh** — Mỗi trẻ có một hồ sơ chính xác thay Taidii và giấy tờ (SRS C&F §1). Hồ sơ mở từ danh sách Children (SRS §4 mục 1.1 View child profile). Prototype đặt phần "Identity" ở tab Overview với ghi chú giải thích: tên trên IC dùng cho hoá đơn, biên lai; citizenship quyết định học phí và trợ cấp, nationality là quốc gia trên hộ chiếu và không quyết định.

**2. Mục tiêu** — SRS không nêu KPI → OQ-OVW-01.

**3. Người dùng**

| Vai trò | Trên Overview | Nguồn |
|---|---|---|
| HQ Admin | Xem mọi Centre, sửa Identity; NRIC hiện đầy đủ (prototype). | BR-CHF-011; Prototype |
| HQ Enrolment | Xem, sửa hồ sơ trẻ mọi Centre. | SRS C&F §2 |
| Centre Director, School Admin | Xem, sửa hồ sơ trẻ của Centre; School Admin thấy NRIC dạng "••••••" (prototype). | SRS C&F §2; BR-CHF-012; Prototype |
| Teacher | Xem trẻ lớp mình; dòng NRIC bị ẩn (prototype). | BR-CHF-013; Prototype |
| HQ Finance | Xem trẻ, dùng billing contact. | SRS C&F §2 |

**4. Đối chiếu yêu cầu khách ↔ SRS ↔ prototype**

| Thông tin khách nêu | SRS C&F | Prototype | Ghi chú / OQ |
|---|---|---|---|
| Status | Enrolled / Temporary withdrawal / Withdrawn / Graduated; chỉ đổi qua Joining & leaving (BR-CHF-006). | Badge "Active"; dải "Enrolment: Active · latest change: Withdrawal submitted 2026-09-30 · Open the case". | Nhãn "Active" ≠ "Enrolled" → OQ-OVW-02. |
| Centre / class / owner | Centre, class, level (list). Không có "owner". | "Small Wonder Tampines · Sunbeams · Owner · Serena Lim" (owner là một guardian). | Owner = primary contact? → AS-OVW-01, OQ-OVW-03. |
| Day-to-day name vs IC-registered name | "name on IC" chỉ ở Search; Create cần "full name". | "Name used day to day" và "IC-registered name — The name used on invoices and receipts." | IC name dùng cho hoá đơn: prototype → OQ-OVW-04 (bắt buộc khi nào). |
| DOB / age | DOB bắt buộc khi tạo (BR-CHF-001); trẻ chưa sinh dùng expected birth date (BR-CHF-002). | "2022-02-14 · 4 years (4y 8m)". | Hiển thị trẻ chưa sinh → AS-OVW-02. |
| Gender | Bắt buộc khi tạo (BR-CHF-001). | Female / Male. | — |
| Nationality vs citizenship | Không có trong C&F. Fees: giá theo citizenship (BR-FEE-013). J&L: "nationality changes" không thuộc Phase 1. | Nationality text tự do; Citizenship: Singapore Citizen / Singapore PR / Foreigner. Trẻ Malaysia ở Centre Malaysia đang là "Foreigner". | Giá trị citizenship cho Malaysia → OQ-OVW-05; đổi nationality trong Phase 1 → OQ-OVW-06. |
| Race | Không có. | Hiển thị; không có trong form Edit identity. | Danh mục và nơi sửa → OQ-OVW-07. |
| Payment method | Fees: GIRO / CDA account ("Pays by GIRO"), PayNow, manual (bank transfer, AXS, cheque); GIRO, CDA chỉ Singapore, DuitNow chỉ Malaysia (BR-ADM-038, BR-FEE-037, 038). | "GIRO" / "CDA" — "Carried on every invoice for this child."; không có trong form Edit; tab Finance có "How this family pays". Trẻ Centre Malaysia đang có CDA, GIRO. | Nguồn giá trị và danh mục theo quốc gia → AS-OVW-03, OQ-OVW-08. |
| Masked ID | NRIC ẩn với vai trò không được xem (BR-CHF-009); protected field Hidden / Masked / Read / Edit; truy cập được ghi log (GEN). | HQ Admin: full; School Admin: "••••••", History ghi "Masked → Full number shown once"; Teacher: ẩn dòng. Nhãn "NRIC / identity document number". | Loại giấy tờ (NRIC / FIN / passport / birth cert) → OQ-OVW-09. |
| Photo | "Upload child photo — a new photo replaces the old one." | "PHOTO · Not uploaded"; header dùng avatar chữ cái. | Không thấy nút upload ở prototype → FR theo SRS. |
| Class card + homeroom teacher | Assign / change class có effective date; class có teachers. | "N2 · Sunbeams · 2 of 20 enrolled · Homeroom · Aisyah Rahman"; ghi chú "Change class applies to infants only. A whole class moves up a level from the class itself." | SRS cho Change class mọi trẻ ↔ prototype chỉ infant → OQ-OVW-10. |
| Medical alert summary | Icon cảnh báo khi có dị ứng / bệnh (BR-CHF-024); chi tiết chỉ cho vai trò được phép, mặc định CD, Teacher, School Admin, HQ Admin (BR-CHF-025). | Ô đỏ ở header nối mọi tình trạng; thẻ Overview "Allergies: …" + "The full record is under Health."; trẻ không có thì không có ô. | Vai trò khác chỉ thấy icon (BR-CHF-025). |
| Actions menu | Profile có: Send message to parents, Assign / Change class, Upload photo (SRS §4 mục 1.1). | "Link a guardian", "Open the family". "Start a case" (withdrawal, temporary withdrawal, transfer) nằm ở tab Enrolment. | Danh sách cuối → OQ-OVW-11. |

**5. Danh mục tab: SRS ↔ prototype** (để khách làm rõ)

| SRS (View child profile) | Prototype | Ghi chú |
|---|---|---|
| Overview | Overview | FRD này. |
| Family | Guardians | Guardian, primary / emergency / billing contact, authorised to collect, siblings. |
| Pickup | (trong Guardians) | Authorised pickup nằm trong tab Guardians. |
| Health | Health | Thông tin từ gia đình, note của staff, tệp, tiêm chủng, nhiệt độ. |
| Documents | Documents | Giấy tờ + consents. |
| Consents (read-only) | (trong Documents) | — |
| Billing (read-only) | Finance | Việc cần làm, flags, trợ cấp, Bill to, GIRO / CDA, payment method. |
| Class history | — | Không có tab riêng → OQ-OVW-12. |
| — | Enrolment | Flags (SUG, Staff, KA child), start a case, enrolment hiện tại. |
| — | Enrichment | Chương trình enrichment. |
| — | Attendance | Xe buýt, số ngày đi học, nhiệt độ. |
| — | Communication | Hội thoại như phụ huynh thấy. |
| — | History | Change record và log xem dữ liệu được che. |

**6. Dữ liệu** — Child: student ID, name, IC-registered name, DOB / expected birth date, gender, nationality, citizenship, race, identity document number (protected), photo, status (từ J&L), centre, level, class, start date; primary contact (owner), billing contact; payment method (từ Finance); medical alert (từ Health). Edit identity tạo change record: effective date, approved by, attachment (BR-CHF-005; prototype).

**7. Rủi ro** — Citizenship sai làm sai giá học phí và trợ cấp (BR-FEE-013) → đổi citizenship phải có effective date và lưu vết; prototype dùng danh mục citizenship của Singapore cho trẻ Malaysia → OQ mức Cao. Payment method CDA ở Centre Malaysia trái BR-ADM-038 → kiểm tra theo quốc gia.

**Đề xuất của BA — trường có thể bổ sung (chưa phải yêu cầu, chờ khách chọn)**
- Start date và Programme (Full day / Half day) trên Overview: giá học phí theo programme + citizenship (BR-FEE-013); start date là trường bắt buộc khi tạo (BR-CHF-001).
- Loại giấy tờ định danh (NRIC / FIN / Passport / Birth certificate) đi kèm số.
- Billing contact cạnh Payment method (BR-CHF-017).
- Expected birth date + nhãn "Unborn" cho trẻ chưa sinh (BR-CHF-002).
- Ngày hiệu lực của citizenship hiện tại (đọc từ change record).

| Mã | Nội dung | Loại | Liên quan |
|---|---|---|---|
| AS-OVW-01 | "Owner" là primary contact của trẻ (BR-CHF-017). | AS → OQ-OVW-03 | US-001 |
| AS-OVW-02 | Trẻ chưa sinh hiện "Expected birth date" thay DOB, tuổi để trống. | AS → OQ-OVW-13 | US-002 |
| AS-OVW-03 | Payment method chỉ đọc trên Overview, lấy từ Finance: GIRO / CDA khi có tài khoản Active và "Pays by GIRO = Yes"; còn lại PayNow (Singapore) hoặc theo phương thức Malaysia. | AS → OQ-OVW-08 | US-002 |
| OQ-OVW-01 → 13 | Xem FRD 3.1 Child Record Overview mục 7. | OQ | — |

## BBA-69 đến BBA-97 — brainstorm nghiệp vụ (10/11/2026)

> Nguồn đã đọc: mô tả ticket trên Plane (BBA Phase 1, WBS P1 · bba-sprint-plan-v7; Sprint S4, 23/11 → 04/12/2026); SRS SMS Children & Families, Communication, Daily Operations, Fees & Payments, Administration, General Requirements v0.1; issue #526 "BBA input: Per-child subsidy list sample" (BBA chưa gửi file mẫu). Mục này là ghi chú nội bộ; FRD không ghi đối chiếu nguồn.
> Quy tắc đợt này: không bịa; thiếu thông tin → AS + OQ; tên file và tên Word ghi mã ticket BBA-xx; không làm wireframe (user không yêu cầu đợt này); mỗi ticket một FRD.

### 1. Bối cảnh, mục tiêu, người dùng (chung)
- BBA thay Taidii bằng SMS; nhóm Finance (3.6) ghi rõ "rebuilt to Taidii parity" → các màn cài đặt tài chính phải làm được việc Finance đang làm trên Taidii.
- Người dùng: Centre Director, Centre Admin / School Admin, Teacher, Senior Teacher, HQ Admin, HQ Finance, District Manager / Operations Manager, HQ Safeguarding, bếp (dùng danh sách dị ứng in ra), phụ huynh (xem kết quả trên Parents App).
- Mỗi ticket BA có cùng việc: "quy tắc, trường hợp đặc biệt và tiêu chí nghiệm thu, chốt với vận hành Centre (CD / HQ ops)" cho 3.1, 3.2; "chốt với BBA Finance" cho 3.6.

### 2. Đánh giá từng ticket — nghiệp vụ có hợp lệ không

| Ticket | Đã biết | Đánh giá nghiệp vụ | Giả định / Câu hỏi mở chính |
|---|---|---|---|
| BBA-69 Allergies list | Danh sách theo Centre / lớp, trẻ nặng nhất lên đầu; cột trẻ, lớp, chất gây dị ứng, phản ứng, cách xử trí, nơi để EpiPen; bếp và giáo viên dùng; lọc lớp / Centre. Mức độ Mild / Moderate / Severe; in và xuất cho bếp; ẩn chi tiết theo vai trò. | Hợp lệ. Điểm vướng: phản ứng, cách xử trí, nơi để EpiPen hiện không có trường riêng — phụ huynh chỉ ghi chữ tự do. Danh sách cho bếp in ra giấy → phải có ngày in để bếp biết bản nào mới nhất. | OQ: thêm trường riêng (phản ứng, cách xử trí, nơi để thuốc khẩn cấp) hay chỉ hiển thị chữ phụ huynh ghi; ai ghi nơi để EpiPen (phụ huynh hay Centre). AS: dùng cùng quy tắc mức cảnh báo của BBA-68. |
| BBA-70 Growth | Màn nhập theo lớp mỗi kỳ: chiều cao, cân nặng, ngày đo; tính BMI / percentile; không duyệt; phụ huynh xem; HQ có báo cáo theo dõi. Nhập cho trẻ có mặt; lưu một lần. | Hợp lệ. Cần mốc kỳ đo (term) và chuẩn percentile — chưa biết. Cần chặn số liệu vô lý (gõ nhầm cm ↔ m). | OQ: lịch các kỳ đo; chuẩn biểu đồ tăng trưởng; giới hạn hợp lệ; nội dung báo cáo HQ. AS: chiều cao cm (1 số lẻ), cân nặng kg (1 số lẻ). |
| BBA-71 Consent status | Mỗi trẻ: các loại consent với trạng thái (chưa gửi / đã gửi, chờ / đồng ý / không đồng ý / hết hạn) và phiên bản; gửi / gửi lại cho phụ huynh qua app / email; số lần nhắc; ngày và kênh trả lời. Consent có thể rút lại nếu biểu mẫu cho phép; nhắc tự động 1 ngày trước hạn. | Hợp lệ. Cần làm rõ "phiên bản": khi nội dung consent đổi, câu trả lời cũ áp cho phiên bản cũ. Trạng thái "Đã rút lại" có trong quy tắc rút consent nhưng ticket không liệt kê. | AS: thêm trạng thái Withdrawn. OQ: danh sách loại consent (media / PDPA, field trip…); thời hạn hiệu lực; số lần gửi lại tối đa; email gửi cho phụ huynh không có app. |
| BBA-72 Bulk promotion | Hằng năm: chọn lớp, lớp / level đích, ngày hiệu lực, xem trước, xác nhận; cập nhật ghi danh, biểu phí theo level, danh sách điểm danh; lịch sử từng trẻ. Trẻ ở lại lớp được bỏ chọn; lớp cũ đóng được. | Hợp lệ. Rủi ro: lên lớp làm đổi học phí → phải chạy trước kỳ tạo hoá đơn của tháng hiệu lực; lớp đích vượt sĩ số chỉ cảnh báo. | OQ: lên lớp có cần duyệt không; K2 tốt nghiệp xử lý ở đâu. AS: ngày hiệu lực mặc định đầu năm học mới. |
| BBA-73 Handover | Khi nhận / trả trẻ ghi người đưa / người đón (phụ huynh, người được uỷ quyền, hoặc "Other" kèm ghi chú) và giờ; cảnh báo nếu người đón không có trong danh sách. Quy tắc an toàn: chỉ trả trẻ cho người trong danh sách đón đã duyệt. | **Có mâu thuẫn an toàn**: ticket cho phép trả trẻ với cảnh báo, quy tắc an toàn chỉ cho trả trẻ cho người trong danh sách. Đề xuất BA: buổi sáng cho "Other" kèm ghi chú; buổi chiều chặn người ngoài danh sách. | OQ (ưu tiên cao): có cho Centre Director trả trẻ cho người ngoài danh sách sau khi gọi xác nhận phụ huynh không. |
| BBA-74 Temperature | Đo kèm giờ và thời điểm (khi đến, trước giờ ngủ, trước khi về, đo thêm khi thấy bất thường); cảnh báo vượt ngưỡng; phụ huynh xem. Ngưỡng sốt theo quốc gia, mặc định 37,5 °C; chọn 36–40, mặc định 36,5. | Hợp lệ. "≥3/ngày" = 3 lần đo bắt buộc; cần nêu cách nhắc khi thiếu. Báo cho phụ huynh khi trẻ sốt — chưa rõ. | OQ: thiếu lần đo thì nhắc ai, lúc nào; phụ huynh có được báo ngay khi trẻ sốt không. |
| BBA-75 Late flag | Đến sau giờ chốt → "Late", chỉ dùng báo cáo Centre, không bao giờ hiện cho phụ huynh. Giờ chốt theo Centre (mặc định 9:15). | Hợp lệ, đơn giản. Trẻ học buổi chiều (Half Day PM) không thể dùng chung giờ chốt buổi sáng. | OQ: giờ chốt theo buổi học (AM / PM) hay một giờ chung. |
| BBA-76 Overview today | Bảng cho HQ / DM: mỗi Centre số trẻ đã đến / dự kiến, đã về, còn ở trường; theo brand; tổng; mở xuống lớp. | Hợp lệ. Cần định nghĩa "dự kiến". | AS: dự kiến = trẻ đang học, không nghỉ phép đã duyệt, không tạm nghỉ, có lịch học hôm đó. OQ: tần suất cập nhật số liệu. |
| BBA-77 Correction | Sửa trạng thái điểm danh hoặc giờ sau khi đã ghi, bắt buộc lý do; giữ giá trị cũ trong lịch sử. Huỷ bản ghi sai đi qua yêu cầu và duyệt. | Hợp lệ. Sửa giờ ảnh hưởng cờ Late và báo cáo trợ cấp (e-Form 1) → cần giới hạn thời gian sửa. | AS: Centre Admin, Centre Director, Senior Teacher được giao sửa trực tiếp; giáo viên gửi yêu cầu. OQ: sửa được lùi tối đa bao nhiêu ngày; tháng đã chốt có sửa được không. |
| BBA-78 Routines web | Xem / sửa sinh hoạt theo lớp và ngày (ăn, sữa, ngủ, thay tã, đi vệ sinh); cài đặt loại sinh hoạt nào phụ huynh thấy. Mỗi lần sửa ghi người sửa. | Hợp lệ. Cài đặt "phụ huynh thấy gì" ở cấp nào chưa rõ. | OQ: cài đặt theo level, Centre hay toàn brand; ai được đổi. |
| BBA-79 Staff clock | Chấm công nhân viên (giờ vào / ra), đánh dấu nghỉ, hiện ở màn Staff; làm cơ sở kiểm tra tỷ lệ giáo viên / trẻ. Đo nhiệt độ khi vào ca. Nghỉ phép, phân ca của nhân viên nằm ngoài Phase 1. | **Cần xác nhận phạm vi**: "đánh dấu nghỉ" và "kiểm tra tỷ lệ" vượt phạm vi Phase 1 đã thống nhất. Tỷ lệ giáo viên / trẻ theo quy định chưa có số liệu. | OQ (cao): đánh dấu nghỉ là đánh dấu đơn giản trong ngày hay quản lý phép; tỷ lệ theo level là bao nhiêu và ai nhận cảnh báo. |
| BBA-80 Payment schedule per child | Mỗi trẻ: loại chương trình (Full Day, Half Day AM / PM, Flexi Care, Emergency, Sessions, Extended, Holiday…), tên lịch phí, nett, subsidy, additional subsidy, FA, discount, GST, amount, ghi chú, trạng thái Set / Not Set, thời gian hiệu lực; là cơ sở tạo hoá đơn hằng tháng. Giá theo brand, level, chương trình, quốc tịch; giá mới = giá mới có ngày hiệu lực. | Hợp lệ. Trẻ "Not Set" sẽ không có hoá đơn → phải cảnh báo trước ngày tạo hoá đơn. Hai lịch phí chồng thời gian cho cùng loại chương trình phải bị chặn. | OQ: công thức amount (thứ tự GST / discount / subsidy — xem BBA-87); trẻ học 2 chương trình cùng lúc. |
| BBA-81 Apply template | Chọn trẻ (lớp / level / quốc tịch) rồi áp mẫu lịch phí để tạo hoặc thay lịch phí cho một khoảng thời gian. | Hợp lệ. "Thay" lịch phí đang hiệu lực phải đóng lịch cũ, không xoá. | OQ: mẫu lịch phí do ai tạo, nằm ở đâu. |
| BBA-82 Batch update | Cập nhật hàng loạt trường lịch phí (ví dụ phí mới từ tháng 1) cho nhóm trẻ, có xem trước. | Hợp lệ; giống BBA-81 nhưng sửa trường. Không được sửa tháng đã chốt. | AS: cập nhật = tạo bản mới từ ngày hiệu lực. |
| BBA-83 Billing company | Gán mỗi trẻ / Centre cho pháp nhân xuất hoá đơn (Bill From) dùng trên hoá đơn, file GIRO và PayNow QR. Hoá đơn đã phát hành giữ thông tin pháp nhân lúc phát hành; mỗi pháp nhân một tài khoản ngân hàng và một UEN. | Hợp lệ. Đổi pháp nhân giữa chừng ảnh hưởng uỷ quyền GIRO (gắn pháp nhân). | OQ: khi đổi pháp nhân, uỷ quyền GIRO cũ còn dùng được không. |
| BBA-84 Payment item | Mô tả / mã, level, chương trình, quốc tịch, nhãn trẻ, đơn giá, loại (định kỳ / một lần), mặc định cho tiêu chí, thuế suất, hiệu lực, ghi chú. Mục phí có mã, tên, tài khoản kế toán, cách tính thuế, được trừ CDA; ngừng dùng từ ngày. | Hợp lệ. "Mặc định cho tiêu chí" — chỉ một mục mặc định cho một bộ tiêu chí trong cùng thời gian. | OQ: danh sách "nhãn trẻ" (staff child, SUG…). |
| BBA-85 Item approval | Mục phí mới hoặc thay đổi phải gửi duyệt ("Apply for new payment item"), HQ Finance duyệt trước khi dùng. | Hợp lệ. Người gửi và người duyệt phải khác nhau. | OQ: ai được gửi (Centre? Finance?). |
| BBA-86 Discount approval | Đơn giảm giá được duyệt / từ chối (Pending / Approved / Rejected); người gửi nhận thông báo trong app. Giảm giá cần duyệt đi qua CD rồi Finance; từ chối cần lý do. | Hợp lệ. | AS: theo tuyến duyệt đã cấu hình. |
| BBA-87 Calculation order | Bật / tắt: GST tính sau hay trước giảm giá; giảm giá trước hay sau trợ cấp; credit note có GST theo thuế suất riêng. | Hợp lệ nhưng **rủi ro cao**: đổi thứ tự làm đổi số tiền hoá đơn. Phải áp từ một ngày hiệu lực, không đổi hoá đơn đã phát hành. | OQ: thiết lập theo pháp nhân hay toàn hệ thống; giá trị mặc định hiện tại trên Taidii. |
| BBA-88 Invoice generation | Ngày trong tháng tạo hoá đơn, kỳ nào (tháng sau…), trạng thái khi tạo, số ngày đến hạn mặc định. Mặc định: tạo bản nháp ngày 24, phát hành trước cuối tháng, đến hạn ngày 5. | Hợp lệ. Ngày phải hợp lệ (1–28) để tháng nào cũng có. | AS: ngày 1–28. |
| BBA-89 GIRO list | Mỗi trẻ 3 loại tài khoản (Non-CDA / CDA / Refund): ngân hàng, số tài khoản (che), chủ tài khoản, mandate ID / DDA, cập nhật lần cuối, cách đăng ký, trạng thái; lọc trẻ, năm, trạng thái trẻ, trạng thái uỷ quyền. Chỉ hiện 4 số cuối. | Hợp lệ. Lưu ý: tài khoản hoàn tiền do phụ huynh tự đặt, Finance chỉ xem. | — |
| BBA-90 Mandate set-up | Tạo uỷ quyền: loại, ngân hàng, tài khoản, chủ tài khoản, cách đăng ký (eGIRO / mẫu giấy), pháp nhân; in mẫu giấy khi đăng ký tay. Mỗi gia đình một tài khoản GIRO và một tài khoản CDA. | Hợp lệ. | OQ: mẫu giấy theo ngân hàng nào. |
| BBA-91 Status tracking | Vòng đời trạng thái (Not set up / Pending / Rejected / Terminated…) có ngày và mã tham chiếu ngân hàng; uỷ quyền bị từ chối / chấm dứt không vào đợt thu; cảnh báo trẻ chưa có uỷ quyền hoạt động. | Hợp lệ. Thiếu tên trạng thái "Active" trong tiêu đề ticket nhưng bắt buộc phải có. | AS: thêm Active. |
| BBA-92 Resend | Gửi lại link eGIRO / mẫu cho phụ huynh (app / email) kèm số lần nhắc. | Hợp lệ. | OQ: giới hạn số lần gửi. |
| BBA-93 Recreate | Tạo uỷ quyền mới sau khi bị từ chối / chấm dứt hoặc đổi ngân hàng; giữ uỷ quyền cũ trong lịch sử. | Hợp lệ. Uỷ quyền cũ đang Active khi đổi ngân hàng phải ngừng khi uỷ quyền mới Active, tránh thu hai lần. | — |
| BBA-94 Import mandates | Nhập hàng loạt chi tiết / trạng thái uỷ quyền từ file xác nhận của ngân hàng hoặc bảng tính (chuyển dữ liệu và cập nhật hằng tháng). | Hợp lệ. Định dạng file ngân hàng chưa có. | OQ: mẫu file ngân hàng. |
| BBA-95 Subsidy per child | Theo năm: mã hồ sơ, lớp, chương trình, loại SCFA (ví dụ LOR), subsidy, additional subsidy, FA, ngày hết hạn, ngày gia hạn; sửa trực tiếp có lịch sử. Hoá đơn trừ trợ cấp theo ngày hết hạn. | Hợp lệ. BBA chưa gửi file mẫu danh sách trợ cấp hiện tại (#526). | OQ: danh sách loại SCFA; sửa trợ cấp có cần duyệt không. |
| BBA-96 Template | Tải mẫu bảng tính chuẩn để nhập trợ cấp hàng loạt. | Hợp lệ. Cột mẫu = các trường của BBA-95; định danh trẻ bằng mã gì chưa chốt. | OQ: cột định danh trẻ (student ID / NRIC / mã hồ sơ). |
| BBA-97 Upload | Tải file trợ cấp cho nhiều trẻ; kiểm tra, xem trước, áp dụng; lưu nhật ký (báo cáo Import Subsidy: file, người tải, ngày, số dòng nhập, giá trị đã đặt, dòng bị loại kèm lý do). | Hợp lệ. Áp dụng một phần (dòng đúng vào, dòng sai bị loại) hay tất cả hoặc không → cần chốt; tải lại cùng file không được nhân đôi. | AS: dòng hợp lệ được áp, dòng lỗi bị loại và báo lý do. OQ: xác nhận cách này với Finance. |

### 3. Đề xuất của BA (chưa phải yêu cầu)
- BBA-69: ghi "In lúc <giờ>" trên bản in cho bếp.
- BBA-73: chặn trả trẻ cho người ngoài danh sách thay vì chỉ cảnh báo.
- BBA-87: thay đổi thứ tự tính chỉ áp dụng từ kỳ hoá đơn sau, có xem trước số tiền thay đổi.

## BBA-67 US-001 — Tab Enrolment: brainstorm lại (11/11/2026)

> Nguồn đã đọc: FRD BBA-67 3.1.1.02 Child Record Tabs – Read Views v0.2 (bản trên Drive, sửa 11/11), BBA-SMS-SRS-Children-and-Families-v0.1 (số trang theo bản Word gốc xuất PDF A4), ticket Plane BBA-67. Không dùng prototype.

### 1. Bối cảnh & vấn đề
**Đã biết**
- Hồ sơ trẻ để Centre và HQ giữ một bản ghi chính xác của từng trẻ, thay Taidii và giấy tờ (nguồn: SRS C&F §1, tr.3).
- BBA-67 yêu cầu tab chỉ đọc "enrolment history (centre, class, programme, dates, status changes)", có liên kết sang màn của module (nguồn: Plane BBA-67).
- SRS liệt kê các tab của hồ sơ trẻ: Overview, Family, Health, Documents, Pickup, **Class history**, Consents, Billing — không có tab "Enrolment" (nguồn: SRS C&F §4 mục 1.1 View child profile, tr.6).
- Trạng thái của trẻ do Joining & leaving đặt (tạm nghỉ, thôi học, tốt nghiệp), không sửa tay trên hồ sơ (nguồn: SRS C&F §4 mục 1.1 View status, tr.6; BR-CHF-006, tr.8; AC-CHF-005, tr.11).
**Chưa biết**
- OQ-RT-16: Tab Enrolment có thay cho tab "Class history" của SRS không?

### 2. Mục tiêu
**Chưa biết** — SRS và ticket không nêu chỉ số đo được cho tab này. Mục tiêu nghiệp vụ suy ra từ user story: nhân viên trả lời phụ huynh về ngày bắt đầu học, lớp, chương trình, tiến độ thôi học mà không phải mở Joining & Leaving.

### 3. Người dùng & vai trò
| Vai trò | Việc chính với tab Enrolment | Nguồn |
|---|---|---|
| School Admin | Trả lời phụ huynh về ngày học, lớp, chương trình; xếp lớp cho trẻ. | SRS C&F §2, tr.3; §3 P1 bước 3, tr.4 |
| Centre Director | Quản lý trẻ và lớp của Centre; theo dõi việc thôi học, chuyển Centre. | SRS C&F §2, tr.3 |
| HQ Enrolment | Hồ sơ trẻ sinh ra từ việc ghi danh; xem và sửa hồ sơ mọi Centre. | SRS C&F §2, tr.3 |
| Teacher | Xem trẻ lớp mình. | SRS C&F §2, tr.3–4; AC-CHF-006, tr.11 |
| HQ Finance | Xem trẻ và gia đình. | SRS C&F §2, tr.4 |

### 4. Phạm vi
| Trong phạm vi | Ngoài phạm vi | Chờ chốt |
|---|---|---|
| Các lần ghi danh (Centre, level, lớp, programme, các ngày, trạng thái); dòng thời gian thay đổi trạng thái; lịch sử lớp (xếp lớp, đổi lớp, lên lớp); việc thay đổi trạng thái đang chờ (case); liên kết sang Joining & Leaving và Classes. | Đổi trạng thái bằng tay (SRS C&F §1.2, tr.3). Bắt đầu case (thuộc Joining & Leaving). Sửa programme (làm ở Edit child profile, có change record). | Đánh dấu SUG / Staff / KA child (OQ-RT-04); liên kết bắt đầu case (OQ-RT-17); pháp nhân, loại chương trình, năm học (OQ-RT-13). |

### 5. Quy trình nghiệp vụ
**5.1 Hiện tại:** Centre dùng Taidii và giấy tờ (nguồn: SRS C&F §1, tr.3). Chưa có mô tả chi tiết cách tra lịch sử ghi danh hôm nay.
**5.2 Mong muốn** — các sự kiện tab phải hiển thị:
1. Ghi danh được xác nhận ở Enrolment → hồ sơ trẻ được tạo với trạng thái Enrolled (SRS C&F §3 P1, tr.4; AC-CHF-001, tr.11).
2. School Admin xếp lớp có ngày hiệu lực (P1 bước 3, tr.4; mục 1.1 Assign class, tr.6).
3. Đổi lớp có ngày hiệu lực; trẻ rời nhóm chat lớp cũ, vào nhóm chat lớp mới (mục 1.1 Change class, tr.6; BR-CHF-046, tr.10).
4. Trẻ sơ sinh chuyển lên playgroup lúc 18 tháng (BR-CHF-047, tr.10).
5. Lên lớp đầu năm học: trẻ chuyển lên level kế tiếp, ngày hiệu lực là đầu năm học mới; trẻ ở lại lớp thì không đổi (§3 P6, tr.5; BR-CHF-048, tr.10).
6. Đổi programme (nửa ngày ↔ cả ngày) qua sửa hồ sơ, có change record ghi người sửa, người duyệt, ngày hiệu lực (AC-CHF-004, tr.11; BR-CHF-005, tr.8).
7. Joining & leaving đặt trạng thái tạm nghỉ, thôi học, tốt nghiệp (mục 1.1 View status, tr.6).
**5.3 Ngoại lệ & nhánh rẽ**
- Trẻ đã thôi học, tốt nghiệp: vẫn tìm được, hồ sơ không bị xoá (BR-CHF-007, tr.8; BR-CHF-008, tr.9) → lịch sử ghi danh vẫn xem được.
- Lớp đã đóng: không xoá, giữ lịch sử (BR-CHF-049, tr.10) → lịch sử lớp vẫn hiện tên lớp cũ.
- Hồ sơ tạo tay (không qua Enrolment) cần Centre, level, start date (BR-CHF-001, tr.8) → có tạo lần ghi danh không? (OQ-RT-14)
- Trẻ chưa sinh có start date trong tương lai (BR-CHF-002, BR-CHF-003, tr.8).
- Chuyển Centre: SRS chỉ có 4 trạng thái Enrolled / Temporary withdrawal / Withdrawn / Graduated → lần ghi danh cũ mang trạng thái nào? (OQ-RT-12)
- Phạm vi xem: nhân viên Centre chỉ thấy trẻ Centre mình (mục 1.1 Apply access scope, tr.6) → nhân viên Centre mới có thấy lần ghi danh ở Centre cũ không? (OQ-RT-15)

### 6. Dữ liệu
| Nguồn | Dữ liệu tab đọc | Chiều |
|---|---|---|
| Joining & Leaving | Lần ghi danh, trạng thái, các lần đổi trạng thái, case đang mở | Chỉ đọc |
| Children & Families › Classes | Lớp, level, ngày hiệu lực xếp lớp / đổi lớp / lên lớp, người thực hiện | Chỉ đọc |
| Children & Families › change record | Đổi programme: giá trị cũ → mới, người sửa, người duyệt, ngày hiệu lực | Chỉ đọc |
| Organisation | Centre, brand | Chỉ đọc |

### 7. Rủi ro
| Loại | Nội dung | Mức độ | Giảm thiểu |
|---|---|---|---|
| Dữ liệu cá nhân | Đánh dấu Staff child kèm mức giảm học phí hiện cho Teacher, trong khi Teacher không xem tab Finance (AS-RT-01). | Cao | Chuyển đánh dấu sang tab Finance hoặc ẩn với Teacher (OQ-RT-04). |
| Mâu thuẫn trạng thái | Trạng thái "Transferred" không có trong danh sách của SRS. | Trung bình | OQ-RT-12. |
| Phạm vi | Liên kết "Start a withdrawal…" là thao tác tạo, trái với tab chỉ đọc (mục 3 FRD). | Trung bình | Bỏ khỏi tab, chờ OQ-RT-17. |
| Chuyển dữ liệu | Lịch sử ghi danh cũ trên Taidii có được chuyển sang không — chưa rõ. | Trung bình | OQ-RT-18. |

### Rà soát US-001 hiện tại (bản Drive v0.2)
| Mục | Nhận xét | Đề xuất |
|---|---|---|
| FR-001, FR-002, FR-007, BR-001, BR-002 | Khớp ticket BBA-67 và SRS (BR-CHF-006, 007, 008). | Giữ; ghi rõ trạng thái theo BR-CHF-006. |
| FR-002: brand, pháp nhân, loại chương trình, năm học | Ticket và SRS C&F không nêu. | Giữ, đánh dấu chờ OQ-RT-13. |
| FR-003: "đổi lớp" trong dòng thời gian, nguồn Joining & Leaving | Đổi lớp là việc của Classes (BR-CHF-046), không phải Joining & Leaving; SRS có tab "Class history" riêng. | Tách thành phần "Lịch sử lớp học". |
| Đổi programme | SRS ghi đổi programme qua change record (AC-CHF-004) — FRD chưa có. | Thêm vào dòng thời gian. |
| FR-004 Cases | Không có trong SRS C&F; là việc đổi trạng thái đang chờ, phù hợp "status changes" của ticket. | Giữ, chỉ đọc, ghi giả định. |
| FR-005 liên kết bắt đầu case | Là thao tác tạo; trái phạm vi "chỉ đọc". | Bỏ khỏi bản nháp, chờ OQ-RT-17. |
| FR-006 Flags | Không có trong ticket và SRS C&F; là thông tin học phí; Teacher thấy được trong khi không xem Finance. | Bỏ khỏi tab Enrolment, đề xuất chuyển sang tab Finance (OQ-RT-04). |
| AC-003 trạng thái "Transferred" | Không có trong 4 trạng thái của SRS. | OQ-RT-12. |
| Thiếu | Trường hợp hồ sơ tạo tay, trẻ chưa sinh, lớp đã đóng, Teacher xem trẻ đã rời lớp. | Thêm luồng thay thế và AC. |

### Đề xuất của BA (chưa phải yêu cầu)
- Tab Enrolment gom luôn nội dung "Class history" của SRS để người dùng xem một chỗ (AS-RT-11).
- Chuyển đánh dấu SUG / Staff / KA child sang tab Finance.

Bản nháp US-001: `FSD/Sprint 4/BBA-67_US-001_Tab_Enrolment_Draft_VI.md`.

### Bổ sung 11/11/2026 — Enrolment hiểu theo SRS (theo góp ý của BA phụ trách)
- Ghi danh được xác nhận → trẻ là Enrolled, kể cả chưa tới ngày bắt đầu học (AC-CHF-001, tr.11).
- Đăng ký (Registration) trước, ghi danh (Enrolment) là bước xác nhận sau cùng: hồ sơ tạo từ dữ liệu đăng ký, phiếu đăng ký đã ký là giấy tờ của trẻ (§3 P1, tr.4; §4 mục 1.4, tr.7; BR-CHF-030, tr.9).
- Ghi danh được cho trẻ chưa sinh bằng ngày dự sinh (§4 mục 1.1, tr.5; BR-CHF-002, tr.8).
- Mọi thay đổi sau ghi danh thuộc Joining & leaving (BR-CHF-006, tr.8).
- Kết luận: tab Enrolment chỉ mô tả thông tin ghi danh và các thay đổi sau ghi danh; không đi sâu lịch sử lớp, case, đổi programme. Bản nháp US-001 nâng lên 0.2.
