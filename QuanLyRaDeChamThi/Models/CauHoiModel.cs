using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("CAU_HOI")]
    public class CauHoiModel
    {
        [Key]
        public int MaCH { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập nội dung câu hỏi")]
        [Display(Name = "Nội dung câu hỏi")]
        public string NoiDung { get; set; }

        [Required(ErrorMessage = "Vui lòng chọn môn học")]
        [Display(Name = "Môn học")]
        public int MaMon { get; set; }

        [Required(ErrorMessage = "Vui lòng chọn độ khó")]
        [Display(Name = "Độ khó")]
        public int MaDoKho { get; set; }

        // Navigation
        [ForeignKey("MaMon")]
        public virtual MonHocModel MonHoc { get; set; }

        [ForeignKey("MaDoKho")]
        public virtual DoKhoModel DoKho { get; set; }

        public virtual ICollection<CTDeThiModel> CTDeThis { get; set; }
    }
}
