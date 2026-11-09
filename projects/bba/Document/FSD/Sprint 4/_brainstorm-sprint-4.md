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
| 2.8 CRM Administration | `BBA_CRM_SRS_v0.1.md` | §1.1 (WBS 2.8.1.01–04, 2.8.2.01–03), §1.2 (2.8.2.04–07 Phase 2), §3 P4, P5, P7, §4 mục 3.3, 4.4, 4.5, §5 BR-CRM-019–020, 023–032, §6.1, §8 AC-CRM-004, 006, 008–010 | BBA-43 (hiển thị Journey runtime) |
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

## 2.8 CRM Administration

**1. Bối cảnh** — Quản trị viên duy trì Journey, Slot Schedule và khoảng loại trừ trong phạm vi được duyệt (nguồn: CRM SRS P7 bước 18).

**2. Mục tiêu** — SRS không nêu KPI. → OQ-ADM-01.

**3. Người dùng** — HQ Admin (cấu hình CRM, quyền, Country/Brand/Centre), Centre Director (host, capacity, phê duyệt theo quốc gia), System (sinh Slot, áp audit) (nguồn: CRM SRS §2).

**4. Phạm vi**

| In scope (Phase 1) | Ngoài phạm vi | Sprint 3 / FRD khác |
|---|---|---|
| 2.8.1.01 Journey template versioning · 2.8.1.02 Visual Journey builder · 2.8.1.03 Journey preview · 2.8.1.04 Activity Template runtime rules (§4 mục 3.3) · 2.8.2.01 Visit Slot Schedule CRUD (§4 mục 4.4) · 2.8.2.02 Sinh và rà Slot theo ngày (§4 mục 4.5) · 2.8.2.03 Huỷ một Slot đã sinh, gồm phê duyệt xoá Slot ở Malaysia (§4 mục 4.5, BR-CRM-029–031) | 2.8.2.04–07: gửi duyệt thay đổi Schedule, duyệt/từ chối, quy tắc tác động lên booking, thời lượng theo loại Visit (Phase 2, §1.2); View Lead score (Not identified in the WBS) | Chạy Journey trên Enquiry (FRD 2.3); đặt Visit, Calendar (nhóm 2.4); hiển thị Journey runtime (BBA-43) |

**5. Quy trình (TO-BE theo SRS)**
1. Admin tạo Journey Template có phạm vi; cấu hình Stage (thứ tự State, phase, base score, tier không chồng lấn), Activity (Task / sub-task, thứ tự, manual/automatic, owner, progress points, score points), sự kiện hoàn tất (nguồn: §4 mục 3.3).
2. Sửa Template không làm đổi Enquiry đang chạy (nguồn: §4 mục 3.3 "without changing existing Enquiry runs", "without silently changing saved Enquiry runs").
3. Preview Template không đổi runtime (nguồn: §4 mục 3.3, Phase 1).
4. Admin tạo Visit Slot Schedule (Visit type, giờ, host, hiệu lực, loại trừ) → lưu thẳng, chỉ Active/Inactive, không duyệt (nguồn: BR-CRM-027, 028, AC-CRM-008).
5. Hệ thống sinh Slot tương lai; Slot chỉ hiển thị khi active, hợp lệ, không bị loại trừ, còn chỗ (nguồn: §4 mục 4.1, 4.5, BR-CRM-026, AC-CRM-006).
6. Xoá một Slot: Malaysia cần phê duyệt cấu hình; đang chờ → ngừng nhận booking; xoá có hiệu lực → Visit đã đặt thành Cancelled lý do "Centre cancelled" (nguồn: BR-CRM-029–031, AC-CRM-009, 010).
- **Chưa biết:** quy tắc phiên bản Journey (OQ-ADM-02); thao tác của builder trực quan (OQ-ADM-03); "Activity Template runtime rules" cụ thể (OQ-ADM-04); khoảng thời gian sinh Slot trước (OQ-ADM-05); vai trò duyệt xoá Slot (OQ-ADM-06); cấu hình khoảng loại trừ (OQ-ADM-07).

**6. Dữ liệu** — Journey Template, Stage, Activity, Scoring tier; Visit Slot Schedule, Slot, Deletion request (nguồn: §4 mục 3.3, 4.4, 4.5). Notification "Scheduled-Slot deletion approval" → người duyệt (nguồn: §6.1).

**7. Rủi ro** — SRS mục 4 nhảy từ 4.5 sang 4.7 (thiếu 4.6) → có thể thiếu nội dung (OQ-ADM-08).

| Mã | Nội dung | Loại |
|---|---|---|
| OQ-ADM-01 | Chỉ số thành công cho cấu hình CRM ở Sprint 4? | OQ |
| OQ-ADM-02 | Versioning: khi nào tạo phiên bản mới (mỗi lần lưu hay khi publish), có trạng thái Draft/Published không, Enquiry mới nhận phiên bản nào. | OQ |
| OQ-ADM-03 | Visual Journey builder: thao tác cần có (kéo thả, sắp thứ tự, nhân bản…) — theo prototype "Journey Settings". | OQ |
| OQ-ADM-04 | Activity Template runtime rules: tính hạn Task, thứ tự bắt đầu, danh mục event key được duyệt. | OQ |
| OQ-ADM-05 | Hệ thống sinh Slot trước bao nhiêu ngày/tuần; xử lý Slot đã sinh khi sửa Schedule. | OQ |
| OQ-ADM-06 | Vai trò duyệt xoá Slot ở Malaysia; Singapore và Vietnam có cần duyệt không. | OQ |
| OQ-ADM-07 | Khoảng loại trừ (ngày lễ, sự kiện Centre) được quản lý ở đâu, ai cấu hình. | OQ |
| OQ-ADM-08 | SRS CRM không có mục 4.6 — có nội dung bị thiếu không? | OQ |

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
| 2.8 CRM Administration | 7 | 32 | 39 | 10 | 3 |
| 3.1 Children and Families | 10 | 66 | 60 | 12 | 2 |
| 3.2 Daily Operations | 14 | 69 | 74 | 14 | 7 |
| 3.6 Finance | 22 | 97 | 107 | 15 | 6 |
