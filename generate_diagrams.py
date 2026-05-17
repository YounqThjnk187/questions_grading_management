#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo diagram PlantUML bằng plantuml.com online service
Không cần cài đặt PlantUML local
"""

import requests
import base64
import zlib
from pathlib import Path
import sys

# PlantUML online API
PLANTUML_API = "http://www.plantuml.com/plantuml"

def plantuml_encode(text):
    """Mã hoá PlantUML text thành URL-safe format"""
    # Dùng zlib compress + custom base64
    encoded = text.strip().encode('utf-8')
    compressed = zlib.compress(encoded, 9)
    # PlantUML uses custom alphabet
    b64 = base64.b64encode(compressed).decode('ascii')
    # Replace standard base64 chars with PlantUML's custom alphabet
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"
    standard = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    trans = str.maketrans(standard, alphabet)
    return b64.translate(trans)

def download_diagram(name, plantuml_code, output_dir):
    """Download diagram từ PlantUML online API"""
    try:
        # Encode code
        encoded = plantuml_encode(plantuml_code)
        
        # Tạo URL
        url = f"{PLANTUML_API}/img/{encoded}"
        
        print(f"⏳ Generating: {name}")
        
        # Download
        response = requests.get(url, timeout=30, stream=True)
        response.raise_for_status()
        
        # Save
        output_file = output_dir / f"{name}.png"
        with open(output_file, 'wb') as f:
            f.write(response.content)
        
        file_size = output_file.stat().st_size / 1024
        print(f"✓ Saved: {name}.png ({file_size:.1f}KB)")
        
        return str(output_file)
        
    except Exception as e:
        print(f"✗ Error: {name} - {e}")
        return None

# Tất cả PlantUML diagrams
DIAGRAMS = {
    "01-UseCase": """
@startuml
!theme cerulean-outline
title Use Case Diagram - Hệ thống Quản lý Ra đề và Chấm thi

left to right direction
skinparam packageStyle rectangle
skinparam backgroundColor #F0F0F0

actor "Giảng viên" as GV

rectangle "Hệ thống" {
  usecase "UC01: Đăng nhập" as UC01
  usecase "UC02: Quản lý câu hỏi" as UC02
  usecase "UC03: Soạn đề thi" as UC03
  usecase "UC04: Chấm thi" as UC04
  usecase "UC05: Tra cứu đề" as UC05
  usecase "UC06: Báo cáo năm" as UC06
  usecase "UC07: Quản lý tham số" as UC07
}

GV --> UC01
GV --> UC02
GV --> UC03
GV --> UC04
GV --> UC05
GV --> UC06
GV --> UC07

UC02 ..> UC01 : <<include>>
UC03 ..> UC01 : <<include>>
UC04 ..> UC01 : <<include>>

@enduml
""",

    "02-Database-ER": """
@startuml
!theme cerulean-outline
title ER Diagram - Schema Database

entity "GIANG_VIEN" as GV {
  *MaGV
  TenGV
  Email
  MatKhau
}

entity "MON_HOC" as MH {
  *MaMH
  TenMH
  SoTinChi
}

entity "DO_KHO" as DK {
  *MaDK
  TenDK
}

entity "CAU_HOI" as CH {
  *MaCH
  NoiDung
  MaMH FK
  MaDK FK
  MaGV FK
}

entity "DE_THI" as DT {
  *MaDT
  TenDT
  MaMH FK
  MaGV FK
  TongDiem
}

entity "CT_DETHI" as CTD {
  *MaDT FK
  *MaCH FK
  Diem
}

entity "SINH_VIEN" as SV {
  *MaSV
  TenSV
  MaLop
}

entity "KET_QUA" as KQ {
  *MaKQ
  MaDT FK
  MaSV FK
  DiemSo
  DiemChu
}

