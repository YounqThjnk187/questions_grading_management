<<<<<<< HEAD:QuanLyRaDeChamThi/QuanLyRaDeChamThi/Controllers/AccountController.cs
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
=======
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

        // GET: Account/Register
        [AllowAnonymous]
        public ActionResult Register()
        {
            if (Session["MaGV"] != null)
                return RedirectToAction("Index", "Home");
            return View();
        }

        // POST: Account/Register
        [HttpPost]
        [AllowAnonymous]
        [ValidateAntiForgeryToken]
        public ActionResult Register(RegisterViewModel model)
        {
            if (!ModelState.IsValid)
                return View(model);

            // Kiểm tra mật khẩu xác nhận
            if (model.MatKhau != model.XacNhanMatKhau)
            {
                ModelState.AddModelError("XacNhanMatKhau", "Mật khẩu xác nhận không khớp!");
                return View(model);
            }

            // Kiểm tra tên đăng nhập đã tồn tại
            var exists = db.GiangViens.Any(g => g.TenDangNhap == model.TenDangNhap);
            if (exists)
            {
                ModelState.AddModelError("TenDangNhap", $"Tên đăng nhập '{model.TenDangNhap}' đã tồn tại!");
                return View(model);
            }

            // Tạo tài khoản mới
            var giangVien = new GiangVienModel
            {
                HoTen = model.HoTen,
                TenDangNhap = model.TenDangNhap.ToLower(),
                MatKhau = HashSHA256(model.MatKhau),
                Email = model.Email
            };

            db.GiangViens.Add(giangVien);
            db.SaveChanges();

            TempData["Success"] = $"✅ Đăng ký thành công! Bạn có thể đăng nhập với tài khoản <strong>{model.TenDangNhap}</strong>";
            return RedirectToAction("Login");
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
>>>>>>> a546afd41e823ba8c7e40278b493716982ebbd39:QuanLyRaDeChamThi/Controllers/AccountController.cs
