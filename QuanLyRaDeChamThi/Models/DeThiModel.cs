using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("DE_THI")]
    public class DeThiModel
    {
        [Key]
        public int MaDT { get; set; }

        [Required(ErrorMessage = "Vui lòng chọn môn học")]
        [Display(Name = "Môn học")]
        public int MaMon { get; set; }

        [Required(ErrorMessage = "Vui lòng chọn học kỳ")]
        [Display(Name = "Học kỳ")]
        [Range(1, 2, ErrorMessage = "Học kỳ chỉ có thể là 1 hoặc 2")]
        public byte HocKy { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập năm học")]
        [Display(Name = "Năm học")]
        [StringLength(10)]
        public string NamHoc { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập thời lượng")]
        [Display(Name = "Thời lượng (phút)")]
        [Range(30, 180, ErrorMessage = "Thời lượng phải từ 30 đến 180 phút")]
        public int ThoiLuong { get; set; }

        [Display(Name = "Ngày thi")]
        [DisplayFormat(DataFormatString = "{0:dd/MM/yyyy}", ApplyFormatInEditMode = true)]
        public DateTime? NgayThi { get; set; }

        public int MaGV { get; set; }

        // Navigation
        [ForeignKey("MaMon")]
        public virtual MonHocModel MonHoc { get; set; }

        [ForeignKey("MaGV")]
        public virtual GiangVienModel GiangVien { get; set; }

        public virtual ICollection<CTDeThiModel> CTDeThis { get; set; }
        public virtual ICollection<KetQuaModel> KetQuas { get; set; }
    }
}
