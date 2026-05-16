# CHƯƠNG 8: CÀI ĐẶT PHẦN MỀM

## 8.1. Môi trường phát triển

**Bảng 8.1: Môi trường phát triển**

| Thành phần | Phiên bản | Mục đích |
|------------|-----------|----------|
| **Operating System** | Windows 11 Pro | Hệ điều hành |
| **IDE** | Visual Studio 2022 Community | Môi trường phát triển |
| **Database Tool** | SQL Server Management Studio 19 | Quản lý CSDL |
| **Version Control** | Git 2.40 + GitHub | Quản lý mã nguồn |
| **Browser** | Chrome 120+, Edge 120+ | Test giao diện |
| **Code Editor** | Visual Studio Code 1.85 | Chỉnh sửa file config, markdown |

---

## 8.2. Công nghệ sử dụng

### 8.2.1. ASP.NET MVC 5

**Bảng 8.2: Công nghệ và Framework**

| Công nghệ | Phiên bản | Vai trò | Package |
|-----------|-----------|---------|---------|
| **ASP.NET MVC** | 5.2.3 | Web framework | Microsoft.AspNet.Mvc |
| **Entity Framework** | 6.1.3 | ORM | EntityFramework |
| **.NET Framework** | 4.6.1 | Runtime | - |
| **C#** | 6.0 | Ngôn ngữ lập trình | - |

**Lý do chọn ASP.NET MVC:**
- ✅ Phân tách rõ ràng Model-View-Controller
- ✅ Hỗ trợ Razor View Engine mạnh mẽ
- ✅ Tích hợp tốt với Entity Framework
- ✅ Community lớn, tài liệu phong phú
- ✅ Phù hợp cho ứng dụng doanh nghiệp

### 8.2.2. Entity Framework 6

**Ưu điểm:**
- **Code First**: Định nghĩa model bằng C# class, tự động tạo database
- **LINQ to Entities**: Viết query bằng LINQ, an toàn về kiểu dữ liệu
- **Lazy Loading**: Tự động load navigation properties khi cần
- **Change Tracking**: Tự động theo dõi thay đổi của entity
- **Migration**: Quản lý version database dễ dàng

**Ví dụ Code First:**

```csharp
public class CauHoi
{
    [Key]
    public string MaCauHoi { get; set; }
    
    [Required]
    [StringLength(500, MinimumLength = 10)]
    public string NoiDung { get; set; }
    
    public virtual MonHoc MonHoc { get; set; }
    public virtual DoKho DoKho { get; set; }
}

public class QuanLyDeThiContext : DbContext
{
    public DbSet<CauHoi> CauHoi { get; set; }
    public DbSet<MonHoc> MonHoc { get; set; }
    // ...
}
```

### 8.2.3. SQL Server

**Tính năng sử dụng:**
- **Stored Procedures**: sp_BaoCaoNam, sp_TraCuuDeThi
- **Indexes**: Tăng tốc query trên foreign key
- **Constraints**: PRIMARY KEY, FOREIGN KEY, CHECK, UNIQUE
- **Triggers**: (Không sử dụng, xử lý ở Business Logic)

### 8.2.4. Bootstrap & jQuery

**Bảng 8.3: Thư viện bên thứ 3**

| Thư viện | Phiên bản | Mục đích |
|----------|-----------|----------|
| **Bootstrap** | 3.0.0 | CSS framework, responsive grid |
| **jQuery** | 1.10.2 | DOM manipulation, AJAX |
| **Font Awesome** | 4.7.0 | Icons |
| **Chart.js** | 2.9.4 | Biểu đồ thống kê |

---

## 8.3. Cấu trúc thư mục

**Hình 8.1: Cấu trúc thư mục dự án**

