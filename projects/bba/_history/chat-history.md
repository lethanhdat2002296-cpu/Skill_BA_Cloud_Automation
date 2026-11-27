# Lịch sử hỏi đáp — BBA Sprint 4

> Ghi lại từng câu hỏi của user và câu trả lời của Claude, theo thứ tự thời gian. Mới nhất ở cuối.

---

## 22/11/2026 — Làm lại tài liệu BBA-71 → BBA-77

**User:**
> Tạm thời đã ổn.
> Giờ các tài liệu từ BBA-71 đến BBA-77
> 1. Theo format của các tài liệu trước
> 2. Nội dung làm kỹ theo tiêu đề của task.
> 3. Khi tham khảo Prototype và test thử trên đó. Các tính năng nào không dính líu đến nội dung của task thì bỏ qua không mô tả nó
> 4. Mỗi câu hỏi của tao và câu trả lời của mày hãy lưu history lại trên github nhé.

**Claude:**
Đã viết lại 7 tài liệu theo format BBA-50/66/51/52 (mỗi tính năng một User Story; FR ngắn, quy tắc ở BR/VAL/DATA; bỏ mục Giả định và Tài liệu tham khảo; câu hỏi đã có câu trả lời thì xoá). Đã đọc comment của Hải trên Drive, task trên Plane và thử trên prototype; tính năng không thuộc task thì bỏ. Mới sửa trên máy, chưa đẩy Drive / Git (chờ "update").

| Ticket | User Story | Thay đổi chính |
|---|---|---|
| BBA-71 Consent | 3: danh sách consent của trẻ theo phiên bản; tạo và gửi; gửi lại và nhắc | Theo comment Hải; bỏ Consent compliance, phát hành phiên bản mới, rút lại, checklist; nhắc tối đa 1 lần/ngày; chỉ sửa consent khi chưa ai trả lời (prototype) |
| BBA-72 Bulk promotion | 3: chọn lớp đích và ngày hiệu lực; xem trước trẻ và tác động; xác nhận và kết quả | Theo comment Hải: lớp cũ giữ danh sách trẻ, cập nhật trạng thái trẻ trong lớp và trạng thái lớp; tạo lớp đích ngay trong luồng (prototype) |
| BBA-73 Handover | 3: ghi người đưa; ghi người đón; quản lý thông tin đưa / đón | Theo comment Hải: ghi nhận và quản lý trên SMS; bỏ iPad / mất mạng; không ấn định sáng / chiều |
| BBA-74 Temperature | 3: ghi lần đo; cảnh báo sốt và lần đo còn thiếu; xem, sửa, phụ huynh xem | Bỏ °F, Bluetooth, iPad, xuất Excel |
| BBA-75 Late flag | 3: giờ chốt; tự đánh dấu Late nội bộ; báo cáo đến muộn | Bỏ đón muộn; thêm OQ về "Mark late — teacher judgement" của prototype |
| BBA-76 Overview today | 2: bảng tổng hợp theo Centre / brand; mở xuống lớp | District Manager → Cluster Head |
| BBA-77 Attendance correction | 3: sửa trạng thái; sửa giờ; lịch sử sửa | Thêm Void có lý do + xác nhận, Absent cần lý do và người báo (prototype) |

---

## 22/11/2026 — Update BBA-71 → BBA-77 lên Drive

**User:**
> Update lên drive

**Claude:** Kiểm tra Drive: 7 file không có chỉnh sửa mới. Xuất Word, gắn lại comment của Mỹ Hải (BBA-71: 2, BBA-72: 2, BBA-73: 3). Upload 7 file mới vào thư mục Drive 1uZpPo7…, file cũ vào thùng rác; cập nhật `_drive.json`; commit Git; thay link trên Plane.

| Ticket | File mới |
|---|---|
| BBA-71 | [FRS] BBA-71-3.1.4.01_Consent_Status_Per_Child_V0.4_VI.docx |
| BBA-72 | [FRS] BBA-72-3.1.5.01_Bulk_Class_Promotion_V0.3_VI.docx |
| BBA-73 | [FRS] BBA-73-3.2.1.01_Handover_Recording_V0.3_VI.docx |
| BBA-74 | [FRS] BBA-74-3.2.1.02_Temperature_Readings_V0.3_VI.docx |
| BBA-75 | [FRS] BBA-75-3.2.1.03_Late_Flag_Internal_V0.2_VI.docx |
| BBA-76 | [FRS] BBA-76-3.2.1.06_Centre_Brand_Overview_Today_V0.2_VI.docx |
| BBA-77 | [FRS] BBA-77-3.2.1.07_Attendance_Correction_V0.2_VI.docx |

---

## 23/11/2026 — BBA-71: sửa theo bản user chỉnh trên Drive

**User:**
> BBA-71 thay đổi chút ít
> 1. Hiện tại, tao có update lại câu từ trong tài liệu => Dựa vào đó update lại nội dung
> 2. Bổ sung thêm thông tin tại US-001, toàn bộ thông tin ở tab Document cho phép toàn bộ giáo viên xem kể cả khi bé chuyển lớp khác. Dựa vào câu từ tao viết hãy mô tả cho chỉnh chu lại nhé
> 3. Chỉ gửi thông tin lại cho phụ huynh khi hết hạn, không gửi lại cho phụ huynh khi họ từ chối
> 4. Ngoài ra, đánh số thứ tự lại giúp tao

**Claude:** Lấy bản Drive (user sửa 23/11 02:02) làm gốc, giữ nguyên câu chữ user sửa. Bổ sung US-001: FR-003, BR-004 (mọi giáo viên xem toàn bộ tab Documents, kể cả khi trẻ chuyển lớp; chỉ xem), luồng thay thế, AC-006, AC-007, dòng Teacher ở mục 4. Gửi lại chỉ khi Expired: BR-009 viết lại, nút Send again chỉ hiện với Expired, thêm AC-020 (Declined không gửi lại), sửa mục 3, mục 5, thuật ngữ. Gỡ tham chiếu tới BR-004, BR-006, BR-007 đã xoá; bỏ AC "Primary contact only". Đánh số lại: FR-001..011, BR-001..009, VAL-001..003, DATA-001..003, AC-001..020. Chưa đẩy Drive / Git (chờ "update").

