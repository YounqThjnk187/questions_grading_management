-- ============================================================
-- HỆ THỐNG QUẢN LÝ RA ĐỀ VÀ CHẤM THI
-- Nhóm 15 - SE104.Q23
-- ============================================================

USE master;
GO

IF EXISTS (SELECT name FROM sys.databases WHERE name = N'QuanLyRaDeChamThi')
    DROP DATABASE QuanLyRaDeChamThi;
GO

CREATE DATABASE QuanLyRaDeChamThi;
GO

USE QuanLyRaDeChamThi;
GO

-- ============================================================
-- 1. BẢNG GIẢNG VIÊN
-- ============================================================
CREATE TABLE GIANG_VIEN (
    MaGV        INT IDENTITY(1,1) PRIMARY KEY,
    HoTen       NVARCHAR(100) NOT NULL,
    TenDangNhap VARCHAR(50)  NOT NULL UNIQUE,
    MatKhau     VARCHAR(256) NOT NULL,  -- lưu dạng SHA256 hash
    Email       VARCHAR(100)
);
GO

-- ============================================================
-- 2. BẢNG MÔN HỌC
-- ============================================================
CREATE TABLE MON_HOC (
    MaMon   INT IDENTITY(1,1) PRIMARY KEY,
    TenMon  NVARCHAR(100) NOT NULL,
    MaGV    INT NOT NULL,
    CONSTRAINT FK_MonHoc_GiangVien FOREIGN KEY (MaGV) REFERENCES GIANG_VIEN(MaGV)
);
GO

-- ============================================================
-- 3. BẢNG ĐỘ KHÓ
-- ============================================================
CREATE TABLE DO_KHO (
    MaDoKho     INT IDENTITY(1,1) PRIMARY KEY,
    TenDoKho    NVARCHAR(50) NOT NULL
);
GO

-- ============================================================
-- 4. BẢNG CÂU HỎI
-- ============================================================
CREATE TABLE CAU_HOI (
    MaCH        INT IDENTITY(1,1) PRIMARY KEY,
    NoiDung     NVARCHAR(MAX) NOT NULL,
    MaMon       INT NOT NULL,
    MaDoKho     INT NOT NULL,
    CONSTRAINT FK_CauHoi_MonHoc FOREIGN KEY (MaMon) REFERENCES MON_HOC(MaMon),
    CONSTRAINT FK_CauHoi_DoKho  FOREIGN KEY (MaDoKho) REFERENCES DO_KHO(MaDoKho)
);
GO

-- ============================================================
-- 5. BẢNG ĐỀ THI
-- ============================================================
CREATE TABLE DE_THI (
    MaDT        INT IDENTITY(1,1) PRIMARY KEY,
    MaMon       INT NOT NULL,
    HocKy       TINYINT NOT NULL CHECK (HocKy IN (1,2)),
    NamHoc      VARCHAR(10) NOT NULL,   -- ví dụ: 2024-2025
    ThoiLuong   INT NOT NULL CHECK (ThoiLuong BETWEEN 30 AND 180),
    NgayThi     DATE,
    MaGV        INT NOT NULL,
    CONSTRAINT FK_DeThi_MonHoc    FOREIGN KEY (MaMon) REFERENCES MON_HOC(MaMon),
    CONSTRAINT FK_DeThi_GiangVien FOREIGN KEY (MaGV)  REFERENCES GIANG_VIEN(MaGV)
);
GO

-- ============================================================
-- 6. BẢNG CHI TIẾT ĐỀ THI (junction)
-- ============================================================
CREATE TABLE CT_DETHI (
    MaDT    INT NOT NULL,
    MaCH    INT NOT NULL,
    PRIMARY KEY (MaDT, MaCH),
    CONSTRAINT FK_CT_DeThi  FOREIGN KEY (MaDT) REFERENCES DE_THI(MaDT) ON DELETE CASCADE,
    CONSTRAINT FK_CT_CauHoi FOREIGN KEY (MaCH) REFERENCES CAU_HOI(MaCH)
);
GO

