# CHƯƠNG 6: THIẾT KẾ DỮ LIỆU

## 6.1. Mô hình thực thể liên kết (ERD)

```
┌─────────────────┐         ┌─────────────────┐
│   GIANG_VIEN    │ 1     * │    CAU_HOI      │
├─────────────────┤◄────────┤─────────────────┤
│ MaGV [PK]       │         │ MaCauHoi [PK]   │
│ HoTen           │         │ NoiDung         │
│ MatKhau         │         │ MaMon [FK]      │
│ Email           │         │ MaDoKho [FK]    │
│ SDT             │         │ MaGV [FK]       │
└────────┬────────┘         └────────┬────────┘
         │                           │
         │ 1                         │ *
         │                           │
         │ *                   ┌─────▼────────┐
┌────────▼────────┐            │   CT_DETHI   │
│     DE_THI      │ 1         *│──────────────│
├─────────────────┤◄───────────│ MaDT [PK,FK] │
│ MaDT [PK]       │            │ MaCauHoi [PK,FK]
│ TenDT           │            │ DiemSo       │
│ MaMon [FK]      │            └──────────────┘
│ HocKy           │
│ Nam             │            ┌──────────────┐
│ ThoiGian        │       *    │   MON_HOC    │
│ NgayTao         │◄───────────┤──────────────┤
│ MaGV [FK]       │            │ MaMon [PK]   │
└────────┬────────┘            │ TenMon       │
         │                     │ SoTinChi     │
         │ 1                   │ GhiChu       │
         │                     └──────────────┘
         │ *
┌────────▼────────┐            ┌──────────────┐
│    KET_QUA      │       *    │    DO_KHO    │
├─────────────────┤◄───────────┤──────────────┤
│ MaDT [PK,FK]    │            │ MaDoKho [PK] │
│ MaSV [PK,FK]    │            │ TenDoKho     │
│ DiemSo          │            │ MoTa         │
│ DiemChu         │            └──────────────┘
└────────┬────────┘
         │
         │ *
         │
         │ 1
┌────────▼────────┐            ┌──────────────┐
│   SINH_VIEN     │       *    │   LOP_HOC    │
├─────────────────┤◄───────────┤──────────────┤
│ MaSV [PK]       │            │ MaLop [PK]   │
│ HoTen           │            │ TenLop       │
│ NgaySinh        │            │ NamHoc       │
│ GioiTinh        │            │ SiSo         │
│ MaLop [FK]      │            └──────────────┘
└─────────────────┘


┌──────────────────┐          ┌──────────────────┐
│  BANG_DIEM_CHU   │          │     THAM_SO      │
├──────────────────┤          ├──────────────────┤
│ MaDiem [PK]      │          │ MaThamSo [PK]    │
│ DiemChu          │          │ TenThamSo        │
│ DiemSoMin        │          │ GiaTri           │
│ DiemSoMax        │          │ MoTa             │
└──────────────────┘          └──────────────────┘
```

**Hình 6.1: Mô hình ERD của hệ thống**

---

## 6.2. Sơ đồ quan hệ

**Hình 6.2: Sơ đồ quan hệ các bảng**

1. **GIANG_VIEN (1) → (N) CAU_HOI**: Một giảng viên soạn nhiều câu hỏi
2. **GIANG_VIEN (1) → (N) DE_THI**: Một giảng viên soạn nhiều đề thi
3. **MON_HOC (1) → (N) CAU_HOI**: Một môn học có nhiều câu hỏi
4. **MON_HOC (1) → (N) DE_THI**: Một môn học có nhiều đề thi
5. **DO_KHO (1) → (N) CAU_HOI**: Một độ khó áp dụng cho nhiều câu hỏi
6. **DE_THI (1) → (N) CT_DETHI**: Một đề thi chứa nhiều câu hỏi (chi tiết)
7. **CAU_HOI (1) → (N) CT_DETHI**: Một câu hỏi có thể xuất hiện trong nhiều đề
8. **DE_THI (1) → (N) KET_QUA**: Một đề thi có nhiều kết quả (từ nhiều SV)
9. **SINH_VIEN (1) → (N) KET_QUA**: Một sinh viên có nhiều kết quả (nhiều đề)
10. **LOP_HOC (1) → (N) SINH_VIEN**: Một lớp có nhiều sinh viên

