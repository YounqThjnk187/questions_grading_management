# MỤC LỤC

## PHẦN MỞ ĐẦU

### CHƯƠNG 1: TỔNG QUAN
1.1. Lý do chọn đề tài  
1.2. Mục tiêu đề tài  
1.3. Đối tượng và phạm vi nghiên cứu  
1.4. Phương pháp nghiên cứu  
1.5. Kết quả đạt được  
1.6. Bố cục báo cáo  

### CHƯƠNG 2: XÁC ĐỊNH YÊU CẦU
2.1. Khảo sát hiện trạng  
2.2. Đề xuất giải pháp  
2.3. Yêu cầu chức năng  
&nbsp;&nbsp;&nbsp;&nbsp;2.3.1. Soạn câu hỏi  
&nbsp;&nbsp;&nbsp;&nbsp;2.3.2. Soạn đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;2.3.3. Chấm thi  
&nbsp;&nbsp;&nbsp;&nbsp;2.3.4. Tra cứu đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;2.3.5. Báo cáo năm  
&nbsp;&nbsp;&nbsp;&nbsp;2.3.6. Thay đổi tham số hệ thống  
&nbsp;&nbsp;&nbsp;&nbsp;2.3.7. Đăng nhập hệ thống  
&nbsp;&nbsp;&nbsp;&nbsp;2.3.8. Tra cứu nhanh  
2.4. Yêu cầu phi chức năng  

### CHƯƠNG 3: PHÂN TÍCH YÊU CẦU
3.1. Danh sách Actor  
3.2. Biểu đồ Use Case tổng quát  
3.3. Đặc tả Use Case chi tiết  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.1. UC01 - Đăng nhập hệ thống  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.2. UC02 - Soạn câu hỏi  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.3. UC03 - Soạn đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.4. UC04 - Chấm thi  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.5. UC05 - Tra cứu đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.6. UC06 - Báo cáo năm  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.7. UC07 - Thay đổi tham số  
&nbsp;&nbsp;&nbsp;&nbsp;3.3.8. UC08 - Tra cứu nhanh  
3.4. Biểu đồ hoạt động (Activity Diagram)  

### CHƯƠNG 4: THIẾT KẾ HỆ THỐNG
4.1. Kiến trúc hệ thống  
&nbsp;&nbsp;&nbsp;&nbsp;4.1.1. Mô hình 3 lớp  
&nbsp;&nbsp;&nbsp;&nbsp;4.1.2. Mô hình MVC  
4.2. Biểu đồ Component  
4.3. Biểu đồ Deployment  
4.4. Thiết kế gói (Package Diagram)  

### CHƯƠNG 5: THIẾT KẾ ĐỐI TƯỢNG
5.1. Biểu đồ lớp (Class Diagram)  
5.2. Mô tả các lớp chính  
5.3. Biểu đồ Sequence  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.1. Sequence Diagram - Đăng nhập  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.2. Sequence Diagram - Soạn câu hỏi  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.3. Sequence Diagram - Soạn đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.4. Sequence Diagram - Chấm thi  
&nbsp;&nbsp;&nbsp;&nbsp;5.3.5. Sequence Diagram - Báo cáo năm  

### CHƯƠNG 6: THIẾT KẾ DỮ LIỆU
6.1. Mô hình thực thể liên kết (ERD)  
6.2. Sơ đồ quan hệ  
6.3. Từ điển dữ liệu  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.1. Bảng GIANG_VIEN  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.2. Bảng MON_HOC  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.3. Bảng DO_KHO  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.4. Bảng CAU_HOI  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.5. Bảng DE_THI  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.6. Bảng CT_DETHI  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.7. Bảng LOP_HOC  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.8. Bảng SINH_VIEN  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.9. Bảng KET_QUA  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.10. Bảng BANG_DIEM_CHU  
&nbsp;&nbsp;&nbsp;&nbsp;6.3.11. Bảng THAM_SO  
6.4. Stored Procedures  
6.5. Ràng buộc toàn vẹn dữ liệu  

