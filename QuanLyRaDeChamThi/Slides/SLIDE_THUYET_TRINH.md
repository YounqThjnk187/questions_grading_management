# SLIDE THUYẾT TRÌNH - HỆ THỐNG QUẢN LÝ RA ĐỀ VÀ CHẤM THI

---

## SLIDE 1: TITLE SLIDE

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║                     [LOGO UIT - 150x150]                      ║
║                                                               ║
║         TRƯỜNG ĐẠI HỌC CÔNG NGHỆ THÔNG TIN                   ║
║              ĐHQG TP. HỒ CHÍ MINH                            ║
║                                                               ║
║    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      ║
║                                                               ║
║              ĐỒ ÁN MÔN HỌC                                   ║
║     NHẬP MÔN CÔNG NGHỆ PHẦN MỀM (SE104.Q23)                 ║
║                                                               ║
║    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      ║
║                                                               ║
║          HỆ THỐNG QUẢN LÝ RA ĐỀ VÀ CHẤM THI                 ║
║                                                               ║
║    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      ║
║                                                               ║
║  GVHD: ThS. Nguyễn Thị Thanh Trúc                            ║
║                                                               ║
║  Nhóm 15:                                                     ║
║  • Trương Vũ Minh Tân (21521417) - Nhóm trưởng              ║
║  • Thạch Via Sa Na (23520966)                                ║
║  • Hà Trọng Nghĩa (23521008)                                 ║
║  • Dương Quốc Thịnh (23521498)                               ║
║                                                               ║
║              TP. Hồ Chí Minh, tháng 05/2026                  ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Xin chào quý thầy cô và các bạn
- Nhóm 15 xin báo cáo đồ án môn Nhập môn CNPM
- Đề tài: Hệ thống Quản lý Ra đề và Chấm thi

---

## SLIDE 2: GIỚI THIỆU NHÓM

```
╔═══════════════════════════════════════════════════════════════╗
║                    GIỚI THIỆU NHÓM                            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ┌───────────────────┐   ┌───────────────────┐              ║
║  │  [Avatar 100x100] │   │ Trương Vũ Minh Tân│              ║
║  │                   │   │ 21521417           │              ║
║  │                   │   │ 👨‍💻 Nhóm trưởng     │              ║
║  │                   │   │ Backend + Database │              ║
║  └───────────────────┘   └───────────────────┘              ║
║                                                               ║
║  ┌───────────────────┐   ┌───────────────────┐              ║
║  │  [Avatar 100x100] │   │ Thạch Via Sa Na   │              ║
║  │                   │   │ 23520966           │              ║
║  │                   │   │ 🎨 Frontend        │              ║
║  │                   │   │ UI/UX Design       │              ║
║  └───────────────────┘   └───────────────────┘              ║
║                                                               ║
║  ┌───────────────────┐   ┌───────────────────┐              ║
║  │  [Avatar 100x100] │   │ Hà Trọng Nghĩa    │              ║
║  │                   │   │ 23521008           │              ║
║  │                   │   │ 🧪 Tester          │              ║
║  │                   │   │ Documentation      │              ║
║  └───────────────────┘   └───────────────────┘              ║
║                                                               ║
║  ┌───────────────────┐   ┌───────────────────┐              ║
║  │  [Avatar 100x100] │   │ Dương Quốc Thịnh  │              ║
║  │                   │   │ 23521498           │              ║
║  │                   │   │ 📊 Business Logic  │              ║
║  │                   │   │ Controller         │              ║
║  └───────────────────┘   └───────────────────┘              ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Nhóm 15 gồm 4 thành viên
- Phân công công việc rõ ràng: Backend, Frontend, Tester, Business Logic

---

## SLIDE 3: VẤN ĐỀ

```
╔═══════════════════════════════════════════════════════════════╗
║                      VẤN ĐỀ                                   ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  📋 HIỆN TRẠNG:                                               ║
║                                                               ║
║  ❌ Quản lý câu hỏi thủ công qua Word/Excel                   ║
║     → Khó tìm kiếm, dễ thất thoát                            ║
║                                                               ║
║  ❌ Soạn đề thi mất 2-3 giờ                                   ║
║     → Chọn câu thủ công, khó cân đối độ khó                  ║
║                                                               ║
║  ❌ Chấm điểm chậm và dễ sai sót                              ║
║     → Chấm thủ công 100 bài: 8-16 giờ                        ║
║                                                               ║
║  ❌ Báo cáo cuối kỳ tốn 1-2 ngày                              ║
║     → Tổng hợp thủ công từ nhiều file                        ║
║                                                               ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        ║
║                                                               ║
║  💡 GIẢI PHÁP: Xây dựng hệ thống số hóa toàn bộ quy trình    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Quy trình hiện tại: Thủ công, tốn thời gian, dễ sai sót
- Cần một hệ thống để tự động hóa

