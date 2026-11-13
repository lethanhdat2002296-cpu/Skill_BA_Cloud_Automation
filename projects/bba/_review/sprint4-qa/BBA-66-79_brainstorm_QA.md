# Brainstorm — Câu hỏi làm rõ SMS Sprint 4 (BBA-66 đến BBA-79)

> Bản nháp để review, **chưa đưa lên Drive / Git**. Ngày 13/11/2026.
> **Nguồn:** file `BBA_SMS_S4_Tổng hợp câu hỏi phản hồi.xlsx` (105 câu; Đã chốt 40 · DOTB tự quyết 17 · Một phần / cần hỏi lại 19 · Chưa phản hồi 29; phản hồi ghi ngày 09/11/2026) + câu trả lời trên Plane (BBA-528, 529 ngày 12/11; BBA-1058, 1059 ngày 13/11) đã dùng ở bước trước.
> **Quy tắc:** chỉ dùng dữ kiện trong nguồn. "DOTB tự quyết" → ghi rõ quyết định của DOTB trong FRD (không phải câu trả lời của BBA). Chưa có câu trả lời → giữ / thêm OQ.
> **Mâu thuẫn:** khi file (09/11) và Plane (12–13/11) nói khác nhau, bản nháp theo **Plane (mới hơn)** và ghi OQ để BBA xác nhận.

Mã câu hỏi trong file ↔ ticket: Q-66 = BBA-66 · Q-67 = BBA-67 · Q-69 = BBA-68 · Q-70 = BBA-69 · Q-71 = BBA-70 · Q-73 = BBA-71 · Q-74 = BBA-72 · Q-75 = BBA-73 · Q-76 = BBA-74 · Q-77 = BBA-75 · Q-80 = BBA-76 · Q-81 = BBA-77 · Q-86 = BBA-78 · Q-90 = BBA-79.

---

## 1. Bối cảnh & mục tiêu (chung)
- Năm học **tháng 1 – tháng 12**, 4 term; lập lớp năm sau vào tháng 11–12 (Q-74-07, Q-73-12).
- Phase 1 chỉ có Singapore và Malaysia, cùng múi giờ UTC+8 (Q-80-08).
- Singapore: điểm danh là bằng chứng với ECDA; e-Form 1 gửi ECDA theo lô **12:00 trưa**; 1 lượt check-in trong tháng là đủ điều kiện subsidy; kiểm tra ngày 18 (Q-81-07, Q-75-08, Q-67-06).
- BBA không muốn spam email phụ huynh: cái gì cần email thì người tạo chọn, còn lại qua app (Q-73-08).

## 2. Người dùng & vai trò (thay đổi so với hiểu biết trước)
| Nội dung | Nguồn |
|---|---|
| Hiện **không có vai trò nào không có quyền Health**; HQ xem Health của trẻ ở mọi Centre | Q-69-05 |
| Biểu tượng cảnh báo y tế: **ai cũng thấy** | Q-66-12 |
| Height / weight: Teacher thao tác lớp mình; CD và School Admin mọi trẻ | Q-71-10 |
| Consent: CD tạo và gửi theo lớp hoặc cả Centre; GV chỉ thấy lớp mình | Q-73-04 |
| Void điểm danh: ai cũng gửi yêu cầu; Admin, CD, Senior Teacher được CD chỉ định duyệt và tự void không cần duyệt | Q-81-03, Q-75-08 |

## 3. Từng ticket — đã chốt / DOTB tự quyết / còn mở → tác động FRD

### BBA-66 Child record Overview (Q-66)
| Loại | Nội dung | Tác động FRD |
|---|---|---|
| Đã chốt | Payment method **thuộc hồ sơ trẻ**: GIRO, GIRO CDA hoặc PayNow; mỗi invoice mang phương thức này; một trẻ có thể có 2 tài khoản GIRO (CDA và non-CDA), **invoice CDA và non-CDA xuất riêng** (Q-66-09) | Sửa FR-013, FR-014; đóng OQ-OVW-08 phần nguồn |
| Đã chốt | Người không có quyền Health vẫn thấy biểu tượng cảnh báo (Q-66-12) | Khớp FR-006 |
| Một phần | Định danh trẻ = **số giấy khai sinh hoặc hộ chiếu**; chặn hay chỉ cảnh báo khi trùng chưa rõ (Q-66-14) | FR-026 (trùng tên + ngày sinh) cần bổ sung khoá định danh → OQ |
| Cần hỏi lại | Owner — BBA chưa hiểu câu hỏi (Q-66-11) | Giữ OQ-OVW-03, hỏi lại kèm ảnh |
| Chưa phản hồi | Payment method sửa được hay chỉ hiển thị (Q-66-10) | OQ mới |

