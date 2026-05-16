# CHƯƠNG 4: THIẾT KẾ HỆ THỐNG

## 4.1. Kiến trúc hệ thống

### 4.1.1. Mô hình 3 lớp (3-Tier Architecture)

Hệ thống được thiết kế theo kiến trúc 3 lớp để đảm bảo tính module hóa, dễ bảo trì và mở rộng:

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                        │
│                      (Lớp trình diễn)                        │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Razor Views │  │   Bootstrap  │  │    jQuery    │      │
│  │              │  │      CSS     │  │  JavaScript  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
│  - Hiển thị giao diện người dùng                            │
│  - Nhận input từ giảng viên                                 │
│  - Validation phía client                                   │
│  - Render dữ liệu từ Controller                             │
└───────────────────────────┬──────────────────────────────────┘
                            │ HTTP Request/Response
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   BUSINESS LOGIC LAYER                       │
│                    (Lớp xử lý nghiệp vụ)                     │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              ASP.NET MVC Controllers                  │   │
│  │                                                       │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │   │
│  │  │   Account   │  │   CauHoi    │  │   DeThi     │  │   │
│  │  │ Controller  │  │ Controller  │  │ Controller  │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │   │
│  │                                                       │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │   │
│  │  │  KetQua     │  │   BaoCao    │  │  ThamSo     │  │   │
│  │  │ Controller  │  │ Controller  │  │ Controller  │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  - Xử lý logic nghiệp vụ                                    │
│  - Validation phía server                                   │
│  - Kiểm tra quyền truy cập (session)                        │
│  - Gọi Model để truy xuất dữ liệu                           │
│  - Trả kết quả về View                                      │
└───────────────────────────┬──────────────────────────────────┘
                            │ LINQ / Entity Framework
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                     DATA ACCESS LAYER                        │
│                   (Lớp truy xuất dữ liệu)                   │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           Entity Framework 6 (ORM)                   │   │
│  │                                                       │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐           │   │
│  │  │ GiangVien│  │  CauHoi  │  │  DeThi   │  Models   │   │
│  │  │   .cs    │  │   .cs    │  │   .cs    │           │   │
│  │  └──────────┘  └──────────┘  └──────────┘           │   │
│  │                                                       │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐           │   │
│  │  │  KetQua  │  │  MonHoc  │  │ ThamSo   │           │   │
│  │  │   .cs    │  │   .cs    │  │   .cs    │           │   │
│  │  └──────────┘  └──────────┘  └──────────┘           │   │
│  │                                                       │   │
│  │              DbContext (QuanLyDeThiContext)          │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  - Mapping giữa Object và Database                          │
│  - Thực thi query LINQ                                      │
│  - Connection pooling                                       │
│  - Transaction management                                   │
└───────────────────────────┬──────────────────────────────────┘
                            │ SQL Query
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      DATABASE LAYER                          │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                 SQL Server 2019                       │   │
│  │                                                       │   │
│  │  11 Tables:                                           │   │
│  │  - GIANG_VIEN      - CAU_HOI       - DE_THI          │   │
│  │  - MON_HOC         - DO_KHO        - CT_DETHI        │   │
│  │  - LOP_HOC         - SINH_VIEN     - KET_QUA         │   │
│  │  - BANG_DIEM_CHU   - THAM_SO                         │   │
│  │                                                       │   │
│  │  4 Stored Procedures:                                │   │
│  │  - sp_BaoCaoNam                                       │   │
│  │  - sp_TraCuuDeThi                                     │   │
│  │  - sp_GetDiemChu                                      │   │
│  │  - sp_ThongKeCauHoi                                   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  - Lưu trữ dữ liệu                                          │
│  - Enforcing constraints (PK, FK, CHECK)                    │
│  - Indexing để tăng tốc query                               │
│  - Backup & recovery                                        │
└──────────────────────────────────────────────────────────────┘
```

**Hình 4.1: Kiến trúc 3 lớp của hệ thống**

**Bảng 4.1: Mô tả các lớp trong kiến trúc 3 lớp**

| Lớp | Công nghệ | Trách nhiệm | Ưu điểm |
|-----|-----------|-------------|---------|
| **Presentation** | Razor, HTML, CSS, JS | Hiển thị UI, nhận input | Dễ thay đổi giao diện mà không ảnh hưởng logic |
| **Business Logic** | ASP.NET MVC Controllers | Xử lý nghiệp vụ, validation | Tập trung logic, dễ test |
| **Data Access** | Entity Framework 6 | Truy xuất CSDL, ORM | Giảm code SQL thủ công, tránh SQL injection |
| **Database** | SQL Server 2019 | Lưu trữ dữ liệu | ACID, transaction, backup |

### 4.1.2. Mô hình MVC (Model-View-Controller)

Trong lớp Business Logic, hệ thống áp dụng mô hình MVC:

```
┌────────────────────────────────────────────────────────────┐
│                         Browser                             │
│                     (Giảng viên)                            │
└──────────────────────┬─────────────────────────────────────┘
                       │ HTTP Request: /cauhoi/create
                       ▼