---

## 6.3. Từ điển dữ liệu

### 6.3.1. Bảng GIANG_VIEN

**Bảng 6.1: Từ điển dữ liệu - GIANG_VIEN**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaGV | NVARCHAR | 10 | NO | - | PRIMARY KEY | Mã giảng viên |
| HoTen | NVARCHAR | 100 | NO | - | - | Họ và tên đầy đủ |
| MatKhau | NVARCHAR | 64 | NO | - | - | Mật khẩu đã mã hóa SHA256 |
| Email | NVARCHAR | 100 | YES | NULL | UNIQUE | Email liên hệ |
| SDT | NVARCHAR | 15 | YES | NULL | - | Số điện thoại |

**Ví dụ dữ liệu:**
```
MaGV       | HoTen                  | MatKhau (hash)                           | Email
gv01       | Nguyễn Văn A           | 8d969eef6ecad3c29a3a629280e686cf0c3f5d5... | nguyenvana@uit.edu.vn
gv02       | Trần Thị B             | 481f6cc0511143ccdd7e2d1b1b94faf0a7a1c18... | tranthib@uit.edu.vn
```

### 6.3.2. Bảng MON_HOC

**Bảng 6.2: Từ điển dữ liệu - MON_HOC**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaMon | NVARCHAR | 10 | NO | - | PRIMARY KEY | Mã môn học |
| TenMon | NVARCHAR | 100 | NO | - | - | Tên môn học |
| SoTinChi | INT | - | NO | 3 | CHECK (SoTinChi > 0) | Số tín chỉ |
| GhiChu | NVARCHAR | 500 | YES | NULL | - | Ghi chú |

**Ví dụ dữ liệu:**
```
MaMon   | TenMon                           | SoTinChi | GhiChu
SE104   | Nhập môn Công nghệ phần mềm      | 4        | Môn bắt buộc
SE113   | Thiết kế phần mềm                | 4        | -
SE114   | Kiểm thử phần mềm                | 3        | -
```

### 6.3.3. Bảng DO_KHO

**Bảng 6.3: Từ điển dữ liệu - DO_KHO**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaDoKho | NVARCHAR | 10 | NO | - | PRIMARY KEY | Mã độ khó |
| TenDoKho | NVARCHAR | 50 | NO | - | - | Tên độ khó |
| MoTa | NVARCHAR | 200 | YES | NULL | - | Mô tả chi tiết |

**Ví dụ dữ liệu:**
```
MaDoKho | TenDoKho       | MoTa
DK01    | Dễ             | Câu hỏi kiến thức cơ bản
DK02    | Trung bình     | Câu hỏi vận dụng
DK03    | Khó            | Câu hỏi phân tích, tổng hợp
DK04    | Rất khó        | Câu hỏi nâng cao, sáng tạo
```

### 6.3.4. Bảng CAU_HOI

**Bảng 6.4: Từ điển dữ liệu - CAU_HOI**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaCauHoi | NVARCHAR | 10 | NO | - | PRIMARY KEY | Mã câu hỏi |
| NoiDung | NVARCHAR | 500 | NO | - | CHECK (LEN(NoiDung) >= 10) | Nội dung câu hỏi |
| MaMon | NVARCHAR | 10 | NO | - | FOREIGN KEY → MON_HOC | Thuộc môn học nào |
| MaDoKho | NVARCHAR | 10 | NO | - | FOREIGN KEY → DO_KHO | Độ khó của câu |
| MaGV | NVARCHAR | 10 | NO | - | FOREIGN KEY → GIANG_VIEN | Người soạn |

