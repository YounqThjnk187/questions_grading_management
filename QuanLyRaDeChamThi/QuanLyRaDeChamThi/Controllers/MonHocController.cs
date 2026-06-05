using System;
using System.Linq;
using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;

namespace QuanLyRaDeChamThi.Controllers
{
    public class MonHocController : Controller
    {
        private AppDB db = new AppDB();

        // GET: MonHoc
        public ActionResult Index()
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            var monHocs = db.MON_HOC
                .Select(m => new
                {
                    m.MaMon,
                    m.TenMon,
                    GiangVien = db.GIANG_VIEN.Where(g => g.MaGV == m.MaGV).Select(g => g.HoTen).FirstOrDefault()
                })
                .OrderBy(m => m.TenMon)
                .ToList();

            return View(monHocs);
        }

        // GET: MonHoc/Create
        public ActionResult Create()
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            ViewBag.GiangViens = db.GIANG_VIEN.OrderBy(g => g.HoTen).ToList();
            return View();
        }

        // POST: MonHoc/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(MonHocModel model)
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            if (string.IsNullOrWhiteSpace(model.TenMon))
            {
                TempData["Error"] = "❌ Vui lòng nhập tên môn học!";
                ViewBag.GiangViens = db.GIANG_VIEN.OrderBy(g => g.HoTen).ToList();
                return View(model);
            }

            // Kiểm tra trùng tên
            var exists = db.MON_HOC.Any(m => m.TenMon == model.TenMon);
            if (exists)
            {
                TempData["Error"] = $"❌ Môn học '{model.TenMon}' đã tồn tại!";
                ViewBag.GiangViens = db.GIANG_VIEN.OrderBy(g => g.HoTen).ToList();
                return View(model);
            }

            db.MON_HOC.Add(model);
            db.SaveChanges();

            TempData["Success"] = $"✅ Đã thêm môn học '{model.TenMon}' thành công!";
            return RedirectToAction("Index");
        }

        // GET: MonHoc/Edit/5
        public ActionResult Edit(int id)
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            var monHoc = db.MON_HOC.Find(id);
            if (monHoc == null) return HttpNotFound();

            ViewBag.GiangViens = db.GIANG_VIEN.OrderBy(g => g.HoTen).ToList();
            return View(monHoc);
        }

        // POST: MonHoc/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(MonHocModel model)
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            if (string.IsNullOrWhiteSpace(model.TenMon))
            {
                TempData["Error"] = "❌ Vui lòng nhập tên môn học!";
                ViewBag.GiangViens = db.GIANG_VIEN.OrderBy(g => g.HoTen).ToList();
                return View(model);
            }

            // Kiểm tra trùng tên (trừ chính nó)
            var exists = db.MON_HOC.Any(m => m.TenMon == model.TenMon && m.MaMon != model.MaMon);
            if (exists)
            {
                TempData["Error"] = $"❌ Môn học '{model.TenMon}' đã tồn tại!";
                ViewBag.GiangViens = db.GIANG_VIEN.OrderBy(g => g.HoTen).ToList();
                return View(model);
            }

            var monHoc = db.MON_HOC.Find(model.MaMon);
            if (monHoc == null) return HttpNotFound();

            monHoc.TenMon = model.TenMon;
            monHoc.MaGV = model.MaGV;
            db.SaveChanges();

            TempData["Success"] = $"✅ Đã cập nhật môn học '{model.TenMon}' thành công!";
            return RedirectToAction("Index");
        }

        // GET: MonHoc/Delete/5
        public ActionResult Delete(int id)
        {
            if (Session["MaGV"] == null) return RedirectToAction("Login", "Account");

            var monHoc = db.MON_HOC.Find(id);
            if (monHoc == null) return HttpNotFound();

            // Kiểm tra có câu hỏi hoặc đề thi không
            var hasCauHoi = db.CAU_HOI.Any(c => c.MaMon == id);
            var hasDeThi = db.DE_THI.Any(d => d.MaMon == id);

            if (hasCauHoi || hasDeThi)
            {
                var countCH = db.CAU_HOI.Count(c => c.MaMon == id);
                var countDT = db.DE_THI.Count(d => d.MaMon == id);
                TempData["Error"] = $"❌ Không thể xóa! Môn học đang có {countCH} câu hỏi và {countDT} đề thi.";
                return RedirectToAction("Index");
            }

            db.MON_HOC.Remove(monHoc);
            db.SaveChanges();

            TempData["Success"] = $"✅ Đã xóa môn học '{monHoc.TenMon}' thành công!";
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}
