## Q-66-09 [Đã chốt] P0 · Payment method
Q: Payment method thuộc Child, Family, Guardian, Enrolment hay Billing Account?
A: Payment method thuộc hồ sơ trẻ (Child). Trên hồ sơ trẻ ghi trẻ trả bằng GIRO, GIRO CDA hay PayNow; mỗi invoice mang theo phương thức này để Finance lọc hàng loạt. Một trẻ có thể có 2 tài khoản GIRO (CDA và non-CDA). CDA và non-CDA xuất invoice riêng.
BA: 
Avail: 

## Q-66-10 [Chưa phản hồi] P1 · Quyền sửa payment method
Q: Payment method trên Overview chỉ hiển thị hay được phép sửa (hiện tại không thấy cho chỉnh sửa); nếu sửa thì module nào là nguồn dữ liệu chính?
A: 
BA: 
Avail: 

## Q-66-11 [Một phần / cần hỏi lại] P1 · Owner
Q: Owner được hiểu là người quản lý hồ sơ, hay người phụ trách enrolment; Owner được gán và thay đổi theo quy tắc nào?
A: Em chưa hiểu định nghĩa "owner" ở đây ạ.
BA: Phía trả lời chưa hiểu câu hỏi. DOTB cần giải thích lại Owner là gì (vd: kèm ảnh prototype) rồi hỏi lại.
Avail: 

## Q-66-12 [Đã chốt] P0 · Medical summary
Q: Người không có quyền xem dữ liệu sức khỏe sẽ thấy toàn bộ medical summary, bản tóm tắt, biểu tượng cảnh báo hay không thấy gì?
A: Biểu tượng cảnh báo. BBA nói chỗ icon thì ai cũng được quyền thấy, vì icon sẽ show những cái dị ứng hoặc quan trọng nhất.
BA: Xem thêm Q-69-05: hiện không có role nào không có quyền Health.
Avail: 

## Q-66-14 [Một phần / cần hỏi lại] P1 · Duplicate
Q: Quy tắc phát hiện Child trùng là gì và cảnh báo trùng có cho phép người dùng tiếp tục tạo không?
A: Alan có nói: định danh trẻ = số giấy khai sinh hoặc số hộ chiếu. Phụ huynh định danh bằng NRIC/FIN/MyKad/Passport, trùng định danh thì gộp làm một tài khoản. (kèm link)
BA: Mới có khóa định danh. Chưa trả lời: khi trùng có cho tạo tiếp không (chặn hay chỉ cảnh báo).
Avail: 

## Q-67-04 [Chưa phản hồi] P0 · Tách dữ liệu theo enrolment
Q: Communication có phải được nhóm theo từng Enrolment/Centre để không trộn dữ liệu lịch sử không?
A: 
BA: Q-74-10 có nhắc: lên lớp/đổi lớp thì tạo thread mới, thread cũ inactive, giữ tới khi trẻ rời trường. Chưa nói về nhóm theo Enrolment/Centre.
Avail: 

## Q-67-05 [Đã chốt] P1 · Enrichment
Q: Tab Enrichment cần hiển thị start date và end date. Hiện tại không có end date, vậy thông tin này lấy từ đâu, khi nào có?
A: Trẻ đang học thì chưa có end date. End date chỉ có khi trẻ dừng hoặc rút khỏi chương trình (team Finance nói hôm 9/9). Rút khỏi enrichment đi qua app, không hoàn tiền, ghi ngày kết thúc và lý do. Đổi chương trình (vd piano sang dance) = rút cái cũ + đăng ký cái mới, báo trước 1 tháng. Trẻ rút khỏi trường thì ngưng xuất invoice enrichment.
BA: 
Avail: 

## Q-67-06 [DOTB tự quyết] P1 · Attendance
Q: Tab Attendance mặc định hiển thị khoảng thời gian nào?
A: Team mình tự thiết kế được. Nghiệp vụ BBA chạy theo tháng: ngày 18 kiểm tra trẻ 0 buổi để giữ subsidy SG; CD app có mục "No attendance this month". Đề xuất mặc định là tháng hiện tại của enrolment đang hiệu lực, kèm bộ chọn khoảng ngày.
BA: 
Avail: 

## Q-67-08 [Đã chốt] P1 · Communication
Q: Tab Communication gồm announcement, message, request và notification nào; có loại trao đổi nội bộ nào phải loại trừ không?
A: 1. Announcements: một chiều, không reply/comment; PH hỏi qua chat hoặc inquiry. HQ/CD gửi, GV chỉ xem (cấu hình được). Không cần duyệt, có hẹn giờ đăng. Gửi theo HQ, brand, centre, lớp hoặc nhóm (vd mọi PH K1 ở mọi centre). Đính kèm file, chèn ảnh, có nút bật/tắt gửi kèm email.
2. Messages: thread lớp có sẵn cho mỗi trẻ, PH nói chuyện với tất cả GV lớp và CD trong một cửa sổ. Lên lớp thì có thread mới, thread cũ chỉ đọc, giữ tới khi trẻ rời trường. Group chat riêng gắn theo người (thường cho sự kiện). Chat riêng CD – PH cho việc nhạy cảm, GV không thấy, chỉ CD khởi tạo. Không có chat CD – GV, không có chat nhiều PH nhiều lớp. CD xem được mọi chat GV – PH. Mặc định gửi cả bố và mẹ, bỏ chọn được một người (ly hôn). Malaysia: School Admin được báo mỗi khi GV nhắn PH để kiểm tiếng Anh.
3. Inquiries: ticket cần admin trả lời hoặc form cần điền; PH không tự chọn người nhận. Học phí → admin hoặc CD; Birthday form → GV chủ nhiệm; còn lại → CD và admin. CD và admin luôn thấy mọi inquiry; CD chuyển cho GV được và vẫn theo dõi.
4. Surveys + consents: survey đính kèm file; tạo survey thì có announcement kèm link (vd thông báo dã ngoại rồi survey bé nào đi).
5. Notifications: màn mô phỏng "What guardian sees", có ô "Viewing as guardian". Khối "Needs you" gồm việc PH phải làm (trả tiền, ký consent), chỉ biến mất khi làm xong, không phải khi đã đọc. BBA thích cách chia này; design có thể làm lại cho đơn giản hơn.
BA: Chưa trả lời vế "loại trao đổi nội bộ cần loại trừ" (gián tiếp: không có chat CD – GV).
Avail: 

