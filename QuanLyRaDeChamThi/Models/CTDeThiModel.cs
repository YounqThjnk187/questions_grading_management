using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("CT_DETHI")]
    public class CTDeThiModel
    {
        [Key, Column(Order = 0)]
        public int MaDT { get; set; }

        [Key, Column(Order = 1)]
        public int MaCH { get; set; }

        // Navigation
        [ForeignKey("MaDT")]
        public virtual DeThiModel DeThi { get; set; }

        [ForeignKey("MaCH")]
        public virtual CauHoiModel CauHoi { get; set; }
    }
}