---

## 23/11/2026 — BBA-71, BBA-73: bổ sung theo file Excel câu hỏi phản hồi

**User:**
> (đính kèm BBA_SMS_S4 — Tổng hợp câu hỏi phản hồi.xlsx) Cập nhật tiếp về BBA-71
> 1. Dựa vào file Excel tao mới gửi. Check từ "Q-73-04 đến Q-73-15" rồi bổ sung thêm vào tài liệu nhé. không bịa thêm ra nha
> Sửa thông tin lại BBA-73
> 1. Tài liệu này đang chỉ mô tả thông tin hệ thống ghi nhận khi có người đưa và người đón trẻ ở trên SMS. Không mô tả thông tin như tạo người đưa người đón trẻ như nào. Chỉ mô tả xem màn hình đó lưu các thông tin gì của trẻ khi được đưa đi đón về
> 2. Check thêm trong file excel từ "Q-75-02 đến Q-75-12" để bổ sung thêm thông tin

**Claude:**
- BBA-71: bổ sung từ Q-73-04, 06, 07, 08, 09, 10, 11, 12, 14 (loại consent theo brand / Crossroad; người nhận theo lớp hoặc cả Centre, cả hai phụ huynh hoặc người liên hệ chính; Announcement kèm link, email tuỳ chọn, nhóm "Surveys + Consents"; câu trả lời về SMS và tick checklist; giáo viên chỉ thấy consent lớp mình ở Surveys & consents; thẻ tổng quan bấm vào chỉ hiện trẻ chưa trả lời; năm học tháng 1–12, Crossroad gia hạn đầu năm; nhiều consent mở cùng lúc; lưu phiên bản và thời điểm đồng ý). Câu chưa phản hồi đưa vào OQ (Q-73-09, Q-73-11, Q-73-12 phần gia hạn, Q-73-06 phần consent gửi sau). Q-73-13 (rút consent, chặn ảnh) không thêm vì ngoài phạm vi; Q-73-15 DOTB tự quyết. Không có Q-73-05 trong file. Đánh số lại.
- BBA-73: chỉ mô tả thông tin màn hình ghi nhận khi trẻ được đưa đến / đón về; bỏ phần chờ duyệt người đón và OQ về người duyệt. Bổ sung từ Q-75-02, 04, 08, 10, 12: ảnh giao nhận bắt buộc, phụ huynh xem ảnh; trẻ đi xe mỗi trẻ một bản ghi, một ảnh; người đưa có thể là người giúp việc; không override. OQ mới: khoảng chỉnh giờ (Q-75-08), thời gian lưu ảnh (Q-75-12). Gộp sửa của user trên Drive (tên tài liệu, phiên bản 0.1). Đánh số lại.
- Chưa đẩy Drive / Git (chờ "update").

---

## 23/11/2026 — Update BBA-71, BBA-73; sửa BBA-74 (SMS chỉ hiển thị)

**User:**
> update BBA-71 và BBA-73 lên drive
> Trong khi Update 2 tài liệu trên. Tài liệu BBA-74 cũng cần thay đổi như sau
> 1. Phần đo và nhập nhiệt độ sẽ ở trên App. Còn SMS sẽ hiển thị thông tin từ App lên => Đối với tài liệu này sẽ mô tả thông tin hiển thị chứ không đi mô tả chức năng trên SMS
> 2. Check trong File excel đó luôn "Q-76-05 đến Q-76-06" để update thêm thông tin. Lưu ý, hệ thống SMS trong tài liệu này chỉ hiển thông tin không đề cập đến việc sửa hay xóa gì trên SMS nha

**Claude:**
- BBA-71, BBA-73: kiểm tra Drive (BBA-71 chỉ đổi tên file, BBA-73 đã gộp trước đó), upload bản mới (V0.1), file cũ vào thùng rác, commit e9dbdb9, thay link Plane.
- BBA-74: viết lại thành tài liệu hiển thị: 3 US (hiển thị lần đo trên bảng điểm danh; cảnh báo sốt và trẻ còn thiếu lần đo; chi tiết lần đo trong ngày ở Day record). Bỏ thêm / sửa / xoá trên SMS, Sign in nhập nhiệt độ, Parent App chuyển ra ngoài phạm vi. Q-76-05: dải nhập trên App (mặc định 36.5, dải nhanh 36.3–36.7, thang 36–40, "Enter manually") ghi vào BR-003; phần nhập ngoài thang cảnh báo hay chặn → OQ-04. Q-76-06: giá trị Bluetooth sửa được trên App, SMS hiện cách đo và nhãn đã sửa (BR-008). Giữ sửa của user trên Drive (tên, phiên bản 0.1, "Parent App", "sức khỏe"). Chưa đẩy Drive / Git.

---

## 23/11/2026 — HTML giao diện BBA-73; update BBA-74

**User:**
> Output UX/UI của BBA-73 ra HTML tao xem
> và Update BBA-74 lên drive nhé

**Claude:**
- BBA-74: Drive không có sửa mới; upload [FRS] BBA-74-3.2.1.02_Temperature_Readings_V0.1_VI.docx (1nTld6QjLYq4zezJWGwXd0YmPVBg8bQsP), file cũ vào thùng rác, commit c439f7c, thay link Plane.
- BBA-73: tạo giao diện nháp `projects/bba/_review/sprint4-qa/frd-draft/BBA-73_giao-dien-nhap.html` (4 màn: Class attendance cột Handover, Sign in, Sign out, Handover sửa; 13 trạng thái), ghi chú dẫn mã FR/BR theo FRS. File nháp, chưa đẩy Git.

---

## 23/11/2026 — Động não BBA-73: SMS chỉ ghi nhận thông tin ra vào từ App

**User:**
> Cần mày động não phần tài liệu này giúp tao. Đối với tài liệu FRS BBA-73 này, hệ thống SMS ghi nhận thông tin từ App lưu thông tin đưa đón của trẻ như thế nào trên SMS.
> Trên SMS không có tạo hay sửa hay xóa thông tin đưa đón. Chỉ quản lý thông tin ra vào của trẻ thôi

