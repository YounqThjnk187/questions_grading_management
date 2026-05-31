using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("MON_HOC")]
    public class MonHocModel
    {
        [Key]
        public int MaMon { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập tên môn học")]
        [Display(Name = "Tên môn học")]
        [StringLength(100)]
        public string TenMon { get; set; }

        [Display(Name = "Giảng viên")]
        public int MaGV { get; set; }

        // Navigation
        [ForeignKey("MaGV")]
        public virtual GiangVienModel GiangVien { get; set; }

        public virtual ICollection<CauHoiModel> CauHois { get; set; }
        public virtual ICollection<DeThiModel> DeThis { get; set; }
    }
}