### BBA-67 Child record tabs (Q-67)
| Loại | Nội dung | Tác động FRD |
|---|---|---|
| Đã chốt | Enrichment: trẻ đang học chưa có end date; end date chỉ có khi dừng / rút (qua app, không hoàn tiền, ghi ngày và lý do); đổi chương trình = rút + đăng ký mới, báo trước 1 tháng; rút khỏi trường thì ngưng invoice enrichment (Q-67-05) | Tab Enrichment: End date "—" khi đang học; hiện lý do khi đã rút |
| DOTB tự quyết | Tab Attendance mặc định **tháng hiện tại** của enrolment đang hiệu lực, có bộ chọn khoảng ngày (Q-67-06) | Ghi quyết định DOTB |
| Đã chốt | Communication: Announcements, Messages (thread lớp; lên lớp → thread mới, thread cũ chỉ đọc), Inquiries, Surveys + consents, Notifications (Q-67-08) | Đối chiếu US-005 sau |
| Chưa phản hồi | Communication nhóm theo Enrolment / Centre? (Q-67-04) | OQ |

### BBA-68 Medical alert banner (Q-69)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Cảnh báo **sinh tự động** (Q-69-02); nguồn Health + Allergies SMS và Parents App (Q-69-03) | Khớp |
| Đã chốt | Critical = medical condition hoặc allergy; phụ huynh bỏ đánh dấu được (Q-69-01) | Không sửa định nghĩa critical (theo yêu cầu trước của user) |
| Đã chốt | Không có vai trò nào thiếu quyền Health (Q-69-05) | FR-012 (vai trò bị ẩn) chỉ là cấu hình dự phòng → ghi chú |
| DOTB tự quyết | Thứ tự, độ dài, mở xem toàn bộ (Q-69-06) | Giữ FR-003, FR-010 |
| **Mâu thuẫn** | File Q-69-08 (09/11): sửa trên Parents App **đồng bộ ngay, không duyệt** ↔ Plane BBA-1058 (13/11): **chỉ áp sau khi CD / Admin đánh giá** | Giữ theo Plane; OQ-MAB-09 ghi cả hai nguồn |

### BBA-69 Allergies list (Q-70)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Không giới hạn số dị ứng / bệnh (Q-70-02) | BR mới |
| Đã chốt | Thang chính thức trên form: **Mild, Moderate, Life Threatening**; Life Threatening lên đầu; form có thể tuỳ theo brand / Centre (Q-70-03) | Ghi Life Threatening = Severe (giữ tên Severe trên UI); cấu hình theo brand → OQ |
| Đã chốt | **Chưa khai báo ≠ đã khai báo không dị ứng**; Health info bắt buộc; trẻ chưa sinh bỏ qua, hệ thống nhắc admin gần ngày nhập học (Q-70-09) | FR mới: trạng thái "Not provided" |
| Đã chốt | Staff không ghi đè thông tin phụ huynh (Q-70-10) | Khớp BR-001 |
| DOTB tự quyết | Mô hình dữ liệu (Q-70-01), cách sắp xếp (Q-70-04), export / audit (Q-70-11) | DOTB: giữ chữ tự do + mức độ; mỗi trẻ một dòng; không lưu nhật ký (khớp Plane BBA-1058) |
| Chưa phản hồi | Cột Reaction / Action Plan / EpiPen (Q-70-05); condition chung danh sách (Q-70-06); kênh cho bếp (Q-70-07); đồng bộ (Q-70-12) | Giữ OQ |

