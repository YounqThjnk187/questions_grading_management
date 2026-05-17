# 🎓 Hệ thống Quản lý Ra đề và Chấm thi
## Nhóm 15 – SE104.Q23

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/YounqThjnk187/questions_grading_management)
[![.NET Framework](https://img.shields.io/badge/.NET%20Framework-4.6.1-512BD4)](https://dotnet.microsoft.com/)
[![Python Demo](https://img.shields.io/badge/Python-3.11-3776AB)](https://www.python.org/)

---

## 👥 Thành viên nhóm
| Họ tên | MSSV |
|---|---|
| Trương Vũ Minh Tân | 21521417 |
| Thạch Via Sa Na | 23520966 |
| Hà Trọng Nghĩa | 23521008 |
| Dương Quốc Thịnh | 23521498 |

---

## ⚡ Quick Start - Python Demo

**Chạy nhanh demo (không cần Visual Studio):**

```powershell
# 1. Chạy server
python demo_app.py

# 2. Mở trình duyệt: http://localhost:8080/login
# 3. Đăng nhập: gv01 / 123456
```

**Yêu cầu:** Python 3.11+ (không cần thư viện ngoài)

---

## 🛠️ Công nghệ sử dụng

### Backend chính (ASP.NET)
- **Framework**: ASP.NET MVC 5, C#
- **ORM**: Entity Framework 6
- **Database**: SQL Server (LocalDB)
- **Frontend**: Razor Views, Bootstrap 3, jQuery
- **Kiến trúc**: 3 lớp (MVC)

### Demo App (Python)
- **Python 3.11** (stdlib only - không cần pip install)
- **SQLite** (database nhẹ, tự động tạo)
- **HTTP Server** (http.server built-in)

---

## 📦 Hướng dẫn cài đặt

### Phương án 1: Chạy Python Demo (Khuyến nghị để test nhanh)

```powershell
cd QuanLyRaDeChamThi
python demo_app.py
```

Mở trình duyệt: `http://localhost:8080/login`

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

## ✨ Tính năng

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

## 🗂️ Cấu trúc project
```
QuanLyRaDeChamThi/
├── 📁 QuanLyRaDeChamThi/ (ASP.NET MVC)
│   ├── App_Start/
│   │   ├── BundleConfig.cs
│   │   ├── FilterConfig.cs
│   │   └── RouteConfig.cs
│   ├── Controllers/
│   │   ├── AccountController.cs    # Đăng nhập
│   │   ├── CauHoiController.cs     # CRUD câu hỏi
│   │   ├── DeThiController.cs      # Soạn đề
│   │   ├── KetQuaController.cs     # Nhập điểm
│   │   ├── BaoCaoController.cs     # Báo cáo
│   │   └── ThamSoController.cs     # Tham số
│   ├── Models/
│   │   ├── AppDB.cs                # EF DbContext
│   │   ├── GiangVienModel.cs
│   │   ├── CauHoiModel.cs
│   │   ├── DeThiModel.cs
│   │   ├── KetQuaModel.cs
│   │   └── ViewModels/
│   ├── Views/
│   │   ├── Account/Login.cshtml
│   │   ├── CauHoi/*.cshtml
│   │   ├── DeThi/*.cshtml
│   │   └── Shared/_Layout.cshtml
│   └── Web.config
├── 📁 Database/
│   └── QuanLyRaDeChamThi.sql      # SQL Script
├── 📄 demo_app.py                  # Python Demo Server
├── 📄 README.md
└── 📄 .gitignore
```

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
- `GIANG_VIEN` - Giảng viên
- `MON_HOC` - Môn học
- `DO_KHO` - Độ khó (Dễ, Trung bình, Phức tạp, Khó)
- `CAU_HOI` - Ngân hàng câu hỏi
- `DE_THI` - Đề thi
- `CT_DETHI` - Chi tiết đề thi (N-N)
- `LOP_HOC` - Lớp học
- `SINH_VIEN` - Sinh viên
- `KET_QUA` - Kết quả thi
- `BANG_DIEM_CHU` - Bảng quy đổi điểm
- `THAM_SO` - Tham số hệ thống

---

## 🤝 Contributing

Contributions are welcome! Vui lòng:
1. Fork repo này
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

---

## 📝 License

Đồ án môn học SE104.Q23 - Nhập môn Công nghệ phần mềm  
Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM

---

## 📧 Contact

Nhóm 15 - SE104.Q23

- GitHub: [https://github.com/YounqThjnk187/questions_grading_management](https://github.com/YounqThjnk187/questions_grading_management)
- Email: 23521498@gm.uit.edu.vn

---

## 🙏 Acknowledgments

- Bootstrap 3 framework
- Entity Framework 6
- Tham khảo: [Bookstore Management System](https://github.com/hoangtv2000/bookstore_management)

---

**⭐ Nếu thấy hữu ích, hãy star repo này!**

---

## Các chức năng đã hoàn thành

| STT | Chức năng | Mô tả | Trạng thái |
|---|---|---|---|
| 1 | **Đăng nhập** | Xác thực giảng viên bằng SHA256 | ✅ |
| 2 | **Quản lý câu hỏi** | Thêm/sửa/xóa câu hỏi theo môn, độ khó | ✅ |
| 3 | **Soạn đề thi** | Tạo đề từ ngân hàng câu hỏi, kiểm tra tham số | ✅ |
| 4 | **Tra cứu đề thi** | Tìm kiếm theo môn, HK, năm học | ✅ |
| 5 | **Nhập điểm** | Ghi nhận điểm, tự động tính điểm chữ | ✅ |
| 6 | **Báo cáo năm** | Thống kê phân loại điểm, tỉ lệ đỗ | ✅ |
| 7 | **Tham số hệ thống** | Thay đổi số câu tối đa, thời lượng, ... | ✅ |

---

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
