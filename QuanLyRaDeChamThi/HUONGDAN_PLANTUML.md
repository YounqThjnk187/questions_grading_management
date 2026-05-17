# HƯỚNG DẪN TẠO SƠ ĐỒ PLANTUML TỰ ĐỘNG

## Giới thiệu

File này chứa:
1. **PlantUML code** cho tất cả sơ đồ trong báo cáo
2. **Python script** tự động generate PNG images
3. **Hướng dẫn** cài đặt và sử dụng

---

## Cài đặt PlantUML

### Phương pháp 1: Cài Java + PlantUML.jar

```powershell
# Cài Java
choco install openjdk11

# Tải PlantUML.jar
Invoke-WebRequest -Uri "https://sourceforge.net/projects/plantuml/files/plantuml.jar/download" -OutFile plantuml.jar

# Test
java -jar plantuml.jar -version
```

### Phương pháp 2: Cài VS Code Extension

```
1. Mở VS Code
2. Cài extension: "PlantUML" by jebbs
3. Ctrl+Shift+P → "PlantUML: Install"
```

### Phương pháp 3: Online Editor

- URL: http://www.plantuml.com/plantuml/uml/
- Copy code vào → Generate → Download PNG

---

## PlantUML Code cho từng sơ đồ

### 1. Use Case Diagram

```plantuml
@startuml UseCase_QuanLyRaDeChamThi
!theme cerulean-outline
title Use Case Diagram - Hệ thống Quản lý Ra đề và Chấm thi

left to right direction
skinparam packageStyle rectangle

actor "Giảng viên" as GV

rectangle "Hệ thống Quản lý Ra đề và Chấm thi" {
  usecase "UC01: Đăng nhập\nhệ thống" as UC01
  usecase "UC02: Quản lý\ncâu hỏi" as UC02
  usecase "UC03: Soạn đề thi" as UC03
  usecase "UC04: Chấm thi" as UC04
  usecase "UC05: Tra cứu\nđề thi" as UC05
  usecase "UC06: Báo cáo năm" as UC06
  usecase "UC07: Thay đổi\ntham số" as UC07
  usecase "UC08: Tra cứu\nnhanh" as UC08
}

GV --> UC01
GV --> UC02
GV --> UC03
GV --> UC04
GV --> UC05
GV --> UC06
GV --> UC07
GV --> UC08

UC02 ..> UC01 : <<include>>
UC03 ..> UC01 : <<include>>
UC04 ..> UC01 : <<include>>
UC05 ..> UC01 : <<include>>
UC06 ..> UC01 : <<include>>
UC07 ..> UC01 : <<include>>
UC08 ..> UC01 : <<include>>

note right of UC03
  Validate:
  - Tổng điểm = 10
  - Số câu ≥ min
end note

@enduml
```

### 2. Class Diagram