**Index:**
- `IX_CAU_HOI_MaMon` ON (MaMon)
- `IX_CAU_HOI_MaDoKho` ON (MaDoKho)
- `IX_CAU_HOI_MaGV` ON (MaGV)

**Ví dụ dữ liệu:**
```
MaCauHoi | NoiDung                                                      | MaMon | MaDoKho | MaGV
CH0001   | Vẽ use case diagram cho hệ thống quản lý thư viện           | SE104 | DK02    | gv01
CH0002   | Giải thích các bước của quy trình RUP                        | SE104 | DK01    | gv01
CH0003   | Phân tích lớp đối tượng trong hệ thống quản lý bán hàng     | SE113 | DK03    | gv01
```

### 6.3.5. Bảng DE_THI

**Bảng 6.5: Từ điển dữ liệu - DE_THI**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaDT | NVARCHAR | 10 | NO | - | PRIMARY KEY | Mã đề thi |
| TenDT | NVARCHAR | 200 | NO | - | CHECK (LEN(TenDT) >= 5) | Tên đề thi |
| MaMon | NVARCHAR | 10 | NO | - | FOREIGN KEY → MON_HOC | Thuộc môn học nào |
| HocKy | INT | - | NO | 1 | CHECK (HocKy IN (1,2,3)) | Học kỳ 1, 2, 3 |
| Nam | INT | - | NO | - | CHECK (Nam BETWEEN 2000 AND 2100) | Năm học |
| ThoiGian | INT | - | NO | 90 | CHECK (ThoiGian BETWEEN 15 AND 180) | Thời gian thi (phút) |
| NgayTao | DATETIME | - | NO | GETDATE() | - | Ngày tạo đề |
| MaGV | NVARCHAR | 10 | NO | - | FOREIGN KEY → GIANG_VIEN | Người soạn đề |

**Index:**
- `IX_DE_THI_MaMon` ON (MaMon)
- `IX_DE_THI_MaGV` ON (MaGV)
- `IX_DE_THI_NgayTao` ON (NgayTao DESC)

**Ví dụ dữ liệu:**
```
MaDT  | TenDT                    | MaMon | HocKy | Nam  | ThoiGian | NgayTao             | MaGV
DT001 | Đề thi giữa kỳ CNPM      | SE104 | 1     | 2026 | 90       | 2026-03-01 10:00:00 | gv01
DT002 | Đề thi cuối kỳ CNPM      | SE104 | 1     | 2026 | 120      | 2026-05-01 14:00:00 | gv01
```

### 6.3.6. Bảng CT_DETHI (Chi tiết đề thi)

**Bảng 6.6: Từ điển dữ liệu - CT_DETHI**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaDT | NVARCHAR | 10 | NO | - | PRIMARY KEY, FOREIGN KEY → DE_THI | Mã đề thi |
| MaCauHoi | NVARCHAR | 10 | NO | - | PRIMARY KEY, FOREIGN KEY → CAU_HOI | Mã câu hỏi |
| DiemSo | DECIMAL | (4,1) | NO | - | CHECK (DiemSo BETWEEN 0 AND 10) | Điểm số của câu |

**Ràng buộc đặc biệt:**
- Composite Primary Key: (MaDT, MaCauHoi)
- Tổng DiemSo của tất cả câu hỏi trong 1 đề phải = 10 (kiểm tra ở tầng Business Logic)

**Ví dụ dữ liệu:**
```
MaDT  | MaCauHoi | DiemSo
DT001 | CH0001   | 2.0
DT001 | CH0002   | 1.5
DT001 | CH0003   | 2.5
DT001 | CH0005   | 1.0
DT001 | CH0007   | 1.5
DT001 | CH0010   | 1.5
(Tổng = 10.0)
```

### 6.3.7. Bảng LOP_HOC