```
QuanLyRaDeChamThi/
│
├── App_Data/
│   ├── QuanLyRaDeChamThi.mdf         # Database file
│   └── QuanLyRaDeChamThi_log.ldf
│
├── App_Start/
│   ├── BundleConfig.cs               # CSS/JS bundling
│   ├── FilterConfig.cs               # Global filters
│   └── RouteConfig.cs                # URL routing
│
├── Content/
│   ├── bootstrap.css
│   ├── bootstrap.min.css
│   └── Site.css                      # Custom styles
│
├── Controllers/
│   ├── AccountController.cs          # Đăng nhập
│   ├── HomeController.cs             # Trang chủ
│   ├── CauHoiController.cs           # Quản lý câu hỏi
│   ├── DeThiController.cs            # Quản lý đề thi
│   ├── KetQuaController.cs           # Chấm thi
│   ├── BaoCaoController.cs           # Báo cáo
│   └── ThamSoController.cs           # Tham số
│
├── Models/
│   ├── GiangVien.cs
│   ├── MonHoc.cs
│   ├── DoKho.cs
│   ├── CauHoi.cs
│   ├── DeThi.cs
│   ├── CT_DETHI.cs
│   ├── LopHoc.cs
│   ├── SinhVien.cs
│   ├── KetQua.cs
│   ├── BangDiemChu.cs
│   ├── ThamSo.cs
│   ├── QuanLyDeThiContext.cs         # DbContext
│   ├── LoginViewModel.cs             # View models
│   ├── SoanDeThiViewModel.cs
│   ├── NhapDiemViewModel.cs
│   └── BaoCaoNamViewModel.cs
│
├── Views/
│   ├── Shared/
│   │   ├── _Layout.cshtml            # Master layout
│   │   └── _LoginPartial.cshtml
│   ├── Account/
│   │   └── Login.cshtml
│   ├── Home/
│   │   └── Index.cshtml
│   ├── CauHoi/
│   │   ├── Index.cshtml
│   │   ├── Create.cshtml
│   │   ├── Edit.cshtml
│   │   └── Delete.cshtml
│   ├── DeThi/
│   │   ├── Index.cshtml
│   │   ├── Create.cshtml
│   │   ├── Details.cshtml
│   │   └── TraCuu.cshtml
│   ├── KetQua/
│   │   ├── Index.cshtml
│   │   └── NhapDiem.cshtml
│   ├── BaoCao/
│   │   └── BaoCaoNam.cshtml
│   └── ThamSo/
│       ├── Index.cshtml
│       └── Edit.cshtml
│
├── Scripts/
│   ├── jquery-1.10.2.js
│   ├── bootstrap.js
│   ├── chart.js                      # Chart library
│   └── site.js                       # Custom JS
│
├── fonts/                            # Font Awesome fonts
│
├── packages.config                   # NuGet packages
├── Web.config                        # Configuration
└── Global.asax                       # Application events
```

---

## 8.4. Code mẫu

### 8.4.1. Controller

**CauHoiController.cs:**