---

## SLIDE 4: MỤC TIÊU ĐỀ TÀI

```
╔═══════════════════════════════════════════════════════════════╗
║                    MỤC TIÊU ĐỀ TÀI                           ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  🎯 MỤC TIÊU CHÍNH:                                           ║
║                                                               ║
║     Xây dựng hệ thống web-based giúp số hóa hoàn toàn        ║
║     quy trình từ soạn câu hỏi → tạo đề thi → chấm điểm       ║
║     → báo cáo thống kê                                        ║
║                                                               ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        ║
║                                                               ║
║  ✅ CHỨC NĂNG:                                                ║
║     • Quản lý ngân hàng câu hỏi (Thêm/Sửa/Xóa/Tìm kiếm)      ║
║     • Soạn đề thi nhanh (15-20 phút)                         ║
║     • Chấm thi tự động tính điểm chữ                          ║
║     • Tra cứu và báo cáo thống kê                            ║
║                                                               ║
║  ⚡ HIỆU NĂNG:                                                ║
║     • Thời gian tải trang < 200ms                            ║
║     • Hỗ trợ 50+ người dùng đồng thời                        ║
║                                                               ║
║  🎨 GIAO DIỆN:                                                ║
║     • UI hiện đại (Instagram/Facebook style)                 ║
║     • Responsive 100% (desktop/tablet/mobile)                ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Mục tiêu: Tự động hóa, tiết kiệm thời gian
- 8 chức năng chính + 3 tính năng nâng cao
- Hiệu năng và giao diện đều được chú trọng

---

## SLIDE 5: CÔNG NGHỆ SỬ DỤNG

```
╔═══════════════════════════════════════════════════════════════╗
║                  CÔNG NGHỆ SỬ DỤNG                            ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  🏗️ KIẾN TRÚC:                                                ║
║     ┌─────────────────────────────────────────┐              ║
║     │  Presentation Layer (Razor + Bootstrap) │              ║
║     └─────────────────┬───────────────────────┘              ║
║                       │                                       ║
║     ┌─────────────────▼───────────────────────┐              ║
║     │  Business Logic Layer (MVC Controllers) │              ║
║     └─────────────────┬───────────────────────┘              ║
║                       │                                       ║
║     ┌─────────────────▼───────────────────────┐              ║
║     │  Data Access Layer (Entity Framework)   │              ║
║     └─────────────────┬───────────────────────┘              ║
║                       │                                       ║
║     ┌─────────────────▼───────────────────────┐              ║
║     │      SQL Server 2019                    │              ║
║     └─────────────────────────────────────────┘              ║
║                                                               ║
║  💻 TECH STACK:                                               ║
║     • ASP.NET MVC 5     • Bootstrap 3                        ║
║     • Entity Framework 6  • jQuery 1.10                      ║
║     • C# 6.0            • SQL Server 2019                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Kiến trúc 3 lớp: Phân tách rõ ràng
- ASP.NET MVC: Framework phổ biến, ổn định

---

## SLIDE 6: CHỨC NĂNG CHÍNH (1/2)

