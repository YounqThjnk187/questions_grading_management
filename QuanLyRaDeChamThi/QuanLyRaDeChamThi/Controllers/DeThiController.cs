using System;
using System.Collections.Generic;
using System.Linq;
using System.Web.Mvc;
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

        // GET: DeThi - Danh sách đề thi
        public ActionResult Index()
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var deThis = db.DeThis
                .Include("MonHoc")
                .Where(d => d.MaGV == maGV)
                .OrderByDescending(d => d.MaDT)
                .ToList();

            return View(deThis);
        }

        // GET: DeThi/Create - Form soạn đề thi
        public ActionResult Create()
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var vm = new SoanDeThiViewModel
            {
                DanhSachMonHoc = db.MonHocs.Where(m => m.MaGV == maGV).ToList(),
                DanhSachDoKho  = db.DoKhos.ToList(),
                NamHoc         = DateTime.Now.Year + "-" + (DateTime.Now.Year + 1)
            };
            return View(vm);
        }

        // POST: DeThi/GetCauHoi - Ajax lấy câu hỏi theo môn
        [HttpPost]
        public JsonResult GetCauHoiByMon(int maMon, int? maDoKho)
        {
            if (Session["MaGV"] == null)
                return Json(new { success = false });

            var query = db.CauHois.Include("DoKho").Where(c => c.MaMon == maMon);
            if (maDoKho.HasValue)
                query = query.Where(c => c.MaDoKho == maDoKho.Value);

            var cauHois = query.Select(c => new
            {
                c.MaCH,
                c.NoiDung,
                TenDoKho = c.DoKho.TenDoKho
            }).ToList();

            return Json(cauHois);
        }

        // POST: DeThi/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(SoanDeThiViewModel vm)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            // Kiểm tra tham số hệ thống
            int soCauToiDa    = GetThamSo("SoCauToiDa", 5);
            int thoiLuongMin  = GetThamSo("ThoiLuongToiThieu", 30);
            int thoiLuongMax  = GetThamSo("ThoiLuongToiDa", 180);

            // Validate
            if (vm.CauHoiDuocChon == null || vm.CauHoiDuocChon.Count == 0)
                ModelState.AddModelError("", "Vui lòng chọn ít nhất 1 câu hỏi.");

            if (vm.CauHoiDuocChon != null && vm.CauHoiDuocChon.Count > soCauToiDa)
                ModelState.AddModelError("", $"Số câu hỏi không được vượt quá {soCauToiDa} câu.");

            if (vm.ThoiLuong < thoiLuongMin || vm.ThoiLuong > thoiLuongMax)
                ModelState.AddModelError("ThoiLuong", $"Thời lượng phải từ {thoiLuongMin} đến {thoiLuongMax} phút.");

            if (ModelState.IsValid)
            {
                var deThi = new DeThiModel
                {
                    MaMon     = vm.MaMon,
                    HocKy     = vm.HocKy,
                    NamHoc    = vm.NamHoc,
                    ThoiLuong = vm.ThoiLuong,
                    NgayThi   = vm.NgayThi,
                    MaGV      = maGV
                };
                db.DeThis.Add(deThi);
                db.SaveChanges();

                // Thêm chi tiết đề thi
                foreach (var maCH in vm.CauHoiDuocChon)
                {
                    db.CTDeThis.Add(new CTDeThiModel { MaDT = deThi.MaDT, MaCH = maCH });
                }
                db.SaveChanges();

                TempData["Success"] = "Đề thi đã được tạo thành công!";
                return RedirectToAction("Details", new { id = deThi.MaDT });
            }

            // Reload dropdowns
            vm.DanhSachMonHoc = db.MonHocs.Where(m => m.MaGV == maGV).ToList();
            vm.DanhSachDoKho  = db.DoKhos.ToList();
            if (vm.MaMon > 0)
                vm.DanhSachCauHoi = db.CauHois.Include("DoKho").Where(c => c.MaMon == vm.MaMon).ToList();

            return View(vm);
        }

        // GET: DeThi/Details/5
        public ActionResult Details(int id)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var deThi = db.DeThis
                .Include("MonHoc")
                .Include("CTDeThis")
                .FirstOrDefault(d => d.MaDT == id && d.MaGV == maGV);
            if (deThi == null) return HttpNotFound();

            // Load câu hỏi trong đề
            foreach (var ct in deThi.CTDeThis)
            {
                db.Entry(ct).Reference("CauHoi").Load();
                db.Entry(ct.CauHoi).Reference("DoKho").Load();
            }

            return View(deThi);
        }

        // GET: DeThi/TraCuu - Tra cứu đề thi
        public ActionResult TraCuu(string tenMon, int? hocKy, string namHoc)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var query = db.DeThis.Include("MonHoc")
                .Where(d => d.MaGV == maGV);

            if (!string.IsNullOrEmpty(tenMon))
                query = query.Where(d => d.MonHoc.TenMon.Contains(tenMon));
            if (hocKy.HasValue)
                query = query.Where(d => d.HocKy == hocKy.Value);
            if (!string.IsNullOrEmpty(namHoc))
                query = query.Where(d => d.NamHoc == namHoc);

            ViewBag.TenMon  = tenMon;
            ViewBag.HocKy   = hocKy;
            ViewBag.NamHoc  = namHoc;
            ViewBag.DanhSachNamHoc = db.DeThis.Where(d => d.MaGV == maGV)
                .Select(d => d.NamHoc).Distinct().ToList();

            return View(query.OrderByDescending(d => d.MaDT).ToList());
        }

        // POST: DeThi/Delete/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Delete(int id)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var deThi = db.DeThis.FirstOrDefault(d => d.MaDT == id && d.MaGV == maGV);
            if (deThi != null)
            {
                db.DeThis.Remove(deThi);
                db.SaveChanges();
                TempData["Success"] = "Đề thi đã được xóa!";
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
}
