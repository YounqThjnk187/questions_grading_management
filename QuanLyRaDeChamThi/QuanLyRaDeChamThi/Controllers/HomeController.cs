using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;

namespace QuanLyRaDeChamThi.Controllers
{
    public class HomeController : Controller
    {
        // GET: Home
        public ActionResult Index()
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");

            return View();
        }
    }
}
