# Prompt Canva AI - 17 Slides Presentation

## 🎯 Project Overview

**Tên Dự án:** Hệ thống Quản lý Ra đề & Chấm thi  
**Số Slides:** 17 slides  
**Ngôn ngữ:** Tiếng Việt  
**Trường học:** UIT - ĐHQG TP. Hồ Chí Minh  
**Môn học:** SE104.Q23 - Nhập môn CNPM  
**Nhóm:** Nhóm 15 (4 thành viên)

---

## 🎨 Design Guidelines

### Color Palette:
- **Primary Gradient:** `#4F46E5` (Indigo) → `#7C3AED` (Violet) → `#EC4899` (Pink)
- **Accent Cyan:** `#06B6D4`
- **Accent Orange:** `#F59E0B`
- **Dark Text:** `#0F172A`
- **Light Background:** `#FAFBFF` / White
- **Muted Text:** `#475569`

### Typography:
- **Font Family:** Be Vietnam Pro (modern, Vietnamese-friendly)
- **Headings:** Bold 800, sizes 32-104px, letter-spacing -1.5px to 2px
- **Body:** Regular 400-500, size 20-26px
- **Code/Tags:** JetBrains Mono, monospace, 14-18px
- **Section Labels:** All caps, 16-18px, letter-spacing 2-3px

### Layout Elements:
- Background gradient blobs (soft, subtle)
- Gradient accent lines/dividers
- Shadow depth: 16-24px blur, 0.06-0.15 opacity
- Border radius: 8-24px (modern, smooth)
- Dotted grid accents (top right areas)
- Footer gradient bar with metadata

---

## 📊 Slide-by-Slide Content

### **SLIDE 1: COVER PAGE**
**Title:** Hệ thống Quản lý Ra đề & Chấm thi