**Bảng 6.7: Từ điển dữ liệu - LOP_HOC**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaLop | NVARCHAR | 20 | NO | - | PRIMARY KEY | Mã lớp học |
| TenLop | NVARCHAR | 100 | NO | - | - | Tên lớp |
| NamHoc | INT | - | NO | - | CHECK (NamHoc BETWEEN 2000 AND 2100) | Năm học |
| SiSo | INT | - | YES | 0 | CHECK (SiSo >= 0) | Sĩ số lớp |

**Ví dụ dữ liệu:**
```
MaLop      | TenLop                                | NamHoc | SiSo
SE104.Q23  | Nhập môn CNPM - Nhóm thứ 2, thứ 4     | 2026   | 45
SE104.Q24  | Nhập môn CNPM - Nhóm thứ 3, thứ 5     | 2026   | 50
SE113.Q11  | Thiết kế phần mềm - Nhóm thứ 6        | 2026   | 40
```

### 6.3.8. Bảng SINH_VIEN

**Bảng 6.8: Từ điển dữ liệu - SINH_VIEN**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaSV | NVARCHAR | 10 | NO | - | PRIMARY KEY | Mã sinh viên |
| HoTen | NVARCHAR | 100 | NO | - | - | Họ và tên |
| NgaySinh | DATE | - | YES | NULL | - | Ngày sinh |
| GioiTinh | NVARCHAR | 10 | YES | NULL | CHECK (GioiTinh IN (N'Nam', N'Nữ')) | Giới tính |
| MaLop | NVARCHAR | 20 | NO | - | FOREIGN KEY → LOP_HOC | Thuộc lớp nào |

**Index:**
- `IX_SINH_VIEN_MaLop` ON (MaLop)

**Ví dụ dữ liệu:**
```
MaSV     | HoTen                    | NgaySinh   | GioiTinh | MaLop
21520001 | Nguyễn Văn An            | 2003-05-15 | Nam      | SE104.Q23
21520002 | Trần Thị Bình            | 2003-08-20 | Nữ       | SE104.Q23
21520003 | Lê Hoàng Cường           | 2003-03-10 | Nam      | SE104.Q23
```

### 6.3.9. Bảng KET_QUA

**Bảng 6.9: Từ điển dữ liệu - KET_QUA**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaDT | NVARCHAR | 10 | NO | - | PRIMARY KEY, FOREIGN KEY → DE_THI | Mã đề thi |
| MaSV | NVARCHAR | 10 | NO | - | PRIMARY KEY, FOREIGN KEY → SINH_VIEN | Mã sinh viên |
| DiemSo | DECIMAL | (4,1) | YES | NULL | CHECK (DiemSo BETWEEN 0 AND 10) | Điểm số |
| DiemChu | NVARCHAR | 5 | YES | NULL | - | Điểm chữ (A, B+, B...) |

**Ràng buộc đặc biệt:**
- Composite Primary Key: (MaDT, MaSV)
- DiemChu được tính tự động dựa trên DiemSo và bảng BANG_DIEM_CHU

**Index:**
- `IX_KET_QUA_MaDT` ON (MaDT)
- `IX_KET_QUA_MaSV` ON (MaSV)

**Ví dụ dữ liệu:**
```
MaDT  | MaSV     | DiemSo | DiemChu
DT001 | 21520001 | 8.5    | B+
DT001 | 21520002 | 7.0    | C+
DT001 | 21520003 | 9.5    | A
```

### 6.3.10. Bảng BANG_DIEM_CHU

**Bảng 6.10: Từ điển dữ liệu - BANG_DIEM_CHU**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaDiem | NVARCHAR | 10 | NO | - | PRIMARY KEY | Mã điểm chữ |
| DiemChu | NVARCHAR | 5 | NO | - | - | Điểm chữ (A, B+...) |
| DiemSoMin | DECIMAL | (4,1) | NO | - | - | Điểm số tối thiểu |
| DiemSoMax | DECIMAL | (4,1) | NO | - | - | Điểm số tối đa |