## Q-69-01 [Đã chốt] P0 · Tiêu chí critical
Q: Tiêu chí nào xác định một thông tin sức khỏe là critical và ai có quyền đánh dấu hoặc bỏ đánh dấu critical?
A: Trẻ có medical condition hoặc allergy như dị ứng đồ ăn, các loại dị ứng, hen suyễn… Dữ liệu do Phụ huynh khai, nên Phụ huynh có quyền bỏ đánh dấu critical.
BA: 
Avail: 

## Q-69-02 [Đã chốt] P0 · Tự động hay thủ công
Q: Medical alert được sinh tự động từ severity/type hay do người dùng chọn thủ công?
A: Được sinh tự động, ví dụ khi lớp có sinh nhật thì có cảnh báo trẻ này dị ứng với sữa.
BA: 
Avail: 

## Q-69-03 [Đã chốt] P0 · Nguồn dữ liệu
Q: Alert lấy dữ liệu từ allergy, dietary restriction, medical condition, medication, family note và staff note nào?
A: SMS có module Health + Allergies. Parents app cũng có module Health. Lấy từ đó.
BA: Chưa nêu rõ từng loại (medication, family note, staff note) có vào alert không.
Avail: 

## Q-69-05 [Đã chốt] P0 · Quyền xem
Q: Người không có quyền Health sẽ thấy biểu tượng cảnh báo, nội dung rút gọn hay không thấy cảnh báo?
A: Đang không có đối tượng nào không có quyền Health. HQ cũng được quyền xem health của trẻ ở cơ sở bất kỳ. Nếu có, chị cho em xin vài ví dụ ạ.
BA: Phía trả lời xin ví dụ – nếu DOTB có case role không có quyền Health thì gửi lại.
Avail: 

## Q-69-06 [DOTB tự quyết] P1 · Nhiều cảnh báo
Q: Khi Child có nhiều cảnh báo, thứ tự, giới hạn độ dài và cơ chế mở xem toàn bộ là gì?
A: Cái này nhà mình tự thiết kế được.
BA: 
Avail: 

## Q-69-08 [Đã chốt] P1 · Cập nhật
Q: Alert cập nhật ngay khi Parent/Staff sửa Health record hay cần review/approval trước?
A: Khi PH sửa Health trên Parents app, dữ liệu tự đồng bộ ngay vào hồ sơ trẻ, không cần duyệt. CD và GV chủ nhiệm nhận notification khi PH update. CD và GV có thể ghi chú thêm; PH không cần thấy các ghi chú này.
BA: 
Avail: 

## Q-70-01 [DOTB tự quyết] P0 · Mô hình dữ liệu
Q: Allergy được lưu dưới dạng bản ghi có cấu trúc hay các trường free text như prototype hiện tại?
A: BBA không có yêu cầu đặc biệt. Nhà mình có thể tự quyết.
BA: 
Avail: 

## Q-70-02 [Đã chốt] P0 · Số lượng allergy
Q: Một Child có bị giới hạn số lượng allergy/condition?
A: Không ạ.
BA: 
Avail: 

## Q-70-03 [Đã chốt] P0 · Severity
Q: Danh mục severity chính thức là gì và có được cấu hình theo Country/Brand không?
A: Xem các form BBA đang dùng trong folder của BBA (có link). Thang severity trên form chính thức có 3 mức: Mild, Moderate, Life Threatening – đủ làm căn cứ sắp "most severe first" (Life Threatening lên đầu). BBA có đề cập form y tế có thể customisable theo từng brand/centre.
BA: Cấu hình theo brand/centre mới ở mức "có thể" – nên xác nhận có cần cấu hình ở Phase 1.
Avail: 

## Q-70-04 [DOTB tự quyết] P0 · Cách sắp xếp
Q: Most severe first được sắp xếp theo severity cao nhất của Child hay mỗi allergy là một dòng độc lập?
A: Nhà mình có thể tự quyết được ạ.
BA: 
Avail: 

## Q-70-05 [Chưa phản hồi] P1 · Trường hiển thị
Q: Các cột bắt buộc có đúng là Child, Class, Allergen, Reaction, Severity, Action Plan và EpiPen Location không?
A: 
BA: 
Avail: 

## Q-70-06 [Chưa phản hồi] P1 · Loại condition
Q: Skin condition, respiratory condition và medical history có nằm chung danh sách Allergy không?
A: 
BA: 
Avail: 

## Q-70-07 [Chưa phản hồi] P0 · Kitchen access
Q: Kitchen staff truy cập trực tiếp hệ thống, nhận bản in hay nhận export riêng; họ được xem dữ liệu nhận dạng nào?
A: 
BA: 
Avail: Allergy view phải đọc nhanh theo Class và toàn Centre, dùng lúc có rủi ro (bữa ăn, sinh nhật, outing). Còn mở: kênh cho Kitchen staff và phạm vi dữ liệu nhận dạng.

## Q-70-09 [Đã chốt] P0 · No allergy và unknown
Q: Hệ thống phân biệt No allergy, Unknown/Not provided và Health profile chưa hoàn thành như thế nào?
A: Health Info / Allergies là bắt buộc, PH phải acknowledge and declare. Hồ sơ chưa khai báo khác với hồ sơ đã khai báo là không có dị ứng. Với trẻ unborn, BBA muốn bỏ qua phần giấy tờ (kể cả allergy), hệ thống nhắc admin liên hệ PH khi gần ngày nhập học. Tức có trạng thái "chưa cung cấp" hợp lệ.
BA: 
Avail: 

## Q-70-10 [Đã chốt] P1 · Nguồn cập nhật
Q: Staff có được sửa dữ liệu do Parent cung cấp hay chỉ được thêm Staff Note; thay đổi có cần review hoặc notification không?
A: Staff không thể ghi đè info do PH cung cấp.
BA: Phần notification/review đã trả ở Q-69-08: không cần duyệt, CD + GV chủ nhiệm nhận noti.
Avail: Parent có thể cập nhật allergy trong app. Còn mở: ai được thông báo, quyền Staff sửa dữ liệu Parent, review.

## Q-70-11 [DOTB tự quyết] P1 · Export và audit
Q: Export/print danh sách allergy có cần hạn chế, watermark hoặc lưu audit không?
A: Nhà mình tự thiết kế được ạ.
BA: 
Avail: 