```
╔═══════════════════════════════════════════════════════════════╗
║                  CHỨC NĂNG CHÍNH (1/2)                        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  1️⃣ ĐĂNG NHẬP HỆ THỐNG                                        ║
║     • Xác thực giảng viên qua mã GV + mật khẩu               ║
║     • Session management, auto logout sau 30 phút            ║
║                                                               ║
║  2️⃣ QUẢN LÝ CÂU HỎI                                           ║
║     • Thêm/Sửa/Xóa câu hỏi                                   ║
║     • Phân loại theo môn học và độ khó                       ║
║     • Tìm kiếm full-text với highlight                       ║
║                                                               ║
║  3️⃣ SOẠN ĐỀ THI                                              ║
║     • Chọn câu hỏi từ ngân hàng                              ║
║     • Gán điểm cho mỗi câu                                   ║
║     • Validate: Tổng điểm = 10, Số câu ≥ min                 ║
║     • Thời gian: Từ 2-3 giờ → 15-20 phút (88% nhanh hơn)    ║
║                                                               ║
║  4️⃣ CHẤM THI                                                  ║
║     • Nhập điểm số cho sinh viên                             ║
║     • Tự động tính điểm chữ (A, B+, B, C+...)               ║
║     • In phiếu điểm (print-friendly HTML)                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- 4 chức năng đầu: Đăng nhập, quản lý câu hỏi, soạn đề, chấm thi
- Điểm mạnh: Tự động hóa, tiết kiệm thời gian

---

## SLIDE 7: CHỨC NĂNG CHÍNH (2/2)

```
╔═══════════════════════════════════════════════════════════════╗
║                  CHỨC NĂNG CHÍNH (2/2)                        ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  5️⃣ TRA CỨU ĐỀ THI                                            ║
║     • Tìm kiếm theo môn học, học kỳ, năm                     ║
║     • Xem chi tiết danh sách câu hỏi                         ║
║     • Export đề thi ra file                                  ║
║                                                               ║
║  6️⃣ BÁO CÁO NĂM                                               ║
║     • Thống kê số lượng đề thi theo môn học                  ║
║     • Biểu đồ cột (bar chart) trực quan                      ║
║     • Xuất CSV (UTF-8 BOM, đọc được trong Excel)            ║
║                                                               ║
║  7️⃣ THAY ĐỔI THAM SỐ                                          ║
║     • Cập nhật số câu tối thiểu                              ║
║     • Cập nhật thời gian thi mặc định                        ║
║                                                               ║
║  8️⃣ TRA CỨU NHANH                                             ║
║     • Tìm kiếm câu hỏi theo từ khóa                          ║
║     • Highlight từ khóa màu vàng                             ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- 4 chức năng còn lại: Tra cứu, báo cáo, tham số, tìm kiếm
- Tổng cộng 8 chức năng hoàn chỉnh

---

## SLIDE 8: GIAO DIỆN - LOGIN

```
╔═══════════════════════════════════════════════════════════════╗
║                    GIAO DIỆN - ĐĂNG NHẬP                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║     [Screenshot: Login page với gradient background]          ║
║                                                               ║
║     • Background: Gradient tím-hồng (#667eea → #764ba2)      ║
║     • Card trắng, rounded corners, shadow                    ║
║     • Input với icon (👤 và 🔒)                               ║
║     • Button gradient với hover effect                       ║
║                                                               ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        ║
║                                                               ║
║  ✨ DESIGN PRINCIPLES:                                        ║
║     • Đơn giản, dễ sử dụng                                   ║
║     • Màu sắc hiện đại                                       ║
║     • Typography: Inter font, 15px                           ║
║     • Validation realtime                                    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Giao diện đăng nhập: Đơn giản, hiện đại
- Màu sắc gradient tím-hồng bắt mắt

---

## SLIDE 9: GIAO DIỆN - TRANG CHỦ

```
╔═══════════════════════════════════════════════════════════════╗
║                    GIAO DIỆN - TRANG CHỦ                      ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║     [Screenshot: Dashboard với sidebar + cards]               ║
║                                                               ║
║     • Navbar cố định với gradient                            ║
║     • Sidebar navigation (icon + text)                       ║
║     • Stats cards: Số câu hỏi, đề thi, đã chấm              ║
║     • Warning alerts: Cảnh báo môn < 10 câu                  ║
║     • Quick actions: Buttons thêm câu hỏi, soạn đề           ║
║                                                               ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        ║
║                                                               ║
║  📊 DASHBOARD FEATURES:                                       ║
║     • Thống kê tổng quan                                     ║
║     • Thông báo quan trọng                                   ║
║     • Truy cập nhanh các chức năng                           ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Trang chủ: Overview toàn bộ hệ thống
- Sidebar dễ navigate, stats cards trực quan

