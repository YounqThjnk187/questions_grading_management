using System.Linq;
using System.Web.Mvc;
using System.Data.Entity;
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

        // GET: CauHoi
        public ActionResult Index(int? maMonFilter, int? maDoKhoFilter)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            // ✅ FIX QUAN TRỌNG: Include bằng LINQ chuẩn
            var query = db.CauHois
                .Include(c => c.MonHoc)
                .Include(c => c.DoKho)
                .Where(c => c.MonHoc.MaGV == maGV);

            // filter
            if (maMonFilter.HasValue)
                query = query.Where(c => c.MaMon == maMonFilter.Value);

            if (maDoKhoFilter.HasValue)
                query = query.Where(c => c.MaDoKho == maDoKhoFilter.Value);

            // dropdown data
            ViewBag.DanhSachMon = db.MonHocs
                .Where(m => m.MaGV == maGV)
                .ToList();

            ViewBag.DanhSachDoKho = db.DoKhos.ToList();

            ViewBag.MaMonFilter = maMonFilter;
            ViewBag.MaDoKhoFilter = maDoKhoFilter;

            // ⚠️ FIX QUAN TRỌNG: materialize sau include
            var result = query.ToList();

            return View(result);
        }

        // GET: Create
        public ActionResult Create()
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            ViewBag.DanhSachMon = new SelectList(
                db.MonHocs.Where(m => m.MaGV == maGV),
                "MaMon",
                "TenMon"
            );

            ViewBag.DanhSachDoKho = new SelectList(
                db.DoKhos,
                "MaDoKho",
                "TenDoKho"
            );

            return View(new CauHoiModel());
        }

        // POST: Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(CauHoiModel model)
        {
            var check = CheckLogin();
            if (check != null) return check;

            if (ModelState.IsValid)
            {
                db.CauHois.Add(model);
                db.SaveChanges();

                TempData["Success"] = "Thêm câu hỏi thành công!";
                return RedirectToAction("Index");
            }

            int maGV = GetMaGV();

            ViewBag.DanhSachMon = new SelectList(
                db.MonHocs.Where(m => m.MaGV == maGV),
                "MaMon",
                "TenMon",
                model.MaMon
            );

            ViewBag.DanhSachDoKho = new SelectList(
                db.DoKhos,
                "MaDoKho",
                "TenDoKho",
                model.MaDoKho
            );

            return View(model);
        }

        // GET: Edit
        public ActionResult Edit(int id)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var cauHoi = db.CauHois
                .Include(c => c.MonHoc)
                .Include(c => c.DoKho)
                .FirstOrDefault(c => c.MaCH == id && c.MonHoc.MaGV == maGV);

            if (cauHoi == null) return HttpNotFound();

            ViewBag.DanhSachMon = new SelectList(
                db.MonHocs.Where(m => m.MaGV == maGV),
                "MaMon",
                "TenMon",
                cauHoi.MaMon
            );

            ViewBag.DanhSachDoKho = new SelectList(
                db.DoKhos,
                "MaDoKho",
                "TenDoKho",
                cauHoi.MaDoKho
            );

            return View(cauHoi);
        }

        // POST: Edit
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(CauHoiModel model)
        {
            var check = CheckLogin();
            if (check != null) return check;

            if (ModelState.IsValid)
            {
                db.Entry(model).State = System.Data.Entity.EntityState.Modified;
                db.SaveChanges();

                TempData["Success"] = "Cập nhật thành công!";
                return RedirectToAction("Index");
            }

            int maGV = GetMaGV();

            ViewBag.DanhSachMon = new SelectList(
                db.MonHocs.Where(m => m.MaGV == maGV),
                "MaMon",
                "TenMon",
                model.MaMon
            );

            ViewBag.DanhSachDoKho = new SelectList(
                db.DoKhos,
                "MaDoKho",
                "TenDoKho",
                model.MaDoKho
            );

            return View(model);
        }

        // GET: Delete
        public ActionResult Delete(int id)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var cauHoi = db.CauHois
                .Include(c => c.MonHoc)
                .Include(c => c.DoKho)
                .FirstOrDefault(c => c.MaCH == id && c.MonHoc.MaGV == maGV);

            if (cauHoi == null) return HttpNotFound();

            return View(cauHoi);
        }

        // POST: Delete
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            var check = CheckLogin();
            if (check != null) return check;

            var cauHoi = db.CauHois.Find(id);

            if (cauHoi != null)
            {
                db.CauHois.Remove(cauHoi);
                db.SaveChanges();
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