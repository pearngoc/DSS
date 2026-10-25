# DW_Thiet_Ke_4_Buoc_VI (1)

Source: `DW_Thiet_Ke_4_Buoc_VI (1).pdf`  
Slides: 50

## Slide 1 — Quy trình thiết kế chiều 4 bước

Chương trình Thạc sĩ

2026.2027

Hệ hỗ trợ ra quyết định

**Thiết kế Kho dữ liệu**

Giảng viên: TS. Vũ Thị Mỹ Hằng

## Slide 2 — Nội dung

- Ôn tập: Fact và Dimension
- Quy trình 4 bước
- Bước 1: Quy trình nghiệp vụ
- Bước 2: Độ hạt (grain)
- Bước 3: Các chiều
- Bước 4: Các fact
- Kết quả và lỗi thường gặp
- Bài tập vận dụng

## Slide 3 — Nội dung

- **Ôn tập: Fact và Dimension**
- Quy trình 4 bước
- Bước 1: Quy trình nghiệp vụ
- Bước 2: Độ hạt (grain)
- Bước 3: Các chiều
- Bước 4: Các fact
- Kết quả và lỗi thường gặp
- Bài tập vận dụng

## Slide 4 — Bảng Fact & Dimension

**Bảng fact – số đo**

• Một dòng = một **sự kiện đo lường**

• Giá trị số, phần lớn **cộng được**

• Khóa ngoại tới các chiều; khóa phức hợp

- **Sâu và hẹp**: hàng triệu dòng, ít cột

(≈ 90% dung lượng)

• Ví dụ: số lượng bán, doanh thu

**Bảng chiều – ngữ cảnh**

  - **Ai, cái gì, ở đâu, khi nào, tại sao,** **thế nào** của sự kiện

• Thuộc tính mô tả dạng văn bản

• Nguồn của điều kiện lọc, nhóm, nhãn báo cáo

  - **Rộng và nông**: 50–100 thuộc tính, ít dòng

• Ví dụ: thương hiệu, quận của cửa hàng

*Nguồn: Kimball & Ross, The Data Warehouse Toolkit, 3rd ed., 2013, tr. 10–15*

## Slide 5 — Lược đồ hình sao (star schema)

**Chiều Ngày**

**Chiều Cửa hàng**

**Chiều Thu ngân**

**Fact Bán hàng**

**Khóa Ngày, Khóa SP, Khóa CH …**

**Số lượng, Doanh thu**

**Chiều Sản phẩm**

**Chiều Khuyến mãi**

**Chiều Thanh toán**

*Mỗi chiều cách bảng fact đúng một phép kết – đích đến của quy trình 4 bước.*

## Slide 6 — Nội dung

- Ôn tập: Fact và Dimension
- **Quy trình 4 bước**
- Bước 1: Quy trình nghiệp vụ
- Bước 2: Độ hạt (grain)
- Bước 3: Các chiều
- Bước 4: Các fact
- Kết quả và lỗi thường gặp
- Bài tập vận dụng

## Slide 7 — Quy trình thiết kế chiều 4 bước

### 1. Chọn quy

### 2. Tuyên bố 3. Xác định 4. Xác định trình độ hạt các chiều các fact nghiệp vụ

*Muốn đo hoạt Một dòng fact Người dùng mô tả Quy trình này* *động nào? chính xác là gì? sự kiện bằng gì? đo cái gì?*

**Thứ tự là bắt buộc.** Độ hạt (bước 2) là “hợp đồng ràng buộc”: mọi chiều và fact phải khớp với nó.

Nếu ở bước 3 hoặc 4 phát hiện độ hạt sai → quay về bước 2, phát biểu lại, làm lại bước 3–4.

*Nguồn: Kimball & Ross (2013), tr. 38–40, 70–72*

## Slide 8 — Hai đầu vào của mọi quyết định

**Yêu cầu nghiệp vụ**

Phỏng vấn, workshop với chuyên gia nghiệp vụ

**Mô hình chiều**

Quy trình nghiệp vụ

Độ hạt

Các chiều

Các fact

**Thực tế dữ liệu**

Hệ thống nguồn, dữ liệu sẵn có và chất lượng

*“Dữ liệu không thể thay thế ý kiến người dùng nghiệp vụ.” Chỉ nhìn dữ liệu nguồn để mô hình* *hóa là con đường dễ nhất – và hiếm khi thành công.*

*Nguồn: Kimball & Ross (2013), Figure 3-1, tr. 72*

## Slide 9 — Hai case study

**CASE 1 · Bán lẻ POS**

**Bối cảnh:** chuỗi siêu thị 100 cửa hàng,

~60.000 mặt hàng

**Nguồn:** máy quét mã vạch tại quầy

(POS)

**Nhu cầu:** sản phẩm nào bán ở cửa hàng nào, ngày nào, theo khuyến mãi nào

**Tài liệu:** Kimball & Ross (2013), Ch. 3

**CASE 2 · Thương mại điện tử**

**Bối cảnh:** sàn TMĐT trên web và ứng dụng di động

**Nguồn:** Sản phẩm, Khách hàng, Lịch sử tương tác (xem, thêm giỏ, đặt hàng + thời điểm, thiết bị)

**Nhu cầu: tỷ lệ chuyển đổi** xem → đặt hàng theo ngày, tuần, sản phẩm, thể loại

**Tài liệu:** Bài tập 1