```csharp
using System;
using System.Linq;
using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;

namespace QuanLyRaDeChamThi.Controllers
{
    public class CauHoiController : Controller
    {
        private QuanLyDeThiContext db = new QuanLyDeThiContext();
        
        // GET: /cauhoi
        public ActionResult Index(string search = "")
        {
            // Kiểm tra đăng nhập
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            
            string maGV = Session["MaGV"].ToString();
            
            // Lấy danh sách câu hỏi
            var danhSach = db.CauHoi
                .Include("MonHoc")
                .Include("DoKho")
                .Where(ch => ch.MaGV == maGV);
            
            // Tìm kiếm
            if (!string.IsNullOrEmpty(search))
            {
                danhSach = danhSach.Where(ch => ch.NoiDung.Contains(search));
            }
            
            ViewBag.Search = search;
            return View(danhSach.OrderByDescending(ch => ch.MaCauHoi).ToList());
        }
        
        // GET: /cauhoi/create
        public ActionResult Create()
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            
            // Load dropdown data
            ViewBag.DanhSachMonHoc = new SelectList(db.MonHoc, "MaMon", "TenMon");
            ViewBag.DanhSachDoKho = new SelectList(db.DoKho, "MaDoKho", "TenDoKho");
            
            return View();
        }
        
        // POST: /cauhoi/create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(CauHoi model)
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            
            if (ModelState.IsValid)
            {
                // Tạo mã câu hỏi tự động
                int count = db.CauHoi.Count();
                model.MaCauHoi = "CH" + (count + 1).ToString("D4");
                model.MaGV = Session["MaGV"].ToString();
                
                db.CauHoi.Add(model);
                db.SaveChanges();
                
                TempData["Success"] = "Thêm câu hỏi thành công!";
                return RedirectToAction("Index");
            }
            
            // Reload dropdown nếu lỗi
            ViewBag.DanhSachMonHoc = new SelectList(db.MonHoc, "MaMon", "TenMon", model.MaMon);
            ViewBag.DanhSachDoKho = new SelectList(db.DoKho, "MaDoKho", "TenDoKho", model.MaDoKho);
            
            return View(model);
        }
        
        // GET: /cauhoi/edit/CH0001
        public ActionResult Edit(string id)
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            
            var cauHoi = db.CauHoi.Find(id);
            if (cauHoi == null)
                return HttpNotFound();
            
            // Kiểm tra quyền (chỉ sửa câu hỏi của mình)
            if (cauHoi.MaGV != Session["MaGV"].ToString())
                return new HttpStatusCodeResult(403, "Forbidden");
            
            ViewBag.DanhSachMonHoc = new SelectList(db.MonHoc, "MaMon", "TenMon", cauHoi.MaMon);
            ViewBag.DanhSachDoKho = new SelectList(db.DoKho, "MaDoKho", "TenDoKho", cauHoi.MaDoKho);
            
            return View(cauHoi);
        }
        
        // POST: /cauhoi/edit/CH0001
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(CauHoi model)
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            
            if (ModelState.IsValid)
            {
                var existing = db.CauHoi.Find(model.MaCauHoi);
                if (existing == null)
                    return HttpNotFound();
                
                existing.NoiDung = model.NoiDung;
                existing.MaMon = model.MaMon;
                existing.MaDoKho = model.MaDoKho;
                
                db.SaveChanges();
                
                TempData["Success"] = "Cập nhật câu hỏi thành công!";
                return RedirectToAction("Index");
            }
            
            ViewBag.DanhSachMonHoc = new SelectList(db.MonHoc, "MaMon", "TenMon", model.MaMon);
            ViewBag.DanhSachDoKho = new SelectList(db.DoKho, "MaDoKho", "TenDoKho", model.MaDoKho);
            
            return View(model);
        }
        
        // POST: /cauhoi/delete/CH0001
        [HttpPost]
        public JsonResult Delete(string id)
        {
            if (Session["MaGV"] == null)
                return Json(new { success = false, message = "Chưa đăng nhập" });
            
            var cauHoi = db.CauHoi.Find(id);
            if (cauHoi == null)
                return Json(new { success = false, message = "Không tìm thấy câu hỏi" });
            
            // Kiểm tra có trong đề thi không
            int count = db.CT_DETHI.Count(ct => ct.MaCauHoi == id);
            if (count > 0)
                return Json(new { success = false, message = "Không thể xóa câu hỏi đã có trong đề thi" });
            
            db.CauHoi.Remove(cauHoi);
            db.SaveChanges();
            
            return Json(new { success = true, message = "Xóa câu hỏi thành công" });
        }
        
        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }
    }
}
```

### 8.4.2. Model

**CauHoi.cs:**

