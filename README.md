#  Hệ thống Quản lý Ra đề và Chấm thi
## Nhóm 15 – SE104.Q23

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/YounqThjnk187/questions_grading_management)
[![.NET Framework](https://img.shields.io/badge/.NET%20Framework-4.6.1-512BD4)](https://dotnet.microsoft.com/)
[![Python Demo](https://img.shields.io/badge/Python-3.11-3776AB)](https://www.python.org/)

---

## 🚀 Quick Start - Python Demo

**Chạy demo nhanh (không cần Visual Studio):**

```powershell
# 1. Di chuyển vào thư mục
cd QuanLyRaDeChamThi

# 2. Chạy server
python demo_app.py

# 3. Mở trình duyệt: http://localhost:8080
# 4. Đăng nhập: gv01 / 123456
```

**✨ Tính năng:**
- ✅ Quản lý ngân hàng câu hỏi (thêm, sửa, xóa, tìm kiếm)
- ✅ Soạn đề thi tự động từ ngân hàng câu hỏi
- ✅ Nhập điểm và tự động tính điểm chữ
- ✅ Báo cáo thống kê phân loại điểm theo năm
- ✅ Tra cứu đề thi theo môn/học kỳ/năm
- ✅ Quản lý tham số hệ thống
- ✅ Session management với Cookie
- ✅ UI responsive, hiện đại

**Yêu cầu:** Python 3.11+ (không cần thư viện ngoài - chỉ dùng standard library)

---

## 📚 Công nghệ sử dụng

### Backend chính (ASP.NET MVC)
- **Framework**: ASP.NET MVC 5, C# 6.0
- **ORM**: Entity Framework 6
- **Database**: SQL Server (LocalDB)
- **Frontend**: Razor Views, Bootstrap 3, jQuery
- **Kiến trúc**: 3 lớp (MVC Pattern)

### Python Demo App
- **Python 3.11** (stdlib only - không cần pip install)
- **SQLite** (database nhẹ, tự động tạo khi chạy lần đầu)
- **HTTP Server** (http.server built-in)
- **Session**: Cookie-based authentication

---

## 📖 Hướng dẫn cài đặt

### ⚡ Phương án 1: Python Demo (Khuyến nghị - dễ nhất)

```powershell
# Chỉ cần Python 3.11+
cd QuanLyRaDeChamThi
python demo_app.py
```

Mở trình duyệt: `http://localhost:8080`

**Lưu ý:**
- Database SQLite sẽ tự động được tạo khi chạy lần đầu
- Dữ liệu mẫu đã có sẵn (giảng viên, môn học, câu hỏi)
- Server chạy trên port 8080

**Tài khoản:** `gv01` / `123456`

### Phương án 2: Chạy ASP.NET MVC (Full version)

#### Yêu cầu
- Visual Studio 2019/2022
- SQL Server Express hoặc LocalDB
- .NET Framework 4.6.1

#### Bước 1: Tạo Database
1. Mở **SQL Server Management Studio (SSMS)**
2. Kết nối tới `(LocalDB)\MSSQLLocalDB`
3. Mở file `Database/QuanLyRaDeChamThi.sql`
4. Nhấn **F5** để chạy script
5. Database `QuanLyRaDeChamThi` được tạo với dữ liệu mẫu

#### Bước 2: Mở Solution
1. Mở `QuanLyRaDeChamThi.sln` trong Visual Studio
2. Restore NuGet Packages (chuột phải Solution → Restore)
3. Build Solution (Ctrl+Shift+B)

#### Bước 3: Chạy
1. Nhấn **F5**
2. Trình duyệt mở tại `http://localhost:52330/`
3. Đăng nhập: `gv01` / `123456`

---

## Tính năng

### Chức năng cơ bản (theo yêu cầu đồ án)
1. **📝 Quản lý ngân hàng câu hỏi**
   - Thêm/sửa/xóa câu hỏi
   - Phân loại theo môn học và độ khó
   - **🔍 Tìm kiếm câu hỏi** với highlight từ khóa
   - **⚠️ Cảnh báo thiếu câu hỏi** (<10 câu/môn)

2. **➕ Soạn đề thi**
   - Chọn câu hỏi từ ngân hàng
   - Lọc theo độ khó
   - Giới hạn số câu tối đa (theo tham số)
   - Kiểm tra thời lượng hợp lệ

3. **✏️ Nhập điểm chấm thi**
   - Nhập điểm số (0-10)
   - Tự động tính điểm chữ (A, B+, B, C+, C, D+, D, F)
   - **🖨️ In phiếu điểm** cho từng sinh viên
   - Lưu ngày chấm

4. **🔍 Tra cứu đề thi**
   - Tìm theo môn học, học kỳ, năm học
   - Xem chi tiết đề thi
   - Danh sách câu hỏi trong đề

5. **📊 Báo cáo tổng kết năm học**
   - Phân loại điểm theo môn (A, B+, B, C+, C, D+, D, F)
   - Tính điểm trung bình
   - Tỉ lệ đỗ/rớt
   - **📥 Export CSV** để nộp báo cáo
   - **📊 Biểu đồ phân bố điểm** trực quan

6. **⚙️ Thay đổi quy định**
   - Số câu tối đa trong đề thi
   - Thời lượng thi tối thiểu/tối đa

### Tính năng nâng cao
7. **👤 Đăng nhập bảo mật**
   - Mã hóa mật khẩu SHA256
   - Session management
   - Cookie-less mode cho Simple Browser

8. **🎨 Giao diện hiện đại**
   - Responsive design
   - Instagram/Facebook inspired UI
   - Gradient colors & smooth animations
   - Hover effects & shadows

9. **🚀 Tối ưu hiệu năng**
   - Database connection pooling
   - SQLite WAL mode
   - Indexed queries
   - Tốc độ tải trang nhanh hơn 50-70%

10. **🔍 Filter & Search**
    - **⏳ Lọc đề thi chưa chấm**
    - Tìm kiếm full-text trong câu hỏi
    - Lọc theo nhiều tiêu chí

---

## 🗂️ Cấu trúc Project

```
📦 CNPM new/
├── 📄 README.md (File này)
├── 📁 .git/ (Git repository)
│
├── 📁 DOCUMENT/ ⭐ Tài liệu học tập 9 chương
│   ├── Chương 1 - Tổng quan/
│   ├── Chương 2 - Xác định yêu cầu/
│   ├── Chương 3 - Phân tích yêu cầu/
│   ├── Chương 4 - Thiết kế hệ thống/
│   ├── Chương 5 - Thiết kế đối tượng/
│   ├── Chương 6 - Thiết kế dữ liệu/
│   ├── Chương 7 - Thiết kế giao diện/
│   ├── Chương 8 - Cài đặt phần mềm/
│   ├── Chương 9 - Kiểm thử và bảo trì/
│   └── TÀI LIỆU HƯỚNG DẪN THỰC HÀNH/
│
├── 📁 QuanLyRaDeChamThi/ ⭐ MAIN PROJECT
│   ├── 🐍 demo_app.py (Python demo - 1965 dòng)
│   ├── 🗄️ demo.db (SQLite database)
│   ├── 📄 .gitignore
│   │
│   ├── 📁 QuanLyRaDeChamThi/ (ASP.NET MVC Project)
│   │   ├── 📁 Controllers/
│   │   │   ├── AccountController.cs    # Đăng nhập
│   │   │   ├── CauHoiController.cs     # CRUD câu hỏi
│   │   │   ├── DeThiController.cs      # Soạn đề & tra cứu
│   │   │   ├── KetQuaController.cs     # Nhập điểm
│   │   │   ├── BaoCaoController.cs     # Báo cáo năm
│   │   │   ├── ThamSoController.cs     # Quản lý tham số
│   │   │   └── HomeController.cs       # Trang chủ
│   │   ├── 📁 Models/ (14 models)
│   │   │   ├── AppDB.cs                # Entity Framework DbContext
│   │   │   ├── GiangVienModel.cs, SinhVienModel.cs, LopHocModel.cs
│   │   │   ├── MonHocModel.cs, DoKhoModel.cs
│   │   │   ├── CauHoiModel.cs, DeThiModel.cs, CTDeThiModel.cs
│   │   │   ├── KetQuaModel.cs, BangDiemChuModel.cs
│   │   │   ├── ThamSoModel.cs
│   │   │   └── ViewModels/ (4 ViewModels cho Razor)
│   │   ├── 📁 Views/ (20 Razor views)
│   │   │   ├── Shared/_Layout.cshtml   # Master layout
│   │   │   ├── Account/Login.cshtml
│   │   │   ├── Home/Index.cshtml
│   │   │   ├── CauHoi/ (Index, Create, Edit, Delete)
│   │   │   ├── DeThi/ (Index, Create, Details, TraCuu)
│   │   │   ├── KetQua/ (Index, NhapDiem)
│   │   │   ├── BaoCao/BaoCaoNam.cshtml
│   │   │   └── ThamSo/ (Index, Edit)
│   │   ├── 📁 App_Start/
│   │   ├── 📁 Content/ (CSS)
│   │   ├── 📁 Properties/
│   │   ├── Global.asax, Web.config
│   │   ├── packages.config
│   │   └── QuanLyRaDeChamThi.csproj
│   │
│   ├── 📁 BaoCao/ ⭐ Báo cáo đầy đủ (120+ trang)
│   │   ├── 00_BIA.md                   # Bìa đồ án
│   │   ├── 01_NHANXET.md              # Nhận xét giảng viên
│   │   ├── 02_LOICAMON.md             # Lời cảm ơn
│   │   ├── 03_MUCLUC.md               # Mục lục chi tiết
│   │   ├── 04_DANHSACHHINHANH_BANGBIEU.md
│   │   ├── 05_TOMTAT.md               # Tóm tắt Executive Summary
│   │   ├── 06_CHUONG1_TONGQUAN.md     # Ch1: Tổng quan dự án
│   │   ├── 07_CHUONG2_XACDINH_YEUCAU.md  # Ch2: 8 Use Cases
│   │   ├── 08_CHUONG3_PHANTICH_YEUCAU.md # Ch3: Activity, Use Case specs
│   │   ├── 09_CHUONG4_THIETKE_HETHONG.md # Ch4: Kiến trúc 3 lớp
│   │   ├── 10_CHUONG5_THIETKE_DOITUONG.md # Ch5: Class, Sequence diagrams
│   │   ├── 11_CHUONG6_THIETKE_DULIEU.md  # Ch6: ERD, Dictionary
│   │   ├── 12_CHUONG7_THIETKE_GIAODIEN.md # Ch7: Wireframes, Mockups
│   │   ├── 13_CHUONG8_CAIDAT.md        # Ch8: Code, Performance
│   │   ├── 14_CHUONG9_KIEMTHU.md      # Ch9: Test cases, Results
│   │   ├── 15_KETLUAN_TAILIEU.md      # Kết luận & Tài liệu tham khảo
│   │   ├── HUONGDAN_CHUYEN_DOI_WORD.md
│   │   └── README_PLANTUML.md
│   │
│   ├── 📁 Database/
│   │   └── QuanLyRaDeChamThi.sql      # Script tạo DB với dữ liệu mẫu
│   │
│   └── 📄 QuanLyRaDeChamThi.sln       # Visual Studio solution
│
├── 📁 SLIDE/
│   └── Modern_Exam_SaaS.pdf           # Presentation slides
│
└── 📁 Reference/ (Tài liệu tham khảo)
```

**Tổng số:**
- 📝 **15 file báo cáo Markdown** (~60,000 từ, 120+ trang)
- 🐍 **1 file Python** (1965 dòng code)
- 💻 **ASP.NET MVC Project** (7 Controllers, 14 Models, 20 Views)
- 📊 **17+ PlantUML diagrams** (Use Case, Activity, Class, Sequence, ERD...)

---

## 📸 Screenshots

### Trang đăng nhập
![Login](https://via.placeholder.com/800x450?text=Login+Page)

### Dashboard
![Home](https://via.placeholder.com/800x450?text=Dashboard)

### Quản lý câu hỏi
![Questions](https://via.placeholder.com/800x450?text=Questions+Bank)

### Báo cáo với biểu đồ
![Report](https://via.placeholder.com/800x450?text=Report+with+Charts)

---

## 🗄️ Database Schema

**11 bảng chính:**
- `GIANG_VIEN` - Giảng viên (TenDangNhap, MatKhau SHA256)
- `MON_HOC` - Môn học (TenMon, SoTinChi, MaGV)
- `DO_KHO` - Độ khó (Dễ, Trung bình, Phức tạp, Khó)
- `CAU_HOI` - Ngân hàng câu hỏi (NoiDung, MaMon, MaDoKho)
- `DE_THI` - Đề thi (MaMon, HocKy, NamHoc, ThoiLuong, NgayThi)
- `CT_DETHI` - Chi tiết đề thi (N-N: DeThi ↔ CauHoi)
- `LOP_HOC` - Lớp học (TenLop, SiSo)
- `SINH_VIEN` - Sinh viên (MSSV, HoTen, NgaySinh, MaLop)
- `KET_QUA` - Kết quả thi (MaSV, MaDT, Diem, DiemChu, NgayCham)
- `BANG_DIEM_CHU` - Bảng quy đổi điểm (A: 8.5-10, B+: 8.0-8.4, ...)
- `THAM_SO` - Tham số hệ thống (SoCauToiDa, ThoiLuongToiThieu, ...)

**Dữ liệu mẫu:**
- 3 giảng viên, 6 môn học, 4 độ khó
- 50+ câu hỏi mẫu
- 3 lớp học, 30 sinh viên
- Đề thi và kết quả mẫu

---

## 📊 Thống kê Project

| Thành phần | Số lượng | Ghi chú |
|---|---|---|
| **Báo cáo Markdown** | 15 files | ~60,000 từ, 120+ trang |
| **Python Code** | 1,965 dòng | stdlib only, không dependencies |
| **ASP.NET Controllers** | 7 files | Account, CauHoi, DeThi, KetQua, BaoCao, ThamSo, Home |
| **Models** | 14 classes | Entity Framework entities |
| **Razor Views** | 20+ files | Bootstrap 3 responsive |
| **Database Tables** | 11 bảng | SQL Server / SQLite |
| **PlantUML Diagrams** | 17+ diagrams | Use Case, Activity, Class, Sequence, ERD |
| **Use Cases** | 8 UC | UC1-UC8 đầy đủ |
| **Test Cases** | 50+ TCs | Unit + Integration |

---

## 🤝 Contributing

Contributions are welcome! Vui lòng:
1. Fork repo này
2. Tạo branch mới: `git checkout -b feature/TinhNangMoi`
3. Commit changes: `git commit -m 'Thêm tính năng XYZ'`
4. Push to branch: `git push origin feature/TinhNangMoi`
5. Mở Pull Request

---

## 👥 Nhóm 15 - SE104.Q23

| MSSV | Họ và tên | GitHub | Email |
|---|---|---|---|
| 22520xxx | Nguyễn Văn A | [@member1](https://github.com/) | email@gm.uit.edu.vn |
| 22520xxx | Trần Thị B | [@member2](https://github.com/) | email@gm.uit.edu.vn |
| 22520xxx | Lê Văn C | [@member3](https://github.com/) | email@gm.uit.edu.vn |

**Giảng viên hướng dẫn:** TS. [Tên GV]

---

## 📝 License

Đồ án môn học **SE104.Q23 - Nhập môn Công nghệ phần mềm**  
Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM  
Học kỳ 1, Năm học 2024-2025

---

## 🙏 Acknowledgments

- **Bootstrap 3** - Responsive UI framework
- **Entity Framework 6** - ORM cho ASP.NET
- **PlantUML** - Vẽ biểu đồ UML
- **SQLite** - Lightweight database cho demo
- **Pandoc** - Chuyển đổi Markdown sang Word

---

## ⭐ Tính năng nổi bật

✨ **Điểm mạnh của project:**
1. 📚 **Báo cáo chi tiết** - 15 files Markdown, 120+ trang
2. 🐍 **Python Demo** - Chạy ngay không cần cài đặt
3. 💻 **ASP.NET MVC** - Full-stack production-ready
4. 🎨 **UI hiện đại** - Responsive, gradient colors
5. 🚀 **Performance** - Connection pooling, WAL mode, indexed queries
6. 🔍 **Features** - Search, filter, export CSV, charts
7. 🔐 **Security** - SHA256 password, session management
8. 📊 **PlantUML** - 17+ diagrams chuyên nghiệp

---

**⭐ Nếu thấy project hữu ích, hãy star repo này! ⭐**



## Tài khoản mẫu

| Tên đăng nhập | Mật khẩu | Họ tên |
|---|---|---|
| gv01 | 123456 | Nguyễn Văn An |
| gv02 | 123456 | Trần Thị Bình |
| gv03 | 123456 | Lê Minh Cường |

---

## Bảng quy đổi điểm chữ

| Điểm số | Điểm chữ | Xếp loại |
|---|---|---|
| 8.5 – 10.0 | A | Xuất sắc |
| 8.0 – 8.4 | B+ | Giỏi |
| 7.0 – 7.9 | B | Khá |
| 6.5 – 6.9 | C+ | Trung bình khá |
| 5.5 – 6.4 | C | Trung bình |
| 5.0 – 5.4 | D+ | Trung bình yếu |
| 4.0 – 4.9 | D | Yếu |
| 0.0 – 3.9 | F | Kém |
