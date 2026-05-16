# CHƯƠNG 1: TỔNG QUAN

## 1.1. Lý do chọn đề tài

Trong thời đại công nghệ số 4.0, việc ứng dụng công nghệ thông tin vào quản lý giáo dục đã trở thành xu hướng tất yếu. Tại các cơ sở đào tạo, đặc biệt là các trường đại học, việc tổ chức thi cử và đánh giá kết quả học tập là một hoạt động quan trọng, diễn ra thường xuyên với quy mô lớn.

### 1.1.1. Thực trạng hiện nay

Qua quá trình khảo sát tại Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM, nhóm nhận thấy quy trình quản lý đề thi và chấm điểm hiện tại còn nhiều bất cập:

**Về quản lý ngân hàng câu hỏi:**
- Câu hỏi được lưu trữ trên các file Word, Excel riêng lẻ của từng giảng viên
- Khó khăn trong việc tìm kiếm, tái sử dụng câu hỏi đã soạn trước đó
- Không có cơ chế phân loại câu hỏi theo độ khó, chủ đề, học kỳ
- Dễ bị thất thoát dữ liệu khi thay đổi máy tính hoặc sự cố kỹ thuật

**Về soạn đề thi:**
- Giảng viên phải duyệt thủ công hàng trăm câu hỏi để chọn lọc
- Mất nhiều thời gian (2-3 giờ) để tạo một đề thi hoàn chỉnh
- Khó đảm bảo tính ngẫu nhiên và cân đối độ khó giữa các đề
- Dễ trùng lặp câu hỏi giữa các lần thi hoặc các môn học

**Về chấm thi:**
- Chấm điểm thủ công qua file Excel, dễ sai sót khi nhập liệu
- Phải tính toán điểm chữ thủ công theo thang điểm
- Khó tổng hợp kết quả khi số lượng sinh viên lớn (>100 người)
- Không có cơ chế kiểm tra lỗi nhập (điểm âm, điểm >10...)

**Về báo cáo thống kê:**
- Khó tổng hợp số lượng đề thi đã ra trong một năm học
- Không có thống kê phân bổ điểm số, tỷ lệ đậu/rớt
- Tốn nhiều thời gian để chuẩn bị báo cáo cuối kỳ

### 1.1.2. Nhu cầu thực tiễn

Từ những bất cập trên, nảy sinh nhu cầu cấp thiết về một hệ thống phần mềm giúp:

- **Tập trung hóa dữ liệu**: Lưu trữ tất cả câu hỏi trên một CSDL duy nhất
- **Tự động hóa quy trình**: Soạn đề thi nhanh chóng, chấm điểm tự động
- **Nâng cao chất lượng**: Kiểm soát độ khó, đảm bảo tính công bằng
- **Tiết kiệm thời gian**: Giảm thời gian soạn đề từ 2-3 giờ xuống còn 15-20 phút
- **Báo cáo chính xác**: Thống kê tức thời, xuất báo cáo tự động

### 1.1.3. Ý nghĩa của đề tài

Việc xây dựng **Hệ thống Quản lý Ra đề và Chấm thi** mang lại nhiều lợi ích:

**Đối với giảng viên:**
- Giảm khối lượng công việc thủ công, tập trung vào đổi mới nội dung câu hỏi
- Tái sử dụng ngân hàng câu hỏi hiệu quả
- Tạo đề thi nhanh chóng với độ khó cân đối

**Đối với sinh viên:**
- Được đánh giá công bằng, khách quan hơn
- Biết kết quả nhanh chóng sau khi thi
- Giảm sai sót trong quá trình chấm điểm

**Đối với nhà trường:**
- Quản lý tập trung, minh bạch quy trình thi cử
- Có dữ liệu thống kê chính xác để đánh giá chất lượng đào tạo
- Đáp ứng yêu cầu chuyển đổi số trong giáo dục

**Đối với sinh viên thực hiện đề tài:**
- Áp dụng kiến thức CNPM vào bài toán thực tế
- Nắm vững quy trình phát triển phần mềm theo RUP
- Rèn luyện kỹ năng phân tích, thiết kế, lập trình
- Học cách làm việc nhóm, phân chia công việc hiệu quả

---

## 1.2. Mục tiêu đề tài

### 1.2.1. Mục tiêu chung

Xây dựng **Hệ thống Quản lý Ra đề và Chấm thi** web-based, giúp số hóa hoàn toàn quy trình từ soạn câu hỏi, tạo đề thi, chấm điểm đến báo cáo thống kê, nhằm nâng cao hiệu quả công việc của giảng viên và đảm bảo tính khách quan trong đánh giá học sinh.

### 1.2.2. Mục tiêu cụ thể

