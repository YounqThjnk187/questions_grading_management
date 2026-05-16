# CHƯƠNG 5: THIẾT KẾ ĐỐI TƯỢNG

## 5.1. Biểu đồ lớp (Class Diagram)

Biểu đồ lớp mô tả các lớp chính trong hệ thống và quan hệ giữa chúng:

```
┌──────────────────────────┐
│      GiangVien           │
├──────────────────────────┤
│ - MaGV: string [PK]      │
│ - HoTen: string          │
│ - MatKhau: string        │
│ - Email: string          │
│ - SDT: string            │
├──────────────────────────┤
│ + Login(): bool          │
│ + UpdateProfile(): void  │
└────────┬─────────────────┘
         │ 1
         │
         │ *
┌────────▼─────────────────┐         ┌──────────────────────────┐
│       CauHoi             │    *    │        MonHoc            │
├──────────────────────────┤  ◄─────┤──────────────────────────┤
│ - MaCauHoi: string [PK]  │   MaMon│ - MaMon: string [PK]     │
│ - NoiDung: string        │         │ - TenMon: string         │
│ - MaMon: string [FK]     │         │ - SoTinChi: int          │
│ - MaDoKho: string [FK]   │         │ - GhiChu: string         │
│ - MaGV: string [FK]      │         ├──────────────────────────┤
├──────────────────────────┤         │ + GetSoCauHoi(): int     │
│ + Create(): void         │         └──────────────────────────┘
│ + Update(): void         │
│ + Delete(): bool         │         ┌──────────────────────────┐
│ + Search(keyword): List  │    *    │         DoKho            │
└────────┬─────────────────┘  ◄─────┤──────────────────────────┤
         │ *                  MaDoKho│ - MaDoKho: string [PK]   │
         │                           │ - TenDoKho: string       │
         │                           │ - MoTa: string           │
         │ *                         ├──────────────────────────┤
┌────────▼─────────────────┐         │ + GetMucDo(): string     │
│      CT_DETHI            │         └──────────────────────────┘
├──────────────────────────┤
│ - MaDT: string [PK, FK]  │ *
│ - MaCauHoi: string [PK, FK]
│ - DiemSo: decimal        │         ┌──────────────────────────┐
├──────────────────────────┤    1    │         DeThi            │
│ + CalculateTotal(): dec  │  ◄──────┤──────────────────────────┤
└────────┬─────────────────┘   MaDT  │ - MaDT: string [PK]      │
         │                           │ - TenDT: string          │
         │                           │ - MaMon: string [FK]     │
         │ 1                         │ - HocKy: int             │
┌────────▼─────────────────┐         │ - Nam: int               │
│       KetQua             │         │ - ThoiGian: int          │
├──────────────────────────┤         │ - NgayTao: DateTime      │
│ - MaDT: string [PK, FK]  │ *       │ - MaGV: string [FK]      │
│ - MaSV: string [PK, FK]  │  ◄──────┤──────────────────────────┤
│ - DiemSo: decimal        │         │ + Create(): void         │
│ - DiemChu: string        │         │ + GetCauHoi(): List      │
├──────────────────────────┤         │ + Validate(): bool       │
│ + CalculateDiemChu():str │         │ + Export(): string       │
│ + Save(): void           │         └──────────────────────────┘
└────────┬─────────────────┘
         │ *
         │
         │ 1
┌────────▼─────────────────┐
│      SinhVien            │         ┌──────────────────────────┐
├──────────────────────────┤    *    │        LopHoc            │
│ - MaSV: string [PK]      │  ◄──────┤──────────────────────────┤
│ - HoTen: string          │   MaLop │ - MaLop: string [PK]     │
│ - NgaySinh: DateTime     │         │ - TenLop: string         │
│ - GioiTinh: string       │         │ - NamHoc: int            │
│ - MaLop: string [FK]     │         │ - SiSo: int              │
├──────────────────────────┤         ├──────────────────────────┤
│ + GetDiem(): List        │         │ + GetSinhVien(): List    │
│ + GetDiemTB(): decimal   │         └──────────────────────────┘
└──────────────────────────┘


┌──────────────────────────┐         ┌──────────────────────────┐
│    BangDiemChu           │         │        ThamSo            │
├──────────────────────────┤         ├──────────────────────────┤
│ - MaDiem: string [PK]    │         │ - MaThamSo: string [PK]  │
│ - DiemChu: string        │         │ - TenThamSo: string      │
│ - DiemSoMin: decimal     │         │ - GiaTri: string         │
│ - DiemSoMax: decimal     │         │ - MoTa: string           │
├──────────────────────────┤         ├──────────────────────────┤
│ + GetDiemChu(diem): str  │         │ + Get(name): string      │
└──────────────────────────┘         │ + Update(name, val):void │
                                     └──────────────────────────┘


┌──────────────────────────────────────────────────────────────┐
│                    QuanLyDeThiContext : DbContext            │
├──────────────────────────────────────────────────────────────┤
│ + GiangVien: DbSet<GiangVien>                                │
│ + MonHoc: DbSet<MonHoc>                                       │
│ + DoKho: DbSet<DoKho>                                         │
│ + CauHoi: DbSet<CauHoi>                                       │
│ + DeThi: DbSet<DeThi>                                         │
│ + CT_DETHI: DbSet<CT_DETHI>                                   │
│ + LopHoc: DbSet<LopHoc>                                       │
│ + SinhVien: DbSet<SinhVien>                                   │
│ + KetQua: DbSet<KetQua>                                       │
│ + BangDiemChu: DbSet<BangDiemChu>                             │
│ + ThamSo: DbSet<ThamSo>                                       │
├──────────────────────────────────────────────────────────────┤
│ + OnModelCreating(modelBuilder): void                         │
│ + SaveChanges(): int                                          │
│ + ExecuteSqlCommand(sql, params): int                         │
└──────────────────────────────────────────────────────────────┘
```