GV ||--o{ CH : tạo
GV ||--o{ DT : soạn
MH ||--o{ CH : chứa
DK ||--o{ CH : phân loại
DT ||--o{ CTD : có
CH ||--o{ CTD : trong
DT ||--o{ KQ : chấm
SV ||--o{ KQ : làm

@enduml
""",

    "03-ClassDiagram": """
@startuml
!theme cerulean-outline
title Class Diagram - Kiến trúc Object

class GiangVien {
  - MaGV: string
  - TenGV: string
  - Email: string
  - MatKhau: string
  + GetCauHois(): List<CauHoi>
  + GetDeThis(): List<DeThi>
}

class CauHoi {
  - MaCH: int
  - NoiDung: string
  - NgayTao: DateTime
  + Validate(): bool
}

class DeThi {
  - MaDT: int
  - TenDT: string
  - TongDiem: decimal
  + ValidateTongDiem(): bool
  + GetCauHois(): List<CauHoi>
}

class KetQua {
  - MaKQ: int
  - DiemSo: decimal
  - DiemChu: string
  + GetDiemChu(score): string
}

GiangVien "1" -- "0..*" CauHoi
GiangVien "1" -- "0..*" DeThi
DeThi "1" -- "0..*" KetQua

@enduml
""",

    "04-Activity-CreateExam": """
@startuml
!theme cerulean-outline
title Activity Diagram - Soạn Đề Thi

start
:Giảng viên mở Soạn đề thi;
:Nhập tên đề thi, chọn môn học;
:Chọn học kỳ, năm, thời gian;
:Hệ thống hiển thị danh sách câu hỏi;
:Giảng viên chọn câu hỏi;
:Nhập điểm cho từng câu;

if (Tổng điểm = 10?) then (No)
  :Lỗi! Tổng điểm phải = 10;
  :Quay lại chỉnh sửa;
  :Nhập lại;
else (Yes)
  if (Số câu hỏi >= tối thiểu?) then (No)
    :Lỗi! Số câu quá ít;
    :Chọn thêm câu;
  else (Yes)
    :Click Lưu Đề Thi;
    :Hệ thống lưu vào database;
    :Thông báo thành công;
    stop
  endif
endif

@enduml
""",

    "05-Sequence-Login": """
@startuml
!theme cerulean-outline
title Sequence Diagram - UC01 Đăng Nhập

actor "Giảng Viên" as GV
participant "Browser" as View
participant "LoginController" as Ctrl
database "SQL Server" as DB

GV -> View: Nhập MaGV, MatKhau
GV -> View: Click [Đăng nhập]

View -> Ctrl: POST /Account/Login
activate Ctrl

Ctrl -> Ctrl: ValidateModel()

alt Model không hợp lệ
  Ctrl --> View: Return form + errors
  View --> GV: Hiển thị lỗi
else Model hợp lệ
  Ctrl -> DB: SELECT * FROM GIANG_VIEN
  activate DB
  DB --> Ctrl: GiangVien record
  deactivate DB
  
  Ctrl -> Ctrl: VerifyPassword()
  
  alt Mật khẩu sai
    Ctrl --> View: Error: Sai mật khẩu
    View --> GV: Hiển thị thông báo
  else Mật khẩu đúng
    Ctrl -> Ctrl: Session["MaGV"] = MaGV
    deactivate Ctrl
    Ctrl --> View: Redirect /Home/Index
    View --> GV: Trang chủ
  endif
endif

@enduml
""",

    "06-Architecture": """
@startuml
!theme cerulean-outline
title Kiến trúc Hệ thống - 3-Tier Architecture

package "Presentation Layer" {
  component [Web Browser] as Browser
  component [HTML/CSS/JS] as Frontend
}

package "Application Layer" {
  component [ASP.NET MVC 5] as MVC
  component [Controllers] as Ctrl
  component [Views] as Views
  component [Business Logic] as BL
}

package "Data Layer" {
  component [Entity Framework 6] as EF
  component [Models] as Models
  component [LINQ Queries] as LINQ
}

package "Database" {
  database [SQL Server 2019] as SQL
}

Browser --> Frontend
Frontend --|> MVC
MVC --> Ctrl
Ctrl --> Views
Ctrl --> BL
BL --> EF
EF --> Models
EF --> LINQ
LINQ --> SQL
SQL ..> SQL

@enduml
"""
}

def main():
    print("=" * 70)
    print(" 📊 PlantUML Diagram Generator - Hoàn chỉnh Báo Cáo")
    print("=" * 70)
    
    # Create output directory
    output_dir = Path("/Users/duongthinh/Downloads/Project/QuanLyRaDeChamThi/BaoCao/diagrams")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n📁 Output directory: {output_dir}\n")
    
    # Download all diagrams
    results = {}
    for diagram_name, plantuml_code in DIAGRAMS.items():
        result = download_diagram(diagram_name, plantuml_code, output_dir)
        results[diagram_name] = result
        print()
    
    # Summary
    print("=" * 70)
    successful = sum(1 for r in results.values() if r)
    print(f"✓ Success: {successful}/{len(DIAGRAMS)} diagrams")
    print("=" * 70)
    
    return 0 if successful == len(DIAGRAMS) else 1

if __name__ == "__main__":
    sys.exit(main())