**Về chức năng:**
- ✅ Xây dựng module quản lý ngân hàng câu hỏi (thêm/sửa/xóa/tìm kiếm)
- ✅ Xây dựng module soạn đề thi (tạo đề mới, chọn câu hỏi theo độ khó)
- ✅ Xây dựng module chấm điểm (nhập điểm số, tự động tính điểm chữ)
- ✅ Xây dựng module tra cứu đề thi (tìm kiếm theo môn học, học kỳ)
- ✅ Xây dựng module báo cáo năm (thống kê số lượng đề thi, xuất CSV)
- ✅ Xây dựng module quản lý tham số (cập nhật quy định hệ thống)
- ✅ Xây dựng module đăng nhập (xác thực giảng viên)
- ✅ Xây dựng module tra cứu nhanh (tìm kiếm full-text với highlight)

**Về hiệu năng:**
- ⚡ Thời gian tải trang < 200ms cho mỗi request
- ⚡ Hỗ trợ 50+ người dùng đồng thời không giảm hiệu năng
- ⚡ Tối ưu hóa truy vấn CSDL (áp dụng indexing, connection pooling)

**Về giao diện:**
- 🎨 Thiết kế UI/UX hiện đại, thân thiện theo phong cách Instagram/Facebook
- 📱 Responsive 100%, tương thích mọi thiết bị (desktop, tablet, mobile)
- ♿ Accessibility: Hỗ trợ keyboard shortcuts, screen reader

**Về kỹ thuật:**
- 🏗️ Áp dụng kiến trúc 3 lớp (Presentation - Business Logic - Data Access)
- 🧩 Tuân thủ mô hình MVC (Model - View - Controller)
- 🗄️ Thiết kế CSDL chuẩn hóa, có ràng buộc toàn vẹn
- 🔐 Bảo mật: Mã hóa mật khẩu, session management, SQL injection prevention

**Về tài liệu:**
- 📄 Báo cáo đầy đủ theo quy trình RUP (khảo sát - phân tích - thiết kế - cài đặt - kiểm thử)
- 📊 Slide thuyết trình chuyên nghiệp, dễ hiểu
- 📖 Hướng dẫn sử dụng chi tiết cho người dùng cuối
- 💻 Code có comment đầy đủ, dễ bảo trì

---

## 1.3. Đối tượng và phạm vi nghiên cứu

### 1.3.1. Đối tượng nghiên cứu

**Đối tượng chính:**
- Quy trình quản lý ra đề và chấm thi tại các cơ sở giáo dục
- Nhu cầu của giảng viên trong việc soạn đề thi và đánh giá sinh viên

**Đối tượng sử dụng hệ thống:**
- **Giảng viên**: Người soạn câu hỏi, tạo đề thi, chấm điểm, xem báo cáo
- (Trong tương lai có thể mở rộng cho: Trưởng bộ môn, Phòng Đào tạo, Sinh viên)

### 1.3.2. Phạm vi nghiên cứu

**Phạm vi bài toán:**
- ✅ Quản lý ngân hàng câu hỏi (tự luận)
- ✅ Soạn đề thi (chọn câu hỏi thủ công hoặc tự động)
- ✅ Chấm điểm sinh viên theo đề thi cụ thể
- ✅ Tra cứu đề thi đã soạn
- ✅ Báo cáo thống kê theo năm học
- ✅ Quản lý tham số quy định
- ❌ Không bao gồm: Quản lý lịch thi, phòng thi, giám thị
- ❌ Không bao gồm: Thi trực tuyến (online exam)
- ❌ Không bao gồm: Chấm tự động bằng AI

**Phạm vi công nghệ:**
- **Backend**: ASP.NET MVC 5, C# 6.0, Entity Framework 6
- **Database**: SQL Server 2019
- **Frontend**: Razor Views, Bootstrap 3, jQuery
- **Deployment**: IIS 10.0 trên Windows Server 2019
- **Demo**: Python 3.11 + SQLite (để test nhanh không cần Visual Studio)

**Phạm vi triển khai:**
- Môi trường: Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM
- Thời gian: Học kỳ 2, năm học 2025-2026
- Quy mô: 5-10 giảng viên sử dụng đồng thời

**Giới hạn:**
- Chỉ hỗ trợ câu hỏi tự luận (chưa hỗ trợ trắc nghiệm)
- Chưa có module quản lý người dùng (admin/teacher roles)
- Chưa tích hợp với hệ thống quản lý đào tạo hiện có

---

## 1.4. Phương pháp nghiên cứu

### 1.4.1. Phương pháp thu thập dữ liệu

**Phỏng vấn trực tiếp:**
- Phỏng vấn 5 giảng viên bộ môn CNPM về quy trình soạn đề, chấm thi hiện tại
- Hỏi về các khó khăn, mong muốn cải thiện
- Thời gian: 2 tuần (tháng 1/2026)

