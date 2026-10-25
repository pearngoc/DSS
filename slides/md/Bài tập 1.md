# Bài tập 1

Source: `Bài tập 1.pdf`  
Slides: 1

## Slide 1

Một nền tảng thương mại điện tử thu thập dữ liệu hành vi người dùng và đơn hàng. Cần phân tích tỷ lệ chuyển đổi từ hành vi xem sản phẩm thành hành vi đặt hàng theo ngày và theo tuần. Tỷ lệ chuyển đổi cho biết: trong số các lượt xem sản phẩm có bao nhiêu phần trăm dẫn đến việc đặt hàng. Công thức như sau: Tỷ lệ chuyển đổi = Số lượng đơn hàng / Số lượng lượt xem.

Trong đó: Số lượng đơn hàng: Là tổng số đơn hàng được xác nhận trong khoảng thời gian xét (ngày, tuần, tháng, v.v.). Số lượng lượt xem sản phẩm: Là tổng số lần sản phẩm được xem bởi người dùng trong cùng khoảng thời gian. Giả sử dữ liệu nguồn như sau:

- Sản phẩm (Mã SP, Tên sản phẩm, Ngày sản xuất, Giá, Thể loại sản phẩm)
- Khách hàng (Mã KH, Tên KH)
- Lịch sử tương tác (Mã tương tác, mã KH, Mã SP, Loại tương tác, Ngày)

**Mã tương tác MaKH MaSP Loại sự kiện Ngày**

E1 U1 P1 xem 2025-01-01

E2 U1 P1 Thêm vào giỏ hàng 2025-01-01

E3 U1 P1 Đặt hàng 2025-01-01

E4 U2 P1 xem 2025-01-02

E5 U2 P1 Đặt hàng 2025-01-02

Giả sử DDS được thiết kế như sau:

  - DimThoiGian (IDNgaySK, NgayDayDu, Ngay, Thang, Nam, NgayTao, NgayCapNhat)
  - DimSanPham (MaSPSK, MaSPNK, TenSP, NgaySX, Gia, TheLoai, NgayTao, NgayCapNhat)
  - FactChuyenDoi (IDNgaySK, MaSPSK, TyLeChuyenDoi, NgayTao, NgayCapNhat).

a. Có thể roll-up để tính tỷ lệ chuyển đổi theo tháng/năm (gồm ngày 01/01 và 02/01 dựa trên bảng dữ kiện FactChuyenDoi được không? Vì sao có thể / không thể thực hiện được?

b. Với lược đồ nguồn cho ở trên, có thể thiết kế quy trình nạp dữ liệu vào DDS theo cơ chế incremental extract (chỉ lấy phần dữ liệu mới hoặc thay đổi) hay không? Giải thích ngắn gọn nếu có thể thực hiện. Nếu không thể, hãy nêu 1 giải pháp nạp dữ liệu phù hợp điều kiện hiện tại

c. Thiết kế lại bảng FactChuyenDoi sao cho có thể roll-up để tính tỷ lệ chuyển đổi theo thời gian. Cho dữ liệu minh hoạ cách tính trên thiết kế mới, viết truy vấn tính toán dữ kiện
