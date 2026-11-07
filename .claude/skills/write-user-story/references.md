# User story & backlog — nguyên tắc tham khảo

## Nguồn
- Mike Cohn, *User Stories Applied* (Addison-Wesley, 2004) — mẫu "As a… I want… so that…", 3C (Card, Conversation, Confirmation).
- Bill Wake, "INVEST in Good Stories, and SMART Tasks" (2003).
- Richard Lawrence & Peter Green, "The Humanizing Work Guide to Splitting User Stories" (humanizingwork.com) — các mẫu tách story.
- IIBA, *BABOK Guide v3*, kỹ thuật 10.49 "User Stories"; *Agile Extension to the BABOK Guide v2*.
- Atlassian, "Keep work parent-child relationships during CSV import to Jira Cloud": https://support.atlassian.com/jira/kb/map-issueid-parentid-fields-jira-csv-import — cột Issue ID + Parent, epic đứng trước story (Parent thay Epic Link trên Jira Cloud).

## INVEST
| Chữ | Nghĩa | Dấu hiệu vi phạm | Cách sửa |
|---|---|---|---|
| I — Independent | Làm và giao được riêng | "chỉ làm được sau khi xong US-xx và US-yy" ở cùng mức | Gộp story phụ thuộc chặt, hoặc ghi Phụ thuộc rõ |
| N — Negotiable | Nói *cái gì*, chưa chốt *cách làm* | Story ghi tên bảng, tên hàm | Đưa chi tiết kỹ thuật xuống FR / task |
| V — Valuable | Có giá trị cho người dùng / khách | Story "tạo bảng dữ liệu", "viết API" | Viết lại theo lát nghiệp vụ end-to-end |
| E — Estimable | Ước lượng được | Có OQ chặn, chưa rõ quy tắc | Spike hoặc AS + OQ |
| S — Small | Vừa 1 sprint (≤ 8 điểm) | 13 điểm trở lên | Tách theo mẫu bên dưới |
| T — Testable | Có AC kiểm thử được | AC "nhanh", "dễ dùng" | AC Given/When/Then có số liệu |

## Mẫu tách story (thử theo thứ tự)
1. **Luồng theo lát mỏng (workflow steps):** làm trước đường đơn giản nhất xuyên suốt đầu–cuối, thêm bước giữa sau. *Không* tách mỗi bước một story nếu bước đó không có giá trị riêng.
2. **Thao tác (CRUD):** "quản lý X" → tạo / sửa / huỷ / tìm kiếm X.
3. **Biến thể quy tắc nghiệp vụ:** mỗi quy tắc / trường hợp đặc biệt một story (vd. giá từ hợp đồng → giá từ Price List → nhập tay).
4. **Biến thể dữ liệu:** một loại dữ liệu trước, loại khác sau (vd. vật tư Nhập kho trước, Dịch vụ sau).
5. **Cách nhập dữ liệu / giao diện:** nhập tay trước, import Excel / đọc email sau.
6. **Nỗ lực lớn ở lần đầu:** story đầu dựng nền + một trường hợp; các trường hợp sau rẻ hơn.
7. **Đơn giản / phức tạp:** phiên bản tối thiểu trước, các ngoại lệ (từ chối, gửi lại, huỷ) sau.
8. **Trì hoãn hiệu năng:** "chạy đúng" trước, "chạy nhanh / chịu tải" sau (NFR thành story riêng).
9. **Spike:** chưa ước lượng được vì chưa rõ kỹ thuật → story điều tra có thời hạn (timebox), rồi mới tách.

## Thang story point (mốc tham chiếu gợi ý cho dự án Odoo)
| Điểm | Đặc điểm |
|---|---|
| 1 | Đổi nhãn, thêm trường đơn giản, bộ lọc có sẵn |
| 2 | Thêm trường + quy tắc kiểm tra đơn giản trên form có sẵn |
| 3 | **Mốc:** một hành động mới trên model có sẵn (nút + chuyển trạng thái + thông báo) |
| 5 | Model / form mới nhỏ, hoặc luồng duyệt nhiều bước dùng module chuẩn |
| 8 | Model mới + nhiều quy tắc + tích hợp (email vào/ra, đọc file), hoặc báo cáo phức tạp |
| 13 | Quá lớn — tách; chỉ giữ tạm cho release sau |

Ước lượng bằng so sánh với story mốc, không quy đổi giờ. Căn cứ ghi ngắn: số màn mới/sửa, số quy tắc (BR), tích hợp, model mới, dữ liệu migrate.

## MoSCoW → Jira priority (backlog.csv)
Must → Highest · Should → High · Could → Medium · Won't → Low.
