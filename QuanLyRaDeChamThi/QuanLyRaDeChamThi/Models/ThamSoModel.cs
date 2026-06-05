using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("THAM_SO")]
    public class ThamSoModel
    {
        [Key]
        [Display(Name = "Tên tham số")]
        [StringLength(50)]
        public string TenThamSo { get; set; }

        [Required]
        [Display(Name = "Giá trị")]
        public int GiaTri { get; set; }

        [Display(Name = "Ghi chú")]
        [StringLength(200)]
        public string GhiChu { get; set; }
    }
}