*Mỗi bước được áp dụng lần lượt cho cả hai case.*

## Slide 10 — Nội dung

- Ôn tập: Fact và Dimension
- Quy trình 4 bước
- **Bước 1: Quy trình nghiệp vụ**
- Bước 2: Độ hạt (grain)
- Bước 3: Các chiều
- Bước 4: Các fact
- Kết quả và lỗi thường gặp
- Bài tập vận dụng

## Slide 11 — Bước 1: Quy trình nghiệp vụ là gì?

Một hoạt động cấp thấp mà tổ chức thực hiện, tạo ra hoặc ghi nhận các chỉ số

**Động từ hành động**

**1**

**Hệ thống tác nghiệp**

**2**

**Chỉ số hiệu quả**

**3**

hiệu quả

nhận đơn, xuất hóa đơn, đăng ký học phần, xử lý bồi thường

có hệ thống nguồn hỗ trợ: bán hàng, mua hàng, POS

sinh ra số đo mà người dùng muốn lọc, cắt theo vô số cách

**Chuỗi đầu vào → đầu ra** đầu ra quy trình này là đầu vào quy trình sau → chuỗi

**4**

*Nguồn: Kimball & Ross (2013), tr. 70*

bảng fact

## Slide 12 — Quy trình, không phải phòng ban

- **Mô hình theo phòng ban**

• “Mart Marketing”, “Mart Bán hàng”,

“Mart Tài chính”

• Cùng dữ liệu bán hàng bị sao chép 3 lần với nhãn, giá trị khác nhau

• Số liệu không khớp khi họp

  - **Mô hình theo quy trình**

• Một mô hình “Bán lẻ” dùng chung cho mọi phòng ban

• Công bố dữ liệu một lần

• Số liệu nhất quán toàn doanh nghiệp

**Làm quy trình nào trước?** Quy trình vừa **quan trọng nhất** với người dùng vừa **khả thi nhất** (dữ liệu sẵn có, chất lượng tốt, tổ chức sẵn sàng).

Sáng kiến chiến lược (“tăng lòng trung thành”) phải phân rã thành các quy trình trước.

*Nguồn: Kimball & Ross (2013), tr. 71, 74*

## Slide 13 — Bước 1 – Case 1: Chuỗi giá trị bán lẻ

*Các quy trình ứng viên (dòng của bus matrix bán lẻ):*

Đặt hàng nhà cung cấp Nhận hàng vào kho

Tồn kho cửa hàng **Bán lẻ tại quầy (POS)**

**Chọn:** giao dịch bán lẻ tại quầy POS

**CASE 1 · Bán lẻ POS**

Tồn kho tại kho

Khách trả hàng

**Lý do:** ban quản lý muốn hiểu hành vi mua của khách qua máy POS – quan trọng nhất, dữ liệu quét mã vạch sẵn có

**Trả lời được:** sản phẩm nào bán, ở cửa hàng nào, ngày nào, theo khuyến mãi nào, trong giao dịch nào

*Nguồn: Kimball & Ross (2013), tr. 74, 125*

## Slide 14 — Bước 1 – Case 2: Tương tác khách hàng

**CASE 2 · Thương mại điện tử**

*Các quy trình ứng viên trên hành trình khách hàng:*

**Xem sản Thêm vào**

**Đặt hàng** Thanh toán Giao hàng Đổi trả **phẩm giỏ**

**Chọn:** sự kiện tương tác khách hàng – sản phẩm (xem, thêm giỏ, đặt hàng)

**Vì sao gộp thành một?** Cả ba đến từ cùng một nhật ký tương tác và có cùng các chiều (khách, sản phẩm, thời điểm, thiết bị)

**Quy tắc:** nếu các sự kiện có chiều khác nhau → tách thành các bảng fact riêng

Tỷ lệ chuyển đổi cần **hai** loại sự kiện (xem và đặt hàng) → chọn quy trình ghi nhận được cả hai

*Quy tắc theo Kimball & Ross (2013), tr. 117–118*

## Slide 15 — Nội dung

- Ôn tập: Fact và Dimension
- Quy trình 4 bước
- Bước 1: Quy trình nghiệp vụ
- **Bước 2: Độ hạt (grain)**
- Bước 3: Các chiều
- Bước 4: Các fact
- Kết quả và lỗi thường gặp
- Bài tập vận dụng

## Slide 16 — Bước 2: Tuyên bố độ hạt (grain)

Nói chính xác một dòng của bảng fact biểu diễn điều gì – bằng ngôn ngữ

**Ngôn ngữ nghiệp vụ, không**

**1** **phải danh sách khóa**

**Không bỏ qua**

**2**

**Mỗi bảng fact một grain**

**3**

nghiệp vụ

Grain tương đương khóa chính, nhưng liệt kê vài chiều không phải là tuyên bố grain

Thiếu grain: tranh luận về chiều đi vòng tròn, fact “lạc loài” lọt vào

Grain khác nhau → bảng vật lý khác nhau; không trộn

**Do hệ thống nguồn quyết định** Thực tế vật lý của cách hệ thống tác nghiệp ghi nhận sự

**4**

*Nguồn: Kimball & Ross (2013), tr. 39, 71*

kiện

## Slide 17 — Ví dụ tuyên bố độ hạt

**Lĩnh vực**

**Bán lẻ**

**Y tế**

**Hàng không**

**Kho hàng**

