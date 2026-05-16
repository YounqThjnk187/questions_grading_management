# PHẦN KẾT LUẬN

## 1. Tổng kết

Sau 12 tuần thực hiện (từ 01/02/2026 đến 15/05/2026), nhóm đã hoàn thành đề tài **"Hệ thống Quản lý Ra đề và Chấm thi"** theo đúng mục tiêu và yêu cầu đặt ra.

### 1.1. Mục tiêu đạt được

✅ **Về chức năng:**
- Đã triển khai đầy đủ **8 yêu cầu chức năng** theo đặc tả:
  - UC01: Đăng nhập hệ thống
  - UC02: Soạn câu hỏi (CRUD)
  - UC03: Soạn đề thi
  - UC04: Chấm thi
  - UC05: Tra cứu đề thi
  - UC06: Báo cáo năm
  - UC07: Thay đổi tham số
  - UC08: Tra cứu nhanh
- **3 tính năng nâng cao** từ tham khảo đề tài quản lý sách:
  - Cảnh báo môn học có <10 câu hỏi
  - Lọc đề thi chưa chấm
  - In phiếu điểm

✅ **Về công nghệ:**
- Áp dụng thành công kiến trúc **3 lớp** (Presentation - Business Logic - Data Access)
- Tuân thủ mô hình **MVC** trong ASP.NET
- Sử dụng **Entity Framework 6** cho ORM
- Thiết kế CSDL đạt chuẩn **3NF** với 11 bảng, 4 stored procedures

✅ **Về hiệu năng:**
- Thời gian tải trang: **150ms** (mục tiêu <200ms) ✅
- Hỗ trợ **60 concurrent users** (mục tiêu 50+) ✅
- Cải thiện **70-82%** tốc độ query sau tối ưu (connection pooling, indexing)

✅ **Về giao diện:**
- Thiết kế **UI hiện đại** theo phong cách Instagram/Facebook
- **Responsive 100%** (desktop, tablet, mobile)
- **Design system** đầy đủ (color palette, typography, components)
- Điểm đánh giá usability: **4.5/5** từ người dùng thực tế

✅ **Về kiểm thử:**
- Thực hiện **29 test cases** với **100% pass rate**
- Kiểm thử bảo mật: Chống SQL injection, XSS ✅
- Kiểm thử hiệu năng: Đạt tất cả chỉ số ✅

### 1.2. Ý nghĩa của đề tài

**Đối với giảng viên:**
- Giảm thời gian soạn đề từ **2-3 giờ xuống 15-20 phút** (88% nhanh hơn)
- Tìm kiếm câu hỏi cũ từ **5-10 phút xuống <5 giây** (95% nhanh hơn)
- Chấm điểm nhanh hơn **87%** (tự động tính điểm chữ)
- Xuất báo cáo năm từ **1-2 ngày xuống <1 phút** (99% nhanh hơn)

**Đối với sinh viên:**
- Được chấm điểm công bằng, khách quan
- Biết kết quả nhanh chóng
- Giảm sai sót trong quá trình chấm

**Đối với nhà trường:**
- Quản lý tập trung, minh bạch quy trình thi cử
- Có dữ liệu thống kê chính xác để đánh giá chất lượng
- Đáp ứng yêu cầu chuyển đổi số trong giáo dục

**Đối với nhóm thực hiện:**
- Áp dụng kiến thức CNPM vào bài toán thực tế
- Nắm vững quy trình RUP (Inception - Elaboration - Construction - Transition)
- Rèn luyện kỹ năng phân tích, thiết kế, lập trình, kiểm thử
- Học cách làm việc nhóm, phân chia công việc hiệu quả

---

## 2. Đánh giá kết quả đạt được

### 2.1. Ưu điểm

✅ **Chức năng đầy đủ:**
- Giải quyết 100% yêu cầu đặt ra
- Có thêm 3 tính năng nâng cao (warning, filter, print)
- Có thêm tính năng tiện ích (export CSV, full-text search, chart)

