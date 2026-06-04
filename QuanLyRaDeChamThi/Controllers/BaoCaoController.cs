using System.Linq;
using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;
using QuanLyRaDeChamThi.Models.ViewModels;
using System.Text;
using System.Collections.Generic;

namespace QuanLyRaDeChamThi.Controllers
{
    public class BaoCaoController : Controller
    {
        private AppDB db = new AppDB();

        public ActionResult BaoCaoNam(string namHoc)
        {
            // Lấy danh sách năm học
            var namHocs = db.DeThis
                .Select(x => x.NamHoc)
                .Distinct()
                .OrderByDescending(x => x)
                .ToList();

            ViewBag.NamHocs = namHocs;

            var query = from kq in db.KetQuas
                        join dt in db.DeThis on kq.MaDT equals dt.MaDT
                        join mh in db.MonHocs on dt.MaMon equals mh.MaMon
                        where string.IsNullOrEmpty(namHoc) || dt.NamHoc == namHoc
                        select new
                        {
                            TenMon = mh.TenMon,
                            HocKy = dt.HocKy,
                            NamHoc = dt.NamHoc,
                            Diem = kq.DiemSo
                        };

            var data = query.ToList();

            var grouped = data
                .GroupBy(x => new { x.TenMon, x.HocKy, x.NamHoc })
                .Select(g => new BaoCaoMonHocItem
                {
                    TenMon = g.Key.TenMon,
                    HocKy = g.Key.HocKy,

                    TongSinhVien = g.Count(),

                    SoA = g.Count(x => x.Diem >= 8.5m),
                    SoBPlus = g.Count(x => x.Diem >= 8.0m && x.Diem < 8.5m),
                    SoB = g.Count(x => x.Diem >= 7.0m && x.Diem < 8.0m),
                    SoCPlus = g.Count(x => x.Diem >= 6.5m && x.Diem < 7.0m),
                    SoC = g.Count(x => x.Diem >= 5.5m && x.Diem < 6.5m),
                    SoDPlus = g.Count(x => x.Diem >= 5.0m && x.Diem < 5.5m),
                    SoD = g.Count(x => x.Diem >= 4.0m && x.Diem < 5.0m),
                    SoF = g.Count(x => x.Diem < 4.0m),

                    DiemTrungBinh = g.Any() ? g.Average(x => x.Diem) : 0
                })
                .ToList();

            var model = new BaoCaoNamViewModel
            {
                NamHoc = namHoc ?? "Tất cả",
                DanhSachBaoCao = grouped
            };

            return View(model);
        }

