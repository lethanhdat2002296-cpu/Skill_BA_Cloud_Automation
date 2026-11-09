---
name: doc-import
description: Nhập tài liệu có sẵn (URD, FSD, SRS của khách hoặc nhóm khác) vào chuẩn của repo — giữ nội dung, bảng đối chiếu mã gốc ↔ mã mới, không sót yêu cầu — rồi chạy tiếp chuỗi từ bước sau. Dùng khi dự án chưa có SRS mà user đưa URD/FSD/SRS có sẵn.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(python *), Bash(python3 *), Bash(pandoc *)
---

# doc-import — nhập URD / FSD / SRS có sẵn

Khác `brainstorm` (phân tích tài liệu khảo sát thô): tài liệu ở đây **đã là đặc tả**. Việc của skill là **chuyển hình thức, giữ nguyên ý**: đưa vào khung URD / SRS của repo, đặt mã của repo, ghi mã gốc để truy ngược, chỗ thiếu → `AS-xx` / `OQ-xx`. Không thêm yêu cầu không có trong tài liệu gốc.

Không hỏi user. Lệnh Python: `python3` nếu có, không thì `python`.

## Bước 0 — Điều kiện
1. Tài liệu đã nằm trong `projects/<du-an>/input/` (chưa có → `ba-intake` trước, `--note "<URD|FSD|SRS> gốc của <ai>, v<x>"`).
2. Dự án **chưa có** `docs/SRS.md`. Đã có SRS → không nhập; tài liệu mới là thay đổi → `ba-intake` (so khác biệt) → `srs-update`.
3. BRD / tài liệu nghiệp vụ chung (mục tiêu, AS-IS/TO-BE, không có yêu cầu chi tiết) → **không** dùng skill này; để `srs-pipeline` chạy từ `brainstorm` như input thường.

## Bước 1 — Dàn ý (không đọc cả file một lần)
```bash
python .claude/skills/doc-import/scripts/import_doc.py <du-an> <file> [--type urd|fsd|srs]
```
- In cây mục `§số Tên [dòng bắt đầu, số dòng, số mã gốc]` + 1 dòng tổng kết (loại đoán được, hệ mã gốc, số bảng/ảnh). User đã nói loại ("đây là FSD") → truyền `--type`.
- File Word được chuyển sang `input/_extracted/<ten>-docx.md` (ảnh trong `<ten>-docx-media/`). Đọc **từng mục** bằng `Read` với `offset` = dòng bắt đầu, `limit` = số dòng.
- Tài liệu > 1.500 dòng: xử lý theo từng chương, viết xong chương này mới đọc chương sau.

## Bước 2 — Chuyển theo loại

| Loại | Viết ra | Bỏ qua trong pipeline |
|---|---|---|
| **URD** (user story, yêu cầu người dùng theo vai trò) | `docs/URD.md` theo `write-urd/template-urd.md` | `brainstorm`, `write-urd` |
| **FSD / SRS** (chức năng, màn hình, trường, validation, quy tắc) | `docs/srs/*.md` theo `write-srs/template-srs.md` + `docs/URD.md` suy ngược | `brainstorm`, `write-urd`, phần viết của `write-srs` |

### URD
- Mỗi yêu cầu / user story gốc → `US-xx` (đánh lại liên tục theo vai trò của repo). Câu chưa theo mẫu "Là … tôi muốn … để …" → viết lại đúng mẫu, giữ ý; thiếu "để …" → suy từ ngữ cảnh nếu rõ, không thì `AS-xx`.
- AC: giữ AC gốc (chuyển sang Given/When/Then). Không có AC → viết AC từ chính câu yêu cầu (quy tắc, giới hạn đã nêu); không đủ để viết → 1 AC tối thiểu + `OQ-xx` "Tiêu chí nghiệm thu của US-xx".
- Ưu tiên: giữ của bản gốc (map sang MoSCoW); không có → `Must` + `AS-xx` "Ưu tiên chưa được nêu, tạm Must".
- Dòng `- **Nguồn:** <file> §<số> (<mã gốc>)` ở mỗi US.