```plantuml
@startuml ClassDiagram_QuanLyRaDeChamThi
!theme cerulean-outline
title Class Diagram - Hệ thống Quản lý Ra đề và Chấm thi

class GiangVien {
  + MaGV : string
  + TenGV : string
  + Email : string
  + MatKhau : string
  + NgaySinh : DateTime?
  --
  + CauHois : ICollection<CauHoi>
  + DeThis : ICollection<DeThi>
}

class MonHoc {
  + MaMH : string
  + TenMH : string
  + SoTinChi : int
  --
  + CauHois : ICollection<CauHoi>
}

class DoKho {
  + MaDK : string
  + TenDK : string
  + MoTa : string
  --
  + CauHois : ICollection<CauHoi>
}

class CauHoi {
  + MaCH : int
  + NoiDung : string
  + MaMH : string
  + MaDK : string
  + MaGV : string
  + NgayTao : DateTime
  --
  + MonHoc : MonHoc
  + DoKho : DoKho
  + GiangVien : GiangVien
  + CT_DeThis : ICollection<CT_DETHI>
}

class DeThi {
  + MaDT : int
  + TenDT : string
  + MaMH : string
  + MaGV : string
  + HocKy : int
  + Nam : int
  + TongDiem : decimal
  + ThoiGian : int
  + NgayTao : DateTime
  --
  + MonHoc : MonHoc
  + GiangVien : GiangVien
  + CT_DeThis : ICollection<CT_DETHI>
  + KetQuas : ICollection<KetQua>
}

class CT_DETHI {
  + MaDT : int
  + MaCH : int
  + ThuTu : int
  + Diem : decimal
  --
  + DeThi : DeThi
  + CauHoi : CauHoi
}

class LopHoc {
  + MaLop : string
  + TenLop : string
  + SiSo : int
  --
  + SinhViens : ICollection<SinhVien>
}

class SinhVien {
  + MaSV : string
  + TenSV : string
  + NgaySinh : DateTime
  + MaLop : string
  --
  + LopHoc : LopHoc
  + KetQuas : ICollection<KetQua>
}

class KetQua {
  + MaKQ : int
  + MaDT : int
  + MaSV : string
  + DiemSo : decimal
  + DiemChu : string
  + NgayCham : DateTime
  --
  + DeThi : DeThi
  + SinhVien : SinhVien
}

class BangDiemChu {
  + MaDiemChu : string
  + DiemMin : decimal
  + DiemMax : decimal
}

class ThamSo {
  + TenTS : string
  + GiaTri : string
  + MoTa : string
}

class QuanLyDeThiContext {
  + GiangViens : DbSet<GiangVien>
  + MonHocs : DbSet<MonHoc>
  + DoKhos : DbSet<DoKho>
  + CauHois : DbSet<CauHoi>
  + DeThis : DbSet<DeThi>
  + CT_DETHIs : DbSet<CT_DETHI>
  + LopHocs : DbSet<LopHoc>
  + SinhViens : DbSet<SinhVien>
  + KetQuas : DbSet<KetQua>
  + BangDiemChus : DbSet<BangDiemChu>
  + ThamSos : DbSet<ThamSo>
  --
  + OnModelCreating(builder) : void
}

GiangVien "1" -- "0..*" CauHoi : tạo >
GiangVien "1" -- "0..*" DeThi : soạn >
MonHoc "1" -- "0..*" CauHoi : thuộc >
DoKho "1" -- "0..*" CauHoi : có độ khó >
CauHoi "0..*" -- "0..*" DeThi
(CauHoi, DeThi) .. CT_DETHI
DeThi "1" -- "0..*" KetQua : có >
SinhVien "1" -- "0..*" KetQua : làm bài >
LopHoc "1" -- "0..*" SinhVien : học >

@enduml
```

### 3. Sequence Diagram - Login

```plantuml
@startuml Sequence_Login
!theme cerulean-outline
title Sequence Diagram - UC01: Đăng nhập hệ thống

actor "Giảng viên" as GV
participant "LoginView" as View
participant "AccountController" as Controller
participant "QuanLyDeThiContext" as Context
database "SQL Server" as DB

GV -> View : Nhập MaGV, MatKhau
GV -> View : Click [Đăng nhập]

View -> Controller : POST /Account/Login(model)
activate Controller

Controller -> Controller : ValidateModel()
alt Model không hợp lệ
  Controller --> View : Return View(model) với errors
  View --> GV : Hiển thị lỗi validation
else Model hợp lệ
  Controller -> Context : GiangViens.FirstOrDefault(\n  g => g.MaGV == model.MaGV)
  activate Context
  
  Context -> DB : SELECT * FROM GIANG_VIEN\n  WHERE MaGV = @MaGV
  activate DB
  DB --> Context : GiangVien entity hoặc null
  deactivate DB
  
  Context --> Controller : gv
  deactivate Context
  
  alt Giảng viên không tồn tại
    Controller --> View : ModelState.AddError(\n  "Mã GV không tồn tại")
    View --> GV : Hiển thị lỗi
  else Giảng viên tồn tại
    Controller -> Controller : VerifyPassword(\n  model.MatKhau, gv.MatKhau)
    
    alt Mật khẩu sai
      Controller --> View : ModelState.AddError(\n  "Mật khẩu không đúng")
      View --> GV : Hiển thị lỗi
    else Mật khẩu đúng
      Controller -> Controller : Session["MaGV"] = gv.MaGV\nSession["TenGV"] = gv.TenGV
      Controller --> View : RedirectToAction("Index", "Home")
      deactivate Controller
      View --> GV : Chuyển đến trang chủ
    end
  end
end

@enduml
```

### 4. Sequence Diagram - Create Question