### BBA-70 Growth (Q-71)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Term **do HQ đặt theo brand**, Centre không sửa; 4 term, bắt đầu 1/1, ngày đổi theo năm (vd Schoolhouse T1 2/1–15/3, Agape T1 2/1–10/3); nhắc **giữa tháng cuối mỗi term** (Q-71-03) | Sửa FR-001, FR-011 |
| Đã chốt | Đơn vị cm, kg (Q-71-05); **mọi trẻ** của lớp (Q-71-06); một lần mỗi term + **Measurement history** (Q-71-07); Change record có "Updated By" (Q-71-08); Teacher lớp mình, CD và Admin mọi trẻ (Q-71-10) | Khớp / sửa BR-005 |
| DOTB tự quyết | Lưu cả lớp khi có dòng lỗi (Q-71-09) | DOTB: lưu dòng hợp lệ, dòng lỗi giữ lại kèm báo lỗi |
| **Mâu thuẫn** | File Q-71-02 (09/11): **bỏ BMI và percentile, chỉ cần height + weight** ↔ Plane BBA-1059 (13/11): gửi chuẩn biểu đồ SG / MY | Giữ biểu đồ theo Plane; OQ ghi cả hai |
| Chưa phản hồi trong file | Phụ huynh thấy gì (Q-71-11), báo cáo HQ (Q-71-12) | Đã có trả lời trên Plane BBA-1059 Q4, Q5 |

### BBA-71 Consent (Q-73)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Loại và vòng đời: Privacy policy, Medical authorisation, Media — **một lần lúc nhập học, không hết hạn** (media khác nội dung theo brand); Field trip / learning journey và ad hoc — **theo từng chuyến / sự kiện, có ngày đóng**; Crossroad — **chỉ Singapore, Centre không có sân ngoài trời, gia hạn hằng năm** (Q-73-04, Q-73-12) | Sửa FR-001, FR-007 |
| Đã chốt | **CD tạo consent và gửi theo lớp hoặc cả Centre, có ngày đóng**; GV chỉ thấy lớp mình (Q-73-04); tạo consent phải có **Announcement kèm link**; email chỉ khi người tạo chọn (Q-73-08) | Sửa FR-003; bỏ "email tự động cho phụ huynh chưa có app" |
| Đã chốt | Người nhận mặc định cả hai phụ huynh; mỗi trẻ cấu hình "cả hai" hay "chỉ người liên hệ chính" (Q-73-07) | FR mới |
| Đã chốt | Phụ huynh trả lời trong app → kết quả về SMS và **tự tick Consent trong checklist học sinh** (Q-73-08) | FR mới |
| Đã chốt | Nhiều request mở cùng lúc cho cùng trẻ và loại (mỗi request gắn một sự kiện) (Q-73-14) | Sửa FR-001 |
| Đã chốt | Rút media / data consent bằng văn bản; trẻ không có media consent → chặn hoặc cảnh báo khi tag; Marketing phải biết (Q-73-13) | Khớp BR-005 |
| DOTB tự quyết | Đếm lần nhắc; **thẻ tổng quan "đã trả lời / tổng", bấm vào chỉ hiện người chưa trả lời; bộ lọc consent** (Q-73-10); bằng chứng lưu (Q-73-15) | FR mới (theo mong muốn BBA nêu) |
| Một phần | Form đăng ký cần 2 chữ ký; consent gửi sau cần 1 hay 2 phụ huynh chưa rõ (Q-73-06) | OQ |
| Chưa phản hồi | Nhắc tự động / giới hạn (Q-73-09); phiên bản (Q-73-11) | Q-73-11 đã có Plane BBA-488 (tuỳ từng lần) |

### BBA-72 Bulk promotion (Q-74)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | 3 luồng khác nhau: **annual promotion** (cuối năm, cả lớp), **Infant promotion** (bất kỳ lúc nào, từng trẻ, 18 tháng tuổi), **class change** (đổi lớp cùng level). **K2 graduation = mass withdrawal** (reason graduation), chỉ K2 rời vào tháng 12 (Q-74-01, Q-74-06) | Ticket này = annual promotion; đóng OQ-05 |
| Đã chốt | Chỉ **trong cùng Centre**; khác Centre / brand là Transfer (Q-74-02) | BR mới |
| Đã chốt | Chọn cả cohort, **bỏ tick ngoại lệ**; trẻ ở lại giữ lớp hoặc chuyển lớp khác cùng level (Q-74-03 / 05) | Khớp FR-003 |
| Đã chốt | Capacity linh hoạt (vd tối đa 24 vẫn nhận em thứ 25); CD cấu hình sĩ số từng lớp (Q-74-08) | Khớp BR-003 |
| Đã chốt | Không void hoá đơn đã phát hành, sửa bằng credit note (Q-74-09) | Khớp BR-002 |
| Đã chốt | Lên lớp → **tạo thread mới** cho lớp mới; thread cũ **chỉ đọc**, giữ tới khi trẻ rời trường (Q-74-10) | Sửa FR-005 |
| DOTB tự quyết | Preview, lỗi từng phần, chạy lại (Q-74-11 / 12 / 13) | Ghi quyết định DOTB |
| Còn mở | Effective date mặc định / huỷ trước hiệu lực (Q-74-07); fee scheme áp từ ngày nào (Q-74-09); roster điểm danh chuyển khi nào (Q-74-10); thông báo, đóng lớp cũ (Q-74-15); trạng thái đủ điều kiện (Q-74-06) | Giữ / thêm OQ |

