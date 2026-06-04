using QuanLyRaDeChamThi.Models;
using QuanLyRaDeChamThi.Models.ViewModels;
using System;
using System.Linq;
using System.Web.Mvc;

namespace QuanLyRaDeChamThi.Controllers
{
    public class KetQuaController : Controller
    {
        private AppDB db = new AppDB();

        private int GetMaGV() => Session["MaGV"] != null ? (int)Session["MaGV"] : 0;

        private ActionResult CheckLogin()
        {
            if (Session["MaGV"] == null)
                return RedirectToAction("Login", "Account");
            return null;
        }

        // GET: KetQua
        public ActionResult Index()
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            // FIX: không trả entity trực tiếp nữa
            var deThis = db.DeThis
                .Where(d => d.MaGV == maGV)
                .Select(d => new DeThiNhapDiemItem
                {
                    MaDT = d.MaDT,
                    HocKy = d.HocKy,
                    NamHoc = d.NamHoc,
                    NgayThi = d.NgayThi,
                    TenMon = d.MonHoc.TenMon
                })
                .ToList();

            return View(deThis);
        }

        // GET: Nhập điểm
        public ActionResult NhapDiem(int maDT, int? maLop)
        {
            var check = CheckLogin();
            if (check != null) return check;

            int maGV = GetMaGV();

            var deThi = db.DeThis
                .Where(d => d.MaDT == maDT && d.MaGV == maGV)
                .Select(d => new
                {
                    d.MaDT,
                    TenMon = d.MonHoc.TenMon,
                    d.NamHoc,
                    d.HocKy
                })
                .FirstOrDefault();

            if (deThi == null) return HttpNotFound();

            var lopHocs = db.LopHocs.ToList();

            // Lấy TẤT CẢ sinh viên (không filter theo năm học)
            var sinhVienQuery = db.SinhViens.AsQueryable();

            if (maLop.HasValue)
                sinhVienQuery = sinhVienQuery.Where(s => s.MaLop == maLop.Value);

            var sinhViens = sinhVienQuery.ToList();

            var ketQuas = db.KetQuas.Where(k => k.MaDT == maDT).ToList();

            var danhSachDiem = sinhViens.Select(sv =>
            {
                var kq = ketQuas.FirstOrDefault(k => k.MaSV == sv.MaSV);

                return new DanhSachDiemItem
                {
                    MaSV = sv.MaSV,
                    HoTen = sv.HoTen,
                    TenLop = sv.LopHoc?.TenLop ?? "Chưa có lớp",
                    DiemSo = kq?.DiemSo,
                    DiemChu = kq?.DiemChu,
                    NgayCham = kq?.NgayCham,
                    DaCham = kq != null
                };
            }).ToList();

            var vm = new NhapDiemViewModel
            {
                MaDT = maDT,
                TenMon = deThi.TenMon,
                HocKy = deThi.HocKy,
                NamHoc = deThi.NamHoc,
                DanhSachDiem = danhSachDiem,
                DanhSachLop = lopHocs,
                MaLopFilter = maLop
            };

            return View(vm);
        }

        // POST: Lưu điểm
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult LuuDiem(int maDT, int[] maSVList, decimal?[] diemSoList)
        {
            var check = CheckLogin();
            if (check != null) return check;

            if (maSVList == null || diemSoList == null)
            {
                TempData["Error"] = "Dữ liệu không hợp lệ";
                return RedirectToAction("NhapDiem", new { maDT });
            }

            for (int i = 0; i < maSVList.Length; i++)
            {
                if (i >= diemSoList.Length || !diemSoList[i].HasValue) continue;

                decimal diem = diemSoList[i].Value;
                if (diem < 0 || diem > 10) continue;

                var maSV = maSVList[i];

                var kq = db.KetQuas.FirstOrDefault(x => x.MaSV == maSV && x.MaDT == maDT);

                if (kq == null)
                {
                    db.KetQuas.Add(new KetQuaModel
                    {
                        MaSV = maSV,
                        MaDT = maDT,
                        DiemSo = diem,
                        DiemChu = GetDiemChu(diem),
                        NgayCham = DateTime.Now
                    });
                }
                else
                {
                    kq.DiemSo = diem;
                    kq.DiemChu = GetDiemChu(diem);
                    kq.NgayCham = DateTime.Now;
                }
            }

            db.SaveChanges();

            TempData["Success"] = "Lưu điểm thành công!";
            return RedirectToAction("NhapDiem", new { maDT });
        }

        private string GetDiemChu(decimal diem)
        {
            if (diem >= 8.5m) return "A";
            if (diem >= 7) return "B";
            if (diem >= 5.5m) return "C";
            if (diem >= 4) return "D";
            return "F";
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }

    // DTO tránh proxy
    public class DeThiNhapDiemItem
    {
        public int MaDT { get; set; }
        public byte HocKy { get; set; }
        public string NamHoc { get; set; }
        public DateTime? NgayThi { get; set; }
        public string TenMon { get; set; }
    }
}