```plantuml
@startuml Sequence_CreateQuestion
!theme cerulean-outline
title Sequence Diagram - UC02: Thêm câu hỏi mới

actor "Giảng viên" as GV
participant "CauHoiView" as View
participant "CauHoiController" as Controller
participant "QuanLyDeThiContext" as Context
database "SQL Server" as DB

GV -> View : Click [Thêm câu hỏi]
View -> Controller : GET /CauHoi/Create
activate Controller

Controller -> Context : MonHocs.ToList()
Controller -> Context : DoKhos.ToList()
Context -> DB : SELECT * FROM MON_HOC, DO_KHO
DB --> Context : List<MonHoc>, List<DoKho>
Context --> Controller : data

Controller --> View : Return View(ViewBag)
deactivate Controller
View --> GV : Hiển thị form thêm mới

GV -> View : Nhập NoiDung, chọn MaMH, MaDK
GV -> View : Click [Lưu]

View -> Controller : POST /CauHoi/Create(model)
activate Controller

Controller -> Controller : ValidateModel()
alt Model không hợp lệ
  Controller --> View : Return View(model) với errors
  View --> GV : Hiển thị lỗi validation
else Model hợp lệ
  Controller -> Controller : model.MaGV = Session["MaGV"]\nmodel.NgayTao = DateTime.Now
  
  Controller -> Context : CauHois.Add(model)
  activate Context
  Context -> Context : SaveChanges()
  Context -> DB : INSERT INTO CAU_HOI\n  (NoiDung, MaMH, MaDK, MaGV, NgayTao)\n  VALUES (...)
  activate DB
  DB --> Context : Rows affected: 1
  deactivate DB
  Context --> Controller : Success
  deactivate Context
  
  Controller --> View : RedirectToAction("Index")
  deactivate Controller
  View --> GV : Chuyển về danh sách câu hỏi
end

@enduml
```

### 5. Sequence Diagram - Create Exam

```plantuml
@startuml Sequence_CreateExam
!theme cerulean-outline
title Sequence Diagram - UC03: Soạn đề thi

actor "Giảng viên" as GV
participant "DeThiView" as View
participant "DeThiController" as Controller
participant "QuanLyDeThiContext" as Context
database "SQL Server" as DB

GV -> View : Click [Soạn đề thi]
View -> Controller : GET /DeThi/Create
activate Controller

Controller -> Context : MonHocs.ToList()
Context -> DB : SELECT * FROM MON_HOC
DB --> Context : List<MonHoc>
Context --> Controller : monHocs

Controller --> View : Return View(ViewBag)
deactivate Controller
View --> GV : Hiển thị form Step 1

GV -> View : Nhập TenDT, chọn MaMH, HocKy, Nam, ThoiGian
GV -> View : Click [Tiếp tục]

View -> Controller : POST /DeThi/SelectQuestions(model)
activate Controller

Controller -> Context : CauHois.Where(\n  c => c.MaMH == model.MaMH).ToList()
Context -> DB : SELECT * FROM CAU_HOI\n  WHERE MaMH = @MaMH
DB --> Context : List<CauHoi>
Context --> Controller : cauHois

Controller --> View : Return View(model, cauHois)
deactivate Controller
View --> GV : Hiển thị form Step 2 với danh sách câu hỏi

GV -> View : Chọn câu hỏi (checkbox)
GV -> View : Nhập điểm cho mỗi câu
GV -> View : Click [Lưu đề thi]

View -> Controller : POST /DeThi/Create(model, selectedQuestions)
activate Controller

Controller -> Controller : ValidateModel()
Controller -> Controller : ValidateTongDiem() // Tổng = 10
Controller -> Controller : ValidateSoCau() // Số câu ≥ min

alt Validation fail
  Controller --> View : Return View(model) với errors
  View --> GV : Hiển thị lỗi
else Validation pass
  Controller -> Controller : model.MaGV = Session["MaGV"]\nmodel.NgayTao = DateTime.Now
  
  Controller -> Context : DeThis.Add(model)
  Context -> Context : SaveChanges()
  Context -> DB : INSERT INTO DE_THI (...)\n  VALUES (...)
  DB --> Context : MaDT (identity)
  
  loop for each selected question
    Controller -> Controller : ct = new CT_DETHI {\n  MaDT = model.MaDT,\n  MaCH = question.MaCH,\n  ThuTu = index,\n  Diem = question.Diem\n}
    Controller -> Context : CT_DETHIs.Add(ct)
  end
  
  Context -> Context : SaveChanges()
  Context -> DB : INSERT INTO CT_DETHI (...)\n  VALUES (...)
  DB --> Context : Success
  
  Context --> Controller : Success
  deactivate Context
  
  Controller --> View : RedirectToAction("Index")
  deactivate Controller
  View --> GV : Chuyển về danh sách đề thi
end

@enduml
```

