# Biên bản khảo sát lần 2 — Phiếu "Yêu cầu mua hàng"

| Thuộc tính | Giá trị |
|---|---|
| Nguồn | Chat (BA dự án) |
| Ngày tài liệu | không ghi |
| Ngày nạp | 2026-10-20 |
| Loại | Biên bản khảo sát (ghi chú BA) |

## Tóm tắt
- Vật tư chia 2 loại: "Nhập kho" và "Dịch vụ". Dịch vụ không cần phiếu "Yêu cầu mua hàng" và không tạo phiếu "Nhập kho".
- "Yêu cầu mua hàng" tạo theo 3 cách: trực tiếp từ menu, từ "Hợp đồng", từ "Báo giá". Phát sinh thêm danh mục Hợp đồng và danh mục Báo giá.
- Số phiếu tự tăng theo mẫu "Mã BP _ XXXX_DD_MM_YY". Duyệt theo trình tự Trưởng nhóm (theo người tạo) → User (MH) → BOD.
- Duyệt xong tự tạo "Yêu cầu báo giá": N nhà cung cấp → N phiếu; 1 nhà cung cấp → đúng 1 phiếu.
- Khi chọn vật tư, hệ thống tự hiển thị giá và nhà cung cấp: ưu tiên hợp đồng còn hiệu lực, không có hợp đồng thì lấy Price List.

## Nội dung có cấu trúc

### Phân loại vật tư
- Danh mục vật tư có 2 loại: (1) "Nhập kho", (2) "Dịch vụ".
- Vật tư "Dịch vụ": không cần tạo phiếu "Yêu cầu mua hàng", không tạo phiếu "Nhập kho".
- Vật tư "Dịch vụ" không có hợp đồng.

### Cách tạo phiếu "Yêu cầu mua hàng"
1. Tạo trực tiếp tại menu "Yêu cầu mua hàng".
2. Tạo từ "Hợp đồng" → phát sinh thêm danh mục Hợp đồng.
3. Tạo từ "Báo giá" → phát sinh thêm danh mục Báo giá và chức năng tạo từ "Báo giá".

### Thông tin trong phiếu
- **Đầu phiếu:** Số phiếu tự tăng theo "Mã BP _ XXXX_DD_MM_YY"; thông tin cơ bản như Người tạo, Bộ phận, Ngày tạo, Ghi chú.
- **Chi tiết phiếu:** Vật tư (chỉ được chọn loại "Nhập kho"), Đơn vị tính, Nhập kho, Số lượng, Nhà cung cấp, Ghi chú.
- **Người duyệt theo trình tự:** Trưởng nhóm (theo người tạo) → User (MH) → BOD.

### Chức năng thêm mới
- Duyệt hoàn tất → hệ thống tự tạo phiếu "Yêu cầu báo giá": phiếu "Yêu cầu mua hàng" chứa N nhà cung cấp khác nhau → tạo N phiếu; chỉ 1 nhà cung cấp → tạo đúng 1 phiếu.
- Vật tư đã có hợp đồng nhưng user tạo phiếu từ màn hình "Yêu cầu mua hàng" (không tạo từ hợp đồng): hệ thống tự kiểm tra hợp đồng còn hiệu lực và tự hiển thị giá, nhà cung cấp.
- Áp dụng tương tự cho Price List: khi chọn vật tư, hệ thống tự kiểm tra Price List.
- Quy tắc: ưu tiên hợp đồng trước, rồi đến Price List. Không có hợp đồng → chuyển thẳng đến Price List.

### Quy tắc ràng buộc
- Chi tiết phiếu không được chọn trùng cả vật tư và nhà cung cấp.
- Không được để trống số lượng.

### Việc cần làm
- Cập nhật thông tin khảo sát chi tiết phần "Yêu cầu mua hàng" trước (các phiếu khác sẽ khảo sát tiếp).

## Nguyên văn

```text
Khảo sát lần 2, lần này kỹ hơn nè, đi từng phiếu 1 nhé

1. Tạo "Yêu cầu mua hàng"
   1. Danh mục vật tư sẽ gồm có loại: 1."Nhập kho" | 2."Dịch vụ" . Đối với Dịch vụ sẽ không cần tạo phiếu "Yêu cầu mua hàng" và không tạo phiếu "Nhập kho" 
   2. Tạo phiếu "Yêu cầu mua hàng" gồm 3 phương thức:
      1. Tạo trực tiếp tại Menu "Yêu cầu mua hàng"
      2. Tạo từ "Hợp đồng" -> Phát sinh thêm danh mục hợp đồng
      3. Tạo từ  "Báo giá" -> Phát sinh thêm danh mục báo giá -> phát sinh thêm chức năng tạo từ "Báo giá"
      4. Riêng đối với vật tư "Dịch vụ" không có hợp đồng và không cần tạo phiếu "Yêu cầu mua hàng"
2. Thông tin trong phiếu: 
   1. Đầu phiếu: Số phiếu tự tăng theo "Mã BP _ XXXX_DD_MM_YY" và các thông tin cơ bản như: Người tạo, bộ phận, ngày tạo, ghi chú
   2. Chi tiết phiếu gồm: Vật tư (Chỉ được chọn loại "Nhập kho"), đơn vị tính, Nhập kho, Số lượng, Nhà cung cấp, Ghi chú
   3. Người duyệt theo trình tự: Trưởng nhóm (Theo người tạo) -> User (MH) -> BOD 
3. Các chức năng thêm mới: 
   1. Sau khi duyệt hoàn tất, hệ thống tự động tạo ra phiếu "Yêu cầu báo giá" với quy tắt sau: Trong 1 phiếu "Yêu cầu mua hàng" có chứa nhiếu N nhà cung cấp khác nhau -> Tạo N phiếu "Yêu cầu báo giá". Nếu 1 phiếu "Yêu cầu mua hàng" chỉ chứa duy nhất 1 nhà cung cấp -> hệ thống chỉ tạo đúng 1 phiếu "Yêu cầu báo giá"
   2. Đối với vật tư đã có hợp đồng, mà user không tạo tự hợp đồng mà tạo từ màn hình "Yêu cầu mua hàng", hệ thống tự động kiểm tra nếu hợp đồng còn hiệu lực, sẽ tự động hiển thị giá và NCC. Áp dụng chức năng tương tự cho Price List , là khi chọn vật tư, hệ thống tự kiểm tra trong Price list luôn nhé. Quy tắc: Ưu tiên hợp đồng trước, rồi đến Price List. Trường hợp hợp đồng không có sẽ chuyển thẳng đến Price List luôn
4. Các quy tắc ràng buộc: 
   1. Chi tiết phiếu không được phép chọn cùng vật tư và cùng nhà cung cấp
   2. Không được để trống số lượng 

trước hết update thông tin khảo sát chi tiết về chỗ "Yêu cầu mua hàng" này nhé
```