**Ngân hàng**

**Tuyên bố độ hạt**

Một dòng cho mỗi lần quét một sản phẩm trong giao dịch của khách

Một dòng cho mỗi dòng mục trên hóa đơn của bác sĩ

Một dòng cho mỗi thẻ lên máy bay được quét tại cửa

Một dòng cho ảnh chụp tồn kho hằng ngày của mỗi mặt hàng trong mỗi kho

Một dòng cho mỗi tài khoản mỗi tháng

**Loại bảng fact**

Giao dịch

Giao dịch

Giao dịch

Ảnh chụp định kỳ

Ảnh chụp định kỳ

**Xử lý đơn hàng** Một dòng cho mỗi dòng đơn hàng, cập nhật ở từng mốc Ảnh chụp tích lũy

*Nguồn: Kimball & Ross (2013), tr. 43–44, 71*

## Slide 18 — Vì sao chọn độ hạt nguyên tử?

Năm × Loại hàng

Tháng × Thương hiệu × Vùng

Ngày × Sản phẩm × Cửa hàng

**Sản phẩm × Giao dịch POS (nguyên tử)**

*Nguồn: Kimball & Ross (2013), tr. 74–75*

Luôn **tổng hợp** được từ dữ liệu nguyên tử **roll-up** …

… nhưng **không bao** **giờ tạo lại chi tiết** từ dữ liệu tổng hợp.

Bảng tổng hợp để tăng tốc, không thay thế.

## Slide 19 — Bước 2 – Case 1: Độ hạt bán lẻ

**CASE 1 · Bán lẻ POS**

**Độ hạt:** một dòng cho mỗi sản phẩm trong một giao dịch POS

*(nhiều lần quét cùng một sản phẩm trong giỏ được gộp thành một dòng)*

**Phương án độ hạt Kết luận**

Sản phẩm × giao dịch POS ✓Chọn

Sản phẩm × cửa hàng × ngày ✗Loại

Cửa hàng × tháng ✗Loại

**Lý do**

Nguyên tử; trả lời mọi câu hỏi bên dưới

Mất chi tiết giao dịch và khuyến mãi

Đoán trước câu hỏi; không có sản phẩm

*Câu hỏi cần dữ liệu nguyên tử: doanh số thứ Hai so với Chủ nhật · số khách dùng phiếu giảm 50 cent cho dầu* *gội · ảnh hưởng khi đối thủ khuyến mãi soda ăn kiêng*

*Nguồn: Kimball & Ross (2013), tr. 75*

## Slide 20 — Bước 2 – Case 2: Độ hạt TMĐT

**CASE 2 · Thương mại điện tử**

**Độ hạt:** một dòng cho mỗi sự kiện tương tác (xem, thêm giỏ, đặt hàng) của

**Phương án độ hạt**

Sự kiện tương tác (nguyên tử)

Sản phẩm × ngày, lưu số đếm

Sản phẩm × ngày, lưu tỷ lệ

khách với một sản phẩm

**Kết luận Lý do**

- Chọn Fact giao dịch; phân tích mọi kỳ, khách, thiết bị
- Tổng hợp Ảnh chụp định kỳ dựng từ bảng nguyên tử
- Loại Tỷ lệ không cộng được → không roll-up

Bài học từ Bài tập 1: lưu **tử số và mẫu số**, không lưu tỷ lệ

## Slide 21 — Nội dung

- Ôn tập: Fact và Dimension
- Quy trình 4 bước
- Bước 1: Quy trình nghiệp vụ
- Bước 2: Độ hạt (grain)
- **Bước 3: Các chiều**
- Bước 4: Các fact
- Kết quả và lỗi thường gặp
- Bài tập vận dụng

## Slide 22 — Bước 3: Xác định các chiều

**Ai Cái gì Ở đâu**

khách hàng, thu ngân sản phẩm cửa hàng, thiết bị

**Khi nào Tại sao Thế nào**

ngày, giờ trong ngày khuyến mãi phương thức thanh toán

**Phép thử đơn trị:** chỉ thêm một chiều nếu nó nhận **đúng một giá trị** ứng với mỗi dòng fact.

Nếu thêm chiều làm phát sinh thêm dòng fact → loại chiều đó, hoặc xem lại độ hạt.

Sau đó bổ sung thuộc tính mô tả đầy đủ cho từng chiều (50–100 thuộc tính là bình thường).

*Nguồn: Kimball & Ross (2013), tr. 40, 72, 76*

## Slide 23 — Bước 3 – Case 1: Các chiều bán lẻ

**Ứng viên**

Ngày

Sản phẩm

Cửa hàng

Khuyến mãi

Thu ngân

Phương thức thanh toán

Số giao dịch POS

Nhân viên trong ca

**Một giá trị cho mỗi dòng hàng POS?**

Có – ngày bán

Có – do độ hạt quy định

Có – nơi diễn ra giao dịch

Có – kể cả dòng “Không khuyến mãi”

Có – người xử lý giao dịch

Có – một phương thức mỗi giao dịch

Có – nhưng không còn thuộc tính

Không – một ca nhiều nhân viên

**CASE 1 · Bán lẻ POS**

**Quyết định**

- Chiều
- Chiều
- Chiều
- Chiều
- Chiều
- Chiều

Chiều suy biến (DD)

- Quy trình khác

*Nguồn: Kimball & Ross (2013), tr. 76, 93; dòng cuối do giảng viên thêm để minh họa*