┌────────────────────────────────────────────────────────────┐
│                        ROUTING                              │
│              (App_Start/RouteConfig.cs)                     │
│                                                             │
│  routes.MapRoute(                                           │
│      name: "Default",                                       │
│      url: "{controller}/{action}/{id}"                      │
│  );                                                         │
└──────────────────────┬─────────────────────────────────────┘
                       │ Route to CauHoiController.Create()
                       ▼
┌────────────────────────────────────────────────────────────┐
│                      CONTROLLER                             │
│              (Controllers/CauHoiController.cs)              │
│                                                             │
│  public class CauHoiController : Controller                │
│  {                                                          │
│      private QuanLyDeThiContext db = new ...();            │
│                                                             │
│      // GET: /cauhoi/create                                │
│      public ActionResult Create()                          │
│      {                                                      │
│          ViewBag.DanhSachMonHoc = db.MonHoc.ToList();      │
│          ViewBag.DanhSachDoKho = db.DoKho.ToList();        │
│          return View();  ─────────────────┐                │
│      }                                     │                │
│                                            │                │
│      // POST: /cauhoi/create               │                │
│      [HttpPost]                            │                │
│      public ActionResult Create(CauHoi model) ◀────┐       │
│      {                                     │        │       │
│          if (ModelState.IsValid)           │        │       │
│          {                                 │        │       │
│              model.MaGV = Session["MaGV"]; │        │       │
│              db.CauHoi.Add(model); ────────┼────────┼───┐   │
│              db.SaveChanges();             │        │   │   │
│              return RedirectToAction("Index");      │   │   │
│          }                                 │        │   │   │
│          return View(model);               │        │   │   │
│      }                                     │        │   │   │
│  }                                         │        │   │   │
└────────────────────────────────────────────┼────────┼───┼───┘
                                             │        │   │
                       ┌─────────────────────┘        │   │
                       │                              │   │
                       ▼                              │   │
┌────────────────────────────────────────────────────┼───┼───┐
│                        VIEW                         │   │   │
│              (Views/CauHoi/Create.cshtml)           │   │   │
│                                                     │   │   │
│  @model QuanLyRaDeChamThi.Models.CauHoi             │   │   │
│                                                     │   │   │
│  @using (Html.BeginForm())                          │   │   │
│  {                                                  │   │   │
│      @Html.LabelFor(m => m.NoiDung)                 │   │   │
│      @Html.TextAreaFor(m => m.NoiDung)              │   │   │
│                                                     │   │   │
│      @Html.LabelFor(m => m.MaMon)                   │   │   │
│      @Html.DropDownListFor(m => m.MaMon,            │   │   │
│          new SelectList(ViewBag.DanhSachMonHoc))    │   │   │
│                                                     │   │   │
│      <button type="submit">Lưu</button> ────────────┼───┘   │
│  }                                                  │       │
└─────────────────────────────────────────────────────┼───────┘
                                                      │
                       ┌──────────────────────────────┘
                       │
                       ▼