**Ví dụ dữ liệu:**
```
MaDiem | DiemChu | DiemSoMin | DiemSoMax
DC01   | A       | 9.0       | 10.0
DC02   | B+      | 8.5       | 8.9
DC03   | B       | 8.0       | 8.4
DC04   | C+      | 7.0       | 7.9
DC05   | C       | 6.5       | 6.9
DC06   | D+      | 5.5       | 6.4
DC07   | D       | 5.0       | 5.4
DC08   | F       | 0.0       | 4.9
```

### 6.3.11. Bảng THAM_SO

**Bảng 6.11: Từ điển dữ liệu - THAM_SO**

| Tên cột | Kiểu dữ liệu | Độ dài | Null | Mặc định | Ràng buộc | Mô tả |
|---------|-------------|--------|------|----------|-----------|-------|
| MaThamSo | NVARCHAR | 10 | NO | - | PRIMARY KEY | Mã tham số |
| TenThamSo | NVARCHAR | 100 | NO | - | - | Tên tham số |
| GiaTri | NVARCHAR | 50 | NO | - | - | Giá trị |
| MoTa | NVARCHAR | 200 | YES | NULL | - | Mô tả |

**Ví dụ dữ liệu:**
```
MaThamSo | TenThamSo              | GiaTri | MoTa
TS01     | SoCauToiThieu          | 5      | Số câu hỏi tối thiểu trong một đề thi
TS02     | ThoiGianThiMacDinh     | 90     | Thời gian thi mặc định (phút)
TS03     | SoCauHoiCanhBao        | 10     | Cảnh báo khi môn học có < X câu hỏi
```

---

## 6.4. Stored Procedures

**Bảng 6.12: Danh sách Stored Procedures**

| Tên SP | Tham số | Mục đích | Trả về |
|--------|---------|----------|--------|
| sp_BaoCaoNam | @Nam INT | Thống kê số lượng đề thi theo môn học trong một năm | Table (TenMon, SoLuongDe) |
| sp_TraCuuDeThi | @MaMon, @HocKy, @Nam | Tra cứu đề thi theo điều kiện | Table (thông tin đề thi) |
| sp_GetDiemChu | @DiemSo DECIMAL | Lấy điểm chữ từ điểm số | NVARCHAR (điểm chữ) |
| sp_ThongKeCauHoi | @MaMon | Đếm số câu hỏi theo độ khó của môn | Table (TenDoKho, SoLuong) |

### 6.4.1. sp_BaoCaoNam

**Hình 6.3: Stored Procedure sp_BaoCaoNam**

```sql
CREATE PROCEDURE sp_BaoCaoNam
    @Nam INT
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT 
        MH.TenMon,
        COUNT(DT.MaDT) AS SoLuongDe
    FROM 
        DE_THI DT
    INNER JOIN 
        MON_HOC MH ON DT.MaMon = MH.MaMon
    WHERE 
        DT.Nam = @Nam
    GROUP BY 
        MH.TenMon
    ORDER BY 
        SoLuongDe DESC;
END
GO
```

**Ví dụ sử dụng:**
```sql
EXEC sp_BaoCaoNam @Nam = 2026

-- Kết quả:
-- TenMon                              | SoLuongDe
-- Nhập môn Công nghệ phần mềm         | 5
-- Thiết kế phần mềm                   | 3
-- Kiểm thử phần mềm                   | 2
```

### 6.4.2. sp_TraCuuDeThi

**Hình 6.4: Stored Procedure sp_TraCuuDeThi**