**Hình 5.1: Biểu đồ lớp tổng quát**

**Quan hệ giữa các lớp:**

| Quan hệ | Mô tả | Multiplicity |
|---------|-------|--------------|
| GiangVien → CauHoi | Một giảng viên soạn nhiều câu hỏi | 1 - * |
| GiangVien → DeThi | Một giảng viên soạn nhiều đề thi | 1 - * |
| MonHoc → CauHoi | Một môn học có nhiều câu hỏi | 1 - * |
| MonHoc → DeThi | Một môn học có nhiều đề thi | 1 - * |
| DoKho → CauHoi | Một độ khó áp dụng cho nhiều câu hỏi | 1 - * |
| DeThi → CT_DETHI | Một đề thi chứa nhiều chi tiết (câu hỏi) | 1 - * |
| CauHoi → CT_DETHI | Một câu hỏi xuất hiện trong nhiều đề thi | * - * (many-to-many qua CT_DETHI) |
| DeThi → KetQua | Một đề thi có nhiều kết quả (từ nhiều SV) | 1 - * |
| SinhVien → KetQua | Một sinh viên có nhiều kết quả (nhiều đề) | 1 - * |
| LopHoc → SinhVien | Một lớp có nhiều sinh viên | 1 - * |

---

## 5.2. Mô tả các lớp chính

### 5.2.1. Lớp GiangVien

**Bảng 5.2: Thuộc tính của lớp GiangVien**

| Thuộc tính | Kiểu dữ liệu | Mô tả | Ràng buộc |
|------------|-------------|-------|-----------|
| MaGV | string | Mã giảng viên (PK) | NOT NULL, UNIQUE, 10 ký tự |
| HoTen | string | Họ và tên | NOT NULL, 5-100 ký tự |
| MatKhau | string | Mật khẩu đã mã hóa SHA256 | NOT NULL, 64 ký tự (hex) |
| Email | string | Email liên hệ | NULL, format email |
| SDT | string | Số điện thoại | NULL, 10-11 số |

