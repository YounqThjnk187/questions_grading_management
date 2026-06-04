using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("BANG_DIEM_CHU")]
    public class BangDiemChuModel
    {
        [Key]
        [Display(Name = "Điểm chữ")]
        [StringLength(5)]
        public string DiemChu { get; set; }

        [Required]
        [Display(Name = "Điểm số từ")]
        [Column(TypeName = "decimal")]
        public decimal DiemSoTu { get; set; }

        [Required]
        [Display(Name = "Điểm số đến")]
        [Column(TypeName = "decimal")]
        public decimal DiemSoDen { get; set; }

        [Display(Name = "Ghi chú")]
        [StringLength(100)]
        public string GhiChu { get; set; }
    }
}