```sql
CREATE PROCEDURE sp_TraCuuDeThi
    @MaMon NVARCHAR(10) = NULL,
    @HocKy INT = NULL,
    @Nam INT = NULL
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT 
        DT.MaDT,
        DT.TenDT,
        MH.TenMon,
        DT.HocKy,
        DT.Nam,
        DT.ThoiGian,
        DT.NgayTao,
        (SELECT COUNT(*) FROM CT_DETHI WHERE MaDT = DT.MaDT) AS SoCau,
        GV.HoTen AS GiangVien
    FROM 
        DE_THI DT
    INNER JOIN 
        MON_HOC MH ON DT.MaMon = MH.MaMon
    INNER JOIN
        GIANG_VIEN GV ON DT.MaGV = GV.MaGV
    WHERE 
        (@MaMon IS NULL OR DT.MaMon = @MaMon)
        AND (@HocKy IS NULL OR DT.HocKy = @HocKy)
        AND (@Nam IS NULL OR DT.Nam = @Nam)
    ORDER BY 
        DT.NgayTao DESC;
END
GO
```

### 6.4.3. sp_GetDiemChu

```sql
CREATE PROCEDURE sp_GetDiemChu
    @DiemSo DECIMAL(4,1)
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @DiemChu NVARCHAR(5);
    
    SELECT TOP 1 
        @DiemChu = DiemChu
    FROM 
        BANG_DIEM_CHU
    WHERE 
        @DiemSo >= DiemSoMin AND @DiemSo <= DiemSoMax
    ORDER BY 
        DiemSoMin DESC;
    
    SELECT @DiemChu AS DiemChu;
END
GO
```

### 6.4.4. sp_ThongKeCauHoi

```sql
CREATE PROCEDURE sp_ThongKeCauHoi
    @MaMon NVARCHAR(10)
AS
BEGIN
    SET NOCOUNT ON;
    
    SELECT 
        DK.TenDoKho,
        COUNT(CH.MaCauHoi) AS SoLuong
    FROM 
        DO_KHO DK
    LEFT JOIN 
        CAU_HOI CH ON DK.MaDoKho = CH.MaDoKho AND CH.MaMon = @MaMon
    GROUP BY 
        DK.TenDoKho
    ORDER BY 
        DK.TenDoKho;
END
GO
```

---

## 6.5. Ràng buộc toàn vẹn dữ liệu

**Bảng 6.13: Ràng buộc toàn vẹn dữ liệu**