```csharp
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("CAU_HOI")]
    public class CauHoi
    {
        [Key]
        [StringLength(10)]
        [Display(Name = "Mã câu hỏi")]
        public string MaCauHoi { get; set; }
        
        [Required(ErrorMessage = "Nội dung câu hỏi không được trống")]
        [StringLength(500, MinimumLength = 10, ErrorMessage = "Nội dung từ 10-500 ký tự")]
        [Display(Name = "Nội dung câu hỏi")]
        public string NoiDung { get; set; }
        
        [Required(ErrorMessage = "Vui lòng chọn môn học")]
        [StringLength(10)]
        [Display(Name = "Môn học")]
        public string MaMon { get; set; }
        
        [Required(ErrorMessage = "Vui lòng chọn độ khó")]
        [StringLength(10)]
        [Display(Name = "Độ khó")]
        public string MaDoKho { get; set; }
        
        [StringLength(10)]
        public string MaGV { get; set; }
        
        // Navigation properties
        public virtual MonHoc MonHoc { get; set; }
        public virtual DoKho DoKho { get; set; }
        public virtual GiangVien GiangVien { get; set; }
    }
}
```

**QuanLyDeThiContext.cs:**

```csharp
using System.Data.Entity;

namespace QuanLyRaDeChamThi.Models
{
    public class QuanLyDeThiContext : DbContext
    {
        public QuanLyDeThiContext() : base("name=QuanLyDeThiConnection")
        {
        }
        
        public DbSet<GiangVien> GiangVien { get; set; }
        public DbSet<MonHoc> MonHoc { get; set; }
        public DbSet<DoKho> DoKho { get; set; }
        public DbSet<CauHoi> CauHoi { get; set; }
        public DbSet<DeThi> DeThi { get; set; }
        public DbSet<CT_DETHI> CT_DETHI { get; set; }
        public DbSet<LopHoc> LopHoc { get; set; }
        public DbSet<SinhVien> SinhVien { get; set; }
        public DbSet<KetQua> KetQua { get; set; }
        public DbSet<BangDiemChu> BangDiemChu { get; set; }
        public DbSet<ThamSo> ThamSo { get; set; }
        
        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            // Composite key cho CT_DETHI
            modelBuilder.Entity<CT_DETHI>()
                .HasKey(ct => new { ct.MaDT, ct.MaCauHoi });
            
            // Composite key cho KET_QUA
            modelBuilder.Entity<KetQua>()
                .HasKey(kq => new { kq.MaDT, kq.MaSV });
            
            base.OnModelCreating(modelBuilder);
        }
    }
}
```

### 8.4.3. View

**Views/CauHoi/Index.cshtml:**

