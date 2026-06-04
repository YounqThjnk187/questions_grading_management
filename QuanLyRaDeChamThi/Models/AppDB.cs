using System.Data.Entity;

namespace QuanLyRaDeChamThi.Models
{
    public class AppDB : DbContext
    {
        public AppDB() : base("AppDB") { }

        public DbSet<GiangVienModel>    GiangViens    { get; set; }
        public DbSet<MonHocModel>       MonHocs       { get; set; }
        public DbSet<DoKhoModel>        DoKhos        { get; set; }
        public DbSet<CauHoiModel>       CauHois       { get; set; }
        public DbSet<DeThiModel>        DeThis        { get; set; }
        public DbSet<CTDeThiModel>      CTDeThis      { get; set; }
        public DbSet<LopHocModel>       LopHocs       { get; set; }
        public DbSet<SinhVienModel>     SinhViens     { get; set; }
        public DbSet<KetQuaModel>       KetQuas       { get; set; }
        public DbSet<BangDiemChuModel>  BangDiemChus  { get; set; }
        public DbSet<ThamSoModel>       ThamSos       { get; set; }

        protected override void OnModelCreating(DbModelBuilder modelBuilder)
        {
            modelBuilder.Entity<GiangVienModel>().ToTable("GIANG_VIEN");
            modelBuilder.Entity<MonHocModel>().ToTable("MON_HOC");
            modelBuilder.Entity<DoKhoModel>().ToTable("DO_KHO");
            modelBuilder.Entity<CauHoiModel>().ToTable("CAU_HOI");
            modelBuilder.Entity<DeThiModel>().ToTable("DE_THI");
            modelBuilder.Entity<CTDeThiModel>().ToTable("CT_DETHI")
                .HasKey(x => new { x.MaDT, x.MaCH });
            modelBuilder.Entity<LopHocModel>().ToTable("LOP_HOC");
            modelBuilder.Entity<SinhVienModel>().ToTable("SINH_VIEN");
            modelBuilder.Entity<KetQuaModel>().ToTable("KET_QUA")
                .HasKey(x => new { x.MaSV, x.MaDT });
            modelBuilder.Entity<BangDiemChuModel>().ToTable("BANG_DIEM_CHU");
            modelBuilder.Entity<ThamSoModel>().ToTable("THAM_SO");

            // Tắt tự động tạo bảng khi có thay đổi schema
            Database.SetInitializer<AppDB>(null);
        }
    }
}
