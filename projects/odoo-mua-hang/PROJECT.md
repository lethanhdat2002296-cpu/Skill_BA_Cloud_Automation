# Quy trình mua hàng trên Odoo (`odoo-mua-hang`)

<!-- card:start -->
> Sinh bởi `python tools/project.py card odoo-mua-hang` — không sửa tay đoạn này. Đọc thẻ này TRƯỚC khi mở tài liệu lớn.

- Phiên bản: SRS 0.3 · URD 0.3 · UC 0.3 · backlog 0.3
- Mã: 27 US · 19 UC · 27 FR · 10 NFR · 12 SCR · 50 AS · 41 OQ
- OQ mở (29): OQ-03, OQ-10, OQ-12, OQ-13, OQ-14, OQ-15, OQ-17, OQ-18, OQ-19, OQ-20, OQ-21, OQ-22, OQ-24, OQ-25, OQ-26, OQ-27, OQ-28, OQ-29, OQ-30, OQ-31, OQ-32, OQ-34, OQ-35, OQ-36, OQ-37, OQ-38, OQ-39, OQ-40, OQ-41 · trả lời một phần: OQ-02, OQ-05, OQ-07, OQ-08, OQ-09, OQ-23
- Lần cập nhật cuối: 0.3 (2026-10-20) — Trả lời câu hỏi mở lần 1: Odoo 17 Odoo.sh/on-premise; không gộp YCMH; đơn mua không ngưỡng; YCMH bị từ chối về Nháp + email. Khảo sát lần 3 — Yêu cầu báo giá: D
- Màn chờ vẽ lại: không
- Drive: https://drive.google.com/drive/folders/1IMQ4RtmxmevegCtPuIEa0lBXV4Eh2iFD (12 mục)
- File: docs/SRS.md (964 dòng), docs/URD.md (421 dòng), docs/UC.md (706 dòng), docs/backlog.md (382 dòng), ui/flows.md (229 dòng) — SRS chưa tách srs/
- Commit cuối: 2026-11-09 feat(skills): học từ OpenBA-Kit — kiểm câu chữ, danh mục thông báo, skill test case

## Bản đồ file

| Cần | Mở | Ghi chú |
|---|---|---|
| Yêu cầu hợp nhất mới nhất | `input/_tong-hop.md` | Nguồn ưu tiên khi có |
| Lịch sử nạp / khác biệt | `input/_manifest.md`, `input/_changes/` | Đọc change report mới nhất, không đọc hết |
| FR / NFR / SCR / AS / OQ | `docs/SRS.md` (hoặc `docs/srs/*.md`) | Tra mã → file: `build_srs.py <du-an> --index`; Read theo offset |
| User story / Use case | `docs/URD.md`, `docs/UC.md` | `grep -n "^#### US-07"` rồi Read đoạn đó |
| Backlog | `docs/backlog.md` → `exports/backlog.csv` | |
| Mã gốc của khách (nếu nhập URD/FSD) | `docs/doi-chieu-ma.md` | `grep -n "REQ-012"` → mã mới |
| Test case | `docs/test-cases.md` → `exports/test-cases.csv` | Tra `grep -n "^### FR-07"`; ma trận phủ ở mục 6 |
| Màn hình | `ui/flows.md`, `ui/screens/SCR-xx-*.html` | Chỉ mở ảnh `ui/png/` khi cần review |
| Sơ đồ | `diagrams/` (`swimlanes/*.json` là nguồn) | |
| File giao khách | `exports/` | Sinh ra — không sửa tay |

## Google Drive

- Thư mục: https://drive.google.com/drive/folders/1IMQ4RtmxmevegCtPuIEa0lBXV4Eh2iFD
- backlog: https://docs.google.com/spreadsheets/d/1adOzG2a-ytG_RZHqpYfsegqXU2HtSkSJI7hVE0m9_Ho/edit
- srs: https://docs.google.com/document/d/1S25a37GVKYYSSZtl1bKr_IsBpqnW_yFplYplyYy-_kg/edit
- uc: https://docs.google.com/document/d/1CpzMgFVcUjgtdQ6kjVUQYajHib7f8EDTY76fQTUwlbM/edit
- urd: https://docs.google.com/document/d/1MZNt5WJV8ojA-_PdewIwQBTxsxWAuURA0C_SeJvaJOQ/edit

<!-- card:end -->

## Ghi chú (viết tay — giữ nguyên khi sinh lại thẻ)

-
