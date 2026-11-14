---
name: write-usecase
description: Viết Use Case UC-xx dạng fully-dressed (tác nhân, kịch bản chính, nhánh 3a, include/extend) + sơ đồ use case + ma trận US ↔ UC ↔ FR → Document/Use_Case/UC.md. Dùng sau URD hoặc khi user nói "viết use case".
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *)
---

# write-usecase — Use Case

Use case mô tả **cách tác nhân đạt một mục tiêu** qua tương tác với hệ thống, gồm cả các nhánh thất bại. User story (URD) nói *cần gì, để làm gì*; use case nói *diễn ra thế nào, sai thì sao*; FR (SRS) nói *hệ thống phải làm gì*. Chuỗi truy vết: US → UC → FR.

## Input
- `projects/<du-an>/Document/URD/URD.md` (bắt buộc — chưa có thì chạy `write-urd` trước): vai trò, user story, AC, mục 4 quy trình TO-BE, AS/OQ.
- `projects/<du-an>/Document/URD/brainstorm.md` mục quy trình và ngoại lệ; `Diagram/Flow/swimlanes/*.json` nếu có.
- `projects/<du-an>/Document/Bien_Ban_Khao_Sat/` chỉ để tra chi tiết.

## Cách làm
1. Đọc `template-uc.md` (khung) và `references.md` (nguyên tắc, ví dụ). Giữ cấu trúc mục, thay hết `{{…}}`.
2. **Tác nhân (mục 1):** mỗi vai trò URD là một tác nhân người; thêm tác nhân hệ thống ngoài (máy chủ email, ngân hàng, hệ thống NCC…) và tác nhân **Thời gian** cho tác vụ định kỳ. Mỗi tác nhân ghi loại: Người / Hệ thống ngoài / Thời gian.
3. **Xác định use case** — mỗi UC = **một mục tiêu của tác nhân chính** ở mức "mục tiêu người dùng" (làm xong trong một lần ngồi, 2–20 phút, xong thì tác nhân có kết quả mang đi được):
   - Gộp các US cùng mục tiêu vào 1 UC (vd. "Tạo YCMH", "Tạo YCMH từ Hợp đồng", "Tự điền giá" → UC "Tạo và gửi Yêu cầu mua hàng" với luồng thay thế). Thường 1 UC phủ 1–4 US.
   - Không tách UC theo từng nút bấm, từng trường, hoặc CRUD lẻ (thêm/sửa/xoá danh mục → 1 UC "Quản lý <danh mục>").
   - Bước duyệt do **tác nhân khác** thực hiện → UC riêng (vd. "Duyệt Yêu cầu mua hàng").
   - Việc hệ thống tự chạy (tạo chứng từ tự động, cron, nhận email) → UC có tác nhân chính "Hệ thống" / "Thời gian", hoặc `include` vào UC kích hoạt nó nếu không có ý nghĩa riêng.
   - Đoạn bước lặp lại ở ≥ 2 UC → tách UC mức "Chức năng con" và `include`. Hành vi tuỳ chọn chen vào UC khác → `extend` (ghi điểm mở rộng).
   - Mã `UC-xx` liên tục toàn tài liệu, không tái sử dụng.
4. **Đặc tả từng UC (mục 4)** theo mẫu fully-dressed trong template, nhóm UC theo phân hệ (`### 4.N <Phân hệ>`):
   - Tên = **động từ + danh từ** theo góc nhìn tác nhân ("Duyệt đơn mua hàng", không phải "Màn hình duyệt").
   - **Kịch bản chính** 3–9 bước, đánh số, mỗi bước một câu *chủ ngữ + động từ* (Tác nhân làm / Hệ thống làm). Chỉ đường đi thành công. Không mô tả giao diện chi tiết (tên nút, vị trí); không `if` trong kịch bản chính.
   - **Luồng thay thế / ngoại lệ**: mã `<số bước><chữ>` (vd. `3a`, `3b`, `*a` = mọi bước). Mỗi nhánh: điều kiện viết như sự thật đã xảy ra ("3a. Dòng thiếu nhà cung cấp:"), các bước con `3a1, 3a2…`, kết thúc bằng "Quay lại bước n" hoặc "Use case kết thúc thất bại". Phủ mọi AC ngoại lệ của US liên quan và mọi ngoại lệ trong brainstorm / swimlane.
   - **Đảm bảo khi thành công** = trạng thái dữ liệu sau khi xong (đo được). **Đảm bảo tối thiểu** = điều hệ thống luôn giữ dù thất bại (không mất dữ liệu đã nhập, ghi log…).
   - Quy tắc nghiệp vụ: dẫn `AS-xx` / quy tắc từ URD; không chép lại FR.
   - `- **Truy vết:** US-01, US-19` — đúng dạng này (script đọc dòng này).
5. **Sơ đồ use case (mục 2):** Mermaid `flowchart LR`, theo mẫu trong template: tác nhân bên ngoài `subgraph` hệ thống, UC là hình `([…])`, `include` / `extend` là mũi tên nét đứt có nhãn. Quá 12 UC → một sơ đồ cho mỗi phân hệ. Không HTML trong nhãn.
6. **AS/OQ (mục 6):** chỉ ghi AS/OQ **mới** phát sinh khi viết UC, đánh tiếp số sau số lớn nhất trong URD (mã toàn dự án). AS/OQ cũ chỉ dẫn mã.
7. Dự án đã có SRS (`SRS.md`): điền mục 5 bằng script (bước dưới). Chưa có SRS: mục 5 chỉ có UC ↔ US; chạy lại script sau `write-srs`.

## Kiểm tra
```bash
python .claude/skills/write-usecase/scripts/check_uc.py <du-an> --write-matrix
```
- `ERROR` (mã trùng, thiếu trường bắt buộc, US không tồn tại trong URD, include/extend trỏ UC không có, nhánh `3a` trỏ bước không có) → sửa hết.
- `WARN` user story `Must` chưa có UC → thêm UC hoặc luồng thay thế; hoặc ghi lý do trong mục 6 nếu US không có tương tác (vd. yêu cầu chung).
- `--write-matrix` ghi lại mục 5 giữa `<!-- uc-matrix:start -->` và `<!-- uc-matrix:end -->` (không sửa tay đoạn này).

## Cập nhật (srs-update)
US đổi / thêm / bỏ → sửa đúng UC liên quan bằng `Edit`; UC bị bỏ giữ heading + `**[Đã bỏ — v<ver>]**` và lý do. Tăng phiên bản trong bảng thuộc tính UC.md cùng phiên bản SRS. Chạy lại `check_uc.py --write-matrix`.

## Output
`projects/<du-an>/Document/Use_Case/UC.md` (+ sơ đồ render vào `Diagram/Flow/uc-NN.png` khi xuất docx: `to_docx.py <du-an> --src UC.md`).
