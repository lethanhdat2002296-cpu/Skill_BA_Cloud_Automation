# Use case — nguyên tắc tham khảo

## Nguồn
- Alistair Cockburn, *Writing Effective Use Cases* (Addison-Wesley, 2001) — mẫu fully-dressed: tác nhân chính, phạm vi, mức, stakeholders & interests, tiền điều kiện, đảm bảo tối thiểu / khi thành công, kích hoạt, kịch bản chính, extensions, biến thể công nghệ & dữ liệu. Mẫu cơ bản 1998: https://cs.otago.ac.nz/coursework/cosc461/uctempla.htm
- IIBA, *BABOK Guide v3*, kỹ thuật 10.47 "Use Cases and Scenarios" và 10.49 "User Stories".
- UML 2.5 (OMG) — sơ đồ use case: tác nhân, ranh giới hệ thống, quan hệ «include» / «extend» / tổng quát hoá.

## Mức use case (Cockburn)
| Mức | Khi nào | Ví dụ |
|---|---|---|
| Tóm tắt (cloud/kite) | Gom nhiều UC mục tiêu người dùng thành một quy trình dài | "Mua vật tư từ nhu cầu tới nhập kho" |
| Mục tiêu người dùng (sea level) | Mặc định. Một lần ngồi, 2–20 phút, xong có kết quả | "Duyệt Yêu cầu mua hàng" |
| Chức năng con (fish) | Đoạn dùng lại ở nhiều UC, qua `include` | "Tra giá vật tư" |

Phép thử: *"Tác nhân có vui lòng đứng dậy đi về sau khi xong việc này không?"* — có → mức mục tiêu người dùng.

## Viết kịch bản
- Mỗi bước: **ai** làm **gì** (chủ ngữ rõ: "Người đề xuất nhập…", "Hệ thống kiểm tra…"). Tránh "người dùng" chung chung khi có tên tác nhân.
- Kịch bản chính chỉ đường thành công, 3–9 bước. Bước kiểm tra viết dạng khẳng định ("Hệ thống xác nhận mọi dòng có nhà cung cấp") — nhánh sai đưa xuống extensions.
- Không mô tả giao diện ("bấm nút xanh góc phải"); nêu ý định ("Người đề xuất gửi phiếu duyệt"). Giao diện thuộc SRS mục 6 / wireframe.
- Extensions: điều kiện là sự thật đã phát hiện ("3a. Dòng thiếu nhà cung cấp"), không phải câu hỏi. Mỗi nhánh kết thúc: quay lại bước nào, hoặc kết thúc thất bại.
- `*a` cho sự kiện có thể xảy ra ở bất kỳ bước nào (huỷ, mất kết nối, hết phiên).

## Include / extend
- `include`: UC gốc **luôn** gọi UC con tại một bước (đoạn dùng chung). Mũi tên từ UC gốc → UC con.
- `extend`: UC mở rộng **tuỳ điều kiện** chen vào UC gốc tại điểm mở rộng; UC gốc vẫn hoàn chỉnh khi không có nó. Mũi tên từ UC mở rộng → UC gốc.
- Không lạm dụng: chỉ tách khi đoạn đó dùng ≥ 2 nơi hoặc có tác nhân/điều kiện riêng.

## Use case vs user story vs FR
| | User story (URD) | Use case (UC.md) | FR (SRS) |
|---|---|---|---|
| Trả lời | Ai cần gì, để làm gì | Tương tác diễn ra thế nào, sai thì sao | Hệ thống phải làm gì, kiểm thử ra sao |
| Độ chi tiết | 1 câu + AC | Kịch bản + nhánh | Input/Output/BR/AC |
| Người đọc chính | Khách hàng, PO | Khách hàng, BA, tester | Dev, tester |

## Lỗi thường gặp
- UC theo màn hình ("UC màn danh sách") hoặc theo CRUD lẻ → gộp theo mục tiêu.
- Kịch bản chính chứa `nếu… thì…` → tách nhánh xuống extensions.
- Đảm bảo khi thành công viết chung chung ("dữ liệu được lưu") → ghi trạng thái cụ thể ("YCMH ở trạng thái Chờ duyệt cấp 1, Trưởng nhóm có activity duyệt").
- Sơ đồ có mũi tên giữa các tác nhân hoặc thể hiện thứ tự bước → sơ đồ use case không phải luồng; luồng để ở swimlane/activity.