**Layout:**
- Logo UIT (top left, ~110x110px)
- University name: "Trường Đại học Công nghệ Thông tin"
- Subtitle: "ĐẠI HỌC QUỐC GIA TP. HỒ CHÍ MINH — VNU-HCM"
- Course badge (gradient indigo→purple): "ĐỒ ÁN · SE104.Q23"
- Main title (HUGE, 100+px bold): "Hệ thống **Quản lý Ra đề** & Chấm thi"
  - Use gradient text for "Quản lý Ra đề" (#4F46E5→#EC4899)
- Divider line (120px, gradient)
- **GVHD:** "ThS. Nguyễn Thị Thanh Trúc"
- **Nhóm:** "Nhóm 15 — Trương Vũ Minh Tân, Thạch Via Sa Na, Hà Trọng Nghĩa, Dương Quốc Thịnh"
- **Tech Stack (right card, white box):**
  - ASP.NET MVC 5 | C# 6.0 | SQL Server | Entity FW 6 | Bootstrap 3 | jQuery
  - Use colored badges (indigo, cyan, pink, green, orange, purple)
- Footer gradient bar: "TP. Hồ Chí Minh · Tháng 05 / 2026" + "UIT — VNU-HCM"
- Background: Subtle radial gradient blobs (purple, cyan, pink)

---

### **SLIDE 2: TEAM INTRODUCTION**
**Title:** Giới thiệu nhóm 15

**Section Label:** "01 / NHÓM"
**Subtitle:** "Bốn thành viên — bốn vai trò rõ ràng..."

**4 Member Cards (2x2 Grid):**

**Card 1 - Leader (Gradient Indigo-Purple)**
- Avatar circle with letter "T" (white, bold)
- Badge: "★ NHÓM TRƯỞNG"
- Name: "Trương Vũ Minh Tân"
- ID: "MSSV · 21521417"
- Role: "Backend & Database\nArchitecture & Coordination"

**Card 2 - Frontend (White, Cyan accent)**
- Avatar circle gradient cyan-blue with "S"
- Badge: "◆ FRONTEND" (cyan background)
- Name: "Thạch Via Sa Na"
- ID: "MSSV · 23520966"
- Role: "UI / UX Design\nRazor View & Styling"

**Card 3 - Tester (White, Orange accent)**
- Avatar circle gradient orange with "N"
- Badge: "▲ TESTER" (orange background)
- Name: "Hà Trọng Nghĩa"
- ID: "MSSV · 23521008"
- Role: "Quality Assurance\nDocumentation & Test Cases"

**Card 4 - Business Logic (White, Green accent)**
- Avatar circle gradient green with "T"
- Badge: "● BUSINESS LOGIC" (green background)
- Name: "Dương Quốc Thịnh"
- ID: "MSSV · 23521498"
- Role: "MVC Controllers\nValidation & Business Rules"

**Footer:** "SE104.Q23 — NHÓM 15" | "02 / 17"

---

### **SLIDE 3: PROBLEMS**
**Title:** Quy trình thủ công — tốn thời gian, dễ sai sót

**Section Label:** "02 / VẤN ĐỀ" (pink)
**Subtitle:** "Giảng viên đang quản lý câu hỏi qua Word/Excel rời rạc..."

**4 Pain Point Cards (2x2, with colored left borders):**

**Card 1 - Red Border (#EF4444)**
- Icon: ✕ (red circle background)
- Badge: "PAIN #1 · QUẢN LÝ" (red)
- Title: "Câu hỏi nằm rải rác Word/Excel"
- Description: "Không có ngân hàng tập trung. Tìm kiếm phải mở từng file..."

**Card 2 - Orange Border (#F59E0B)**
- Icon: ⏱ (orange circle background)
- Badge: "PAIN #2 · SOẠN ĐỀ" (orange)
- Title: "Mỗi đề thi tốn 2 – 3 giờ"
- Description: "Chọn câu thủ công, gõ lại nội dung..."

**Card 3 - Pink Border (#EC4899)**
- Icon: ✎ (pink circle background)
- Badge: "PAIN #3 · CHẤM THI" (pink)
- Title: "100 bài thi = 8 – 16 giờ chấm"
- Description: "Cộng điểm thủ công, quy đổi điểm chữ..."

**Card 4 - Purple Border (#8B5CF6)**
- Icon: ▤ (purple circle background)
- Badge: "PAIN #4 · BÁO CÁO" (purple)
- Title: "Báo cáo cuối kỳ mất 1 – 2 ngày"
- Description: "Tổng hợp thủ công từ nhiều file..."

**Footer:** "SE104.Q23 — NHÓM 15" | "03 / 17"

---

### **SLIDE 4: OBJECTIVES**
**Title:** Mục tiêu đề tài

**Section Label:** "03 / MỤC TIÊU" (cyan)
**Subtitle:** "Xây dựng hệ thống web-based giúp số hóa hoàn toàn..."

**3 Sections with Icons:**

**Section 1: 🎯 MỤC TIÊU CHÍNH**
- Text: "Xây dựng hệ thống web-based giúp số hóa hoàn toàn quy trình từ soạn câu hỏi → tạo đề thi → chấm điểm → báo cáo thống kê"
- Use large icon (target, bullseye)

**Section 2: ✅ CHỨC NĂNG (Use bullet points)**
- • Quản lý ngân hàng câu hỏi (Thêm/Sửa/Xóa/Tìm kiếm)
- • Soạn đề thi nhanh (15-20 phút)
- • Chấm thi tự động tính điểm chữ
- • Tra cứu và báo cáo thống kê

**Section 3: 📊 METRICS (Show numbers)**
- ⚡ Thời gian tải trang < 200ms
- 👥 Hỗ trợ 50+ người dùng đồng thời
- 🎨 Responsive 100% (desktop/tablet/mobile)

**Color scheme:** Light background, icons have gradient colors

---

### **SLIDE 5: TECHNOLOGY STACK**
**Title:** Công nghệ sử dụng

**Section Label:** "04 / CÔNG NGHỆ"

**3-Layer Architecture Diagram:**
```
Presentation Layer (Razor + Bootstrap)
        ↓
Business Logic Layer (MVC Controllers)
        ↓
Data Access Layer (Entity Framework)
        ↓
SQL Server 2019
```
Use vertical flow with colored boxes

**Tech Stack Table/Grid:**
| Category | Technology |
|----------|-----------|
| Backend Framework | ASP.NET MVC 5 |
| Language | C# 6.0 |
| Frontend | Razor + Bootstrap 3 |
| ORM | Entity Framework 6 |
| Database | SQL Server 2019 |
| Scripting | jQuery 1.10 |

Use gradient backgrounds for each tech

---

### **SLIDE 6: FEATURES (1/2)**
**Title:** Chức năng chính (1/2)

**Section Label:** "05 / CHỨC NĂNG"

**4 Feature Cards:**

**1️⃣ ĐĂNG NHẬP HỆ THỐNG**
- Icon: 🔐
- Xác thực giảng viên qua mã GV + mật khẩu
- Session management, auto logout sau 30 phút

**2️⃣ QUẢN LÝ CÂU HỎI**
- Icon: 📝
- Thêm/Sửa/Xóa câu hỏi
- Phân loại theo môn học và độ khó
- Tìm kiếm full-text với highlight

**3️⃣ SOẠN ĐỀ THI**
- Icon: 📄
- Chọn câu hỏi từ ngân hàng
- Gán điểm cho mỗi câu
- Validate: Tổng điểm = 10, Số câu ≥ min
- **Thời gian:** Từ 2-3 giờ → 15-20 phút (88% nhanh hơn)

**4️⃣ CHẤM THI**
- Icon: ✅
- Nhập điểm số cho sinh viên
- Tự động tính điểm chữ (A, B+, B, C+...)
- In phiếu điểm (print-friendly HTML)

---

### **SLIDE 7: FEATURES (2/2)**
**Title:** Chức năng chính (2/2)

**5 Feature Cards:**

**5️⃣ TRA CỨU ĐỀ THI**
- Tìm kiếm theo môn học, học kỳ, năm
- Xem chi tiết danh sách câu hỏi
- Export đề thi ra file

**6️⃣ BÁO CÁO NĂM**
- Thống kê số lượng đề thi theo môn học
- Biểu đồ cột (bar chart) trực quan
- Xuất CSV (UTF-8 BOM, đọc được trong Excel)

**7️⃣ THAY ĐỔI THAM SỐ**
- Cập nhật số câu tối thiểu
- Cập nhật thời gian thi mặc định

**8️⃣ TRA CỨU NHANH**
- Tìm kiếm câu hỏi theo từ khóa
- Highlight từ khóa màu vàng

---

### **SLIDE 8: UI - LOGIN PAGE**
**Title:** Giao diện - Đăng nhập

**Section Label:** "06 / GIAO DIỆN"

**Screenshot/Mockup Elements:**
- Background: Gradient tím-hồng (#667eea → #764ba2)
- Card trắng, rounded corners, shadow
- Input fields với icon (👤 mã GV, 🔒 mật khẩu)
- Button gradient với hover effect
- "Đơn giản, dễ sử dụng"
- "Màu sắc hiện đại"
- "Typography: Be Vietnam Pro, 15px"
- "Validation realtime"

---

### **SLIDE 9: UI - DASHBOARD**
**Title:** Giao diện - Trang chủ

**Section Label:** "07 / GIAO DIỆN"

**Dashboard Elements:**
- Navbar cố định (gradient)
- Sidebar navigation (icon + text)
- Stats cards: Số câu hỏi, đề thi, đã chấm
- Warning alerts: Cảnh báo môn < 10 câu
- Quick actions: Buttons thêm câu hỏi, soạn đề
- "Thống kê tổng quan"
- "Thông báo quan trọng"
- "Truy cập nhanh các chức năng"

---

### **SLIDE 10: UI - QUESTION MANAGEMENT**
**Title:** Giao diện - Quản lý câu hỏi

**Section Label:** "08 / GIAO DIỆN"

**Elements:**
- Danh sách câu hỏi (table format)
- Search box với icon
- Button "Thêm câu hỏi" (prominent)
- Modal popup cho form thêm/sửa
- Validation inline (error message đỏ)
- "Full-text search"
- "Highlight từ khóa"
- "Filter theo môn học, độ khó"

---

### **SLIDE 11: DATABASE DESIGN**
**Title:** Thiết kế Database

**Section Label:** "09 / DATABASE"

**ERD (Entity Relationship Diagram):**
Show relationships between 11 tables:
- GIANG_VIEN (1:N) CAU_HOI
- CAU_HOI (N:M) DE_THI
- DE_THI (1:N) KET_QUA
- MON_HOC, SINH_VIEN, LOP_HOC (relationships)

**Statistics:**
- 📊 11 bảng
- 🔧 4 stored procedures
- ⚡ 5 indexes (tăng tốc 70-82%)
- 📐 Chuẩn hóa 3NF

**Color schema:** Each table/entity has different color

---

### **SLIDE 12: PERFORMANCE**
**Title:** Hiệu năng

**Section Label:** "10 / HIỆU NĂNG"

**Performance Metrics Table:**
| Metric | Before | After | Improved |
|--------|--------|-------|----------|
| Page Load Time | 500ms | 150ms | 70% ✅ |
| Database Query | 50ms | 15ms | 70% ✅ |
| Concurrent Users | 20 | 60 | 200% ✅ |
| Memory Usage | 80MB | 50MB | 37% ✅ |

Use green checkmarks, visual bars showing improvement

**Optimization Techniques:**
- Connection Pooling (min=5, max=100)
- Database Indexing (5 indexes)
- SQLite WAL mode (Python demo)
- Output Caching (ASP.NET)
- **Goal Status:** 5/5 metrics ✅

---

### **SLIDE 13: TESTING**
**Title:** Kiểm thử

**Section Label:** "11 / KIỂM THỬ"

**Test Results Table:**
| Test Type | Total | Pass | Fail | Pass Rate |
|-----------|-------|------|------|-----------|
| Functionality | 15 | 15 | 0 | 100% ✅ |
| Performance | 5 | 5 | 0 | 100% ✅ |
| Security | 5 | 5 | 0 | 100% ✅ |
| Usability | 4 | 4 | 0 | 100% ✅ |
| **TOTAL** | **29** | **29** | **0** | **100% ✅** |

**Security Checkmarks:**
- ✅ Chống SQL Injection (Entity Framework auto-param)
- ✅ Chống XSS (Razor auto HTML-encode)
- ✅ Session timeout 30 phút

**Usability Rating:** ⭐⭐⭐⭐☆ 4.5/5 (từ 3 giảng viên)

---

### **SLIDE 14: DEMO VIDEO**
**Title:** Demo Video

**Section Label:** "12 / DEMO"

**Large Video Frame/Thumbnail:**
- Center: ▶️ PLAY VIDEO button (large, gradient)
- "Demo các chức năng chính:"
  - • Đăng nhập
  - • Thêm câu hỏi
  - • Soạn đề thi
  - • Chấm điểm
  - • Xuất báo cáo CSV
- Demo info: "http://localhost:8080"
- "Username: gv01  Password: 123456"

Use decorative gradient border around the video area

---

### **SLIDE 15: CHALLENGES & SOLUTIONS**
**Title:** Thách thức & Giải pháp

**Section Label:** "13 / THÁCH THỨC"

**5 Challenge Cards (with problem-solution pairs):**

**Challenge 1 (Red icon):**
- Problem: "Trình duyệt VS Code Simple Browser không hỗ trợ cookie"
- Solution: "Session qua URL query string (sid param)"

**Challenge 2 (Orange icon):**
- Problem: "Hiệu năng chậm khi nhiều query"
- Solution: "Connection pooling + Database indexing"

**Challenge 3 (Pink icon):**
- Problem: "Giao diện thiếu hiện đại"
- Solution: "Redesign UI theo phong cách Instagram"

**Challenge 4 (Blue icon):**
- Problem: "Export CSV không đọc được tiếng Việt trong Excel"
- Solution: "UTF-8 BOM encoding"

**Challenge 5 (Purple icon):**
- Problem: "Validation phía client không đủ"
- Solution: "Double validation (client + server)"

---

### **SLIDE 16: RESULTS & ROADMAP**
**Title:** Kết quả đạt được & Hướng phát triển

**Section Label:** "14 / KẾT QUẢ"

**Left Column - Results (✅):**
- 8 chức năng + 3 tính năng nâng cao
- Hiệu năng: 70% nhanh hơn, 60 concurrent users
- Giao diện: UI hiện đại, responsive 100%
- Kiểm thử: 29/29 test cases pass (100%)
- Tài liệu: Báo cáo 120 trang, 9 chương đầy đủ

**Middle Column - Future (v2.0):**
- Module quản lý người dùng (Admin/Teacher roles)
- Tạo đề thi random tự động
- Export Word/PDF
- Email notification
- Mobile app (React Native)

**Right Column - Advanced (v3.0):**
- AI gợi ý câu hỏi (ChatGPT API)
- Auto-grading essay (NLP)
- Predictive analytics
- Interactive dashboards

Use icons and color coding for each version

---

### **SLIDE 17: Q&A - THANK YOU**
**Title:** Q & A

**Section Label:** "15 / Q&A"

**Large centered text:**
- ❓ 💬 🙋 (emoji icons)
- "CÂU HỎI & TRẢ LỜI"
- "Xin mời quý thầy cô và các bạn đặt câu hỏi"

**Contact Information (bottom card, gradient):**
- 📧 Email: 21521417@gm.uit.edu.vn
- 🔗 GitHub: github.com/YounqThjnk187/questions_grading_...
- 🌐 Demo: http://localhost:8080

**Closing:**
- 🙏 "CẢM ƠN QUÝ THẦY CÔ ĐÃ THEO DÕI!"

---

## 🎬 Overall Presentation Style

### Key Design Principles:
1. **Modern & Professional:** Gradient colors, clean layout, plenty of whitespace
2. **Consistent:** Same color palette, typography, icons throughout
3. **Readable:** High contrast, clear hierarchy, legible fonts
4. **Engaging:** Use icons, emojis, cards, visual elements
5. **Vietnamese-friendly:** Be Vietnam Pro font, proper accents

### Animations (Optional but recommended in Canva):
- Slide transitions: Fade or smooth slide
- Text appear: Subtle fade-in
- Icon animations: Gentle scale/bounce
- Number counters: Animated count-up (for metrics)

### Export Format:
- Save as **presentation.pdf** or **presentation.pptx**
- Aspect ratio: 16:9 (standard widescreen)
- Resolution: High quality (300dpi)

---

## 📋 Checklist for Canva Creation

- [ ] All 17 slides created
- [ ] Consistent color scheme across all slides
- [ ] Typography sizes and weights match guidelines
- [ ] Icons added appropriately
- [ ] Tables/charts properly formatted
- [ ] Footer metadata on each slide
- [ ] Background elements (gradient blobs) added
- [ ] Images/logos placed correctly
- [ ] Animations set (if needed)
- [ ] Export as PDF/PPTX
- [ ] Quality check: Review all slides

---

**Good luck! This presentation will wow your professors! 🎉**