## Q-70-12 [Chưa phản hồi] P1 · Đồng bộ
Q: Khi allergy thay đổi, danh sách, medical alert và kitchen output được cập nhật ngay hay theo batch/cache?
A: 
BA: Q-69-08 nói dữ liệu PH sửa đồng bộ ngay vào hồ sơ trẻ – có thể suy ra cập nhật ngay, nên xác nhận.
Avail: 

## Q-71-02 [Đã chốt] P0 · Percentile
Q: Nếu triển khai percentile, sử dụng chuẩn tăng trưởng nào theo quốc gia, tuổi và giới tính?
A: YC và Alan có nói không dùng BMI, Percentile thì nice to have thôi. Nên mình bỏ hết 2 cái này. Chỉ cần height + weight là được.
BA: Comment nằm ở cột J (Answer). Mâu thuẫn với ghi nhận cũ trong file (dùng percentile thay BMI) và Q-71-11 (Parent thấy percentile) – cần cập nhật lại file.
Avail: Workflow xác nhận dùng percentile thay BMI nhưng chưa chốt chuẩn (Singapore chart do BBA cung cấp vs WHO).

## Q-71-03 [Đã chốt] P0 · Term calendar
Q: Term được định nghĩa theo Country, Brand, Centre hay dùng bốn term cố định toàn hệ thống?
A: Term do HQ đặt theo Brand, centre không được sửa, mỗi brand một lịch. Năm học có 4 term, bắt đầu 1/1, ngày term đổi theo từng năm (vd Schoolhouse T1 2/1–15/3, Agape T1 2/1–10/3). Height/weight: Singapore đo mỗi term, 4 term/năm. Nhắc nhập vào giữa tháng cuối mỗi term (giữa tháng 3, 6, 9, 12).
BA: 
Avail: 

## Q-71-04 [Chưa phản hồi] P1 · Trường bắt buộc
Q: Có bắt buộc nhập đủ Height, Weight và Measurement Date cùng lúc không?
A: 
BA: 
Avail: 

## Q-71-05 [Một phần / cần hỏi lại] P1 · Đơn vị và validation
Q: Đơn vị, số chữ số thập phân và khoảng giá trị hợp lệ của Height/Weight là gì?
A: cm và kg. Portfolio Brighton K2 2026 ghi "105 cm", "16 kg".
BA: Mới có đơn vị. Chưa có số thập phân và khoảng hợp lệ (có thể DOTB tự đặt).
Avail: 

## Q-71-06 [Đã chốt] P1 · Đối tượng trong lớp
Q: Chỉ Child có mặt trong ngày mới được nhập số đo hay mọi Child đang thuộc lớp đều được hiển thị?
A: Mọi child.
BA: 
Avail: Teacher nhập height/weight cho cả Class trên một màn hình, mọi nhóm tuổi.

## Q-71-07 [Đã chốt] P0 · Một hay nhiều lần đo
Q: Mỗi Child chỉ có một bản ghi mỗi term hay được phép lưu nhiều lần đo?
A: BBA nói đo một lần mỗi term (Singapore) và muốn có "Measurement history" để biết lần đo vào lúc nào.
BA: 
Avail: 

## Q-71-08 [Một phần / cần hỏi lại] P0 · Lịch sử sửa
Q: Nếu sửa hoặc ghi đè số đo, hệ thống có giữ old/new value, người sửa và lý do không?
A: Wishlist Admin yêu cầu "Change Record" của hồ sơ trẻ hiện rõ "Updated By". Height/weight không cần duyệt.
BA: Có người sửa; chưa rõ old/new value và lý do.
Avail: 

## Q-71-09 [DOTB tự quyết] P1 · Lưu cả lớp
Q: Khi lưu cho cả lớp và một Child có dữ liệu lỗi, lưu các Child hợp lệ hay hủy toàn bộ?
A: Nhà mình tự thiết kế. BBA chỉ yêu cầu lưu 1 lần cho cả lớp để tránh click lắt nhắt.
BA: 
Avail: 

## Q-71-10 [Đã chốt] P1 · Quyền thao tác
Q: Vai trò nào được thêm, sửa, xóa số đo; Teacher có chỉ được thao tác trên lớp mình phụ trách không?
A: Teacher thao tác cho lớp mình, CD và school admin cho mọi trẻ. Height/weight không cần ai duyệt.
BA: 
Avail: 

## Q-71-11 [Chưa phản hồi] P1 · Parent visibility
Q: Dữ liệu hiển thị cho Parent ngay sau khi lưu hay sau một bước review; Parent thấy số đo, chart, percentile và BMI nào?
A: 
BA: Gián tiếp: Q-71-08/Q-71-10 nói height/weight không cần duyệt; Q-71-02 bỏ BMI và percentile. Nên xác nhận lại Parent thấy gì.
Avail: Parent thấy height, weight, thay đổi so với kỳ trước, percentile và lịch sử theo ngày đo. Còn mở: hiển thị ngay hay sau review.

## Q-71-12 [Chưa phản hồi] P1 · HQ report
Q: HQ tracking report cần thống kê những gì?
A: 
BA: 
Avail: 

## Q-73-04 [Đã chốt] P1 · Phạm vi áp dụng
Q: Consent Type áp dụng theo Country, Brand, Centre, Class, Programme hay từng Child?
A: Privacy policy, medical authorisation, media consent: thu một lần lúc nhập học, cho từng trẻ, nằm trong registration form. Nội dung media consent khác nhau theo brand (Learning Vision, The Schoolhouse, Small Wonder mỗi brand một đoạn). Field trip / learning journey: theo từng chuyến (Malaysia cũng vậy). Ad hoc theo sự kiện (món ăn, hoạt động). Crossroad: chỉ Singapore, chỉ centre không có sân ngoài trời, gia hạn hằng năm. Lúc gửi: CD tạo consent/survey rồi gửi theo lớp hoặc cả centre, có ngày đóng. GV chỉ thấy lớp mình, CD thấy mọi lớp.
BA: 
Avail: Crossroad consent chỉ áp dụng tại Singapore và centre không có outdoor yard.