### 6. Sequence Diagram - Grading

```plantuml
@startuml Sequence_Grading
!theme cerulean-outline
title Sequence Diagram - UC04: Chấm thi

actor "Giảng viên" as GV
participant "KetQuaView" as View
participant "KetQuaController" as Controller
participant "QuanLyDeThiContext" as Context
database "SQL Server" as DB

GV -> View : Click [Chấm thi]
View -> Controller : GET /KetQua/Create
activate Controller

Controller -> Context : DeThis.ToList()
Controller -> Context : SinhViens.ToList()
Context -> DB : SELECT * FROM DE_THI, SINH_VIEN
DB --> Context : List<DeThi>, List<SinhVien>
Context --> Controller : data

Controller --> View : Return View(ViewBag)
deactivate Controller
View --> GV : Hiển thị form chấm thi

GV -> View : Chọn MaDT, MaSV
GV -> View : Nhập DiemSo
GV -> View : Click [Lưu điểm]

View -> Controller : POST /KetQua/Create(model)
activate Controller

Controller -> Controller : ValidateModel()
Controller -> Controller : ValidateDiemSo() // 0-10

alt Validation fail
  Controller --> View : Return View(model) với errors
  View --> GV : Hiển thị lỗi
else Validation pass
  Controller -> Context : sp_GetDiemChu(model.DiemSo)
  activate Context
  Context -> DB : EXEC sp_GetDiemChu @DiemSo
  activate DB
  
  note right of DB
    Stored Procedure logic:
    IF @DiemSo >= 8.5 RETURN 'A'
    IF @DiemSo >= 8.0 RETURN 'B+'
    IF @DiemSo >= 7.0 RETURN 'B'
    ...
  end note
  
  DB --> Context : DiemChu (string)
  deactivate DB
  Context --> Controller : diemChu
  deactivate Context
  
  Controller -> Controller : model.DiemChu = diemChu\nmodel.NgayCham = DateTime.Now
  
  Controller -> Context : KetQuas.Add(model)
  Context -> Context : SaveChanges()
  Context -> DB : INSERT INTO KET_QUA\n  (MaDT, MaSV, DiemSo, DiemChu, NgayCham)\n  VALUES (...)
  DB --> Context : Success
  Context --> Controller : Success
  
  Controller --> View : RedirectToAction("Index")
  deactivate Controller
  View --> GV : Chuyển về danh sách kết quả
end

@enduml
```

### 7. Sequence Diagram - Annual Report

```plantuml
@startuml Sequence_AnnualReport
!theme cerulean-outline
title Sequence Diagram - UC06: Báo cáo năm

actor "Giảng viên" as GV
participant "BaoCaoView" as View
participant "BaoCaoController" as Controller
participant "QuanLyDeThiContext" as Context
database "SQL Server" as DB

GV -> View : Click [Báo cáo năm]
View -> Controller : GET /BaoCao/Index
activate Controller

Controller --> View : Return View()
deactivate Controller
View --> GV : Hiển thị form nhập năm

GV -> View : Nhập năm (ví dụ: 2026)
GV -> View : Click [Xem báo cáo]

View -> Controller : POST /BaoCao/Index(nam)
activate Controller

Controller -> Context : Database.SqlQuery<BaoCaoDTO>(\n  "EXEC sp_BaoCaoNam @Nam", nam)
activate Context

Context -> DB : EXEC sp_BaoCaoNam @Nam = 2026
activate DB

note right of DB
  Stored Procedure:
  SELECT 
    mh.TenMH,
    COUNT(dt.MaDT) as SoDeThi
  FROM MON_HOC mh
  LEFT JOIN DE_THI dt 
    ON mh.MaMH = dt.MaMH 
    AND dt.Nam = @Nam
  GROUP BY mh.TenMH
  ORDER BY SoDeThi DESC
end note

DB --> Context : SqlDataReader (rows)
deactivate DB

Context -> Context : Map to List<BaoCaoDTO>
Context --> Controller : List<BaoCaoDTO> data
deactivate Context

Controller -> Controller : ViewBag.Data = data\nViewBag.Nam = nam

Controller --> View : Return View(ViewBag)
deactivate Controller

View -> View : Render bar chart (Chart.js)
View --> GV : Hiển thị biểu đồ cột + bảng

alt GV click [Xuất CSV]
  GV -> View : Click [Xuất CSV]
  View -> Controller : GET /BaoCao/ExportCSV(nam)
  activate Controller
  
  Controller -> Context : sp_BaoCaoNam(nam)
  Context -> DB : EXEC sp_BaoCaoNam @Nam
  DB --> Context : data
  Context --> Controller : data
  
  Controller -> Controller : Generate CSV with UTF-8 BOM
  Controller --> View : Return File(\n  bytes, "text/csv",\n  "BaoCao_2026.csv")
  deactivate Controller
  
  View --> GV : Download file CSV
end

@enduml
```