## Slide 24 — Thuộc tính các chiều bán lẻ

**CASE 1 · Bán lẻ POS**

**Chiều Ngày Chiều Sản phẩm Chiều Cửa hàng Chiều Khuyến mãi**

Ngày Mã SKU (NK) Mã cửa hàng (NK) Mã KM (NK)

Thứ trong tuần Mô tả sản phẩm Tên cửa hàng Tên KM

Tuần / Tháng Thương hiệu Thành phố / Bang Kiểu giảm giá

Quý / Năm Loại hàng Quận Kiểu quảng cáo

Kỳ tài chính Ngành hàng Vùng Kênh truyền thông

Cờ ngày lễ Loại / cỡ bao bì Diện tích Ngày bắt đầu / kết thúc

*Phân cấp Sản phẩm → Thương hiệu → Loại → Ngành nằm phẳng trong một bảng – không snowflake.*

*Nguồn: Kimball & Ross (2013), tr. 79–92*

## Slide 25 — Bước 3 – Case 2: Các chiều TMĐT

**Ứng viên**

Ngày

Giờ trong ngày

Sản phẩm

Khách hàng

Loại tương tác

Thiết bị

Mã tương tác

Thể loại sản phẩm

Kênh marketing

**Một giá trị cho mỗi sự kiện?**

Có – ngày sự kiện (tuần, tháng)

Có – giờ của sự kiện

Có – do độ hạt quy định

Có – người tương tác

Có – xem / thêm giỏ / đặt hàng

Có – web hoặc app

Có – không có thuộc tính

Có – nhưng xác định qua sản phẩm

Nguồn không ghi nhận

**CASE 2 · Thương mại điện tử**

**Quyết định**

- Chiều
- Chiều
- Chiều
- Chiều
- Chiều
- Chiều

Chiều suy biến (DD)

Thuộc tính của SP

- Thiếu dữ liệu

## Slide 26 — Nội dung

- Ôn tập: Fact và Dimension
- Quy trình 4 bước
- Bước 1: Quy trình nghiệp vụ
- Bước 2: Độ hạt (grain)
- Bước 3: Các chiều
- **Bước 4: Các fact**
- Kết quả và lỗi thường gặp
- Bài tập vận dụng

## Slide 27 — Bước 4: Xác định các fact

“Quy trình này đo cái gì?” – mọi fact phải đúng với độ hạt đã tuyên bố

**Cộng được**

Cộng theo mọi chiều

VD: doanh thu, số lượng

**Bán cộng được**

Không cộng theo thời gian

VD: tồn kho, số dư tài khoản

**Không cộng được**

Không bao giờ cộng – tính từ thành phần

VD: đơn giá, biên lãi %, tỷ lệ chuyển đổi

Fact thuộc độ hạt khác phải nằm ở bảng fact khác. Lương cửa hàng trưởng không phải fact của dòng hàng POS.

*Nguồn: Kimball & Ross (2013), tr. 11, 40, 72*

## Slide 28 — Fact dẫn xuất và fact không cộng được

**Dẫn xuất cộng được → lưu**

Lãi gộp = Doanh thu − Giá vốn

Cộng được theo mọi chiều

Tính một lần trong ETL → mọi người, mọi công cụ ra cùng một số

**Tỷ lệ → lưu các thành phần**

Biên lãi gộp = Lãi gộp / Doanh thu

Không cộng, không lấy trung bình được

Lưu tử số và mẫu số; chia sau khi cộng

**Đúng: SUM(LaiGop) / SUM(DoanhThu) Sai: AVG(BienLaiGop)**

*Nguồn: Kimball & Ross (2013), tr. 77–78*

## Slide 29 — Bước 4 – Case 1: Các fact bán lẻ

**Fact (mỗi dòng hàng POS)**

Sales Quantity

Regular / Discount / Net Unit Price

Extended Discount Dollar Amount

Extended Sales Dollar Amount

Extended Cost Dollar Amount

**Tính cộng dồn**

Cộng được

Không cộng được

Cộng được

Cộng được

Cộng được

**CASE 1 · Bán lẻ POS**

**Ghi chú**

Số đơn vị bán

Chỉ để tham chiếu

Số lượng × mức giảm

Số lượng × đơn giá thực

Nếu có giá vốn chuẩn

Extended Gross Profit Dollar Amount Cộng được (dẫn xuất) Doanh thu − giá vốn; lưu

Gross Margin (biên lãi gộp)

Không cộng được

Không lưu; tính ở BI

*Bị loại: lương cửa hàng trưởng, số lượng tồn kho (độ hạt khác / quy trình khác)*

*Nguồn: Kimball & Ross (2013), Figure 3-3, tr. 76–78*

## Slide 30 — Bước 4 – Case 2: Các fact TMĐT

**Fact**

Số lần tương tác (= 1)

Giá sản phẩm tại thời điểm

Số lượt xem

Số lượt thêm giỏ

Số đơn hàng

Tỷ lệ chuyển đổi

**Bảng**

Fact tương tác nguyên tử

Fact tương tác nguyên tử

Fact tổng hợp theo ngày

Fact tổng hợp theo ngày

Fact tổng hợp theo ngày

— (tính trong truy vấn)

**CASE 2 · Thương mại điện tử**

**Tính cộng dồn**

Cộng được

Không cộng được

Cộng được

