using System.Security.Cryptography;
using System.Text;
using System.Web.Mvc;
using System.Web.Security;
using System.Linq;
using QuanLyRaDeChamThi.Models;
using QuanLyRaDeChamThi.Models.ViewModels;

namespace QuanLyRaDeChamThi.Controllers
{
    public class AccountController : Controller
    {
        private AppDB db = new AppDB();

        // GET: Account/Login
        [AllowAnonymous]
        public ActionResult Login(string returnUrl)
        {
            if (Session["MaGV"] != null)
                return RedirectToAction("Index", "Home");
            ViewBag.ReturnUrl = returnUrl;
            return View();
        }

        // POST: Account/Login
        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public ActionResult Login(LoginViewModel model, string returnUrl)
        {
            if (!ModelState.IsValid)
                return View(model);

            string hashedPwd = HashSHA256(model.MatKhau);
            var gv = db.GiangViens.FirstOrDefault(g =>
                g.TenDangNhap == model.TenDangNhap && g.MatKhau == hashedPwd);

            if (gv == null)
            {
                ModelState.AddModelError("", "Tên đăng nhập hoặc mật khẩu không đúng.");
                return View(model);
            }

            Session["MaGV"]  = gv.MaGV;
            Session["HoTen"] = gv.HoTen;
            FormsAuthentication.SetAuthCookie(gv.TenDangNhap, false);

            if (!string.IsNullOrEmpty(returnUrl) && Url.IsLocalUrl(returnUrl))
                return Redirect(returnUrl);

            return RedirectToAction("Index", "Home");
        }

        // POST: Account/Logout
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Logout()
        {
            FormsAuthentication.SignOut();
            Session.Clear();
            Session.Abandon();
            return RedirectToAction("Login", "Account");
        }

        // Hàm băm SHA256
        public static string HashSHA256(string input)
        {
            using (SHA256 sha256 = SHA256.Create())
            {
                byte[] bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(input));
                StringBuilder sb = new StringBuilder();
                foreach (byte b in bytes)
                    sb.Append(b.ToString("x2"));
                return sb.ToString();
            }
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}