**Claude:** Đề xuất khung mới (chưa sửa tài liệu): App ghi nhận, SMS nhận và hiển thị. 3 US: (1) SMS nhận và lưu lượt ra / vào từ App; (2) xem thông tin ra vào trên bảng điểm danh (chỉ đọc); (3) xem chi tiết ra vào trong ngày của một trẻ và các lần "Not on the list". Bỏ toàn bộ popup Sign in / Sign out / Record và VAL nhập liệu trên SMS. Nêu 4 điểm cần user chốt (sửa giờ ở BBA-77, thông báo phụ huynh, thông tin thiết bị, xem lịch sử nhiều ngày).

---

## 23/11/2026 — BBA-73: chỉ giữ US xem thông tin ra vào

**User:**
> 1. Bỏ Us-001 cái này tao không quan tâm hệ thống sync giữa SMS và App
> 2. Giữ lại Us-002
> 3. Bỏ luôn Us-003

**Claude:** Viết lại BBA-73 còn 1 US: "Xem thông tin ra vào của trẻ" trên Class attendance (chỉ xem): giờ vào / ra, Dropped off by, Picked up by (tên · quan hệ; Someone else; Bus driver / Bus attendant), ảnh giao nhận, lọc theo xe. FR-001..003, BR-001..006, DATA-001, AC-001..009. Bỏ toàn bộ Sign in / Sign out / Record, VAL nhập liệu, đồng bộ App–SMS, Day record, Not on the list. OQ còn 2 (phụ xe trong danh sách đón; thời gian lưu ảnh). Giữ anchor comment của Hải (BR-002). Chưa đẩy Drive / Git; HTML nháp chưa vẽ lại.

---

## 23/11/2026 — Update BBA-73

**User:**
> update bba-73

**Claude:** Drive có sửa lúc 03:15 (trên bản 3 US cũ). Gộp phần còn áp dụng vào bản 1 US: tên tính năng "BBA-73 Handover recording"; người đưa chỉ là phụ huynh / Someone else / tài xế xe bus; "xe bus"; bỏ mục Câu hỏi mở; không còn comment để gắn. Upload [FRS] BBA-73-3.2.1.01_Handover_Recording_V0.1_VI.docx (1wG-LSBiHVKpttH8YqdRe24iu5xLZ4TYx), file cũ vào thùng rác, commit, thay link Plane.

---

## 23/11/2026 — Dịch BBA-51, BBA-52 sang tiếng Anh

**User:**
> Dịch BBA-51 và BBA-52 sang tiếng anh nhé. Không push lên Plane

**Claude:** Bản tiếng Việt trên Drive có sửa lúc 04:26 (BBA-51 bỏ US "Xem thiết lập", còn 1 US / 1 AC; BBA-52 bỏ mục Câu hỏi mở, đổi AC-005, rút gọn mục đích). Đồng bộ bản VI trong repo theo Drive (sửa "Depedencies", US-002 → US-001 ở mục 5 của BBA-51), rồi dịch sang tiếng Anh: `2.8_Impact_Preview_Before_Change.md`, `2.8_Change_Request_Second_Approval.md` (ghi đè bản tiếng Anh cũ 14/11). Không đụng Plane. Chưa đẩy Drive / Git.

---

## 23/11/2026 — Update bản tiếng Anh BBA-51, BBA-52