### 8. Activity Diagram - Create Question

```plantuml
@startuml Activity_CreateQuestion
!theme cerulean-outline
title Activity Diagram - Thêm câu hỏi mới

start

:Giảng viên đăng nhập;

:Click [Thêm câu hỏi];

:Hiển thị form thêm mới;

:Nhập nội dung câu hỏi;

:Chọn môn học;

:Chọn độ khó;

:Click [Lưu];

if (Validate form?) then (Fail)
  :Hiển thị lỗi validation;
  stop
else (Pass)
  :Lưu vào database;
  
  if (Lưu thành công?) then (Yes)
    :Hiển thị thông báo thành công;
    :Quay về danh sách câu hỏi;
    stop
  else (No)
    :Hiển thị lỗi database;
    stop
  endif
endif

@enduml
```

### 9. Activity Diagram - Create Exam

```plantuml
@startuml Activity_CreateExam
!theme cerulean-outline
title Activity Diagram - Soạn đề thi

start

:Giảng viên đăng nhập;

:Click [Soạn đề thi];

partition "Step 1: Thông tin đề thi" {
  :Hiển thị form thông tin;
  :Nhập tên đề thi;
  :Chọn môn học;
  :Nhập học kỳ, năm, thời gian;
  :Click [Tiếp tục];
  
  if (Validate form?) then (Fail)
    :Hiển thị lỗi;
    stop
  endif
}

partition "Step 2: Chọn câu hỏi" {
  :Load danh sách câu hỏi theo môn học;
  :Hiển thị danh sách checkbox;
  
  repeat
    :Chọn câu hỏi (checkbox);
    :Nhập điểm cho câu hỏi;
  repeat while (Còn câu hỏi?) is (Yes)
  
  :Click [Lưu đề thi];
  
  if (Tổng điểm = 10?) then (No)
    :Hiển thị lỗi "Tổng điểm phải bằng 10";
    stop
  endif
  
  if (Số câu ≥ min?) then (No)
    :Hiển thị lỗi "Số câu không đủ";
    stop
  endif
}

:Lưu đề thi vào DE_THI;
:Lưu chi tiết vào CT_DETHI;

if (Lưu thành công?) then (Yes)
  :Hiển thị thông báo thành công;
  :Quay về danh sách đề thi;
  stop
else (No)
  :Hiển thị lỗi database;
  stop
endif

@enduml
```

### 10. Component Diagram

```plantuml
@startuml Component_QuanLyRaDeChamThi
!theme cerulean-outline
title Component Diagram - Hệ thống Quản lý Ra đề và Chấm thi

package "Presentation Layer" {
  component [Razor Views] as Views
  component [JavaScript/jQuery] as JS
  component [Bootstrap CSS] as CSS
}

package "Business Logic Layer" {
  component [AccountController] as AccCtrl
  component [CauHoiController] as CHCtrl
  component [DeThiController] as DTCtrl
  component [KetQuaController] as KQCtrl
  component [BaoCaoController] as BCCtrl
  component [ThamSoController] as TSCtrl
}

package "Data Access Layer" {
  component [Entity Framework 6] as EF
  component [QuanLyDeThiContext] as Context
  component [LINQ Queries] as LINQ
}

database "SQL Server 2019" {
  component [Tables (11)] as Tables
  component [Stored Procedures (4)] as SPs
  component [Indexes (5)] as Indexes
}

cloud "External Services" {
  component [Chart.js CDN] as Chart
  component [jQuery CDN] as jQueryCDN
}

Views --> JS : uses
Views --> CSS : styles
Views --> AccCtrl : HTTP POST/GET
Views --> CHCtrl : HTTP POST/GET
Views --> DTCtrl : HTTP POST/GET
Views --> KQCtrl : HTTP POST/GET
Views --> BCCtrl : HTTP POST/GET
Views --> TSCtrl : HTTP POST/GET

JS --> Chart : renders charts
JS --> jQueryCDN : library

AccCtrl --> Context : queries
CHCtrl --> Context : queries
DTCtrl --> Context : queries
KQCtrl --> Context : queries
BCCtrl --> Context : queries
TSCtrl --> Context : queries

Context --> EF : uses ORM
Context --> LINQ : executes
EF --> Tables : CRUD operations
LINQ --> SPs : executes

@enduml
```