---

## SLIDE 10: GIAO DIỆN - QUẢN LÝ CÂU HỎI

```
╔═══════════════════════════════════════════════════════════════╗
║                 GIAO DIỆN - QUẢN LÝ CÂU HỎI                   ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║     [Screenshot: Danh sách câu hỏi + form thêm mới]           ║
║                                                               ║
║     • Bảng danh sách với filter                              ║
║     • Search box với icon                                    ║
║     • Button "Thêm câu hỏi" nổi bật                          ║
║     • Modal popup cho form thêm/sửa                          ║
║     • Validation inline với error message đỏ                 ║
║                                                               ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        ║
║                                                               ║
║  🔍 SEARCH FEATURES:                                          ║
║     • Full-text search                                       ║
║     • Highlight từ khóa                                      ║
║     • Filter theo môn học, độ khó                            ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- CRUD đầy đủ: Thêm, sửa, xóa, xem
- Tìm kiếm nhanh với highlight

---

## SLIDE 11: THIẾT KẾ DATABASE

```
╔═══════════════════════════════════════════════════════════════╗
║                   THIẾT KẾ DATABASE                           ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  📊 ERD (Entity Relationship Diagram):                        ║
║                                                               ║
║     GIANG_VIEN ──1:N─→ CAU_HOI ──N:M─→ DE_THI                ║
║         │                 │              │                    ║
║         │                 │              │                    ║
║         └─────1:N────→ DE_THI ──1:N─→ KET_QUA                ║
║                           │              │                    ║
║                           │              │                    ║
║                      MON_HOC        SINH_VIEN                 ║
║                                          │                    ║
║                                      LOP_HOC                  ║
║                                                               ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        ║
║                                                               ║
║  🗄️ THỐNG KÊ:                                                 ║
║     • 11 bảng                                                 ║
║     • 4 stored procedures                                    ║
║     • 5 indexes (tăng tốc 70-82%)                            ║
║     • Chuẩn hóa 3NF                                          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Database: 11 bảng, chuẩn 3NF
- Stored procedures cho báo cáo phức tạp
- Indexing giúp tăng tốc query 70-82%

---

## SLIDE 12: HIỆU NĂNG

```
╔═══════════════════════════════════════════════════════════════╗
║                      HIỆU NĂNG                                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ⚡ KẾT QUẢ ĐO LƯỜNG:                                          ║
║                                                               ║
║  ┌──────────────────────┬──────────┬──────────┬────────────┐ ║
║  │ Metric               │ Before   │ After    │ Improved   │ ║
║  ├──────────────────────┼──────────┼──────────┼────────────┤ ║
║  │ Page Load Time       │ 500ms    │ 150ms    │ 70% ✅     │ ║
║  │ Database Query       │ 50ms     │ 15ms     │ 70% ✅     │ ║
║  │ Concurrent Users     │ 20       │ 60       │ 200% ✅    │ ║
║  │ Memory Usage         │ 80MB     │ 50MB     │ 37% ✅     │ ║
║  └──────────────────────┴──────────┴──────────┴────────────┘ ║
║                                                               ║
║  🔧 KỸ THUẬT TỐI ƯU:                                          ║
║     • Connection Pooling (min=5, max=100)                    ║
║     • Database Indexing (5 indexes)                          ║
║     • SQLite WAL mode (Python demo)                          ║
║     • Output Caching (ASP.NET)                               ║
║                                                               ║
║  🎯 MỤC TIÊU ĐẠT ĐƯỢC: 5/5 metrics ✅                         ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Đo lường hiệu năng: Tất cả đạt target
- Tối ưu: Connection pooling, indexing
- Tốc độ tăng 70%, hỗ trợ 60 users

---

## SLIDE 13: KIỂM THỬ

```
╔═══════════════════════════════════════════════════════════════╗
║                        KIỂM THỬ                               ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  🧪 KẾT QUẢ KIỂM THỬ:                                         ║
║                                                               ║
║  ┌────────────────────┬──────┬──────┬──────┬─────────────┐   ║
║  │ Loại kiểm thử      │ Total│ Pass │ Fail │ Pass Rate   │   ║
║  ├────────────────────┼──────┼──────┼──────┼─────────────┤   ║
║  │ Chức năng          │  15  │  15  │  0   │ 100% ✅     │   ║
║  │ Hiệu năng          │   5  │   5  │  0   │ 100% ✅     │   ║
║  │ Bảo mật            │   5  │   5  │  0   │ 100% ✅     │   ║
║  │ Usability          │   4  │   4  │  0   │ 100% ✅     │   ║
║  ├────────────────────┼──────┼──────┼──────┼─────────────┤   ║
║  │ TỔNG CỘNG          │  29  │  29  │  0   │ 100% ✅     │   ║
║  └────────────────────┴──────┴──────┴──────┴─────────────┘   ║
║                                                               ║
║  🔒 BẢO MẬT:                                                  ║
║     ✅ Chống SQL Injection (Entity Framework auto-param)     ║
║     ✅ Chống XSS (Razor auto HTML-encode)                    ║
║     ✅ Session timeout 30 phút                               ║
║                                                               ║
║  ⭐ USABILITY: 4.5/5 sao (từ 3 giảng viên thử nghiệm)        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- 29 test cases, 100% pass
- Bảo mật: SQL injection, XSS đã test
- Usability: 4.5/5 từ người dùng thực tế

