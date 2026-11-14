# Test case — {{Tên dự án}}

| Thuộc tính | Giá trị |
|---|---|
| Mã dự án | {{du-an}} |
| Phiên bản | {{0.3 — cùng phiên bản SRS}} |
| Ngày | {{YYYY-MM-DD}} |
| Nguồn | {{SRS.md v…; UC.md v…}} |
| Môi trường test | {{Staging Odoo 17 Enterprise, dữ liệu mẫu mục 2}} |

## 1. Phạm vi & cách đọc
- Mỗi Acceptance criteria (AC) của FR có ít nhất 1 test case; FR `Must` có ít nhất 1 test case `Ngoại lệ`.
- Cột **AC** trỏ đúng tiêu chí trong SRS (`AC2` = tiêu chí số 2 của FR đó); có thể kèm `BR-01.2`, `UC-01 3a`.
- **Loại:** Chức năng · Ngoại lệ · Biên · Phân quyền · Trạng thái · Tích hợp · Phi chức năng.
- **Ưu tiên:** Cao (FR Must) · Trung bình (Should) · Thấp (Could).
- Bước cách nhau bằng `<br>`; kết quả mong đợi đo được, thông báo ghi nguyên văn như mục 8.2 SRS.

## 2. Dữ liệu test dùng chung

| Dữ liệu | Giá trị | Dùng cho |
|---|---|---|
| {{Người đề xuất}} | {{Nguyễn Thu Hà — bộ phận HC, Trưởng nhóm: Phan Thanh Tâm}} | {{FR-01..FR-04}} |

## 3. Test case theo yêu cầu chức năng

### FR-01 — {{Tên FR}}

| TC | AC | Loại | Tiêu đề | Tiền điều kiện | Bước | Kết quả mong đợi | Ưu tiên |
|---|---|---|---|---|---|---|---|
| TC-001 | AC1 | Chức năng | {{Tạo phiếu thành công}} | {{Đăng nhập Người đề xuất}} | {{1) Mở … <br>2) Nhập … <br>3) Bấm "Lưu"}} | {{Phiếu nhận số HC_0012_20_10_26, trạng thái "Nháp"}} | Cao |
| TC-002 | AC3 · BR-01.1 | Ngoại lệ | {{Gửi duyệt phiếu không có dòng}} | {{…}} | {{…}} | {{Hiện lỗi "…"; phiếu giữ "Nháp"}} | Cao |

## 4. Phân quyền
<!-- Từ ma trận phân quyền mục 2.2 SRS: mỗi vai trò × thao tác bị cấm có 1 test case. Cột AC ghi "2.2". -->

| TC | AC | Loại | Tiêu đề | Tiền điều kiện | Bước | Kết quả mong đợi | Ưu tiên |
|---|---|---|---|---|---|---|---|
| TC-0xx | 2.2 | Phân quyền | {{Người đề xuất không xem phiếu của người khác}} | {{…}} | {{…}} | {{…}} | Cao |

## 5. Phi chức năng

### NFR-01 — {{Hiệu năng}}

| TC | AC | Loại | Tiêu đề | Tiền điều kiện | Bước | Kết quả mong đợi | Ưu tiên |
|---|---|---|---|---|---|---|---|
| TC-0xx | — | Phi chức năng | {{…}} | {{…}} | {{…}} | {{p95 ≤ 2 giây với 50 người dùng đồng thời}} | Trung bình |

## 6. Ma trận phủ (RTM)

<!-- tc-matrix:start -->
> Sinh tự động bởi `check_tc.py --write-matrix`.
<!-- tc-matrix:end -->

## 7. Assumptions & Open Questions (phát sinh khi viết test case)

| Mã | Nội dung | Người cần trả lời | Liên quan |
|---|---|---|---|
| {{OQ-xx}} | {{…}} | {{…}} | {{TC-xxx, FR-xx}} |
