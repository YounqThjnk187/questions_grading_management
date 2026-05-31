#  Hệ thống Quản lý Ra đề và Chấm thi
## Nhóm 15 – SE104.Q23

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/YounqThjnk187/questions_grading_management)
[![.NET Framework](https://img.shields.io/badge/.NET%20Framework-4.6.1-512BD4)](https://dotnet.microsoft.com/)
[![Python Demo](https://img.shields.io/badge/Python-3.11-3776AB)](https://www.python.org/)

---

## Giới thiệu nhanh

Đây là hệ thống hỗ trợ giảng viên quản lý câu hỏi – tạo đề thi – nhập điểm – tra cứu kết quả.

Hệ thống gồm 2 phiên bản:

- 💻 ASP.NET MVC (bản chính)
- 🐍 Python Demo (chạy nhanh, không cần Visual Studio)

## Cách chạy nhanh (Python demo)

```powershell
cd QuanLyRaDeChamThi
python demo_app.py
```

Truy cập: http://localhost8080
Đăng nhập: gv01 / 123456

## Chức năng chính
1. Ngân hàng câu hỏi
- Thêm / sửa / xóa câu hỏi
- Phân loại theo môn học và độ khó
- Tìm kiếm và lọc câu hỏi

2. Soạn đề thi
- Chọn câu hỏi từ ngân hàng
- Giới hạn số lượng theo quy định
- Thiết lập thời gian thi

3. Nhập điểm
- Nhập điểm 0–10
- Tự động quy đổi điểm chữ (A, B+, B,...)
- Lưu lịch sử chấm điểm

4. Tra cứu đề thi
- Tìm theo môn học / học kỳ / năm học
- Xem chi tiết đề thi

5. Báo cáo thống kê
- Phân loại điểm theo mức
- Tính điểm trung bình
- Xuất báo cáo CSV

6. Quản lý hệ thống
- Quy định số câu hỏi / thời gian thi
- Quản lý lớp, sinh viên, môn học

## Công nghệ sử dụng 

Backend chính
- ASP.NET MVC 5 (C#)
- Entity Framework 6
- SQL Server / LocalDB
- Bootstrap + jQuery

Demo nhanh
- Python 3.11 (không cần thư viện ngoài)
- SQLite database
- HTTP server built-in

## Cấu trúc hệ thống

```powershell
QuanLyRaDeChamThi/
├── Controllers/   (CauHoi, DeThi, KetQua,...)
├── Models/        (Entity Framework)
├── Views/         (Giao diện Razor)
├── Database/      (SQL script)
├── demo_app.py    (Python demo)
└── README.md
```

## Cơ sở dữ liệu

Hệ thống gồm 11 bảng chính:

- GIANG_VIEN
- MON_HOC
- DO_KHO
- CAU_HOI
- DE_THI
- CT_DETHI
- LOP_HOC
- SINH_VIEN
- KET_QUA
- BANG_DIEM_CHU
- THAM_SO

## Điểm nổi bật
✔ CRUD đầy đủ (câu hỏi, đề thi, điểm)
✔ Tra cứu linh hoạt
✔ Tự động tính điểm chữ
✔ Giao diện Bootstrap responsive
✔ Có bản demo Python chạy ngay
✔ Tách module rõ ràng theo MVC

## Tài khoản mẫu

```powershell
Username	Password
gv01	123456
gv02	123456
gv03	123456
```

## Bảng điểm chữ

```powershell
Điểm	Chữ
8.5–10	A
8.0–8.4	B+
7.0–7.9	B
6.5–6.9	C+
5.5–6.4	C
5.0–5.4	D+
4.0–4.9	D
<4.0	F
```

## Kết luận

Hệ thống giúp:

- Giảm thời gian ra đề
- Tự động hóa chấm điểm
- Quản lý tập trung dữ liệu thi