Cộng được

Cộng được

Không cộng được

**Tỷ lệ chuyển đổi = SUM(SoDonHang) / NULLIF(SUM(SoLuotXem), 0) – ở mọi mức: ngày,** **tuần, tháng, thể loại**

## Slide 31 — Nội dung

- Ôn tập: Fact và Dimension
- Quy trình 4 bước
- Bước 1: Quy trình nghiệp vụ
- Bước 2: Độ hạt (grain)
- Bước 3: Các chiều
- Bước 4: Các fact
- **Kết quả và lỗi thường gặp**
- Bài tập vận dụng

## Slide 32 — Kết quả Case 1: Star schema bán lẻ

**Date Dim**

Date Key (PK)

Day of Week, Month

Quarter, Year

**Store Dim**

Store Key (PK)

Store Number (NK)

District, Region

**Cashier Dim**

Cashier Key (PK)

Employee ID (NK)

Cashier Name

**Retail Sales Fact**

Date Key (FK)

Product Key (FK)

Store Key (FK)

Promotion Key (FK)

Cashier Key (FK)

Payment Method Key (FK)

POS Transaction # (DD)

Sales Quantity

Regular / Discount / Net Unit Price

Extended Discount $

Extended Sales $

Extended Cost $

Extended Gross Profit $

**CASE 1 · Bán lẻ POS**

**Product Dim**

Product Key (PK)

SKU (NK), Description

Brand, Category, Dept

**Promotion Dim**

Promotion Key (PK)

Code (NK), Name

Media Type, Dates

**Payment Method Dim**

Payment Method Key (PK)

Description

Group

*Nguồn: Kimball & Ross (2013), Figure 3-12, tr. 94*

## Slide 33 — Kết quả Case 2: Hai fact, chung chiều

**FactTuongTac (nguyên tử)**

IDNgaySK (FK)

IDGioSK (FK)

MaSPSK (FK)

MaKHSK (FK)

MaLoaiTTSK (FK)

MaThietBiSK (FK)

MaTuongTac (DD)

SoLan = 1

GiaTaiThoiDiem

**DimThoiGian**

Ngày, Tuần

Tháng, Quý, Năm

**DimSanPham**

MaSPNK, TenSP, Gia

TheLoai

**CASE 2 · Thương mại điện tử**

**FactChuyenDoiNgay (tổng hợp)**

IDNgaySK (FK)

MaSPSK (FK)

SoLuotXem

SoLuotThemGio

SoDonHang

ETL: bảng tổng hợp = GROUP BY ngày, sản phẩm từ bảng nguyên tử

Hai bảng fact dùng chung chiều **conform** Thời gian và Sản phẩm →

**Khách hàng · Giờ · Loại TT · Thiết bị** một galaxy nhỏ

## Slide 34 — Lỗi thường gặp theo từng bước

**Bước Lỗi**

**1** Mô hình theo phòng ban (“mart Marketing”)

**1** Gộp các quy trình có chiều khác nhau

**2** Bỏ qua hoặc phát biểu grain mơ hồ

**2** Chọn grain tổng hợp ngay từ đầu

**3** Chiều đa trị ở độ hạt đã chọn

**3** Snowflake phân cấp cố định

**4** Lưu tỷ lệ (chuyển đổi, biên lãi)

**4** Đưa fact của độ hạt khác vào

**Cách sửa**

Mô hình theo quy trình; công bố một lần

Mỗi quy trình một bảng fact

“Một dòng cho mỗi …” bằng từ nghiệp vụ

Bắt đầu nguyên tử; thêm bảng tổng hợp sau

Áp dụng phép thử đơn trị

Làm phẳng vào một bảng chiều

Lưu tử số và mẫu số

Chuyển sang bảng fact khác

## Slide 35 — Nội dung

- Ôn tập: Fact và Dimension
- Quy trình 4 bước
- Bước 1: Quy trình nghiệp vụ
- Bước 2: Độ hạt (grain)
- Bước 3: Các chiều
- Bước 4: Các fact
- Kết quả và lỗi thường gặp
- **Bài tập vận dụng**

## Slide 36 — cdio 4.0 Bài tập 1: Tỷ lệ chuyển đổi (1/2)

Một nền tảng thương mại điện tử ghi nhận hành vi người dùng và đơn hàng. Cần phân tích tỷ lệ chuyển đổi từ lượt xem sản phẩm sang đặt hàng theo ngày, tuần và tháng.

**Tỷ lệ chuyển đổi = Số đơn hàng xác nhận / Số lượt xem (trong cùng kỳ)**

Dữ liệu nguồn:

• Sản phẩm (Mã SP, Tên SP, Ngày sản xuất, Giá, Thể loại) • Khách hàng (Mã KH, Tên KH)

• Lịch sử tương tác (Mã TT, Mã KH, Mã SP, Loại sự kiện, Ngày)

**Mã TT Mã KH Mã SP Loại sự kiện Ngày**

E1 U1 P1 Xem 2025-01-01

E2 U1 P1 Thêm vào giỏ 2025-01-01

E3 U1 P1 Đặt hàng 2025-01-01

E4 U2 P1 Xem 2025-01-01

E5 U3 P1 Xem 2025-01-01

E6 U4 P1 Xem 2025-01-01

E7 U2 P1 Xem 2025-01-02

E8 U2 P1 Đặt hàng 2025-01-02

