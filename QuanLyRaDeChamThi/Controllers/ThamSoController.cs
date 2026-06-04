using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;
using System.Linq;

namespace QuanLyRaDeChamThi.Controllers
{
    public class ThamSoController : Controller
    {
        private AppDB db = new AppDB();

        private ActionResult CheckLogin()
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            return null;
        }

        // GET: ThamSo - Xem tất cả tham số
        public ActionResult Index()
        {
            var check = CheckLogin(); if (check != null) return check;
            return View(db.ThamSos.ToList());
        }

        // GET: ThamSo/Edit/SoCauToiDa
        public ActionResult Edit(string id)
        {
            var check = CheckLogin(); if (check != null) return check;
            var ts = db.ThamSos.Find(id);
            if (ts == null) return HttpNotFound();
            return View(ts);
        }

        // POST: ThamSo/Edit
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(ThamSoModel model)
        {
            var check = CheckLogin(); if (check != null) return check;

            if (ModelState.IsValid)
            {
                db.Entry(model).State = System.Data.Entity.EntityState.Modified;
                db.SaveChanges();
                TempData["Success"] = $"Tham số '{model.TenThamSo}' đã được cập nhật thành {model.GiaTri}!";
                return RedirectToAction("Index");
            }
            return View(model);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}