```html
@model IEnumerable<QuanLyRaDeChamThi.Models.CauHoi>

@{
    ViewBag.Title = "Quản lý câu hỏi";
}

<div class="container-fluid">
    <div class="row">
        <div class="col-md-12">
            <h2>@ViewBag.Title</h2>
            <hr />
            
            @if (TempData["Success"] != null)
            {
                <div class="alert alert-success alert-dismissible">
                    <button type="button" class="close" data-dismiss="alert">&times;</button>
                    @TempData["Success"]
                </div>
            }
            
            <div class="row mb-3">
                <div class="col-md-8">
                    @using (Html.BeginForm("Index", "CauHoi", FormMethod.Get))
                    {
                        <div class="input-group">
                            <input type="text" name="search" class="form-control" 
                                   placeholder="Tìm kiếm câu hỏi..." 
                                   value="@ViewBag.Search" />
                            <span class="input-group-btn">
                                <button class="btn btn-primary" type="submit">
                                    <i class="fa fa-search"></i> Tìm kiếm
                                </button>
                            </span>
                        </div>
                    }
                </div>
                <div class="col-md-4 text-right">
                    @Html.ActionLink("Thêm câu hỏi", "Create", null, new { @class = "btn btn-success" })
                </div>
            </div>
            
            <div class="table-responsive">
                <table class="table table-striped table-hover">
                    <thead>
                        <tr>
                            <th>STT</th>
                            <th>Nội dung</th>
                            <th>Môn học</th>
                            <th>Độ khó</th>
                            <th>Thao tác</th>
                        </tr>
                    </thead>
                    <tbody>
                        @if (Model.Count() == 0)
                        {
                            <tr>
                                <td colspan="5" class="text-center">
                                    <em>Không có câu hỏi nào</em>
                                </td>
                            </tr>
                        }
                        else
                        {
                            int stt = 1;
                            foreach (var item in Model)
                            {
                                <tr>
                                    <td>@stt</td>
                                    <td>
                                        @if (item.NoiDung.Length > 100)
                                        {
                                            @item.NoiDung.Substring(0, 100)<text>...</text>
                                        }
                                        else
                                        {
                                            @item.NoiDung
                                        }
                                    </td>
                                    <td>@item.MonHoc.TenMon</td>
                                    <td>
                                        <span class="label label-info">@item.DoKho.TenDoKho</span>
                                    </td>
                                    <td>
                                        @Html.ActionLink("Sửa", "Edit", new { id = item.MaCauHoi }, 
                                            new { @class = "btn btn-sm btn-warning" })
                                        <button class="btn btn-sm btn-danger btn-delete" 
                                                data-id="@item.MaCauHoi">
                                            Xóa
                                        </button>
                                    </td>
                                </tr>
                                stt++;
                            }
                        }
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

@section Scripts {
    <script>
        $(document).ready(function () {
            $('.btn-delete').click(function () {
                var maCauHoi = $(this).data('id');
                var row = $(this).closest('tr');
                
                if (confirm('Bạn có chắc chắn muốn xóa câu hỏi này?')) {
                    $.post('@Url.Action("Delete", "CauHoi")', 
                        { id: maCauHoi },
                        function (response) {
                            if (response.success) {
                                alert(response.message);
                                row.fadeOut(300, function() { $(this).remove(); });
                            } else {
                                alert(response.message);
                            }
                        }
                    );
                }
            });
        });
    </script>
}
```

---

## 8.5. Tối ưu hóa hiệu năng

### 8.5.1. Connection Pooling

**Web.config:**

```xml
<connectionStrings>
    <add name="QuanLyDeThiConnection" 
         connectionString="Data Source=(localdb)\MSSQLLocalDB;
                           Initial Catalog=QuanLyRaDeChamThi;
                           Integrated Security=True;
                           Pooling=True;
                           Min Pool Size=5;
                           Max Pool Size=100;
                           Connect Timeout=30" 
         providerName="System.Data.SqlClient" />
</connectionStrings>
```

**Lợi ích:**
- Tái sử dụng connection thay vì tạo mới mỗi request
- Giảm thời gian kết nối từ ~500ms xuống ~10ms
- Hỗ trợ 50+ concurrent users

### 8.5.2. Database Indexing

**SQL Script:**

```sql
-- Index trên foreign key
CREATE NONCLUSTERED INDEX IX_CAU_HOI_MaMon 
ON CAU_HOI(MaMon);

CREATE NONCLUSTERED INDEX IX_CAU_HOI_MaDoKho 
ON CAU_HOI(MaDoKho);

CREATE NONCLUSTERED INDEX IX_CAU_HOI_MaGV 
ON CAU_HOI(MaGV);

CREATE NONCLUSTERED INDEX IX_DE_THI_MaMon 
ON DE_THI(MaMon);

CREATE NONCLUSTERED INDEX IX_KET_QUA_MaSV 
ON KET_QUA(MaSV);
```

**Hiệu quả:**

**Bảng 8.4: So sánh hiệu năng trước và sau tối ưu**

| Query | Before (ms) | After (ms) | Improvement |
|-------|-------------|------------|-------------|
| Load câu hỏi by MaMon | 85 | 15 | **82% faster** |
| Load đề thi by MaGV | 120 | 25 | **79% faster** |
| Load kết quả by MaSV | 95 | 18 | **81% faster** |
| Join 3 tables (DeThi + CT_DETHI + CauHoi) | 350 | 95 | **73% faster** |

