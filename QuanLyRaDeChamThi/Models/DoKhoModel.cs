using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("DO_KHO")]
    public class DoKhoModel
    {
        [Key]
        public int MaDoKho { get; set; }

        [Required]
        [Display(Name = "Độ khó")]
        [StringLength(50)]
        public string TenDoKho { get; set; }

        // Navigation
        public virtual ICollection<CauHoiModel> CauHois { get; set; }
    }
}