## Q-73-06 [Một phần / cần hỏi lại] P0 · Guardian authority
Q: Khi có nhiều Guardian, chỉ cần một Guardian đồng ý hay phải có sự đồng ý của tất cả Guardian có quyền pháp lý?
A: Form đăng ký (T+C, declaration, e-Form 1): BBA chốt bắt buộc 2 chữ ký (bố và mẹ), không ô nào tùy chọn, chữ ký thứ hai không ghi đè chữ ký thứ nhất. Nếu chỉ có một người (đơn thân, mồ côi có người giám hộ) thì người đó ký cả hai ô. Lý do: bố mẹ hay đổ cho nhau "chưa đọc T+C", và joint custody cần cả hai đồng ý. Guardian không phải bố mẹ mặc định không có tài khoản app; muốn cấp tài khoản cần parent consent.
BA: Mới chốt cho form đăng ký. Với consent request gửi sau (field trip, ad hoc, Crossroad) cần một hay cả hai PH đồng ý thì chưa rõ.
Avail: 

## Q-73-07 [Đã chốt] P1 · Người nhận
Q: Khi Send/Resend, hệ thống tự xác định Guardian hay người dùng được chọn người nhận?
A: Tin nhắn mặc định gửi cả hai PH. Lúc nhập học, từng trẻ được cấu hình "cả hai" hay "chỉ người liên hệ chính". Trường hợp đặc biệt (ly hôn) mặc định chỉ chọn một người, GV vẫn thêm được người kia. Hóa đơn gửi cho billing person (chỉ định được). Lúc gửi consent, CD chọn đối tượng theo lớp hoặc cả centre.
BA: 
Avail: 

## Q-73-08 [Đã chốt] P1 · Kênh gửi
Q: App và email được gửi đồng thời hay email chỉ là fallback khi Guardian chưa kích hoạt tài khoản?
A: PH trả lời consent trong Parent App, kết quả đổ về SMS và tự tick mục Consent trong checklist học sinh. Tạo survey/consent mới phải có Announcement kèm link. Announcement có tùy chọn gửi kèm email do người tạo chọn. Thông báo app nhóm theo category, có "Surveys + Consents". BBA không muốn spam mail PH: cái gì cần mail thì người tạo chọn, còn lại qua app hết.
BA: 
Avail: 

## Q-73-09 [Chưa phản hồi] P1 · Reminder
Q: Reminder được gửi thủ công hay tự động; giới hạn số lần và khoảng cách giữa các lần gửi là gì?
A: 
BA: 
Avail: 

## Q-73-10 [DOTB tự quyết] P1 · Reminder count
Q: Reminder count tính lần bấm gửi, lần gửi thành công hay cả retry hệ thống?
A: Nhà mình tự thiết kế được. BBA muốn thẻ tổng quan cho biết bao nhiêu nhà đã trả lời, bấm vào thì chỉ hiện người chưa trả lời để centre dễ đi nhắc. BBA cũng muốn bộ lọc consent vì số consent gửi hàng loạt sẽ rất nhiều.
BA: 
Avail: 

## Q-73-11 [Chưa phản hồi] P0 · Version
Q: Khi có version mới, consent cũ còn hiệu lực hay tất cả Guardian phải trả lời lại?
A: 
BA: 
Avail: Hệ thống phải lưu version nội dung PH đã đồng ý và thời điểm đồng ý.

## Q-73-12 [Đã chốt] P1 · Expiry và renewal
Q: Expiry date được cấu hình theo Consent Type, version hay từng request; có tự động tạo renewal request không?
A: Vòng đời theo từng loại: Privacy, medical, media – một lần, không hết hạn (centre có thể hỏi thêm media consent theo sự kiện marketing). Field trip, ad hoc – theo từng lần/sự kiện, có ngày đóng. Crossroad – hằng năm, đầu năm học. Năm học chạy tháng 1 đến tháng 12.
BA: Chưa nói rõ renewal Crossroad tạo tự động hay thủ công.
Avail: Crossroad gia hạn hằng năm, hệ thống nhắc đầu năm học.

## Q-73-13 [Đã chốt] P0 · Rút consent
Q: Guardian có được rút lại consent; thay đổi có hiệu lực ngay và tác động đến chức năng liên quan thế nào?
A: Media/data consent có thể rút bằng văn bản (TSH và Common Terms 2027 đều ghi vậy). BBA muốn PH tự cập nhật marketing/privacy preference trong hồ sơ (Taidii hiện không cho). Trẻ không có media consent thì không được chụp/đăng: hệ thống phải chặn hoặc cảnh báo khi tag trẻ đó, và Marketing cũng phải biết.
BA: 
Avail: 

## Q-73-14 [Đã chốt] P1 · Trùng request
Q: Có được tồn tại đồng thời nhiều request đang mở cho cùng Child và Consent Type không?
A: Có. Field trip và ad hoc là consent theo từng sự kiện, nên mỗi request gắn với một sự kiện hoặc chuyến đi.
BA: 
Avail: 

## Q-73-15 [DOTB tự quyết] P0 · Bằng chứng
Q: Audit/evidence phải lưu những gì: nội dung version, Guardian, response, date/time, channel, IP/device hay electronic signature?
A: Nhà mình tự xử ạ.
BA: 
Avail: 

## Q-74-01 [Đã chốt] P0 · Phạm vi promotion
Q: Chức năng áp dụng cho tất cả level hay chỉ annual promotion; K2 graduation và Infant chuyển Playgroup có dùng cùng flow không?
A: 1. Annual promotion: cuối năm, cả lớp cùng lên lớp mới ở level kế tiếp. 2. Infant promotion: bất kỳ lúc nào trong năm, từng trẻ theo tuổi (18 tháng), Infant lên Playgroup. 3. Class change: đổi lớp trong cùng level (do GV, bạn học). K2 graduation là mass withdrawal (reason = graduation), chỉ áp cho K2 rời vào tháng 12.
BA: 
Avail: K2 thực sự rời BBA dùng mass graduation trên withdrawal engine; trẻ tiếp tục học/move level là continuation.

## Q-74-02 [Đã chốt] P0 · Phạm vi Centre
Q: Nâng level chỉ chuyển sang lớp trong cùng Centre hay hỗ trợ chuyển khác Centre?
A: Chuyển khác centre là luồng Transfer riêng. Trong cùng brand vẫn điền withdrawal ở centre cũ và registration ở centre mới. Khác brand thì tính là withdrawal. Malaysia có ca junior campus → senior campus thuộc hai brand khác nhau, hai tài khoản ngân hàng khác nhau: BBA chốt đi theo kế toán/audit của centre, tức là transfer, không phải promotion.
BA: Bulk promotion chỉ trong cùng Centre.
Avail: 