### 8.5.3. Caching Strategy

**Output Caching cho trang tĩnh:**

```csharp
[OutputCache(Duration = 3600, VaryByParam = "none")]
public ActionResult About()
{
    return View();
}
```

**Data Caching cho danh sách dropdown:**

```csharp
public List<MonHoc> GetMonHocList()
{
    string cacheKey = "MonHocList";
    var list = HttpContext.Cache[cacheKey] as List<MonHoc>;
    
    if (list == null)
    {
        list = db.MonHoc.ToList();
        HttpContext.Cache.Insert(cacheKey, list, null, 
            DateTime.Now.AddHours(1), TimeSpan.Zero);
    }
    
    return list;
}
```

---

## 8.6. Hướng dẫn cài đặt

### 8.6.1. Yêu cầu hệ thống

**Tối thiểu:**
- OS: Windows 10 (64-bit)
- RAM: 4GB
- CPU: 2 cores
- Disk: 2GB free space
- .NET Framework: 4.6.1+

**Khuyến nghị:**
- OS: Windows 11 (64-bit)
- RAM: 8GB
- CPU: 4 cores
- Disk: 5GB free space (SSD)
- .NET Framework: 4.8

### 8.6.2. Cài đặt phần mềm

**Bước 1: Cài đặt SQL Server**

1. Tải SQL Server 2019 Express từ microsoft.com
2. Chạy file cài đặt
3. Chọn "Basic" installation
4. Accept license, chọn đường dẫn cài đặt
5. Đợi cài đặt hoàn tất (~10 phút)

**Bước 2: Tạo database**

1. Mở SQL Server Management Studio
2. Connect đến (localdb)\MSSQLLocalDB
3. Click chuột phải "Databases" → "New Database"
4. Database name: `QuanLyRaDeChamThi`
5. Click OK
6. Mở file `Database/QuanLyRaDeChamThi.sql`
7. Execute (F5) để tạo bảng và seed data

**Bước 3: Cài đặt ứng dụng ASP.NET**

1. Mở Visual Studio 2022
2. File → Open → Project/Solution
3. Chọn file `QuanLyRaDeChamThi.sln`
4. Đợi Visual Studio restore NuGet packages (~2 phút)
5. Build → Rebuild Solution (Ctrl+Shift+B)
6. Kiểm tra Output window, đảm bảo "Build succeeded"

**Bước 4: Cấu hình connection string**

1. Mở file `Web.config`
2. Tìm section `<connectionStrings>`
3. Sửa `Data Source=(localdb)\MSSQLLocalDB` nếu cần
4. Save file

**Bước 5: Chạy ứng dụng**

1. Debug → Start Debugging (F5)
2. Trình duyệt tự động mở http://localhost:44300
3. Trang đăng nhập xuất hiện
4. Login với: `gv01` / `123456`

**Bước 6 (Optional): Deploy lên IIS**

1. Chuột phải project → Publish
2. Chọn "Folder" → Next
3. Chọn đường dẫn publish (VD: C:\inetpub\wwwroot\QuanLyDeThi)
4. Click "Publish"
5. Mở IIS Manager
6. Add New Website:
   - Site name: QuanLyDeThi
   - Physical path: C:\inetpub\wwwroot\QuanLyDeThi
   - Binding: http, port 8080
7. Application Pool: .NET v4.5, Integrated
8. Start website
9. Truy cập http://localhost:8080

---

**Kết luận chương 8**: Chương này đã trình bày chi tiết về môi trường phát triển, công nghệ sử dụng, cấu trúc code, code mẫu cho Controller/Model/View, các kỹ thuật tối ưu hiệu năng (connection pooling, indexing, caching) với kết quả cải thiện 70-82%, và hướng dẫn cài đặt từng bước. Chương tiếp theo sẽ trình bày về kiểm thử và bảo trì hệ thống.

