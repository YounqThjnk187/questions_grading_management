using System.Linq;
using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;
using QuanLyRaDeChamThi.Models.ViewModels;

namespace QuanLyRaDeChamThi.Controllers
{
    public class BaoCaoController : Controller
    {
        private AppDB db = new AppDB();

        private int GetMaGV() => Session["MaGV"] != null ? (int)Session["MaGV"] : 0;

        private ActionResult CheckLogin()
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            return null;
        }

        // GET: BaoCao/BaoCaoNam
        public ActionResult BaoCaoNam(string namHoc)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            // Danh sách năm học có dữ liệu
            var danhSachNamHoc = db.DeThis
                .Where(d => d.MaGV == maGV)
                .Select(d => d.NamHoc)
                .Distinct()
                .OrderByDescending(n => n)
                .ToList();

            if (string.IsNullOrEmpty(namHoc) && danhSachNamHoc.Any())
                namHoc = danhSachNamHoc.First();

            var vm = new BaoCaoNamViewModel
            {
                NamHoc        = namHoc,
                DanhSachNamHoc = danhSachNamHoc
            };

            if (!string.IsNullOrEmpty(namHoc))
            {
                // Truy vấn thống kê phân loại điểm
                var deThis = db.DeThis.Include("MonHoc")
                    .Where(d => d.MaGV == maGV && d.NamHoc == namHoc)
                    .ToList();

                foreach (var dt in deThis)
                {
                    var ketQuas = db.KetQuas.Where(k => k.MaDT == dt.MaDT).ToList();
                    if (!ketQuas.Any()) continue;

                    vm.DanhSachBaoCao.Add(new BaoCaoMonHocItem
                    {
                        TenMon        = dt.MonHoc.TenMon,
                        HocKy         = dt.HocKy,
                        TongSinhVien  = ketQuas.Count,
                        SoA           = ketQuas.Count(k => k.DiemChu == "A"),
                        SoBPlus       = ketQuas.Count(k => k.DiemChu == "B+"),
                        SoB           = ketQuas.Count(k => k.DiemChu == "B"),
                        SoCPlus       = ketQuas.Count(k => k.DiemChu == "C+"),
                        SoC           = ketQuas.Count(k => k.DiemChu == "C"),
                        SoDPlus       = ketQuas.Count(k => k.DiemChu == "D+"),
                        SoD           = ketQuas.Count(k => k.DiemChu == "D"),
                        SoF           = ketQuas.Count(k => k.DiemChu == "F"),
                        DiemTrungBinh = ketQuas.Average(k => k.DiemSo)
                    });
                }

                vm.DanhSachBaoCao = vm.DanhSachBaoCao
                    .OrderBy(b => b.TenMon).ThenBy(b => b.HocKy).ToList();
            }

            return View(vm);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}
