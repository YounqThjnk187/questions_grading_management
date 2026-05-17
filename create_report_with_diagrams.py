#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo báo cáo Word hoàn chỉnh với PlantUML diagrams
"""

import subprocess
from pathlib import Path
import os

def create_enhanced_report():
    """Tạo báo cáo Word với diagram"""
    
    bao_cao_dir = Path("/Users/duongthinh/Downloads/Project/QuanLyRaDeChamThi/BaoCao")
    diagrams_dir = bao_cao_dir / "diagrams"
    
    # Danh sách file markdown theo thứ tự
    md_files = [
        "00_BIA.md",
        "01_NHANXET.md",
        "02_LOICAMON.md",
        "03_MUCLUC.md",
        "04_DANHSACHHINHANH_BANGBIEU.md",
        "05_TOMTAT.md",
        "06_CHUONG1_TONGQUAN.md",
        "07_CHUONG2_XACDINH_YEUCAU.md",
        "08_CHUONG3_PHANTICH_YEUCAU.md",
        "09_CHUONG4_THIETKE_HETHONG.md",
        "10_CHUONG5_THIETKE_DOITUONG.md",
        "11_CHUONG6_THIETKE_DULIEU.md",
        "12_CHUONG7_THIETKE_GIAODIEN.md",
        "13_CHUONG8_CAIDAT.md",
        "14_CHUONG9_KIEMTHU.md",
        "15_KETLUAN_TAILIEU.md",
    ]
    
    # Tạo file markdown tạm thời với diagram
    temp_md = bao_cao_dir / "BAO_CAO_TEMP.md"
    
    with open(temp_md, 'w', encoding='utf-8') as f:
        # Ghi tất cả markdown files
        for md_file in md_files:
            md_path = bao_cao_dir / md_file
            if md_path.exists():
                with open(md_path, 'r', encoding='utf-8') as src:
                    content = src.read()
                    f.write(content)
                    f.write("\n\n")
        
        # Thêm phần diagram
        f.write("\n\n---\n\n")
        f.write("# Phụ lục: Sơ đồ và Kiến trúc\n\n")
        
        if (diagrams_dir / "01-UseCase.png").exists():
            f.write("## 1. Biểu đồ Use Case\n\n")
            f.write("![Use Case Diagram](diagrams/01-UseCase.png)\n\n")
        
        if (diagrams_dir / "02-Database-ER.png").exists():
            f.write("## 2. Sơ đồ ER - Database\n\n")
            f.write("![ER Diagram](diagrams/02-Database-ER.png)\n\n")
        
        if (diagrams_dir / "03-ClassDiagram.png").exists():
            f.write("## 3. Class Diagram\n\n")
            f.write("![Class Diagram](diagrams/03-ClassDiagram.png)\n\n")
        
        if (diagrams_dir / "04-Activity-CreateExam.png").exists():
            f.write("## 4. Activity Diagram - Soạn Đề Thi\n\n")
            f.write("![Activity Diagram](diagrams/04-Activity-CreateExam.png)\n\n")
        
        if (diagrams_dir / "05-Sequence-Login.png").exists():
            f.write("## 5. Sequence Diagram - Đăng Nhập\n\n")
            f.write("![Sequence Diagram](diagrams/05-Sequence-Login.png)\n\n")
        
        if (diagrams_dir / "06-Architecture.png").exists():
            f.write("## 6. Kiến trúc Hệ thống - 3-Tier\n\n")
            f.write("![Architecture Diagram](diagrams/06-Architecture.png)\n\n")
    
    print("✓ Markdown tạm thời tạo thành công")
    
    # Chuyển đổi sang Word với --toc
    output_docx = bao_cao_dir / "BAO_CAO_HOAN_CHINH_VOI_DIAGRAM.docx"
    
    cmd = [
        "pandoc",
        str(temp_md),
        "-o", str(output_docx),
        "--from=markdown",
        "--to=docx",
        "--toc",
        "--toc-depth=3",
        "--number-sections"
    ]
    
    print(f"\n⏳ Đang chuyển đổi sang Word...")
    print(f"   Lệnh: pandoc ... -o {output_docx.name}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(bao_cao_dir))
        
        if result.returncode == 0:
            file_size = output_docx.stat().st_size / (1024 * 1024)
            print(f"✓ Thành công: {output_docx.name} ({file_size:.1f}MB)")
        else:
            print(f"✗ Lỗi: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Lỗi chuyển đổi: {e}")
        return False
    
    # Xoá file tạm
    if temp_md.exists():
        temp_md.unlink()
        print("✓ Xoá file tạm")
    
    return True

if __name__ == "__main__":
    print("=" * 70)
    print(" 📄 Tạo Báo Cáo Word Hoàn Chỉnh Với Diagram")
    print("=" * 70)
    print()
    
    success = create_enhanced_report()
    
    print()
    print("=" * 70)
    if success:
        print("✓ Báo cáo hoàn chỉnh đã được tạo!")
    else:
        print("✗ Có lỗi trong quá trình tạo báo cáo")
    print("=" * 70)
