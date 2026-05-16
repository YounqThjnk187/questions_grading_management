# HƯỚNG DẪN CHUYỂN ĐỔI BÁO CÁO SANG WORD

## Phương pháp 1: Sử dụng Pandoc (Khuyên dùng)

### Cài đặt Pandoc

```powershell
# Tải Pandoc từ: https://pandoc.org/installing.html
# Hoặc dùng Chocolatey:
choco install pandoc
```

### Chuyển đổi từng file

```powershell
cd "c:\Users\UDT4HC\Downloads\CNPM new\Project\QuanLyRaDeChamThi\BaoCao"

# Chuyển 1 file
pandoc 06_CHUONG1_TONGQUAN.md -o Chuong1.docx

# Chuyển tất cả files
Get-ChildItem *.md | ForEach-Object {
    $outFile = $_.BaseName + ".docx"
    pandoc $_.Name -o $outFile
}
```

### Chuyển đổi toàn bộ thành 1 file Word

```powershell
# Gộp tất cả chương thành 1 file Word duy nhất
pandoc 00_BIA.md `
       01_NHANXET.md `
       02_LOICAMON.md `
       03_MUCLUC.md `
       04_DANHSACHHINHANH_BANGBIEU.md `
       05_TOMTAT.md `
       06_CHUONG1_TONGQUAN.md `
       07_CHUONG2_XACDINH_YEUCAU.md `
       08_CHUONG3_PHANTICH_YEUCAU.md `
       09_CHUONG4_THIETKE_HETHONG.md `
       10_CHUONG5_THIETKE_DOITUONG.md `
       11_CHUONG6_THIETKE_DULIEU.md `
       12_CHUONG7_THIETKE_GIAODIEN.md `
       13_CHUONG8_CAIDAT.md `
       14_CHUONG9_KIEMTHU.md `
       15_KETLUAN_TAILIEU.md `
       -o "BAO_CAO_HOAN_CHINH.docx" `
       --toc `
       --toc-depth=3 `
       --number-sections
```

### Tùy chỉnh style với Reference Document

```powershell
# Tạo reference.docx với style tùy chỉnh trước
# Sau đó dùng:
pandoc *.md -o BAO_CAO.docx --reference-doc=reference.docx
```

---

## Phương pháp 2: Sử dụng Python Script (Tự động hóa)

### Script chuyển đổi

```python
# convert_to_word.py
import os
import subprocess
from pathlib import Path

# Đường dẫn thư mục báo cáo
report_dir = Path(r"c:\Users\UDT4HC\Downloads\CNPM new\Project\QuanLyRaDeChamThi\BaoCao")

# Danh sách file theo thứ tự
files = [
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
    "15_KETLUAN_TAILIEU.md"
]

# Tạo đường dẫn đầy đủ
full_paths = [str(report_dir / f) for f in files]

# Output file
output_file = report_dir / "BAO_CAO_HOAN_CHINH.docx"

# Chạy pandoc
cmd = [
    "pandoc",
    *full_paths,
    "-o", str(output_file),
    "--toc",               # Table of Contents
    "--toc-depth=3",       # TOC depth
    "--number-sections",   # Đánh số chương
    "--highlight-style=tango"  # Syntax highlighting cho code
]

try:
    print("Đang chuyển đổi...")
    subprocess.run(cmd, check=True)
    print(f"✅ Chuyển đổi thành công!")
    print(f"📄 File output: {output_file}")
    print(f"📏 Kích thước: {output_file.stat().st_size / 1024:.2f} KB")
except subprocess.CalledProcessError as e:
    print(f"❌ Lỗi: {e}")
except FileNotFoundError:
    print("❌ Không tìm thấy Pandoc. Hãy cài đặt từ: https://pandoc.org/")