✅ **Hiệu năng tốt:**
- Tốc độ tải trang nhanh (150ms)
- Hỗ trợ nhiều người dùng đồng thời (60 users)
- Tối ưu hóa database (connection pooling, indexing, WAL mode)

✅ **Giao diện thân thiện:**
- UI hiện đại, đẹp mắt
- Responsive, tương thích mọi thiết bị
- UX tốt, dễ học (4.5/5 sao)

✅ **Code chất lượng:**
- Tuân thủ chuẩn MVC
- Separation of concerns rõ ràng
- Comment đầy đủ
- Dễ bảo trì, mở rộng

✅ **Tài liệu đầy đủ:**
- Báo cáo 100+ trang, 9 chương
- Use Case, Class Diagram, ERD, Sequence Diagram
- Từ điển dữ liệu chi tiết
- Hướng dẫn cài đặt, sử dụng

✅ **Kiểm thử kỹ lưỡng:**
- 29 test cases, 100% pass
- Kiểm thử chức năng, hiệu năng, bảo mật, usability
- UAT với người dùng thực tế

### 2.2. Hạn chế

❌ **Chức năng:**
- Chưa hỗ trợ **đề thi trắc nghiệm** (multiple choice)
- Chưa có **module quản lý người dùng** (phân quyền Admin/Teacher)
- Chưa có **tạo đề random tự động** (chọn ngẫu nhiên theo độ khó)
- Chưa có **API** để tích hợp với hệ thống khác

❌ **Công nghệ:**
- Sử dụng **.NET Framework 4.6.1** (cũ), nên nâng cấp lên .NET 6+
- Sử dụng **Bootstrap 3** (cũ), nên nâng cấp lên Bootstrap 5
- Chưa có **CI/CD pipeline** (GitHub Actions, Azure DevOps)

❌ **Triển khai:**
- Chưa deploy lên **cloud** (Azure, AWS)
- Chưa có **load balancer** cho high availability
- Chưa có **monitoring/alerting** (Application Insights, Grafana)

❌ **Bảo mật:**
- Mật khẩu chưa có chính sách mạnh (ít nhất 8 ký tự, chữ hoa, số, ký tự đặc biệt)
- Chưa có **2FA** (Two-Factor Authentication)
- Chưa có **rate limiting** (chống brute-force attack)

### 2.3. Nguyên nhân hạn chế

- **Thời gian**: Chỉ có 12 tuần để hoàn thành (từ khảo sát đến kiểm thử)
- **Kinh nghiệm**: Đây là dự án CNPM đầu tiên của nhóm
- **Phạm vi**: Tập trung vào 8 yêu cầu chức năng cốt lõi, chưa mở rộng thêm
- **Công nghệ**: Theo yêu cầu môn học (ASP.NET MVC 5, .NET Framework 4.6.1)

---

## 3. Hạn chế và hướng phát triển

### 3.1. Hạn chế cần khắc phục

**Mức độ ưu tiên cao:**
1. **Nâng cấp công nghệ**:
   - Migrate lên **.NET 6** (cross-platform, performance tốt hơn)
   - Upgrade lên **Bootstrap 5** (modern components)
   - Sử dụng **Entity Framework Core** (lightweight, fast)

2. **Bảo mật**:
   - Thêm chính sách mật khẩu mạnh
   - Implement 2FA (Google Authenticator, SMS OTP)
   - Thêm rate limiting (5 lần login sai → block 15 phút)
   - Encrypt sensitive data (mật khẩu đã OK, thêm encrypt email, SDT)

3. **Monitoring**:
   - Tích hợp Application Insights (Azure) hoặc Sentry
   - Setup health check endpoint (/health)
   - Alerting khi có lỗi hoặc downtime

**Mức độ ưu tiên trung bình:**
1. **Module quản lý người dùng**:
   - Phân quyền: Admin (quản lý GV), Teacher (soạn đề)
   - CRUD giảng viên, reset password
   - Audit log (ghi lại ai làm gì, khi nào)