**User:**
> Update vô folder này. Vẫn giữ file TV lại (thư mục: https://drive.google.com/drive/folders/1KqkgghHymUu7T9_xco51AIjnoSufVg7_)

**Claude:** Upload 2 file tiếng Anh vào thư mục trên: [FRS] BBA-51-1.3.1.02_Impact_Preview_Before_Change_V0.1_EN.docx (1FiL7-K-6ecTxxne8HKM1xxHVRI0WREDq), [FRS] BBA-52-1.3.1.03_Change_request_and_second_approval_V0.1_EN.docx (12sViWlFTOipQ1_DGcgGUQtgsxUUprVfB). File tiếng Việt giữ nguyên, không xoá gì trên Drive. Commit bản EN + VI đồng bộ + `_drive.json`. Không đụng Plane.

---

## 23/11/2026 — BBA-73, BBA-74: SMS cho thêm / sửa / xoá

**User:**
> Quay lại tài liệu BBA-73 và 74
> 1. Tao mới trao đổi lại với sếp: Hệ thống SMS vẫn cho phép người dùng thêm, xóa, sửa => Ngoài việc lấy thông tin từ App, cho người dùng được phép thêm xóa sửa
> 2. Đối với BBA-73. Nhớ chỉ tập trung vào thông tin là Đón và Đưa thôi nhé
> 3. Đối với BBA-74. Nhớ chỉ tập trung vào thông tin đo sốt cho trẻ

**Claude:** Lấy bản Drive làm gốc (BBA-73 sửa 03:49: "attendance", bộ lọc "Bus"; BBA-74 sửa 03:35: còn 1 US xem lần đo, bỏ cảnh báo sốt / Day record / OQ / Phụ lục B — giữ nguyên các chỗ bỏ).
- BBA-73: US-001 xem thông tin đưa / đón (từ App và SMS); thêm US-002 thêm, sửa, xoá người đưa / người đón và giờ trên SMS (người đưa: phụ huynh / Someone else / tài xế; người đón chỉ trong danh sách, không override; giờ hợp lệ; xoá đưa thì xoá cả đón; lịch sử). OQ: khoảng thời gian sửa, ảnh khi thêm trên SMS, lý do khi sửa / xoá. Bỏ trạng thái điểm danh khỏi phạm vi.
- BBA-74: US-001 xem lần đo (từ App và SMS); thêm US-002 thêm, sửa, xoá lần đo trên SMS (dải nhập Q-76-05, Extra cần lý do, giờ hợp lệ, sửa được cả giá trị Bluetooth Q-76-06, lịch sử). OQ: ngoài thang chặn hay cảnh báo; lý do / khoảng thời gian khi sửa xoá.
- Chưa đẩy Drive / Git.

---

## 23/11/2026 — Update BBA-73, BBA-74

**User:**
> Update lên Drive để tao xem nhé

**Claude:** Drive không có sửa mới. Upload BBA-73 (1i-g3BA5Is9mJHpgVYb4o30pgNa2_KdSq) và BBA-74 (1MRxzS8VQaQcH_in8og50nCp1JWdaNhTI) vào thư mục 1uZpPo7…, file cũ vào thùng rác, commit, thay link Plane.

---

## 25/11/2026 — BBA-73, BBA-74 theo UX/UI V13

**User:**
> (đính kèm BBA-73-74_Version_moi.html) Chỗ tài liệu BBA-73 và BBA-74. Sửa thông tin lại theo UX/UI mới nhất tao gửi cho mày. Nhưng vẫn tuân thủ theo các nguyên tắc khi viết FRS mà tao nói mày nhé. Với lần này thay đổi chút là mày không được phép update lên Plane nữa nhé

**Claude:** Đọc UX/UI V13 (tab Attendance và Temperature, sửa trên dòng, Changelog, Round config) và bản user sửa trên Drive (BBA-73 08:06: giờ tự ghi, OQ còn 1; BBA-74 09:00: ô nhiệt độ mặc định trống, bỏ OQ).
- BBA-73: 2 US — xem thông tin đưa / đón (bảng Attendance results, lọc, ảnh bàn giao lúc đón) và thêm / sửa / xóa trên dòng (lý do bắt buộc, Someone else popup, quy tắc nhập cùng nhau, đón sau đưa, chỉ khi Có mặt, Changelog từng trường). Sửa Kết quả / Hủy kết quả để ở BBA-77; bỏ bộ lọc xe bus (V13 không có).
- BBA-74: 4 US — xem lần đo (tab Temperature, x of 3, ≥37.5 tô đỏ), thêm lần đo (dòng mới + popup từ Attendance), sửa / xóa nhiều dòng / Changelog, cấu hình danh mục Round.
- Không đụng Plane từ lần này. Chưa đẩy Drive / Git.

---

## 25/11/2026 — Update BBA-73, BBA-74 (V13)

**User:**
> Update lên drive nhé

**Claude:** Drive không có sửa mới. Upload BBA-73 (17sT9eCHW1GcVRu9iLBpc4-BVUmgNaRT5) và BBA-74 (1s7BQ0UyeHED89EV3kT27JQrKmegyR05y) vào thư mục 1uZpPo7…, file cũ vào thùng rác, commit Git. Không cập nhật Plane (theo yêu cầu).

---

## 25/11/2026 — BBA-73, BBA-74 theo mẫu BBA-79 và Figma

**User:**
> (đính kèm FRS_BBA-79-3.2.5.01_Staff_Clock_In_Out_v0.1.docx, link Figma node 1417-17) Tài liệu 73 và 74 nó na ná như tài liệu BBA-79 kèm theo cái link figma. Thế nên là hãy dựa vào 2 thông tin mới rồi update lại 73 và 74 nhé

**Claude:** Đã đọc FRS BBA-79 (Signed-off). Không mở được link Figma: tài khoản Figma đang kết nối không có quyền vào file (lỗi "don't have edit access"). Chưa sửa tài liệu; nêu hướng sửa theo mẫu BBA-79 và xin quyền / ảnh xuất từ Figma.

---

## 25/11/2026 — BBA-73, BBA-74 theo khung BBA-79 (không dùng Figma)

**User:**
> Không cần phải xem trong Figma đâu

**Claude:** Viết lại BBA-73, BBA-74 theo khung FRS BBA-79 (Signed-off), vẫn tiếng Việt.
- BBA-73: US-001 Xem và xuất thông tin đưa / đón (tìm, lọc Centre / lớp / ngày, ảnh lúc đưa và lúc đón, trẻ đang ở trường, xuất theo khoảng ngày, mục 8 cột xuất); US-002 Ghi và sửa trên SMS (không cần lý do / duyệt, không giới hạn thời gian như BBA-79; giữ các quy tắc người đưa / người đón và giờ).
- BBA-74: US-001 Xem lần đo (tab Temperature, lọc Brand / Centre / lớp / ngày, tìm tên, mỗi lần đo một dòng, x of 3, ≥37.5 tô đỏ); US-002 Thêm / sửa / xóa / View audit (thêm từ dòng điểm danh hoặc tab; Measurement method Manual / Device; sửa xóa không cần lý do; giữ 36.0–40.0, Extra cần lý do, giờ hợp lệ). Bỏ cấu hình Round và bỏ "lý do bắt buộc" của bản V13.
- Không đụng Plane. Chưa đẩy Drive / Git.

---

## 26/11/2026 — Update BBA-73, BBA-74 (khung BBA-79)

**User:**
> Update lên drive nhé

**Claude:** Drive không có sửa mới. Upload BBA-73 (1Wggw3KEZeFsP3LLHMGoSbWiRcz13yEgN) và BBA-74 (19CDqUSUd-nH8byRIh8zffQ6AZq15RMHM) vào thư mục 1uZpPo7…, file cũ vào thùng rác, commit Git. Không cập nhật Plane.

## 26/11/2026 — Quay lại BBA-72 và BBA-67 (trong lúc chờ duyệt 73, 74)

**Hỏi:** BBA-67 mô tả tổng quan các tab trong hồ sơ trẻ dựa vào zip FRS đã duyệt, có mô tả quyền sửa / Edit nếu tab có, viết tiếng Việt. BBA-72 (lên lớp): đọc folder SRS trên Drive; FRD chỉ mô tả tổng quát, nghiệp vụ để ở BR và VAL. Nghiên cứu ems.help.dotb.vn để bổ sung.

**Trả lời:**
- BBA-67: file mới `BBA-67_Child_Record_Tabs_VI.md` — 9 US cho 9 tab (Enrolment, Enrichment, Guardians, Attendance, Finance, Health, Communication, Documents, History), mỗi tab: nội dung tổng quan + thao tác theo quyền + module sở hữu; chi tiết trỏ sang BBA-66/68/69/70/71/73/74. Theo góp ý chị Hải: liệt kê đủ tab của prototype, bỏ "Mô tả của task", Enrolment = lịch sử quá trình ghi danh. OQ-01: tab Communication có nhắn tin trực tiếp (prototype có Reply/Send, bản cũ ghi chỉ đọc). OQ-02: chặn gỡ Primary contact duy nhất?
- BBA-72: viết lại FR ngắn (8 FR), nghiệp vụ dồn vào 14 BR / 4 VAL; giữ chỉnh sửa trên Drive (tiêu đề, US-001, FR-003, version 0.1); bổ sung từ SRS Children & Families (mã lớp duy nhất trong Centre + năm học, lớp có trẻ chỉ đóng không xoá); OQ-06: SRS P6 cho đổi lớp đích từng trẻ.
- ems.help.dotb.vn: không đọc được từ môi trường cloud (proxy chặn / không phân giải được tên miền).
- Chưa đẩy Drive / Git tài liệu, chờ "update".

## 26/11/2026 — Hỏi về BR-010 của BBA-73

**Hỏi:** "Giờ đến đi cùng người đưa, giờ về đi cùng người đón. Chỉ ghi được thông tin đón khi đã có thông tin đưa; giờ về không sớm hơn giờ đến." — không hiểu.

**Trả lời:** BR-010 (US-002) gộp 3 quy tắc khi ghi/sửa trên SMS: (1) có giờ thì phải có người (VAL-004, AC-017); (2) phải có thông tin đưa trong ngày mới ghi được thông tin đón (VAL-005, AC-018); (3) giờ về bằng hoặc sau giờ đến (VAL-006, AC-019). Ý (2), (3) là BA suy luận, không có trong Excel / V13 / BBA-79. Đề xuất viết lại thành 3 gạch đầu dòng; chờ user chọn giữ hay bỏ ý (2), (3).

## 26/11/2026 — Viết lại BR-010 BBA-73 cho dễ hiểu

**Hỏi:** Ghi lại BR-010 cho dễ hiểu.

**Trả lời:** BR-010 mới: "Khi nhập thông tin đưa đón: (1) Nhập giờ trẻ đến thì phải chọn ai đưa trẻ đến; nhập giờ trẻ về thì phải chọn ai đón trẻ về. (2) Trẻ chưa có giờ đến thì chưa nhập được giờ về. (3) Giờ về phải sau giờ đến." VAL-005 và AC-018 đổi thông báo thành "Trẻ chưa có giờ đến, chưa nhập được giờ về." Chỉ sửa repo, chưa đẩy Drive.

## 26/11/2026 — Không tự ý bịa

**Hỏi:** "Với đừng tự ý bịa ra"

**Trả lời:** BBA-73: BR-010 chỉ còn "Nhập giờ trẻ đến thì phải chọn ai đưa trẻ đến; nhập giờ trẻ về thì phải chọn ai đón trẻ về."; bỏ quy tắc tự suy (phải có giờ đến mới nhập giờ về; giờ về sau giờ đến) cùng VAL và AC tương ứng; đánh số lại (6 VAL, 18 AC). BBA-67: bỏ chi tiết tự suy (Export theo bộ lọc, nhãn chờ trả lời mất sau khi gửi). Chưa đẩy Drive.

## 26/11/2026 — BR-010 BBA-73 theo câu của user

**Hỏi:** "Nhập thông tin điểm danh của trẻ phải có giờ đến và giờ đi và người đưa đón của trẻ"

**Trả lời:** BR-010 = "Nhập thông tin điểm danh của trẻ phải có giờ đến, giờ về, người đưa và người đón của trẻ." VAL-004 = thiếu một trong bốn thông tin thì không lưu; 4 trường đổi thành bắt buộc. Hỏi lại: trẻ mới đến, chưa về thì có lưu được giờ đến trước không.

## 26/11/2026 — Update BBA-72 và BBA-67 lên Drive

**Hỏi:** "Update BBA-72 và 67 lên drive đi"

**Trả lời:** Drive không có sửa mới (72: 22/11 13:27, 67: 18/11). Upload vào thư mục 1uZpPo7…: BBA-72 → 1DcRS8KItpdOTWs_PIS-Cy1N3f20Idmu_ (1 comment chị Hải), BBA-67 → 1ggBSCBBbjINkhn_yep2vQ_UFHZsTX1ed (3 comment chị Hải). File cũ 1VT7dKxX…, 1XvEUZcj… vào thùng rác. Cập nhật _drive.json, commit Git. Không cập nhật Plane. BBA-73 (BR-010) chưa đẩy, chờ user xác nhận.

## 26/11/2026 — BBA-72 điều chỉnh theo comment trên Drive và Excel Q-74-06..Q-74-15

**Hỏi:** Sửa BBA-72 theo comment trên Drive, cập nhật lại toàn bộ; đối chiếu Excel Q-74-06 đến Q-74-15.

**Trả lời:** Comment: (1) bỏ tạo lớp trong luồng — lớp đích phải tạo trước ở Classes bởi người có quyền; chưa có lớp thì báo theo prototype, không tiếp tục; (2) nguồn của "tác động" = bước Impact trên prototype + Q-74-11 (DOTB tự quyết); (3) user đổi Actions → Edit. Excel: Q-74-08 sĩ số chỉ cảnh báo, CD cấu hình; Q-74-09 hoá đơn đã phát hành không void, điều chỉnh bằng credit note; Q-74-10 thread cũ inactive giữ tới khi rời trường; Q-74-12/13 DOTB tự quyết (lỗi từng trẻ, Retry). Câu chưa trả lời → OQ-01 (lên lịch/huỷ, ngày quá khứ), OQ-02 (đóng lớp), OQ-03 (trạng thái đủ điều kiện), OQ-04 (thông báo), OQ-07 (đề xuất lớp đích), OQ-08 (học phí từ ngày nào), OQ-09 (thời điểm chuyển điểm danh/thread). Bỏ các quy tắc không có nguồn: chặn ngày quá khứ, trẻ có thay đổi chờ hiệu lực, tự đóng lớp. Thêm Phụ lục C nguồn đối chiếu. Chưa đẩy Drive.

## 26/11/2026 — Update BBA-72 lên Drive

**Hỏi:** "Update BBA-72 lên nhé còn BBA-73 không cần"

**Trả lời:** Drive không có sửa mới sau lần đọc comment. Upload BBA-72 → 1nc2zHpfVmDJrLh4gmdFZI4fuLgVMrP1L (giữ comment chị Hải ở BR-012; comment của user đã xử lý nên không chuyển). File cũ 1DcRS8KI… vào thùng rác; cập nhật _drive.json; commit Git. BBA-73 không đẩy. Không cập nhật Plane.

## 26/11/2026 — BBA-73 theo file user gửi (FRS_BBA-73…V0.1_VI)

**Hỏi:** (1) BR-004 viết lại dễ hiểu (người đưa không có trong danh sách → chọn Someone else, nhập thông tin); (2) UI thêm "Nhiệt độ đưa / đón", "Lý do khi chỉnh sửa"; (3) US-002 chỉ thêm thông tin, không sửa; mọi lần thêm phải có lý do và qua duyệt.

**Trả lời:** Viết lại BBA-73 từ file user gửi. BR-004 chia 3 trường hợp người đưa + người đón. US-001: thêm cột Nhiệt độ lúc đưa / lúc đón (theo BBA-74) và Lý do (thông tin thêm trên SMS). US-002 đổi thành "Thêm thông tin đưa / đón": chỉ thêm thông tin còn thiếu, không sửa / xoá (BR-008); lý do bắt buộc theo BBA-77 (BR-011, VAL-005); qua duyệt theo BBA-53 / My approvals BBA-52, chỉ ghi nhận khi được duyệt (BR-012); lịch sử có lý do, người duyệt, kết quả (BR-013). Không đưa lại 2 quy tắc tự suy (phải có đưa trước đón, giờ về sau giờ đến). OQ-01: chỉ thêm phần đón khi App đã có phần đưa? OQ-02: hiển thị trạng thái chờ duyệt? Chưa đẩy Drive.

## 26/11/2026 — BBA-73 tách quy tắc người thân và xe bus

**Hỏi:** Tách người thân và bus driver ra riêng, không chung một rule.

**Trả lời:** BR-004 tách thành 3: BR-004 người đưa là người thân / Someone else; BR-005 xe bus (Bus driver đưa, Bus attendant đón, kèm số xe, chỉ khi trẻ đi bus); BR-006 người đón chỉ từ danh sách người được phép đón. Bỏ BR trùng ở US-002, đánh số lại (14 BR). Chưa đẩy Drive.

## 26/11/2026 — Giải thích OQ-01, OQ-02 BBA-73

**Hỏi:** OQ-01 và OQ-02 đọc không hiểu.

**Trả lời:** Viết lại bằng ví dụ. OQ-01: App đã ghi phần đến, chỉ thiếu phần về — SMS cho nhập riêng phần về, hay bắt buộc đủ 4 thông tin? OQ-02: đã gửi duyệt mà chưa duyệt — danh sách chưa hiện gì, hay hiện kèm nhãn "Chờ duyệt"? Đã sửa câu chữ trong file.

## 26/11/2026 — Chốt OQ-01, OQ-02 BBA-73

**Hỏi:** Tài liệu chỉ cho bổ sung, không sửa; câu hỏi về sửa đưa qua BBA-77. OQ-02 không cần, bỏ qua, cứ nhập xong là được.

**Trả lời:** BR-011: chỉ nhập phần còn thiếu, phần đã có giữ nguyên; sau khi thêm phải đủ giờ đến, giờ về, người đưa, người đón; sửa thuộc BBA-77. VAL-004 và 4 trường đổi theo; thêm AC chỉ nhập phần về khi App đã có phần đến. Bỏ OQ-02 và câu "danh sách chưa hiện thông tin mới" ở AC; xoá mục Câu hỏi mở; Phụ lục thành mục 7. Chưa đẩy Drive.

## 26/11/2026 — BR-010/011 BBA-73: chỉ thêm mới

**Hỏi:** BBA-73 chỉ được thêm mới, không xoá hay sửa bất kỳ cái gì, kể cả khi đã có thông tin điểm danh buổi sáng.

**Trả lời:** BR-010 = "Trên SMS chỉ được thêm mới thông tin đưa / đón; không được sửa hay xoá bất kỳ thông tin nào đã có, kể cả khi trẻ đã có thông tin điểm danh buổi sáng." BR-011 chỉ còn: sau khi thêm phải đủ giờ đến, giờ về, người đưa, người đón. Bỏ câu "sửa thuộc BBA-77" khỏi BR-011. Chưa đẩy Drive.

## 26/11/2026 — Update BBA-73 lên Drive

**Hỏi:** "Update nhé"

**Trả lời:** Drive (03:38) là bản user gửi, đã gộp; không có comment. Upload vào thư mục user đã chuyển file tới (18AJ7fN7O118NO3zuQGpF5ZmlaYgtNTJ5) → 1yWEvT7yfDM4k79MhlhsJ7F-Pa4-TTQK6. File cũ 1Wggw3KE… vào thùng rác; cập nhật _drive.json; commit Git. Không cập nhật Plane.

## 26/11/2026 — BBA-67 sửa theo comment trên Drive

**Hỏi:** BBA-67 có comment trong tài liệu, dựa vào đó update; lưu trữ lại các comment.

**Trả lời:** 7 comment của user: Enrolment (xem toàn bộ thông tin nhập học, flag, tạo withdrawal… chuyển sang đúng module không popup, change log vào History); Enrichment (bỏ FR liên kết sang Learning, chỉ hiển thị); Guardians (bảng, thêm / sửa / xoá, xoá cần duyệt, mọi thao tác ghi change log; anh chị em và người được đón thuộc task khác); "gỡ người được đón không cần duyệt — check lại" → bỏ, xoá cần duyệt; Attendance (bảng giờ vào / ra + nhiệt độ, không thêm / sửa / xoá, xe đưa rước chỉ xem); Finance (giữ nguyên); Health (thêm nhiệt độ tại tab và hiển thị trên màn BBA-74, nhiệt độ theo ngày, xem full ở BBA-74; chiều cao cân nặng theo kỳ chỉ xem; thông tin phụ huynh không sửa, chỉ thêm / sửa ghi chú nhân viên). Gộp sửa tay trên Drive ("sức khỏe"). Lưu comment ở `_review/sprint4-qa/by-frd/BBA-67/drive-comments.md|json` (kèm 3 comment chị Hải từ bản trước) để gắn lại khi update. Chưa đẩy Drive.

## 26/11/2026 — Update BBA-67 lên Drive

**Hỏi:** "Update"

**Trả lời:** Drive không có sửa mới (07:11). Upload BBA-67 → 1orjPYgyLluEavRwohAtTvb9euq3AfUAt, gắn lại 10 comment (7 của user, 3 của chị Hải). File cũ 1ggBSCBB… vào thùng rác; cập nhật _drive.json; commit Git. Không cập nhật Plane.

## 26/11/2026 — BBA-72 gom 1 US, tập trung lên lớp toàn bộ trẻ

**Hỏi:** Gom các US của BBA-72 thành 1 (đặt tên hợp lý); tập trung đưa toàn bộ trẻ lên lớp, bỏ qua tác động.

**Trả lời:** Drive không có sửa / comment mới. Gom thành "US-001 - Lên lớp cả lớp" (6 FR, 10 BR, 2 VAL, 15 AC): mở từ Edit › Move children up → chọn lớp đích có sẵn + ngày hiệu lực → toàn bộ trẻ chọn sẵn, bỏ chọn trẻ ở lại → Done → kết quả từng trẻ, Retry → lịch sử. Bỏ phần Impact (học phí, hoá đơn, thread, danh sách điểm danh) — đưa vào Ngoài phạm vi; bỏ OQ-08, OQ-09. Giữ cảnh báo sĩ số, giữ quy tắc lớp cũ vẫn giữ danh sách trẻ (comment chị Hải). Chưa đẩy Drive.

## 26/11/2026 — Update BBA-72 (1 US) lên Drive

**Hỏi:** "Update BBA-72 lên drive nhé"

**Trả lời:** Drive không có sửa mới. Upload → 1QB6mSpPzkWOr7TKJQOcSCLxPq8Tfi3YU (gắn lại comment chị Hải ở BR-009). File cũ 1nc2zHpf… vào thùng rác; cập nhật _drive.json; commit Git. Không cập nhật Plane.

## 26/11/2026 — Tên US BBA-72

**Hỏi:** "Lên lớp cả lớp" có từ nào hay hơn không?

**Trả lời:** Gợi ý: (1) Lên lớp hàng loạt cuối năm học (đề xuất — khớp "bulk promotion" và "annual promotion"); (2) Chuyển cả lớp lên level mới; (3) Lên lớp đầu năm học mới; (4) Chuyển lớp theo năm học. Chờ user chọn, chưa sửa file.

## 26/11/2026 — BBA-67 US-002 UI theo wireframe

**Hỏi:** Update UI ở US-002 của BBA-67 theo file wireframe-BBA-67-health.html; không update US khác.

**Trả lời:** Chỉ sửa US-002 (tab Enrichment): bảng cột Programme, Centre, Day, From, To, Start date, End date, Status; Status Waiting / Active / Completed / Withdrawn; lớp Waiting lên đầu, ô lịch và ngày "—"; tiêu đề + dòng phụ + tóm tắt "n programmes · n Waiting · n active"; bỏ khối Waiting for HQ to confirm riêng. Sửa kèm BR-005, BR-006, luồng thay thế, AC-004 trong US-002 cho khớp. Wireframe ghi "Waitting" — dùng "Waiting". Các US khác không đụng. Chưa đẩy Drive.

## 26/11/2026 — Update BBA-67 lên Drive (US-002 UI + sửa của user)

**Hỏi:** "update lên drive"

**Trả lời:** Drive có sửa mới 09:38 và comment mới "Cái này cần làm rõ" ở BR-002. Gộp sửa của user: bỏ tác nhân Read-only User; rút gọn User Story US-001; FR-003 "từ tab Enrolment"; bỏ "không mở popup" ở luồng thay thế; xoá link prototype ở UI Reference (Enrolment, Guardians, Attendance); FR-005 "đã đăng ký"; bỏ câu nhắc tiêm chủng ở BR-019; bỏ "vai trò khác chỉ đọc" ở BR-022; "xoá" → "xóa". Làm rõ BR-002 theo prototype (3 flag Yes / No; Staff Child gắn Staff child discount; SUG / KA chưa có quy tắc tính phí) + OQ-03 (ý nghĩa SUG / KA, Staff Child có tự áp giảm giá không). Upload → 1hcaY9mOxw-jwL74_u39yHwrm0WlHPuCc, gắn lại 7 comment đang mở (comment đã resolve không gắn lại). File cũ 1orjPYgy… vào thùng rác; commit Git. Không cập nhật Plane.

## 27/11/2026 — BBA-72 bỏ phần liên quan Bus

**Hỏi:** "Tài liệu BBA-72 — liên quan đến Bus bỏ ra nha"

**Trả lời:** BBA-72 (repo và bản Drive) không có nội dung nào về Bus — "bus" chỉ khớp chữ "Business Analysis". Bus có ở BBA-73 (Bus driver / Bus attendant, BR-005) và BBA-67 (xe đưa rước ở tab Attendance). Hỏi lại user muốn bỏ ở tài liệu nào. Đồng thời gộp sửa của user trên Drive BBA-72 (08:11) vào repo: tên US "Chuyển cả lớp lên level mới", lớp đích/nguồn → lớp mới/hiện tại, BR-002 bỏ phần Graduation, xoá link prototype ở UI Reference, OQ còn 2, bỏ Phụ lục C. Chưa đẩy Drive.

## 27/11/2026 — BBA-73 bỏ phần Bus

**Hỏi:** "À BBA 73 tao nhầm" — bỏ nội dung liên quan Bus ở BBA-73.

**Trả lời:** Gộp trước sửa của user trên Drive (04:18): bỏ cột "Bắt buộc" ở bảng UI US-001; BR-010 rút còn "Trên SMS chỉ được thêm mới thông tin đưa / đón;". Bỏ Bus: xoá BR xe bus (Bus driver / Bus attendant), bỏ "số xe bus" ở cột Quan hệ, bỏ phần Lucas đi bus ở AC-005, bỏ Bus driver / Bus attendant ở ô chọn người đưa / người đón và AC người đón, bỏ "dịch vụ xe bus" ở phụ thuộc. Đánh số lại còn 13 BR. Chưa đẩy Drive.

## 27/11/2026 — BBA-73 bỏ phần lọc

**Hỏi:** "Phần lọc bỏ luôn nha"

**Trả lời:** Bỏ lọc theo Centre, lớp, ngày, kết quả điểm danh ở BBA-73: FR-002 chỉ còn tìm theo tên / mã trẻ; bỏ 3 ô Centre, Class, Date ở UI; sửa mục đích, phạm vi, vai trò, mục 5, User Story, luồng chính; AC-001 bỏ mặc định Centre / ngày; AC-002 chỉ tìm theo tên; AC-010 không còn chọn ngày. Giữ ô Search. Chưa đẩy Drive.

## 27/11/2026 — BBA-73 khôi phục phần lọc

**Hỏi:** "Quay lại bản cũ đi. Phần lọc bỏ đi cái lọc của bus và các thông tin liên quan đến bus."

**Trả lời:** Khôi phục phần lọc như trước (Centre, lớp, ngày, kết quả điểm danh; 3 ô Centre, Class, Date; AC-001, AC-002, AC-010 như cũ). Bộ lọc của BBA-73 không có lọc Bus; các thông tin Bus khác đã bỏ ở lần trước — trong tài liệu không còn chữ "bus". Chưa đẩy Drive.

## 27/11/2026 — Update BBA-73 lên Drive

**Hỏi:** "Update"

**Trả lời:** Drive BBA-73 không có sửa mới. Upload vào thư mục 18AJ7fN7… → 1kOM9okrdUJv8d5hcSkAqE00NjGvsj4il (đã bỏ Bus, giữ lọc, gộp sửa của user 26/11). File cũ 1yWEvT7y… vào thùng rác; cập nhật _drive.json; commit Git. BBA-72 (đã gộp sửa của user trên Drive 08:11) chưa đẩy, chờ user. Không cập nhật Plane.

## 27/11/2026 — Dịch BBA-73, BBA-74 sang tiếng Anh

**Hỏi:** Dịch BBA-73 và BBA-74 sang tiếng Anh vào folder 1KqkgghHymUu7T9_xco51AIjnoSufVg7_; từ ngữ dễ hiểu, thuật ngữ mảng giáo dục.

**Trả lời:** Kiểm tra Drive: BBA-73, BBA-74 bản VI không có sửa mới. Dịch từ bản VI mới nhất (BBA-73 đã bỏ Bus, giữ lọc). Thuật ngữ: drop-off / pick-up, drop-off adult / pick-up adult, authorised collector, still at the centre, temporary withdrawal, Centre Director, reading, Round. Thông báo lỗi tiếng Việt trong BBA-74 (VAL-003, VAL-005) dịch sang tiếng Anh. Upload: BBA-73 EN → 1Rv-0WXAja-i9VAYcCBhPpc2mx8cWGgX5; BBA-74 EN → 1pkPY5goMoaroCHf3upHuCtoHDGFKkUP1. Bản VI giữ nguyên. Commit Git. Không cập nhật Plane.

## 27/11/2026 — BBA-67 rút còn 5 tab, Enrolment / Enrichment theo wireframe

**Hỏi:** BBA-67 chỉ mô tả 5 tab Enrolment, Enrichment, Attendance, Finance, Communication. Tab Enrolment theo file HTML (bỏ phần Flag). Tab Enrichment theo HTML, mô tả luôn UX/UI.

**Trả lời:** Drive BBA-67 không có sửa mới. Bỏ US Guardians, Health, Documents, History; còn 5 US (Enrolment, Enrichment, Attendance, Finance, Communication); Guardians / Health / Documents / History và Flag đưa vào Ngoài phạm vi; bỏ OQ về guardian và flag. Enrolment theo wireframe: bảng Enrolments (Centre, Level, Class, Programme, Academic year, Enrolled on, Start date, End date, Status, Legal entity), Status Active / Transferred / Completed, tóm tắt "n enrolments · n running now", nút "⋯" (Start withdrawal / temporary withdrawal / transfer) chỉ hiện với người có quyền, chuyển sang Joining & leaving, ghi change log; không mô tả Flag. Enrichment: thêm mục UX / UI (bố cục, tóm tắt bên phải, tên Programme đậm, dòng Waiting nền nhạt, badge Waiting vàng / Active xanh / Completed, Withdrawn xám, không thao tác, định dạng ngày giờ). Finance giữ nguyên. 11 FR, 16 BR, 19 AC. Chưa đẩy Drive.

## 27/11/2026 — Update BBA-67 (5 tab) lên Drive

**Hỏi:** "Update BBA-67 lên drive nhé"

**Trả lời:** Drive không có sửa mới. Upload → 1ymK7zSO_K0TiISFcJz5WGfWcWBZPH4Cf, gắn lại 3 comment còn liên quan (Attendance của user; "Dư thừa", "Liệt kê đủ các tab" của chị Hải); 4 comment về Guardians, Health, xóa người giám hộ, Flag không gắn lại vì nội dung đã bỏ (lưu ở drive-comments.md). File cũ 1hcaY9mO… vào thùng rác; cập nhật _drive.json; commit Git. Không cập nhật Plane.

## 27/11/2026 — BBA-72 check số thứ tự sau khi user sửa trên Drive

**Hỏi:** BBA-72 vừa cập nhật trên Drive, check lại số thứ tự đánh số.

**Trả lời:** Gộp sửa của user (09:21): tên "Bulk Class Promotion"; bỏ Class Viewer; FR-005 chỉ hiển thị số lượng trẻ đã chuyển; bỏ Retry; BR-001, BR-008, BR-009, BR-010 rút gọn; bỏ AC-014 cũ (Retry); bỏ mục Câu hỏi mở, Phụ lục thành mục 7. Đánh số lại: chỉ AC-015 → AC-014 (bị hở sau khi xóa AC-014). FR-001..006, BR-001..010, VAL-001..002, DATA-001..002, AC-001..014 liên tục; luồng 1..n và mục 1..7 đúng. Sửa 3 lỗi gõ nhỏ ("số lượng số lượng", thiếu dấu ";" ở AC-011, dấu ";" thừa ở AC-013). Chưa đẩy Drive.
