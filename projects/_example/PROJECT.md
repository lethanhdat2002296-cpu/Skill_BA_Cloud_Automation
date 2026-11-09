# _example (`_example`)

<!-- card:start -->
> Sinh bởi `python tools/project.py card _example` — không sửa tay đoạn này. Đọc thẻ này TRƯỚC khi mở tài liệu lớn.

- Phiên bản: chưa có tài liệu
- Mã: 0 US · 0 UC · 0 FR · 0 NFR · 0 SCR · 0 AS · 0 OQ
- OQ mở (0): không
- Màn chờ vẽ lại: không
- File: 
- Commit cuối: 2026-11-08 refactor: mỗi dự án một thư mục projects/<du-an>/ (input, docs, diagrams, ui, exports) — khớp Google Drive

## Bản đồ file

| Cần | Mở | Ghi chú |
|---|---|---|
| Biên bản / tài liệu khảo sát | `Document/Bien_Ban_Khao_Sat/` (`_tong-hop.md` là bản hợp nhất — nguồn ưu tiên) | Lịch sử nạp: `_manifest.md`, `_changes/` — đọc change report mới nhất |
| URD (+ brainstorm) | `Document/URD/` | `grep -n "^#### US-07"` rồi Read đoạn đó |
| SRS | `Document/SRS/SRS.md` (nguồn `Document/SRS/srs/*.md`) | Tra mã → file: `build_srs.py <du-an> --index`; Read theo offset |
| FSD | `Document/FSD/` (theo sprint: `FSD/Sprint <n>/`) | `grep -n "^#### "` để xem mục |
| Use case / Backlog | `Document/Use_Case/UC.md`, `Document/Backlog/backlog.md` | |
| Test case | `Document/Test_Case/` (theo sprint: `Test_Case/Sprint <n>/`) | Ma trận phủ ở mục 6 |
| Mã gốc của khách (nếu nhập URD/FSD) | `Document/doi-chieu-ma.md` | `grep -n "REQ-012"` → mã mới |
| Sơ đồ | `Diagram/Flow/` (`swimlanes/*.json` là nguồn) | |
| Màn hình | `Diagram/Wireframe/flows.md`, `screens/SCR-xx-*.html` | Chỉ mở ảnh `png/` khi cần review |
| File Word / CSV xuất ra | `.output/` (không commit) | Đẩy lên Drive: hỏi link thư mục mỗi lần |

<!-- card:end -->

## Ghi chú (viết tay — giữ nguyên khi sinh lại thẻ)

- 