### BBA-73 Handover (Q-75)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Check-out chỉ người đã duyệt, **không override**; người lạ → Centre gọi phụ huynh, phụ huynh điền đủ thông tin ngay, rồi người đó mới được đón (Q-75-02, Q-75-04) | Sửa FR-004 (hướng dẫn) |
| Đã chốt | Check-in: người giao có thể ngoài danh sách (tài xế xe, người giúp việc) (Q-75-02) | Khớp FR-001 |
| Đã chốt | Xe đưa đón: bộ lọc theo xe chỉ để gom; **check-in / out từng trẻ, ảnh riêng từng trẻ**; người giao là **tài xế**, người nhận về là **phụ xe** (Q-75-10) | **Sửa FR-008** (bỏ nhận cả nhóm) |
| Đã chốt | Parents App hiện **ảnh lúc giao nhận** (Q-81-02) | FR mới: ảnh |
| DOTB tự quyết | Cách hiện ô nhập tay ở check-in (Q-75-02) | DOTB: chỉ hiện khi chọn "Someone else" |
| Chưa phản hồi | Lưu ảnh bao lâu, ai xem (Q-75-12) | OQ |

### BBA-74 Temperature (Q-76)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Thang không cần dưới 36, phải lên 39–40; **mặc định 36.5, hiện sẵn dải 36.3–36.7 để bấm**; nút ghi **"Enter manually"** (Q-76-05) | Sửa FR-001 |
| Đã chốt | Được sửa số đọc từ nhiệt kế Bluetooth (Q-76-06) | Sửa FR-003 |
| Đã chốt | **Một số Centre** đo 3 lần: arrival, **sau ngủ trưa**, lúc về; CD có nút "add temperature" (Q-81-02) | "3 lần" không bắt buộc mọi Centre → OQ-06 có thêm dữ kiện; "Before nap" → **"After nap"** |
| Còn mở | Nhập tay ngoài khoảng: cảnh báo hay chặn (Q-76-05) | Giữ AS / OQ |

### BBA-75 Late flag (Q-77)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Giờ chốt theo Centre, **có giờ chốt buổi sáng và buổi chiều** (vd sau 9:15 sáng, sau 12:15 chiều); tính theo **giờ ghi nhận ở cổng**, không phải giờ đồng bộ (Q-77-03) | **Sửa FR-001, FR-002**; đóng OQ-01 |
| Đã chốt | Late không nhập tay, tự gắn (Q-81-02) | Khớp BR-001 |
| DOTB tự quyết | Dữ liệu offline / backdated tự tính lại (Q-77-04) | Khớp FR-005 |
| Một phần | "Ở Singapore" chỉ nhân viên thấy — Malaysia? (Q-77-05) | OQ |
| Chưa phản hồi | Màn hiển thị (Q-77-06), override (Q-77-07), đổi cấu hình (Q-77-08) | Giữ OQ / AS |

### BBA-76 Overview today (Q-80)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Temporary withdrawal: không điểm danh, không tính enrolment number, vẫn trong student list (có tag), **ẩn khỏi Attendance app** (Q-80-01, Q-80-03) | Khớp FR-002 |
| Đã chốt | Điểm danh gắn với **bản ghi enrolment**, không gắn hồ sơ trẻ (Q-80-03) | DATA |
| Đã chốt | "Today" theo Centre hay người xem như nhau (UTC+8) (Q-80-08) | Ghi chú |
| Một phần | 3 stream: Main, Early Intervention (Bright Path), Enrichment; đếm trên overview thế nào chưa rõ (Q-80-09) | OQ |
| Còn mở | Nghỉ phép có trừ khỏi expected không (Q-80-03); realtime (Q-80-04); drill-down (Q-80-07); export (Q-80-11) | Giữ / thêm OQ |

