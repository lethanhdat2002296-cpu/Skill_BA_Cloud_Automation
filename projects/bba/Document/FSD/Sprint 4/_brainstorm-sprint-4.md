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
| 3.1 Child Record Tabs – Read Views (v0.1, thêm 10/11/2026) | 6 | 38 | 44 | 9 | 7 |
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