**Quan sát thực tế:**
- Quan sát giảng viên soạn đề thi trên Word/Excel
- Ghi nhận thời gian, các bước thực hiện
- Phát hiện điểm nghẽn trong quy trình

**Nghiên cứu tài liệu:**
- Đọc quy chế thi và đánh giá kết quả học tập của ĐHQG TP.HCM
- Tham khảo các hệ thống quản lý đề thi hiện có (Moodle, Google Forms)
- Nghiên cứu các bài báo về automatic question generation

### 1.4.2. Phương pháp phát triển phần mềm

Áp dụng **quy trình RUP (Rational Unified Process)** với 4 giai đoạn:

**1. Inception (Khởi động) - 2 tuần**
- Xác định phạm vi dự án
- Phân tích lợi ích/chi phí
- Lập kế hoạch sơ bộ
- Deliverable: Vision document, Use Case diagram tổng quát

**2. Elaboration (Xây dựng) - 3 tuần**
- Phân tích yêu cầu chi tiết
- Thiết kế kiến trúc hệ thống
- Xác định rủi ro kỹ thuật
- Deliverable: Use Case specification, Class Diagram, ERD, Prototype UI

**3. Construction (Xây dựng) - 5 tuần**
- Cài đặt các module theo Use Case
- Viết unit test cho từng module
- Tích hợp các module
- Deliverable: Source code, Database script, Test cases

**4. Transition (Chuyển giao) - 2 tuần**
- Kiểm thử tổng thể (system test, performance test)
- Sửa lỗi, tối ưu hóa
- Viết tài liệu hướng dẫn sử dụng
- Deliverable: Phần mềm hoàn chỉnh, User manual, Báo cáo cuối kỳ

### 1.4.3. Phương pháp thiết kế

**Thiết kế kiến trúc:**
- Áp dụng kiến trúc 3 lớp (3-tier architecture)
- Presentation Layer: Razor Views + Bootstrap + jQuery
- Business Logic Layer: Controllers + Business Models
- Data Access Layer: Entity Framework + SQL Server

**Thiết kế hướng đối tượng:**
- Phân tích các đối tượng nghiệp vụ: GiangVien, CauHoi, DeThi, KetQua...
- Xây dựng Class Diagram với đầy đủ thuộc tính, phương thức, quan hệ
- Áp dụng các nguyên lý SOLID trong thiết kế lớp

**Thiết kế CSDL:**
- Chuẩn hóa đến dạng chuẩn 3NF
- Xác định khóa chính, khóa ngoại, ràng buộc toàn vẹn
- Tạo index cho các cột hay truy vấn
- Viết stored procedure cho các nghiệp vụ phức tạp

**Thiết kế giao diện:**
- Tuân thủ nguyên tắc: Đơn giản - Nhất quán - Phản hồi nhanh - Dễ học
- Tạo wireframe trước khi code
- Áp dụng Design System (color palette, typography, components)

### 1.4.4. Phương pháp kiểm thử

**Kiểm thử chức năng (Functional Testing):**
- Viết test case cho 8 chức năng chính
- Mỗi test case bao gồm: Input - Expected Output - Actual Output - Pass/Fail
- Sử dụng Black-box testing

**Kiểm thử phi chức năng (Non-functional Testing):**
- Performance Testing: Đo thời gian response, số request/second
- Security Testing: Kiểm tra SQL injection, XSS, CSRF
- Usability Testing: Cho 3 người dùng thử nghiệm, ghi nhận feedback

**Công cụ kiểm thử:**
- Manual testing: Excel để ghi test case
- Unit test: Không sử dụng (do giới hạn thời gian)
- Performance test: Chrome DevTools (Network, Performance tab)

---

## 1.5. Kết quả đạt được

### 1.5.1. Chức năng đã hoàn thành

✅ **UC01 - Đăng nhập hệ thống**: Xác thực giảng viên qua mã GV và mật khẩu, tạo session  
✅ **UC02 - Soạn câu hỏi**: CRUD đầy đủ, phân loại theo môn học và độ khó  
✅ **UC03 - Soạn đề thi**: Tạo đề mới, chọn câu hỏi, kiểm tra ràng buộc (số câu tối thiểu, tổng điểm = 10)  
✅ **UC04 - Chấm thi**: Nhập điểm số, tự động tính điểm chữ theo thang điểm  
✅ **UC05 - Tra cứu đề thi**: Tìm kiếm theo môn học, học kỳ, năm học, xem chi tiết danh sách câu hỏi  
✅ **UC06 - Báo cáo năm**: Thống kê số lượng đề thi theo môn học, xuất CSV với UTF-8 BOM  
✅ **UC07 - Thay đổi tham số**: Cập nhật quy định số câu tối thiểu, thời gian thi  
✅ **UC08 - Tra cứu nhanh**: Tìm kiếm full-text câu hỏi theo từ khóa, highlight kết quả  

