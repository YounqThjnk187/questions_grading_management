using System.Linq;
using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;

namespace QuanLyRaDeChamThi.Controllers
{
    public class CauHoiController : Controller
    {
        private AppDB db = new AppDB();

        private int GetMaGV()
        {
            return Session["MaGV"] != null ? (int)Session["MaGV"] : 0;
        }

        private ActionResult CheckLogin()
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            return null;
        }

        // GET: CauHoi - danh sách câu hỏi của giảng viên hiện tại
        public ActionResult Index(int? maMonFilter, int? maDoKhoFilter)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var query = db.CauHois
                .Include("MonHoc")
                .Include("DoKho")
                .Where(c => c.MonHoc.MaGV == maGV);

            if (maMonFilter.HasValue)
                query = query.Where(c => c.MaMon == maMonFilter.Value);
            if (maDoKhoFilter.HasValue)
                query = query.Where(c => c.MaDoKho == maDoKhoFilter.Value);

            ViewBag.DanhSachMon   = db.MonHocs.Where(m => m.MaGV == maGV).ToList();
            ViewBag.DanhSachDoKho = db.DoKhos.ToList();
            ViewBag.MaMonFilter   = maMonFilter;
            ViewBag.MaDoKhoFilter = maDoKhoFilter;

            return View(query.ToList());
        }

        // GET: CauHoi/Create
        public ActionResult Create()
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();
            ViewBag.DanhSachMon   = new SelectList(db.MonHocs.Where(m => m.MaGV == maGV), "MaMon", "TenMon");
            ViewBag.DanhSachDoKho = new SelectList(db.DoKhos, "MaDoKho", "TenDoKho");
            return View(new CauHoiModel());
        }

        // POST: CauHoi/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(CauHoiModel model)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            if (ModelState.IsValid)
            {
                db.CauHois.Add(model);
                db.SaveChanges();
                TempData["Success"] = "Câu hỏi đã được thêm thành công!";
                return RedirectToAction("Index");
            }

            ViewBag.DanhSachMon   = new SelectList(db.MonHocs.Where(m => m.MaGV == maGV), "MaMon", "TenMon", model.MaMon);
            ViewBag.DanhSachDoKho = new SelectList(db.DoKhos, "MaDoKho", "TenDoKho", model.MaDoKho);
            return View(model);
        }

        // GET: CauHoi/Edit/5
        public ActionResult Edit(int id)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var cauHoi = db.CauHois.Include("MonHoc").FirstOrDefault(c => c.MaCH == id && c.MonHoc.MaGV == maGV);
            if (cauHoi == null) return HttpNotFound();

            ViewBag.DanhSachMon   = new SelectList(db.MonHocs.Where(m => m.MaGV == maGV), "MaMon", "TenMon", cauHoi.MaMon);
            ViewBag.DanhSachDoKho = new SelectList(db.DoKhos, "MaDoKho", "TenDoKho", cauHoi.MaDoKho);
            return View(cauHoi);
        }

        // POST: CauHoi/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(CauHoiModel model)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            if (ModelState.IsValid)
            {
                db.Entry(model).State = System.Data.Entity.EntityState.Modified;
                db.SaveChanges();
                TempData["Success"] = "Câu hỏi đã được cập nhật!";
                return RedirectToAction("Index");
            }

            ViewBag.DanhSachMon   = new SelectList(db.MonHocs.Where(m => m.MaGV == maGV), "MaMon", "TenMon", model.MaMon);
            ViewBag.DanhSachDoKho = new SelectList(db.DoKhos, "MaDoKho", "TenDoKho", model.MaDoKho);
            return View(model);
        }

        // GET: CauHoi/Delete/5
        public ActionResult Delete(int id)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var cauHoi = db.CauHois.Include("MonHoc").Include("DoKho")
                .FirstOrDefault(c => c.MaCH == id && c.MonHoc.MaGV == maGV);
            if (cauHoi == null) return HttpNotFound();
            return View(cauHoi);
        }

        // POST: CauHoi/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            var check = CheckLogin(); if (check != null) return check;

            var cauHoi = db.CauHois.Find(id);
            if (cauHoi != null)
            {
                db.CauHois.Remove(cauHoi);
                db.SaveChanges();
                TempData["Success"] = "Câu hỏi đã được xóa!";
            }
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}