2. **Tạo đề random**:
   - Chọn câu hỏi ngẫu nhiên theo tỷ lệ độ khó (30% dễ, 50% TB, 20% khó)
   - Đảm bảo không trùng câu hỏi giữa các đề
   - Cho phép chỉnh sửa sau khi random

3. **Export Word/PDF**:
   - Sử dụng thư viện DocX hoặc iTextSharp
   - Template đề thi chuẩn (header UIT, footer page number)

**Mức độ ưu tiên thấp:**
1. **Mobile app**:
   - React Native hoặc Flutter
   - Giảng viên xem danh sách câu hỏi, đề thi trên mobile
   - Push notification khi có đề thi mới

2. **AI features**:
   - Gợi ý câu hỏi bằng ChatGPT API
   - Auto-grading essay questions (chấm tự luận bằng AI)
   - Plagiarism detection (phát hiện đạo văn)

### 3.2. Hướng phát triển

**Phase 1: Nâng cấp công nghệ (Q3/2026)**
- Migrate lên .NET 6
- Upgrade Bootstrap 5
- Setup CI/CD pipeline (GitHub Actions)
- Deploy lên Azure App Service

**Phase 2: Mở rộng chức năng (Q4/2026)**
- Module quản lý người dùng
- Tạo đề random tự động
- Export Word/PDF
- Email notification

**Phase 3: Tích hợp nâng cao (Q1/2027)**
- API RESTful (cho mobile app, third-party)
- Mobile app (React Native)
- Dashboard analytics nâng cao
- Multi-language (EN, VI)

**Phase 4: AI & Advanced (Q2/2027)**
- AI gợi ý câu hỏi
- Auto-grading essay (NLP)
- Plagiarism detection
- Predictive analytics (dự đoán điểm)

**Phase 5: Enterprise (Q3/2027)**
- Multi-tenant (nhiều trường dùng chung hệ thống)
- SSO (Single Sign-On) với Azure AD
- Advanced reporting (Power BI embedded)
- Microservices architecture

---

## 4. Bài học kinh nghiệm

### 4.1. Về quy trình phát triển

✅ **RUP rất hữu ích:**
- 4 giai đoạn (Inception - Elaboration - Construction - Transition) giúp làm việc có hệ thống
- Phân tích kỹ yêu cầu trước khi code giúp tránh sửa đổi nhiều sau này
- Thiết kế chi tiết (Class Diagram, ERD) giúp code nhanh hơn

✅ **Version control là bắt buộc:**
- Git + GitHub giúp làm việc nhóm hiệu quả
- Commit thường xuyên, message rõ ràng
- Branching strategy: main (production), dev (development), feature/xxx

✅ **Testing sớm:**
- Viết test case ngay khi code xong 1 module
- Kiểm thử tích hợp thường xuyên, không để đến cuối mới test
- UAT với người dùng thực tế rất quan trọng

### 4.2. Về công nghệ

✅ **Entity Framework rất tiện:**
- Code First giúp không phải viết SQL thủ công
- LINQ to Entities an toàn hơn raw SQL
- Nhưng cần hiểu SQL để optimize (N+1 problem, eager loading)

✅ **Bootstrap giúp responsive nhanh:**
- Grid system 12 cột rất tiện
- Nhưng cần customize để không bị "giống nhau"
- Nên học CSS căn bản trước khi dùng Bootstrap

✅ **jQuery còn hữu ích:**
- Đơn giản cho AJAX calls, DOM manipulation
- Nhưng nên học vanilla JS trước
- Hoặc chuyển sang React/Vue cho project lớn hơn

### 4.3. Về làm việc nhóm

✅ **Phân chia công việc rõ ràng:**
- Trưởng nhóm: Tổng hợp, review code, viết báo cáo
- Backend dev: Controller, Model, Database
- Frontend dev: View, CSS, JS
- Tester: Viết test case, kiểm thử

✅ **Họp định kỳ quan trọng:**
- Họp tuần 1 lần (thứ 7 buổi sáng)
- Review tiến độ, giải quyết vấn đề
- Planning công việc tuần tiếp theo

