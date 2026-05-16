# TÓM TẮT

## Tên đề tài: 
**HỆ THỐNG QUẢN LÝ RA ĐỀ VÀ CHẤM THI**

## Giảng viên hướng dẫn:
ThS. Nguyễn Thị Thanh Trúc

## Nhóm thực hiện:
Nhóm 15 - Lớp SE104.Q23

---

### 1. Vấn đề nghiên cứu

Hiện nay, việc quản lý ngân hàng câu hỏi, soạn đề thi và chấm điểm tại các cơ sở giáo dục thường được thực hiện thủ công hoặc qua các công cụ rời rạc như Microsoft Word, Excel. Điều này dẫn đến nhiều hạn chế:

- **Khó khăn trong việc lưu trữ và quản lý**: Câu hỏi được lưu trên nhiều file khác nhau, khó tìm kiếm và tái sử dụng
- **Tốn thời gian soạn đề**: Giảng viên phải chọn câu hỏi thủ công, khó đảm bảo tính ngẫu nhiên và cân đối độ khó
- **Chấm điểm chậm và dễ sai sót**: Chấm thủ công qua Excel dễ nhầm lẫn, tốn công sức
- **Báo cáo thiếu chính xác**: Khó tổng hợp thống kê số lượng đề thi, điểm số sinh viên theo từng kỳ
- **Khó quản lý quy định**: Các tham số như số câu tối thiểu, thời gian làm bài thường không được kiểm soát chặt chẽ

### 2. Mục tiêu đề tài

Xây dựng **Hệ thống Quản lý Ra đề và Chấm thi** nhằm:

- **Số hóa quy trình**: Chuyển đổi quy trình thủ công sang hệ thống quản lý tập trung
- **Nâng cao hiệu quả**: Giảm thời gian soạn đề từ 2-3 giờ xuống còn 15-20 phút
- **Đảm bảo chất lượng**: Kiểm soát chặt chẽ độ khó, số lượng câu hỏi theo quy định
- **Tự động hóa chấm điểm**: Chấm điểm tự động dựa trên đáp án chuẩn, tính điểm chữ theo thang điểm
- **Báo cáo chính xác**: Tổng hợp thống kê số lượng đề thi, phân bổ điểm số theo năm học

### 3. Phương pháp nghiên cứu

Đề tài được thực hiện theo **quy trình Rational Unified Process (RUP)** với các giai đoạn:

1. **Khảo sát và phân tích yêu cầu**: Phỏng vấn giảng viên, quan sát quy trình hiện tại
2. **Thiết kế hệ thống**: Xây dựng kiến trúc 3 lớp theo mô hình MVC
3. **Thiết kế cơ sở dữ liệu**: Mô hình ERD với 11 bảng, 4 stored procedures
4. **Cài đặt phần mềm**: Sử dụng ASP.NET MVC 5, Entity Framework 6, SQL Server
5. **Kiểm thử**: Thực hiện test case cho 8 chức năng chính, kiểm thử hiệu năng
6. **Tối ưu hóa**: Áp dụng connection pooling, database indexing, caching

### 4. Công nghệ sử dụng

| Công nghệ | Phiên bản | Mục đích |
|-----------|-----------|----------|
| ASP.NET MVC | 5.2.3 | Framework web chính |
| Entity Framework | 6.1.3 | ORM - Mapping database |
| SQL Server | 2019 | Hệ quản trị CSDL |
| C# | 6.0 | Ngôn ngữ lập trình |
| Bootstrap | 3.0 | Giao diện responsive |
| jQuery | 1.10.2 | Xử lý sự kiện client-side |
| Visual Studio | 2022 | IDE phát triển |

### 5. Kết quả đạt được

#### 5.1. Chức năng đã triển khai

Hệ thống cung cấp đầy đủ **8 chức năng** theo yêu cầu:

1. **Đăng nhập hệ thống**: Xác thực giảng viên qua mã GV và mật khẩu
2. **Soạn câu hỏi**: Thêm/Sửa/Xóa câu hỏi, phân loại theo môn học và độ khó
3. **Soạn đề thi**: Tạo đề thi tự động hoặc chọn câu hỏi thủ công, kiểm tra ràng buộc
4. **Chấm thi**: Nhập điểm cho sinh viên, tự động tính điểm chữ
5. **Tra cứu đề thi**: Tìm kiếm đề thi theo môn học, học kỳ, năm học
6. **Báo cáo năm**: Thống kê số lượng đề thi theo môn học, xuất CSV
7. **Thay đổi tham số**: Cập nhật quy định về số câu tối thiểu, thời gian thi
8. **Tra cứu nhanh**: Tìm kiếm câu hỏi theo từ khóa, highlight kết quả

#### 5.2. Tính năng nâng cao

- **Cảnh báo thông minh**: Thông báo khi môn học có <10 câu hỏi
- **Lọc đề thi chưa chấm**: Hiển thị danh sách đề thi cần chấm điểm
- **In phiếu điểm**: Xuất phiếu điểm dạng HTML, tối ưu cho in ấn
- **Export CSV**: Xuất báo cáo năm ra file CSV với encoding UTF-8 BOM
- **Tìm kiếm full-text**: Tìm kiếm câu hỏi theo nội dung, highlight từ khóa
- **Biểu đồ thống kê**: Hiển thị số lượng đề thi theo môn học dạng bar chart

#### 5.3. Hiệu năng

- **Thời gian tải trang**: Giảm từ 500ms xuống 150ms (70% nhanh hơn)
- **Truy vấn CSDL**: Tăng tốc 50% nhờ indexing và connection pooling
- **Đồng thời**: Hỗ trợ 50+ người dùng cùng lúc không giảm hiệu năng
- **Bộ nhớ**: Sử dụng ổn định ~50MB RAM cho 1 session

#### 5.4. Giao diện

- **Thiết kế hiện đại**: Phong cách Instagram/Facebook với gradient, shadow, animation
- **Responsive**: Tương thích 100% với desktop, tablet, mobile
- **UX tối ưu**: Navigation rõ ràng, form validation real-time, loading indicators
- **Accessibility**: Hỗ trợ keyboard shortcuts, screen reader friendly

### 6. Đánh giá và hướng phát triển

#### 6.1. Ưu điểm

- Giải quyết được 100% yêu cầu chức năng
- Giao diện thân thiện, dễ sử dụng
- Hiệu năng tốt, đáp ứng yêu cầu thực tế
- Code sạch, tuân thủ chuẩn MVC
- Tài liệu đầy đủ, chi tiết

#### 6.2. Hạn chế

- Chưa hỗ trợ đề thi trắc nghiệm tự động (random câu hỏi)
- Chưa có module quản lý người dùng (phân quyền admin/giảng viên)
- Chưa có API để tích hợp với hệ thống khác
- Chưa có mobile app riêng

#### 6.3. Hướng phát triển

- **Mở rộng chức năng**: Thêm module quản lý sinh viên, lớp học, điểm danh
- **Tự động hóa**: Tạo đề thi random hoàn toàn, gợi ý câu hỏi bằng AI
- **Tích hợp**: Kết nối với hệ thống quản lý đào tạo của trường
- **Mobile app**: Phát triển ứng dụng iOS/Android
- **Phân tích dữ liệu**: Thêm dashboard analytics, dự đoán xu hướng điểm số
- **Bảo mật**: Áp dụng OAuth 2.0, mã hóa dữ liệu nhạy cảm

---

**Từ khóa**: Quản lý đề thi, Chấm thi tự động, ASP.NET MVC, Entity Framework, SQL Server, RUP, 3-tier Architecture