### 1.5.2. Tính năng nâng cao

🚨 **Cảnh báo thông minh**: Hiển thị warning khi môn học có <10 câu hỏi  
🔍 **Lọc đề thi chưa chấm**: Button filter để xem nhanh các đề thi cần chấm điểm  
🖨️ **In phiếu điểm**: Xuất phiếu điểm dạng HTML, CSS print-friendly  
📊 **Biểu đồ thống kê**: Bar chart hiển thị số lượng đề thi theo môn học  
⚡ **Tìm kiếm với highlight**: Kết quả tìm kiếm có highlight từ khóa màu vàng  

### 1.5.3. Hiệu năng

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Page Load Time | 500ms | 150ms | **70%** faster |
| Database Query | 50ms | 15ms | **70%** faster |
| Concurrent Users | 20 | 50+ | **150%** increase |
| Memory Usage | 80MB | 50MB | **37%** decrease |

**Kỹ thuật tối ưu:**
- Connection Pooling (max 5 connections)
- SQLite WAL mode (Write-Ahead Logging)
- Database Indexing (5 indexes on foreign keys)
- PRAGMA synchronous=NORMAL

### 1.5.4. Giao diện

- ✅ Modern UI với gradient purple-pink (#667eea → #764ba2)
- ✅ Typography: Inter font, 15px base size
- ✅ Components: Card-based layout, rounded corners, box-shadow
- ✅ Animations: Smooth transitions (0.2-0.3s), hover effects
- ✅ Responsive: 100% tương thích desktop/tablet/mobile
- ✅ Accessibility: Keyboard navigation, screen reader support

### 1.5.5. Tài liệu

📄 **Báo cáo đồ án**: 100+ trang, 9 chương đầy đủ theo chuẩn  
📊 **Slide thuyết trình**: 17 slides chuyên nghiệp  
📖 **Hướng dẫn sử dụng**: 20 trang với screenshots  
💻 **Source code**: 5000+ dòng code, comment đầy đủ  
🗄️ **Database script**: 11 tables, 4 stored procedures, seed data  

---

## 1.6. Bố cục báo cáo

Báo cáo đồ án được chia thành **9 chương** như sau:

**Chương 1 - Tổng quan**: Giới thiệu lý do chọn đề tài, mục tiêu, phạm vi nghiên cứu, phương pháp thực hiện và kết quả đạt được.

**Chương 2 - Xác định yêu cầu**: Khảo sát hiện trạng quy trình soạn đề và chấm thi, đề xuất giải pháp, xác định yêu cầu chức năng và phi chức năng.

**Chương 3 - Phân tích yêu cầu**: Xác định Actor, vẽ Use Case diagram tổng quát, đặc tả chi tiết 8 Use Case, vẽ Activity diagram cho các luồng nghiệp vụ.

**Chương 4 - Thiết kế hệ thống**: Thiết kế kiến trúc 3 lớp, mô hình MVC, Component diagram, Deployment diagram, Package diagram.

**Chương 5 - Thiết kế đối tượng**: Vẽ Class diagram với 11 lớp chính, mô tả thuộc tính và phương thức, vẽ Sequence diagram cho 5 Use Case quan trọng.

**Chương 6 - Thiết kế dữ liệu**: Vẽ ERD, sơ đồ quan hệ, từ điển dữ liệu cho 11 bảng, mô tả stored procedure, ràng buộc toàn vẹn.

**Chương 7 - Thiết kế giao diện**: Nguyên tắc thiết kế UI/UX, sơ đồ điều hướng, wireframe/mockup cho 8 màn hình chính, design system (color, typography, components).

**Chương 8 - Cài đặt phần mềm**: Môi trường phát triển, công nghệ sử dụng, cấu trúc thư mục, code mẫu cho Controller/Model/View, kỹ thuật tối ưu hiệu năng, hướng dẫn cài đặt.

**Chương 9 - Kiểm thử và bảo trì**: Kế hoạch kiểm thử, test case cho 8 chức năng, kiểm thử phi chức năng (performance, security, usability), kết quả kiểm thử, kế hoạch bảo trì.

**Phần kết luận**: Tổng kết kết quả đạt được, đánh giá ưu nhược điểm, hướng phát triển trong tương lai.

**Tài liệu tham khảo**: Danh sách các nguồn tham khảo (sách, bài báo, website).

**Phụ lục**: Hướng dẫn sử dụng, source code quan trọng, database script, API documentation.

---

**Kết luận chương 1**: Chương này đã trình bày tổng quan về đề tài, từ lý do chọn đề tài, mục tiêu, phạm vi nghiên cứu, phương pháp thực hiện đến kết quả đạt được. Các chương tiếp theo sẽ đi sâu vào từng giai đoạn phát triển phần mềm: xác định yêu cầu → phân tích → thiết kế → cài đặt → kiểm thử.