**Giả định: mỗi sự kiện “Đặt hàng” là một đơn hàng đã xác nhận, chỉ chứa một sản phẩm.**

## Slide 37 — cdio 4.0 Bài tập 1: Tỷ lệ chuyển đổi (2/2)

**Kho dữ liệu (DDS) hiện tại:**

DimThoiGian (IDNgaySK, NgayDayDu, Ngay, Thang, Nam, NamISO, TuanISO, NgayTao, NgayCapNhat)

DimSanPham (MaSPSK, MaSPNK, TenSP, NgaySX, Gia, TheLoai, NgayTao, NgayCapNhat)

FactChuyenDoi (IDNgaySK, MaSPSK, TyLeChuyenDoi, NgayTao, NgayCapNhat)

Có thể tổng hợp (roll-up) tỷ lệ chuyển đổi theo tháng/quý từ FactChuyenDoi hiện tại không? Vì sao? Chứng minh **a** bằng số liệu ngày 01/01 và 02/01.

Giả sử nguồn có thể thêm, sửa, xóa; mã tương tác không tăng theo thời gian và không có cơ chế phát hiện và **b** ghi nhận những thay đổi của dữ liệu trong hệ thống nguồn hoặc cột ghi nhận thời điểm thay đổi. Có thể incremental extract (trích xuất dữ liệu tăng dần) đáng tin cậy không? Đề xuất một giải pháp.

Tuyên bố độ hạt và thiết kế lại FactChuyenDoi để roll-up đúng theo thời gian. Minh họa dữ liệu, viết SQL nạp số **c** đếm và truy vấn tính tỷ lệ theo ngày/tuần/tháng.

**Gợi ý: tỷ lệ là số đo không cộng được; cần tổng hợp tử số và mẫu số trước khi chia.**

## Slide 38 — Bài tập 1 – Hướng dẫn giải (a, b)

**a. Không – tỷ lệ là fact không cộng được; fact đã mất tử số và mẫu số**

**IDNgaySK**

20250101

20250102

Tháng 01

**b. Nạp incremental:**

**Bảng nguồn**

**MaSPSK Lượt xem Đơn hàng**

P1 1 1

P1 1 1

SUM = 200% (vô AVG = 100% (trùng

P1 nghĩa) hợp)

**Incremental? Cách làm**

**TyLeChuyenDoi**

100%

100%

Đúng: 2/2 = 100%

Chỉ ghi thêm; lọc Ngày > mốc lần trước hoặc Mã TT > mã lớn nhất. Ngày

Lịch sử tương tác

Được không có giờ → nạp lại cả ngày gần nhất (xóa–chèn)

Không có ngày cập nhật → full extract, so với bản trước (so cột hoặc

Sản phẩm

Không hash) → SCD

Khách hàng Không Như Sản phẩm; đề xuất thêm cột NgayCapNhat hoặc bật CDC ở nguồn

## Slide 39 — Bài tập 1 – Hướng dẫn giải (c)

DimThoiGian + Tuan, Quy

FactChuyenDoi (

IDNgaySK, MaSPSK,

SoLuotXem, SoDonHang,

NgayTao, NgayCapNhat)

**IDNgaySK MaSPSK**

20250101 1

20250102 1

-- Nạp dữ kiện

INSERT INTO FactChuyenDoi

SELECT t.IDNgaySK, sp.MaSPSK,

SUM(CASE WHEN s.Loai=N'Xem'

THEN 1 ELSE 0 END),

SUM(CASE WHEN s.Loai=N'Đặt hàng'

THEN 1 ELSE 0 END),

GETDATE(), GETDATE()

FROM stg_TuongTac s

JOIN DimThoiGian t

ON t.NgayDayDu = s.Ngay

**SoLuotXem SoDonHang** JOIN DimSanPham sp

ON sp.MaSPNK = s.MaSP

1

1

GROUP BY t.IDNgaySK, sp.MaSPSK;

1

1

-- Roll-up theo tháng

SELECT t.Nam, t.Thang,

1.0*SUM(f.SoDonHang)

/NULLIF(SUM(f.SoLuotXem),0)

FROM FactChuyenDoi f JOIN DimThoiGian t

ON t.IDNgaySK = f.IDNgaySK

GROUP BY t.Nam, t.Thang;

*Tháng 01/2025: 2/2 = 100%. E2 (thêm vào giỏ) không thuộc tử số hay mẫu số.*

## Slide 40 — cdio Bài tập 1 – Hướng dẫn giải (a, b)

**a. Không – tỷ lệ chuyển đổi không cộng được; phải tổng hợp tử số và mẫu số**

**Ngày Sản phẩm Lượt xem Đơn hàng Tỷ lệ**

01/01/2025 P1 4 1

02/01/2025 P1 1 1

Tháng 01 P1 5 2

**Sai: AVG(25%, 100%) = 62,5% Đúng: (1 + 1) / (4 + 1) = 40%**

**b. Incremental Extract: chưa thể bảo đảm đầy đủ thay đổi**

**Bảng nguồn Đánh giá Giải thích / giải pháp**

25%

100%

40%

Lịch sử tương tác Chưa bảo đảm Có thêm, sửa, xóa; mã TT không tăng; thiếu CDC / NgayCapNhat.

Sản phẩm Chưa bảo đảm Thiếu dấu vết cập nhật, xóa; so sánh ảnh chụp nguồn.