## Q-74-03 [Một phần / cần hỏi lại] P1 · Đề xuất target
Q: Hệ thống tự đề xuất target level/class theo rule nào hay người dùng luôn chọn thủ công?
A: Với graduation: chọn cả cohort, bỏ tick ngoại lệ. Ngoại lệ là K2 học lại ("K3"), trẻ quá tuổi, trẻ được gia hạn; trẻ ngoại lệ vẫn giữ record. K2 không tốt nghiệp mà admin chưa xử lý thì hệ thống gắn cờ để năm sau biết xếp lớp nào. Cuối năm admin rà trẻ nào đã lên lớp, rút hay tốt nghiệp. Trẻ ở lại thì giữ lớp hoặc chuyển sang lớp khác cùng level.
BA: Comment đặt ở ô của Q-74-03 nhưng nội dung trả lời Q-74-05 (ngoại lệ từng Child). Rule đề xuất target level/class vẫn chưa có.
Avail: 

## Q-74-05 [Chưa phản hồi] P0 · Ngoại lệ từng Child
Q: Người dùng có thể bỏ chọn từng Child để lưu ban, rút học hoặc xử lý ngoại lệ không?
A: 
BA: Thực tế đã được trả lời trong comment ở ô H56 (Q-74-03): chọn cả cohort, bỏ tick ngoại lệ; trẻ ở lại giữ lớp hoặc chuyển lớp cùng level.
Avail: Cho mass graduation: chọn toàn bộ cohort trước, bỏ chọn ngoại lệ. Còn mở: áp dụng cho bulk promotion?

## Q-74-06 [Đã chốt] P0 · Điều kiện đủ
Q: Những trạng thái Child/Enrolment nào đủ điều kiện lên lớp/tốt nghiệp và xử lý future withdrawal, transfer hoặc temporary leave thế nào?
A: Graduation chỉ cho K2 rời vào tháng 12. K2 rời sớm (vd 30/11) đi luồng withdrawal thường và vẫn nộp Form 3; K2 tháng 12 được miễn Form 3. Temporary withdrawal là tạm dừng, trẻ vẫn trong hệ thống (tối đa 3 tháng).
BA: Chưa nói rõ trạng thái nào đủ điều kiện cho annual promotion.
Avail: 

## Q-74-07 [Một phần / cần hỏi lại] P1 · Effective date
Q: Effective Date mặc định là ngày đầu của lớp học hay do người dùng chọn; có cho phép lên lịch và hủy trước ngày hiệu lực không?
A: Năm học tháng 1 đến tháng 12. Lập kế hoạch lớp năm sau vào tháng 11–12: CD lập lớp và gán GV, admin xếp trẻ. Annual promotion làm cuối năm. BBA muốn hệ thống tự tạo lịch term và lớp của năm sau, sau Quý 1.
BA: Mới có bối cảnh lịch năm học. Chưa trả lời Effective Date mặc định, lên lịch và hủy.
Avail: 

## Q-74-08 [Đã chốt] P0 · Capacity
Q: Nếu target class vượt capacity, hệ thống chỉ cảnh báo và cho tiếp tục hay chặn?
A: Capacity không cố định, cần linh hoạt: tối đa 24 nhưng vẫn có thể nhận em thứ 25. Capacity tính theo centre và theo level. CD cấu hình sĩ số tối đa từng lớp.
BA: Hiểu là chỉ cảnh báo, cho tiếp tục.
Avail: 

## Q-74-09 [Một phần / cần hỏi lại] P0 · Fee scheme
Q: Fee scheme mới có hiệu lực từ ngày chuyển thế nào và có được ảnh hưởng invoice đã phát hành không?
A: BBA không cho void hóa đơn; hóa đơn đã phát hành thì sửa bằng credit note trỏ về hóa đơn đó. BBA cần change report hằng tháng (trẻ mới, rút, suspended, đổi chương trình, đổi subsidy…), bấm vào xem danh sách, bắt buộc ở Phase 1. Hóa đơn tháng sinh nháp khoảng ngày 24.
BA: Đã rõ phần invoice đã phát hành. Chưa rõ fee scheme mới áp từ ngày nào (theo Effective Date hay đầu tháng sau).
Avail: 

## Q-74-10 [Một phần / cần hỏi lại] P1 · Attendance và communication
Q: Attendance roster và communication thread được chuyển ngay khi xác nhận hay tại Effective Date; lịch sử lớp cũ được giữ thế nào?
A: Communication: khi trẻ lên lớp hoặc đổi lớp, hệ thống tạo thread mới cho lớp mới. Thread cũ thành inactive, chỉ xem. Không archive theo năm, giữ tới khi trẻ rời trường. Private group chat gắn theo người.
BA: Chưa trả lời phần Attendance roster và thời điểm chuyển.
Avail: 

## Q-74-11 [DOTB tự quyết] P1 · Preview
Q: Preview phải hiển thị trường nào, warning nào và những Child nào sẽ bị loại khỏi batch?
A: Nhà mình tự xử ạ.
BA: 
Avail: 

## Q-74-12 [DOTB tự quyết] P0 · Lỗi từng phần
Q: Nếu một Child cập nhật thất bại, batch tiếp tục với Child khác hay rollback toàn bộ; partial-failure report gồm gì?
A: Nhà mình tự xử.
BA: 
Avail: 

## Q-74-13 [DOTB tự quyết] P1 · Idempotency
Q: Nếu người dùng chạy lại cùng một yêu cầu nâng lớp, hệ thống ngăn thay đổi trùng như thế nào?
A: Nhà mình tự xử.
BA: 
Avail: 

## Q-74-15 [Một phần / cần hỏi lại] P1 · Thông báo và lớp cũ
Q: Parent/Teacher có nhận thông báo không và lớp cũ được tự động đóng khi không còn Child hay phải đóng thủ công?
A: Graduation: app báo PH "your child is graduating, you have outstanding amount that will be refunded", PH xác nhận thông tin ngân hàng. Nhập học mới: welcome letter và báo GV lớp 2 tuần trước ngày đầu đi học, cấu hình theo brand/centre. HQ/centre dùng Announcement để báo thay đổi lớn.
BA: Chưa trả lời: thông báo khi annual promotion, và lớp cũ đóng tự động hay thủ công.
Avail: 