**Phương thức:**

```csharp
public class GiangVien
{
    [Key]
    [StringLength(10)]
    public string MaGV { get; set; }
    
    [Required(ErrorMessage = "Họ tên không được trống")]
    [StringLength(100, MinimumLength = 5)]
    public string HoTen { get; set; }
    
    [Required]
    [StringLength(64)]
    public string MatKhau { get; set; }
    
    [EmailAddress]
    public string Email { get; set; }
    
    [Phone]
    public string SDT { get; set; }
    
    // Navigation properties
    public virtual ICollection<CauHoi> DanhSachCauHoi { get; set; }
    public virtual ICollection<DeThi> DanhSachDeThi { get; set; }
    
    // Methods
    public bool Login(string matKhauNhap)
    {
        string hash = ComputeSHA256(matKhauNhap);
        return hash == this.MatKhau;
    }
    
    public void UpdateProfile(string hoTen, string email, string sdt)
    {
        this.HoTen = hoTen;
        this.Email = email;
        this.SDT = sdt;
    }
    
    private string ComputeSHA256(string rawData)
    {
        using (SHA256 sha256Hash = SHA256.Create())
        {
            byte[] bytes = sha256Hash.ComputeHash(Encoding.UTF8.GetBytes(rawData));
            return BitConverter.ToString(bytes).Replace("-", "").ToLower();
        }
    }
}
```

### 5.2.2. Lớp CauHoi

**Bảng 5.3: Thuộc tính của lớp CauHoi**

| Thuộc tính | Kiểu dữ liệu | Mô tả | Ràng buộc |
|------------|-------------|-------|-----------|
| MaCauHoi | string | Mã câu hỏi (PK) | NOT NULL, UNIQUE, auto-gen |
| NoiDung | string | Nội dung câu hỏi | NOT NULL, 10-500 ký tự |
| MaMon | string | Mã môn học (FK) | NOT NULL |
| MaDoKho | string | Mã độ khó (FK) | NOT NULL |
| MaGV | string | Mã giảng viên tạo (FK) | NOT NULL |

**Phương thức:**

```csharp
public class CauHoi
{
    [Key]
    [StringLength(10)]
    public string MaCauHoi { get; set; }
    
    [Required(ErrorMessage = "Nội dung không được trống")]
    [StringLength(500, MinimumLength = 10)]
    public string NoiDung { get; set; }
    
    [Required]
    [StringLength(10)]
    public string MaMon { get; set; }
    
    [Required]
    [StringLength(10)]
    public string MaDoKho { get; set; }
    
    [Required]
    [StringLength(10)]
    public string MaGV { get; set; }
    
    // Navigation properties
    public virtual MonHoc MonHoc { get; set; }
    public virtual DoKho DoKho { get; set; }
    public virtual GiangVien GiangVien { get; set; }
    public virtual ICollection<CT_DETHI> ChiTietDeThi { get; set; }
    
    // Methods
    public void Create(QuanLyDeThiContext db)
    {
        this.MaCauHoi = GenerateMaCauHoi(db);
        db.CauHoi.Add(this);
        db.SaveChanges();
    }
    
    public void Update(QuanLyDeThiContext db, string noiDung, string maMon, string maDoKho)
    {
        this.NoiDung = noiDung;
        this.MaMon = maMon;
        this.MaDoKho = maDoKho;
        db.SaveChanges();
    }
    
    public bool Delete(QuanLyDeThiContext db)
    {
        // Kiểm tra có trong đề thi không
        int count = db.CT_DETHI.Count(ct => ct.MaCauHoi == this.MaCauHoi);
        if (count > 0)
            return false; // Không thể xóa
        
        db.CauHoi.Remove(this);
        db.SaveChanges();
        return true;
    }
    
    public static List<CauHoi> Search(QuanLyDeThiContext db, string keyword, string maGV)
    {
        return db.CauHoi
            .Where(ch => ch.NoiDung.Contains(keyword) && ch.MaGV == maGV)
            .ToList();
    }
    
    private string GenerateMaCauHoi(QuanLyDeThiContext db)
    {
        int count = db.CauHoi.Count();
        return "CH" + (count + 1).ToString("D4"); // CH0001, CH0002...
    }
}
```