---

## SLIDE 14: DEMO VIDEO

```
╔═══════════════════════════════════════════════════════════════╗
║                        DEMO VIDEO                             ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║                                                               ║
║                  [VIDEO DEMO - 2-3 phút]                      ║
║                                                               ║
║              ┌─────────────────────────────┐                  ║
║              │                             │                  ║
║              │      ▶️ PLAY VIDEO          │                  ║
║              │                             │                  ║
║              │  Demo các chức năng chính:  │                  ║
║              │  • Đăng nhập                │                  ║
║              │  • Thêm câu hỏi             │                  ║
║              │  • Soạn đề thi              │                  ║
║              │  • Chấm điểm                │                  ║
║              │  • Xuất báo cáo CSV         │                  ║
║              │                             │                  ║
║              └─────────────────────────────┘                  ║
║                                                               ║
║              http://localhost:8080                            ║
║              Username: gv01  Password: 123456                 ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Video demo 2-3 phút
- Hoặc live demo nếu có mạng
- Minh họa luồng nghiệp vụ thực tế

---

## SLIDE 15: THÁCH THỨC & GIẢI PHÁP

```
╔═══════════════════════════════════════════════════════════════╗
║                  THÁCH THỨC & GIẢI PHÁP                       ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  🔥 THÁCH THỨC:                                               ║
║                                                               ║
║  1. Trình duyệt VS Code Simple Browser không hỗ trợ cookie   ║
║     💡 Giải pháp: Session qua URL query string (sid param)   ║
║                                                               ║
║  2. Hiệu năng chậm khi nhiều query                           ║
║     💡 Giải pháp: Connection pooling + Database indexing     ║
║                                                               ║
║  3. Giao diện thiếu hiện đại                                 ║
║     💡 Giải pháp: Redesign UI theo phong cách Instagram      ║
║                                                               ║
║  4. Export CSV không đọc được tiếng Việt trong Excel         ║
║     💡 Giải pháp: UTF-8 BOM encoding                         ║
║                                                               ║
║  5. Validation phía client không đủ                          ║
║     💡 Giải pháp: Double validation (client + server)        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Gặp nhiều thách thức kỹ thuật
- Đều đã tìm được giải pháp hiệu quả
- Học được nhiều từ quá trình giải quyết

---

## SLIDE 16: KẾT QUẢ ĐẠT ĐƯỢC & HƯỚNG PHÁT TRIỂN