-- ============================================================
-- 7. BẢNG LỚP HỌC
-- ============================================================
CREATE TABLE LOP_HOC (
    MaLop   INT IDENTITY(1,1) PRIMARY KEY,
    TenLop  NVARCHAR(50) NOT NULL,
    NamHoc  VARCHAR(10) NOT NULL,
    MaGV    INT NOT NULL,
    CONSTRAINT FK_LopHoc_GiangVien FOREIGN KEY (MaGV) REFERENCES GIANG_VIEN(MaGV)
);
GO

-- ============================================================
-- 8. BẢNG SINH VIÊN
-- ============================================================
CREATE TABLE SINH_VIEN (
    MaSV        INT IDENTITY(1,1) PRIMARY KEY,
    HoTen       NVARCHAR(100) NOT NULL,
    NgaySinh    DATE,
    MaLop       INT NOT NULL,
    CONSTRAINT FK_SinhVien_LopHoc FOREIGN KEY (MaLop) REFERENCES LOP_HOC(MaLop)
);
GO

-- ============================================================
-- 9. BẢNG KẾT QUẢ THI
-- ============================================================
CREATE TABLE KET_QUA (
    MaSV        INT NOT NULL,
    MaDT        INT NOT NULL,
    DiemSo      DECIMAL(4,2) NOT NULL CHECK (DiemSo BETWEEN 0 AND 10),
    DiemChu     VARCHAR(5),
    NgayCham    DATE DEFAULT GETDATE(),
    PRIMARY KEY (MaSV, MaDT),
    CONSTRAINT FK_KetQua_SinhVien FOREIGN KEY (MaSV) REFERENCES SINH_VIEN(MaSV),
    CONSTRAINT FK_KetQua_DeThi    FOREIGN KEY (MaDT) REFERENCES DE_THI(MaDT)
);
GO

-- ============================================================
-- 10. BẢNG BẢNG ĐIỂM CHỮ
-- ============================================================
CREATE TABLE BANG_DIEM_CHU (
    DiemChu     VARCHAR(5)      NOT NULL PRIMARY KEY,
    DiemSoTu    DECIMAL(4,2)    NOT NULL,
    DiemSoDen   DECIMAL(4,2)    NOT NULL,
    GhiChu      NVARCHAR(100)
);
GO

-- ============================================================
-- 11. BẢNG THAM SỐ
-- ============================================================
CREATE TABLE THAM_SO (
    TenThamSo   VARCHAR(50)     NOT NULL PRIMARY KEY,
    GiaTri      INT             NOT NULL,
    GhiChu      NVARCHAR(200)
);
GO

-- ============================================================
-- DỮ LIỆU MẪU
-- ============================================================

-- Độ khó (4 mức)
INSERT INTO DO_KHO (TenDoKho) VALUES
    (N'Dễ'),
    (N'Trung Bình'),
    (N'Phức Tạp'),
    (N'Khó');
GO

-- Bảng điểm chữ
INSERT INTO BANG_DIEM_CHU (DiemChu, DiemSoTu, DiemSoDen, GhiChu) VALUES
    ('A',   8.5,  10.0, N'Xuất sắc'),
    ('B+',  8.0,   8.4, N'Giỏi'),
    ('B',   7.0,   7.9, N'Khá'),
    ('C+',  6.5,   6.9, N'Trung bình khá'),
    ('C',   5.5,   6.4, N'Trung bình'),
    ('D+',  5.0,   5.4, N'Trung bình yếu'),
    ('D',   4.0,   4.9, N'Yếu'),
    ('F',   0.0,   3.9, N'Kém');
GO

-- Tham số hệ thống
INSERT INTO THAM_SO (TenThamSo, GiaTri, GhiChu) VALUES
    ('SoCauToiDa',        5,   N'Số câu hỏi tối đa mỗi đề thi'),
    ('ThoiLuongToiThieu', 30,  N'Thời lượng tối thiểu (phút)'),
    ('ThoiLuongToiDa',    180, N'Thời lượng tối đa (phút)'),
    ('SoLopToiDa',        50,  N'Số lớp tối đa mỗi năm'),
    ('SoMonToiDa',        4,   N'Số môn học tối đa');
GO