### 11. Deployment Diagram

```plantuml
@startuml Deployment_QuanLyRaDeChamThi
!theme cerulean-outline
title Deployment Diagram - Hệ thống Quản lý Ra đề và Chấm thi

node "Client Machine" as Client {
  component [Web Browser\n(Chrome/Edge/Firefox)] as Browser
}

node "Application Server\n(192.168.1.100)" as AppServer {
  artifact "IIS 10.0" as IIS {
    component [ASP.NET MVC 5\nApplication] as App
  }
  
  note right of IIS
    OS: Windows Server 2019
    RAM: 8GB
    CPU: 4 cores
    .NET Framework 4.6.1
  end note
}

node "Database Server\n(192.168.1.101)" as DBServer {
  database "SQL Server 2019\nExpress Edition" as DB {
    component [QuanLyRaDeChamThi\nDatabase] as QLDT_DB
  }
  
  note right of DB
    OS: Windows Server 2019
    RAM: 16GB
    CPU: 8 cores
    Storage: 500GB SSD
  end note
}

node "Backup Server\n(192.168.1.102)" as BackupServer {
  folder "Backup Storage" as Backup {
    artifact [Daily Backups\n(.bak files)] as BakFiles
  }
  
  note right of Backup
    OS: Windows Server 2019
    Storage: 2TB HDD
    Schedule: Daily 2:00 AM
  end note
}

Browser -down-> IIS : HTTPS (443)\nHTTP (80)
App -down-> QLDT_DB : ADO.NET\nTCP/IP (1433)
QLDT_DB -right-> BakFiles : Backup Job\n(Daily)

@enduml
```

### 12. ERD (Entity Relationship Diagram)

```plantuml
@startuml ERD_QuanLyRaDeChamThi
!theme cerulean-outline
title ERD - Hệ thống Quản lý Ra đề và Chấm thi

entity "GIANG_VIEN" as GV {
  * MaGV : varchar(10) <<PK>>
  --
  TenGV : nvarchar(100)
  Email : varchar(100)
  MatKhau : varchar(255)
  NgaySinh : date
}

entity "MON_HOC" as MH {
  * MaMH : varchar(10) <<PK>>
  --
  TenMH : nvarchar(100)
  SoTinChi : int
}

entity "DO_KHO" as DK {
  * MaDK : varchar(10) <<PK>>
  --
  TenDK : nvarchar(50)
  MoTa : nvarchar(255)
}

entity "CAU_HOI" as CH {
  * MaCH : int <<PK, Identity>>
  --
  NoiDung : nvarchar(MAX)
  MaMH : varchar(10) <<FK>>
  MaDK : varchar(10) <<FK>>
  MaGV : varchar(10) <<FK>>
  NgayTao : datetime
}

entity "DE_THI" as DT {
  * MaDT : int <<PK, Identity>>
  --
  TenDT : nvarchar(200)
  MaMH : varchar(10) <<FK>>
  MaGV : varchar(10) <<FK>>
  HocKy : int
  Nam : int
  TongDiem : decimal(5,2)
  ThoiGian : int
  NgayTao : datetime
}

entity "CT_DETHI" as CT {
  * MaDT : int <<PK, FK>>
  * MaCH : int <<PK, FK>>
  --
  ThuTu : int
  Diem : decimal(5,2)
}

entity "LOP_HOC" as LH {
  * MaLop : varchar(10) <<PK>>
  --
  TenLop : nvarchar(100)
  SiSo : int
}

entity "SINH_VIEN" as SV {
  * MaSV : varchar(10) <<PK>>
  --
  TenSV : nvarchar(100)
  NgaySinh : date
  MaLop : varchar(10) <<FK>>
}

entity "KET_QUA" as KQ {
  * MaKQ : int <<PK, Identity>>
  --
  MaDT : int <<FK>>
  MaSV : varchar(10) <<FK>>
  DiemSo : decimal(5,2)
  DiemChu : nvarchar(5)
  NgayCham : datetime
}

entity "BANG_DIEM_CHU" as BDC {
  * MaDiemChu : nvarchar(5) <<PK>>
  --
  DiemMin : decimal(5,2)
  DiemMax : decimal(5,2)
}

entity "THAM_SO" as TS {
  * TenTS : nvarchar(50) <<PK>>
  --
  GiaTri : nvarchar(255)
  MoTa : nvarchar(500)
}

GV ||--o{ CH : "tạo"
GV ||--o{ DT : "soạn"
MH ||--o{ CH : "thuộc"
MH ||--o{ DT : "dành cho"
DK ||--o{ CH : "phân loại"

CH }o--|| CT
DT ||--o{ CT
DT ||--o{ KQ : "có"

LH ||--o{ SV : "học"
SV ||--o{ KQ : "làm bài"

@enduml
```