## Q-75-02 [Đã chốt] P0 · Người giao trẻ
Q: Khi check-in, người giao trẻ được chọn từ Parent/Authorised Pickup và cho phép Someone else nhập tay tên và relationship. Ưu tiên hiển thị cả 2 hay ưu tiên chọn, nhập tay chỉ hiện khi chọn option nhập tay?
A: Check-out: người đón phải là người đã được duyệt, không có lựa chọn người lạ hay đón tạm thời. Người không có trong danh sách thì centre gọi PH, PH điền đủ thông tin ngay lúc đó rồi người đó mới được đón. Check-in: người giao có thể không phải PH hay authorised pickup (bus: tài xế giao, phụ xe của công ty bus nhận về; có nhà nhờ người giúp việc). Vậy check-in cần cách ghi một người ngoài danh sách.
BA: Nghiệp vụ đã rõ. Cách hiển thị trên UI (cả 2 hay ẩn ô nhập tay) DOTB tự quyết.
Avail: 

## Q-75-04 [Đã chốt] P0 · Ngoại lệ khẩn cấp
Q: Nếu có ngoại lệ khẩn cấp cho người chưa được duyệt, ai được override và cần bằng chứng/phê duyệt gì?
A: BBA không muốn có cơ chế "override". Người đến đón phải được duyệt đầy đủ. Khi có người lạ đến, centre gọi PH, PH điền nhanh đủ thông tin rồi người đó mới được đón.
BA: 
Avail: 

## Q-75-08 [Một phần / cần hỏi lại] P1 · Chỉnh giờ
Q: Check-in/out time được chỉnh trong khoảng nào, bởi ai và có được nhập thời gian tương lai hoặc ngày khác không?
A: Void (hủy) bản ghi điểm danh không cần duyệt ở cả Singapore lẫn Malaysia. Chỉ một số người có quyền: CD, admin, senior teacher (tách role riêng). Singapore bắt buộc audit trail vì một lượt check-in nhầm trong tháng có thể làm sai subsidy ECDA. Singapore đẩy điểm danh sang ECDA theo batch lúc 12h trưa để buổi sáng còn sửa được chỗ nhập sai.
BA: Trả lời về void, chưa trả lời khoảng chỉnh giờ / ngày khác / tương lai. Lưu ý: "void không cần duyệt" khác với Q-81-03 (ai cũng gửi request, Admin/CD/ST duyệt) – cần thống nhất.
Avail: 

## Q-75-10 [Đã chốt] P1 · Bus check-in
Q: Khi bulk check-in theo bus, adult handover và photo được ghi thế nào cho từng Child?
A: Bộ lọc theo xe chỉ để gom trẻ của một xe vào một danh sách cho nhanh. Check-in/out vẫn làm từng trẻ vì còn chụp ảnh từng trẻ, nên không có bản ghi chung cho cả nhóm: mỗi trẻ có bản ghi riêng, ảnh riêng. Người giao lúc xe đến là tài xế, người nhận trẻ về là phụ xe của công ty bus. GV của centre chụp ảnh trẻ cùng phụ xe khi xe đến và trước khi xe đi, theo quy trình sign-in/sign-out.
BA: 
Avail: Có filter theo Bus để mark cả nhóm; bus assistant chụp ảnh khi trẻ lên và xuống xe.

## Q-75-12 [Chưa phản hồi] P0 · Retention
Q: Photo và handover evidence được lưu bao lâu, ai được xem/export và có tự động xóa/ẩn không?
A: 
BA: Gián tiếp: Parent app hiện ảnh lúc giao nhận (Q-81-02).
Avail: 

## Q-76-05 [Đã chốt] P1 · Giá trị hợp lệ
Q: Khoảng 36–40°C là giới hạn chặn hay chỉ picker; nhập tay ngoài khoảng được cảnh báo hay bị từ chối?
A: Thang không cần xuống dưới 36 (35 độ là trẻ đã bị lạnh), nhưng phải lên được 39–40 vì sốt cao có thật. Mặc định 36.5, hiện sẵn dải 36.3–36.7 để bấm luôn. Nút phải ghi "Enter manually".
BA: Chưa nói rõ nhập tay ngoài khoảng thì cảnh báo hay chặn.
Avail: 

## Q-76-06 [Đã chốt] P1 · Bluetooth
Q: Người dùng có được sửa giá trị được đọc tự động từ thiết bị Bluetooth không?
A: Có.
BA: 
Avail: Một số Centre có Bluetooth thermometer tự điền vào tablet; Centre khác nhập tay.

## Q-77-03 [Đã chốt] P0 · Thời gian dùng để tính
Q: Late được tính theo actual check-in time, device time, server time hay thời gian đã correction?
A: Late tự gắn khi so giờ check-in với giờ cấu hình của từng centre (vd sau 9:15 sáng, sau 12:15 chiều). Chọn giờ máy hay server, xử lý lệch giờ khi offline là chuyện kỹ thuật DOTB tự quyết. Hợp lý nhất là dùng giờ ghi nhận tại cổng (giờ check-in), không phải giờ đồng bộ.
BA: 
Avail: 

## Q-77-04 [DOTB tự quyết] P1 · Backdated/offline
Q: Record sync muộn hoặc được nhập backdated có tự tính lại Late flag không?
A: Đây là luật technical DOTB tự đặt được.
BA: 
Avail: 

## Q-77-05 [Một phần / cần hỏi lại] P0 · Không hiển thị cho Parent
Q: Late flag phải bị loại khỏi những nơi nào: Parent App, notification, export, API và email?
A: Ở Singapore, late chỉ nhân viên thấy, phụ huynh không thấy.
BA: Chưa nêu rõ từng kênh (API, email, notification, export cho PH). Câu trả lời ghi "ở Singapore" – Malaysia thì sao?
Avail: Late flag không hiển thị trong Parent view.

## Q-77-06 [Chưa phản hồi] P1 · Màn hình nội bộ
Q: Late flag hiển thị ở class attendance, child day record, centre overview và report nào?
A: 
BA: 
Avail: 

## Q-77-07 [Chưa phản hồi] P1 · Override
Q: Người dùng có được bỏ Late flag thủ công và nhập lý do không?
A: 
BA: Q-81-02 nói "Late flag không nhập tay, tự gắn theo giờ cấu hình" – mâu thuẫn với ghi nhận cũ (staff gắn cờ thủ công). Vẫn cần hỏi có cho override không.
Avail: Late arrival hiện được Staff gắn cờ thủ công.