### 5.2.3. Lớp DeThi

**Bảng 5.4: Thuộc tính của lớp DeThi**

| Thuộc tính | Kiểu dữ liệu | Mô tả | Ràng buộc |
|------------|-------------|-------|-----------|
| MaDT | string | Mã đề thi (PK) | NOT NULL, UNIQUE, auto-gen |
| TenDT | string | Tên đề thi | NOT NULL, 5-200 ký tự |
| MaMon | string | Mã môn học (FK) | NOT NULL |
| HocKy | int | Học kỳ (1, 2, 3) | NOT NULL, 1-3 |
| Nam | int | Năm học | NOT NULL, 2000-2100 |
| ThoiGian | int | Thời gian làm bài (phút) | NOT NULL, 15-180 |
| NgayTao | DateTime | Ngày tạo đề | NOT NULL, default = NOW() |
| MaGV | string | Mã giảng viên soạn (FK) | NOT NULL |

**Phương thức:**

```csharp
public class DeThi
{
    [Key]
    [StringLength(10)]
    public string MaDT { get; set; }
    
    [Required(ErrorMessage = "Tên đề thi không được trống")]
    [StringLength(200, MinimumLength = 5)]
    public string TenDT { get; set; }
    
    [Required]
    [StringLength(10)]
    public string MaMon { get; set; }
    
    [Required]
    [Range(1, 3, ErrorMessage = "Học kỳ từ 1 đến 3")]
    public int HocKy { get; set; }
    
    [Required]
    [Range(2000, 2100)]
    public int Nam { get; set; }
    
    [Required]
    [Range(15, 180, ErrorMessage = "Thời gian từ 15 đến 180 phút")]
    public int ThoiGian { get; set; }
    
    public DateTime NgayTao { get; set; }
    
    [Required]
    [StringLength(10)]
    public string MaGV { get; set; }
    
    // Navigation properties
    public virtual MonHoc MonHoc { get; set; }
    public virtual GiangVien GiangVien { get; set; }
    public virtual ICollection<CT_DETHI> ChiTietDeThi { get; set; }
    public virtual ICollection<KetQua> DanhSachKetQua { get; set; }
    
    // Methods
    public void Create(QuanLyDeThiContext db, List<CauHoi> danhSachCauHoi, List<decimal> danhSachDiem)
    {
        this.MaDT = GenerateMaDeThi(db);
        this.NgayTao = DateTime.Now;
        
        db.DeThi.Add(this);
        db.SaveChanges();
        
        // Thêm chi tiết đề thi
        for (int i = 0; i < danhSachCauHoi.Count; i++)
        {
            var ct = new CT_DETHI
            {
                MaDT = this.MaDT,
                MaCauHoi = danhSachCauHoi[i].MaCauHoi,
                DiemSo = danhSachDiem[i]
            };
            db.CT_DETHI.Add(ct);
        }
        db.SaveChanges();
    }
    
    public List<CauHoi> GetCauHoi(QuanLyDeThiContext db)
    {
        return db.CT_DETHI
            .Where(ct => ct.MaDT == this.MaDT)
            .Select(ct => ct.CauHoi)
            .ToList();
    }
    
    public bool Validate(QuanLyDeThiContext db, List<decimal> danhSachDiem)
    {
        // Kiểm tra số câu tối thiểu
        var thamSo = db.ThamSo.FirstOrDefault();
        int soCauToiThieu = int.Parse(thamSo.SoCauToiThieu);
        
        if (danhSachDiem.Count < soCauToiThieu)
            return false;
        
        // Kiểm tra tổng điểm = 10
        decimal tongDiem = danhSachDiem.Sum();
        if (tongDiem != 10)
            return false;
        
        return true;
    }
    
    public string Export(QuanLyDeThiContext db)
    {
        StringBuilder sb = new StringBuilder();
        sb.AppendLine($"ĐỀ THI: {this.TenDT}");
        sb.AppendLine($"Môn: {this.MonHoc.TenMon}");
        sb.AppendLine($"Thời gian: {this.ThoiGian} phút");
        sb.AppendLine(new string('-', 50));
        
        var chiTiet = db.CT_DETHI
            .Where(ct => ct.MaDT == this.MaDT)
            .Include(ct => ct.CauHoi)
            .OrderBy(ct => ct.MaCauHoi)
            .ToList();
        
        int stt = 1;
        foreach (var ct in chiTiet)
        {
            sb.AppendLine($"Câu {stt}: {ct.CauHoi.NoiDung} ({ct.DiemSo} điểm)");
            stt++;
        }
        
        return sb.ToString();
    }
    
    private string GenerateMaDeThi(QuanLyDeThiContext db)
    {
        int count = db.DeThi.Count();
        return "DT" + (count + 1).ToString("D4"); // DT0001, DT0002...
    }
}
```