-- Giảng viên mẫu (mật khẩu: "123456" → SHA256)
-- SHA256("123456") = 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
INSERT INTO GIANG_VIEN (HoTen, TenDangNhap, MatKhau, Email) VALUES
    (N'Nguyễn Văn An',    'gv01', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 'gv01@uit.edu.vn'),
    (N'Trần Thị Bình',    'gv02', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 'gv02@uit.edu.vn'),
    (N'Lê Minh Cường',    'gv03', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', 'gv03@uit.edu.vn');
GO

-- Môn học mẫu
INSERT INTO MON_HOC (TenMon, MaGV) VALUES
    (N'Lập trình hướng đối tượng', 1),
    (N'Cơ sở dữ liệu',             1),
    (N'Mạng máy tính',             2),
    (N'Công nghệ phần mềm',        2);
GO

-- Câu hỏi mẫu
INSERT INTO CAU_HOI (NoiDung, MaMon, MaDoKho) VALUES
    (N'Kế thừa trong OOP là gì?',                                     1, 1),
    (N'Sự khác biệt giữa abstract class và interface?',               1, 2),
    (N'Polymorphism được thể hiện như thế nào trong C#?',             1, 3),
    (N'Giải thích nguyên lý SOLID.',                                  1, 4),
    (N'Override và Overload khác nhau như thế nào?',                  1, 2),
    (N'Khóa chính (Primary Key) là gì?',                              2, 1),
    (N'Sự khác biệt giữa JOIN và UNION trong SQL?',                   2, 2),
    (N'Chuẩn hóa CSDL (3NF) là gì?',                                 2, 3),
    (N'Giải thích Transaction và ACID properties.',                   2, 4),
    (N'Index trong SQL có tác dụng gì?',                              2, 2),
    (N'Giao thức TCP/IP là gì?',                                      3, 1),
    (N'HTTP và HTTPS khác nhau như thế nào?',                         3, 2),
    (N'Giải thích mô hình OSI 7 lớp.',                                3, 3),
    (N'DNS hoạt động như thế nào?',                                   3, 2),
    (N'Firewall là gì và hoạt động như thế nào?',                     3, 3),
    (N'SDLC là gì?',                                                  4, 1),
    (N'Agile và Waterfall khác nhau như thế nào?',                    4, 2),
    (N'Kiểm thử hộp đen và hộp trắng là gì?',                        4, 2),
    (N'Giải thích mô hình kiến trúc 3 lớp.',                         4, 3),
    (N'Use case diagram được dùng để làm gì?',                        4, 1);
GO

-- Lớp học mẫu
INSERT INTO LOP_HOC (TenLop, NamHoc, MaGV) VALUES
    (N'SE104.P11', '2024-2025', 1),
    (N'SE104.P12', '2024-2025', 1),
    (N'NT101.P11', '2024-2025', 2);
GO

-- Sinh viên mẫu
INSERT INTO SINH_VIEN (HoTen, NgaySinh, MaLop) VALUES
    (N'Nguyễn Văn A',   '2003-01-15', 1),
    (N'Trần Thị B',     '2003-05-20', 1),
    (N'Lê Minh C',      '2002-12-10', 1),
    (N'Phạm Thị D',     '2003-03-25', 2),
    (N'Hoàng Văn E',    '2002-08-14', 2),
    (N'Đỗ Thị F',       '2003-07-07', 3);
GO

-- Đề thi mẫu
INSERT INTO DE_THI (MaMon, HocKy, NamHoc, ThoiLuong, NgayThi, MaGV) VALUES
    (1, 1, '2024-2025', 90,  '2025-01-10', 1),
    (2, 1, '2024-2025', 60,  '2025-01-12', 1),
    (4, 1, '2024-2025', 75,  '2025-01-15', 2);
GO

-- Chi tiết đề thi
INSERT INTO CT_DETHI (MaDT, MaCH) VALUES
    (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
    (2, 6), (2, 7), (2, 8), (2, 9), (2,10),
    (3,16), (3,17), (3,18), (3,19), (3,20);
GO

-- Kết quả thi mẫu
INSERT INTO KET_QUA (MaSV, MaDT, DiemSo, NgayCham) VALUES
    (1, 1, 8.5, '2025-01-20'),
    (2, 1, 7.0, '2025-01-20'),
    (3, 1, 5.5, '2025-01-20'),
    (4, 2, 9.0, '2025-01-22'),
    (5, 2, 4.5, '2025-01-22');
GO

-- Cập nhật điểm chữ sau khi nhập điểm số
UPDATE KQ
SET DiemChu = (
    SELECT TOP 1 BDC.DiemChu
    FROM BANG_DIEM_CHU BDC
    WHERE KQ.DiemSo BETWEEN BDC.DiemSoTu AND BDC.DiemSoDen
)
FROM KET_QUA KQ;
GO

-- ============================================================
-- STORED PROCEDURES
-- ============================================================

-- SP: Lấy điểm chữ từ điểm số
CREATE PROCEDURE sp_GetDiemChu
    @DiemSo DECIMAL(4,2),
    @DiemChu VARCHAR(5) OUTPUT
AS
BEGIN
    SELECT TOP 1 @DiemChu = DiemChu
    FROM BANG_DIEM_CHU
    WHERE @DiemSo BETWEEN DiemSoTu AND DiemSoDen;
END;
GO

-- SP: Báo cáo năm - thống kê phân loại điểm theo môn học
CREATE PROCEDURE sp_BaoCaoNam
    @NamHoc VARCHAR(10),
    @MaGV INT
AS
BEGIN
    SELECT
        MH.TenMon,
        DT.HocKy,
        COUNT(KQ.MaSV) AS TongSinhVien,
        SUM(CASE WHEN KQ.DiemChu = 'A'  THEN 1 ELSE 0 END) AS SoA,
        SUM(CASE WHEN KQ.DiemChu = 'B+' THEN 1 ELSE 0 END) AS SoBPlus,
        SUM(CASE WHEN KQ.DiemChu = 'B'  THEN 1 ELSE 0 END) AS SoB,
        SUM(CASE WHEN KQ.DiemChu = 'C+' THEN 1 ELSE 0 END) AS SoCPlus,
        SUM(CASE WHEN KQ.DiemChu = 'C'  THEN 1 ELSE 0 END) AS SoC,
        SUM(CASE WHEN KQ.DiemChu = 'D+' THEN 1 ELSE 0 END) AS SoDPlus,
        SUM(CASE WHEN KQ.DiemChu = 'D'  THEN 1 ELSE 0 END) AS SoD,
        SUM(CASE WHEN KQ.DiemChu = 'F'  THEN 1 ELSE 0 END) AS SoF,
        AVG(KQ.DiemSo) AS DiemTrungBinh
    FROM DE_THI DT
    JOIN MON_HOC MH   ON MH.MaMon = DT.MaMon
    JOIN KET_QUA KQ   ON KQ.MaDT  = DT.MaDT
    WHERE DT.NamHoc = @NamHoc AND DT.MaGV = @MaGV
    GROUP BY MH.TenMon, DT.HocKy
    ORDER BY MH.TenMon, DT.HocKy;
END;
GO

-- SP: Tra cứu đề thi
CREATE PROCEDURE sp_TraCuuDeThi
    @MaGV INT,
    @TenMon NVARCHAR(100) = NULL,
    @HocKy TINYINT = NULL,
    @NamHoc VARCHAR(10) = NULL
AS
BEGIN
    SELECT
        DT.MaDT,
        MH.TenMon,
        DT.HocKy,
        DT.NamHoc,
        DT.ThoiLuong,
        DT.NgayThi,
        COUNT(CT.MaCH) AS SoCauHoi
    FROM DE_THI DT
    JOIN MON_HOC MH ON MH.MaMon = DT.MaMon
    LEFT JOIN CT_DETHI CT ON CT.MaDT = DT.MaDT
    WHERE DT.MaGV = @MaGV
      AND (@TenMon IS NULL OR MH.TenMon LIKE N'%' + @TenMon + N'%')
      AND (@HocKy  IS NULL OR DT.HocKy = @HocKy)
      AND (@NamHoc IS NULL OR DT.NamHoc = @NamHoc)
    GROUP BY DT.MaDT, MH.TenMon, DT.HocKy, DT.NamHoc, DT.ThoiLuong, DT.NgayThi
    ORDER BY DT.MaDT DESC;
END;
GO

PRINT N'Database QuanLyRaDeChamThi đã được tạo thành công!';
GO
