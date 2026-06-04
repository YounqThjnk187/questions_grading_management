using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("KET_QUA")]
    public class KetQuaModel
    {
        [Key, Column(Order = 0)]
        [Display(Name = "Sinh viên")]
        public int MaSV { get; set; }

        [Key, Column(Order = 1)]
        [Display(Name = "Đề thi")]
        public int MaDT { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập điểm số")]
        [Display(Name = "Điểm số")]
        [Range(0, 10, ErrorMessage = "Điểm phải từ 0 đến 10")]
        [Column(TypeName = "decimal")]
        public decimal DiemSo { get; set; }

        [Display(Name = "Điểm chữ")]
        [StringLength(5)]
        public string DiemChu { get; set; }

        [Display(Name = "Ngày chấm")]
        [DisplayFormat(DataFormatString = "{0:dd/MM/yyyy}", ApplyFormatInEditMode = true)]
        public DateTime? NgayCham { get; set; }

        // Navigation
        [ForeignKey("MaSV")]
        public virtual SinhVienModel SinhVien { get; set; }

        [ForeignKey("MaDT")]
        public virtual DeThiModel DeThi { get; set; }
    }
}