### 5.2.4. Lớp KetQua

**Bảng 5.5: Thuộc tính của lớp KetQua**

| Thuộc tính | Kiểu dữ liệu | Mô tả | Ràng buộc |
|------------|-------------|-------|-----------|
| MaDT | string | Mã đề thi (PK, FK) | NOT NULL |
| MaSV | string | Mã sinh viên (PK, FK) | NOT NULL |
| DiemSo | decimal | Điểm số | NULL, 0-10 |
| DiemChu | string | Điểm chữ (A, B+, B, C+...) | NULL, tính tự động |

**Phương thức:**

```csharp
public class KetQua
{
    [Key, Column(Order = 0)]
    [StringLength(10)]
    public string MaDT { get; set; }
    
    [Key, Column(Order = 1)]
    [StringLength(10)]
    public string MaSV { get; set; }
    
    [Range(0, 10, ErrorMessage = "Điểm từ 0 đến 10")]
    public decimal? DiemSo { get; set; }
    
    [StringLength(5)]
    public string DiemChu { get; set; }
    
    // Navigation properties
    public virtual DeThi DeThi { get; set; }
    public virtual SinhVien SinhVien { get; set; }
    
    // Methods
    public string CalculateDiemChu(QuanLyDeThiContext db)
    {
        if (DiemSo == null)
            return null;
        
        var bangDiem = db.BangDiemChu
            .Where(bd => DiemSo >= bd.DiemSoMin && DiemSo <= bd.DiemSoMax)
            .FirstOrDefault();
        
        return bangDiem?.DiemChu ?? "F";
    }
    
    public void Save(QuanLyDeThiContext db)
    {
        // Tính điểm chữ
        this.DiemChu = CalculateDiemChu(db);
        
        // Kiểm tra đã có kết quả chưa
        var existing = db.KetQua
            .FirstOrDefault(kq => kq.MaDT == this.MaDT && kq.MaSV == this.MaSV);
        
        if (existing == null)
        {
            // Insert
            db.KetQua.Add(this);
        }
        else
        {
            // Update
            existing.DiemSo = this.DiemSo;
            existing.DiemChu = this.DiemChu;
        }
        
        db.SaveChanges();
    }
}
```

---

## 5.3. Biểu đồ Sequence

### 5.3.1. Sequence Diagram - Đăng nhập

