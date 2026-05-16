using System;
using System.Collections.Generic;
using System.Linq;
using System.Web.Mvc;
using QuanLyRaDeChamThi.Models;
using QuanLyRaDeChamThi.Models.ViewModels;

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

        // GET: KetQua - Chọn đề thi để nhập điểm
        public ActionResult Index()
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var deThis = db.DeThis.Include("MonHoc")
                .Where(d => d.MaGV == maGV)
                .OrderByDescending(d => d.MaDT)
                .ToList();

            return View(deThis);
        }

        // GET: KetQua/NhapDiem/5 - Nhập điểm cho đề thi
        public ActionResult NhapDiem(int maDT, int? maLop)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            var deThi = db.DeThis.Include("MonHoc")
                .FirstOrDefault(d => d.MaDT == maDT && d.MaGV == maGV);
            if (deThi == null) return HttpNotFound();

            var lopHocs = db.LopHocs.Where(l => l.NamHoc == deThi.NamHoc && l.MaGV == maGV).ToList();

            // Lấy danh sách sinh viên
            var sinhVienQuery = db.SinhViens.Include("LopHoc")
                .Where(s => s.LopHoc.NamHoc == deThi.NamHoc && s.LopHoc.MaGV == maGV);
            if (maLop.HasValue)
                sinhVienQuery = sinhVienQuery.Where(s => s.MaLop == maLop.Value);

            var sinhViens = sinhVienQuery.ToList();

            // Lấy kết quả đã chấm
            var ketQuas = db.KetQuas.Where(k => k.MaDT == maDT).ToList();

            var danhSachDiem = sinhViens.Select(sv => {
                var kq = ketQuas.FirstOrDefault(k => k.MaSV == sv.MaSV);
                return new DanhSachDiemItem
                {
                    MaSV      = sv.MaSV,
                    HoTen     = sv.HoTen,
                    TenLop    = sv.LopHoc.TenLop,
                    DiemSo    = kq?.DiemSo,
                    DiemChu   = kq?.DiemChu,
                    NgayCham  = kq?.NgayCham,
                    DaCham    = kq != null
                };
            }).OrderBy(x => x.TenLop).ThenBy(x => x.HoTen).ToList();

            var vm = new NhapDiemViewModel
            {
                MaDT          = maDT,
                TenMon        = deThi.MonHoc.TenMon,
                NamHoc        = deThi.NamHoc,
                HocKy         = deThi.HocKy,
                DanhSachDiem  = danhSachDiem,
                DanhSachLop   = lopHocs,
                MaLopFilter   = maLop
            };

            return View(vm);
        }

        // POST: KetQua/LuuDiem - Lưu điểm hàng loạt
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult LuuDiem(int maDT, List<int> maSVList, List<decimal?> diemSoList)
        {
            var check = CheckLogin(); if (check != null) return check;
            int maGV = GetMaGV();

            if (maSVList == null || diemSoList == null)
            {
                TempData["Error"] = "Dữ liệu không hợp lệ.";
                return RedirectToAction("NhapDiem", new { maDT = maDT });
            }

            for (int i = 0; i < maSVList.Count; i++)
            {
                if (i >= diemSoList.Count || !diemSoList[i].HasValue) continue;

                decimal diem = diemSoList[i].Value;
                if (diem < 0 || diem > 10) continue;

                int maSV = maSVList[i];
                string diemChu = GetDiemChu(diem);

                var kq = db.KetQuas.FirstOrDefault(k => k.MaSV == maSV && k.MaDT == maDT);
                if (kq == null)
                {
                    db.KetQuas.Add(new KetQuaModel
                    {
                        MaSV     = maSV,
                        MaDT     = maDT,
                        DiemSo   = diem,
                        DiemChu  = diemChu,
                        NgayCham = DateTime.Today
                    });
                }
                else
                {
                    kq.DiemSo   = diem;
                    kq.DiemChu  = diemChu;
                    kq.NgayCham = DateTime.Today;
                    db.Entry(kq).State = System.Data.Entity.EntityState.Modified;
                }
            }

            db.SaveChanges();
            TempData["Success"] = "Điểm đã được lưu thành công!";
            return RedirectToAction("NhapDiem", new { maDT = maDT });
        }

        // Tự động tính điểm chữ từ điểm số
        private string GetDiemChu(decimal diemSo)
        {
            var bdc = db.BangDiemChus
                .Where(b => diemSo >= b.DiemSoTu && diemSo <= b.DiemSoDen)
                .FirstOrDefault();
            return bdc?.DiemChu ?? "F";
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}