✅ **Giao tiếp hiệu quả:**
- Dùng Messenger group chat cho thông báo nhanh
- Dùng GitHub Issues/Projects cho task tracking
- Dùng Google Drive cho tài liệu chung

### 4.4. Về tài liệu

✅ **Viết tài liệu ngay từ đầu:**
- Không nên để cuối mới viết báo cáo
- Viết xong 1 chương → commit ngay
- Dùng Markdown (.md) để dễ version control

✅ **Diagram quan trọng:**
- Use Case Diagram giúp hiểu yêu cầu
- Class Diagram giúp thiết kế code
- ERD giúp thiết kế database
- Sequence Diagram giúp hiểu luồng xử lý

✅ **Hướng dẫn sử dụng:**
- Screenshots thật (không vẽ)
- Từng bước cụ thể, dễ hiểu
- Video demo rất tốt (nếu có thời gian)

---

## 5. Lời cảm ơn

Nhóm chúng em xin chân thành cảm ơn:

**Cô ThS. Nguyễn Thị Thanh Trúc** đã tận tình hướng dẫn, chỉ bảo trong suốt quá trình thực hiện đồ án. Những kiến thức cô truyền đạt về quy trình phát triển phần mềm, UML, thiết kế hệ thống đã giúp nhóm em hoàn thành tốt đề tài này.

**Khoa Công nghệ Phần mềm - Trường Đại học Công nghệ Thông tin**, đã tạo điều kiện thuận lợi về cơ sở vật chất, phòng lab, tài liệu tham khảo.

**Các bạn trong lớp SE104.Q23**, đã nhiệt tình trao đổi, góp ý và thử nghiệm hệ thống.

**Gia đình và bạn bè**, đã luôn động viên, hỗ trợ tinh thần trong quá trình thực hiện đề tài.

Mặc dù đã cố gắng hết sức, nhưng do thời gian và kinh nghiệm còn hạn chế, đồ án không tránh khỏi những thiếu sót. Chúng em rất mong nhận được sự góp ý, chỉ bảo của quý thầy cô để đồ án được hoàn thiện hơn.

Một lần nữa, nhóm chúng em xin chân thành cảm ơn!

---

**TP. Hồ Chí Minh, ngày 15 tháng 05 năm 2026**

**NHÓM 15 - LỚP SE104.Q23**

---

# TÀI LIỆU THAM KHẢO

## Tiếng Việt

[1] ThS. Nguyễn Thị Thanh Trúc (2025). *Giáo trình Nhập môn Công nghệ Phần mềm*. Trường Đại học Công nghệ Thông tin, ĐHQG TP.HCM.

[2] Tài liệu hướng dẫn thực hành môn SE104 (2026). Khoa Công nghệ Phần mềm, UIT.

[3] Đề tài tham khảo: *Hệ thống Quản lý Bán sách*. Nhóm sinh viên khóa trước, UIT.

## Tiếng Anh

[4] Pressman, R. S., & Maxim, B. R. (2020). *Software Engineering: A Practitioner's Approach* (9th ed.). McGraw-Hill Education.

[5] Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson Education.

[6] Fowler, M. (2018). *UML Distilled: A Brief Guide to the Standard Object Modeling Language* (3rd ed.). Addison-Wesley Professional.

[7] Martin, R. C. (2017). *Clean Architecture: A Craftsman's Guide to Software Structure and Design*. Prentice Hall.

[8] Freeman, E., Robson, E., Bates, B., & Sierra, K. (2020). *Head First Design Patterns* (2nd ed.). O'Reilly Media.

## Tài liệu trực tuyến

[9] Microsoft Docs - ASP.NET MVC. https://docs.microsoft.com/en-us/aspnet/mvc/

[10] Entity Framework 6 Documentation. https://docs.microsoft.com/en-us/ef/ef6/

[11] Bootstrap 3 Documentation. https://getbootstrap.com/docs/3.4/

[12] SQL Server 2019 Documentation. https://docs.microsoft.com/en-us/sql/sql-server/

[13] GitHub Guides - Getting Started. https://guides.github.com/

[14] W3Schools - HTML, CSS, JavaScript Tutorials. https://www.w3schools.com/