```
Giảng viên    Browser    AccountController    GiangVien Model    Database
    |            |              |                    |               |
    | Nhập mã GV |              |                    |               |
    | + mật khẩu |              |                    |               |
    |----------->|              |                    |               |
    |            | POST /login  |                    |               |
    |            |------------->|                    |               |
    |            |              | Query by MaGV      |               |
    |            |              |------------------->|               |
    |            |              |                    | SELECT *      |
    |            |              |                    | FROM GIANG_VIEN
    |            |              |                    | WHERE MaGV=?  |
    |            |              |                    |-------------->|
    |            |              |                    | <result>      |
    |            |              |                    |<--------------|
    |            |              | <GiangVien object> |               |
    |            |              |<-------------------|               |
    |            |              |                    |               |
    |            |              | Login(password)    |               |
    |            |              |------------------->|               |
    |            |              | (kiểm tra hash)    |               |
    |            |              | return true/false  |               |
    |            |              |<-------------------|               |
    |            |              |                    |               |
    |            |   [if valid] |                    |               |
    |            |              | CreateSession()    |               |
    |            |              | Session["MaGV"] = MaGV             |
    |            |              | Session["HoTen"] = HoTen           |
    |            |              |                    |               |
    |            | Redirect "/"  |                    |               |
    |            |<-------------|                    |               |
    | Trang chủ  |              |                    |               |
    |<-----------|              |                    |               |
    |            |              |                    |               |
    |            |   [if invalid]                    |               |
    |            | ViewBag.Error = "Sai mật khẩu"    |               |
    |            | Return View() |                    |               |
    |            |<-------------|                    |               |
    | Hiển thị lỗi              |                    |               |
    |<-----------|              |                    |               |
```

**Hình 5.2: Sequence Diagram - Đăng nhập**

### 5.3.2. Sequence Diagram - Soạn câu hỏi

```
Giảng viên   Browser   CauHoiController   CauHoi Model   MonHoc Model   Database
    |           |              |                |              |            |
    | Click     |              |                |              |            |
    | "Thêm CH" |              |                |              |            |
    |---------->| GET /cauhoi/create           |              |            |
    |           |------------->|                |              |            |
    |           |              | Load MonHoc list              |            |
    |           |              |------------------------------>|            |
    |           |              |                |              | SELECT *   |
    |           |              |                |              | FROM MON_HOC
    |           |              |                |              |----------->|
    |           |              |                |              | <list>     |
    |           |              |                |              |<-----------|
    |           |              | Load DoKho list               |            |
    |           |              |------------------------------>|            |
    |           |              |                |              | SELECT *   |
    |           |              |                |              | FROM DO_KHO|
    |           |              |                |              |----------->|
    |           |              |                |              | <list>     |
    |           |              |                |              |<-----------|
    |           |              | Return View()  |              |            |
    |           | <form>       |                |              |            |
    |           |<-------------|                |              |            |
    | Hiển thị form            |                |              |            |
    |<----------|              |                |              |            |
    |           |              |                |              |            |
    | Điền form |              |                |              |            |
    | Click "Lưu"             |                |              |            |
    |---------->| POST /cauhoi/create          |              |            |
    |           |------------->|                |              |            |
    |           |              | Model Binding  |              |            |
    |           |              | <CauHoi object>|              |            |
    |           |              |                |              |            |
    |           |              | Validate       |              |            |
    |           |              | ModelState     |              |            |
    |           |              |                |              |            |
    |           |   [if valid] |                |              |            |
    |           |              | Create()       |              |            |
    |           |              |--------------->|              |            |
    |           |              |                | GenerateMaCauHoi()        |
    |           |              |                | INSERT INTO CAU_HOI       |
    |           |              |                |----------------------------->
    |           |              |                | <success>    |            |
    |           |              |                |<-----------------------------|
    |           |              | <void>         |              |            |
    |           |              |<---------------|              |            |
    |           |              | RedirectToAction("Index")     |            |
    |           | Redirect /cauhoi/index        |              |            |
    |           |<-------------|                |              |            |
    | Danh sách câu hỏi        |                |              |            |
    |<----------|              |                |              |            |
```

**Hình 5.3: Sequence Diagram - Soạn câu hỏi**

### 5.3.3. Sequence Diagram - Soạn đề thi

