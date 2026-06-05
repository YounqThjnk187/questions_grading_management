<<<<<<< HEAD:QuanLyRaDeChamThi/QuanLyRaDeChamThi/Models/ViewModels/BaoCaoNamViewModel.cs
using System.Collections.Generic;

namespace QuanLyRaDeChamThi.Models.ViewModels
{
    public class BaoCaoNamViewModel
    {
        public string NamHoc { get; set; }
        public List<BaoCaoMonHocItem> DanhSachBaoCao { get; set; } = new List<BaoCaoMonHocItem>();
        public List<string> DanhSachNamHoc { get; set; } = new List<string>();
    }

    public class BaoCaoMonHocItem
    {
        public string TenMon { get; set; }
        public int HocKy { get; set; }
        public int TongSinhVien { get; set; }

        public int SoA { get; set; }
        public int SoBPlus { get; set; }
        public int SoB { get; set; }
        public int SoCPlus { get; set; }
        public int SoC { get; set; }
        public int SoDPlus { get; set; }
        public int SoD { get; set; }
        public int SoF { get; set; }

        public decimal DiemTrungBinh { get; set; }

        public decimal TiLeDao => TongSinhVien > 0
            ? (decimal)(TongSinhVien - SoF) / TongSinhVien * 100
            : 0;
        public List<string> DanhSachNamHoc { get; set; } = new List<string>();
    }
=======
using System.Collections.Generic;

namespace QuanLyRaDeChamThi.Models.ViewModels
{
    public class BaoCaoNamViewModel
    {
        public string NamHoc { get; set; }
        public List<BaoCaoMonHocItem> DanhSachBaoCao { get; set; } = new List<BaoCaoMonHocItem>();
        public List<string> DanhSachNamHoc { get; set; } = new List<string>();
    }

    public class BaoCaoMonHocItem
    {
        public string TenMon { get; set; }
        public int HocKy { get; set; }
        public int TongSinhVien { get; set; }

        public int SoA { get; set; }
        public int SoBPlus { get; set; }
        public int SoB { get; set; }
        public int SoCPlus { get; set; }
        public int SoC { get; set; }
        public int SoDPlus { get; set; }
        public int SoD { get; set; }
        public int SoF { get; set; }

        public decimal DiemTrungBinh { get; set; }

        public decimal TiLeDao => TongSinhVien > 0
            ? (decimal)(TongSinhVien - SoF) / TongSinhVien * 100
            : 0;
        public List<string> DanhSachNamHoc { get; set; } = new List<string>();
    }
>>>>>>> a546afd41e823ba8c7e40278b493716982ebbd39:QuanLyRaDeChamThi/Models/ViewModels/BaoCaoNamViewModel.cs
}