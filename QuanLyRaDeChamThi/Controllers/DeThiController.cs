<<<<<<< HEAD:QuanLyRaDeChamThi/QuanLyRaDeChamThi/Controllers/DeThiController.cs
using System;
using System.Linq;
using System.Web.Mvc;
using System.Data.Entity;
using QuanLyRaDeChamThi.Models;
using QuanLyRaDeChamThi.Models.ViewModels;

namespace QuanLyRaDeChamThi.Controllers
{
    public class DeThiController : Controller
    {
        private AppDB db = new AppDB();

        private int GetMaGV() => Session["MaGV"] != null ? (int)Session["MaGV"] : 0;

        private ActionResult CheckLogin()
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            return null;
        }

        // GET: DeThi
        public ActionResult Index()
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var deThis = db.DeThis
                .Include(d => d.MonHoc)
                .Where(d => d.MaGV == maGV)
                .OrderByDescending(d => d.MaDT)
                .ToList();

            return View(deThis);
        }

        // GET: Create
        public ActionResult Create()
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var vm = new SoanDeThiViewModel
            {
                DanhSachMonHoc = db.MonHocs.Where(m => m.MaGV == maGV).ToList(),
                DanhSachDoKho = db.DoKhos.ToList(),
                NamHoc = DateTime.Now.Year + "-" + (DateTime.Now.Year + 1)
            };

            return View(vm);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(SoanDeThiViewModel vm)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            int soCauToiDa = GetThamSo("SoCauToiDa", 5);
            int thoiLuongMin = GetThamSo("ThoiLuongToiThieu", 30);
            int thoiLuongMax = GetThamSo("ThoiLuongToiDa", 180);

            if (vm.CauHoiDuocChon == null || vm.CauHoiDuocChon.Count == 0)
                ModelState.AddModelError("", "Vui lòng chọn ít nhất 1 câu hỏi.");

            if (vm.CauHoiDuocChon != null && vm.CauHoiDuocChon.Count > soCauToiDa)
                ModelState.AddModelError("", $"Không được vượt quá {soCauToiDa} câu hỏi.");

            if (vm.ThoiLuong < thoiLuongMin || vm.ThoiLuong > thoiLuongMax)
                ModelState.AddModelError("ThoiLuong",
                    $"Thời lượng từ {thoiLuongMin} - {thoiLuongMax} phút.");

            if (ModelState.IsValid)
            {
                var deThi = new DeThiModel
                {
                    MaMon = vm.MaMon,
                    HocKy = (byte)vm.HocKy,
                    NamHoc = vm.NamHoc,
                    ThoiLuong = vm.ThoiLuong,
                    NgayThi = vm.NgayThi,
                    MaGV = maGV
                };

                db.DeThis.Add(deThi);
                db.SaveChanges();

                if (vm.CauHoiDuocChon != null)
                {
                    foreach (var maCH in vm.CauHoiDuocChon)
                    {
                        db.CTDeThis.Add(new CTDeThiModel
                        {
                            MaDT = deThi.MaDT,
                            MaCH = maCH
                        });
                    }
                    db.SaveChanges();
                }

                TempData["Success"] = "Tạo đề thi thành công!";
                return RedirectToAction("Details", new { id = deThi.MaDT });
            }

            vm.DanhSachMonHoc = db.MonHocs.Where(m => m.MaGV == maGV).ToList();
            vm.DanhSachDoKho = db.DoKhos.ToList();

            if (vm.MaMon > 0)
            {
                vm.DanhSachCauHoi = db.CauHois
                    .Include(c => c.DoKho)
                    .Where(c => c.MaMon == vm.MaMon)
                    .ToList();
            }

            return View(vm);
        }

        // GET: Details
        public ActionResult Details(int id)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var deThi = db.DeThis
                .Include(d => d.MonHoc)
                .Include(d => d.CTDeThis.Select(ct => ct.CauHoi.DoKho))
                .FirstOrDefault(d => d.MaDT == id && d.MaGV == maGV);

            if (deThi == null) return HttpNotFound();

            return View(deThi);
        }

        // GET: TraCuu (FIXED - KHÔNG DÙNG DeThiTraCuuItem)
        public ActionResult TraCuu(string tenMon, int? hocKy, string namHoc)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var query = db.DeThis
                .Include(d => d.MonHoc)
                .Where(d => d.MaGV == maGV);

            if (!string.IsNullOrEmpty(tenMon))
                query = query.Where(d => d.MonHoc.TenMon.Contains(tenMon));

            if (hocKy.HasValue)
                query = query.Where(d => d.HocKy == hocKy.Value);

            if (!string.IsNullOrEmpty(namHoc))
                query = query.Where(d => d.NamHoc == namHoc);

            var result = query
                .OrderByDescending(d => d.MaDT)
                .ToList();

            ViewBag.TenMon = tenMon;
            ViewBag.HocKy = hocKy;
            ViewBag.NamHoc = namHoc;

            return View(result);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(int id)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var deThi = db.DeThis.FirstOrDefault(d => d.MaDT == id && d.MaGV == maGV);

            if (deThi != null)
            {
                db.DeThis.Remove(deThi);
                db.SaveChanges();
            }

            return RedirectToAction("Index");
        }

        private int GetThamSo(string ten, int defaultValue)
        {
            var ts = db.ThamSos.FirstOrDefault(t => t.TenThamSo == ten);
            return ts != null ? ts.GiaTri : defaultValue;
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
=======
using System;
using System.Linq;
using System.Web.Mvc;
using System.Data.Entity;
using QuanLyRaDeChamThi.Models;
using QuanLyRaDeChamThi.Models.ViewModels;

namespace QuanLyRaDeChamThi.Controllers
{
    public class DeThiController : Controller
    {
        private AppDB db = new AppDB();

        private int GetMaGV() => Session["MaGV"] != null ? (int)Session["MaGV"] : 0;

        private ActionResult CheckLogin()
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            return null;
        }

        // GET: DeThi
        public ActionResult Index()
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var deThis = db.DeThis
                .Include(d => d.MonHoc)
                .Where(d => d.MaGV == maGV)
                .OrderByDescending(d => d.MaDT)
                .ToList();

            return View(deThis);
        }

        // GET: Create
        public ActionResult Create()
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var vm = new SoanDeThiViewModel
            {
                DanhSachMonHoc = db.MonHocs.Where(m => m.MaGV == maGV).ToList(),
                DanhSachDoKho = db.DoKhos.ToList(),
                NamHoc = DateTime.Now.Year + "-" + (DateTime.Now.Year + 1)
            };

            return View(vm);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(SoanDeThiViewModel vm)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            int soCauToiDa = GetThamSo("SoCauToiDa", 5);
            int thoiLuongMin = GetThamSo("ThoiLuongToiThieu", 30);
            int thoiLuongMax = GetThamSo("ThoiLuongToiDa", 180);

            if (vm.CauHoiDuocChon == null || vm.CauHoiDuocChon.Count == 0)
                ModelState.AddModelError("", "Vui lòng chọn ít nhất 1 câu hỏi.");

            if (vm.CauHoiDuocChon != null && vm.CauHoiDuocChon.Count > soCauToiDa)
                ModelState.AddModelError("", $"Không được vượt quá {soCauToiDa} câu hỏi.");

            if (vm.ThoiLuong < thoiLuongMin || vm.ThoiLuong > thoiLuongMax)
                ModelState.AddModelError("ThoiLuong",
                    $"Thời lượng từ {thoiLuongMin} - {thoiLuongMax} phút.");

            if (ModelState.IsValid)
            {
                var deThi = new DeThiModel
                {
                    MaMon = vm.MaMon,
                    HocKy = (byte)vm.HocKy,
                    NamHoc = vm.NamHoc,
                    ThoiLuong = vm.ThoiLuong,
                    NgayThi = vm.NgayThi,
                    MaGV = maGV
                };

                db.DeThis.Add(deThi);
                db.SaveChanges();

                if (vm.CauHoiDuocChon != null)
                {
                    foreach (var maCH in vm.CauHoiDuocChon)
                    {
                        db.CTDeThis.Add(new CTDeThiModel
                        {
                            MaDT = deThi.MaDT,
                            MaCH = maCH
                        });
                    }
                    db.SaveChanges();
                }

                TempData["Success"] = "Tạo đề thi thành công!";
                return RedirectToAction("Details", new { id = deThi.MaDT });
            }

            vm.DanhSachMonHoc = db.MonHocs.Where(m => m.MaGV == maGV).ToList();
            vm.DanhSachDoKho = db.DoKhos.ToList();

            if (vm.MaMon > 0)
            {
                vm.DanhSachCauHoi = db.CauHois
                    .Include(c => c.DoKho)
                    .Where(c => c.MaMon == vm.MaMon)
                    .ToList();
            }

            return View(vm);
        }

        // GET: Details
        public ActionResult Details(int id)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var deThi = db.DeThis
                .Include(d => d.MonHoc)
                .Include(d => d.CTDeThis.Select(ct => ct.CauHoi.DoKho))
                .FirstOrDefault(d => d.MaDT == id && d.MaGV == maGV);

            if (deThi == null) return HttpNotFound();

            return View(deThi);
        }

        // GET: TraCuu (FIXED - KHÔNG DÙNG DeThiTraCuuItem)
        public ActionResult TraCuu(string tenMon, int? hocKy, string namHoc)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var query = db.DeThis
                .Include(d => d.MonHoc)
                .Where(d => d.MaGV == maGV);

            if (!string.IsNullOrEmpty(tenMon))
                query = query.Where(d => d.MonHoc.TenMon.Contains(tenMon));

            if (hocKy.HasValue)
                query = query.Where(d => d.HocKy == hocKy.Value);

            if (!string.IsNullOrEmpty(namHoc))
                query = query.Where(d => d.NamHoc == namHoc);

            var result = query
                .OrderByDescending(d => d.MaDT)
                .ToList();

            ViewBag.TenMon = tenMon;
            ViewBag.HocKy = hocKy;
            ViewBag.NamHoc = namHoc;

            return View(result);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(int id)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var deThi = db.DeThis.FirstOrDefault(d => d.MaDT == id && d.MaGV == maGV);

            if (deThi != null)
            {
                db.DeThis.Remove(deThi);
                db.SaveChanges();
            }

            return RedirectToAction("Index");
        }

        private int GetThamSo(string ten, int defaultValue)
        {
            var ts = db.ThamSos.FirstOrDefault(t => t.TenThamSo == ten);
            return ts != null ? ts.GiaTri : defaultValue;
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
>>>>>>> a546afd41e823ba8c7e40278b493716982ebbd39:QuanLyRaDeChamThi/Controllers/DeThiController.cs
}