| Loại ràng buộc | Bảng | Mô tả | SQL |
|----------------|------|-------|-----|
| **Primary Key** | Tất cả bảng | Đảm bảo mỗi dòng duy nhất | `CONSTRAINT PK_TenBang PRIMARY KEY (TenCot)` |
| **Foreign Key** | CAU_HOI → MON_HOC | Câu hỏi phải thuộc môn hợp lệ | `CONSTRAINT FK_CauHoi_MonHoc FOREIGN KEY (MaMon) REFERENCES MON_HOC(MaMon)` |
| **Foreign Key** | CAU_HOI → DO_KHO | Câu hỏi phải có độ khó hợp lệ | `CONSTRAINT FK_CauHoi_DoKho FOREIGN KEY (MaDoKho) REFERENCES DO_KHO(MaDoKho)` |
| **Foreign Key** | CAU_HOI → GIANG_VIEN | Câu hỏi phải do GV hợp lệ tạo | `CONSTRAINT FK_CauHoi_GiangVien FOREIGN KEY (MaGV) REFERENCES GIANG_VIEN(MaGV)` |
| **Foreign Key** | DE_THI → MON_HOC | Đề thi phải thuộc môn hợp lệ | `CONSTRAINT FK_DeThi_MonHoc FOREIGN KEY (MaMon) REFERENCES MON_HOC(MaMon)` |
| **Foreign Key** | DE_THI → GIANG_VIEN | Đề thi phải do GV hợp lệ tạo | `CONSTRAINT FK_DeThi_GiangVien FOREIGN KEY (MaGV) REFERENCES GIANG_VIEN(MaGV)` |
| **Foreign Key** | CT_DETHI → DE_THI | Chi tiết phải thuộc đề hợp lệ | `CONSTRAINT FK_CTDeThi_DeThi FOREIGN KEY (MaDT) REFERENCES DE_THI(MaDT) ON DELETE CASCADE` |
| **Foreign Key** | CT_DETHI → CAU_HOI | Chi tiết phải chứa câu hợp lệ | `CONSTRAINT FK_CTDeThi_CauHoi FOREIGN KEY (MaCauHoi) REFERENCES CAU_HOI(MaCauHoi)` |
| **Foreign Key** | SINH_VIEN → LOP_HOC | Sinh viên phải thuộc lớp hợp lệ | `CONSTRAINT FK_SinhVien_LopHoc FOREIGN KEY (MaLop) REFERENCES LOP_HOC(MaLop)` |
| **Foreign Key** | KET_QUA → DE_THI | Kết quả phải thuộc đề hợp lệ | `CONSTRAINT FK_KetQua_DeThi FOREIGN KEY (MaDT) REFERENCES DE_THI(MaDT) ON DELETE CASCADE` |
| **Foreign Key** | KET_QUA → SINH_VIEN | Kết quả phải thuộc SV hợp lệ | `CONSTRAINT FK_KetQua_SinhVien FOREIGN KEY (MaSV) REFERENCES SINH_VIEN(MaSV)` |
| **Check** | CAU_HOI.NoiDung | Nội dung tối thiểu 10 ký tự | `CONSTRAINT CK_CauHoi_NoiDung CHECK (LEN(NoiDung) >= 10)` |
| **Check** | DE_THI.HocKy | Học kỳ từ 1-3 | `CONSTRAINT CK_DeThi_HocKy CHECK (HocKy IN (1,2,3))` |
| **Check** | DE_THI.Nam | Năm từ 2000-2100 | `CONSTRAINT CK_DeThi_Nam CHECK (Nam BETWEEN 2000 AND 2100)` |
| **Check** | DE_THI.ThoiGian | Thời gian 15-180 phút | `CONSTRAINT CK_DeThi_ThoiGian CHECK (ThoiGian BETWEEN 15 AND 180)` |
| **Check** | CT_DETHI.DiemSo | Điểm từ 0-10 | `CONSTRAINT CK_CTDeThi_DiemSo CHECK (DiemSo BETWEEN 0 AND 10)` |
| **Check** | KET_QUA.DiemSo | Điểm từ 0-10 | `CONSTRAINT CK_KetQua_DiemSo CHECK (DiemSo BETWEEN 0 AND 10)` |
| **Check** | SINH_VIEN.GioiTinh | Nam hoặc Nữ | `CONSTRAINT CK_SinhVien_GioiTinh CHECK (GioiTinh IN (N'Nam', N'Nữ'))` |
| **Unique** | GIANG_VIEN.Email | Email không trùng lặp | `CONSTRAINT UQ_GiangVien_Email UNIQUE (Email)` |
| **Default** | DE_THI.NgayTao | Ngày tạo mặc định | `CONSTRAINT DF_DeThi_NgayTao DEFAULT (GETDATE())` |
| **Default** | DE_THI.ThoiGian | Thời gian mặc định 90 phút | `CONSTRAINT DF_DeThi_ThoiGian DEFAULT (90)` |

**Ràng buộc phức tạp (kiểm tra ở Business Logic):**
- **BR_DeThi_TongDiem**: Tổng điểm của tất cả câu hỏi trong 1 đề thi phải = 10
- **BR_DeThi_SoCau**: Số câu hỏi trong 1 đề ≥ SoCauToiThieu (từ bảng THAM_SO)
- **BR_CauHoi_XoaTrongDeThi**: Không được xóa câu hỏi đã có trong đề thi

---

**Kết luận chương 6**: Chương này đã thiết kế cơ sở dữ liệu hoàn chỉnh với 11 bảng, ERD, từ điển dữ liệu chi tiết, 4 stored procedures và các ràng buộc toàn vẹn. Thiết kế đạt chuẩn 3NF, đảm bảo tính nhất quán và hiệu năng truy vấn cao. Chương tiếp theo sẽ thiết kế giao diện người dùng.