### CHƯƠNG 7: THIẾT KẾ GIAO DIỆN
7.1. Nguyên tắc thiết kế giao diện  
7.2. Sơ đồ điều hướng  
7.3. Thiết kế màn hình  
&nbsp;&nbsp;&nbsp;&nbsp;7.3.1. Màn hình Đăng nhập  
&nbsp;&nbsp;&nbsp;&nbsp;7.3.2. Màn hình Trang chủ  
&nbsp;&nbsp;&nbsp;&nbsp;7.3.3. Màn hình Quản lý câu hỏi  
&nbsp;&nbsp;&nbsp;&nbsp;7.3.4. Màn hình Soạn đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;7.3.5. Màn hình Chấm thi  
&nbsp;&nbsp;&nbsp;&nbsp;7.3.6. Màn hình Tra cứu đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;7.3.7. Màn hình Báo cáo năm  
&nbsp;&nbsp;&nbsp;&nbsp;7.3.8. Màn hình Tham số hệ thống  
7.4. Design System  
&nbsp;&nbsp;&nbsp;&nbsp;7.4.1. Color Palette  
&nbsp;&nbsp;&nbsp;&nbsp;7.4.2. Typography  
&nbsp;&nbsp;&nbsp;&nbsp;7.4.3. Components  

### CHƯƠNG 8: CÀI ĐẶT PHẦN MỀM
8.1. Môi trường phát triển  
8.2. Công nghệ sử dụng  
&nbsp;&nbsp;&nbsp;&nbsp;8.2.1. ASP.NET MVC 5  
&nbsp;&nbsp;&nbsp;&nbsp;8.2.2. Entity Framework 6  
&nbsp;&nbsp;&nbsp;&nbsp;8.2.3. SQL Server  
&nbsp;&nbsp;&nbsp;&nbsp;8.2.4. Bootstrap & jQuery  
8.3. Cấu trúc thư mục  
8.4. Code mẫu  
&nbsp;&nbsp;&nbsp;&nbsp;8.4.1. Controller  
&nbsp;&nbsp;&nbsp;&nbsp;8.4.2. Model  
&nbsp;&nbsp;&nbsp;&nbsp;8.4.3. View  
8.5. Tối ưu hóa hiệu năng  
&nbsp;&nbsp;&nbsp;&nbsp;8.5.1. Connection Pooling  
&nbsp;&nbsp;&nbsp;&nbsp;8.5.2. Database Indexing  
&nbsp;&nbsp;&nbsp;&nbsp;8.5.3. Caching Strategy  
8.6. Hướng dẫn cài đặt  

### CHƯƠNG 9: KIỂM THỬ VÀ BẢO TRÌ
9.1. Kế hoạch kiểm thử  
9.2. Kiểm thử chức năng  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.1. Test Case - Đăng nhập  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.2. Test Case - Soạn câu hỏi  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.3. Test Case - Soạn đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.4. Test Case - Chấm thi  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.5. Test Case - Tra cứu đề thi  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.6. Test Case - Báo cáo năm  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.7. Test Case - Thay đổi tham số  
&nbsp;&nbsp;&nbsp;&nbsp;9.2.8. Test Case - Tra cứu nhanh  
9.3. Kiểm thử phi chức năng  
&nbsp;&nbsp;&nbsp;&nbsp;9.3.1. Kiểm thử hiệu năng  
&nbsp;&nbsp;&nbsp;&nbsp;9.3.2. Kiểm thử bảo mật  
&nbsp;&nbsp;&nbsp;&nbsp;9.3.3. Kiểm thử khả năng sử dụng  
9.4. Kết quả kiểm thử  
9.5. Kế hoạch bảo trì  

## PHẦN KẾT LUẬN
- Tổng kết
- Đánh giá kết quả đạt được
- Hạn chế và hướng phát triển

## TÀI LIỆU THAM KHẢO

## PHỤ LỤC
- Phụ lục A: Hướng dẫn sử dụng
- Phụ lục B: Source Code chính
- Phụ lục C: Database Script
- Phụ lục D: API Documentation

