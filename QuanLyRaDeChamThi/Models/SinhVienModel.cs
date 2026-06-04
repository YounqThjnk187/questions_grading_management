using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("SINH_VIEN")]
    public class SinhVienModel
    {
        [Key]
        public int MaSV { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập họ tên")]
        [Display(Name = "Họ tên")]
        [StringLength(100)]
        public string HoTen { get; set; }

        [Display(Name = "Ngày sinh")]
        [DisplayFormat(DataFormatString = "{0:dd/MM/yyyy}", ApplyFormatInEditMode = true)]
        public DateTime? NgaySinh { get; set; }

        [Required(ErrorMessage = "Vui lòng chọn lớp học")]
        [Display(Name = "Lớp học")]
        public int MaLop { get; set; }

        // Navigation
        [ForeignKey("MaLop")]
        public virtual LopHocModel LopHoc { get; set; }

        public virtual ICollection<KetQuaModel> KetQuas { get; set; }
    }
}