## Q-77-08 [Chưa phản hồi] P1 · Thay đổi cấu hình
Q: Khi đổi cấu hình giờ late: cho nhập thời gian bắt đầu áp dụng hay áp dụng ngay sau khi lưu? Nếu cho nhập ngày quá khứ thì tính lại dữ liệu cũ thế nào; dữ liệu đã cập nhật tay bị cập nhật theo hay giữ nguyên?
A: 
BA: 
Avail: 

## Q-80-01 [Đã chốt] P0 · Expected count
Q: Quy tắc để tính Expected count?
A: Trẻ Temporary withdrawal/suspension không điểm danh, không subsidy, không invoice, không tính vào enrolment number, vẫn có trong student list (gắn tag), ẩn khỏi attendance app để GV khỏi bấm nhầm.
BA: Mới có quy tắc loại trừ temporary withdrawal; xem thêm Q-80-03.
Avail: 

## Q-80-03 [Đã chốt] P1 · Ngoại lệ roster
Q: Approved leave, temporary withdrawal, future start, ended enrolment và absent được tính vào expected thế nào?
A: Temporary withdrawal: ra khỏi màn điểm danh, không tính enrolment number, vẫn trong student list có tag. Leave: PH xin nghỉ trên app, hệ thống hiện 2 lưu ý (tối thiểu 1 ngày/tháng cho trẻ công dân SG; không miễn phí); kiểm tra ngày 18 vẫn áp dụng cho trẻ nghỉ phép. Future start / bản ghi mới: điểm danh gắn với bản ghi enrolment, không gắn với hồ sơ trẻ; chuyển centre hoặc rút rồi nhập lại là bản ghi mới. Ended enrolment: Form 3 ECDA có trường "Last Day of Attendance" (gợi ý ngày cuối đi học là mốc kết thúc).
BA: Approved leave có tính vào expected hay không vẫn chưa nói thẳng.
Avail: 

## Q-80-04 [Chưa phản hồi] P0 · Realtime
Q: Overview cần cập nhật realtime hay theo chu kỳ; độ trễ chấp nhận được là bao lâu?
A: 
BA: 
Avail: 

## Q-80-05 [DOTB tự quyết] P0 · Offline/stale
Q: Nếu một iPad đang offline, overview hiển thị last sync và cảnh báo dữ liệu chưa đầy đủ như thế nào?
A: Attendance phải điểm danh được khi mất mạng rồi đồng bộ sau; Parent App không cần offline. Phần còn lại nhà mình tự thiết kế.
BA: 
Avail: 

## Q-80-07 [Chưa phản hồi] P1 · Drill-down
Q: Drill-down đi từ Brand → Centre → Class → Child hay có mức Country/District; cần giữ filter nào?
A: 
BA: 
Avail: 

## Q-80-08 [Đã chốt] P1 · Timezone
Q: Today được xác định theo timezone của Centre hay người xem?
A: Phase 1 chỉ có Singapore và Malaysia, cùng múi giờ UTC+8, nên "today" theo centre hay theo người xem đều cho cùng kết quả.
BA: 
Avail: 

## Q-80-09 [Một phần / cần hỏi lại] P1 · Đếm trùng
Q: Nếu Child có nhiều programme/stream trong ngày, overview thống kê theo quy tắc nào?
A: 3 stream: Main / Early Intervention (Bright Path) / Enrichment. Enrichment học hằng tuần, do enrichment trainer điểm danh. Phase 1 tối thiểu: điểm danh được theo từng program và biết trẻ thuộc program nào; tạo/vận hành program để Phase 2. Billing tính theo số program.
BA: Chưa có quy tắc đếm trên overview (đếm theo trẻ hay theo stream).
Avail: Main programme, Early Intervention và enrichment là 3 attendance stream riêng, do các vai trò khác nhau ghi nhận.

## Q-80-11 [Chưa phản hồi] P1 · Export và hiệu năng
Q: Có cho phép export snapshot; yêu cầu thời gian tải khi tổng hợp toàn bộ Brand/Country là bao lâu?
A: 
BA: 
Avail: 

## Q-81-01 [Một phần / cần hỏi lại] P0 · Correction hay void
Q: Khi sửa sai attendance mark/time, hệ thống thực hiện correction giữ record hay void record và tạo lại?
A: Check-in nhầm phải void (remove), không phải check-out. Lý do: ở Singapore chỉ cần 1 lần check-in trong tháng là trẻ được subsidy, nên check-in nhầm phải gỡ và sẽ bị audit.
BA: Đã rõ với check-in nhầm. Sửa sai thời gian (không phải nhầm cả lượt) dùng correction hay void vẫn chưa rõ.
Avail: Attendance ghi nhầm phải Void và loại khỏi record; check-out không thay thế Void.

## Q-81-02 [Một phần / cần hỏi lại] P0 · Trường được sửa
Q: Những trường nào được correction: status, check-in/out time, adult handover, photo, late flag, temperature hay leave status?
A: Late flag không nhập tay: BBA chốt đến trễ tự gắn theo giờ cấu hình của centre. Nhiệt độ: đo nhiều lần/ngày (một số centre 3 lần: arrival, sau ngủ trưa, lúc về); CD có nút "add temperature". Parent app hiện ảnh lúc giao nhận để PH thấy ai đưa/đón.
BA: Chưa có danh sách trường được correction (time, handover, photo, leave status).
Avail: 

## Q-81-03 [Đã chốt] P0 · Quyền sửa
Q: Vai trò nào được correction trực tiếp và vai trò nào chỉ được request correction?
A: Ai cũng gửi được yêu cầu; người duyệt là Admin, CD hoặc Senior Teacher được CD chỉ định; chính những người này tự void thì không qua duyệt.
BA: 
Avail: Cho Void: ai cũng gửi request; Admin, CD hoặc Senior Teacher được CD chỉ định approve/void.

## Q-81-04 [Chưa phản hồi] P0 · Approval
Q: Correction có luôn không cần phê duyệt hay correction sau ngày hiện tại/ảnh hưởng subsidy cần CD approval?
A: 
BA: Gián tiếp: Q-81-03 (request → Admin/CD/ST duyệt) và Q-75-08 (void không cần duyệt) – cần thống nhất.
Avail: Cho Void: cần approval, trừ khi người làm là Admin, CD hoặc designated Senior Teacher.

## Q-81-05 [Một phần / cần hỏi lại] P0 · Reason
Q: Reason có bắt buộc cho mọi correction và có danh mục reason code ngoài free text không?
A: BBA yêu cầu audit trail rõ ràng cho mọi thay đổi điểm danh ở Singapore vì đây là bằng chứng giải trình với ECDA.
BA: Chưa trả lời reason bắt buộc hay không, có reason code hay không.
Avail: 

