using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace QuanLyRaDeChamThi.Models
{
    [Table("GIANG_VIEN")]
    public class GiangVienModel
    {
        [Key]
        public int MaGV { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập họ tên")]
        [Display(Name = "Họ tên")]
        [StringLength(100)]
        public string HoTen { get; set; }

        [Required(ErrorMessage = "Vui lòng nhập tên đăng nhập")]
        [Display(Name = "Tên đăng nhập")]
        [StringLength(50)]
        public string TenDangNhap { get; set; }

        [Required]
        [StringLength(256)]
        public string MatKhau { get; set; }

        [Display(Name = "Email")]
        [EmailAddress]
        [StringLength(100)]
        public string Email { get; set; }

        // Navigation
        public virtual ICollection<MonHocModel> MonHocs { get; set; }
        public virtual ICollection<DeThiModel> DeThis { get; set; }
        public virtual ICollection<LopHocModel> LopHocs { get; set; }
    }
}