### FSD / SRS
- **Phân hệ** = chương chức năng của tài liệu gốc (giữ tên chương). Mỗi chức năng gốc → `FR-xx` đủ trường template: Mô tả (cuối câu ghi `*(Nguồn: <file> §<số>, <mã gốc>)*`), Vai trò, Truy vết, Input, Output, BR, AC, Ưu tiên.
- Validation / thông báo lỗi trong bản gốc → `BR-xx.n` + AC lỗi với thông báo **nguyên văn** (`hiện lỗi "…"`). Bảng trường của màn hình → Input của FR + dòng SCR trong Screen Inventory (6.1).
- Màn hình / mockup gốc → `SCR-xx` (6.1, 6.2). Ảnh gốc trong `-media/` chỉ để `ui-spec` / `wireframe` tham khảo bố cục; wireframe vẫn vẽ bằng design kit của repo.
- Mục bản gốc không có (ma trận phân quyền, mô hình trạng thái, NFR, tích hợp, từ điển dữ liệu) → điền phần suy ra chắc chắn từ nội dung; còn lại để trống có ghi chú + `OQ-xx`. Không bịa số liệu.
- **URD suy ngược:** vai trò = các vai trò xuất hiện trong FR; mỗi mục tiêu người dùng (gom các FR phục vụ cùng mục tiêu) → 1 `US-xx`, AC lấy từ AC của FR ở mức nghiệp vụ; ghi `- **Nguồn:** suy ra từ <file> (FR-01, FR-02)`. Dòng Truy vết của FR trỏ đúng US đó.
- Phiên bản: `0.1`, Lịch sử phiên bản: `| 0.1 | <ngày> | Nhập từ <file> (bản gốc v<x> của <ai>) | <file> | Toàn bộ |`.

## Bước 3 — Bảng đối chiếu (bắt buộc)
Tạo `docs/doi-chieu-ma.md` theo `template-doi-chieu.md`: mỗi tài liệu gốc một mục `## <tên file trong input/> — <loại> v<x>`, mỗi **mã gốc** (hoặc mỗi **mục lá** nếu bản gốc không đánh mã) một dòng: Mã gốc, Mục gốc (`§số Tên`), tóm tắt, Mã mới, Xử lý (Giữ / Viết lại / Tách / Gộp vào … / Bỏ: lý do / Mâu thuẫn → OQ-xx).

```bash
python .claude/skills/doc-import/scripts/check_import.py <du-an>
```
- `ERROR` mã gốc chưa có dòng, mã mới không tồn tại → sửa hết.
- `WARN` mục chưa đối chiếu, dòng không có mã mới mà không ghi lý do → bổ sung.

## Bước 4 — Chạy tiếp chuỗi
- Gọi từ `srs-pipeline` → quay lại pipeline, **bắt đầu từ bước sau** tài liệu vừa nhập (bảng Bước 2): URD → `write-usecase`; FSD/SRS → `write-usecase`, rồi `build_srs.py` + `check_srs.py` (sửa `ERROR`), `write-user-story`, `ui-spec`, `wireframe`, `render-screens`, Word, tự review, PR.
- Gọi riêng ("nhập FSD cho dự án X") → `build_srs.py` + `check_srs.py` (FSD/SRS), `python tools/project.py card <du-an>`, commit `docs(<du-an>): nhập <loại> từ <file>`, push; gợi ý "Làm SRS cho dự án X" để chạy phần còn lại.

## Báo cáo
```markdown
## Đã nhập <file> (<loại> v<x>) vào <du-an>
- Mã gốc: <n> (<hệ mã>) → <n> US · <n> FR · <n> SCR · đối chiếu: check_import PASS
- Giữ <n> · Viết lại <n> · Tách <n> · Gộp <n> · Bỏ <n> (lý do) · Mâu thuẫn → OQ: <danh sách>
- Phần bản gốc chưa có (đã ghi OQ): phân quyền / trạng thái / NFR / …
```

## Cập nhật sau này
Khách gửi bản mới của chính tài liệu đó → `ba-intake` lưu `__v2` + diff → `srs-update` dùng `docs/doi-chieu-ma.md` để đổi mã gốc trong diff sang mã mới (REQ-012 → FR-02), đổi tiêu đề mục `## <file>` sang file `__v2`, thêm dòng cho mã gốc mới, chạy lại `check_import.py`.
