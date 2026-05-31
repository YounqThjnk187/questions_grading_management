using System.Linq;
using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;
using QuanLyRaDeChamThi.Models.ViewModels;

namespace QuanLyRaDeChamThi.Controllers
{
    public class BaoCaoController : Controller
    {
        private AppDB db = new AppDB();

        public ActionResult BaoCaoNam(string namHoc)
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

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}