┌────────────────────────────────────────────────────────────┐
│                        MODEL                                │
│               (Models/CauHoi.cs)                            │
│                                                             │
│  public class CauHoi                                        │
│  {                                                          │
│      [Key]                                                  │
│      public string MaCauHoi { get; set; }                   │
│                                                             │
│      [Required(ErrorMessage = "Nội dung không được trống")] │
│      [StringLength(500, MinimumLength = 10)]                │
│      public string NoiDung { get; set; }                    │
│                                                             │
│      [Required]                                             │
│      public string MaMon { get; set; }                      │
│                                                             │
│      [Required]                                             │
│      public string MaDoKho { get; set; }                    │
│                                                             │
│      public string MaGV { get; set; }                       │
│                                                             │
│      // Navigation properties                               │
│      public virtual MonHoc MonHoc { get; set; }             │
│      public virtual DoKho DoKho { get; set; }               │
│      public virtual GiangVien GiangVien { get; set; }       │
│  }                                                          │
│                                                             │
│  // DbContext                                               │
│  public class QuanLyDeThiContext : DbContext                │
│  {                                                          │
│      public DbSet<CauHoi> CauHoi { get; set; }              │
│      public DbSet<MonHoc> MonHoc { get; set; }              │
│      // ... other DbSets                                    │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
```

**Hình 4.2: Mô hình MVC trong ASP.NET**

**Giải thích luồng xử lý:**

1. **User request**: Giảng viên click "Thêm câu hỏi" → Browser gửi GET /cauhoi/create
2. **Routing**: RouteConfig map URL → CauHoiController.Create()
3. **Controller xử lý GET**: 
   - Load danh sách môn học, độ khó từ database
   - Gán vào ViewBag
   - Return View() → Render Create.cshtml
4. **View hiển thị**: Form với dropdown môn học, độ khó, textarea nội dung
5. **User submit**: Giảng viên điền form → Click "Lưu" → POST /cauhoi/create
6. **Controller xử lý POST**:
   - Model binding: Map form data → CauHoi object
   - Validation: Kiểm tra ModelState.IsValid
   - Nếu hợp lệ: Add vào database, SaveChanges()
   - Redirect về trang danh sách
7. **Model**: Entity Framework map CauHoi object → SQL INSERT command

---

## 4.2. Biểu đồ Component

Component Diagram mô tả các thành phần chính của hệ thống và quan hệ giữa chúng:

```
┌─────────────────────────────────────────────────────────────────┐
│                        Web Browser                               │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   HTML/CSS   │  │  JavaScript  │  │   jQuery     │          │
│  │   Bootstrap  │  │   Vanilla    │  │   AJAX       │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/HTTPS
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                         IIS Web Server                           │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              ASP.NET MVC Application                       │  │
│  │                                                            │  │
│  │  ┌────────────────────────────────────────────────────┐   │  │
│  │  │           Authentication Module                     │   │  │
│  │  │   - Session Management                              │   │  │
│  │  │   - Authorization Filter                            │   │  │
│  │  └────────────────────────────────────────────────────┘   │  │
│  │                                                            │  │
│  │  ┌────────────────┐  ┌────────────────┐                   │  │
│  │  │   Account      │  │   CauHoi       │                   │  │
│  │  │   Controller   │  │   Controller   │                   │  │
│  │  │                │  │                │                   │  │
│  │  │  + Login()     │  │  + Index()     │                   │  │
│  │  │  + Logout()    │  │  + Create()    │                   │  │
│  │  └────────────────┘  │  + Edit()      │                   │  │
│  │                      │  + Delete()    │                   │  │
│  │  ┌────────────────┐  └────────────────┘                   │  │
│  │  │   DeThi        │                                       │  │
│  │  │   Controller   │  ┌────────────────┐                   │  │
│  │  │                │  │   KetQua       │                   │  │
│  │  │  + Index()     │  │   Controller   │                   │  │
│  │  │  + Create()    │  │                │                   │  │
│  │  │  + TraCuu()    │  │  + Index()     │                   │  │
│  │  └────────────────┘  │  + NhapDiem()  │                   │  │
│  │                      └────────────────┘                   │  │
│  │  ┌────────────────┐                                       │  │
│  │  │   BaoCao       │  ┌────────────────┐                   │  │
│  │  │   Controller   │  │   ThamSo       │                   │  │
│  │  │                │  │   Controller   │                   │  │
│  │  │  + BaoCaoNam() │  │                │                   │  │
│  │  │  + ExportCSV() │  │  + Index()     │                   │  │
│  │  └────────────────┘  │  + Edit()      │                   │  │
│  │                      └────────────────┘                   │  │
│  │                                                            │  │
│  │  ┌──────────────────────────────────────────────────────┐ │  │
│  │  │              Entity Framework 6                       │ │  │
│  │  │                                                       │ │  │
│  │  │  - DbContext (QuanLyDeThiContext)                    │ │  │
│  │  │  - DbSet<T> for each entity                          │ │  │
│  │  │  - LINQ to Entities                                  │ │  │
│  │  │  - Change Tracking                                   │ │  │
│  │  │  - Migration                                         │ │  │
│  │  └───────────────────┬───────────────────────────────────┘ │  │
│  └────────────────────────┼─────────────────────────────────┘  │
└────────────────────────────┼─────────────────────────────────────┘
                             │ ADO.NET
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SQL Server 2019                             │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │  Tables          │  │  Stored Procs    │                     │
│  │                  │  │                  │                     │
│  │  - GIANG_VIEN    │  │  - sp_BaoCaoNam  │                     │
│  │  - MON_HOC       │  │  - sp_TraCuuDeThi│                     │
│  │  - DO_KHO        │  │  - sp_GetDiemChu │                     │
│  │  - CAU_HOI       │  │                  │                     │
│  │  - DE_THI        │  └──────────────────┘                     │
│  │  - CT_DETHI      │                                           │
│  │  - LOP_HOC       │  ┌──────────────────┐                     │
│  │  - SINH_VIEN     │  │  Indexes         │                     │
│  │  - KET_QUA       │  │                  │                     │
│  │  - BANG_DIEM_CHU │  │  - IX_MaMon      │                     │
│  │  - THAM_SO       │  │  - IX_MaDoKho    │                     │
│  └──────────────────┘  │  - IX_MaGV       │                     │
│                        │  - IX_MaDT       │                     │
│                        │  - IX_MaSV       │                     │
│                        └──────────────────┘                     │
└──────────────────────────────────────────────────────────────────┘
```

**Hình 4.3: Biểu đồ Component**

**Bảng 4.2: Phân tích các Component**

| Component | Chức năng | Interface cung cấp | Dependency |
|-----------|-----------|-------------------|------------|
| **AccountController** | Xác thực người dùng | Login(), Logout() | GiangVien Model, Session |
| **CauHoiController** | Quản lý câu hỏi | Index(), Create(), Edit(), Delete() | CauHoi, MonHoc, DoKho Models |
| **DeThiController** | Quản lý đề thi | Index(), Create(), TraCuu() | DeThi, CauHoi, CT_DETHI Models |
| **KetQuaController** | Chấm điểm | Index(), NhapDiem() | KetQua, SinhVien, DeThi Models |
| **BaoCaoController** | Thống kê báo cáo | BaoCaoNam(), ExportCSV() | sp_BaoCaoNam, CauHoi Model |
| **ThamSoController** | Quản lý tham số | Index(), Edit() | ThamSo Model |
| **Entity Framework** | ORM | DbContext, DbSet<T>, LINQ | ADO.NET, SQL Server |
| **SQL Server** | Database | Tables, Stored Procedures, Indexes | - |

---

## 4.3. Biểu đồ Deployment

Deployment Diagram mô tả cách triển khai hệ thống trên các node vật lý:

```
┌─────────────────────────────────────────────────────────────────┐
│                      Client Workstation                          │
│                                                                  │
│  OS: Windows 10/11                                               │
│  Browser: Chrome 120+ / Edge 120+ / Firefox 120+                │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │              Web Browser                                │     │
│  │                                                         │     │
│  │  - Render HTML/CSS                                      │     │
│  │  - Execute JavaScript                                   │     │
│  │  - Send HTTP requests                                   │     │
│  │  - Store session cookies                                │     │
│  └────────────────────────────────────────────────────────┘     │
└────────────────────────┬────────────────────────────────────────┘
                         │ HTTP/HTTPS (Port 80/443)
                         │ LAN/WAN
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Application Server                          │
│                                                                  │
│  OS: Windows Server 2019/2022                                    │
│  IP: 192.168.1.100 (Internal)                                   │
│  RAM: 8GB, CPU: 4 cores                                          │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │              IIS 10.0 Web Server                        │     │
│  │                                                         │     │
│  │  - Application Pool (.NET Framework 4.6.1)              │     │
│  │  - Site: QuanLyRaDeChamThi                              │     │
│  │  - Binding: http://localhost:8080                       │     │
│  │  - Authentication: Anonymous + Windows Auth             │     │
│  └────────────────────────────────────────────────────────┘     │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │         ASP.NET MVC Application                         │     │
│  │                                                         │     │
│  │  Files:                                                 │     │
│  │  - /bin/*.dll (compiled assemblies)                     │     │
│  │  - /Views/*.cshtml (Razor views)                        │     │
│  │  - /Content/*.css (stylesheets)                         │     │
│  │  - /Scripts/*.js (JavaScript files)                     │     │
│  │  - /Web.config (configuration)                          │     │
│  └────────────────────────────────────────────────────────┘     │
└────────────────────────┬────────────────────────────────────────┘
                         │ ADO.NET (Port 1433)
                         │ TCP/IP
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Database Server                             │
│                                                                  │
│  OS: Windows Server 2019/2022                                    │
│  IP: 192.168.1.101 (Internal)                                   │
│  RAM: 16GB, CPU: 8 cores, SSD: 500GB                            │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │           SQL Server 2019 Express                       │     │
│  │                                                         │     │
│  │  Database: QuanLyRaDeChamThi                            │     │
│  │  - 11 Tables                                            │     │
│  │  - 4 Stored Procedures                                  │     │
│  │  - 5 Indexes                                            │     │
│  │  - Full-text search enabled                             │     │
│  │                                                         │     │
│  │  Security:                                              │     │
│  │  - SQL Server Authentication                            │     │
│  │  - User: sa / Password: ********                        │     │
│  │  - Firewall: Port 1433 open to App Server only         │     │
│  └────────────────────────────────────────────────────────┘     │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │           SQL Server Agent                              │     │
│  │                                                         │     │
│  │  Jobs:                                                  │     │
│  │  - Daily backup (2:00 AM)                               │     │
│  │  - Weekly maintenance (Sunday 3:00 AM)                  │     │
│  │  - Cleanup old logs (monthly)                           │     │
│  └────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      Backup Server (Optional)                    │
│                                                                  │
│  OS: Windows Server 2019                                         │
│  IP: 192.168.1.102 (Internal)                                   │
│  Storage: 2TB HDD                                                │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐     │
│  │           File Storage                                  │     │
│  │                                                         │     │
│  │  - Database backups (.bak files)                        │     │
│  │  - Log files                                            │     │
│  │  - Retention: 30 days                                   │     │
│  └────────────────────────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘
```

**Hình 4.4: Biểu đồ Deployment**

**Cấu hình triển khai:**

### 4.3.1. Môi trường Development (Dev)

- **Máy tính dev**: Windows 11, Visual Studio 2022
- **IIS Express**: localhost:44300
- **SQL Server LocalDB**: (localdb)\MSSQLLocalDB
- **Mục đích**: Phát triển và test cục bộ

### 4.3.2. Môi trường Testing (Test)

- **App Server**: Windows Server 2019, IIS 10.0, 4GB RAM
- **DB Server**: SQL Server 2019 Express, 8GB RAM
- **Mục đích**: Kiểm thử tích hợp, UAT

### 4.3.3. Môi trường Production (Prod)

- **App Server**: Windows Server 2022, IIS 10.0, 8GB RAM, 4 cores
- **DB Server**: SQL Server 2019 Standard, 16GB RAM, 8 cores, SSD
- **Load Balancer**: Không cần (quy mô nhỏ)
- **Backup**: Backup hàng ngày lúc 2:00 AM, lưu 30 ngày

---

## 4.4. Thiết kế gói (Package Diagram)

Package Diagram mô tả cách tổ chức code thành các gói (namespace):

```
┌─────────────────────────────────────────────────────────────────┐
│              QuanLyRaDeChamThi (Root Namespace)                  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    Controllers                            │   │
│  │                                                           │   │
│  │  - AccountController.cs                                   │   │
│  │  - HomeController.cs                                      │   │
│  │  - CauHoiController.cs                                    │   │
│  │  - DeThiController.cs                                     │   │
│  │  - KetQuaController.cs                                    │   │
│  │  - BaoCaoController.cs                                    │   │
│  │  - ThamSoController.cs                                    │   │
│  │                                                           │   │
│  │  <<uses>>                                                 │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   │                                              │
│  ┌────────────────▼─────────────────────────────────────────┐   │
│  │                       Models                              │   │
│  │                                                           │   │
│  │  Entities:                                                │   │
│  │  - GiangVien.cs                                           │   │
│  │  - MonHoc.cs                                              │   │
│  │  - DoKho.cs                                               │   │
│  │  - CauHoi.cs                                              │   │
│  │  - DeThi.cs                                               │   │
│  │  - CT_DETHI.cs                                            │   │
│  │  - LopHoc.cs                                              │   │
│  │  - SinhVien.cs                                            │   │
│  │  - KetQua.cs                                              │   │
│  │  - BangDiemChu.cs                                         │   │
│  │  - ThamSo.cs                                              │   │
│  │                                                           │   │
│  │  ViewModels:                                              │   │
│  │  - LoginViewModel.cs                                      │   │
│  │  - SoanDeThiViewModel.cs                                  │   │
│  │  - NhapDiemViewModel.cs                                   │   │
│  │  - BaoCaoNamViewModel.cs                                  │   │
│  │                                                           │   │
│  │  DbContext:                                               │   │
│  │  - QuanLyDeThiContext.cs                                  │   │
│  │                                                           │   │
│  │  <<uses>>                                                 │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   │                                              │
│  ┌────────────────▼─────────────────────────────────────────┐   │
│  │                       Views                               │   │
│  │                                                           │   │
│  │  Shared/                                                  │   │
│  │  - _Layout.cshtml                                         │   │
│  │  - _LoginPartial.cshtml                                   │   │
│  │                                                           │   │
│  │  Account/                                                 │   │
│  │  - Login.cshtml                                           │   │
│  │                                                           │   │
│  │  Home/                                                    │   │
│  │  - Index.cshtml                                           │   │
│  │                                                           │   │
│  │  CauHoi/                                                  │   │
│  │  - Index.cshtml                                           │   │
│  │  - Create.cshtml                                          │   │
│  │  - Edit.cshtml                                            │   │
│  │  - Delete.cshtml                                          │   │
│  │                                                           │   │
│  │  DeThi/                                                   │   │
│  │  - Index.cshtml                                           │   │
│  │  - Create.cshtml                                          │   │
│  │  - Details.cshtml                                         │   │
│  │  - TraCuu.cshtml                                          │   │
│  │                                                           │   │
│  │  KetQua/                                                  │   │
│  │  - Index.cshtml                                           │   │
│  │  - NhapDiem.cshtml                                        │   │
│  │                                                           │   │
│  │  BaoCao/                                                  │   │
│  │  - BaoCaoNam.cshtml                                       │   │
│  │                                                           │   │
│  │  ThamSo/                                                  │   │
│  │  - Index.cshtml                                           │   │
│  │  - Edit.cshtml                                            │   │
│  │                                                           │   │
│  │  <<renders>>                                              │   │
│  └────────────────┬─────────────────────────────────────────┘   │
│                   │                                              │
│                   │                                              │
│  ┌────────────────▼─────────────────────────────────────────┐   │
│  │                    App_Start                              │   │
│  │                                                           │   │
│  │  - RouteConfig.cs  (URL routing)                          │   │
│  │  - FilterConfig.cs  (Global filters)                      │   │
│  │  - BundleConfig.cs  (CSS/JS bundling)                     │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                     Content                               │   │
│  │                                                           │   │
│  │  - bootstrap.css                                          │   │
│  │  - Site.css (custom styles)                               │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                     Scripts                               │   │
│  │                                                           │   │
│  │  - jquery-1.10.2.js                                       │   │
│  │  - bootstrap.js                                           │   │
│  │  - site.js (custom JS)                                    │   │
│  └───────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

**Hình 4.5: Package Diagram**

**Dependency giữa các gói:**
- Controllers → Models (sử dụng entities, ViewModels, DbContext)
- Controllers → Views (render views với data)
- Views → Models (binding với ViewModels)
- Models.DbContext → SQL Server (EF mapping)

---

**Kết luận chương 4**: Chương này đã trình bày thiết kế kiến trúc hệ thống theo mô hình 3 lớp, áp dụng MVC pattern, Component Diagram, Deployment Diagram và Package Diagram. Thiết kế này đảm bảo tính module hóa, dễ bảo trì và mở rộng. Chương tiếp theo sẽ thiết kế chi tiết các đối tượng (Class Diagram, Sequence Diagram).

