---
name: write-testcase
description: Viết test case từ SRS (mỗi AC ≥ 1 TC; ngoại lệ, biên, trạng thái, phân quyền, NFR) + ma trận phủ FR → AC → TC → Document/Test_Case/test-cases.md + .output/test-cases.csv. Chạy khi user nói "viết test case", "làm kịch bản test", "xuất file test cho QA".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *)
---

# write-testcase — Test case & ma trận phủ

Test case biến Acceptance criteria của SRS thành các bước QA chạy được và có kết quả đối chiếu. Chuỗi truy vết: US → UC → FR → **AC → TC**. Không viết test case cho thứ SRS chưa có: thiếu → `OQ-xx`.

Chỉ chạy khi user yêu cầu (không nằm trong `srs-pipeline`): tài liệu này lớn, thường làm khi SRS đã ổn định (sau khách duyệt).

## Input
- `projects/<du-an>/Document/SRS/SRS.md` (bắt buộc; dự án tách `Document/SRS/srs/` thì script tự ghép). Đọc **từng FR** theo `grep -n "^#\{3,4\} FR-"` + `Read` offset — không đọc cả file một lần.
- Mục 2.2 (ma trận phân quyền), 3.0 (bảng chuyển trạng thái), 4 (NFR), 8.2 (danh mục thông báo) của SRS.
- `Document/Use_Case/UC.md` nếu có: nhánh `3a…` để bổ sung TC ngoại lệ.

## Cách làm
1. Đọc `template-tc.md` (khung) và `references.md` (cách suy TC từ AC: biên, bảng quyết định, trạng thái, phân quyền). Giữ cấu trúc, thay hết `{{…}}`.
2. **Mục 2 — Dữ liệu dùng chung:** người dùng mẫu theo vai trò, vật tư / khách hàng / NCC mẫu, cấu hình — lấy đúng tên trong AC của SRS.
3. **Mục 3 — Theo FR** (thứ tự FR trong SRS, heading `### FR-xx — Tên` đúng như SRS; FR đã bỏ thì bỏ qua):
   - Mỗi AC ≥ 1 TC, cột `AC` ghi `AC<n>` (số thứ tự trong SRS), kèm `BR-xx.n` / `UC-xx 3a` nếu TC kiểm quy tắc / nhánh đó.
   - FR `Must`: ít nhất 1 TC `Ngoại lệ`. AC có ngưỡng → thêm TC `Biên` (đúng ngưỡng, ngay dưới, ngay trên).
   - Thông báo trong Kết quả mong đợi chép **nguyên văn** từ AC (cùng chữ với mục 8.2 SRS).
   - Mã `TC-001`, `TC-002`… liên tục toàn tài liệu, 3 chữ số, không tái sử dụng.
   - Ưu tiên: Must → Cao, Should → Trung bình, Could → Thấp.
4. **Mục 3 (tiếp) — Trạng thái:** mỗi dòng bảng chuyển trạng thái (SRS 3.0) có TC `Trạng thái` trong FR tương ứng + 1 TC chuyển không hợp lệ cho mỗi chứng từ.
5. **Mục 4 — Phân quyền:** mỗi thao tác bị cấm quan trọng trong ma trận 2.2 → 1 TC, cột AC = `2.2`.
6. **Mục 5 — Phi chức năng:** mỗi NFR có ngưỡng → 1 TC (`### NFR-xx — Tên`, cột AC = `—`).
7. **Mục 7:** chỉ OQ/AS mới, đánh tiếp số lớn nhất của dự án.

## Kiểm tra + xuất CSV
```bash
python .claude/skills/write-testcase/scripts/check_tc.py <du-an> --write-matrix
```
- `ERROR` (mã trùng, AC/BR/FR trỏ sai, thiếu Bước / Kết quả, Loại sai, placeholder) → sửa hết.
- `WARN` AC chưa phủ, FR chưa có TC, FR Must thiếu TC Ngoại lệ → bổ sung; không bổ sung được (AC mơ hồ) → `OQ-xx` và báo trong báo cáo.
- `--write-matrix` ghi mục 6 (RTM) giữa `<!-- tc-matrix:start -->` / `end` — không sửa tay.
- Sinh `.output/test-cases.csv` (UTF-8 BOM) có sẵn cột Trạng thái = "Chưa chạy", Kết quả thực tế, Người test, Ngày test → QA chạy test trên Excel / Google Sheet.

## Cập nhật (srs-update)
FR / AC đổi → sửa đúng TC có cột `AC` trỏ tới AC đó (`grep -n "| AC3" ` trong mục FR); AC mới → TC mới (số tiếp theo); FR bỏ → thêm `[Đã bỏ — v<ver>]` vào Tiêu đề TC, giữ dòng. Chạy lại `check_tc.py --write-matrix`. Tăng phiên bản trong bảng thuộc tính cùng SRS.

## Output
`projects/<du-an>/Document/Test_Case/test-cases.md`, `projects/<du-an>/.output/test-cases.csv`.
Báo cáo: số TC theo loại, phủ AC (x/y), FR chưa đủ, OQ mới.