```
Giảng viên   Browser   DeThiController   DeThi Model   CauHoi Model   Database
    |           |              |              |             |             |
    | Click     |              |              |             |             |
    | "Soạn đề" |              |              |             |             |
    |---------->| GET /dethi/create          |             |             |
    |           |------------->|              |             |             |
    |           |              | Load MonHoc  |             |             |
    |           |              | Return View()|             |             |
    |           | <form>       |              |             |             |
    |           |<-------------|              |             |             |
    | Nhập thông tin đề thi   |              |             |             |
    |---------->| POST /dethi/create (step 1)|             |             |
    |           |------------->|              |             |             |
    |           |              | Get CauHoi by MaMon        |             |
    |           |              |----------------------------->             |
    |           |              |              |             | SELECT *    |
    |           |              |              |             | WHERE MaMon=?
    |           |              |              |             |------------>|
    |           |              |              |             | <list>      |
    |           |              |              |             |<------------|
    |           |              | Return PartialView(list)   |             |
    |           | <table câu hỏi>            |             |             |
    |           |<-------------|              |             |             |
    | Chọn câu hỏi + nhập điểm|              |             |             |
    | Click "Lưu đề"          |              |             |             |
    |---------->| POST /dethi/create (step 2)|             |             |
    |           |------------->|              |             |             |
    |           |              | Validate()   |             |             |
    |           |              |------------->|             |             |
    |           |              | - Check số câu >= min      |             |
    |           |              | - Check tổng điểm = 10     |             |
    |           |              | return bool  |             |             |
    |           |              |<-------------|             |             |
    |           |   [if valid] |              |             |             |
    |           |              | Create()     |             |             |
    |           |              |------------->|             |             |
    |           |              |              | INSERT INTO DE_THI         |
    |           |              |              |--------------------------->|
    |           |              |              | INSERT INTO CT_DETHI (loop)|
    |           |              |              |--------------------------->|
    |           |              |              | <success>   |             |
    |           |              |              |<---------------------------|
    |           |              | <void>       |             |             |
    |           |              |<-------------|             |             |
    |           |              | RedirectToAction("Details", MaDT)         |
    |           | Redirect /dethi/details/DT0001           |             |
    |           |<-------------|              |             |             |
    | Chi tiết đề thi         |              |             |             |
    |<----------|              |              |             |             |
```

**Hình 5.4: Sequence Diagram - Soạn đề thi**

### 5.3.4. Sequence Diagram - Chấm thi

```
Giảng viên   Browser   KetQuaController   KetQua Model   BangDiemChu   Database
    |           |              |                |             |            |
    | Click     |              |                |             |            |
    | "Chấm thi"|              |                |             |            |
    |---------->| GET /ketqua/nhapdiem        |             |            |
    |           |------------->|                |             |            |
    |           |              | Load DeThi list|             |            |
    |           |              | Load LopHoc list             |            |
    |           |              | Return View()  |             |            |
    |           | <form>       |                |             |            |
    |           |<-------------|                |             |            |
    | Chọn đề + lớp           |                |             |            |
    |---------->| POST /ketqua/nhapdiem?madt=DT0001&malop=SE104.Q23      |
    |           |------------->|                |             |            |
    |           |              | Get SinhVien by MaLop        |            |
    |           |              |---------------------------------------->|
    |           |              |                |             | SELECT *   |
    |           |              |                |             | WHERE MaLop=?
    |           |              |                |             |<-----------|
    |           |              | Get existing KetQua          |            |
    |           |              |---------------------------------------->|
    |           |              |                |             | SELECT *   |
    |           |              |                |             | WHERE MaDT=?
    |           |              |                |             |<-----------|
    |           |              | Return View(viewModel)       |            |
    |           | <table with inputs>          |             |            |
    |           |<-------------|                |             |            |
    | Nhập điểm số            |                |             |            |
    | Click "Lưu điểm"        |                |             |            |
    |---------->| POST /ketqua/nhapdiem (with scores)        |            |
    |           |------------->|                |             |            |
    |           |              | Loop each student:          |            |
    |           |              | - Create KetQua object      |            |
    |           |              | - CalculateDiemChu()        |            |
    |           |              |--------------->|            |            |
    |           |              |                | Query BangDiemChu        |
    |           |              |                |------------------------->|
    |           |              |                | SELECT DiemChu           |
    |           |              |                | WHERE DiemSo BETWEEN ... |
    |           |              |                |<-------------------------|
    |           |              |                | return "B+"             |
    |           |              |<---------------|            |            |
    |           |              | - Save()       |            |            |
    |           |              |--------------->|            |            |
    |           |              |                | INSERT/UPDATE KET_QUA   |
    |           |              |                |------------------------->|
    |           |              |                | <success>  |            |
    |           |              |                |<-------------------------|
    |           |              | RedirectToAction("Index")   |            |
    |           | Redirect /ketqua/index       |            |            |
    |           |<-------------|                |            |            |
    | Thông báo "Lưu thành công"              |            |            |
    |<----------|              |                |            |            |
```