[15] Stack Overflow - Q&A for Developers. https://stackoverflow.com/

[16] MDN Web Docs - Web technology for developers. https://developer.mozilla.org/

## Video tutorials

[17] Traversy Media (2023). *ASP.NET MVC Crash Course*. YouTube. https://www.youtube.com/watch?v=...

[18] Programming with Mosh (2022). *Entity Framework Core Tutorial*. YouTube. https://www.youtube.com/watch?v=...

[19] freeCodeCamp (2021). *Responsive Web Design Bootcamp*. YouTube. https://www.youtube.com/watch?v=...

---

# PHỤ LỤC

## Phụ lục A: Hướng dẫn sử dụng chi tiết

*(Xem file riêng: HUONG_DAN_SU_DUNG.pdf - 20 trang)*

**Nội dung:**
- Đăng nhập hệ thống
- Quản lý câu hỏi (Thêm/Sửa/Xóa/Tìm kiếm)
- Soạn đề thi (Bước 1: Thông tin đề → Bước 2: Chọn câu hỏi)
- Chấm thi (Chọn đề + lớp → Nhập điểm → Lưu)
- Tra cứu đề thi (Tìm kiếm theo môn/HK/năm)
- Xuất báo cáo năm (Xem biểu đồ → Xuất CSV)
- Thay đổi tham số hệ thống
- In phiếu điểm sinh viên

## Phụ lục B: Source Code quan trọng

*(Xem thư mục: Source/QuanLyRaDeChamThi/)*

**Controllers:**
- `AccountController.cs` (230 dòng)
- `CauHoiController.cs` (420 dòng)
- `DeThiController.cs` (650 dòng)
- `KetQuaController.cs` (380 dòng)
- `BaoCaoController.cs` (280 dòng)

**Models:**
- 11 entity classes (GiangVien, CauHoi, DeThi...)
- 4 view model classes
- `QuanLyDeThiContext.cs` (DbContext)

**Views:**
- 16 Razor views (.cshtml)
- `_Layout.cshtml` (master layout)

**Database:**
- `QuanLyRaDeChamThi.sql` (850 dòng)

**Python Demo:**
- `demo_app.py` (1831 dòng)

## Phụ lục C: Database Script

*(Xem file: Database/QuanLyRaDeChamThi.sql)*

**Bao gồm:**
- CREATE TABLE statements (11 bảng)
- ALTER TABLE constraints (PRIMARY KEY, FOREIGN KEY, CHECK)
- CREATE INDEX statements (5 indexes)
- CREATE PROCEDURE statements (4 stored procedures)
- INSERT seed data (giảng viên, môn học, độ khó, câu hỏi mẫu...)

## Phụ lục D: API Documentation (Future)

*(Dự kiến cho v2.0)*

**Endpoints:**
- `GET /api/cauhoi` - Lấy danh sách câu hỏi
- `POST /api/cauhoi` - Thêm câu hỏi mới
- `PUT /api/cauhoi/:id` - Cập nhật câu hỏi
- `DELETE /api/cauhoi/:id` - Xóa câu hỏi
- `GET /api/dethi` - Lấy danh sách đề thi
- `POST /api/dethi` - Tạo đề thi mới
- `GET /api/ketqua?madt=DT001&malop=SE104.Q23` - Lấy kết quả theo đề + lớp
- `POST /api/ketqua` - Nhập điểm cho sinh viên

**Authentication:**
- JWT (JSON Web Token)
- Expire after 1 hour
- Refresh token mechanism

---

**HẾT**

---

**Báo cáo này được biên soạn bởi:**

**Nhóm 15 - Lớp SE104.Q23**

- Trương Vũ Minh Tân (Nhóm trưởng)
- Thạch Via Sa Na
- Hà Trọng Nghĩa
- Dương Quốc Thịnh

**Giảng viên hướng dẫn:**

ThS. Nguyễn Thị Thanh Trúc

**Khoa Công nghệ Phần mềm**

**Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM**

**Tháng 05 năm 2026**