```

### Chạy script

```powershell
cd "c:\Users\UDT4HC\Downloads\CNPM new\Project\QuanLyRaDeChamThi"
python convert_to_word.py
```

---

## Phương pháp 3: Sử dụng Online Converter

### Các công cụ online miễn phí:

1. **Dillinger.io**
   - URL: https://dillinger.io/
   - Bước:
     1. Copy nội dung Markdown
     2. Paste vào editor
     3. Export as → Microsoft Word

2. **Markdown to Word**
   - URL: https://www.markdowntoword.com/
   - Bước:
     1. Upload file .md
     2. Click "Convert"
     3. Download .docx

3. **CloudConvert**
   - URL: https://cloudconvert.com/md-to-docx
   - Bước:
     1. Select files (có thể upload nhiều file)
     2. Convert MD to DOCX
     3. Download

---

## Phương pháp 4: Sử dụng VS Code Extension

### Cài đặt extension

1. Mở VS Code
2. Cài extension: **Markdown PDF**
3. Hoặc: **Markdown All in One**

### Sử dụng

```
1. Mở file .md trong VS Code
2. Ctrl+Shift+P → "Markdown: Export to Word"
3. Chọn vị trí lưu file
```

---

## Sau khi chuyển đổi: Chỉnh sửa trong Word

### Các bước chỉnh sửa:

1. **Thêm logo UIT:**
   - Insert → Pictures → Chọn logo
   - Đặt ở header/footer

2. **Chỉnh format:**
   - Heading 1: Arial 16pt, Bold, Màu xanh
   - Heading 2: Arial 14pt, Bold
   - Body text: Times New Roman 13pt
   - Line spacing: 1.5

3. **Thêm page numbers:**
   - Insert → Page Number
   - Format: Bottom center

4. **Tạo Table of Contents:**
   - References → Table of Contents
   - Chọn style Automatic

5. **Thêm header/footer:**
   - Insert → Header & Footer
   - Header: Tên đồ án
   - Footer: Số trang

6. **Chỉnh bảng biểu:**
   - Table Design → Table Style Medium 2
   - Autofit to Window

7. **Syntax highlighting cho code:**
   - Chọn code block
   - Font: Consolas 10pt
   - Shading: Light Gray

---

## Kiểm tra chất lượng

### Checklist trước khi nộp:

- [ ] Logo UIT đúng vị trí
- [ ] Trang bìa đầy đủ thông tin
- [ ] Mục lục tự động (có thể click)
- [ ] Đánh số trang đúng
- [ ] Hình ảnh rõ nét
- [ ] Bảng biểu format đẹp
- [ ] Code syntax highlighting
- [ ] Không có lỗi chính tả
- [ ] Font chữ thống nhất
- [ ] Line spacing 1.5
- [ ] Margin: Top/Bottom 2cm, Left 3cm, Right 2cm
- [ ] File size < 10MB

---

## Tips nâng cao

### 1. Tạo template Word chuẩn UIT

```powershell
# Tạo file reference.docx với:
# - Logo UIT trong header
# - Font Times New Roman 13pt
# - Heading styles đã định nghĩa
# - Page numbering format

# Sau đó dùng:
pandoc *.md -o output.docx --reference-doc=reference_uit.docx
```

### 2. Batch convert nhiều báo cáo

```powershell
# Script convert nhiều project
$projects = @("Project1", "Project2", "Project3")

foreach ($proj in $projects) {
    $dir = "C:\Projects\$proj\BaoCao"
    cd $dir
    pandoc *.md -o "$proj-Report.docx" --toc
    Write-Host "✅ Done: $proj"
}
```

### 3. Thêm watermark

```powershell
# Sử dụng VBA hoặc online tool
# hoặc: Insert → Watermark trong Word
```

---

## Troubleshooting

### Lỗi thường gặp:

**1. "pandoc: command not found"**
```powershell
# Giải pháp: Cài đặt Pandoc
choco install pandoc
# Hoặc tải từ: https://pandoc.org/
```

**2. Unicode/tiếng Việt bị lỗi**
```powershell
# Giải pháp: Thêm option
pandoc input.md -o output.docx --to=docx+native_numbering
```

**3. Bảng quá rộng**
```powershell
# Giải pháp: Chia bảng thành nhiều bảng nhỏ
# Hoặc xoay trang landscape trong Word
```

**4. Code block mất format**
```powershell
# Giải pháp:
pandoc input.md -o output.docx --highlight-style=tango
```

**5. Hình ảnh không hiển thị**
```powershell
# Giải pháo: Dùng đường dẫn tuyệt đối
pandoc input.md -o output.docx --resource-path="./images"
```

---

## Kết quả cuối cùng

Sau khi chuyển đổi và chỉnh sửa, bạn sẽ có:

✅ **BAO_CAO_HOAN_CHINH.docx** (~5-8MB)
   - 120+ trang
   - Có mục lục tự động
   - Format chuẩn UIT
   - Hình ảnh, bảng biểu đầy đủ
   - Syntax highlighting cho code
   - Header/footer đẹp
   - Sẵn sàng nộp hoặc in

---

## Câu hỏi thường gặp

**Q: Có cần cài Visual Studio không?**
A: Không, chỉ cần Pandoc hoặc online converter.

**Q: Mất bao lâu để convert?**
A: Pandoc: 5-10 giây. Online: 1-2 phút.

**Q: File Word có giữ được format Markdown không?**
A: Có, Pandoc chuyển đổi rất tốt (headings, tables, code blocks).

**Q: Có thể convert ngược Word → Markdown không?**
A: Có, dùng: `pandoc input.docx -o output.md`

**Q: Làm sao thêm cover page đẹp?**
A: Tạo file `cover.md` riêng với layout đẹp, hoặc thêm trong Word sau.

---

**Chúc bạn thành công! 📝✨**