**Hình 5.5: Sequence Diagram - Chấm thi**

### 5.3.5. Sequence Diagram - Báo cáo năm

```
Giảng viên   Browser   BaoCaoController   sp_BaoCaoNam   Database
    |           |              |                |           |
    | Click     |              |                |           |
    | "Báo cáo năm"           |                |           |
    |---------->| GET /baocao/baocaonam         |           |
    |           |------------->|                |           |
    |           |              | Return View()  |           |
    |           | <form>       |                |           |
    |           |<-------------|                |           |
    | Nhập năm: 2026          |                |           |
    | Click "Xem báo cáo"     |                |           |
    |---------->| POST /baocao/baocaonam?nam=2026          |
    |           |------------->|                |           |
    |           |              | ExecuteSqlCommand()        |
    |           |              | EXEC sp_BaoCaoNam @Nam=2026|
    |           |              |------------------------------>
    |           |              |                | Execute SP |
    |           |              |                | SELECT MH.TenMon,
    |           |              |                |   COUNT(*) AS SoLuong
    |           |              |                | FROM DE_THI DT
    |           |              |                | JOIN MON_HOC MH ...
    |           |              |                | WHERE Nam=2026
    |           |              |                | GROUP BY MH.TenMon
    |           |              | <result set>   |           |
    |           |              |<------------------------------|
    |           |              | ViewBag.Data = result       |
    |           |              | Return View()  |           |
    |           | <table + chart>              |           |
    |           |<-------------|                |           |
    | Hiển thị bảng + biểu đồ |                |           |
    |<----------|              |                |           |
    |           |              |                |           |
    | Click "Xuất CSV"        |                |           |
    |---------->| GET /baocao/exportcsv?nam=2026           |
    |           |------------->|                |           |
    |           |              | (Same query as above)      |
    |           |              |------------------------------>
    |           |              | <result set>   |           |
    |           |              |<------------------------------|
    |           |              | GenerateCSV()  |           |
    |           |              | - Add UTF-8 BOM             |
    |           |              | - Write header              |
    |           |              | - Write rows   |           |
    |           | File Download: BaoCao_Nam2026.csv        |
    |           |<-------------|                |           |
    | Save file |              |                |           |
    |<----------|              |                |           |
```

**Hình 5.6: Sequence Diagram - Báo cáo năm**

---

**Kết luận chương 5**: Chương này đã thiết kế chi tiết các lớp đối tượng với đầy đủ thuộc tính, phương thức, và mối quan hệ giữa chúng. Biểu đồ Sequence minh họa rõ ràng luồng tương tác giữa các đối tượng trong 5 Use Case quan trọng nhất. Chương tiếp theo sẽ thiết kế cơ sở dữ liệu (ERD, từ điển dữ liệu, stored procedures).