Khách hàng Chưa bảo đảm Tương tự sản phẩm; có thể bổ sung CDC / nhật ký thay đổi.

**Giải pháp hiện tại: Full Extract + so sánh với bản trích xuất trước theo khóa nghiệp vụ để phát hiện thêm/sửa/xóa.**

## Slide 41 — cdio Bài tập 1 – Hướng dẫn giải (c)

**Grain: một dòng cho mỗi sản phẩm trong một ngày. Lưu số đếm, không chỉ lưu tỷ lệ.**

FactChuyenDoi (

IDNgaySK, MaSPSK, SoLuotXem, SoDonHang,

NgayTao, NgayCapNhat )

**IDNgaySK MaSPSK SoLuotXem SoDonHang**

20250101 1 4 1

20250102 1 1 1

**Tháng 01/2025: 2 / 5 = 40%**

-- Nạp dữ liệu tổng hợp (lần đầu)

INSERT INTO FactChuyenDoi

(IDNgaySK, MaSPSK, SoLuotXem, SoDonHang)

SELECT t.IDNgaySK, p.MaSPSK,

SUM(CASE WHEN s.Loai=N'Xem' THEN 1 ELSE 0 END),

SUM(CASE WHEN s.Loai=N'Đặt hàng' THEN 1 ELSE 0 END)

FROM Stg_TuongTac s

JOIN DimThoiGian t ON t.NgayDayDu=s.Ngay

JOIN DimSanPham p ON p.MaSPNK=s.MaSP

GROUP BY t.IDNgaySK, p.MaSPSK;

-- Tỷ lệ theo tháng

SELECT t.Nam, t.Thang,

1.0*SUM(f.SoDonHang)/NULLIF(SUM(f.SoLuotXem),0)

AS TyLeChuyenDoi

FROM FactChuyenDoi f JOIN DimThoiGian t

ON f.IDNgaySK=t.IDNgaySK

GROUP BY t.Nam,t.Thang;

Lưu ý: nạp lại cần chống trùng; nếu DimSanPham dùng SCD2, nối đúng phiên bản theo ngày tương tác.

## Slide 42 — Bài tập 1 – Câu c: Lược đồ hình sao

**Độ hạt: một dòng cho mỗi sản phẩm trong mỗi ngày**

**FactChuyenDoi**

**DimThoiGian DimSanPham**

IDNgaySK (PK)

NgayDayDu

Ngay, Tuan, Thang

Quy, Nam

IDNgaySK (FK)

MaSPSK (FK) MaSPSK (PK)

SoLuotXem MaSPNK

SoDonHang TenSP, NgaySX

NgayTao Gia, TheLoai

NgayCapNhat

**Tỷ lệ chuyển đổi = SUM(SoDonHang) / NULLIF(SUM(SoLuotXem), 0)**

**Tổng hợp theo ngày, tuần, tháng, quý hoặc năm bằng DimThoiGian.**

Lưu tử số và mẫu số trong fact; không lưu trực tiếp tỷ lệ để cộng dồn.

## Slide 43 — Bài tập 2 – Thiết kế kho dữ liệu bảo hiểm (1/3)

**cdio**

**Bối cảnh**

Công ty Bảo hiểm Fitchwood chuyên cung cấp các sản phẩm bảo hiểm cho khách hàng. Công ty muốn xây dựng một kho dữ liệu phục vụ hoạt động phân tích bán hàng và tiếp thị.

**Nhóm báo cáo doanh số**

• Tổng doanh số theo tháng/quý, khu vực và loại hợp đồng

• Tổng doanh số theo tháng, đại lý và loại hợp đồng

• Tổng doanh số theo tháng, đại lý và mã bưu chính

**Nhóm báo cáo giá trị hợp đồng**

• Tổng giá trị bảo hiểm theo tháng/quý của ngày hiệu lực

• Tổng giá trị bảo hiểm theo tháng hiệu lực và đại lý

• Tổng giá trị bảo hiểm do từng đại lý bán

**Lưu ý: “doanh số” và “giá trị bảo hiểm” cần được định nghĩa nhất quán với nghiệp vụ.**

## Slide 44 — Bài tập 2 – Thiết kế kho dữ liệu bảo hiểm (2/3)

**cdio**

**Các báo cáo còn lại**

• Số hợp đồng đang có hiệu lực theo đại lý

• Số hợp đồng không còn hiệu lực theo đại lý

• Tổng hoa hồng ban đầu đã trả cho từng đại lý

• Đại lý có doanh số cao nhất theo khu vực và tháng

**Yêu cầu a**

Thiết kế lược đồ hình sao đáp ứng các yêu cầu truy vấn. Đưa ra một hoặc hai ví dụ chứng minh khả năng trả lời của lược đồ.

**Yêu cầu b**

Đề xuất một lược đồ cải tiến theo hướng chuẩn hóa hơn. So sánh ưu điểm, hạn chế với lược đồ hình sao đơn giản.

## Slide 45 — Bài tập 2 – Thiết kế kho dữ liệu bảo hiểm (3/3)

Dữ liệu nguồn:

• Đại lý (Mã đại lý, Tên đại lý, Ngày tuyển dụng, Mã khu vực)

• Khu vực (Mã khu vực, Ngày điều chỉnh gần nhất)

• Thông tin khu vực (Mã khu vực, Mã bưu chính, Thu nhập trung vị, Mật độ dân số, Tuổi trung vị)

