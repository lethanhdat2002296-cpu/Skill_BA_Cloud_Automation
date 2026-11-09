# Test case — nguyên tắc tham khảo

## Nguồn
- ISTQB, *Certified Tester Foundation Level Syllabus v4.0* (2023), chương 4 "Test Analysis and Design": phân vùng tương đương, giá trị biên, bảng quyết định, chuyển trạng thái.
- ISO/IEC/IEEE 29119-3:2021 — cấu trúc tài liệu test case (ID, mục tiêu, tiền điều kiện, bước, kết quả mong đợi, truy vết yêu cầu).
- IIBA, *BABOK Guide v3*, 7.6 "Verify Requirements" và 10.1 "Acceptance and Evaluation Criteria".
- Ý tưởng ma trận truy vết FR → AC → TC và "mỗi AC ≥ 1 test case": OpenBA-Kit (MIT), `rules/14-test-case-traceability.md`.

## Từ AC ra test case
| AC trong SRS | Test case cần có |
|---|---|
| Thành công (Then tạo / chuyển / hiện kết quả) | 1 TC `Chức năng` — đúng dữ liệu mẫu của AC |
| Lỗi / bị chặn (Then hiện lỗi "…", giữ trạng thái) | 1 TC `Ngoại lệ` — kiểm cả thông báo nguyên văn và việc dữ liệu KHÔNG đổi |
| Có ngưỡng (≥, ≤, tối đa, hạn N ngày) | TC `Biên`: đúng ngưỡng, ngay dưới, ngay trên (vd. 0 / 1 / 2; ngày hôm qua / hôm nay) |
| Nhiều điều kiện kết hợp (BR dạng KHI … THÌ … TRỪ KHI) | Bảng quyết định: mỗi tổ hợp điều kiện có kết quả khác nhau = 1 TC |
| Chuyển trạng thái (mục 3.0 SRS) | Mỗi dòng bảng chuyển trạng thái = 1 TC `Trạng thái`; thêm 1 TC chuyển **không hợp lệ** (vd. duyệt phiếu đã huỷ) |
| Ma trận phân quyền (mục 2.2 SRS) | Mỗi ô `—` quan trọng (thao tác bị cấm) = 1 TC `Phân quyền` |
| Tích hợp / email / cron | TC `Tích hợp`: thành công + đối tác lỗi / timeout / dữ liệu thiếu |
| NFR có ngưỡng | TC `Phi chức năng` với cách đo trong NFR |

## Viết một test case tốt
- **Một mục tiêu** mỗi TC; tiêu đề = điều được kiểm ("Gửi duyệt phiếu không có dòng bị chặn").
- **Tiền điều kiện** đủ để người khác dựng lại: tài khoản, trạng thái chứng từ, cấu hình.
- **Bước** là thao tác của người dùng, đánh số `1) … <br>2) …`; 3–8 bước. Không ghi "kiểm tra hệ thống chạy đúng".
- **Kết quả mong đợi** quan sát được: giá trị, trạng thái, thông báo nguyên văn, bản ghi sinh ra, người nhận activity/email. Không dùng "thành công", "bình thường" một mình.
- Dữ liệu cụ thể (tên, số, ngày) lấy từ AC; dữ liệu dùng nhiều lần đưa lên mục 2.
- Không lặp: hai AC cùng kịch bản → 1 TC, cột AC ghi `AC1, AC2`.