        public ActionResult ExportExcel(string namHoc)
        {
            var query = from kq in db.KetQuas
                        join dt in db.DeThis on kq.MaDT equals dt.MaDT
                        join mh in db.MonHocs on dt.MaMon equals mh.MaMon
                        where string.IsNullOrEmpty(namHoc) || dt.NamHoc == namHoc
                        select new
                        {
                            TenMon = mh.TenMon,
                            HocKy = dt.HocKy,
                            NamHoc = dt.NamHoc,
                            Diem = kq.DiemSo
                        };

            var data = query.ToList();

            var grouped = data
                .GroupBy(x => new { x.TenMon, x.HocKy, x.NamHoc })
                .Select(g => new
                {
                    TenMon = g.Key.TenMon,
                    HocKy = g.Key.HocKy,
                    NamHoc = g.Key.NamHoc,
                    TongSV = g.Count(),
                    DiemTB = g.Average(x => x.Diem),
                    SoA = g.Count(x => x.Diem >= 8.5m),
                    SoBPlus = g.Count(x => x.Diem >= 8.0m && x.Diem < 8.5m),
                    SoB = g.Count(x => x.Diem >= 7.0m && x.Diem < 8.0m),
                    SoCPlus = g.Count(x => x.Diem >= 6.5m && x.Diem < 7.0m),
                    SoC = g.Count(x => x.Diem >= 5.5m && x.Diem < 6.5m),
                    SoDPlus = g.Count(x => x.Diem >= 5.0m && x.Diem < 5.5m),
                    SoD = g.Count(x => x.Diem >= 4.0m && x.Diem < 5.0m),
                    SoF = g.Count(x => x.Diem < 4.0m)
                })
                .OrderBy(x => x.NamHoc)
                .ThenBy(x => x.HocKy)
                .ThenBy(x => x.TenMon)
                .ToList();

            // Tính thống kê tổng quan
            var tongSinhVien = grouped.Sum(x => x.TongSV);
            var diemTBChung = grouped.Any() ? grouped.Average(x => x.DiemTB) : 0;
            var tongA = grouped.Sum(x => x.SoA);
            var tongBPlus = grouped.Sum(x => x.SoBPlus);
            var tongB = grouped.Sum(x => x.SoB);
            var tongCPlus = grouped.Sum(x => x.SoCPlus);
            var tongC = grouped.Sum(x => x.SoC);
            var tongDPlus = grouped.Sum(x => x.SoDPlus);
            var tongD = grouped.Sum(x => x.SoD);
            var tongF = grouped.Sum(x => x.SoF);
            var tongDau = tongSinhVien - tongF;
            var tiLeDauChung = tongSinhVien > 0 ? (decimal)tongDau / tongSinhVien * 100 : 0;

            // Xây dựng bảng chi tiết cho Excel
            var detailRows = new StringBuilder();
            int stt = 1;
            foreach (var item in grouped)
            {
                decimal tiLeDao = item.TongSV > 0 ? (decimal)(item.TongSV - item.SoF) / item.TongSV * 100 : 0;
                string xepLoai, rowBg, rowColor;
                
                // Xếp loại và màu sắc
                if (tiLeDao >= 90 && item.DiemTB >= 7.5m)
                {
                    xepLoai = "Xuất sắc"; rowBg = "#C6EFCE"; rowColor = "#006100";
                }
                else if (tiLeDao >= 85 && item.DiemTB >= 7.0m)
                {
                    xepLoai = "Tốt"; rowBg = "#BDD7EE"; rowColor = "#0066CC";
                }
                else if (tiLeDao >= 75 && item.DiemTB >= 6.0m)
                {
                    xepLoai = "Khá"; rowBg = "#FFF2CC"; rowColor = "#CC9900";
                }
                else if (tiLeDao >= 60 && item.DiemTB >= 5.0m)
                {
                    xepLoai = "Trung bình"; rowBg = "#F2F2F2"; rowColor = "#666666";
                }
                else
                {
                    xepLoai = "Cần cải thiện"; rowBg = "#FFC7CE"; rowColor = "#CC0000";
                }
                
                detailRows.AppendLine($@"
    <tr>
      <td style=""border: 1px solid #000; text-align: center; background-color: {rowBg}; color: {rowColor}; font-weight: bold;"">{stt}</td>
      <td style=""border: 1px solid #000; padding-left: 10px; background-color: {rowBg}; color: {rowColor}; font-weight: bold;"">{item.TenMon}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: {rowBg}; color: {rowColor};"">{item.HocKy}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: {rowBg}; color: {rowColor};"">{item.NamHoc}</td>
      <td style=""border: 1px solid #000; text-align: center; font-weight: bold; background-color: {rowBg}; color: {rowColor};"">{item.TongSV}</td>
      <td style=""border: 1px solid #000; text-align: center; font-weight: bold; background-color: {rowBg}; color: {rowColor};"">{item.DiemTB:F2}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: #C6EFCE; color: #006100; font-weight: bold;"">{item.SoA}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: #C6EFCE; color: #006100;"">{item.SoBPlus}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: #D9EAD3; color: #38761D;"">{item.SoB}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: #FFF2CC; color: #CC9900;"">{item.SoCPlus}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: #FCE5CD; color: #E69138;"">{item.SoC}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: #F4CCCC; color: #CC0000;"">{item.SoDPlus}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: #EA9999; color: #990000;"">{item.SoD}</td>
      <td style=""border: 1px solid #000; text-align: center; background-color: #CC0000; color: white; font-weight: bold;"">{item.SoF}</td>
      <td style=""border: 1px solid #000; text-align: center; font-weight: bold; background-color: {rowBg}; color: {rowColor};"">{tiLeDao:F1}%</td>
      <td style=""border: 1px solid #000; text-align: center; font-weight: bold; background-color: {rowBg}; color: {rowColor};"">{xepLoai}</td>
    </tr>");
                stt++;
            }

            // Tạo HTML với format Excel-compatible
            var excelHtml = $@"<html xmlns:o=""urn:schemas-microsoft-com:office:office""
xmlns:x=""urn:schemas-microsoft-com:office:excel""
xmlns=""http://www.w3.org/TR/REC-html40"">
<head>
  <meta http-equiv=""Content-Type"" content=""text/html; charset=utf-8"">
  <meta name=""ProgId"" content=""Excel.Sheet"">
  <meta name=""Generator"" content=""Microsoft Excel 15"">
  <style>
    table {{ border-collapse: collapse; font-family: Calibri, Arial, sans-serif; font-size: 11pt; }}
    th {{ border: 2px solid #000; background-color: #4472C4; color: white; font-weight: bold; text-align: center; padding: 8px; font-size: 11pt; }}
    td {{ border: 1px solid #000; padding: 5px; font-size: 11pt; }}
    .header-cell {{ background-color: #4472C4; color: white; font-weight: bold; font-size: 14pt; text-align: center; padding: 15px; border: 2px solid #000; }}
    .section-header {{ background-color: #305496; color: white; font-weight: bold; font-size: 12pt; text-align: center; padding: 10px; border: 2px solid #000; }}
    .label-cell {{ background-color: #D9E1F2; font-weight: bold; border: 1px solid #000; padding: 5px; }}
    .value-cell {{ text-align: center; font-weight: bold; border: 1px solid #000; padding: 5px; }}
  </style>
</head>
<body>
  <table>
    <tr><td colspan=""16"" class=""header-cell"">BÁO CÁO THỐNG KÊ THÀNH TÍCH HỌC TẬP<br>NĂM HỌC: {namHoc ?? "Tất cả"}</td></tr>
    <tr>
      <td colspan=""8"" style=""border: 1px solid #000; padding: 5px;""><b>Ngày xuất:</b> {System.DateTime.Now:dd/MM/yyyy HH:mm:ss}</td>
      <td colspan=""8"" style=""border: 1px solid #000; padding: 5px;""><b>Người xuất:</b> {Session["TenDangNhap"] ?? "Admin"}</td>
    </tr>
    <tr><td colspan=""16"" style=""height: 10px; border: none;""></td></tr>
    
    <tr><td colspan=""16"" class=""section-header"">THỐNG KÊ TỔNG QUAN</td></tr>
    <tr>
      <td colspan=""4"" class=""label-cell"">Tổng số sinh viên:</td>
      <td colspan=""3"" class=""value-cell"" style=""background-color: #E7E6E6;"">{tongSinhVien}</td>
      <td colspan=""3"" class=""label-cell"">Điểm TB chung:</td>
      <td colspan=""3"" class=""value-cell"" style=""background-color: #E7E6E6;"">{diemTBChung:F2}</td>
      <td colspan=""3"" style=""border: 1px solid #000;""></td>
    </tr>
    <tr>
      <td colspan=""4"" class=""label-cell"">Tỉ lệ đậu:</td>
      <td colspan=""3"" class=""value-cell"" style=""background-color: #C6EFCE; color: #006100; font-weight: bold;"">{tiLeDauChung:F1}%</td>
      <td colspan=""3"" class=""label-cell"">Tỉ lệ rớt:</td>
      <td colspan=""3"" class=""value-cell"" style=""background-color: #FFC7CE; color: #CC0000; font-weight: bold;"">{(100 - tiLeDauChung):F1}%</td>
      <td colspan=""3"" style=""border: 1px solid #000;""></td>
    </tr>
    <tr><td colspan=""16"" style=""height: 5px; border: none;""></td></tr>
    
    <tr><td colspan=""16"" class=""section-header"">PHÂN BỐ ĐIỂM CHỮ</td></tr>
    <tr>
      <td colspan=""2"" class=""label-cell"">A (≥8.5)</td>
      <td colspan=""2"" class=""label-cell"">B+ (8.0-8.4)</td>
      <td colspan=""2"" class=""label-cell"">B (7.0-7.9)</td>
      <td colspan=""2"" class=""label-cell"">C+ (6.5-6.9)</td>
      <td colspan=""2"" class=""label-cell"">C (5.5-6.4)</td>
      <td colspan=""2"" class=""label-cell"">D+ (5.0-5.4)</td>
      <td colspan=""2"" class=""label-cell"">D (4.0-4.9)</td>
      <td colspan=""2"" class=""label-cell"">F (<4.0)</td>
    </tr>
    <tr>
      <td colspan=""2"" style=""border: 1px solid #000; text-align: center; background-color: #C6EFCE; color: #006100; font-weight: bold; font-size: 14pt;"">{tongA}</td>
      <td colspan=""2"" style=""border: 1px solid #000; text-align: center; background-color: #C6EFCE; color: #006100; font-weight: bold; font-size: 14pt;"">{tongBPlus}</td>
      <td colspan=""2"" style=""border: 1px solid #000; text-align: center; background-color: #D9EAD3; color: #38761D; font-weight: bold; font-size: 14pt;"">{tongB}</td>
      <td colspan=""2"" style=""border: 1px solid #000; text-align: center; background-color: #FFF2CC; color: #CC9900; font-weight: bold; font-size: 14pt;"">{tongCPlus}</td>
      <td colspan=""2"" style=""border: 1px solid #000; text-align: center; background-color: #FCE5CD; color: #E69138; font-weight: bold; font-size: 14pt;"">{tongC}</td>
      <td colspan=""2"" style=""border: 1px solid #000; text-align: center; background-color: #F4CCCC; color: #CC0000; font-weight: bold; font-size: 14pt;"">{tongDPlus}</td>
      <td colspan=""2"" style=""border: 1px solid #000; text-align: center; background-color: #EA9999; color: #990000; font-weight: bold; font-size: 14pt;"">{tongD}</td>
      <td colspan=""2"" style=""border: 1px solid #000; text-align: center; background-color: #CC0000; color: white; font-weight: bold; font-size: 14pt;"">{tongF}</td>
    </tr>
    <tr><td colspan=""16"" style=""height: 10px; border: none;""></td></tr>
    
    <tr><td colspan=""16"" class=""section-header"">CHI TIẾT THEO MÔN HỌC VÀ HỌC KỲ</td></tr>
    <tr>
      <th style=""width: 40px;"">STT</th>
      <th style=""width: 200px;"">Môn học</th>
      <th style=""width: 60px;"">HK</th>
      <th style=""width: 90px;"">Năm học</th>
      <th style=""width: 70px;"">Tổng SV</th>
      <th style=""width: 70px;"">Điểm TB</th>
      <th style=""width: 60px;"">A<br>(≥8.5)</th>
      <th style=""width: 60px;"">B+<br>(8.0)</th>
      <th style=""width: 60px;"">B<br>(7.0)</th>
      <th style=""width: 60px;"">C+<br>(6.5)</th>
      <th style=""width: 60px;"">C<br>(5.5)</th>
      <th style=""width: 60px;"">D+<br>(5.0)</th>
      <th style=""width: 60px;"">D<br>(4.0)</th>
      <th style=""width: 60px;"">F<br>(<4.0)</th>
      <th style=""width: 80px;"">Tỉ lệ đỗ</th>
      <th style=""width: 120px;"">Xếp loại</th>
    </tr>
{detailRows}
    <tr><td colspan=""16"" style=""height: 10px; border: none;""></td></tr>
    
    <tr>
      <td colspan=""16"" style=""border: 1px solid #000; padding: 10px; background-color: #F2F2F2;"">
        <b>CHÚ THÍCH:</b><br>
        • Xếp loại Xuất sắc: Tỉ lệ đỗ ≥90% và Điểm TB ≥7.5<br>
        • Xếp loại Tốt: Tỉ lệ đỗ ≥85% và Điểm TB ≥7.0<br>
        • Xếp loại Khá: Tỉ lệ đỗ ≥75% và Điểm TB ≥6.0<br>
        • Xếp loại Trung bình: Tỉ lệ đỗ ≥60% và Điểm TB ≥5.0<br>
        • Màu sắc: Xanh (tốt) → Vàng (trung bình) → Đỏ (yếu/kém)
      </td>
    </tr>
    <tr>
      <td colspan=""16"" style=""border: 1px solid #000; text-align: center; padding: 5px; background-color: #E7E6E6; font-style: italic;"">
        Báo cáo được tạo tự động bởi Hệ thống Quản lý Ra đề và Chấm thi v1.0 | © 2026 Nhóm 15 - SE104.Q23
      </td>
    </tr>
  </table>
</body>
</html>";

            var fileName = $"BaoCao_NamHoc_{namHoc ?? "TatCa"}_{System.DateTime.Now:yyyyMMdd_HHmmss}.xlsx";
            
            // Thêm UTF-8 BOM để Excel hiển thị tiếng Việt đúng
            var excelBytes = Encoding.UTF8.GetBytes("\ufeff" + excelHtml);
            
            return File(excelBytes, "application/vnd.ms-excel", fileName);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}