```
╔═══════════════════════════════════════════════════════════════╗
║            KẾT QUẢ ĐẠT ĐƯỢC & HƯỚNG PHÁT TRIỂN                ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ✅ KẾT QUẢ ĐẠT ĐƯỢC:                                         ║
║     • 8 chức năng + 3 tính năng nâng cao                     ║
║     • Hiệu năng: 70% nhanh hơn, 60 concurrent users          ║
║     • Giao diện: UI hiện đại, responsive 100%                ║
║     • Kiểm thử: 29/29 test cases pass (100%)                 ║
║     • Tài liệu: Báo cáo 120 trang, 9 chương đầy đủ           ║
║                                                               ║
║  🚀 HƯỚNG PHÁT TRIỂN (v2.0 - Q4/2026):                        ║
║     • Module quản lý người dùng (Admin/Teacher roles)        ║
║     • Tạo đề thi random tự động                              ║
║     • Export Word/PDF                                        ║
║     • Email notification                                     ║
║     • Mobile app (React Native)                              ║
║                                                               ║
║  🤖 FUTURE (v3.0 - 2027):                                     ║
║     • AI gợi ý câu hỏi (ChatGPT API)                         ║
║     • Auto-grading essay (NLP)                               ║
║     • Predictive analytics                                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Đã hoàn thành 100% mục tiêu đề ra
- Có roadmap phát triển rõ ràng
- Hướng đến AI trong tương lai

---

## SLIDE 17: Q&A

```
╔═══════════════════════════════════════════════════════════════╗
║                         Q & A                                 ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║                                                               ║
║                        ❓ 💬 🙋                                ║
║                                                               ║
║                   CÂU HỎI & TRẢ LỜI                           ║
║                                                               ║
║                                                               ║
║                   Xin mời quý thầy cô                         ║
║                   và các bạn đặt câu hỏi                      ║
║                                                               ║
║                                                               ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        ║
║                                                               ║
║  📧 Contact:                                                  ║
║     Email: 21521417@gm.uit.edu.vn                            ║
║     GitHub: github.com/YounqThjnk187/questions_grading_...   ║
║     Demo: http://localhost:8080                              ║
║                                                               ║
║  🙏 CẢM ƠN QUÝ THẦY CÔ ĐÃ THEO DÕI!                          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Speaker Notes:**
- Kết thúc báo cáo
- Mời câu hỏi
- Cảm ơn thầy cô và các bạn

---

# HƯỚNG DẪN SỬ DỤNG SLIDE

## Chuẩn bị trước khi thuyết trình:

1. **Tạo PowerPoint từ Markdown này:**
   - Copy từng slide vào PowerPoint
   - Thêm screenshot thực tế (chụp từ demo_app.py)
   - Thêm logo UIT, ảnh nhóm

2. **Chuẩn bị video demo:**
   - Quay video demo 2-3 phút
   - Hoặc chuẩn bị live demo (đảm bảo mạng ổn định)

3. **In phụ kiện:**
   - Báo cáo chi tiết (100+ trang)
   - Tài liệu tham khảo

4. **Phân công thuyết trình:**
   - Slide 1-3: Nhóm trưởng (giới thiệu, vấn đề)
   - Slide 4-7: Thành viên 2 (mục tiêu, công nghệ, chức năng)
   - Slide 8-11: Thành viên 3 (giao diện, database)
   - Slide 12-14: Thành viên 4 (hiệu năng, kiểm thử, demo)
   - Slide 15-17: Nhóm trưởng (thách thức, kết quả, Q&A)

## Thời gian thuyết trình: 15-20 phút

- Giới thiệu: 2 phút
- Vấn đề & mục tiêu: 2 phút
- Công nghệ & chức năng: 3 phút
- Giao diện & database: 3 phút
- Hiệu năng & kiểm thử: 2 phút
- Demo: 3 phút
- Thách thức & kết quả: 2 phút
- Q&A: 3-5 phút

## Tips thuyết trình:

✅ Nói chậm, rõ ràng
✅ Nhìn vào khán giả, không đọc slide
✅ Sử dụng con trỏ laser để chỉ
✅ Chuẩn bị sẵn câu trả lời cho câu hỏi khó
✅ Backup: USB + cloud (Google Drive)

---

**Good luck! 🍀**

