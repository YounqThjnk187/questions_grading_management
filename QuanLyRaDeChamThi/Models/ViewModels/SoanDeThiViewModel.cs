using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace QuanLyRaDeChamThi.Models.ViewModels
{
    public class SoanDeThiViewModel
    {
        // Thông tin đề thi
        public int MaDT { get; set; }

        [Required(ErrorMessage = "Vui lòng chọn môn học")]
        [Display(Name = "Môn học")]
        public int MaMon { get; set; }

        [Required(ErrorMessage = "Vui lòng chọn học kỳ")]
        [Display(Name = "Học kỳ")]
        public int HocKy { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập năm học")]
        [Display(Name = "Năm học")]
        public string NamHoc { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập thời lượng")]
        [Display(Name = "Thời lượng (phút)")]
        [Range(30, 180, ErrorMessage = "Thời lượng phải từ 30 đến 180 phút")]
        public int ThoiLuong { get; set; }

        [Display(Name = "Ngày thi")]
        [DisplayFormat(DataFormatString = "{0:yyyy-MM-dd}", ApplyFormatInEditMode = true)]
        public DateTime? NgayThi { get; set; }

        // Danh sách câu hỏi được chọn (ID)
        public List<int> CauHoiDuocChon { get; set; } = new List<int>();

        // Danh sách để hiển thị (dropdown/list)
        public List<MonHocModel> DanhSachMonHoc { get; set; } = new List<MonHocModel>();
        public List<CauHoiModel> DanhSachCauHoi { get; set; } = new List<CauHoiModel>();
        public List<DoKhoModel>  DanhSachDoKho   { get; set; } = new List<DoKhoModel>();

        // Filter câu hỏi
        public int? FilterDoKho { get; set; }
    }
}