---

## Python Script tự động generate

Tạo file `generate_diagrams.py`:

```python
#!/usr/bin/env python3
"""
Script tự động generate tất cả PlantUML diagrams
Yêu cầu: Java + plantuml.jar
"""

import os
import subprocess
from pathlib import Path

# Cấu hình
PLANTUML_JAR = "plantuml.jar"  # Đường dẫn đến plantuml.jar
DIAGRAMS_DIR = Path(__file__).parent / "diagrams"
OUTPUT_DIR = DIAGRAMS_DIR / "output"

# Danh sách các diagram files
DIAGRAM_FILES = {
    "UseCase": "01_UseCase_QuanLyRaDeChamThi.puml",
    "ClassDiagram": "02_ClassDiagram_QuanLyRaDeChamThi.puml",
    "Sequence_Login": "03_Sequence_Login.puml",
    "Sequence_CreateQuestion": "04_Sequence_CreateQuestion.puml",
    "Sequence_CreateExam": "05_Sequence_CreateExam.puml",
    "Sequence_Grading": "06_Sequence_Grading.puml",
    "Sequence_AnnualReport": "07_Sequence_AnnualReport.puml",
    "Activity_CreateQuestion": "08_Activity_CreateQuestion.puml",
    "Activity_CreateExam": "09_Activity_CreateExam.puml",
    "Component": "10_Component_QuanLyRaDeChamThi.puml",
    "Deployment": "11_Deployment_QuanLyRaDeChamThi.puml",
    "ERD": "12_ERD_QuanLyRaDeChamThi.puml",
}


def check_plantuml():
    """Kiểm tra PlantUML có sẵn không"""
    if not Path(PLANTUML_JAR).exists():
        print(f"❌ Không tìm thấy {PLANTUML_JAR}")
        print("   Tải từ: https://sourceforge.net/projects/plantuml/files/plantuml.jar/download")
        return False
    
    try:
        result = subprocess.run(
            ["java", "-version"],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("❌ Java chưa được cài đặt")
            print("   Cài đặt: choco install openjdk11")
            return False
    except FileNotFoundError:
        print("❌ Java chưa được cài đặt")
        return False
    
    return True


def generate_diagram(puml_file, output_format="png"):
    """Generate 1 diagram từ .puml file"""
    input_path = DIAGRAMS_DIR / puml_file
    
    if not input_path.exists():
        print(f"⚠️  File không tồn tại: {puml_file}")
        return False
    
    cmd = [
        "java",
        "-jar",
        PLANTUML_JAR,
        "-t" + output_format,  # png, svg, eps
        "-o",
        str(OUTPUT_DIR.absolute()),
        str(input_path.absolute())
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            output_file = OUTPUT_DIR / input_path.with_suffix(f".{output_format}").name
            print(f"✅ Generated: {output_file.name}")
            return True
        else:
            print(f"❌ Error generating {puml_file}:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False


def generate_all_diagrams(output_format="png"):
    """Generate tất cả diagrams"""
    print("🚀 Bắt đầu generate PlantUML diagrams...")
    print(f"📁 Output directory: {OUTPUT_DIR}")
    print(f"📊 Format: {output_format.upper()}")
    print("=" * 60)
    
    # Tạo thư mục output nếu chưa có
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    success_count = 0
    fail_count = 0
    
    for name, puml_file in DIAGRAM_FILES.items():
        print(f"\n📐 {name}...")
        if generate_diagram(puml_file, output_format):
            success_count += 1
        else:
            fail_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Thành công: {success_count}/{len(DIAGRAM_FILES)}")
    print(f"❌ Thất bại: {fail_count}/{len(DIAGRAM_FILES)}")
    print(f"📁 Xem kết quả tại: {OUTPUT_DIR}")


def main():
    """Main function"""
    print("=" * 60)
    print("   PlantUML Diagram Generator")
    print("   Hệ thống Quản lý Ra đề và Chấm thi")
    print("=" * 60)
    
    # Kiểm tra dependencies
    if not check_plantuml():
        print("\n⚠️  Vui lòng cài đặt Java và tải plantuml.jar")
        return
    
    # Generate diagrams
    print("\n✅ Java và PlantUML đã sẵn sàng!")
    
    # Chọn format
    print("\nChọn output format:")
    print("  1. PNG (default)")
    print("  2. SVG (vector, scalable)")
    print("  3. EPS (for LaTeX)")
    
    choice = input("\nLựa chọn (1-3, Enter = PNG): ").strip()
    
    format_map = {
        "1": "png",
        "2": "svg",
        "3": "eps",
        "": "png"
    }
    
    output_format = format_map.get(choice, "png")
    
    # Generate
    generate_all_diagrams(output_format)
    
    print("\n🎉 Hoàn thành!")


if __name__ == "__main__":
    main()
```