## Q-81-07 [Đã chốt] P0 · Tác động downstream
Q: Correction tác động thế nào đến subsidy, e-Form 1, invoice/charge, reports và staff-child safety counts?
A: Subsidy: 1 check-in trong tháng là đủ điều kiện, nên void check-in nhầm làm thay đổi trạng thái subsidy và cảnh báo ngày 18. e-Form 1: hệ thống tự gửi ECDA vào ngày có điểm danh thật đầu tiên, chạy lô 12:00 trưa; BBA chọn 12:00 để chặn điểm danh nhầm buổi sáng.
BA: Chưa nói tác động tới invoice/charge, reports và staff-child counts.
Avail: 

## Q-81-08 [Chưa phản hồi] P1 · Parent notification
Q: Parent có được thông báo khi check-in/out đã gửi trước đó bị correction không; nội dung nào được hiển thị?
A: 
BA: 
Avail: 

## Q-81-09 [Chưa phản hồi] P0 · Khóa kỳ
Q: Sau mốc nào attendance bị khóa correction: cuối ngày, month close, subsidy submission hay không khóa?
A: 
BA: Gián tiếp: e-Form 1 gửi ECDA lô 12:00 trưa (Q-81-07). Mốc khóa vẫn chưa có.
Avail: 

## Q-81-10 [DOTB tự quyết] P1 · Unsynced và synced
Q: Unsynced record được sửa trên iPad, còn synced record được correction trên web hay phải qua void request?
A: BBA chỉ yêu cầu điểm danh offline rồi đồng bộ sau. Phân biệt "chưa đồng bộ thì sửa trên iPad, đã đồng bộ thì correction/void trên web" là thiết kế kỹ thuật của DOTB.
BA: 
Avail: 

## Q-86-01 [Đã chốt] P0 · Loại routine
Q: Danh mục Phase 1 chính thức gồm Meals, Milk/Bottle, Naps, Nappy/Toilet và Mood hay những loại nào?
A: Ảnh app Taidii và file export BBA gửi đều có 4 loại: Bottle, Food, Nap, Potty.
BA: Mood không có trong 4 loại – nên xác nhận bỏ Mood ở Phase 1.
Avail: Teacher workflow nêu Meals, Naps, Nappies và Mood; Parent Health record trẻ nhỏ có Feeds.

## Q-86-02 [DOTB tự quyết] P1 · Trường dữ liệu
Q: Trường bắt buộc cho từng routine là gì: meal amount, bottle prepared/drunk, nap quality, diaper/potty/accident, wet/BM/dry?
A: Dùng lại trên Taidii cũng được ạ.
BA: Tham khảo trường của Taidii.
Avail: 

## Q-86-04 [Một phần / cần hỏi lại] P1 · Bulk class entry
Q: Khi record whole class, Child vắng mặt/on leave có được áp dụng; người dùng chỉnh ngoại lệ trước hay sau khi lưu?
A: Cả 2.
BA: Trả lời quá ngắn, câu hỏi có 2 vế – nên xác nhận "cả 2" là: cho chỉnh ngoại lệ cả trước và sau khi lưu? Trẻ vắng có được áp dụng không?
Avail: 

## Q-86-05 [DOTB tự quyết] P1 · Partial failure
Q: Nếu một Child lỗi khi lưu routine cho cả lớp, lưu các Child khác hay hủy toàn bộ?
A: Nhà mình tự xử.
BA: 
Avail: 

## Q-86-06 [Chưa phản hồi] P1 · Thời gian
Q: Có cho phép nhập backdated/future routine?
A: 
BA: 
Avail: 

## Q-86-08 [Chưa phản hồi] P0 · Parent visibility
Q: Privacy setting được cấu hình theo Country/Brand/Centre/Level/Routine?
A: 
BA: 
Avail: 

## Q-86-09 [Một phần / cần hỏi lại] P1 · Notification
Q: Parent nhận notification một lần khi checkout; nếu routine được thêm/sửa sau checkout thì thông báo lại hay chỉ cập nhật dữ liệu?
A: BBA chốt có thông báo theo category, có Routines, và PH chọn chỉ nhận một số category; BBA lo PH bị báo quá nhiều.
BA: Chưa trả lời: thêm/sửa sau checkout có báo lại không.
Avail: 

## Q-86-10 [Chưa phản hồi] P1 · Notes from home
Q: Notes from home có hiển thị trong class routine view và có được liên kết với routine/day record không?
A: 
BA: 
Avail: 

## Q-90-05 [Một phần / cần hỏi lại] P0 · Nhiều ca
Q: Một staff có được clock-in/out nhiều lần trong ngày cho split shift hoặc break không? Việt Nam đang chia ca sáng và ca chiều.
A: Phạm vi Phase 1 BBA chốt là chấm công tối thiểu: nhân viên đến báo có mặt và đo nhiệt độ, vì họ cần report.
BA: Chưa trả lời có cho nhiều lượt clock/ngày không.
Avail: 

## Q-90-07 [Chưa phản hồi] P0 · Temperature
Q: Staff temperature có bắt buộc tại clock-in; khi vượt threshold hệ thống chỉ cảnh báo hay chặn vào làm và thông báo cho ai?
A: 
BA: Gián tiếp: Q-90-05 nói staff đến báo có mặt và đo nhiệt độ.
Avail: 

## Q-90-08 [Chưa phản hồi] P0 · Missed clock-out
Q: Nếu staff quên clock-out, hệ thống tự đóng ca, nhắc người dùng hay yêu cầu correction ngày hôm sau?
A: 
BA: 
Avail: 

## Q-90-09 [Chưa phản hồi] P0 · Correction
Q: Ai được sửa clock time/temperature; reason và approval có bắt buộc không?
A: 
BA: 
Avail: 

## Q-90-10 [Chưa phản hồi] P1 · Staff on site
Q: Staff on site được tính từ open clock record; xử lý staff clock tại nhiều Centre hoặc record sync trễ thế nào?
A: 
BA: 
Avail: 

## Q-90-12 [DOTB tự quyết] P1 · Offline conflict
Q: Nếu staff clock trên iPad khi offline và sau đó clock trên web, hệ thống phát hiện và xử lý duplicate thế nào?
A: Nhà mình tự xử.
BA: 
Avail: 