• Khách hàng (Mã khách hàng, Tên khách hàng)

• Địa chỉ khách hàng (Mã địa chỉ, Mã khách hàng, Đường, Thành phố, Bang, Mã bưu chính)

• Hợp đồng bảo hiểm (Mã hợp đồng, Mã đại lý, Mã khách hàng, Loại hợp đồng, Còn hiệu lực, Ngày hiệu lực, Giá trị bảo hiểm, Hoa hồng ban đầu, Hoa hồng)

## Slide 46 — Bài tập 2 – Hướng dẫn giải (a): Phân tích

**cdio**

**Bước 1 · Quy trình nghiệp vụ**

Bán/phát hành hợp đồng bảo hiểm và ghi nhận hoa hồng ban đầu.

**Bước 3 · Các chiều**

• Ngày bán; ngày hiệu lực (hai vai trò của chiều ngày)

• Đại lý; khu vực; mã bưu chính

• Loại hợp đồng

**Bước 2 · Tuyên bố độ hạt**

Một dòng cho mỗi hợp đồng được phát hành (giả sử mỗi hợp đồng có một đại lý chính).

**Bước 4 · Các số đo**

• Doanh số: quy ước bằng số hợp đồng bán (= 1) hoặc số tiền bán, tùy định nghĩa

• Giá trị bảo hiểm (face value)

• Hoa hồng ban đầu

**Chú ý: trạng thái hiệu lực thay đổi theo thời gian; muốn báo cáo “tại một thời điểm” cần lưu lịch sử** **hoặc ảnh chụp trạng thái.**

## Slide 47 — Bài tập 2 – Đáp án (a): Lược đồ hình sao

**cdio**

**DimNgay**

NgaySK (PK)

Ngay, Tuan, Thang

Quy, Nam

**DimDaiLy**

DaiLySK (PK)

MaDaiLy, TenDaiLy

KhuVuc, MaBuuChinh

**FactBanHopDong**

MaHopDong (DD)

NgayBanSK (FK)

NgayHieuLucSK (FK)

DaiLySK (FK)

LoaiHopDongSK (FK)

SoHopDong = 1

DoanhSo

GiaTriBaoHiem

HoaHongBanDau

**DimLoaiHopDong**

LoaiHopDongSK (PK)

MaLoai, TenLoai,

## Slide 48 — Bài tập 2 – Đáp án (a): Ví dụ truy vấn

**cdio**

**Ví dụ 1 · Doanh số theo tháng, khu vực và loại hợp đồng**

SELECT n.Nam, n.Thang, a.KhuVuc, l.TenLoai,

SUM(f.DoanhSo) AS TongDoanhSo

FROM FactBanHopDong f

JOIN DimNgay n ON f.NgayBanSK = n.NgaySK

JOIN DimDaiLy a ON f.DaiLySK = a.DaiLySK

JOIN DimLoaiHopDong l ON f.LoaiHopDongSK = l.LoaiHopDongSK

GROUP BY n.Nam, n.Thang, a.KhuVuc, l.TenLoai;

**Ví dụ 2 · Tổng giá trị bảo hiểm theo tháng hiệu lực và đại lý**

SELECT n.Nam, n.Thang, a.MaDaiLy,

SUM(f.GiaTriBaoHiem) AS TongGiaTri

FROM FactBanHopDong f

JOIN DimNgay n ON f.NgayHieuLucSK = n.NgaySK

JOIN DimDaiLy a ON f.DaiLySK = a.DaiLySK

GROUP BY n.Nam, n.Thang, a.MaDaiLy;

## Slide 49 — Bài tập 2 – Hướng dẫn giải (b): Chuẩn hóa

**cdio**

**Phương án chuẩn hóa hơn (snowflake)**

• DimDaiLy → DimKhuVuc → DimMaBuuChinh (tùy quan hệ nghiệp vụ thực tế)

• DimLoaiHopDong → DimNhomSanPham

• Giữ FactBanHopDong ở cùng độ hạt, không đổi ý nghĩa số đo

• Với trạng thái thay đổi theo thời gian: FactTrangThaiHopDongNgay hoặc bảng lịch sử trạng thái

**Ưu điểm Hạn chế so với hình sao**

• Giảm lặp thuộc tính mô tả • Nhiều phép nối khi truy vấn

• Dễ quản lý phân cấp và cập nhật dữ liệu dùng • Khó hiểu hơn đối với người dùng BI chung • ETL và mô hình ngữ nghĩa phức tạp hơn

• Tăng tính nhất quán dữ liệu tham chiếu

**Kết luận: ưu tiên hình sao cho phân tích; chuẩn hóa có chọn lọc khi phân cấp và quản trị dữ liệu thực sự cần.**

## Slide 50 — Ghi nhớ

**1 Quy trình** Mô hình theo quy trình nghiệp vụ, không theo phòng ban

**2 Độ hạt** Tuyên bố đầu tiên, bằng từ nghiệp vụ, ở mức nguyên tử

**3 Chiều**

**4 Fact**

Đơn trị ở độ hạt đã chọn; thuộc tính đầy đủ, phân cấp phẳng

Đúng độ hạt; lưu thành phần cộng được, tính tỷ lệ khi truy vấn

*Tài liệu: R. Kimball & M. Ross, The Data Warehouse Toolkit, 3rd ed., Wiley, 2013 – Ch. 2–4*