### BBA-77 Attendance correction (Q-81)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | **Check-in nhầm phải Void** (gỡ), không dùng check-out để thay (Q-81-01) | OQ-04 trả lời một phần: lượt nhầm → Void |
| Đã chốt | Ai cũng gửi yêu cầu; Admin, CD, Senior Teacher được chỉ định duyệt; chính họ void không cần duyệt (Q-81-03, Q-75-08) | Khớp FR-010, FR-011 |
| Đã chốt | Void check-in đổi trạng thái subsidy và cảnh báo ngày 18; e-Form 1 gửi ECDA ngày có điểm danh thật đầu tiên, lô 12:00 (Q-81-07) | Sửa FR-007 |
| DOTB tự quyết | Bản ghi chưa đồng bộ sửa trên iPad, đã đồng bộ void trên web (Q-81-10) | Khớp BR-005 |
| Còn mở | Sửa sai giờ (không nhầm cả lượt) dùng correction hay void (Q-81-01); danh sách trường được sửa (Q-81-02); reason code (Q-81-05); khoá kỳ (Q-81-09); thông báo phụ huynh (Q-81-08) | Giữ / thêm OQ |

### BBA-78 Daily routines (Q-86)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt | Taidii và file export của BBA có **4 loại: Bottle, Food, Nap, Potty** (Q-86-01) | **Bỏ Mood** đã thêm ở nháp trước → OQ |
| DOTB tự quyết | Trường dữ liệu dùng lại như Taidii (Q-86-02); lỗi từng phần (Q-86-05) | Ghi quyết định DOTB |
| Một phần | Ghi cả lớp: chỉnh ngoại lệ "cả 2" (trước và sau khi lưu) (Q-86-04) | Sửa FR-003; trẻ vắng có áp không → OQ |
| Một phần | Thông báo theo category, có Routines, phụ huynh chọn nhận (Q-86-09) | Sửa FR-012 |
| Chưa phản hồi | Backdated / future (Q-86-06); cài đặt hiện cho phụ huynh (Q-86-08); ghi chú từ gia đình (Q-86-10) | Giữ OQ |

### BBA-79 Staff clock (Q-90)
| Loại | Nội dung | Tác động FRD nháp |
|---|---|---|
| Đã chốt (một phần) | Phase 1 chấm công **tối thiểu**: nhân viên báo có mặt, đo nhiệt độ, cần báo cáo (Q-90-05) | Khớp |
| Chưa phản hồi trong file | Nhiều lượt / ngày (Q-90-05); nhiệt độ vượt ngưỡng (Q-90-07); quên clock-out (Q-90-08); ai sửa (Q-90-09); nhiều Centre (Q-90-10) | Q-90-09 đã có Plane BBA-528 (CD sửa); còn lại OQ |
| DOTB tự quyết | Trùng lượt offline / web (Q-90-12) | Không còn web clock (Plane BBA-528) |

## 4. Rủi ro
| Loại | Nội dung | Mức | Giảm thiểu |
|---|---|---|---|
| Nguồn mâu thuẫn | Health record (Q-69-08 ↔ BBA-1058), Growth chart (Q-71-02 ↔ BBA-1059), Void có / không cần duyệt (Q-75-08 ↔ Q-81-03 — thực ra khớp: người được giao void không cần duyệt, người khác gửi yêu cầu) | Cao | Ghi OQ, hỏi BBA một lần |
| An toàn trẻ | Chờ đánh giá mới hiện dị ứng mới | Cao | OQ-MAB-10 |
| Subsidy / ECDA | Void sau 12:00 khi e-Form 1 đã gửi | Trung bình | OQ khoá kỳ |

## Đề xuất của BA (chưa phải yêu cầu)
- Gửi lại BBA một danh sách ngắn các câu "Một phần / Chưa phản hồi" P0 (29 + 19 câu) kèm ảnh wireframe, ưu tiên: Q-66-11 Owner, Q-73-06, Q-74-07, Q-80-03, Q-81-01/09, Q-86-01 (Mood), Q-90-07/08.