---

## Hướng dẫn sử dụng

### Bước 1: Chuẩn bị môi trường

```powershell
# Cài Java
choco install openjdk11

# Tải PlantUML.jar
cd "c:\Users\UDT4HC\Downloads\CNPM new\Project\QuanLyRaDeChamThi"
Invoke-WebRequest -Uri "https://sourceforge.net/projects/plantuml/files/plantuml.jar/download" -OutFile plantuml.jar
```

### Bước 2: Tạo thư mục diagrams

```powershell
mkdir diagrams
mkdir diagrams\output
```

### Bước 3: Copy PlantUML code

Copy từng đoạn code PlantUML ở trên vào các file:
- `diagrams/01_UseCase_QuanLyRaDeChamThi.puml`
- `diagrams/02_ClassDiagram_QuanLyRaDeChamThi.puml`
- ... (12 files)

### Bước 4: Generate diagrams

```powershell
# Chạy Python script
python generate_diagrams.py

# Hoặc generate thủ công
java -jar plantuml.jar -tpng -o "diagrams/output" "diagrams/*.puml"
```

### Bước 5: Sử dụng trong báo cáo

```markdown
# Trong file .md
![Use Case Diagram](diagrams/output/01_UseCase_QuanLyRaDeChamThi.png)
```

---

## Tips

### 1. Preview trong VS Code

- Cài extension "PlantUML"
- Mở file .puml
- Nhấn `Alt+D` để xem preview

### 2. Generate multiple formats

```powershell
# PNG + SVG + EPS cùng lúc
java -jar plantuml.jar -tpng -tsvg -teps -o "output" "*.puml"
```

### 3. Custom themes

```plantuml
!theme cerulean-outline  ' Xanh dương
!theme amiga             ' Retro
!theme sketchy-outline   ' Hand-drawn style
```

### 4. Export to Word/PDF

- Generate PNG với resolution cao
- Insert vào Word: Insert → Pictures
- Trong Pandoc: Images tự động embed

---

## Troubleshooting

**Q: "java: command not found"**
```powershell
# Cài Java
choco install openjdk11
```

**Q: "Error reading plantuml.jar"**
```powershell
# Tải lại
Invoke-WebRequest -Uri "https://sourceforge.net/projects/plantuml/files/plantuml.jar/download" -OutFile plantuml.jar
```

**Q: "Syntax error in .puml file"**
```
→ Kiểm tra lại code PlantUML
→ Preview trong VS Code để debug
```

**Q: "PNG quá nhỏ"**
```powershell
# Tăng DPI
java -DPLANTUML_LIMIT_SIZE=8192 -jar plantuml.jar -tpng *.puml
```