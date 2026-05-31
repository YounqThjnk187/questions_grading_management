using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("LOP_HOC")]
    public class LopHocModel
    {
        [Key]
        public int MaLop { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập tên lớp")]
        [Display(Name = "Tên lớp")]
        [StringLength(50)]
        public string TenLop { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập năm học")]
        [Display(Name = "Năm học")]
        [StringLength(10)]
        public string NamHoc { get; set; }

        [Display(Name = "Giảng viên")]
        public int MaGV { get; set; }

        // Navigation
        [ForeignKey("MaGV")]
        public virtual GiangVienModel GiangVien { get; set; }

        public virtual ICollection<SinhVienModel> SinhViens { get; set; }
    }
}
