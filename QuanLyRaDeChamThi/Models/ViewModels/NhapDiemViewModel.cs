using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace QuanLyRaDeChamThi.Models.ViewModels
{
    public class NhapDiemViewModel
    {
        public int MaDT { get; set; }
        public string TenMon { get; set; }
        public string NamHoc { get; set; }
        public int HocKy { get; set; }

        public List<DanhSachDiemItem> DanhSachDiem { get; set; } = new List<DanhSachDiemItem>();
        public List<LopHocModel>      DanhSachLop  { get; set; } = new List<LopHocModel>();
        public List<DeThiModel>       DanhSachDeThi { get; set; } = new List<DeThiModel>();
        public int? MaLopFilter { get; set; }
    }

    public class DanhSachDiemItem
    {
        public int MaSV { get; set; }
        public string HoTen { get; set; }
        public string TenLop { get; set; }

        [Range(0, 10, ErrorMessage = "Điểm phải từ 0 đến 10")]
        public decimal? DiemSo { get; set; }
        public string DiemChu { get; set; }
        public DateTime? NgayCham { get; set; }
        public bool DaCham { get; set; }
    }
}
