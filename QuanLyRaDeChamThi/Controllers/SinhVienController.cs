using System;
using System.Linq;
using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;

namespace QuanLyRaDeChamThi.Controllers
{
    public class SinhVienController : Controller
    {
        private AppDB db = new AppDB();

        // GET: SinhVien
        public ActionResult Index()
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            var sinhViens = db.SINH_VIEN
                .Select(s => new
                {
                    s.MaSV,
                    s.HoTen,
                    s.NgaySinh,
                    TenLop = db.LOP_HOC.Where(l => l.MaLop == s.MaLop).Select(l => l.TenLop).FirstOrDefault()
                })
                .OrderBy(s => s.HoTen)
                .ToList();

            ViewBag.TotalCount = sinhViens.Count;
            return View(sinhViens);
        }

        // GET: SinhVien/Create
        public ActionResult Create()
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            ViewBag.LopHocs = db.LOP_HOC.OrderBy(l => l.TenLop).ToList();
            return View();
        }

        // POST: SinhVien/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(SinhVienModel model)
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            if (string.IsNullOrWhiteSpace(model.HoTen) || model.MaLop == null)
            {
                TempData["Error"] = "❌ Vui lòng điền đầy đủ thông tin!";
                ViewBag.LopHocs = db.LOP_HOC.OrderBy(l => l.TenLop).ToList();
                return View(model);
            }

            db.SINH_VIEN.Add(model);
            db.SaveChanges();

            TempData["Success"] = $"✅ Đã thêm sinh viên '{model.HoTen}' thành công!";
            return RedirectToAction("Index");
        }

        // GET: SinhVien/Edit/5
        public ActionResult Edit(int id)
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            var sinhVien = db.SINH_VIEN.Find(id);
            if (sinhVien == null) return HttpNotFound();

            ViewBag.LopHocs = db.LOP_HOC.OrderBy(l => l.TenLop).ToList();
            return View(sinhVien);
        }

        // POST: SinhVien/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(SinhVienModel model)
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            if (string.IsNullOrWhiteSpace(model.HoTen) || model.MaLop == null)
            {
                TempData["Error"] = "❌ Vui lòng điền đầy đủ thông tin!";
                ViewBag.LopHocs = db.LOP_HOC.OrderBy(l => l.TenLop).ToList();
                return View(model);
            }

            var sinhVien = db.SINH_VIEN.Find(model.MaSV);
            if (sinhVien == null) return HttpNotFound();

            sinhVien.HoTen = model.HoTen;
            sinhVien.NgaySinh = model.NgaySinh;
            sinhVien.MaLop = model.MaLop;
            db.SaveChanges();

            TempData["Success"] = $"✅ Đã cập nhật sinh viên '{model.HoTen}' thành công!";
            return RedirectToAction("Index");
        }

        // GET: SinhVien/Delete/5
        public ActionResult Delete(int id)
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            var sinhVien = db.SINH_VIEN.Find(id);
            if (sinhVien == null) return HttpNotFound();

            // Kiểm tra có kết quả thi không
            var hasKetQua = db.KET_QUA.Any(k => k.MaSV == id);
            if (hasKetQua)
            {
                var count = db.KET_QUA.Count(k => k.MaSV == id);
                TempData["Error"] = $"❌ Không thể xóa! Sinh viên đã có {count} kết quả thi.";
                return RedirectToAction("Index");
            }

            db.SINH_VIEN.Remove(sinhVien);
            db.SaveChanges();

            TempData["Success"] = $"✅ Đã xóa sinh viên '{sinhVien.HoTen}' thành công!";
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}
