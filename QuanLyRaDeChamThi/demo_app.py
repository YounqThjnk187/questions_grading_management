<<<<<<< HEAD
﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo: Hệ thống Quản lý Ra đề và Chấm thi
Nhóm 15 – SE104.Q23
Chạy: python demo_app.py
Truy cập: http://localhost:8080
"""

import hashlib, json, sqlite3, os, urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "demo.db")

# ── Bootstrap 3 CSS CDN (sẽ dùng inline nếu offline) ──────────────────────────
BOOTSTRAP_CDN = "https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css"

# ── Connection Pool (tăng tốc độ truy vấn) ──────────────────────────────────
_db_pool = []
def get_db():
    """Lấy connection từ pool hoặc tạo mới"""
    if _db_pool:
        return _db_pool.pop()
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10.0)
    conn.execute("PRAGMA journal_mode=WAL")  # Tăng tốc đọc
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA busy_timeout=5000")  # Wait 5s if locked
    return conn

def release_db(conn):
    """Trả connection về pool"""
    if len(_db_pool) < 5:  # Giới hạn pool size
        _db_pool.append(conn)
    else:
        conn.close()

def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()

# ══════════════════════════════════════════════════════════════════════
# DATABASE SETUP
# ══════════════════════════════════════════════════════════════════════
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS GIANG_VIEN(
        MaGV INTEGER PRIMARY KEY AUTOINCREMENT,
        HoTen TEXT, TenDangNhap TEXT UNIQUE, MatKhau TEXT, Email TEXT
    );
    CREATE TABLE IF NOT EXISTS MON_HOC(
        MaMon INTEGER PRIMARY KEY AUTOINCREMENT,
        TenMon TEXT, MaGV INTEGER
    );
    CREATE TABLE IF NOT EXISTS DO_KHO(
        MaDoKho INTEGER PRIMARY KEY AUTOINCREMENT,
        TenDoKho TEXT
    );
    CREATE TABLE IF NOT EXISTS CAU_HOI(
        MaCH INTEGER PRIMARY KEY AUTOINCREMENT,
        NoiDung TEXT, MaMon INTEGER, MaDoKho INTEGER
    );
    CREATE TABLE IF NOT EXISTS DE_THI(
        MaDT INTEGER PRIMARY KEY AUTOINCREMENT,
        MaMon INTEGER, HocKy INTEGER, NamHoc TEXT,
        ThoiLuong INTEGER, NgayThi TEXT, MaGV INTEGER
    );
    CREATE TABLE IF NOT EXISTS CT_DETHI(
        MaDT INTEGER, MaCH INTEGER,
        PRIMARY KEY(MaDT, MaCH)
    );
    CREATE TABLE IF NOT EXISTS LOP_HOC(
        MaLop INTEGER PRIMARY KEY AUTOINCREMENT,
        TenLop TEXT, NamHoc TEXT, MaGV INTEGER
    );
    CREATE TABLE IF NOT EXISTS SINH_VIEN(
        MaSV INTEGER PRIMARY KEY AUTOINCREMENT,
        HoTen TEXT, NgaySinh TEXT, MaLop INTEGER
    );
    CREATE TABLE IF NOT EXISTS KET_QUA(
        MaSV INTEGER, MaDT INTEGER,
        DiemSo REAL, DiemChu TEXT, NgayCham TEXT,
        PRIMARY KEY(MaSV, MaDT)
    );
    CREATE TABLE IF NOT EXISTS BANG_DIEM_CHU(
        DiemChu TEXT PRIMARY KEY,
        DiemSoTu REAL, DiemSoDen REAL, GhiChu TEXT
    );
    CREATE TABLE IF NOT EXISTS THAM_SO(
        TenThamSo TEXT PRIMARY KEY,
        GiaTri INTEGER, GhiChu TEXT
    );
    """)

    # Seed nếu chưa có dữ liệu
    if cur.execute("SELECT COUNT(*) FROM DO_KHO").fetchone()[0] == 0:
        cur.executemany("INSERT INTO DO_KHO(TenDoKho) VALUES(?)",
            [("Dễ",),("Trung Bình",),("Phức Tạp",),("Khó",)])
        cur.executemany("INSERT INTO BANG_DIEM_CHU VALUES(?,?,?,?)",[
            ("A",8.5,10.0,"Xuất sắc"),("B+",8.0,8.49,"Giỏi"),
            ("B",7.0,7.99,"Khá"),("C+",6.5,6.99,"Trung bình khá"),
            ("C",5.5,6.49,"Trung bình"),("D+",5.0,5.49,"Trung bình yếu"),
            ("D",4.0,4.99,"Yếu"),("F",0.0,3.99,"Kém"),
        ])
        cur.executemany("INSERT INTO THAM_SO VALUES(?,?,?)",[
            ("SoCauToiDa",5,"Số câu hỏi tối đa mỗi đề thi"),
            ("ThoiLuongToiThieu",30,"Thời lượng tối thiểu (phút)"),
            ("ThoiLuongToiDa",180,"Thời lượng tối đa (phút)"),
            ("SoLopToiDa",50,"Số lớp tối đa mỗi năm"),
            ("SoMonToiDa",4,"Số môn học tối đa"),
        ])
        pwd = sha256("123456")
        cur.executemany("INSERT INTO GIANG_VIEN(HoTen,TenDangNhap,MatKhau,Email) VALUES(?,?,?,?)",[
            ("Nguyễn Văn An","gv01",pwd,"gv01@uit.edu.vn"),
            ("Trần Thị Bình","gv02",pwd,"gv02@uit.edu.vn"),
        ])
        cur.executemany("INSERT INTO MON_HOC(TenMon,MaGV) VALUES(?,?)",[
            ("Lập trình hướng đối tượng",1),
            ("Cơ sở dữ liệu",1),
            ("Mạng máy tính",2),
            ("Công nghệ phần mềm",1),
        ])
        cur.executemany("INSERT INTO CAU_HOI(NoiDung,MaMon,MaDoKho) VALUES(?,?,?)",[
            ("Kế thừa trong OOP là gì?",1,1),
            ("Sự khác biệt giữa abstract class và interface?",1,2),
            ("Polymorphism trong C# hoạt động như thế nào?",1,3),
            ("Giải thích nguyên lý SOLID.",1,4),
            ("Override và Overload khác nhau như thế nào?",1,2),
            ("Khóa chính (Primary Key) là gì?",2,1),
            ("Sự khác biệt giữa JOIN và UNION trong SQL?",2,2),
            ("Chuẩn hóa CSDL 3NF là gì?",2,3),
            ("Giải thích Transaction và ACID properties.",2,4),
            ("Index trong SQL có tác dụng gì?",2,2),
            ("Giao thức TCP/IP là gì?",3,1),
            ("HTTP và HTTPS khác nhau như thế nào?",3,2),
            ("Giải thích mô hình OSI 7 lớp.",3,3),
            ("DNS hoạt động như thế nào?",3,2),
            ("SDLC là gì?",4,1),
            ("Agile và Waterfall khác nhau như thế nào?",4,2),
            ("Kiểm thử hộp đen và hộp trắng là gì?",4,2),
            ("Giải thích mô hình kiến trúc 3 lớp.",4,3),
        ])
        cur.executemany("INSERT INTO LOP_HOC(TenLop,NamHoc,MaGV) VALUES(?,?,?)",[
            ("SE104.P11","2024-2025",1),("SE104.P12","2024-2025",1),("NT101.P11","2024-2025",2),
        ])
        cur.executemany("INSERT INTO SINH_VIEN(HoTen,NgaySinh,MaLop) VALUES(?,?,?)",[
            ("Nguyễn Văn A","2003-01-15",1),("Trần Thị B","2003-05-20",1),
            ("Lê Minh C","2002-12-10",1),("Phạm Thị D","2003-03-25",2),
            ("Hoàng Văn E","2002-08-14",2),("Đỗ Thị F","2003-07-07",2),
        ])
        cur.execute("INSERT INTO DE_THI(MaMon,HocKy,NamHoc,ThoiLuong,NgayThi,MaGV) VALUES(1,1,'2024-2025',90,'2025-01-10',1)")
        maDT = cur.lastrowid
        for maCH in [1,2,3,4,5]:
            cur.execute("INSERT INTO CT_DETHI VALUES(?,?)", (maDT, maCH))
        cur.executemany("INSERT INTO KET_QUA VALUES(?,?,?,?,?)",[
            (1,maDT,8.5,"A","2025-01-20"),
            (2,maDT,7.0,"B","2025-01-20"),
            (3,maDT,5.5,"C","2025-01-20"),
        ])
        
        # Tạo indexes để tăng tốc query
        cur.execute("CREATE INDEX IF NOT EXISTS idx_cauhoi_mon ON CAU_HOI(MaMon)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_cauhoi_dokho ON CAU_HOI(MaDoKho)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_dethi_magv ON DE_THI(MaGV)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_ketqua_madt ON KET_QUA(MaDT)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_monhoc_magv ON MON_HOC(MaGV)")
        
    conn.commit()
    conn.close()

# ══════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════
def get_diem_chu(diem):
    if diem >= 8.5: return "A"
    if diem >= 8.0: return "B+"
    if diem >= 7.0: return "B"
    if diem >= 6.5: return "C+"
    if diem >= 5.5: return "C"
    if diem >= 5.0: return "D+"
    if diem >= 4.0: return "D"
    return "F"

def label_class(diem_chu):
    m = {"A":"success","B+":"info","B":"info","C+":"warning","C":"warning","D+":"default","D":"default","F":"danger"}
    return m.get(diem_chu, "default")

SESSIONS = {}  # session_id -> {MaGV, HoTen}

def get_sid(handler):
    """Extract sid from cookie first, then URL query string"""
    # Check cookie first
    cookie = handler.headers.get("Cookie","")
    print(f"[get_sid] Cookie header: {cookie[:100] if cookie else 'EMPTY'}", flush=True)
    for part in cookie.split(";"):
        k,_,v = part.strip().partition("=")
        if k.strip() == "sid":
            print(f"[get_sid] Found sid in cookie: {v.strip()[:8]}...", flush=True)
            return v.strip()
    # Fallback to URL query string
    qs = urllib.parse.urlparse(handler.path).query
    sid_from_qs = urllib.parse.parse_qs(qs).get("sid", [""])[0]
    if sid_from_qs:
        print(f"[get_sid] Found sid in query string: {sid_from_qs[:8]}...", flush=True)
    else:
        print(f"[get_sid] NO SID FOUND!", flush=True)
    return sid_from_qs

def get_session(handler):
    # Primary: check cookie (standard web practice)
    cookie = handler.headers.get("Cookie","")
    for part in cookie.split(";"):
        k,_,v = part.strip().partition("=")
        if k.strip() == "sid":
            sid = v.strip()
            if sid and sid in SESSIONS:
                return SESSIONS[sid]
    # Fallback: check URL query string (for compatibility)
    sid = get_sid(handler)
    if sid and sid in SESSIONS:
        return SESSIONS[sid]
    return None

# ══════════════════════════════════════════════════════════════════════
# HTML TEMPLATES
# ══════════════════════════════════════════════════════════════════════
STYLE = """
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ── Modern UI inspired by Facebook/Instagram ── */
*,*:before,*:after{box-sizing:border-box;margin:0;padding:0;}
body{
  font-family:'Inter','Segoe UI',sans-serif;
  font-size:15px;
  line-height:1.6;
  color:#1c1e21;
  background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
  background-attachment:fixed;
}
a{color:#1877f2;text-decoration:none;transition:all 0.2s;}
a:hover{color:#0a58ca;}
h1,h2,h3,h4{font-weight:700;color:#1c1e21;}
.container-fluid{padding:0 20px;max-width:1400px;margin:0 auto;}
.row{display:flex;flex-wrap:wrap;margin:0 -10px;}
[class*="col-"]{padding:0 10px;}
.col-md-3{flex:0 0 25%;max-width:25%;}
.col-md-4{flex:0 0 33.33%;max-width:33.33%;}
.col-md-6{flex:0 0 50%;max-width:50%;}
.col-md-8{flex:0 0 66.66%;max-width:66.66%;}
.col-md-12{flex:0 0 100%;max-width:100%;}

/* ── Navbar (Instagram/Facebook style) ── */
.navbar{
  position:fixed;
  top:0;
  width:100%;
  z-index:1000;
  background:#fff;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
  height:60px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:0 24px;
}
.navbar-brand{
  font-size:22px;
  font-weight:700;
  background:linear-gradient(135deg,#667eea,#764ba2);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  background-clip:text;
}
.navbar-nav{
  display:flex;
  list-style:none;
  gap:8px;
}
.navbar-nav li a{
  padding:8px 16px;
  border-radius:8px;
  color:#65676b;
  font-weight:500;
  transition:all 0.2s;
  display:flex;
  align-items:center;
  gap:6px;
}
.navbar-nav li a:hover{
  background:#f0f2f5;
  color:#1c1e21;
}
.dropdown{position:relative;}
.dropdown-menu{
  display:none;
  position:absolute;
  right:0;
  top:calc(100% + 8px);
  background:#fff;
  border-radius:12px;
  box-shadow:0 8px 24px rgba(0,0,0,.15);
  min-width:200px;
  padding:8px;
  animation:fadeIn 0.2s;
}
@keyframes fadeIn{from{opacity:0;transform:translateY(-10px)}to{opacity:1;transform:translateY(0)}}
.dropdown-menu li a{
  display:flex;
  align-items:center;
  gap:12px;
  padding:10px 12px;
  border-radius:8px;
  color:#1c1e21;
  font-weight:500;
}
.dropdown-menu li a:hover{background:#f0f2f5;}
.dropdown:hover .dropdown-menu{display:block;}

/* ── Modern Buttons ── */
.btn{
  display:inline-block;
  padding:10px 20px;
  font-size:15px;
  font-weight:600;
  text-align:center;
  cursor:pointer;
  border:none;
  border-radius:8px;
  transition:all 0.2s;
  box-shadow:0 2px 4px rgba(0,0,0,.1);
}
.btn:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.15);}
.btn:active{transform:translateY(0);box-shadow:0 2px 4px rgba(0,0,0,.1);}
.btn-primary{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;}
.btn-success{background:linear-gradient(135deg,#56ab2f,#a8e063);color:#fff;}
.btn-info{background:linear-gradient(135deg,#00c6ff,#0072ff);color:#fff;}
.btn-warning{background:linear-gradient(135deg,#f093fb,#f5576c);color:#fff;}
.btn-danger{background:linear-gradient(135deg,#eb3349,#f45c43);color:#fff;}
.btn-default{background:#fff;color:#1c1e21;border:1px solid #ccd0d5;}
.btn-lg{padding:14px 28px;font-size:16px;}
.btn-sm{padding:6px 12px;font-size:13px;}
.btn-xs{padding:4px 8px;font-size:12px;font-weight:500;}
.btn-block{display:block;width:100%;}
.pull-right{float:right;}

/* ── Modern Forms ── */
.form-control{
  width:100%;
  padding:12px 16px;
  font-size:15px;
  border:1px solid #ccd0d5;
  border-radius:8px;
  background:#fff;
  transition:all 0.2s;
  font-family:inherit;
}
.form-control:focus{
  outline:none;
  border-color:#667eea;
  box-shadow:0 0 0 4px rgba(102,126,234,.1);
}
.form-group{margin-bottom:16px;}
label{display:block;margin-bottom:6px;font-weight:600;color:#1c1e21;font-size:14px;}
.form-inline{display:flex;gap:12px;align-items:center;flex-wrap:wrap;}
.form-inline .form-group{margin-bottom:0;}
.form-inline .form-control{width:auto;}
.form-inline label{margin-bottom:0;margin-right:8px;}

/* ── Modern Cards/Panels ── */
.panel{
  background:#fff;
  border-radius:12px;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
  margin-bottom:20px;
  overflow:hidden;
  transition:all 0.3s;
}
.panel:hover{box-shadow:0 8px 24px rgba(0,0,0,.12);}
.panel-heading{
  padding:20px 24px;
  font-weight:700;
  font-size:18px;
  border-bottom:1px solid #f0f2f5;
}
.panel-body{padding:24px;}
.panel-default .panel-heading{background:#f7f8fa;color:#1c1e21;}
.panel-info .panel-heading{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;}
.panel-success .panel-heading{background:linear-gradient(135deg,#56ab2f,#a8e063);color:#fff;}
.panel-warning .panel-heading{background:linear-gradient(135deg,#f093fb,#f5576c);color:#fff;}
.panel-danger .panel-heading{background:linear-gradient(135deg,#eb3349,#f45c43);color:#fff;}

/* ── Modern Alerts ── */
.alert{
  padding:16px 20px;
  border-radius:12px;
  margin-bottom:20px;
  font-weight:500;
  border:none;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
}
.alert-success{background:linear-gradient(135deg,#d4fc79,#96e6a1);color:#155724;}
.alert-info{background:linear-gradient(135deg,#a1c4fd,#c2e9fb);color:#0c5460;}
.alert-warning{background:linear-gradient(135deg,#ffecd2,#fcb69f);color:#856404;}
.alert-danger{background:linear-gradient(135deg,#fbc2eb,#f093fb);color:#721c24;}
.close{
  float:right;
  font-size:24px;
  font-weight:700;
  line-height:1;
  color:inherit;
  opacity:.5;
  background:none;
  border:none;
  cursor:pointer;
}
.close:hover{opacity:.8;}

/* ── Modern Tables ── */
.table{
  width:100%;
  border-collapse:separate;
  border-spacing:0;
  background:#fff;
  border-radius:12px;
  overflow:hidden;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
}
.table th{
  background:linear-gradient(135deg,#667eea,#764ba2);
  color:#fff;
  padding:16px;
  font-weight:600;
  text-align:left;
  border:none;
}
.table td{
  padding:14px 16px;
  border-bottom:1px solid #f0f2f5;
}
.table tbody tr:last-child td{border-bottom:none;}
.table-hover tbody tr{transition:all 0.2s;}
.table-hover tbody tr:hover{background:#f7f8fa;transform:scale(1.01);}
.table-striped tbody tr:nth-child(odd){background:#fafbfc;}

/* ── Labels & Badges ── */
.label,.badge{
  display:inline-block;
  padding:4px 10px;
  font-size:12px;
  font-weight:600;
  border-radius:12px;
  color:#fff;
}
.label-success{background:linear-gradient(135deg,#56ab2f,#a8e063);}
.label-info{background:linear-gradient(135deg,#00c6ff,#0072ff);}
.label-warning{background:linear-gradient(135deg,#f093fb,#f5576c);}
.label-danger{background:linear-gradient(135deg,#eb3349,#f45c43);}
.label-default{background:#65676b;}

/* ── Sidebar (Instagram style) ── */
.sidebar{
  position:fixed;
  left:0;
  top:60px;
  width:240px;
  height:calc(100vh - 60px);
  background:#fff;
  box-shadow:2px 0 8px rgba(0,0,0,.08);
  padding:20px 0;
  overflow-y:auto;
}
.sidebar a{
  display:flex;
  align-items:center;
  gap:12px;
  padding:12px 20px;
  color:#65676b;
  font-weight:500;
  transition:all 0.2s;
  border-left:3px solid transparent;
}
.sidebar a:hover,.sidebar a.active{
  background:linear-gradient(90deg,rgba(102,126,234,.1),transparent);
  color:#667eea;
  border-left-color:#667eea;
}
.sidebar .hdr{
  color:#8a8d91;
  font-size:12px;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:0.5px;
  padding:16px 20px 8px;
  margin-top:12px;
}

/* ── Main Content (with sidebar) ── */
.content-wrap{
  margin-left:240px;
  padding:80px 24px 24px;
  min-height:100vh;
}
.main-content{
  background:#fff;
  border-radius:16px;
  padding:32px;
  box-shadow:0 4px 12px rgba(0,0,0,.1);
  margin-bottom:24px;
}
.main-content-full{
  padding:80px 24px 24px;
  min-height:100vh;
}

/* ── Page Header ── */
.page-header{
  border-bottom:2px solid #f0f2f5;
  padding-bottom:16px;
  margin-bottom:24px;
}
.page-header h2{
  font-size:28px;
  font-weight:700;
  background:linear-gradient(135deg,#667eea,#764ba2);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  background-clip:text;
}

/* ── Stat Cards (Dashboard) ── */
.card-stat{
  text-align:center;
  padding:28px;
  border-radius:16px;
  color:#fff;
  box-shadow:0 4px 12px rgba(0,0,0,.15);
  transition:all 0.3s;
}
.card-stat:hover{transform:translateY(-8px);box-shadow:0 12px 24px rgba(0,0,0,.2);}
.card-stat h2{
  font-size:42px;
  font-weight:700;
  margin-bottom:8px;
  color:#fff;
}
.card-stat p{
  font-size:14px;
  font-weight:500;
  opacity:.9;
  margin:0;
}

/* ── Thumbnails (Home cards) ── */
.thumbnail{
  background:#fff;
  border-radius:16px;
  padding:28px;
  text-align:center;
  box-shadow:0 4px 12px rgba(0,0,0,.08);
  transition:all 0.3s;
  border:2px solid transparent;
  height:100%;
  display:flex;
  flex-direction:column;
  justify-content:center;
}
.thumbnail:hover{
  transform:translateY(-8px);
  box-shadow:0 12px 28px rgba(0,0,0,.15);
  border-color:#667eea;
}
.thumbnail h4{
  font-size:18px;
  font-weight:700;
  color:#1c1e21;
  margin:12px 0 8px;
}
.thumbnail .text-muted{
  color:#65676b;
  font-size:13px;
}

/* ── Footer ── */
footer{
  text-align:center;
  padding:24px;
  color:#8a8d91;
  font-size:14px;
  background:#fff;
  border-radius:12px;
  margin-top:24px;
  box-shadow:0 -2px 8px rgba(0,0,0,.05);
}

/* ── Utilities ── */
.text-center{text-align:center;}
.text-right{text-align:right;}
.text-muted{color:#65676b;}
.text-info{color:#0072ff;}
.text-danger{color:#f45c43;}
.text-success{color:#56ab2f;}
mark{background:#fff59d;padding:2px 6px;border-radius:4px;font-weight:600;}

/* ── Smooth Scrollbar ── */
::-webkit-scrollbar{width:8px;}
::-webkit-scrollbar-track{background:#f0f2f5;}
::-webkit-scrollbar-thumb{background:#ccd0d5;border-radius:4px;}
::-webkit-scrollbar-thumb:hover{background:#8a8d91;}
</style>
<script>
// Modern interactions
document.addEventListener('DOMContentLoaded',function(){
  // Close alert buttons
  document.querySelectorAll('.close').forEach(b=>{
    b.onclick=()=>b.parentElement.style.display='none';
  });
  
  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.onclick=e=>{
      e.preventDefault();
      document.querySelector(a.getAttribute('href'))?.scrollIntoView({behavior:'smooth'});
    };
  });
});
</script>
"""

def layout(title, body, session, active=""):
    user = session["HoTen"] if session else ""
    nav_links = ""
    if session:
        nav_links = f"""
        <li class="dropdown">
          <a href="#">
            👤 {user} ▾
          </a>
          <ul class="dropdown-menu">
            <li><a href="/logout">🚪 Đăng xuất</a></li>
          </ul>
        </li>"""

    if session:
        def li(href,icon,label,key):
            cls = "active" if active==key else ""
            return f'<a href="{href}" class="{cls}">{icon} {label}</a>'
        sidebar_html = f"""
        <div class="sidebar">
          <div class="hdr">Dashboard</div>
          {li("/","🏠","Trang chủ","home")}
          <div class="hdr">Quản lý</div>
          {li("/cauhoi","📝","Câu hỏi","cauhoi")}
          {li("/dethi","📄","Đề thi","dethi")}
          {li("/dethi/create","➕","Soạn đề mới","dethi_create")}
          {li("/ketqua","✏️","Nhập điểm","ketqua")}
          <div class="hdr">Tra cứu & Báo cáo</div>
          {li("/dethi/tracuu","🔍","Tra cứu đề","tracuu")}
          {li("/baocao","📊","Báo cáo năm","baocao")}
          <div class="hdr">Cài đặt</div>
          {li("/thamso","⚙️","Tham số","thamso")}
        </div>
        <div class="content-wrap">
          <div class="main-content">{body}</div>
          <footer>© 2026 Nhóm 15 – SE104.Q23 | 🎓 Quản Lý Ra Đề và Chấm Thi</footer>
        </div>"""
    else:
        sidebar_html = f'<div class="main-content-full">{body}</div><footer>© 2026 Nhóm 15 – SE104.Q23</footer>'

    return f"""<!DOCTYPE html><html lang="vi">
<head>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>{title} – Quản Lý Ra Đề & Chấm Thi</title>
{STYLE}
<script>
// Force reload when navigating - bypass cache completely
window.addEventListener('pageshow', function(event) {{
  if (event.persisted) {{
    window.location.reload(true);
  }}
}});
</script>
</head>
<body>
<nav class="navbar navbar-inverse" style="position:fixed;top:0;width:100%;z-index:1000;background:#222;min-height:50px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;">
  <a class="navbar-brand" href="/" style="color:#fff;font-size:18px;font-weight:bold;text-decoration:none;">🎓 Quản Lý Ra Đề &amp; Chấm Thi</a>
  <ul style="list-style:none;margin:0;padding:0;display:flex;position:relative;">{nav_links}</ul>
</nav>
{sidebar_html}
</body></html>"""

def alert(msg, kind="success"):
    icon = "✅" if kind=="success" else "❌"
    return f'<div class="alert alert-{kind} alert-dismissible"><button class="close" data-dismiss="alert">&times;</button>{icon} {msg}</div>'

# ══════════════════════════════════════════════════════════════════════
# ROUTE HANDLER
# ══════════════════════════════════════════════════════════════════════
class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silence logs

    def set_cookie(self, name, value, max_age=86400):
        """Set a cookie - call before end_headers()"""
        self.send_header("Set-Cookie", f"{name}={value}; Path=/; Max-Age={max_age}; HttpOnly")

    def send_html(self, html, code=200, headers=None):
        body = html.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type","text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Content-Length", str(len(body)))
        if headers:
            for k,v in headers.items():
                self.send_header(k,v)
        self.end_headers()
        self.wfile.write(body)

    def redirect(self, loc, extra_headers=None):
        # Use standard 302 redirect - cookie will carry session
        self.send_response(302)
        self.send_header("Location", loc)
        if extra_headers:
            for k,v in extra_headers.items():
                self.send_header(k,v)
        self.end_headers()

    def parse_body(self):
        length = int(self.headers.get("Content-Length",0))
        raw = self.rfile.read(length).decode("utf-8") if length else ""
        return urllib.parse.parse_qs(raw, keep_blank_values=True)

    def pv(self, form, key, default=""):
        return form.get(key,[""])[0] or default

    # ── PAGES ─────────────────────────────────────────────────────────
    def page_login(self, error=""):
        err_html = f'<div class="alert alert-danger">{error}</div>' if error else ""
        body = f"""
        <div style="max-width:440px;margin:80px auto;">
          <div style="background:#fff;border-radius:20px;padding:48px;box-shadow:0 20px 60px rgba(0,0,0,.3);">
            <div style="text-align:center;margin-bottom:24px;">
              <div style="font-size:72px;margin-bottom:8px;">🎓</div>
              <h1 style="font-size:28px;font-weight:700;background:linear-gradient(135deg,#667eea,#764ba2);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:8px;">
                Quản Lý Ra Đề & Chấm Thi
              </h1>
              <p style="color:#65676b;font-size:14px;margin:0;">Nhóm 15 – SE104.Q23</p>
            </div>
            {err_html}
            <form method="post" action="/login">
              <div class="form-group">
                <label>Tên đăng nhập</label>
                <input name="username" class="form-control" placeholder="Nhập tên đăng nhập" required autofocus>
              </div>
              <div class="form-group">
                <label>Mật khẩu</label>
                <input name="password" type="password" class="form-control" placeholder="Nhập mật khẩu" required>
              </div>
              <button type="submit" class="btn btn-primary btn-block btn-lg" style="margin-top:24px;">
                🔑 Đăng nhập
              </button>
            </form>
            <div style="text-align:center;margin-top:24px;padding-top:24px;border-top:1px solid #f0f2f5;">
              <p style="color:#65676b;font-size:13px;margin:0;">
                💡 Demo: <strong>gv01</strong> / <strong>123456</strong>
              </p>
            </div>
          </div>
        </div>"""
        return f"""<!DOCTYPE html><html lang="vi">
<head><title>Đăng nhập – Quản Lý Ra Đề &amp; Chấm Thi</title>{STYLE}</head>
<body style="display:flex;align-items:center;justify-content:center;min-height:100vh;">
{body}
</body></html>"""

    def page_home(self, session):
        import time
        sid_debug = self.sid if hasattr(self, 'sid') and self.sid else 'EMPTY!!!'
        print(f"[page_home] self.sid = {sid_debug}", flush=True)
        ts = int(time.time() * 1000)  # timestamp to bypass cache
        body = f"""
        <div class="page-header"><h2>🏠 Trang chủ</h2></div>
        <div class="alert alert-success"><h4>👋 Xin chào, <strong>{session['HoTen']}</strong>!</h4>
        Chào mừng đến với Hệ thống Quản lý Ra đề và Chấm thi.</div>
        <div class="row" style="margin-top:20px;">
          <div class="col-md-3">
            <a href="/cauhoi?_t={ts}" style="text-decoration:none;">
            <div class="thumbnail text-center" style="padding:20px;border:2px solid #3498db;">
              <div style="font-size:48px;">📋</div>
              <h4 style="color:#2c3e50;">Ngân hàng câu hỏi</h4>
              <p class="text-muted small">Soạn và quản lý câu hỏi</p>
            </div></a>
          </div>
          <div class="col-md-3">
            <a href="/dethi/create?_t={ts}" style="text-decoration:none;">
            <div class="thumbnail text-center" style="padding:20px;border:2px solid #27ae60;">
              <div style="font-size:48px;">➕</div>
              <h4 style="color:#2c3e50;">Soạn đề thi</h4>
              <p class="text-muted small">Tạo đề thi mới</p>
            </div></a>
          </div>
          <div class="col-md-3">
            <a href="/ketqua?_t={ts}" style="text-decoration:none;">
            <div class="thumbnail text-center" style="padding:20px;border:2px solid #e74c3c;">
              <div style="font-size:48px;">✏️</div>
              <h4 style="color:#2c3e50;">Nhập điểm</h4>
              <p class="text-muted small">Ghi nhận kết quả chấm thi</p>
            </div></a>
          </div>
          <div class="col-md-3">
            <a href="/baocao?_t={ts}" style="text-decoration:none;">
            <div class="thumbnail text-center" style="padding:20px;border:2px solid #f39c12;">
              <div style="font-size:48px;">📊</div>
              <h4 style="color:#2c3e50;">Báo cáo năm</h4>
              <p class="text-muted small">Thống kê phân loại điểm</p>
            </div></a>
          </div>
        </div>
        <div class="row" style="margin-top:15px;">
          <div class="col-md-6">
            <div class="panel panel-info">
              <div class="panel-heading">📖 Hướng dẫn sử dụng</div>
              <div class="panel-body">
                <ol>
                  <li>Vào <strong>Ngân hàng câu hỏi</strong> để thêm câu hỏi</li>
                  <li>Vào <strong>Soạn đề thi</strong> để tạo đề từ ngân hàng</li>
                  <li>Sau khi thi, vào <strong>Nhập điểm</strong> để ghi nhận kết quả</li>
                  <li>Xem <strong>Báo cáo năm</strong> để thống kê tổng kết</li>
                </ol>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="panel panel-warning">
              <div class="panel-heading">📌 Quy định hệ thống</div>
              <div class="panel-body">
                <ul>
                  <li>Mỗi đề thi tối đa <strong>5 câu hỏi</strong></li>
                  <li>Thời lượng thi: <strong>30 – 180 phút</strong></li>
                  <li>Điểm số: <strong>0.0 – 10.0</strong></li>
                  <li>Điểm chữ tự động tính theo bảng quy đổi</li>
                </ul>
              </div>
            </div>
          </div>
        </div>"""
        return layout("Trang chủ", body, session, "home")

    def page_cauhoi(self, session, flash=""):
        conn = get_db()
        cur = conn.cursor()
        ma_gv = session["MaGV"]
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        f_mon = params.get("maMonFilter",[""])[0]
        f_dk  = params.get("maDoKhoFilter",[""])[0]
        f_search = params.get("search",[""])[0].strip()

        sql = """SELECT c.MaCH, c.NoiDung, m.TenMon, d.TenDoKho, d.MaDoKho
                 FROM CAU_HOI c
                 JOIN MON_HOC m ON m.MaMon=c.MaMon
                 JOIN DO_KHO d ON d.MaDoKho=c.MaDoKho
                 WHERE m.MaGV=?"""
        args = [ma_gv]
        if f_search: 
            sql += " AND c.NoiDung LIKE ?"
            args.append(f"%{f_search}%")
        if f_mon: sql += " AND c.MaMon=?"; args.append(f_mon)
        if f_dk:  sql += " AND c.MaDoKho=?"; args.append(f_dk)
        rows = cur.execute(sql, args).fetchall()
        monhocs = cur.execute("SELECT MaMon,TenMon FROM MON_HOC WHERE MaGV=?", (ma_gv,)).fetchall()
        dokhoes = cur.execute("SELECT MaDoKho,TenDoKho FROM DO_KHO").fetchall()
        
        # Đếm số câu hỏi theo môn để cảnh báo
        mon_counts = {}
        for mh in monhocs:
            count = cur.execute("SELECT COUNT(*) FROM CAU_HOI WHERE MaMon=?", (mh[0],)).fetchone()[0]
            mon_counts[mh[0]] = count
        
        release_db(conn)

        mon_opts = "<option value=''>-- Tất cả --</option>" + "".join(
            f"<option value='{r[0]}' {'selected' if str(r[0])==f_mon else ''}>{r[1]}</option>" for r in monhocs)
        dk_opts = "<option value=''>-- Tất cả --</option>" + "".join(
            f"<option value='{r[0]}' {'selected' if str(r[0])==f_dk else ''}>{r[1]}</option>" for r in dokhoes)

        dk_badge = {1:("success","Dễ"),2:("info","Trung Bình"),3:("warning","Phức Tạp"),4:("danger","Khó")}
        rows_html = ""
        for r in rows:
            bclass, btext = dk_badge.get(r[4], ("default","?"))
            nd = r[1][:90]+"..." if len(r[1])>90 else r[1]
            # Highlight từ khóa tìm kiếm
            if f_search and f_search.lower() in nd.lower():
                import re
                nd = re.sub(f"({re.escape(f_search)})", r'<mark style="background:#ff0;padding:2px 4px;font-weight:bold;">\1</mark>', nd, flags=re.IGNORECASE)
            rows_html += f"""<tr>
              <td>{r[0]}</td>
              <td>{nd}</td>
              <td>{r[2]}</td>
              <td><span class="label label-{bclass}">{r[3]}</span></td>
              <td>
                <a href="/cauhoi/edit/{r[0]}?sid={self.sid}" class="btn btn-xs btn-warning">✏️ Sửa</a>
                <a href="/cauhoi/delete/{r[0]}?sid={self.sid}" class="btn btn-xs btn-danger"
                   onclick="return confirm('Xóa câu hỏi này?')">🗑️ Xóa</a>
              </td>
            </tr>"""
        if not rows_html:
            rows_html = "<tr><td colspan='5' class='text-center text-muted'><i>Chưa có câu hỏi nào</i></td></tr>"

        search_value = params.get("search",[""])[0]
        search_info = f'<div class="alert alert-info">🔍 Tìm kiếm: "<strong>{search_value}</strong>" - Tìm thấy <strong>{len(rows)}</strong> kết quả</div>' if search_value else ""
        
        # Cảnh báo thiếu câu hỏi
        warnings_html = ""
        low_question_subjects = [(mh[1], mon_counts[mh[0]]) for mh in monhocs if mon_counts[mh[0]] < 10]
        if low_question_subjects:
            warnings_list = "".join([f"<li><strong>{mh[0]}</strong>: {mh[1]} câu hỏi</li>" for mh in low_question_subjects])
            warnings_html = f"""
            <div class="alert alert-warning">
              <strong>⚠️ Cảnh báo thiếu câu hỏi!</strong>
              <p style="margin:8px 0 0 0;">Các môn học sau cần bổ sung thêm câu hỏi (tối thiểu 10 câu):</p>
              <ul style="margin:8px 0 0 20px;">{warnings_list}</ul>
            </div>"""
        
        body = f"""
        <div class="page-header"><h2>📋 Ngân hàng câu hỏi</h2></div>
        {flash}
        {warnings_html}
        <div class="panel panel-default">
          <div class="panel-body">
            <form class="form-inline" method="get" style="margin-bottom:10px;">
              <input type="hidden" name="sid" value="{self.sid}">
              <div class="form-group">
                <input type="text" name="search" class="form-control" placeholder="🔍 Tìm kiếm nội dung câu hỏi..." 
                       value="{search_value}" style="width:300px;margin-right:10px;">
              </div>
              <button class="btn btn-primary">🔎 Tìm</button>
              <a href="/cauhoi?sid={self.sid}" class="btn btn-default">Xóa tìm kiếm</a>
            </form>
            <form class="form-inline" method="get">
              <input type="hidden" name="sid" value="{self.sid}">
              <input type="hidden" name="search" value="{search_value}">
              <div class="form-group">Môn học: <select name="maMonFilter" class="form-control" style="margin:0 10px;">{mon_opts}</select></div>
              <div class="form-group">Độ khó: <select name="maDoKhoFilter" class="form-control" style="margin:0 10px;">{dk_opts}</select></div>
              <button class="btn btn-info">🔍 Lọc</button>
              <a href="/cauhoi?search={search_value}&sid={self.sid}" class="btn btn-default">Xóa lọc</a>
              <a href="/cauhoi/create?sid={self.sid}" class="btn btn-success pull-right">➕ Thêm câu hỏi</a>
            </form>
          </div>
        </div>
        {search_info}
        <table class="table table-bordered table-striped table-hover">
          <thead><tr><th>Mã CH</th><th>Nội dung</th><th>Môn học</th><th>Độ khó</th><th>Thao tác</th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>
        <p class="text-muted">Tổng số: <strong>{len(rows)}</strong> câu hỏi</p>"""
        return layout("Câu hỏi", body, session, "cauhoi")

    def page_cauhoi_create(self, session, flash="", old=None):
        conn = get_db(); cur = conn.cursor()
        monhocs = cur.execute("SELECT MaMon,TenMon FROM MON_HOC WHERE MaGV=?", (session["MaGV"],)).fetchall()
        dokhoes = cur.execute("SELECT MaDoKho,TenDoKho FROM DO_KHO").fetchall()
        release_db(conn)
        old = old or {}
        mon_opts = "<option value=''>-- Chọn môn học --</option>" + "".join(
            f"<option value='{r[0]}' {'selected' if old.get('mon')==str(r[0]) else ''}>{r[1]}</option>" for r in monhocs)
        dk_opts = "<option value=''>-- Chọn độ khó --</option>" + "".join(
            f"<option value='{r[0]}' {'selected' if old.get('dk')==str(r[0]) else ''}>{r[1]}</option>" for r in dokhoes)
        body = f"""
        <div class="page-header"><h2>➕ Thêm câu hỏi mới</h2></div>
        {flash}
        <form method="post" action="/cauhoi/create?sid={self.sid}">
          <input type="hidden" name="sid" value="{self.sid}">
          <div class="panel panel-default"><div class="panel-body">
            <div class="form-group">
              <label>Môn học <span class="text-danger">*</span></label>
              <select name="MaMon" class="form-control" required>{mon_opts}</select>
            </div>
            <div class="form-group">
              <label>Độ khó <span class="text-danger">*</span></label>
              <select name="MaDoKho" class="form-control" required>{dk_opts}</select>
            </div>
            <div class="form-group">
              <label>Nội dung câu hỏi <span class="text-danger">*</span></label>
              <textarea name="NoiDung" class="form-control" rows="4" placeholder="Nhập nội dung câu hỏi..." required>{old.get('nd','')}</textarea>
            </div>
            <button class="btn btn-primary">💾 Lưu câu hỏi</button>
            <a href="/cauhoi?sid={self.sid}" class="btn btn-default">← Quay lại</a>
          </div></div>
        </form>"""
        return layout("Thêm câu hỏi", body, session, "cauhoi")

    def page_cauhoi_edit(self, session, mach, flash=""):
        conn = get_db(); cur = conn.cursor()
        row = cur.execute("SELECT MaCH,NoiDung,MaMon,MaDoKho FROM CAU_HOI WHERE MaCH=?", (mach,)).fetchone()
        monhocs = cur.execute("SELECT MaMon,TenMon FROM MON_HOC WHERE MaGV=?", (session["MaGV"],)).fetchall()
        dokhoes = cur.execute("SELECT MaDoKho,TenDoKho FROM DO_KHO").fetchall()
        release_db(conn)
        if not row: return self.send_html("Not found", 404)
        mon_opts = "".join(
            f"<option value='{r[0]}' {'selected' if r[0]==row[2] else ''}>{r[1]}</option>" for r in monhocs)
        dk_opts = "".join(
            f"<option value='{r[0]}' {'selected' if r[0]==row[3] else ''}>{r[1]}</option>" for r in dokhoes)
        body = f"""
        <div class="page-header"><h2>✏️ Sửa câu hỏi #{row[0]}</h2></div>
        {flash}
        <form method="post" action="/cauhoi/edit/{row[0]}?sid={self.sid}">
          <input type="hidden" name="sid" value="{self.sid}">
          <div class="panel panel-default"><div class="panel-body">
            <div class="form-group">
              <label>Môn học</label>
              <select name="MaMon" class="form-control">{mon_opts}</select>
            </div>
            <div class="form-group">
              <label>Độ khó</label>
              <select name="MaDoKho" class="form-control">{dk_opts}</select>
            </div>
            <div class="form-group">
              <label>Nội dung câu hỏi</label>
              <textarea name="NoiDung" class="form-control" rows="4">{row[1]}</textarea>
            </div>
            <button class="btn btn-primary">💾 Cập nhật</button>
            <a href="/cauhoi?sid={self.sid}" class="btn btn-default">← Quay lại</a>
          </div></div>
        </form>"""
        return layout("Sửa câu hỏi", body, session, "cauhoi")

    def page_dethi_list(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        
        # Lấy filter từ query string
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        filter_type = params.get("filter",[""])[0]
        
        rows = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.ThoiLuong,d.NgayThi,
                                    (SELECT COUNT(*) FROM CT_DETHI WHERE MaDT=d.MaDT),
                                    (SELECT COUNT(*) FROM KET_QUA WHERE MaDT=d.MaDT)
                              FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                              WHERE d.MaGV=? ORDER BY d.MaDT DESC""", (session["MaGV"],)).fetchall()
        
        # Filter đề chưa chấm
        if filter_type == "unchecked":
            rows = [r for r in rows if r[7] == 0]
        
        release_db(conn)
        rows_html = ""
        for r in rows:
            ngay = r[5] if r[5] else "--"
            # Badge cho trạng thái chấm
            status_badge = f'<span class="label label-success">✓ Đã chấm ({r[7]} SV)</span>' if r[7] > 0 else '<span class="label label-warning">⏳ Chưa chấm</span>'
            rows_html += f"""<tr>
              <td>DT-{r[0]:03d}</td><td>{r[1]}</td>
              <td><span class="badge">HK {r[2]}</span></td>
              <td>{r[3]}</td><td>{r[4]} phút</td><td>{ngay}</td>
              <td>{status_badge}</td>
              <td>
                <a href="/dethi/{r[0]}?sid={self.sid}" class="btn btn-xs btn-info">👁 Xem</a>
                <a href="/ketqua/nhap/{r[0]}?sid={self.sid}" class="btn btn-xs btn-warning">✏️ Nhập điểm</a>
              </td>
            </tr>"""
        if not rows_html:
            rows_html = "<tr><td colspan='8' class='text-center text-muted'><i>Chưa có đề thi nào</i></td></tr>"
        
        filter_active = ' class="active"' if filter_type == "unchecked" else ""
        filter_btns = f"""
        <div class="btn-group" style="margin-bottom:15px;">
          <a href="/dethi?sid={self.sid}" class="btn btn-default">📋 Tất cả</a>
          <a href="/dethi?filter=unchecked&sid={self.sid}" class="btn btn-warning{filter_active}">⏳ Chưa chấm</a>
        </div>"""
        
        body = f"""
        <div class="page-header"><h2>📄 Danh sách đề thi</h2></div>
        {flash}
        <div style="margin-bottom:15px;">
          <a href="/dethi/create?sid={self.sid}" class="btn btn-success">➕ Soạn đề thi mới</a>
          <a href="/dethi/tracuu?sid={self.sid}" class="btn btn-info">🔍 Tra cứu</a>
        </div>
        {filter_btns}
        <table class="table table-bordered table-striped table-hover">
          <thead><tr><th>Mã ĐT</th><th>Môn học</th><th>HK</th><th>Năm học</th><th>Thời lượng</th><th>Ngày thi</th><th>Trạng thái</th><th>Thao tác</th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>
        <p class="text-muted">Tổng số: <strong>{len(rows)}</strong> đề thi</p>"""
        return layout("Đề thi", body, session, "dethi")

    def page_dethi_create(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        monhocs = cur.execute("SELECT MaMon,TenMon FROM MON_HOC WHERE MaGV=?", (session["MaGV"],)).fetchall()
        dokhoes = cur.execute("SELECT MaDoKho,TenDoKho FROM DO_KHO").fetchall()
        release_db(conn)
        mon_opts = "<option value=''>-- Chọn môn học --</option>" + "".join(
            f"<option value='{r[0]}'>{r[1]}</option>" for r in monhocs)
        dk_opts = "<option value=''>Tất cả độ khó</option>" + "".join(
            f"<option value='{r[0]}'>{r[1]}</option>" for r in dokhoes)
        body = f"""
        <div class="page-header"><h2>➕ Soạn đề thi mới</h2></div>
        {flash}
        <form method="post" action="/dethi/create?sid={self.sid}">
          <input type="hidden" name="sid" value="{self.sid}">
          <div class="row">
            <div class="col-md-5">
              <div class="panel panel-primary">
                <div class="panel-heading">📝 Thông tin đề thi</div>
                <div class="panel-body">
                  <div class="form-group">
                    <label>Môn học <span class="text-danger">*</span></label>
                    <select name="MaMon" id="ddlMon" class="form-control" required>{mon_opts}</select>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group"><label>Học kỳ</label>
                        <select name="HocKy" class="form-control">
                          <option value="1">Học kỳ 1</option>
                          <option value="2">Học kỳ 2</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group"><label>Năm học</label>
                        <input name="NamHoc" class="form-control" placeholder="2024-2025" value="{date.today().year-1}-{date.today().year}" required>
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group"><label>Thời lượng (phút)</label>
                        <input name="ThoiLuong" type="number" class="form-control" min="30" max="180" value="90" required>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group"><label>Ngày thi</label>
                        <input name="NgayThi" type="date" class="form-control">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="panel panel-success">
                <div class="panel-heading">✅ Câu hỏi đã chọn: <span id="cnt">0</span>/5</div>
                <div class="panel-body" id="chosen" style="min-height:60px;"><em class="text-muted">Chưa chọn câu hỏi nào</em></div>
              </div>
              <div id="hidden_inputs"></div>
              <button type="submit" class="btn btn-primary btn-block btn-lg">💾 Lưu đề thi</button>
              <a href="/dethi?sid={self.sid}" class="btn btn-default btn-block" style="margin-top:5px;">← Hủy bỏ</a>
            </div>
            <div class="col-md-7">
              <div class="panel panel-default">
                <div class="panel-heading">📚 Ngân hàng câu hỏi <small class="text-warning">(Tối đa 5 câu)</small></div>
                <div class="panel-body">
                  <div class="form-inline" style="margin-bottom:10px;">
                    Lọc độ khó: <select id="fdk" class="form-control" style="margin:0 8px;">{dk_opts}</select>
                    <button type="button" class="btn btn-default btn-sm" onclick="loadCauHoi()">🔍 Lọc</button>
                  </div>
                  <div id="cauhoiList" style="max-height:420px;overflow-y:auto;">
                    <em class="text-muted">Hãy chọn môn học trước ↑</em>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </form>
        <script>
        var sel = [];
        document.getElementById('ddlMon').addEventListener('change', loadCauHoi);
        function loadCauHoi(){{
          var mon = document.getElementById('ddlMon').value;
          var dk = document.getElementById('fdk').value;
          if(!mon)return;
          fetch('/api/cauhoi?maMon='+mon+'&maDoKho='+dk)
            .then(function(r){{return r.json();}}).then(function(data){{
              var html='';
              if(data.length===0){{html='<em style="color:#999;">Không có câu hỏi nào</em>';}}
              data.forEach(function(c){{
                var chk = sel.indexOf(c.MaCH)!==-1;
                var colors=['','#5cb85c','#5bc0de','#f0ad4e','#d9534f'];
                var clr = colors[c.MaDoKho]||'#777';
                html += '<div style="border-bottom:1px solid #eee;padding:8px 4px;">';
                html += '<label style="font-weight:normal;cursor:pointer;">';
                html += '<input type="checkbox" class="ckCH" value="'+c.MaCH+'" '+(chk?'checked':'')+' onchange="toggle(this,'+c.MaCH+')" style="margin-right:6px;"> ';
                html += '<strong>#'+c.MaCH+'</strong> '+c.NoiDung.substring(0,80)+(c.NoiDung.length>80?'...':'');
                html += ' <span style="background:'+clr+';color:#fff;padding:2px 6px;border-radius:3px;font-size:11px;">'+c.TenDoKho+'</span>';
                html += '</label></div>';
              }});
              document.getElementById('cauhoiList').innerHTML = html;
            }});
        }}
        function toggle(el, id){{
          if(el.checked){{
            if(sel.length>=5){{alert('Chỉ được chọn tối đa 5 câu hỏi!');el.checked=false;return;}}
            sel.push(id);
          }} else {{ sel=sel.filter(function(x){{return x!==id;}}); }}
          renderChosen();
        }}
        function remove(id){{
          sel=sel.filter(function(x){{return x!==id;}});
          var el=document.querySelector('.ckCH[value="'+id+'"]');
          if(el) el.checked=false;
          renderChosen();
        }}
        function renderChosen(){{
          document.getElementById('cnt').textContent=sel.length;
          var html=''; var hinputs='';
          if(sel.length===0){{html='<em style="color:#999;">Chưa chọn câu hỏi nào</em>';}}
          sel.forEach(function(id){{
            html+='<div style="background:#dff0d8;border:1px solid #d6e9c6;padding:5px 10px;margin-bottom:4px;border-radius:3px;">✅ Câu hỏi #'+id;
            html+=' <a href="#" onclick="remove('+id+');return false;" style="float:right;color:#333;font-weight:bold;">&times;</a></div>';
            hinputs+='<input type="hidden" name="CauHoi" value="'+id+'">';
          }});
          document.getElementById('chosen').innerHTML=html;
          document.getElementById('hidden_inputs').innerHTML=hinputs;
        }}
        </script>"""
        return layout("Soạn đề thi", body, session, "dethi_create")

    def page_dethi_detail(self, session, maDT):
        conn = get_db(); cur = conn.cursor()
        dt = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.ThoiLuong,d.NgayThi
                            FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                            WHERE d.MaDT=? AND d.MaGV=?""", (maDT, session["MaGV"])).fetchone()
        if not dt: conn.close(); return self.send_html("Not found",404)
        cauHois = cur.execute("""SELECT c.MaCH,c.NoiDung,dk.TenDoKho,dk.MaDoKho
                                 FROM CT_DETHI ct
                                 JOIN CAU_HOI c ON c.MaCH=ct.MaCH
                                 JOIN DO_KHO dk ON dk.MaDoKho=c.MaDoKho
                                 WHERE ct.MaDT=?""", (maDT,)).fetchall()
        conn.close()
        ngay = dt[5] if dt[5] else "Chưa xác định"
        dk_badge = {1:"success",2:"info",3:"warning",4:"danger"}
        chs = ""
        for i,c in enumerate(cauHois):
            bclass = dk_badge.get(c[3],"default")
            chs += f"""<div class="well well-sm" style="margin-bottom:8px;">
              <strong>Câu {i+1}:</strong>
              <span class="label label-{bclass} pull-right">{c[2]}</span>
              <p style="margin-top:5px;margin-bottom:0;">{c[1]}</p>
            </div>"""
        if not chs: chs = "<p class='text-muted'>Chưa có câu hỏi nào trong đề.</p>"
        body = f"""
        <div class="page-header"><h2>📄 Chi tiết đề thi DT-{dt[0]:03d} <small>{dt[1]}</small></h2></div>
        <div class="row">
          <div class="col-md-4">
            <div class="panel panel-info">
              <div class="panel-heading">ℹ️ Thông tin đề thi</div>
              <div class="panel-body">
                <table class="table table-condensed" style="margin:0;">
                  <tr><th>Mã đề:</th><td>DT-{dt[0]:03d}</td></tr>
                  <tr><th>Môn:</th><td>{dt[1]}</td></tr>
                  <tr><th>Học kỳ:</th><td>HK {dt[2]}</td></tr>
                  <tr><th>Năm học:</th><td>{dt[3]}</td></tr>
                  <tr><th>Thời lượng:</th><td>{dt[4]} phút</td></tr>
                  <tr><th>Ngày thi:</th><td>{ngay}</td></tr>
                  <tr><th>Số câu:</th><td><span class="badge">{len(cauHois)}</span></td></tr>
                </table>
              </div>
            </div>
            <a href="/ketqua/nhap/{dt[0]}?sid={self.sid}" class="btn btn-warning btn-block">✏️ Nhập điểm</a>
            <a href="/dethi?sid={self.sid}" class="btn btn-default btn-block" style="margin-top:5px;">← Danh sách</a>
          </div>
          <div class="col-md-8">
            <div class="panel panel-default">
              <div class="panel-heading">📚 Danh sách câu hỏi trong đề</div>
              <div class="panel-body">{chs}</div>
            </div>
          </div>
        </div>"""
        return layout("Chi tiết đề thi", body, session, "dethi")

    def page_dethi_tracuu(self, session):
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        f_mon  = params.get("tenMon",[""])[0]
        f_hk   = params.get("hocKy",[""])[0]
        f_nam  = params.get("namHoc",[""])[0]
        conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
        sql = """SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.ThoiLuong,d.NgayThi
                 FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                 WHERE d.MaGV=?"""
        args = [session["MaGV"]]
        if f_mon: sql += " AND m.TenMon LIKE ?"; args.append(f"%{f_mon}%")
        if f_hk:  sql += " AND d.HocKy=?"; args.append(f_hk)
        if f_nam: sql += " AND d.NamHoc=?"; args.append(f_nam)
        sql += " ORDER BY d.MaDT DESC"
        rows = cur.execute(sql, args).fetchall()
        namhocs = [r[0] for r in cur.execute("SELECT DISTINCT NamHoc FROM DE_THI WHERE MaGV=? ORDER BY NamHoc DESC", (session["MaGV"],)).fetchall()]
        conn.close()
        nam_opts = "<option value=''>-- Tất cả --</option>" + "".join(
            f"<option value='{n}' {'selected' if n==f_nam else ''}>{n}</option>" for n in namhocs)
        rows_html = ""
        for r in rows:
            ngay = r[5] if r[5] else "--"
            rows_html += f"""<tr>
              <td>DT-{r[0]:03d}</td><td>{r[1]}</td>
              <td><span class="badge">HK {r[2]}</span></td>
              <td>{r[3]}</td><td>{r[4]} phút</td><td>{ngay}</td>
              <td><a href="/dethi/{r[0]}?sid={self.sid}" class="btn btn-xs btn-info">👁 Chi tiết</a></td>
            </tr>"""
        if not rows_html:
            rows_html = "<tr><td colspan='7' class='text-center text-muted'><i>Không tìm thấy kết quả</i></td></tr>"
        hk_sel = lambda v: "selected" if f_hk==str(v) else ""
        body = f"""
        <div class="page-header"><h2>🔍 Tra cứu đề thi</h2></div>
        <div class="panel panel-default">
          <div class="panel-heading">Bộ lọc</div>
          <div class="panel-body">
            <form class="form-inline" method="get">
              <input type="hidden" name="sid" value="{self.sid}">
              <div class="form-group">Môn: <input name="tenMon" class="form-control" value="{f_mon}" style="margin:0 8px;width:180px;"></div>
              <div class="form-group">HK: <select name="hocKy" class="form-control" style="margin:0 8px;">
                <option value="">Tất cả</option>
                <option value="1" {hk_sel(1)}>HK 1</option>
                <option value="2" {hk_sel(2)}>HK 2</option>
              </select></div>
              <div class="form-group">Năm học: <select name="namHoc" class="form-control" style="margin:0 8px;">{nam_opts}</select></div>
              <button class="btn btn-primary">🔍 Tìm</button>
            </form>
          </div>
        </div>
        <p>Tìm thấy <strong>{len(rows)}</strong> đề thi</p>
        <table class="table table-bordered table-striped table-hover">
          <thead><tr><th>Mã ĐT</th><th>Môn</th><th>HK</th><th>Năm học</th><th>Thời lượng</th><th>Ngày thi</th><th></th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>"""
        return layout("Tra cứu", body, session, "tracuu")

    def page_ketqua(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        rows = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.NgayThi
                              FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                              WHERE d.MaGV=? ORDER BY d.MaDT DESC""", (session["MaGV"],)).fetchall()
        conn.close()
        rows_html = ""
        for r in rows:
            rows_html += f"""<tr>
              <td>DT-{r[0]:03d}</td><td>{r[1]}</td>
              <td><span class="badge">HK {r[2]}</span></td><td>{r[3]}</td>
              <td>{r[4] or '--'}</td>
              <td><a href="/ketqua/nhap/{r[0]}?sid={self.sid}" class="btn btn-sm btn-warning">✏️ Nhập điểm</a></td>
            </tr>"""
        if not rows_html:
            rows_html = "<tr><td colspan='6' class='text-center text-muted'><i>Chưa có đề thi nào</i></td></tr>"
        body = f"""
        <div class="page-header"><h2>✏️ Nhập điểm – Chọn đề thi</h2></div>
        {flash}
        <div class="alert alert-info">ℹ️ Chọn một đề thi để nhập điểm. Điểm chữ sẽ được tự động tính.</div>
        <table class="table table-bordered table-striped table-hover">
          <thead><tr><th>Mã ĐT</th><th>Môn</th><th>HK</th><th>Năm học</th><th>Ngày thi</th><th></th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>"""
        return layout("Nhập điểm", body, session, "ketqua")

    def page_nhap_diem(self, session, maDT, flash=""):
        conn = get_db(); cur = conn.cursor()
        dt = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc
                            FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                            WHERE d.MaDT=? AND d.MaGV=?""", (maDT, session["MaGV"])).fetchone()
        if not dt: conn.close(); return self.send_html("Not found",404)
        svs = cur.execute("""SELECT s.MaSV,s.HoTen,l.TenLop,
                             (SELECT DiemSo FROM KET_QUA WHERE MaSV=s.MaSV AND MaDT=?),
                             (SELECT DiemChu FROM KET_QUA WHERE MaSV=s.MaSV AND MaDT=?),
                             (SELECT NgayCham FROM KET_QUA WHERE MaSV=s.MaSV AND MaDT=?)
                             FROM SINH_VIEN s JOIN LOP_HOC l ON l.MaLop=s.MaLop
                             WHERE l.NamHoc=? AND l.MaGV=?
                             ORDER BY l.TenLop,s.HoTen""",
                          (maDT, maDT, maDT, dt[3], session["MaGV"])).fetchall()
        conn.close()
        da_cham = sum(1 for s in svs if s[3] is not None)
        rows_html = ""
        for i,s in enumerate(svs):
            diem_str = str(s[3]) if s[3] is not None else ""
            diem_chu = s[4] or "--"
            ngay = s[5] or "--"
            cls = "label-" + label_class(s[4]) if s[4] else "label-default"
            row_cls = "success" if s[3] is not None else ""
            print_btn = f'<a href="/ketqua/phieu/{maDT}/{s[0]}?sid={self.sid}" class="btn btn-xs btn-info" target="_blank" title="In phiếu điểm">🖨️</a>' if s[3] is not None else ""
            rows_html += f"""<tr class="{row_cls}">
              <td>{i+1}</td><td>{s[1]}</td><td>{s[2]}</td>
              <td>
                <input type="hidden" name="maSV" value="{s[0]}">
                <input type="number" name="diemSo" value="{diem_str}"
                       min="0" max="10" step="0.25" class="form-control input-sm diem-input"
                       style="width:90px;" onchange="tinhChu(this,{i})" placeholder="0-10">
              </td>
              <td><span id="chu_{i}" class="label {cls}">{diem_chu}</span></td>
              <td class="text-muted small">{ngay}</td>
              <td>{print_btn}</td>
            </tr>"""
        body = f"""
        <div class="page-header">
          <h2>✏️ Nhập điểm – {dt[1]} <small>HK{dt[2]} – {dt[3]}</small></h2>
        </div>
        {flash}
        <p>Tổng: <strong>{len(svs)}</strong> SV | Đã chấm: <strong>{da_cham}</strong> | Chưa chấm: <strong>{len(svs)-da_cham}</strong></p>
        <form method="post" action="/ketqua/luu/{maDT}?sid={self.sid}">
          <input type="hidden" name="sid" value="{self.sid}">
          <table class="table table-bordered table-striped">
            <thead><tr><th>STT</th><th>Họ tên</th><th>Lớp</th><th>Điểm số</th><th>Điểm chữ</th><th>Ngày chấm</th><th>In</th></tr></thead>
            <tbody>{rows_html}</tbody>
          </table>
          <button class="btn btn-primary btn-lg">💾 Lưu tất cả điểm</button>
          <a href="/ketqua?sid={self.sid}" class="btn btn-default btn-lg">← Quay lại</a>
        </form>
        <script>
        var bang=[
          {{tu:8.5,den:10,chu:'A',cls:'label-success'}},
          {{tu:8.0,den:8.49,chu:'B+',cls:'label-info'}},
          {{tu:7.0,den:7.99,chu:'B',cls:'label-info'}},
          {{tu:6.5,den:6.99,chu:'C+',cls:'label-warning'}},
          {{tu:5.5,den:6.49,chu:'C',cls:'label-warning'}},
          {{tu:5.0,den:5.49,chu:'D+',cls:'label-default'}},
          {{tu:4.0,den:4.99,chu:'D',cls:'label-default'}},
          {{tu:0.0,den:3.99,chu:'F',cls:'label-danger'}}
        ];
        function tinhChu(el,i){{
          var v=parseFloat(el.value);
          var sp=document.getElementById('chu_'+i);
          if(isNaN(v)||v<0||v>10){{sp.textContent='--';sp.className='label label-default';return;}}
          for(var b of bang){{if(v>=b.tu&&v<=b.den){{sp.textContent=b.chu;sp.className='label '+b.cls;break;}}}}
        }}
        </script>"""
        return layout("Nhập điểm", body, session, "ketqua")

    def page_baocao(self, session):
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
        namhocs = [r[0] for r in cur.execute(
            "SELECT DISTINCT NamHoc FROM DE_THI WHERE MaGV=? ORDER BY NamHoc DESC",
            (session["MaGV"],)).fetchall()]
        f_nam = params.get("namHoc",[""])[0] or (namhocs[0] if namhocs else "")
        bao_cao = []
        if f_nam:
            deThis = cur.execute(
                "SELECT d.MaDT,m.TenMon,d.HocKy FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon WHERE d.MaGV=? AND d.NamHoc=?",
                (session["MaGV"], f_nam)).fetchall()
            for dt in deThis:
                kqs = cur.execute("SELECT DiemSo,DiemChu FROM KET_QUA WHERE MaDT=?", (dt[0],)).fetchall()
                if not kqs: continue
                total = len(kqs)
                counts = {c: sum(1 for k in kqs if k[1]==c) for c in ["A","B+","B","C+","C","D+","D","F"]}
                avg = sum(k[0] for k in kqs)/total
                bao_cao.append((dt[1], dt[2], total, counts, avg))
        conn.close()
        nam_opts = "".join(f"<option value='{n}' {'selected' if n==f_nam else ''}>{n}</option>" for n in namhocs)

        bao_html = ""
        total_sv = total_f = 0
        total_kha = 0
        for bc in bao_cao:
            total_sv += bc[2]; total_f += bc[3]["F"]; total_kha += bc[3]["A"]+bc[3]["B+"]+bc[3]["B"]
            tl_dao = (bc[2]-bc[3]["F"])/bc[2]*100 if bc[2] else 0
            def pct(k): return f"{bc[3][k]/bc[2]*100:.0f}%" if bc[2] else "0%"
            bao_html += f"""
            <div class="panel panel-default">
              <div class="panel-heading">
                <h4 style="margin:0;">📘 {bc[0]} <span class="badge">HK {bc[1]}</span>
                  <span class="text-info" style="font-size:13px;margin-left:15px;">
                    Tổng: {bc[2]} SV | ĐTB: {bc[4]:.2f} | Tỉ lệ đỗ: {tl_dao:.1f}%
                  </span>
                </h4>
              </div>
              <div class="panel-body">
                <table class="table table-bordered text-center">
                  <thead><tr>
                    <th style="background:#27ae60;color:#fff;">A<br><small>≥8.5</small></th>
                    <th style="background:#2980b9;color:#fff;">B+<br><small>8.0-8.4</small></th>
                    <th style="background:#3498db;color:#fff;">B<br><small>7.0-7.9</small></th>
                    <th style="background:#f39c12;color:#fff;">C+<br><small>6.5-6.9</small></th>
                    <th style="background:#e67e22;color:#fff;">C<br><small>5.5-6.4</small></th>
                    <th style="background:#95a5a6;color:#fff;">D+<br><small>5.0-5.4</small></th>
                    <th style="background:#7f8c8d;color:#fff;">D<br><small>4.0-4.9</small></th>
                    <th style="background:#e74c3c;color:#fff;">F<br><small>&lt;4.0</small></th>
                  </tr></thead>
                  <tbody><tr>
                    <td><strong>{bc[3]['A']}</strong><br><small>{pct('A')}</small></td>
                    <td><strong>{bc[3]['B+']}</strong><br><small>{pct('B+')}</small></td>
                    <td><strong>{bc[3]['B']}</strong><br><small>{pct('B')}</small></td>
                    <td><strong>{bc[3]['C+']}</strong><br><small>{pct('C+')}</small></td>
                    <td><strong>{bc[3]['C']}</strong><br><small>{pct('C')}</small></td>
                    <td><strong>{bc[3]['D+']}</strong><br><small>{pct('D+')}</small></td>
                    <td><strong>{bc[3]['D']}</strong><br><small>{pct('D')}</small></td>
                    <td><strong style="color:#e74c3c;">{bc[3]['F']}</strong><br><small>{pct('F')}</small></td>
                  </tr></tbody>
                </table>
              </div>
            </div>"""
        stats = ""
        chart_html = ""
        if bao_cao:
            tl = (total_sv-total_f)/total_sv*100 if total_sv else 0
            stats = f"""<div class="row" style="margin-bottom:15px;">
              <div class="col-md-3"><div class="card-stat" style="background:#3498db;">
                <h2>{total_sv}</h2><p>Tổng sinh viên</p></div></div>
              <div class="col-md-3"><div class="card-stat" style="background:#27ae60;">
                <h2>{total_kha}</h2><p>Khá/Giỏi/Xuất sắc</p></div></div>
              <div class="col-md-3"><div class="card-stat" style="background:#e74c3c;">
                <h2>{total_f}</h2><p>Không đạt (F)</p></div></div>
              <div class="col-md-3"><div class="card-stat" style="background:#f39c12;">
                <h2>{tl:.1f}%</h2><p>Tỉ lệ đỗ</p></div></div>
            </div>"""
            
            # Tạo biểu đồ phân bố điểm tổng hợp
            grade_totals = {"A":0,"B+":0,"B":0,"C+":0,"C":0,"D+":0,"D":0,"F":0}
            for bc in bao_cao:
                for g in grade_totals:
                    grade_totals[g] += bc[3][g]
            max_count = max(grade_totals.values()) if grade_totals.values() else 1
            
            bars = ""
            colors = {"A":"#27ae60","B+":"#2980b9","B":"#3498db","C+":"#f39c12","C":"#e67e22","D+":"#95a5a6","D":"#7f8c8d","F":"#e74c3c"}
            for grade in ["A","B+","B","C+","C","D+","D","F"]:
                count = grade_totals[grade]
                pct_val = (count/total_sv*100) if total_sv else 0
                width = (count/max_count*100) if max_count else 0
                bars += f"""
                <div style="margin-bottom:8px;">
                  <div style="display:flex;align-items:center;">
                    <div style="width:40px;font-weight:bold;text-align:right;margin-right:10px;">{grade}</div>
                    <div style="flex:1;background:#ecf0f1;border-radius:4px;height:28px;position:relative;">
                      <div style="background:{colors[grade]};width:{width:.1f}%;height:100%;border-radius:4px;transition:width 0.3s;"></div>
                      <div style="position:absolute;top:50%;right:10px;transform:translateY(-50%);font-weight:bold;color:#2c3e50;">
                        {count} ({pct_val:.1f}%)
                      </div>
                    </div>
                  </div>
                </div>"""
            
            chart_html = f"""
            <div class="panel panel-info" style="margin-top:20px;">
              <div class="panel-heading"><h4 style="margin:0;">📊 Biểu đồ phân bố điểm tổng hợp năm học</h4></div>
              <div class="panel-body" style="padding:20px;">
                {bars}
                <p class="text-muted text-center" style="margin-top:15px;">
                  <small>Biểu đồ thể hiện tổng số sinh viên đạt từng loại điểm chữ trong toàn bộ các môn thi</small>
                </p>
              </div>
            </div>"""
        empty = "" if bao_cao else ('<div class="alert alert-warning">⚠️ Chưa có dữ liệu điểm cho năm học này.</div>' if f_nam else "")

        export_btn = f'<a href="/baocao/export?namHoc={f_nam}&sid={self.sid}" class="btn btn-success" style="margin-left:10px;">📥 Export CSV</a>' if (f_nam and bao_cao) else ""
        
        body = f"""
        <div class="page-header"><h2>📊 Báo cáo tổng kết năm học</h2></div>
        <form method="get" class="form-inline" style="margin-bottom:15px;">
          <input type="hidden" name="sid" value="{self.sid}">
          <label>Năm học: </label>
          <select name="namHoc" class="form-control" style="margin:0 10px;width:150px;">{nam_opts}</select>
          <button class="btn btn-primary">📊 Xem báo cáo</button>
          {export_btn}
        </form>
        {"<h3>Năm học: <strong>"+f_nam+"</strong></h3>" if f_nam else ""}
        {stats}{chart_html}{empty}{bao_html}"""
        return layout("Báo cáo năm", body, session, "baocao")

    def page_thamso(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        rows = cur.execute("SELECT TenThamSo,GiaTri,GhiChu FROM THAM_SO").fetchall()
        conn.close()
        rows_html = ""
        for r in rows:
            val = f"{r[1]} phút" if "ThoiLuong" in r[0] else str(r[1])
            rows_html += f"""<tr>
              <td><strong>{r[0]}</strong></td>
              <td><span class="badge">{val}</span></td>
              <td class="text-muted">{r[2]}</td>
              <td><a href="/thamso/edit/{r[0]}?sid={self.sid}" class="btn btn-xs btn-warning">✏️ Sửa</a></td>
            </tr>"""
        body = f"""
        <div class="page-header"><h2>⚙️ Tham số hệ thống</h2></div>
        {flash}
        <div class="alert alert-info">ℹ️ Các tham số kiểm soát quy định nghiệp vụ của hệ thống.</div>
        <table class="table table-bordered table-striped">
          <thead><tr><th>Tên tham số</th><th>Giá trị</th><th>Ghi chú</th><th></th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>"""
        return layout("Tham số", body, session, "thamso")

    def page_thamso_edit(self, session, ten, flash=""):
        conn = get_db(); cur = conn.cursor()
        row = cur.execute("SELECT TenThamSo,GiaTri,GhiChu FROM THAM_SO WHERE TenThamSo=?", (ten,)).fetchone()
        conn.close()
        if not row: return self.send_html("Not found",404)
        body = f"""
        <div class="page-header"><h2>✏️ Sửa tham số: {row[0]}</h2></div>
        {flash}
        <form method="post" action="/thamso/edit/{row[0]}?sid={self.sid}" style="max-width:450px;">
          <input type="hidden" name="sid" value="{self.sid}">
          <div class="panel panel-default"><div class="panel-body">
            <div class="form-group"><label>Tên:</label><p class="form-control-static"><strong>{row[0]}</strong></p></div>
            <div class="form-group"><label>Ghi chú:</label><p class="text-muted">{row[2]}</p></div>
            <div class="form-group"><label>Giá trị mới <span class="text-danger">*</span></label>
              <input name="GiaTri" type="number" class="form-control" value="{row[1]}" required>
            </div>
            <button class="btn btn-primary">💾 Cập nhật</button>
            <a href="/thamso" class="btn btn-default">← Hủy</a>
          </div></div>
        </form>"""
        return layout("Sửa tham số", body, session, "thamso")


    # ── ROUTING ──────────────────────────────────────────────────────
    def do_GET(self):
        print(f"\n{'='*60}\n[RAW GET] {self.path}\n{'='*60}", flush=True)
        path = urllib.parse.urlparse(self.path).path.rstrip("/") or "/"
        self.sid = get_sid(self)
        session = get_session(self)
        
        # Debug logging
        print(f"[GET] {path} | sid={self.sid[:8] if self.sid else 'None'} | session={'OK' if session else 'NO'}", flush=True)

        def need_login():
            self.redirect("/login"); return None

        if path == "/login":
            return self.send_html(self.page_login())
        if path == "/logout":
            if self.sid: SESSIONS.pop(self.sid, None)
            self.sid = ""
            # Clear cookie and redirect to login
            self.send_response(302)
            self.set_cookie("sid", "", max_age=0)  # Delete cookie
            self.send_header("Location", "/login")
            self.end_headers()
            return

        if not session: 
            self.redirect("/login")
            return

        if path == "/" or path == "/home":
            return self.send_html(self.page_home(session))
        if path == "/cauhoi":
            return self.send_html(self.page_cauhoi(session))
        if path == "/cauhoi/create":
            return self.send_html(self.page_cauhoi_create(session))
        if path.startswith("/cauhoi/edit/"):
            mach = int(path.split("/")[-1])
            return self.send_html(self.page_cauhoi_edit(session, mach))
        if path.startswith("/cauhoi/delete/"):
            mach = int(path.split("/")[-1])
            conn = sqlite3.connect(DB_PATH)
            conn.execute("DELETE FROM CT_DETHI WHERE MaCH=?", (mach,))
            conn.execute("DELETE FROM CAU_HOI WHERE MaCH=?", (mach,))
            conn.commit(); conn.close()
            self.redirect("/cauhoi"); return
        if path == "/dethi":
            return self.send_html(self.page_dethi_list(session))
        if path == "/dethi/create":
            return self.send_html(self.page_dethi_create(session))
        if path == "/dethi/tracuu":
            return self.send_html(self.page_dethi_tracuu(session))
        if path.startswith("/dethi/") and path.count("/")==2:
            maDT = int(path.split("/")[-1])
            return self.send_html(self.page_dethi_detail(session, maDT))
        if path == "/ketqua":
            return self.send_html(self.page_ketqua(session))
        if path.startswith("/ketqua/nhap/"):
            maDT = int(path.split("/")[-1])
            return self.send_html(self.page_nhap_diem(session, maDT))
        if path.startswith("/ketqua/phieu/"):
            # In phiếu điểm cho sinh viên
            parts = path.split("/")
            maDT = int(parts[3])
            maSV = int(parts[4])
            
            conn = get_db(); cur = conn.cursor()
            dt = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.NgayThi
                                FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                                WHERE d.MaDT=?""", (maDT,)).fetchone()
            sv = cur.execute("""SELECT s.MaSV,s.HoTen,s.NgaySinh,l.TenLop
                                FROM SINH_VIEN s JOIN LOP_HOC l ON l.MaLop=s.MaLop
                                WHERE s.MaSV=?""", (maSV,)).fetchone()
            kq = cur.execute("""SELECT DiemSo,DiemChu,NgayCham FROM KET_QUA
                                WHERE MaSV=? AND MaDT=?""", (maSV, maDT)).fetchone()
            release_db(conn)
            
            if not (dt and sv and kq):
                return self.send_html("<h1>404</h1><p>Không tìm thấy dữ liệu</p>", 404)
            
            # HTML phiếu điểm để in
            html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Phiếu điểm - {sv[1]}</title>
<style>
body{{font-family:'Segoe UI',sans-serif;padding:40px;background:#fff;}}
.phieu{{max-width:800px;margin:0 auto;border:2px solid #333;padding:30px;}}
h1{{text-align:center;color:#2c3e50;border-bottom:3px solid #3498db;padding-bottom:10px;}}
.info{{margin:20px 0;}}
.info table{{width:100%;border-collapse:collapse;}}
.info td{{padding:8px;border:1px solid #ddd;}}
.info td:first-child{{background:#f0f2f5;font-weight:600;width:200px;}}
.diem{{text-align:center;margin:30px 0;}}
.diem-so{{font-size:48px;font-weight:700;color:#27ae60;}}
.diem-chu{{font-size:32px;color:#2980b9;}}
.footer{{margin-top:40px;text-align:right;}}
@media print{{body{{padding:0;}} .no-print{{display:none;}}}}
</style>
</head>
<body>
<div class="no-print" style="text-align:center;margin-bottom:20px;">
  <button onclick="window.print()" class="btn">🖨️ In phiếu</button>
  <button onclick="window.close()" class="btn">✖️ Đóng</button>
</div>
<div class="phieu">
  <h1>🎓 PHIẾU ĐIỂM</h1>
  <div class="info">
    <table>
      <tr><td>Họ và tên</td><td><strong>{sv[1]}</strong></td></tr>
      <tr><td>MSSV</td><td>{sv[0]}</td></tr>
      <tr><td>Ngày sinh</td><td>{sv[2]}</td></tr>
      <tr><td>Lớp</td><td>{sv[3]}</td></tr>
      <tr><td>Môn học</td><td><strong>{dt[1]}</strong></td></tr>
      <tr><td>Học kỳ / Năm học</td><td>HK{dt[2]} – {dt[3]}</td></tr>
      <tr><td>Ngày thi</td><td>{dt[4] or 'N/A'}</td></tr>
      <tr><td>Ngày chấm</td><td>{kq[2]}</td></tr>
    </table>
  </div>
  <div class="diem">
    <div class="diem-so">{kq[0]}</div>
    <div class="diem-chu">({kq[1]})</div>
  </div>
  <div class="footer">
    <p><em>Giảng viên chấm thi</em></p>
    <p style="margin-top:60px;">({session['HoTen']})</p>
  </div>
</div>
</body></html>"""
            self.send_html(html)
            return
        if path == "/baocao":
            return self.send_html(self.page_baocao(session))
        if path.startswith("/baocao/export"):
            # Export báo cáo năm ra CSV
            qs = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(qs)
            f_nam = params.get("namHoc",[""])[0]
            if not f_nam:
                self.send_html("<h1>400 Bad Request</h1><p>Thiếu tham số namHoc</p>", 400)
                return
            
            conn = get_db(); cur = conn.cursor()
            deThis = cur.execute(
                "SELECT d.MaDT,m.TenMon,d.HocKy FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon WHERE d.MaGV=? AND d.NamHoc=?",
                (session["MaGV"], f_nam)).fetchall()
            
            csv_rows = [["Môn học", "Học kỳ", "Tổng SV", "A", "B+", "B", "C+", "C", "D+", "D", "F", "Điểm TB", "Tỉ lệ đỗ (%)"]]
            
            for dt in deThis:
                kqs = cur.execute("SELECT DiemSo,DiemChu FROM KET_QUA WHERE MaDT=?", (dt[0],)).fetchall()
                if not kqs: continue
                total = len(kqs)
                counts = {c: sum(1 for k in kqs if k[1]==c) for c in ["A","B+","B","C+","C","D+","D","F"]}
                avg = sum(k[0] for k in kqs)/total
                tl_dao = (total-counts["F"])/total*100 if total else 0
                csv_rows.append([
                    dt[1], dt[2], total,
                    counts["A"], counts["B+"], counts["B"], counts["C+"], counts["C"],
                    counts["D+"], counts["D"], counts["F"],
                    f"{avg:.2f}", f"{tl_dao:.1f}"
                ])
            release_db(conn)
            
            # Build CSV
            csv_content = "\n".join([",".join([f'"{str(c)}"' for c in row]) for row in csv_rows])
            csv_bytes = csv_content.encode("utf-8-sig")  # BOM cho Excel
            
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", f'attachment; filename="BaoCao_{f_nam}.csv"')
            self.send_header("Content-Length", str(len(csv_bytes)))
            self.end_headers()
            self.wfile.write(csv_bytes)
            return
        if path == "/thamso":
            return self.send_html(self.page_thamso(session))
        if path.startswith("/thamso/edit/"):
            ten = path.split("/thamso/edit/")[1]
            return self.send_html(self.page_thamso_edit(session, ten))
        if path.startswith("/api/cauhoi"):
            qs = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(qs)
            maMon = params.get("maMon",[""])[0]
            maDK  = params.get("maDoKho",[""])[0]
            conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
            sql = "SELECT c.MaCH,c.NoiDung,dk.TenDoKho,dk.MaDoKho FROM CAU_HOI c JOIN DO_KHO dk ON dk.MaDoKho=c.MaDoKho WHERE c.MaMon=?"
            args = [maMon]
            if maDK: sql += " AND c.MaDoKho=?"; args.append(maDK)
            rows = cur.execute(sql, args).fetchall()
            conn.close()
            data = [{"MaCH":r[0],"NoiDung":r[1],"TenDoKho":r[2],"MaDoKho":r[3]} for r in rows]
            body = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type","application/json; charset=utf-8")
            self.send_header("Content-Length",str(len(body)))
            self.end_headers(); self.wfile.write(body); return
        
        if path == "/test":
            # Test page để debug links
            html = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Test</title></head>
<body><h1>Test Links</h1>
<p><a href="/cauhoi?sid=test123">Test Link 1: /cauhoi?sid=test123</a></p>
<p><a href="/dethi/create?sid=test123">Test Link 2: /dethi/create?sid=test123</a></p>
<p><button onclick="location.href='/ketqua?sid=test123'">Test Button: JS redirect</button></p>
<p>Current SID: <span id="sid"></span></p>
<script>
var qs = new URLSearchParams(window.location.search);
document.getElementById('sid').textContent = qs.get('sid') || 'NONE';
</script></body></html>"""
            return self.send_html(html)

        self.send_html("<h1>404 Not Found</h1>", 404)

    def do_POST(self):
        print(f"\n{'='*60}\n[RAW POST] {self.path}\n{'='*60}", flush=True)
        path = urllib.parse.urlparse(self.path).path.rstrip("/")
        self.sid = get_sid(self)
        session = get_session(self)
        form = self.parse_body()
        # Also check sid from POST body if not in URL
        if not self.sid:
            self.sid = self.pv(form, "sid")
            if self.sid and self.sid in SESSIONS:
                session = SESSIONS[self.sid]
        
        # Debug logging
        print(f"[POST] {path} | sid={self.sid[:8] if self.sid else 'None'} | session={'OK' if session else 'NO'}", flush=True)

        if path == "/login":
            username = self.pv(form, "username")
            password = sha256(self.pv(form, "password"))
            conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
            row = cur.execute("SELECT MaGV,HoTen FROM GIANG_VIEN WHERE TenDangNhap=? AND MatKhau=?",
                              (username, password)).fetchone()
            conn.close()
            if not row:
                return self.send_html(self.page_login("❌ Tên đăng nhập hoặc mật khẩu không đúng!"))
            import secrets
            sid = secrets.token_hex(16)
            SESSIONS[sid] = {"MaGV": row[0], "HoTen": row[1]}
            self.sid = sid
            print(f"[LOGIN SUCCESS] Created session {sid[:8]}... for user {row[1]}", flush=True)
            # Set cookie via JavaScript and redirect
            html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<script>
document.cookie = "sid={sid}; path=/; max-age=86400";
console.log("Cookie set:", document.cookie);
setTimeout(function(){{ window.location.href = "/"; }}, 100);
</script>
</head><body>
<p>Đăng nhập thành công! Đang chuyển hướng...</p>
</body></html>"""
            print(f"[LOGIN SUCCESS] Sending HTML with JS cookie set for sid={sid[:8]}...", flush=True)
            return self.send_html(html)

        if not session:
            self.redirect("/login"); return

        if path == "/cauhoi/create":
            maMon = self.pv(form,"MaMon")
            maDK  = self.pv(form,"MaDoKho")
            noiDung = self.pv(form,"NoiDung").strip()
            if not (maMon and maDK and noiDung):
                return self.send_html(self.page_cauhoi_create(session,
                    alert("Vui lòng điền đầy đủ thông tin!","danger"),
                    {"mon":maMon,"dk":maDK,"nd":noiDung}))
            conn = sqlite3.connect(DB_PATH)
            conn.execute("INSERT INTO CAU_HOI(NoiDung,MaMon,MaDoKho) VALUES(?,?,?)",
                         (noiDung, maMon, maDK))
            conn.commit(); conn.close()
            self.redirect("/cauhoi"); return

        if path.startswith("/cauhoi/edit/"):
            mach = int(path.split("/")[-1])
            conn = sqlite3.connect(DB_PATH)
            conn.execute("UPDATE CAU_HOI SET NoiDung=?,MaMon=?,MaDoKho=? WHERE MaCH=?",
                         (self.pv(form,"NoiDung"), self.pv(form,"MaMon"), self.pv(form,"MaDoKho"), mach))
            conn.commit(); conn.close()
            self.redirect("/cauhoi"); return

        if path == "/dethi/create":
            maMon = self.pv(form,"MaMon"); hocKy = self.pv(form,"HocKy")
            namHoc = self.pv(form,"NamHoc"); thoiLuong = self.pv(form,"ThoiLuong")
            ngayThi = self.pv(form,"NgayThi") or None
            cauHois = form.get("CauHoi",[])
            # Validate
            tl = int(thoiLuong) if thoiLuong.isdigit() else 0
            conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
            tl_min = cur.execute("SELECT GiaTri FROM THAM_SO WHERE TenThamSo='ThoiLuongToiThieu'").fetchone()[0]
            tl_max = cur.execute("SELECT GiaTri FROM THAM_SO WHERE TenThamSo='ThoiLuongToiDa'").fetchone()[0]
            so_max = cur.execute("SELECT GiaTri FROM THAM_SO WHERE TenThamSo='SoCauToiDa'").fetchone()[0]
            if not (tl_min <= tl <= tl_max):
                conn.close()
                return self.send_html(self.page_dethi_create(session,
                    alert(f"Thời lượng phải từ {tl_min} đến {tl_max} phút!","danger")))
            if len(cauHois) == 0:
                conn.close()
                return self.send_html(self.page_dethi_create(session,
                    alert("Vui lòng chọn ít nhất 1 câu hỏi!","danger")))
            if len(cauHois) > so_max:
                conn.close()
                return self.send_html(self.page_dethi_create(session,
                    alert(f"Mỗi đề thi tối đa {so_max} câu hỏi!","danger")))
            cur.execute("INSERT INTO DE_THI(MaMon,HocKy,NamHoc,ThoiLuong,NgayThi,MaGV) VALUES(?,?,?,?,?,?)",
                        (maMon, hocKy, namHoc, thoiLuong, ngayThi, session["MaGV"]))
            maDT = cur.lastrowid
            for ch in cauHois:
                cur.execute("INSERT OR IGNORE INTO CT_DETHI VALUES(?,?)", (maDT, ch))
            conn.commit(); conn.close()
            self.redirect("/dethi"); return

        if path.startswith("/ketqua/luu/"):
            maDT = int(path.split("/")[-1])
            maSVs = form.get("maSV",[])
            diems = form.get("diemSo",[])
            conn = sqlite3.connect(DB_PATH)
            for i, maSV in enumerate(maSVs):
                if i >= len(diems) or not diems[i].strip(): continue
                try: d = float(diems[i])
                except: continue
                if not 0 <= d <= 10: continue
                dc = get_diem_chu(d)
                existing = conn.execute("SELECT 1 FROM KET_QUA WHERE MaSV=? AND MaDT=?",
                                        (maSV, maDT)).fetchone()
                if existing:
                    conn.execute("UPDATE KET_QUA SET DiemSo=?,DiemChu=?,NgayCham=? WHERE MaSV=? AND MaDT=?",
                                 (d, dc, str(date.today()), maSV, maDT))
                else:
                    conn.execute("INSERT INTO KET_QUA VALUES(?,?,?,?,?)",
                                 (maSV, maDT, d, dc, str(date.today())))
            conn.commit(); conn.close()
            self.redirect(f"/ketqua/nhap/{maDT}"); return

        if path.startswith("/thamso/edit/"):
            ten = path.split("/thamso/edit/")[1]
            gia_tri = self.pv(form,"GiaTri")
            conn = sqlite3.connect(DB_PATH)
            conn.execute("UPDATE THAM_SO SET GiaTri=? WHERE TenThamSo=?", (gia_tri, ten))
            conn.commit(); conn.close()
            self.redirect("/thamso"); return

        self.send_html("Not found", 404)


if __name__ == "__main__":
    init_db()
    port = 8080
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"""
╔══════════════════════════════════════════════════════════╗
║   🎓 Quản Lý Ra Đề & Chấm Thi – Nhóm 15 SE104.Q23      ║
╠══════════════════════════════════════════════════════════╣
║   ✅ Server đang chạy tại: http://localhost:{port}          ║
║   🔑 Đăng nhập: gv01 / 123456                           ║
║   🛑 Nhấn Ctrl+C để dừng                                ║
╚══════════════════════════════════════════════════════════╝
""")
    server.serve_forever()
=======
﻿#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo: Hệ thống Quản lý Ra đề và Chấm thi
Nhóm 15 – SE104.Q23
Chạy: python demo_app.py
Truy cập: http://localhost:8080
"""

import hashlib, json, sqlite3, os, urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import date

DB_PATH = os.path.join(os.path.dirname(__file__), "demo.db")

# ── Bootstrap 3 CSS CDN (sẽ dùng inline nếu offline) ──────────────────────────
BOOTSTRAP_CDN = "https://cdn.jsdelivr.net/npm/bootstrap@3.4.1/dist/css/bootstrap.min.css"

# ── Connection Pool (tăng tốc độ truy vấn) ──────────────────────────────────
_db_pool = []
def get_db():
    """Lấy connection từ pool hoặc tạo mới"""
    if _db_pool:
        return _db_pool.pop()
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=10.0)
    conn.execute("PRAGMA journal_mode=WAL")  # Tăng tốc đọc
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA busy_timeout=5000")  # Wait 5s if locked
    return conn

def release_db(conn):
    """Trả connection về pool"""
    if len(_db_pool) < 5:  # Giới hạn pool size
        _db_pool.append(conn)
    else:
        conn.close()

def sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()

# ══════════════════════════════════════════════════════════════════════
# DATABASE SETUP
# ══════════════════════════════════════════════════════════════════════
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS GIANG_VIEN(
        MaGV INTEGER PRIMARY KEY AUTOINCREMENT,
        HoTen TEXT, TenDangNhap TEXT UNIQUE, MatKhau TEXT, Email TEXT
    );
    CREATE TABLE IF NOT EXISTS MON_HOC(
        MaMon INTEGER PRIMARY KEY AUTOINCREMENT,
        TenMon TEXT, MaGV INTEGER
    );
    CREATE TABLE IF NOT EXISTS DO_KHO(
        MaDoKho INTEGER PRIMARY KEY AUTOINCREMENT,
        TenDoKho TEXT
    );
    CREATE TABLE IF NOT EXISTS CAU_HOI(
        MaCH INTEGER PRIMARY KEY AUTOINCREMENT,
        NoiDung TEXT, MaMon INTEGER, MaDoKho INTEGER
    );
    CREATE TABLE IF NOT EXISTS DE_THI(
        MaDT INTEGER PRIMARY KEY AUTOINCREMENT,
        MaMon INTEGER, HocKy INTEGER, NamHoc TEXT,
        ThoiLuong INTEGER, NgayThi TEXT, MaGV INTEGER
    );
    CREATE TABLE IF NOT EXISTS CT_DETHI(
        MaDT INTEGER, MaCH INTEGER,
        PRIMARY KEY(MaDT, MaCH)
    );
    CREATE TABLE IF NOT EXISTS LOP_HOC(
        MaLop INTEGER PRIMARY KEY AUTOINCREMENT,
        TenLop TEXT, NamHoc TEXT, MaGV INTEGER
    );
    CREATE TABLE IF NOT EXISTS SINH_VIEN(
        MaSV INTEGER PRIMARY KEY AUTOINCREMENT,
        HoTen TEXT, NgaySinh TEXT, MaLop INTEGER
    );
    CREATE TABLE IF NOT EXISTS KET_QUA(
        MaSV INTEGER, MaDT INTEGER,
        DiemSo REAL, DiemChu TEXT, NgayCham TEXT,
        PRIMARY KEY(MaSV, MaDT)
    );
    CREATE TABLE IF NOT EXISTS BANG_DIEM_CHU(
        DiemChu TEXT PRIMARY KEY,
        DiemSoTu REAL, DiemSoDen REAL, GhiChu TEXT
    );
    CREATE TABLE IF NOT EXISTS THAM_SO(
        TenThamSo TEXT PRIMARY KEY,
        GiaTri INTEGER, GhiChu TEXT
    );
    """)

    # Seed nếu chưa có dữ liệu
    if cur.execute("SELECT COUNT(*) FROM DO_KHO").fetchone()[0] == 0:
        cur.executemany("INSERT INTO DO_KHO(TenDoKho) VALUES(?)",
            [("Dễ",),("Trung Bình",),("Phức Tạp",),("Khó",)])
        cur.executemany("INSERT INTO BANG_DIEM_CHU VALUES(?,?,?,?)",[
            ("A",8.5,10.0,"Xuất sắc"),("B+",8.0,8.49,"Giỏi"),
            ("B",7.0,7.99,"Khá"),("C+",6.5,6.99,"Trung bình khá"),
            ("C",5.5,6.49,"Trung bình"),("D+",5.0,5.49,"Trung bình yếu"),
            ("D",4.0,4.99,"Yếu"),("F",0.0,3.99,"Kém"),
        ])
        cur.executemany("INSERT INTO THAM_SO VALUES(?,?,?)",[
            ("SoCauToiDa",5,"Số câu hỏi tối đa mỗi đề thi"),
            ("ThoiLuongToiThieu",30,"Thời lượng tối thiểu (phút)"),
            ("ThoiLuongToiDa",180,"Thời lượng tối đa (phút)"),
            ("SoLopToiDa",50,"Số lớp tối đa mỗi năm"),
            ("SoMonToiDa",4,"Số môn học tối đa"),
        ])
        pwd = sha256("123456")
        cur.executemany("INSERT INTO GIANG_VIEN(HoTen,TenDangNhap,MatKhau,Email) VALUES(?,?,?,?)",[
            ("Nguyễn Văn An","gv01",pwd,"gv01@uit.edu.vn"),
            ("Trần Thị Bình","gv02",pwd,"gv02@uit.edu.vn"),
        ])
        cur.executemany("INSERT INTO MON_HOC(TenMon,MaGV) VALUES(?,?)",[
            ("Lập trình hướng đối tượng",1),
            ("Cơ sở dữ liệu",1),
            ("Mạng máy tính",2),
            ("Công nghệ phần mềm",1),
        ])
        cur.executemany("INSERT INTO CAU_HOI(NoiDung,MaMon,MaDoKho) VALUES(?,?,?)",[
            ("Kế thừa trong OOP là gì?",1,1),
            ("Sự khác biệt giữa abstract class và interface?",1,2),
            ("Polymorphism trong C# hoạt động như thế nào?",1,3),
            ("Giải thích nguyên lý SOLID.",1,4),
            ("Override và Overload khác nhau như thế nào?",1,2),
            ("Khóa chính (Primary Key) là gì?",2,1),
            ("Sự khác biệt giữa JOIN và UNION trong SQL?",2,2),
            ("Chuẩn hóa CSDL 3NF là gì?",2,3),
            ("Giải thích Transaction và ACID properties.",2,4),
            ("Index trong SQL có tác dụng gì?",2,2),
            ("Giao thức TCP/IP là gì?",3,1),
            ("HTTP và HTTPS khác nhau như thế nào?",3,2),
            ("Giải thích mô hình OSI 7 lớp.",3,3),
            ("DNS hoạt động như thế nào?",3,2),
            ("SDLC là gì?",4,1),
            ("Agile và Waterfall khác nhau như thế nào?",4,2),
            ("Kiểm thử hộp đen và hộp trắng là gì?",4,2),
            ("Giải thích mô hình kiến trúc 3 lớp.",4,3),
        ])
        cur.executemany("INSERT INTO LOP_HOC(TenLop,NamHoc,MaGV) VALUES(?,?,?)",[
            ("SE104.P11","2024-2025",1),("SE104.P12","2024-2025",1),("NT101.P11","2024-2025",2),
            ("SE104.P11","2023-2024",1),("SE104.P12","2023-2024",1),("NT101.P11","2023-2024",2),
            ("SE104.P11","2022-2023",1),("SE104.P12","2022-2023",1),
        ])
        cur.executemany("INSERT INTO SINH_VIEN(HoTen,NgaySinh,MaLop) VALUES(?,?,?)",[
            # Lớp SE104.P11 (2024-2025) - MaLop=1
            ("Nguyễn Văn An","2003-01-15",1),("Trần Thị Bảo","2003-05-20",1),
            ("Lê Minh Châu","2002-12-10",1),("Phạm Thị Dung","2003-03-25",1),
            ("Hoàng Văn Đạt","2002-08-14",1),("Đỗ Thị Hương","2003-07-07",1),
            ("Nguyễn Thị Giang","2002-09-18",1),("Võ Văn Hải","2002-11-22",1),
            ("Bùi Thị Lan","2002-06-30",1),("Đặng Văn Khoa","2002-04-12",1),
            # Lớp SE104.P12 (2024-2025) - MaLop=2
            ("Lý Thị Mai","2001-08-25",2),("Trịnh Văn Nam","2001-10-15",2),
            ("Mai Thị Nga","2001-05-08",2),("Phan Văn Phúc","2002-02-18",2),
            ("Vũ Thị Quỳnh","2002-03-22",2),("Đinh Văn Tâm","2003-09-10",2),
            ("Hồ Thị Thanh","2003-08-05",2),("Lương Văn Tùng","2002-07-14",2),
            # Lớp NT101.P11 (2024-2025) - MaLop=3
            ("Cao Thị Uyên","2002-12-25",3),("Đào Văn Vinh","2003-02-08",3),
            ("Dương Thị Xuân","2002-10-30",3),("Tô Văn Yên","2003-04-17",3),
            # Lớp SE104.P11 (2023-2024) - MaLop=4
            ("Ngô Thị Ánh","2001-11-09",4),("Từ Văn Bình","2001-12-12",4),
            ("Ung Thị Chi","2002-01-20",4),("Xa Văn Duy","2001-09-05",4),
            ("Yên Thị Hoa","2002-05-15",4),("Trương Văn Kiên","2001-07-28",4),
            # Lớp SE104.P12 (2023-2024) - MaLop=5
            ("Lâm Thị Linh","2002-03-11",5),("Kim Văn Long","2001-08-19",5),
            ("Huỳnh Thị Mỹ","2002-06-22",5),("Tạ Văn Nhật","2001-04-30",5),
            # Lớp NT101.P11 (2023-2024) - MaLop=6
            ("Quách Thị Oanh","2002-02-14",6),("Văn Văn Phong","2001-10-03",6),
            # Lớp SE104.P11 (2022-2023) - MaLop=7
            ("Diệp Thị Quyên","2000-12-05",7),("Lưu Văn Sơn","2000-11-18",7),
            ("Nghiêm Thị Trang","2001-01-22",7),("Bành Văn Thắng","2000-09-09",7),
            # Lớp SE104.P12 (2022-2023) - MaLop=8
            ("Thái Thị Vân","2001-03-07",8),("Phùng Văn Tuấn","2000-08-16",8),
        ])
        
        # Đề thi năm 2024-2025
        cur.execute("INSERT INTO DE_THI(MaMon,HocKy,NamHoc,ThoiLuong,NgayThi,MaGV) VALUES(1,1,'2024-2025',90,'2025-01-10',1)")
        maDT = cur.lastrowid
        for maCH in [1,2,3,4,5]:
            cur.execute("INSERT INTO CT_DETHI VALUES(?,?)", (maDT, maCH))
        cur.executemany("INSERT INTO KET_QUA VALUES(?,?,?,?,?)",[
            (1,maDT,8.5,"A","2025-01-20"),(2,maDT,7.0,"B","2025-01-20"),
            (3,maDT,5.5,"C","2025-01-20"),(4,maDT,6.5,"C+","2025-01-20"),
            (5,maDT,9.0,"A","2025-01-20"),(6,maDT,7.5,"B","2025-01-20"),
            (7,maDT,8.0,"B+","2025-01-20"),(8,maDT,4.5,"D+","2025-01-20"),
            (9,maDT,5.0,"D+","2025-01-20"),(10,maDT,3.0,"F","2025-01-20"),
        ])
        
        # Đề thi năm 2023-2024 - Môn OOP
        cur.execute("INSERT INTO DE_THI(MaMon,HocKy,NamHoc,ThoiLuong,NgayThi,MaGV) VALUES(1,1,'2023-2024',90,'2024-01-15',1)")
        maDT2 = cur.lastrowid
        for maCH in [1,2,3,4,5]:
            cur.execute("INSERT INTO CT_DETHI VALUES(?,?)", (maDT2, maCH))
        cur.executemany("INSERT INTO KET_QUA VALUES(?,?,?,?,?)",[
            (13,maDT2,9.0,"A","2024-01-25"),(14,maDT2,8.2,"B+","2024-01-25"),
            (15,maDT2,7.5,"B","2024-01-25"),(16,maDT2,6.0,"C","2024-01-25"),
            (17,maDT2,8.5,"A","2024-01-25"),(18,maDT2,7.0,"B","2024-01-25"),
        ])
        
        # Đề thi năm 2023-2024 - Môn CSDL
        cur.execute("INSERT INTO DE_THI(MaMon,HocKy,NamHoc,ThoiLuong,NgayThi,MaGV) VALUES(2,2,'2023-2024',90,'2024-05-20',1)")
        maDT3 = cur.lastrowid
        for maCH in [6,7,8,9,10]:
            cur.execute("INSERT INTO CT_DETHI VALUES(?,?)", (maDT3, maCH))
        cur.executemany("INSERT INTO KET_QUA VALUES(?,?,?,?,?)",[
            (13,maDT3,8.8,"A","2024-05-30"),(14,maDT3,7.8,"B","2024-05-30"),
            (15,maDT3,6.5,"C+","2024-05-30"),(16,maDT3,5.0,"D+","2024-05-30"),
            (17,maDT3,9.5,"A","2024-05-30"),(18,maDT3,8.0,"B+","2024-05-30"),
        ])
        
        # Đề thi năm 2022-2023 - Môn OOP
        cur.execute("INSERT INTO DE_THI(MaMon,HocKy,NamHoc,ThoiLuong,NgayThi,MaGV) VALUES(1,1,'2022-2023',90,'2023-01-12',1)")
        maDT4 = cur.lastrowid
        for maCH in [1,2,3,4,5]:
            cur.execute("INSERT INTO CT_DETHI VALUES(?,?)", (maDT4, maCH))
        cur.executemany("INSERT INTO KET_QUA VALUES(?,?,?,?,?)",[
            (27,maDT4,7.5,"B","2023-01-22"),(28,maDT4,6.8,"C+","2023-01-22"),
            (29,maDT4,4.5,"D","2023-01-22"),(30,maDT4,8.0,"B+","2023-01-22"),
        ])
        
        # Đề thi năm 2022-2023 - Môn CSDL
        cur.execute("INSERT INTO DE_THI(MaMon,HocKy,NamHoc,ThoiLuong,NgayThi,MaGV) VALUES(2,2,'2022-2023',90,'2023-05-18',1)")
        maDT5 = cur.lastrowid
        for maCH in [6,7,8,9,10]:
            cur.execute("INSERT INTO CT_DETHI VALUES(?,?)", (maDT5, maCH))
        cur.executemany("INSERT INTO KET_QUA VALUES(?,?,?,?,?)",[
            (11,maDT5,9.2,"A","2023-05-28"),
            (12,maDT5,8.5,"A","2023-05-28"),
            (13,maDT5,3.5,"F","2023-05-28"),
        ])
        
        # Tạo indexes để tăng tốc query
        cur.execute("CREATE INDEX IF NOT EXISTS idx_cauhoi_mon ON CAU_HOI(MaMon)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_cauhoi_dokho ON CAU_HOI(MaDoKho)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_dethi_magv ON DE_THI(MaGV)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_ketqua_madt ON KET_QUA(MaDT)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_monhoc_magv ON MON_HOC(MaGV)")
        
    conn.commit()
    conn.close()

# ══════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════
def get_diem_chu(diem):
    if diem >= 8.5: return "A"
    if diem >= 8.0: return "B+"
    if diem >= 7.0: return "B"
    if diem >= 6.5: return "C+"
    if diem >= 5.5: return "C"
    if diem >= 5.0: return "D+"
    if diem >= 4.0: return "D"
    return "F"

def label_class(diem_chu):
    m = {"A":"success","B+":"info","B":"info","C+":"warning","C":"warning","D+":"default","D":"default","F":"danger"}
    return m.get(diem_chu, "default")

SESSIONS = {}  # session_id -> {MaGV, HoTen}

def get_sid(handler):
    """Extract sid from cookie first, then URL query string"""
    # Check cookie first
    cookie = handler.headers.get("Cookie","")
    print(f"[get_sid] Cookie header: {cookie[:100] if cookie else 'EMPTY'}", flush=True)
    for part in cookie.split(";"):
        k,_,v = part.strip().partition("=")
        if k.strip() == "sid":
            print(f"[get_sid] Found sid in cookie: {v.strip()[:8]}...", flush=True)
            return v.strip()
    # Fallback to URL query string
    qs = urllib.parse.urlparse(handler.path).query
    sid_from_qs = urllib.parse.parse_qs(qs).get("sid", [""])[0]
    if sid_from_qs:
        print(f"[get_sid] Found sid in query string: {sid_from_qs[:8]}...", flush=True)
    else:
        print(f"[get_sid] NO SID FOUND!", flush=True)
    return sid_from_qs

def get_session(handler):
    # Primary: check cookie (standard web practice)
    cookie = handler.headers.get("Cookie","")
    for part in cookie.split(";"):
        k,_,v = part.strip().partition("=")
        if k.strip() == "sid":
            sid = v.strip()
            if sid and sid in SESSIONS:
                return SESSIONS[sid]
    # Fallback: check URL query string (for compatibility)
    sid = get_sid(handler)
    if sid and sid in SESSIONS:
        return SESSIONS[sid]
    return None

# ══════════════════════════════════════════════════════════════════════
# HTML TEMPLATES
# ══════════════════════════════════════════════════════════════════════
STYLE = """
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ── Modern UI inspired by Facebook/Instagram ── */
*,*:before,*:after{box-sizing:border-box;margin:0;padding:0;}
body{
  font-family:'Inter','Segoe UI',sans-serif;
  font-size:15px;
  line-height:1.6;
  color:#1c1e21;
  background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);
  background-attachment:fixed;
}
a{color:#1877f2;text-decoration:none;transition:all 0.2s;}
a:hover{color:#0a58ca;}
h1,h2,h3,h4{font-weight:700;color:#1c1e21;}
.container-fluid{padding:0 20px;max-width:1400px;margin:0 auto;}
.row{display:flex;flex-wrap:wrap;margin:0 -10px;}
[class*="col-"]{padding:0 10px;}
.col-md-3{flex:0 0 25%;max-width:25%;}
.col-md-4{flex:0 0 33.33%;max-width:33.33%;}
.col-md-6{flex:0 0 50%;max-width:50%;}
.col-md-8{flex:0 0 66.66%;max-width:66.66%;}
.col-md-12{flex:0 0 100%;max-width:100%;}

/* ── Navbar (Instagram/Facebook style) ── */
.navbar{
  position:fixed;
  top:0;
  width:100%;
  z-index:1000;
  background:#fff;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
  height:60px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding:0 24px;
}
.navbar-brand{
  font-size:22px;
  font-weight:700;
  background:linear-gradient(135deg,#667eea,#764ba2);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  background-clip:text;
}
.navbar-nav{
  display:flex;
  list-style:none;
  gap:8px;
}
.navbar-nav li a{
  padding:8px 16px;
  border-radius:8px;
  color:#65676b;
  font-weight:500;
  transition:all 0.2s;
  display:flex;
  align-items:center;
  gap:6px;
}
.navbar-nav li a:hover{
  background:#f0f2f5;
  color:#1c1e21;
}
.dropdown{position:relative;}
.dropdown-menu{
  display:none;
  position:absolute;
  right:0;
  top:calc(100% + 8px);
  background:#fff;
  border-radius:12px;
  box-shadow:0 8px 24px rgba(0,0,0,.15);
  min-width:200px;
  padding:8px;
  animation:fadeIn 0.2s;
}
@keyframes fadeIn{from{opacity:0;transform:translateY(-10px)}to{opacity:1;transform:translateY(0)}}
.dropdown-menu li a{
  display:flex;
  align-items:center;
  gap:12px;
  padding:10px 12px;
  border-radius:8px;
  color:#1c1e21;
  font-weight:500;
}
.dropdown-menu li a:hover{background:#f0f2f5;}
.dropdown:hover .dropdown-menu{display:block;}

/* ── Modern Buttons ── */
.btn{
  display:inline-block;
  padding:10px 20px;
  font-size:15px;
  font-weight:600;
  text-align:center;
  cursor:pointer;
  border:none;
  border-radius:8px;
  transition:all 0.2s;
  box-shadow:0 2px 4px rgba(0,0,0,.1);
}
.btn:hover{transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.15);}
.btn:active{transform:translateY(0);box-shadow:0 2px 4px rgba(0,0,0,.1);}
.btn-primary{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;}
.btn-success{background:linear-gradient(135deg,#56ab2f,#a8e063);color:#fff;}
.btn-info{background:linear-gradient(135deg,#00c6ff,#0072ff);color:#fff;}
.btn-warning{background:linear-gradient(135deg,#f093fb,#f5576c);color:#fff;}
.btn-danger{background:linear-gradient(135deg,#eb3349,#f45c43);color:#fff;}
.btn-default{background:#fff;color:#1c1e21;border:1px solid #ccd0d5;}
.btn-lg{padding:14px 28px;font-size:16px;}
.btn-sm{padding:6px 12px;font-size:13px;}
.btn-xs{padding:4px 8px;font-size:12px;font-weight:500;}
.btn-block{display:block;width:100%;}
.pull-right{float:right;}

/* ── Modern Forms ── */
.form-control{
  width:100%;
  padding:12px 16px;
  font-size:15px;
  border:1px solid #ccd0d5;
  border-radius:8px;
  background:#fff;
  transition:all 0.2s;
  font-family:inherit;
}
.form-control:focus{
  outline:none;
  border-color:#667eea;
  box-shadow:0 0 0 4px rgba(102,126,234,.1);
}
.form-group{margin-bottom:16px;}
label{display:block;margin-bottom:6px;font-weight:600;color:#1c1e21;font-size:14px;}
.form-inline{display:flex;gap:12px;align-items:center;flex-wrap:wrap;}
.form-inline .form-group{margin-bottom:0;}
.form-inline .form-control{width:auto;}
.form-inline label{margin-bottom:0;margin-right:8px;}

/* ── Modern Cards/Panels ── */
.panel{
  background:#fff;
  border-radius:12px;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
  margin-bottom:20px;
  overflow:hidden;
  transition:all 0.3s;
}
.panel:hover{box-shadow:0 8px 24px rgba(0,0,0,.12);}
.panel-heading{
  padding:20px 24px;
  font-weight:700;
  font-size:18px;
  border-bottom:1px solid #f0f2f5;
}
.panel-body{padding:24px;}
.panel-default .panel-heading{background:#f7f8fa;color:#1c1e21;}
.panel-info .panel-heading{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;}
.panel-success .panel-heading{background:linear-gradient(135deg,#56ab2f,#a8e063);color:#fff;}
.panel-warning .panel-heading{background:linear-gradient(135deg,#f093fb,#f5576c);color:#fff;}
.panel-danger .panel-heading{background:linear-gradient(135deg,#eb3349,#f45c43);color:#fff;}

/* ── Modern Alerts ── */
.alert{
  padding:16px 20px;
  border-radius:12px;
  margin-bottom:20px;
  font-weight:500;
  border:none;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
}
.alert-success{background:linear-gradient(135deg,#d4fc79,#96e6a1);color:#155724;}
.alert-info{background:linear-gradient(135deg,#a1c4fd,#c2e9fb);color:#0c5460;}
.alert-warning{background:linear-gradient(135deg,#ffecd2,#fcb69f);color:#856404;}
.alert-danger{background:linear-gradient(135deg,#fbc2eb,#f093fb);color:#721c24;}
.close{
  float:right;
  font-size:24px;
  font-weight:700;
  line-height:1;
  color:inherit;
  opacity:.5;
  background:none;
  border:none;
  cursor:pointer;
}
.close:hover{opacity:.8;}

/* ── Modern Tables ── */
.table{
  width:100%;
  border-collapse:separate;
  border-spacing:0;
  background:#fff;
  border-radius:12px;
  overflow:hidden;
  box-shadow:0 2px 8px rgba(0,0,0,.08);
}
.table th{
  background:linear-gradient(135deg,#667eea,#764ba2);
  color:#fff;
  padding:16px;
  font-weight:600;
  text-align:left;
  border:none;
}
.table td{
  padding:14px 16px;
  border-bottom:1px solid #f0f2f5;
}
.table tbody tr:last-child td{border-bottom:none;}
.table-hover tbody tr{transition:all 0.2s;}
.table-hover tbody tr:hover{background:#f7f8fa;transform:scale(1.01);}
.table-striped tbody tr:nth-child(odd){background:#fafbfc;}

/* ── Labels & Badges ── */
.label,.badge{
  display:inline-block;
  padding:4px 10px;
  font-size:12px;
  font-weight:600;
  border-radius:12px;
  color:#fff;
}
.label-success{background:linear-gradient(135deg,#56ab2f,#a8e063);}
.label-info{background:linear-gradient(135deg,#00c6ff,#0072ff);}
.label-warning{background:linear-gradient(135deg,#f093fb,#f5576c);}
.label-danger{background:linear-gradient(135deg,#eb3349,#f45c43);}
.label-default{background:#65676b;}

/* ── Sidebar (Instagram style) ── */
.sidebar{
  position:fixed;
  left:0;
  top:60px;
  width:240px;
  height:calc(100vh - 60px);
  background:#fff;
  box-shadow:2px 0 8px rgba(0,0,0,.08);
  padding:20px 0;
  overflow-y:auto;
}
.sidebar a{
  display:flex;
  align-items:center;
  gap:12px;
  padding:12px 20px;
  color:#65676b;
  font-weight:500;
  transition:all 0.2s;
  border-left:3px solid transparent;
}
.sidebar a:hover,.sidebar a.active{
  background:linear-gradient(90deg,rgba(102,126,234,.1),transparent);
  color:#667eea;
  border-left-color:#667eea;
}
.sidebar .hdr{
  color:#8a8d91;
  font-size:12px;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:0.5px;
  padding:16px 20px 8px;
  margin-top:12px;
}

/* ── Main Content (with sidebar) ── */
.content-wrap{
  margin-left:240px;
  padding:80px 24px 24px;
  min-height:100vh;
}
.main-content{
  background:#fff;
  border-radius:16px;
  padding:32px;
  box-shadow:0 4px 12px rgba(0,0,0,.1);
  margin-bottom:24px;
}
.main-content-full{
  padding:80px 24px 24px;
  min-height:100vh;
}

/* ── Page Header ── */
.page-header{
  border-bottom:2px solid #f0f2f5;
  padding-bottom:16px;
  margin-bottom:24px;
}
.page-header h2{
  font-size:28px;
  font-weight:700;
  background:linear-gradient(135deg,#667eea,#764ba2);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  background-clip:text;
}

/* ── Stat Cards (Dashboard) ── */
.card-stat{
  text-align:center;
  padding:28px;
  border-radius:16px;
  color:#fff;
  box-shadow:0 4px 12px rgba(0,0,0,.15);
  transition:all 0.3s;
}
.card-stat:hover{transform:translateY(-8px);box-shadow:0 12px 24px rgba(0,0,0,.2);}
.card-stat h2{
  font-size:42px;
  font-weight:700;
  margin-bottom:8px;
  color:#fff;
}
.card-stat p{
  font-size:14px;
  font-weight:500;
  opacity:.9;
  margin:0;
}

/* ── Thumbnails (Home cards) ── */
.thumbnail{
  background:#fff;
  border-radius:16px;
  padding:28px;
  text-align:center;
  box-shadow:0 4px 12px rgba(0,0,0,.08);
  transition:all 0.3s;
  border:2px solid transparent;
  height:100%;
  display:flex;
  flex-direction:column;
  justify-content:center;
}
.thumbnail:hover{
  transform:translateY(-8px);
  box-shadow:0 12px 28px rgba(0,0,0,.15);
  border-color:#667eea;
}
.thumbnail h4{
  font-size:18px;
  font-weight:700;
  color:#1c1e21;
  margin:12px 0 8px;
}
.thumbnail .text-muted{
  color:#65676b;
  font-size:13px;
}

/* ── Footer ── */
footer{
  text-align:center;
  padding:24px;
  color:#8a8d91;
  font-size:14px;
  background:#fff;
  border-radius:12px;
  margin-top:24px;
  box-shadow:0 -2px 8px rgba(0,0,0,.05);
}

/* ── Utilities ── */
.text-center{text-align:center;}
.text-right{text-align:right;}
.text-muted{color:#65676b;}
.text-info{color:#0072ff;}
.text-danger{color:#f45c43;}
.text-success{color:#56ab2f;}
mark{background:#fff59d;padding:2px 6px;border-radius:4px;font-weight:600;}

/* ── Smooth Scrollbar ── */
::-webkit-scrollbar{width:8px;}
::-webkit-scrollbar-track{background:#f0f2f5;}
::-webkit-scrollbar-thumb{background:#ccd0d5;border-radius:4px;}
::-webkit-scrollbar-thumb:hover{background:#8a8d91;}
</style>
<script>
// Modern interactions
document.addEventListener('DOMContentLoaded',function(){
  // Close alert buttons
  document.querySelectorAll('.close').forEach(b=>{
    b.onclick=()=>b.parentElement.style.display='none';
  });
  
  // Smooth scroll
  document.querySelectorAll('a[href^="#"]').forEach(a=>{
    a.onclick=e=>{
      e.preventDefault();
      document.querySelector(a.getAttribute('href'))?.scrollIntoView({behavior:'smooth'});
    };
  });
});
</script>
"""

def layout(title, body, session, active=""):
    user = session["HoTen"] if session else ""
    nav_links = ""
    if session:
        nav_links = f"""
        <li class="dropdown">
          <a href="#">
            👤 {user} ▾
          </a>
          <ul class="dropdown-menu">
            <li><a href="/logout">🚪 Đăng xuất</a></li>
          </ul>
        </li>"""

    if session:
        def li(href,icon,label,key):
            cls = "active" if active==key else ""
            return f'<a href="{href}" class="{cls}">{icon} {label}</a>'
        sidebar_html = f"""
        <div class="sidebar">
          <div class="hdr">Dashboard</div>
          {li("/","🏠","Trang chủ","home")}
          <div class="hdr">Quản lý</div>
          {li("/monhoc","📚","Môn học","monhoc")}
          {li("/sinhvien","👨‍🎓","Sinh viên","sinhvien")}
          {li("/cauhoi","📝","Câu hỏi","cauhoi")}
          {li("/dethi","📄","Đề thi","dethi")}
          {li("/dethi/create","➕","Soạn đề mới","dethi_create")}
          {li("/ketqua","✏️","Nhập điểm","ketqua")}
          <div class="hdr">Tra cứu & Báo cáo</div>
          {li("/dethi/tracuu","🔍","Tra cứu đề","tracuu")}
          {li("/baocao","📊","Báo cáo năm","baocao")}
          <div class="hdr">Cài đặt</div>
          {li("/thamso","⚙️","Tham số","thamso")}
        </div>
        <div class="content-wrap">
          <div class="main-content">{body}</div>
          <footer>© 2026 Nhóm 15 – SE104.Q23 | 🎓 Quản Lý Ra Đề và Chấm Thi</footer>
        </div>"""
    else:
        sidebar_html = f'<div class="main-content-full">{body}</div><footer>© 2026 Nhóm 15 – SE104.Q23</footer>'

    return f"""<!DOCTYPE html><html lang="vi">
<head>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>{title} – Quản Lý Ra Đề & Chấm Thi</title>
{STYLE}
<script>
// Force reload when navigating - bypass cache completely
window.addEventListener('pageshow', function(event) {{
  if (event.persisted) {{
    window.location.reload(true);
  }}
}});
</script>
</head>
<body>
<nav class="navbar navbar-inverse" style="position:fixed;top:0;width:100%;z-index:1000;background:#222;min-height:50px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;">
  <a class="navbar-brand" href="/" style="color:#fff;font-size:18px;font-weight:bold;text-decoration:none;">🎓 Quản Lý Ra Đề &amp; Chấm Thi</a>
  <ul style="list-style:none;margin:0;padding:0;display:flex;position:relative;">{nav_links}</ul>
</nav>
{sidebar_html}
</body></html>"""

def alert(msg, kind="success"):
    icon = "✅" if kind=="success" else "❌"
    return f'<div class="alert alert-{kind} alert-dismissible"><button class="close" data-dismiss="alert">&times;</button>{icon} {msg}</div>'

# ══════════════════════════════════════════════════════════════════════
# ROUTE HANDLER
# ══════════════════════════════════════════════════════════════════════
class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silence logs

    def set_cookie(self, name, value, max_age=86400):
        """Set a cookie - call before end_headers()"""
        self.send_header("Set-Cookie", f"{name}={value}; Path=/; Max-Age={max_age}; HttpOnly")

    def send_html(self, html, code=200, headers=None):
        body = html.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type","text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Content-Length", str(len(body)))
        if headers:
            for k,v in headers.items():
                self.send_header(k,v)
        self.end_headers()
        self.wfile.write(body)

    def redirect(self, loc, extra_headers=None):
        # Use standard 302 redirect - cookie will carry session
        self.send_response(302)
        self.send_header("Location", loc)
        if extra_headers:
            for k,v in extra_headers.items():
                self.send_header(k,v)
        self.end_headers()

    def parse_body(self):
        length = int(self.headers.get("Content-Length",0))
        raw = self.rfile.read(length).decode("utf-8") if length else ""
        return urllib.parse.parse_qs(raw, keep_blank_values=True)

    def pv(self, form, key, default=""):
        return form.get(key,[""])[0] or default

    # ── PAGES ─────────────────────────────────────────────────────────
    def page_login(self, error=""):
        err_html = f'<div class="alert alert-danger">{error}</div>' if error else ""
        body = f"""
        <div style="max-width:440px;margin:80px auto;">
          <div style="background:#fff;border-radius:20px;padding:48px;box-shadow:0 20px 60px rgba(0,0,0,.3);">
            <div style="text-align:center;margin-bottom:24px;">
              <div style="font-size:72px;margin-bottom:8px;">🎓</div>
              <h1 style="font-size:28px;font-weight:700;background:linear-gradient(135deg,#667eea,#764ba2);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:8px;">
                Quản Lý Ra Đề & Chấm Thi
              </h1>
              <p style="color:#65676b;font-size:14px;margin:0;">Nhóm 15 – SE104.Q23</p>
            </div>
            {err_html}
            <form method="post" action="/login">
              <div class="form-group">
                <label>Tên đăng nhập</label>
                <input name="username" class="form-control" placeholder="Nhập tên đăng nhập" required autofocus>
              </div>
              <div class="form-group">
                <label>Mật khẩu</label>
                <input name="password" type="password" class="form-control" placeholder="Nhập mật khẩu" required>
              </div>
              <button type="submit" class="btn btn-primary btn-block btn-lg" style="margin-top:24px;">
                🔑 Đăng nhập
              </button>
            </form>
            <div style="text-align:center;margin-top:24px;padding-top:24px;border-top:1px solid #f0f2f5;">
              <p style="color:#65676b;font-size:13px;margin-bottom:12px;">
                Chưa có tài khoản? <a href="/register" style="color:#667eea;font-weight:600;text-decoration:none;">Đăng ký ngay</a>
              </p>
              <p style="color:#999;font-size:12px;margin:0;">
                💡 Demo: <strong>gv01</strong> / <strong>123456</strong>
              </p>
            </div>
          </div>
        </div>"""
        return f"""<!DOCTYPE html><html lang="vi">
<head><title>Đăng nhập – Quản Lý Ra Đề &amp; Chấm Thi</title>{STYLE}</head>
<body style="display:flex;align-items:center;justify-content:center;min-height:100vh;">
{body}
</body></html>"""

    def page_register(self, error="", success=""):
        err_html = f'<div class="alert alert-danger">{error}</div>' if error else ""
        suc_html = f'<div class="alert alert-success">{success}</div>' if success else ""
        body = f"""
        <div style="max-width:480px;margin:60px auto;">
          <div style="background:#fff;border-radius:20px;padding:48px;box-shadow:0 20px 60px rgba(0,0,0,.3);">
            <div style="text-align:center;margin-bottom:24px;">
              <div style="font-size:64px;margin-bottom:8px;">👨‍🏫</div>
              <h1 style="font-size:26px;font-weight:700;background:linear-gradient(135deg,#667eea,#764ba2);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:8px;">
                Đăng ký tài khoản Giảng viên
              </h1>
              <p style="color:#65676b;font-size:13px;margin:0;">Tạo tài khoản để sử dụng hệ thống</p>
            </div>
            {err_html}{suc_html}
            <form method="post" action="/register">
              <div class="form-group">
                <label>Họ và tên <span class="text-danger">*</span></label>
                <input name="hoten" class="form-control" placeholder="VD: Nguyễn Văn A" required autofocus>
              </div>
              <div class="form-group">
                <label>Tên đăng nhập <span class="text-danger">*</span></label>
                <input name="username" class="form-control" placeholder="VD: nguyenvana" required pattern="[a-z0-9]+" title="Chỉ chữ thường và số, không dấu">
                <small class="text-muted">Chỉ dùng chữ thường và số (a-z, 0-9)</small>
              </div>
              <div class="form-group">
                <label>Mật khẩu <span class="text-danger">*</span></label>
                <input name="password" type="password" class="form-control" placeholder="Tối thiểu 6 ký tự" required minlength="6">
              </div>
              <div class="form-group">
                <label>Xác nhận mật khẩu <span class="text-danger">*</span></label>
                <input name="password2" type="password" class="form-control" placeholder="Nhập lại mật khẩu" required minlength="6">
              </div>
              <div class="form-group">
                <label>Email</label>
                <input name="email" type="email" class="form-control" placeholder="example@uit.edu.vn (tùy chọn)">
              </div>
              <button type="submit" class="btn btn-success btn-block btn-lg" style="margin-top:24px;">
                ✅ Đăng ký tài khoản
              </button>
            </form>
            <div style="text-align:center;margin-top:24px;padding-top:24px;border-top:1px solid #f0f2f5;">
              <p style="color:#65676b;font-size:13px;margin:0;">
                Đã có tài khoản? <a href="/login" style="color:#667eea;font-weight:600;text-decoration:none;">Đăng nhập</a>
              </p>
            </div>
          </div>
        </div>"""
        return f"""<!DOCTYPE html><html lang="vi">
<head><title>Đăng ký – Quản Lý Ra Đề &amp; Chấm Thi</title>{STYLE}</head>
<body style="display:flex;align-items:center;justify-content:center;min-height:100vh;">
{body}
</body></html>"""

    def page_home(self, session):
        import time
        sid_debug = self.sid if hasattr(self, 'sid') and self.sid else 'EMPTY!!!'
        print(f"[page_home] self.sid = {sid_debug}", flush=True)
        ts = int(time.time() * 1000)  # timestamp to bypass cache
        body = f"""
        <div class="page-header"><h2>🏠 Trang chủ</h2></div>
        <div class="alert alert-success"><h4>👋 Xin chào, <strong>{session['HoTen']}</strong>!</h4>
        Chào mừng đến với Hệ thống Quản lý Ra đề và Chấm thi.</div>
        <div class="row" style="margin-top:20px;">
          <div class="col-md-3">
            <a href="/cauhoi?_t={ts}" style="text-decoration:none;">
            <div class="thumbnail text-center" style="padding:20px;border:2px solid #3498db;">
              <div style="font-size:48px;">📋</div>
              <h4 style="color:#2c3e50;">Ngân hàng câu hỏi</h4>
              <p class="text-muted small">Soạn và quản lý câu hỏi</p>
            </div></a>
          </div>
          <div class="col-md-3">
            <a href="/dethi/create?_t={ts}" style="text-decoration:none;">
            <div class="thumbnail text-center" style="padding:20px;border:2px solid #27ae60;">
              <div style="font-size:48px;">➕</div>
              <h4 style="color:#2c3e50;">Soạn đề thi</h4>
              <p class="text-muted small">Tạo đề thi mới</p>
            </div></a>
          </div>
          <div class="col-md-3">
            <a href="/ketqua?_t={ts}" style="text-decoration:none;">
            <div class="thumbnail text-center" style="padding:20px;border:2px solid #e74c3c;">
              <div style="font-size:48px;">✏️</div>
              <h4 style="color:#2c3e50;">Nhập điểm</h4>
              <p class="text-muted small">Ghi nhận kết quả chấm thi</p>
            </div></a>
          </div>
          <div class="col-md-3">
            <a href="/baocao?_t={ts}" style="text-decoration:none;">
            <div class="thumbnail text-center" style="padding:20px;border:2px solid #f39c12;">
              <div style="font-size:48px;">📊</div>
              <h4 style="color:#2c3e50;">Báo cáo năm</h4>
              <p class="text-muted small">Thống kê phân loại điểm</p>
            </div></a>
          </div>
        </div>
        <div class="row" style="margin-top:15px;">
          <div class="col-md-6">
            <div class="panel panel-info">
              <div class="panel-heading">📖 Hướng dẫn sử dụng</div>
              <div class="panel-body">
                <ol>
                  <li>Vào <strong>Ngân hàng câu hỏi</strong> để thêm câu hỏi</li>
                  <li>Vào <strong>Soạn đề thi</strong> để tạo đề từ ngân hàng</li>
                  <li>Sau khi thi, vào <strong>Nhập điểm</strong> để ghi nhận kết quả</li>
                  <li>Xem <strong>Báo cáo năm</strong> để thống kê tổng kết</li>
                </ol>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="panel panel-warning">
              <div class="panel-heading">📌 Quy định hệ thống</div>
              <div class="panel-body">
                <ul>
                  <li>Mỗi đề thi tối đa <strong>5 câu hỏi</strong></li>
                  <li>Thời lượng thi: <strong>30 – 180 phút</strong></li>
                  <li>Điểm số: <strong>0.0 – 10.0</strong></li>
                  <li>Điểm chữ tự động tính theo bảng quy đổi</li>
                </ul>
              </div>
            </div>
          </div>
        </div>"""
        return layout("Trang chủ", body, session, "home")

    def page_cauhoi(self, session, flash=""):
        conn = get_db()
        cur = conn.cursor()
        ma_gv = session["MaGV"]
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        f_mon = params.get("maMonFilter",[""])[0]
        f_dk  = params.get("maDoKhoFilter",[""])[0]
        f_search = params.get("search",[""])[0].strip()

        sql = """SELECT c.MaCH, c.NoiDung, m.TenMon, d.TenDoKho, d.MaDoKho
                 FROM CAU_HOI c
                 JOIN MON_HOC m ON m.MaMon=c.MaMon
                 JOIN DO_KHO d ON d.MaDoKho=c.MaDoKho
                 WHERE m.MaGV=?"""
        args = [ma_gv]
        if f_search: 
            sql += " AND c.NoiDung LIKE ?"
            args.append(f"%{f_search}%")
        if f_mon: sql += " AND c.MaMon=?"; args.append(f_mon)
        if f_dk:  sql += " AND c.MaDoKho=?"; args.append(f_dk)
        rows = cur.execute(sql, args).fetchall()
        monhocs = cur.execute("SELECT MaMon,TenMon FROM MON_HOC WHERE MaGV=?", (ma_gv,)).fetchall()
        dokhoes = cur.execute("SELECT MaDoKho,TenDoKho FROM DO_KHO").fetchall()
        
        # Đếm số câu hỏi theo môn để cảnh báo
        mon_counts = {}
        for mh in monhocs:
            count = cur.execute("SELECT COUNT(*) FROM CAU_HOI WHERE MaMon=?", (mh[0],)).fetchone()[0]
            mon_counts[mh[0]] = count
        
        release_db(conn)

        mon_opts = "<option value=''>-- Tất cả --</option>" + "".join(
            f"<option value='{r[0]}' {'selected' if str(r[0])==f_mon else ''}>{r[1]}</option>" for r in monhocs)
        dk_opts = "<option value=''>-- Tất cả --</option>" + "".join(
            f"<option value='{r[0]}' {'selected' if str(r[0])==f_dk else ''}>{r[1]}</option>" for r in dokhoes)

        dk_badge = {1:("success","Dễ"),2:("info","Trung Bình"),3:("warning","Phức Tạp"),4:("danger","Khó")}
        rows_html = ""
        for r in rows:
            bclass, btext = dk_badge.get(r[4], ("default","?"))
            nd = r[1][:90]+"..." if len(r[1])>90 else r[1]
            # Highlight từ khóa tìm kiếm
            if f_search and f_search.lower() in nd.lower():
                import re
                nd = re.sub(f"({re.escape(f_search)})", r'<mark style="background:#ff0;padding:2px 4px;font-weight:bold;">\1</mark>', nd, flags=re.IGNORECASE)
            rows_html += f"""<tr>
              <td>{r[0]}</td>
              <td>{nd}</td>
              <td>{r[2]}</td>
              <td><span class="label label-{bclass}">{r[3]}</span></td>
              <td>
                <a href="/cauhoi/edit/{r[0]}?sid={self.sid}" class="btn btn-xs btn-warning">✏️ Sửa</a>
                <a href="/cauhoi/delete/{r[0]}?sid={self.sid}" class="btn btn-xs btn-danger"
                   onclick="return confirm('Xóa câu hỏi này?')">🗑️ Xóa</a>
              </td>
            </tr>"""
        if not rows_html:
            rows_html = "<tr><td colspan='5' class='text-center text-muted'><i>Chưa có câu hỏi nào</i></td></tr>"

        search_value = params.get("search",[""])[0]
        search_info = f'<div class="alert alert-info">🔍 Tìm kiếm: "<strong>{search_value}</strong>" - Tìm thấy <strong>{len(rows)}</strong> kết quả</div>' if search_value else ""
        
        # Cảnh báo thiếu câu hỏi
        warnings_html = ""
        low_question_subjects = [(mh[1], mon_counts[mh[0]]) for mh in monhocs if mon_counts[mh[0]] < 10]
        if low_question_subjects:
            warnings_list = "".join([f"<li><strong>{mh[0]}</strong>: {mh[1]} câu hỏi</li>" for mh in low_question_subjects])
            warnings_html = f"""
            <div class="alert alert-warning">
              <strong>⚠️ Cảnh báo thiếu câu hỏi!</strong>
              <p style="margin:8px 0 0 0;">Các môn học sau cần bổ sung thêm câu hỏi (tối thiểu 10 câu):</p>
              <ul style="margin:8px 0 0 20px;">{warnings_list}</ul>
            </div>"""
        
        body = f"""
        <div class="page-header"><h2>📋 Ngân hàng câu hỏi</h2></div>
        {flash}
        {warnings_html}
        <div class="panel panel-default">
          <div class="panel-body">
            <form class="form-inline" method="get" style="margin-bottom:10px;">
              <input type="hidden" name="sid" value="{self.sid}">
              <div class="form-group">
                <input type="text" name="search" class="form-control" placeholder="🔍 Tìm kiếm nội dung câu hỏi..." 
                       value="{search_value}" style="width:300px;margin-right:10px;">
              </div>
              <button class="btn btn-primary">🔎 Tìm</button>
              <a href="/cauhoi?sid={self.sid}" class="btn btn-default">Xóa tìm kiếm</a>
            </form>
            <form class="form-inline" method="get">
              <input type="hidden" name="sid" value="{self.sid}">
              <input type="hidden" name="search" value="{search_value}">
              <div class="form-group">Môn học: <select name="maMonFilter" class="form-control" style="margin:0 10px;">{mon_opts}</select></div>
              <div class="form-group">Độ khó: <select name="maDoKhoFilter" class="form-control" style="margin:0 10px;">{dk_opts}</select></div>
              <button class="btn btn-info">🔍 Lọc</button>
              <a href="/cauhoi?search={search_value}&sid={self.sid}" class="btn btn-default">Xóa lọc</a>
              <a href="/cauhoi/create?sid={self.sid}" class="btn btn-success pull-right">➕ Thêm câu hỏi</a>
            </form>
          </div>
        </div>
        {search_info}
        <table class="table table-bordered table-striped table-hover">
          <thead><tr><th>Mã CH</th><th>Nội dung</th><th>Môn học</th><th>Độ khó</th><th>Thao tác</th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>
        <p class="text-muted">Tổng số: <strong>{len(rows)}</strong> câu hỏi</p>"""
        return layout("Câu hỏi", body, session, "cauhoi")

    def page_cauhoi_create(self, session, flash="", old=None):
        conn = get_db(); cur = conn.cursor()
        monhocs = cur.execute("SELECT MaMon,TenMon FROM MON_HOC WHERE MaGV=?", (session["MaGV"],)).fetchall()
        dokhoes = cur.execute("SELECT MaDoKho,TenDoKho FROM DO_KHO").fetchall()
        release_db(conn)
        old = old or {}
        mon_opts = "<option value=''>-- Chọn môn học --</option>" + "".join(
            f"<option value='{r[0]}' {'selected' if old.get('mon')==str(r[0]) else ''}>{r[1]}</option>" for r in monhocs)
        dk_opts = "<option value=''>-- Chọn độ khó --</option>" + "".join(
            f"<option value='{r[0]}' {'selected' if old.get('dk')==str(r[0]) else ''}>{r[1]}</option>" for r in dokhoes)
        body = f"""
        <div class="page-header"><h2>➕ Thêm câu hỏi mới</h2></div>
        {flash}
        <form method="post" action="/cauhoi/create?sid={self.sid}">
          <input type="hidden" name="sid" value="{self.sid}">
          <div class="panel panel-default"><div class="panel-body">
            <div class="form-group">
              <label>Môn học <span class="text-danger">*</span></label>
              <select name="MaMon" class="form-control" required>{mon_opts}</select>
            </div>
            <div class="form-group">
              <label>Độ khó <span class="text-danger">*</span></label>
              <select name="MaDoKho" class="form-control" required>{dk_opts}</select>
            </div>
            <div class="form-group">
              <label>Nội dung câu hỏi <span class="text-danger">*</span></label>
              <textarea name="NoiDung" class="form-control" rows="4" placeholder="Nhập nội dung câu hỏi..." required>{old.get('nd','')}</textarea>
            </div>
            <button class="btn btn-primary">💾 Lưu câu hỏi</button>
            <a href="/cauhoi?sid={self.sid}" class="btn btn-default">← Quay lại</a>
          </div></div>
        </form>"""
        return layout("Thêm câu hỏi", body, session, "cauhoi")

    def page_cauhoi_edit(self, session, mach, flash=""):
        conn = get_db(); cur = conn.cursor()
        row = cur.execute("SELECT MaCH,NoiDung,MaMon,MaDoKho FROM CAU_HOI WHERE MaCH=?", (mach,)).fetchone()
        monhocs = cur.execute("SELECT MaMon,TenMon FROM MON_HOC WHERE MaGV=?", (session["MaGV"],)).fetchall()
        dokhoes = cur.execute("SELECT MaDoKho,TenDoKho FROM DO_KHO").fetchall()
        release_db(conn)
        if not row: return self.send_html("Not found", 404)
        mon_opts = "".join(
            f"<option value='{r[0]}' {'selected' if r[0]==row[2] else ''}>{r[1]}</option>" for r in monhocs)
        dk_opts = "".join(
            f"<option value='{r[0]}' {'selected' if r[0]==row[3] else ''}>{r[1]}</option>" for r in dokhoes)
        body = f"""
        <div class="page-header"><h2>✏️ Sửa câu hỏi #{row[0]}</h2></div>
        {flash}
        <form method="post" action="/cauhoi/edit/{row[0]}?sid={self.sid}">
          <input type="hidden" name="sid" value="{self.sid}">
          <div class="panel panel-default"><div class="panel-body">
            <div class="form-group">
              <label>Môn học</label>
              <select name="MaMon" class="form-control">{mon_opts}</select>
            </div>
            <div class="form-group">
              <label>Độ khó</label>
              <select name="MaDoKho" class="form-control">{dk_opts}</select>
            </div>
            <div class="form-group">
              <label>Nội dung câu hỏi</label>
              <textarea name="NoiDung" class="form-control" rows="4">{row[1]}</textarea>
            </div>
            <button class="btn btn-primary">💾 Cập nhật</button>
            <a href="/cauhoi?sid={self.sid}" class="btn btn-default">← Quay lại</a>
          </div></div>
        </form>"""
        return layout("Sửa câu hỏi", body, session, "cauhoi")

    def page_dethi_list(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        
        # Lấy filter từ query string
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        filter_type = params.get("filter",[""])[0]
        
        rows = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.ThoiLuong,d.NgayThi,
                                    (SELECT COUNT(*) FROM CT_DETHI WHERE MaDT=d.MaDT),
                                    (SELECT COUNT(*) FROM KET_QUA WHERE MaDT=d.MaDT)
                              FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                              WHERE d.MaGV=? ORDER BY d.MaDT DESC""", (session["MaGV"],)).fetchall()
        
        # Filter đề chưa chấm
        if filter_type == "unchecked":
            rows = [r for r in rows if r[7] == 0]
        
        release_db(conn)
        rows_html = ""
        for r in rows:
            ngay = r[5] if r[5] else "--"
            # Badge cho trạng thái chấm
            status_badge = f'<span class="label label-success">✓ Đã chấm ({r[7]} SV)</span>' if r[7] > 0 else '<span class="label label-warning">⏳ Chưa chấm</span>'
            rows_html += f"""<tr>
              <td>DT-{r[0]:03d}</td><td>{r[1]}</td>
              <td><span class="badge">HK {r[2]}</span></td>
              <td>{r[3]}</td><td>{r[4]} phút</td><td>{ngay}</td>
              <td>{status_badge}</td>
              <td>
                <a href="/dethi/{r[0]}?sid={self.sid}" class="btn btn-xs btn-info">👁 Xem</a>
                <a href="/ketqua/nhap/{r[0]}?sid={self.sid}" class="btn btn-xs btn-warning">✏️ Nhập điểm</a>
              </td>
            </tr>"""
        if not rows_html:
            rows_html = "<tr><td colspan='8' class='text-center text-muted'><i>Chưa có đề thi nào</i></td></tr>"
        
        filter_active = ' class="active"' if filter_type == "unchecked" else ""
        filter_btns = f"""
        <div class="btn-group" style="margin-bottom:15px;">
          <a href="/dethi?sid={self.sid}" class="btn btn-default">📋 Tất cả</a>
          <a href="/dethi?filter=unchecked&sid={self.sid}" class="btn btn-warning{filter_active}">⏳ Chưa chấm</a>
        </div>"""
        
        body = f"""
        <div class="page-header"><h2>📄 Danh sách đề thi</h2></div>
        {flash}
        <div style="margin-bottom:15px;">
          <a href="/dethi/create?sid={self.sid}" class="btn btn-success">➕ Soạn đề thi mới</a>
          <a href="/dethi/tracuu?sid={self.sid}" class="btn btn-info">🔍 Tra cứu</a>
        </div>
        {filter_btns}
        <table class="table table-bordered table-striped table-hover">
          <thead><tr><th>Mã ĐT</th><th>Môn học</th><th>HK</th><th>Năm học</th><th>Thời lượng</th><th>Ngày thi</th><th>Trạng thái</th><th>Thao tác</th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>
        <p class="text-muted">Tổng số: <strong>{len(rows)}</strong> đề thi</p>"""
        return layout("Đề thi", body, session, "dethi")

    def page_dethi_create(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        monhocs = cur.execute("SELECT MaMon,TenMon FROM MON_HOC WHERE MaGV=?", (session["MaGV"],)).fetchall()
        dokhoes = cur.execute("SELECT MaDoKho,TenDoKho FROM DO_KHO").fetchall()
        release_db(conn)
        mon_opts = "<option value=''>-- Chọn môn học --</option>" + "".join(
            f"<option value='{r[0]}'>{r[1]}</option>" for r in monhocs)
        dk_opts = "<option value=''>Tất cả độ khó</option>" + "".join(
            f"<option value='{r[0]}'>{r[1]}</option>" for r in dokhoes)
        body = f"""
        <div class="page-header"><h2>➕ Soạn đề thi mới</h2></div>
        {flash}
        <form method="post" action="/dethi/create?sid={self.sid}">
          <input type="hidden" name="sid" value="{self.sid}">
          <div class="row">
            <div class="col-md-5">
              <div class="panel panel-primary">
                <div class="panel-heading">📝 Thông tin đề thi</div>
                <div class="panel-body">
                  <div class="form-group">
                    <label>Môn học <span class="text-danger">*</span></label>
                    <select name="MaMon" id="ddlMon" class="form-control" required>{mon_opts}</select>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group"><label>Học kỳ</label>
                        <select name="HocKy" class="form-control">
                          <option value="1">Học kỳ 1</option>
                          <option value="2">Học kỳ 2</option>
                        </select>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group"><label>Năm học</label>
                        <input name="NamHoc" class="form-control" placeholder="2024-2025" value="{date.today().year-1}-{date.today().year}" required>
                      </div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-md-6">
                      <div class="form-group"><label>Thời lượng (phút)</label>
                        <input name="ThoiLuong" type="number" class="form-control" min="30" max="180" value="90" required>
                      </div>
                    </div>
                    <div class="col-md-6">
                      <div class="form-group"><label>Ngày thi</label>
                        <input name="NgayThi" type="date" class="form-control">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="panel panel-success">
                <div class="panel-heading">✅ Câu hỏi đã chọn: <span id="cnt">0</span>/5</div>
                <div class="panel-body" id="chosen" style="min-height:60px;"><em class="text-muted">Chưa chọn câu hỏi nào</em></div>
              </div>
              <div id="hidden_inputs"></div>
              <button type="submit" class="btn btn-primary btn-block btn-lg">💾 Lưu đề thi</button>
              <a href="/dethi?sid={self.sid}" class="btn btn-default btn-block" style="margin-top:5px;">← Hủy bỏ</a>
            </div>
            <div class="col-md-7">
              <div class="panel panel-default">
                <div class="panel-heading">📚 Ngân hàng câu hỏi <small class="text-warning">(Tối đa 5 câu)</small></div>
                <div class="panel-body">
                  <div class="form-inline" style="margin-bottom:10px;">
                    Lọc độ khó: <select id="fdk" class="form-control" style="margin:0 8px;">{dk_opts}</select>
                    <button type="button" class="btn btn-default btn-sm" onclick="loadCauHoi()">🔍 Lọc</button>
                  </div>
                  <div id="cauhoiList" style="max-height:420px;overflow-y:auto;">
                    <em class="text-muted">Hãy chọn môn học trước ↑</em>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </form>
        <script>
        var sel = [];
        document.getElementById('ddlMon').addEventListener('change', loadCauHoi);
        function loadCauHoi(){{
          var mon = document.getElementById('ddlMon').value;
          var dk = document.getElementById('fdk').value;
          if(!mon)return;
          fetch('/api/cauhoi?maMon='+mon+'&maDoKho='+dk)
            .then(function(r){{return r.json();}}).then(function(data){{
              var html='';
              if(data.length===0){{html='<em style="color:#999;">Không có câu hỏi nào</em>';}}
              data.forEach(function(c){{
                var chk = sel.indexOf(c.MaCH)!==-1;
                var colors=['','#5cb85c','#5bc0de','#f0ad4e','#d9534f'];
                var clr = colors[c.MaDoKho]||'#777';
                html += '<div style="border-bottom:1px solid #eee;padding:8px 4px;">';
                html += '<label style="font-weight:normal;cursor:pointer;">';
                html += '<input type="checkbox" class="ckCH" value="'+c.MaCH+'" '+(chk?'checked':'')+' onchange="toggle(this,'+c.MaCH+')" style="margin-right:6px;"> ';
                html += '<strong>#'+c.MaCH+'</strong> '+c.NoiDung.substring(0,80)+(c.NoiDung.length>80?'...':'');
                html += ' <span style="background:'+clr+';color:#fff;padding:2px 6px;border-radius:3px;font-size:11px;">'+c.TenDoKho+'</span>';
                html += '</label></div>';
              }});
              document.getElementById('cauhoiList').innerHTML = html;
            }});
        }}
        function toggle(el, id){{
          if(el.checked){{
            if(sel.length>=5){{alert('Chỉ được chọn tối đa 5 câu hỏi!');el.checked=false;return;}}
            sel.push(id);
          }} else {{ sel=sel.filter(function(x){{return x!==id;}}); }}
          renderChosen();
        }}
        function remove(id){{
          sel=sel.filter(function(x){{return x!==id;}});
          var el=document.querySelector('.ckCH[value="'+id+'"]');
          if(el) el.checked=false;
          renderChosen();
        }}
        function renderChosen(){{
          document.getElementById('cnt').textContent=sel.length;
          var html=''; var hinputs='';
          if(sel.length===0){{html='<em style="color:#999;">Chưa chọn câu hỏi nào</em>';}}
          sel.forEach(function(id){{
            html+='<div style="background:#dff0d8;border:1px solid #d6e9c6;padding:5px 10px;margin-bottom:4px;border-radius:3px;">✅ Câu hỏi #'+id;
            html+=' <a href="#" onclick="remove('+id+');return false;" style="float:right;color:#333;font-weight:bold;">&times;</a></div>';
            hinputs+='<input type="hidden" name="CauHoi" value="'+id+'">';
          }});
          document.getElementById('chosen').innerHTML=html;
          document.getElementById('hidden_inputs').innerHTML=hinputs;
        }}
        </script>"""
        return layout("Soạn đề thi", body, session, "dethi_create")

    def page_dethi_detail(self, session, maDT):
        conn = get_db(); cur = conn.cursor()
        dt = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.ThoiLuong,d.NgayThi
                            FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                            WHERE d.MaDT=? AND d.MaGV=?""", (maDT, session["MaGV"])).fetchone()
        if not dt: conn.close(); return self.send_html("Not found",404)
        cauHois = cur.execute("""SELECT c.MaCH,c.NoiDung,dk.TenDoKho,dk.MaDoKho
                                 FROM CT_DETHI ct
                                 JOIN CAU_HOI c ON c.MaCH=ct.MaCH
                                 JOIN DO_KHO dk ON dk.MaDoKho=c.MaDoKho
                                 WHERE ct.MaDT=?""", (maDT,)).fetchall()
        conn.close()
        ngay = dt[5] if dt[5] else "Chưa xác định"
        dk_badge = {1:"success",2:"info",3:"warning",4:"danger"}
        chs = ""
        for i,c in enumerate(cauHois):
            bclass = dk_badge.get(c[3],"default")
            chs += f"""<div class="well well-sm" style="margin-bottom:8px;">
              <strong>Câu {i+1}:</strong>
              <span class="label label-{bclass} pull-right">{c[2]}</span>
              <p style="margin-top:5px;margin-bottom:0;">{c[1]}</p>
            </div>"""
        if not chs: chs = "<p class='text-muted'>Chưa có câu hỏi nào trong đề.</p>"
        body = f"""
        <div class="page-header"><h2>📄 Chi tiết đề thi DT-{dt[0]:03d} <small>{dt[1]}</small></h2></div>
        <div class="row">
          <div class="col-md-4">
            <div class="panel panel-info">
              <div class="panel-heading">ℹ️ Thông tin đề thi</div>
              <div class="panel-body">
                <table class="table table-condensed" style="margin:0;">
                  <tr><th>Mã đề:</th><td>DT-{dt[0]:03d}</td></tr>
                  <tr><th>Môn:</th><td>{dt[1]}</td></tr>
                  <tr><th>Học kỳ:</th><td>HK {dt[2]}</td></tr>
                  <tr><th>Năm học:</th><td>{dt[3]}</td></tr>
                  <tr><th>Thời lượng:</th><td>{dt[4]} phút</td></tr>
                  <tr><th>Ngày thi:</th><td>{ngay}</td></tr>
                  <tr><th>Số câu:</th><td><span class="badge">{len(cauHois)}</span></td></tr>
                </table>
              </div>
            </div>
            <a href="/ketqua/nhap/{dt[0]}?sid={self.sid}" class="btn btn-warning btn-block">✏️ Nhập điểm</a>
            <a href="/dethi?sid={self.sid}" class="btn btn-default btn-block" style="margin-top:5px;">← Danh sách</a>
          </div>
          <div class="col-md-8">
            <div class="panel panel-default">
              <div class="panel-heading">📚 Danh sách câu hỏi trong đề</div>
              <div class="panel-body">{chs}</div>
            </div>
          </div>
        </div>"""
        return layout("Chi tiết đề thi", body, session, "dethi")

    def page_dethi_tracuu(self, session):
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        f_mon  = params.get("tenMon",[""])[0]
        f_hk   = params.get("hocKy",[""])[0]
        f_nam  = params.get("namHoc",[""])[0]
        conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
        sql = """SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.ThoiLuong,d.NgayThi
                 FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                 WHERE d.MaGV=?"""
        args = [session["MaGV"]]
        if f_mon: sql += " AND m.TenMon LIKE ?"; args.append(f"%{f_mon}%")
        if f_hk:  sql += " AND d.HocKy=?"; args.append(f_hk)
        if f_nam: sql += " AND d.NamHoc=?"; args.append(f_nam)
        sql += " ORDER BY d.MaDT DESC"
        rows = cur.execute(sql, args).fetchall()
        namhocs = [r[0] for r in cur.execute("SELECT DISTINCT NamHoc FROM DE_THI WHERE MaGV=? ORDER BY NamHoc DESC", (session["MaGV"],)).fetchall()]
        conn.close()
        nam_opts = "<option value=''>-- Tất cả --</option>" + "".join(
            f"<option value='{n}' {'selected' if n==f_nam else ''}>{n}</option>" for n in namhocs)
        rows_html = ""
        for r in rows:
            ngay = r[5] if r[5] else "--"
            rows_html += f"""<tr>
              <td>DT-{r[0]:03d}</td><td>{r[1]}</td>
              <td><span class="badge">HK {r[2]}</span></td>
              <td>{r[3]}</td><td>{r[4]} phút</td><td>{ngay}</td>
              <td><a href="/dethi/{r[0]}?sid={self.sid}" class="btn btn-xs btn-info">👁 Chi tiết</a></td>
            </tr>"""
        if not rows_html:
            rows_html = "<tr><td colspan='7' class='text-center text-muted'><i>Không tìm thấy kết quả</i></td></tr>"
        hk_sel = lambda v: "selected" if f_hk==str(v) else ""
        body = f"""
        <div class="page-header"><h2>🔍 Tra cứu đề thi</h2></div>
        <div class="panel panel-default">
          <div class="panel-heading">Bộ lọc</div>
          <div class="panel-body">
            <form class="form-inline" method="get">
              <input type="hidden" name="sid" value="{self.sid}">
              <div class="form-group">Môn: <input name="tenMon" class="form-control" value="{f_mon}" style="margin:0 8px;width:180px;"></div>
              <div class="form-group">HK: <select name="hocKy" class="form-control" style="margin:0 8px;">
                <option value="">Tất cả</option>
                <option value="1" {hk_sel(1)}>HK 1</option>
                <option value="2" {hk_sel(2)}>HK 2</option>
              </select></div>
              <div class="form-group">Năm học: <select name="namHoc" class="form-control" style="margin:0 8px;">{nam_opts}</select></div>
              <button class="btn btn-primary">🔍 Tìm</button>
            </form>
          </div>
        </div>
        <p>Tìm thấy <strong>{len(rows)}</strong> đề thi</p>
        <table class="table table-bordered table-striped table-hover">
          <thead><tr><th>Mã ĐT</th><th>Môn</th><th>HK</th><th>Năm học</th><th>Thời lượng</th><th>Ngày thi</th><th></th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>"""
        return layout("Tra cứu", body, session, "tracuu")

    def page_ketqua(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        rows = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.NgayThi
                              FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                              WHERE d.MaGV=? ORDER BY d.MaDT DESC""", (session["MaGV"],)).fetchall()
        conn.close()
        rows_html = ""
        for r in rows:
            rows_html += f"""<tr>
              <td>DT-{r[0]:03d}</td><td>{r[1]}</td>
              <td><span class="badge">HK {r[2]}</span></td><td>{r[3]}</td>
              <td>{r[4] or '--'}</td>
              <td><a href="/ketqua/nhap/{r[0]}?sid={self.sid}" class="btn btn-sm btn-warning">✏️ Nhập điểm</a></td>
            </tr>"""
        if not rows_html:
            rows_html = "<tr><td colspan='6' class='text-center text-muted'><i>Chưa có đề thi nào</i></td></tr>"
        body = f"""
        <div class="page-header"><h2>✏️ Nhập điểm – Chọn đề thi</h2></div>
        {flash}
        <div class="alert alert-info">ℹ️ Chọn một đề thi để nhập điểm. Điểm chữ sẽ được tự động tính.</div>
        <table class="table table-bordered table-striped table-hover">
          <thead><tr><th>Mã ĐT</th><th>Môn</th><th>HK</th><th>Năm học</th><th>Ngày thi</th><th></th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>"""
        return layout("Nhập điểm", body, session, "ketqua")

    def page_nhap_diem(self, session, maDT, flash=""):
        conn = get_db(); cur = conn.cursor()
        dt = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.MaMon
                            FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                            WHERE d.MaDT=? AND d.MaGV=?""", (maDT, session["MaGV"])).fetchone()
        if not dt: conn.close(); return self.send_html("Not found",404)
        
        # Lấy TẤT CẢ sinh viên (không giới hạn theo năm học)
        svs = cur.execute("""SELECT s.MaSV,s.HoTen,l.TenLop,
                             (SELECT DiemSo FROM KET_QUA WHERE MaSV=s.MaSV AND MaDT=?),
                             (SELECT DiemChu FROM KET_QUA WHERE MaSV=s.MaSV AND MaDT=?),
                             (SELECT NgayCham FROM KET_QUA WHERE MaSV=s.MaSV AND MaDT=?)
                             FROM SINH_VIEN s JOIN LOP_HOC l ON l.MaLop=s.MaLop
                             ORDER BY l.TenLop,s.HoTen""",
                          (maDT, maDT, maDT)).fetchall()
        conn.close()
        da_cham = sum(1 for s in svs if s[3] is not None)
        
        # Tạo danh sách sinh viên với checkbox
        rows_html = ""
        for i,s in enumerate(svs):
            diem_str = str(s[3]) if s[3] is not None else ""
            diem_chu = s[4] or "--"
            ngay = s[5] or "--"
            cls = "label-" + label_class(s[4]) if s[4] else "label-default"
            
            # Tự động check nếu đã có điểm
            checked = 'checked' if s[3] is not None else ''
            row_cls = "success" if s[3] is not None else ""
            print_btn = f'<a href="/ketqua/phieu/{maDT}/{s[0]}?sid={self.sid}" class="btn btn-xs btn-info" target="_blank" title="In phiếu điểm">🖨️</a>' if s[3] is not None else ""
            
            rows_html += f"""<tr class="{row_cls} sv-row" data-masv="{s[0]}">
              <td class="text-center">
                <input type="checkbox" class="sv-checkbox" value="{s[0]}" {checked} onchange="toggleRow(this)">
              </td>
              <td>{i+1}</td><td>{s[1]}</td><td>{s[2]}</td>
              <td>
                <input type="hidden" name="maSV" value="{s[0]}" class="masv-input" disabled>
                <input type="number" name="diemSo" value="{diem_str}"
                       min="0" max="10" step="0.25" class="form-control input-sm diem-input"
                       style="width:90px;" onchange="tinhChu(this,{i})" placeholder="0-10" disabled>
              </td>
              <td><span id="chu_{i}" class="label {cls}">{diem_chu}</span></td>
              <td class="text-muted small">{ngay}</td>
              <td>{print_btn}</td>
            </tr>"""
        
        if not rows_html:
            rows_html = '<tr><td colspan="8" class="text-center text-muted"><em>Chưa có sinh viên nào trong hệ thống. Vui lòng thêm sinh viên trước!</em></td></tr>'
        
        body = f"""
        <div class="page-header">
          <h2>✏️ Nhập điểm – {dt[1]} <small>HK{dt[2]} – {dt[3]}</small></h2>
        </div>
        {flash}
        <div class="alert alert-info">
          📋 <strong>Hướng dẫn:</strong> 
          <ol style="margin:8px 0 0 0;">
            <li><strong>Bước 1:</strong> Chọn ✅ checkbox sinh viên tham gia thi</li>
            <li><strong>Bước 2:</strong> Nhập điểm số (0-10), hệ thống tự động quy đổi điểm chữ</li>
            <li><strong>Bước 3:</strong> Nhấn "💾 Lưu tất cả điểm"</li>
          </ol>
        </div>
        <div style="margin:10px 0;">
          <button type="button" class="btn btn-sm btn-success" onclick="checkAll()">✅ Chọn tất cả</button>
          <button type="button" class="btn btn-sm btn-warning" onclick="uncheckAll()">❌ Bỏ chọn tất cả</button>
          <span style="margin-left:20px;">Tổng: <strong>{len(svs)}</strong> SV | Đã chấm: <strong id="count-cham">{da_cham}</strong> | Chưa chấm: <strong id="count-chua">{len(svs)-da_cham}</strong></span>
        </div>
        <form method="post" action="/ketqua/luu/{maDT}?sid={self.sid}">
          <input type="hidden" name="sid" value="{self.sid}">
          <table class="table table-bordered table-striped">
            <thead><tr><th width="40">✅</th><th width="50">STT</th><th>Họ tên</th><th width="120">Lớp</th><th width="100">Điểm số</th><th width="80">Điểm chữ</th><th width="100">Ngày chấm</th><th width="50">In</th></tr></thead>
            <tbody>{rows_html}</tbody>
          </table>
          <button class="btn btn-primary btn-lg">💾 Lưu tất cả điểm</button>
          <a href="/ketqua?sid={self.sid}" class="btn btn-default btn-lg">← Quay lại</a>
        </form>
        <script>
        var bang=[
          {{tu:8.5,den:10,chu:'A',cls:'label-success'}},
          {{tu:8.0,den:8.49,chu:'B+',cls:'label-info'}},
          {{tu:7.0,den:7.99,chu:'B',cls:'label-info'}},
          {{tu:6.5,den:6.99,chu:'C+',cls:'label-warning'}},
          {{tu:5.5,den:6.49,chu:'C',cls:'label-warning'}},
          {{tu:5.0,den:5.49,chu:'D+',cls:'label-default'}},
          {{tu:4.0,den:4.99,chu:'D',cls:'label-default'}},
          {{tu:0.0,den:3.99,chu:'F',cls:'label-danger'}}
        ];
        function tinhChu(el,i){{
          var v=parseFloat(el.value);
          var sp=document.getElementById('chu_'+i);
          if(isNaN(v)||v<0||v>10){{sp.textContent='--';sp.className='label label-default';return;}}
          for(var b of bang){{if(v>=b.tu&&v<=b.den){{sp.textContent=b.chu;sp.className='label '+b.cls;break;}}}}
        }}
        
        // Toggle row khi check/uncheck
        function toggleRow(checkbox){{
          var row = checkbox.closest('tr');
          var inputs = row.querySelectorAll('input[name="maSV"], input[name="diemSo"]');
          if(checkbox.checked){{
            inputs.forEach(function(inp){{ inp.disabled = false; }});
            row.style.opacity = '1';
          }} else {{
            inputs.forEach(function(inp){{ inp.disabled = true; }});
            row.style.opacity = '0.4';
          }}
        }}
        
        // Chọn tất cả
        function checkAll(){{
          document.querySelectorAll('.sv-checkbox').forEach(function(cb){{
            cb.checked = true;
            toggleRow(cb);
          }});
        }}
        
        // Bỏ chọn tất cả
        function uncheckAll(){{
          document.querySelectorAll('.sv-checkbox').forEach(function(cb){{
            if(!cb.closest('tr').querySelector('input[name="diemSo"]').value){{ // Chỉ uncheck nếu chưa có điểm
              cb.checked = false;
              toggleRow(cb);
            }}
          }});
        }}
        
        // Khởi tạo trạng thái ban đầu
        document.addEventListener('DOMContentLoaded', function(){{
          document.querySelectorAll('.sv-checkbox').forEach(function(cb){{
            toggleRow(cb);
          }});
        }});
        </script>"""
        return layout("Nhập điểm", body, session, "ketqua")

    def page_baocao(self, session):
        qs = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(qs)
        conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
        namhocs = [r[0] for r in cur.execute(
            "SELECT DISTINCT NamHoc FROM DE_THI WHERE MaGV=? ORDER BY NamHoc DESC",
            (session["MaGV"],)).fetchall()]
        f_nam = params.get("namHoc",[""])[0] or (namhocs[0] if namhocs else "")
        bao_cao = []
        if f_nam:
            deThis = cur.execute(
                "SELECT d.MaDT,m.TenMon,d.HocKy FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon WHERE d.MaGV=? AND d.NamHoc=?",
                (session["MaGV"], f_nam)).fetchall()
            for dt in deThis:
                kqs = cur.execute("SELECT DiemSo,DiemChu FROM KET_QUA WHERE MaDT=?", (dt[0],)).fetchall()
                if not kqs: continue
                total = len(kqs)
                counts = {c: sum(1 for k in kqs if k[1]==c) for c in ["A","B+","B","C+","C","D+","D","F"]}
                avg = sum(k[0] for k in kqs)/total
                bao_cao.append((dt[1], dt[2], total, counts, avg))
        conn.close()
        
        # Tạo dropdown với option rỗng đầu tiên
        if namhocs:
            nam_opts = "<option value=''>-- Chọn năm học --</option>"
            nam_opts += "".join(f"<option value='{n}' {'selected' if n==f_nam else ''}>{n}</option>" for n in namhocs)
        else:
            nam_opts = "<option value=''>Chưa có dữ liệu</option>"

        bao_html = ""
        total_sv = total_f = 0
        total_kha = 0
        for bc in bao_cao:
            total_sv += bc[2]; total_f += bc[3]["F"]; total_kha += bc[3]["A"]+bc[3]["B+"]+bc[3]["B"]
            tl_dao = (bc[2]-bc[3]["F"])/bc[2]*100 if bc[2] else 0
            def pct(k): return f"{bc[3][k]/bc[2]*100:.0f}%" if bc[2] else "0%"
            bao_html += f"""
            <div class="panel panel-default">
              <div class="panel-heading">
                <h4 style="margin:0;">📘 {bc[0]} <span class="badge">HK {bc[1]}</span>
                  <span class="text-info" style="font-size:13px;margin-left:15px;">
                    Tổng: {bc[2]} SV | ĐTB: {bc[4]:.2f} | Tỉ lệ đỗ: {tl_dao:.1f}%
                  </span>
                </h4>
              </div>
              <div class="panel-body">
                <table class="table table-bordered text-center">
                  <thead><tr>
                    <th style="background:#27ae60;color:#fff;">A<br><small>≥8.5</small></th>
                    <th style="background:#2980b9;color:#fff;">B+<br><small>8.0-8.4</small></th>
                    <th style="background:#3498db;color:#fff;">B<br><small>7.0-7.9</small></th>
                    <th style="background:#f39c12;color:#fff;">C+<br><small>6.5-6.9</small></th>
                    <th style="background:#e67e22;color:#fff;">C<br><small>5.5-6.4</small></th>
                    <th style="background:#95a5a6;color:#fff;">D+<br><small>5.0-5.4</small></th>
                    <th style="background:#7f8c8d;color:#fff;">D<br><small>4.0-4.9</small></th>
                    <th style="background:#e74c3c;color:#fff;">F<br><small>&lt;4.0</small></th>
                  </tr></thead>
                  <tbody><tr>
                    <td><strong>{bc[3]['A']}</strong><br><small>{pct('A')}</small></td>
                    <td><strong>{bc[3]['B+']}</strong><br><small>{pct('B+')}</small></td>
                    <td><strong>{bc[3]['B']}</strong><br><small>{pct('B')}</small></td>
                    <td><strong>{bc[3]['C+']}</strong><br><small>{pct('C+')}</small></td>
                    <td><strong>{bc[3]['C']}</strong><br><small>{pct('C')}</small></td>
                    <td><strong>{bc[3]['D+']}</strong><br><small>{pct('D+')}</small></td>
                    <td><strong>{bc[3]['D']}</strong><br><small>{pct('D')}</small></td>
                    <td><strong style="color:#e74c3c;">{bc[3]['F']}</strong><br><small>{pct('F')}</small></td>
                  </tr></tbody>
                </table>
              </div>
            </div>"""
        stats = ""
        chart_html = ""
        if bao_cao:
            tl = (total_sv-total_f)/total_sv*100 if total_sv else 0
            stats = f"""<div class="row" style="margin-bottom:15px;">
              <div class="col-md-3"><div class="card-stat" style="background:#3498db;">
                <h2>{total_sv}</h2><p>Tổng sinh viên</p></div></div>
              <div class="col-md-3"><div class="card-stat" style="background:#27ae60;">
                <h2>{total_kha}</h2><p>Khá/Giỏi/Xuất sắc</p></div></div>
              <div class="col-md-3"><div class="card-stat" style="background:#e74c3c;">
                <h2>{total_f}</h2><p>Không đạt (F)</p></div></div>
              <div class="col-md-3"><div class="card-stat" style="background:#f39c12;">
                <h2>{tl:.1f}%</h2><p>Tỉ lệ đỗ</p></div></div>
            </div>"""
            
            # Tạo biểu đồ phân bố điểm tổng hợp
            grade_totals = {"A":0,"B+":0,"B":0,"C+":0,"C":0,"D+":0,"D":0,"F":0}
            for bc in bao_cao:
                for g in grade_totals:
                    grade_totals[g] += bc[3][g]
            max_count = max(grade_totals.values()) if grade_totals.values() else 1
            
            bars = ""
            colors = {"A":"#27ae60","B+":"#2980b9","B":"#3498db","C+":"#f39c12","C":"#e67e22","D+":"#95a5a6","D":"#7f8c8d","F":"#e74c3c"}
            for grade in ["A","B+","B","C+","C","D+","D","F"]:
                count = grade_totals[grade]
                pct_val = (count/total_sv*100) if total_sv else 0
                width = (count/max_count*100) if max_count else 0
                bars += f"""
                <div style="margin-bottom:8px;">
                  <div style="display:flex;align-items:center;">
                    <div style="width:40px;font-weight:bold;text-align:right;margin-right:10px;">{grade}</div>
                    <div style="flex:1;background:#ecf0f1;border-radius:4px;height:28px;position:relative;">
                      <div style="background:{colors[grade]};width:{width:.1f}%;height:100%;border-radius:4px;transition:width 0.3s;"></div>
                      <div style="position:absolute;top:50%;right:10px;transform:translateY(-50%);font-weight:bold;color:#2c3e50;">
                        {count} ({pct_val:.1f}%)
                      </div>
                    </div>
                  </div>
                </div>"""
            
            chart_html = f"""
            <div class="panel panel-info" style="margin-top:20px;">
              <div class="panel-heading"><h4 style="margin:0;">📊 Biểu đồ phân bố điểm tổng hợp năm học</h4></div>
              <div class="panel-body" style="padding:20px;">
                {bars}
                <p class="text-muted text-center" style="margin-top:15px;">
                  <small>Biểu đồ thể hiện tổng số sinh viên đạt từng loại điểm chữ trong toàn bộ các môn thi</small>
                </p>
              </div>
            </div>"""
        empty = "" if bao_cao else ('<div class="alert alert-warning">⚠️ Chưa có dữ liệu điểm cho năm học này.</div>' if f_nam else "")

        export_btn = f'<a href="/baocao/export-excel?namHoc={f_nam}&sid={self.sid}" class="btn btn-success" style="margin-left:10px;">📊 Xuất báo cáo Excel</a>' if (f_nam and bao_cao) else ""
        
        body = f"""
        <div class="page-header"><h2>📊 Báo cáo tổng kết năm học</h2></div>
        <form method="get" action="/baocao" class="form-inline" style="margin-bottom:15px;" onsubmit="return document.querySelector('select[name=namHoc]').value !== '';">
          <input type="hidden" name="sid" value="{self.sid}">
          <label>Năm học: </label>
          <select name="namHoc" class="form-control" style="margin:0 10px;width:150px;">{nam_opts}</select>
          <button type="submit" class="btn btn-primary">📊 Xem báo cáo</button>
          {export_btn}
        </form>
        {"<h3>Năm học: <strong>"+f_nam+"</strong></h3>" if f_nam else ""}
        {stats}{chart_html}{empty}{bao_html}"""
        return layout("Báo cáo năm", body, session, "baocao")

    def page_monhoc(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        rows = cur.execute("""SELECT m.MaMon, m.TenMon, g.HoTen 
                              FROM MON_HOC m 
                              LEFT JOIN GIANG_VIEN g ON g.MaGV=m.MaGV
                              ORDER BY m.TenMon""").fetchall()
        conn.close()
        rows_html = ""
        for r in rows:
            gv = r[2] if r[2] else "<em class='text-muted'>Chưa phân công</em>"
            rows_html += f"""<tr>
              <td class="text-center"><strong>#{r[0]}</strong></td>
              <td><span style="font-size:16px;">📖 {r[1]}</span></td>
              <td>{gv}</td>
              <td class="text-center">
                <a href="/monhoc/edit/{r[0]}?sid={self.sid}" class="btn btn-xs btn-warning">✏️ Sửa</a>
                <a href="/monhoc/delete/{r[0]}?sid={self.sid}" class="btn btn-xs btn-danger" onclick="return confirm('Xóa môn {r[1]}?')">🗑️ Xóa</a>
              </td>
            </tr>"""
        if not rows_html:
            rows_html = '<tr><td colspan="4" class="text-center text-muted">Chưa có môn học nào</td></tr>'
        body = f"""
        <div class="page-header">
          <h2>📚 Quản lý Môn học</h2>
          <a href="/monhoc/create?sid={self.sid}" class="btn btn-success pull-right" style="margin-top:-40px;">➕ Thêm môn mới</a>
        </div>
        {flash}
        <table class="table table-bordered table-striped">
          <thead><tr><th class="text-center" width="80">Mã</th><th>Tên môn học</th><th width="200">Giảng viên phụ trách</th><th class="text-center" width="150">Thao tác</th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>"""
        return layout("Môn học", body, session, "monhoc")

    def page_monhoc_create(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        gvs = cur.execute("SELECT MaGV, HoTen FROM GIANG_VIEN ORDER BY HoTen").fetchall()
        conn.close()
        gv_options = '<option value="">-- Chọn giảng viên --</option>'
        for g in gvs:
            gv_options += f'<option value="{g[0]}">{g[1]}</option>'
        body = f"""
        <div class="page-header"><h2>➕ Thêm môn học mới</h2></div>
        {flash}
        <form method="post" class="form-horizontal" style="max-width:600px;">
          <div class="form-group">
            <label class="col-sm-3 control-label">Tên môn học <span class="text-danger">*</span></label>
            <div class="col-sm-9">
              <input type="text" name="TenMon" class="form-control" placeholder="VD: Lập trình hướng đối tượng" required>
            </div>
          </div>
          <div class="form-group">
            <label class="col-sm-3 control-label">Giảng viên phụ trách</label>
            <div class="col-sm-9">
              <select name="MaGV" class="form-control">{gv_options}</select>
              <small class="text-muted">Có thể để trống, phân công sau</small>
            </div>
          </div>
          <div class="form-group">
            <div class="col-sm-offset-3 col-sm-9">
              <button type="submit" class="btn btn-success">💾 Lưu môn học</button>
              <a href="/monhoc?sid={self.sid}" class="btn btn-default">❌ Hủy</a>
            </div>
          </div>
        </form>"""
        return layout("Thêm môn học", body, session, "monhoc")

    def page_monhoc_edit(self, session, ma_mon, flash=""):
        conn = get_db(); cur = conn.cursor()
        mon = cur.execute("SELECT TenMon, MaGV FROM MON_HOC WHERE MaMon=?", (ma_mon,)).fetchone()
        if not mon:
            conn.close()
            return self.send_html("Không tìm thấy môn học", 404)
        gvs = cur.execute("SELECT MaGV, HoTen FROM GIANG_VIEN ORDER BY HoTen").fetchall()
        conn.close()
        gv_options = '<option value="">-- Chọn giảng viên --</option>'
        for g in gvs:
            sel = 'selected' if g[0] == mon[1] else ''
            gv_options += f'<option value="{g[0]}" {sel}>{g[1]}</option>'
        body = f"""
        <div class="page-header"><h2>✏️ Chỉnh sửa môn học #{ma_mon}</h2></div>
        {flash}
        <form method="post" class="form-horizontal" style="max-width:600px;">
          <div class="form-group">
            <label class="col-sm-3 control-label">Tên môn học <span class="text-danger">*</span></label>
            <div class="col-sm-9">
              <input type="text" name="TenMon" class="form-control" value="{mon[0]}" required>
            </div>
          </div>
          <div class="form-group">
            <label class="col-sm-3 control-label">Giảng viên phụ trách</label>
            <div class="col-sm-9">
              <select name="MaGV" class="form-control">{gv_options}</select>
            </div>
          </div>
          <div class="form-group">
            <div class="col-sm-offset-3 col-sm-9">
              <button type="submit" class="btn btn-success">💾 Cập nhật</button>
              <a href="/monhoc?sid={self.sid}" class="btn btn-default">❌ Hủy</a>
            </div>
          </div>
        </form>"""
        return layout("Sửa môn học", body, session, "monhoc")

    def page_sinhvien(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        rows = cur.execute("""SELECT s.MaSV, s.HoTen, s.NgaySinh, l.TenLop
                              FROM SINH_VIEN s
                              LEFT JOIN LOP_HOC l ON l.MaLop=s.MaLop
                              ORDER BY s.HoTen""").fetchall()
        conn.close()
        rows_html = ""
        for r in rows:
            lop = r[3] if r[3] else "<em class='text-muted'>Chưa vào lớp</em>"
            rows_html += f"""<tr>
              <td class="text-center"><strong>#{r[0]}</strong></td>
              <td><span style="font-size:16px;">👤 {r[1]}</span></td>
              <td class="text-center">{r[2]}</td>
              <td>{lop}</td>
              <td class="text-center">
                <a href="/sinhvien/edit/{r[0]}?sid={self.sid}" class="btn btn-xs btn-warning">✏️ Sửa</a>
                <a href="/sinhvien/delete/{r[0]}?sid={self.sid}" class="btn btn-xs btn-danger" onclick="return confirm('Xóa sinh viên {r[1]}?')">🗑️ Xóa</a>
              </td>
            </tr>"""
        if not rows_html:
            rows_html = '<tr><td colspan="5" class="text-center text-muted">Chưa có sinh viên nào</td></tr>'
        body = f"""
        <div class="page-header">
          <h2>👨‍🎓 Quản lý Sinh viên</h2>
          <a href="/sinhvien/create?sid={self.sid}" class="btn btn-success pull-right" style="margin-top:-40px;">➕ Thêm sinh viên</a>
        </div>
        {flash}
        <div class="alert alert-info">📊 Tổng số: <strong>{len(rows)} sinh viên</strong></div>
        <table class="table table-bordered table-striped">
          <thead><tr><th class="text-center" width="80">Mã SV</th><th>Họ tên</th><th class="text-center" width="120">Ngày sinh</th><th width="150">Lớp</th><th class="text-center" width="150">Thao tác</th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>"""
        return layout("Sinh viên", body, session, "sinhvien")

    def page_sinhvien_create(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        lops = cur.execute("SELECT MaLop, TenLop FROM LOP_HOC ORDER BY TenLop").fetchall()
        conn.close()
        lop_options = '<option value="">-- Chọn lớp --</option>'
        for lop in lops:
            lop_options += f'<option value="{lop[0]}">{lop[1]}</option>'
        body = f"""
        <div class="page-header"><h2>➕ Thêm sinh viên mới</h2></div>
        {flash}
        <form method="post" class="form-horizontal" style="max-width:600px;">
          <div class="form-group">
            <label class="col-sm-3 control-label">Họ tên <span class="text-danger">*</span></label>
            <div class="col-sm-9">
              <input type="text" name="HoTen" class="form-control" placeholder="VD: Nguyễn Văn A" required>
            </div>
          </div>
          <div class="form-group">
            <label class="col-sm-3 control-label">Ngày sinh <span class="text-danger">*</span></label>
            <div class="col-sm-9">
              <input type="date" name="NgaySinh" class="form-control" required>
            </div>
          </div>
          <div class="form-group">
            <label class="col-sm-3 control-label">Lớp <span class="text-danger">*</span></label>
            <div class="col-sm-9">
              <select name="MaLop" class="form-control" required>{lop_options}</select>
            </div>
          </div>
          <div class="form-group">
            <div class="col-sm-offset-3 col-sm-9">
              <button type="submit" class="btn btn-success">💾 Lưu sinh viên</button>
              <a href="/sinhvien?sid={self.sid}" class="btn btn-default">❌ Hủy</a>
            </div>
          </div>
        </form>"""
        return layout("Thêm sinh viên", body, session, "sinhvien")

    def page_sinhvien_edit(self, session, ma_sv, flash=""):
        conn = get_db(); cur = conn.cursor()
        sv = cur.execute("SELECT HoTen, NgaySinh, MaLop FROM SINH_VIEN WHERE MaSV=?", (ma_sv,)).fetchone()
        if not sv:
            conn.close()
            return self.send_html("Không tìm thấy sinh viên", 404)
        lops = cur.execute("SELECT MaLop, TenLop FROM LOP_HOC ORDER BY TenLop").fetchall()
        conn.close()
        lop_options = '<option value="">-- Chọn lớp --</option>'
        for lop in lops:
            sel = 'selected' if lop[0] == sv[2] else ''
            lop_options += f'<option value="{lop[0]}" {sel}>{lop[1]}</option>'
        body = f"""
        <div class="page-header"><h2>✏️ Chỉnh sửa sinh viên #{ma_sv}</h2></div>
        {flash}
        <form method="post" class="form-horizontal" style="max-width:600px;">
          <div class="form-group">
            <label class="col-sm-3 control-label">Họ tên <span class="text-danger">*</span></label>
            <div class="col-sm-9">
              <input type="text" name="HoTen" class="form-control" value="{sv[0]}" required>
            </div>
          </div>
          <div class="form-group">
            <label class="col-sm-3 control-label">Ngày sinh <span class="text-danger">*</span></label>
            <div class="col-sm-9">
              <input type="date" name="NgaySinh" class="form-control" value="{sv[1]}" required>
            </div>
          </div>
          <div class="form-group">
            <label class="col-sm-3 control-label">Lớp <span class="text-danger">*</span></label>
            <div class="col-sm-9">
              <select name="MaLop" class="form-control" required>{lop_options}</select>
            </div>
          </div>
          <div class="form-group">
            <div class="col-sm-offset-3 col-sm-9">
              <button type="submit" class="btn btn-success">💾 Cập nhật</button>
              <a href="/sinhvien?sid={self.sid}" class="btn btn-default">❌ Hủy</a>
            </div>
          </div>
        </form>"""
        return layout("Sửa sinh viên", body, session, "sinhvien")

    def page_thamso(self, session, flash=""):
        conn = get_db(); cur = conn.cursor()
        rows = cur.execute("SELECT TenThamSo,GiaTri,GhiChu FROM THAM_SO").fetchall()
        conn.close()
        rows_html = ""
        for r in rows:
            val = f"{r[1]} phút" if "ThoiLuong" in r[0] else str(r[1])
            rows_html += f"""<tr>
              <td><strong>{r[0]}</strong></td>
              <td><span class="badge" style="background:#337ab7;color:#000;font-weight:bold">{val}</span></td>
              <td class="text-muted">{r[2]}</td>
              <td><a href="/thamso/edit/{r[0]}?sid={self.sid}" class="btn btn-xs btn-warning">✏️ Sửa</a></td>
            </tr>"""
        body = f"""
        <div class="page-header"><h2>⚙️ Tham số hệ thống</h2></div>
        {flash}
        <div class="alert alert-info">ℹ️ Các tham số kiểm soát quy định nghiệp vụ của hệ thống.</div>
        <table class="table table-bordered table-striped">
          <thead><tr><th>Tên tham số</th><th>Giá trị</th><th>Ghi chú</th><th></th></tr></thead>
          <tbody>{rows_html}</tbody>
        </table>"""
        return layout("Tham số", body, session, "thamso")

    def page_thamso_edit(self, session, ten, flash=""):
        conn = get_db(); cur = conn.cursor()
        row = cur.execute("SELECT TenThamSo,GiaTri,GhiChu FROM THAM_SO WHERE TenThamSo=?", (ten,)).fetchone()
        conn.close()
        if not row: return self.send_html("Not found",404)
        body = f"""
        <div class="page-header"><h2>✏️ Sửa tham số: {row[0]}</h2></div>
        {flash}
        <form method="post" action="/thamso/edit/{row[0]}?sid={self.sid}" style="max-width:450px;">
          <input type="hidden" name="sid" value="{self.sid}">
          <div class="panel panel-default"><div class="panel-body">
            <div class="form-group"><label>Tên:</label><p class="form-control-static"><strong>{row[0]}</strong></p></div>
            <div class="form-group"><label>Ghi chú:</label><p class="text-muted">{row[2]}</p></div>
            <div class="form-group"><label>Giá trị mới <span class="text-danger">*</span></label>
              <input name="GiaTri" type="number" class="form-control" value="{row[1]}" required>
            </div>
            <button class="btn btn-primary">💾 Cập nhật</button>
            <a href="/thamso" class="btn btn-default">← Hủy</a>
          </div></div>
        </form>"""
        return layout("Sửa tham số", body, session, "thamso")


    # ── ROUTING ──────────────────────────────────────────────────────
    def do_GET(self):
        print(f"\n{'='*60}\n[RAW GET] {self.path}\n{'='*60}", flush=True)
        path = urllib.parse.urlparse(self.path).path.rstrip("/") or "/"
        self.sid = get_sid(self)
        session = get_session(self)
        
        # Debug logging
        print(f"[GET] {path} | sid={self.sid[:8] if self.sid else 'None'} | session={'OK' if session else 'NO'}", flush=True)

        def need_login():
            self.redirect("/login"); return None

        if path == "/login":
            return self.send_html(self.page_login())
        if path == "/register":
            return self.send_html(self.page_register())
        if path == "/logout":
            if self.sid: SESSIONS.pop(self.sid, None)
            self.sid = ""
            # Clear cookie and redirect to login
            self.send_response(302)
            self.set_cookie("sid", "", max_age=0)  # Delete cookie
            self.send_header("Location", "/login")
            self.end_headers()
            return

        if not session: 
            self.redirect("/login")
            return

        if path == "/" or path == "/home":
            return self.send_html(self.page_home(session))
        if path == "/monhoc":
            return self.send_html(self.page_monhoc(session))
        if path == "/monhoc/create":
            return self.send_html(self.page_monhoc_create(session))
        if path.startswith("/monhoc/edit/"):
            ma_mon = int(path.split("/")[-1])
            return self.send_html(self.page_monhoc_edit(session, ma_mon))
        if path.startswith("/monhoc/delete/"):
            ma_mon = int(path.split("/")[-1])
            conn = sqlite3.connect(DB_PATH)
            # Kiểm tra xem môn có câu hỏi hay đề thi không
            has_ch = conn.execute("SELECT COUNT(*) FROM CAU_HOI WHERE MaMon=?", (ma_mon,)).fetchone()[0]
            has_dt = conn.execute("SELECT COUNT(*) FROM DE_THI WHERE MaMon=?", (ma_mon,)).fetchone()[0]
            if has_ch > 0 or has_dt > 0:
                conn.close()
                flash_msg = alert(f"❌ Không thể xóa! Môn học đang có {has_ch} câu hỏi và {has_dt} đề thi.", "danger")
                return self.send_html(self.page_monhoc(session, flash_msg))
            conn.execute("DELETE FROM MON_HOC WHERE MaMon=?", (ma_mon,))
            conn.commit(); conn.close()
            self.redirect("/monhoc"); return
        if path == "/sinhvien":
            return self.send_html(self.page_sinhvien(session))
        if path == "/sinhvien/create":
            return self.send_html(self.page_sinhvien_create(session))
        if path.startswith("/sinhvien/edit/"):
            ma_sv = int(path.split("/")[-1])
            return self.send_html(self.page_sinhvien_edit(session, ma_sv))
        if path.startswith("/sinhvien/delete/"):
            ma_sv = int(path.split("/")[-1])
            conn = sqlite3.connect(DB_PATH)
            # Kiểm tra xem sinh viên có kết quả thi không
            has_kq = conn.execute("SELECT COUNT(*) FROM KET_QUA WHERE MaSV=?", (ma_sv,)).fetchone()[0]
            if has_kq > 0:
                conn.close()
                flash_msg = alert(f"❌ Không thể xóa! Sinh viên đã có {has_kq} kết quả thi.", "danger")
                return self.send_html(self.page_sinhvien(session, flash_msg))
            conn.execute("DELETE FROM SINH_VIEN WHERE MaSV=?", (ma_sv,))
            conn.commit(); conn.close()
            self.redirect("/sinhvien"); return
        if path == "/cauhoi":
            return self.send_html(self.page_cauhoi(session))
        if path == "/cauhoi/create":
            return self.send_html(self.page_cauhoi_create(session))
        if path.startswith("/cauhoi/edit/"):
            mach = int(path.split("/")[-1])
            return self.send_html(self.page_cauhoi_edit(session, mach))
        if path.startswith("/cauhoi/delete/"):
            mach = int(path.split("/")[-1])
            conn = sqlite3.connect(DB_PATH)
            conn.execute("DELETE FROM CT_DETHI WHERE MaCH=?", (mach,))
            conn.execute("DELETE FROM CAU_HOI WHERE MaCH=?", (mach,))
            conn.commit(); conn.close()
            self.redirect("/cauhoi"); return
        if path == "/dethi":
            return self.send_html(self.page_dethi_list(session))
        if path == "/dethi/create":
            return self.send_html(self.page_dethi_create(session))
        if path == "/dethi/tracuu":
            return self.send_html(self.page_dethi_tracuu(session))
        if path.startswith("/dethi/") and path.count("/")==2:
            maDT = int(path.split("/")[-1])
            return self.send_html(self.page_dethi_detail(session, maDT))
        if path == "/ketqua":
            return self.send_html(self.page_ketqua(session))
        if path.startswith("/ketqua/nhap/"):
            maDT = int(path.split("/")[-1])
            return self.send_html(self.page_nhap_diem(session, maDT))
        if path.startswith("/ketqua/phieu/"):
            # In phiếu điểm cho sinh viên
            parts = path.split("/")
            maDT = int(parts[3])
            maSV = int(parts[4])
            
            conn = get_db(); cur = conn.cursor()
            dt = cur.execute("""SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc,d.NgayThi
                                FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon
                                WHERE d.MaDT=?""", (maDT,)).fetchone()
            sv = cur.execute("""SELECT s.MaSV,s.HoTen,s.NgaySinh,l.TenLop
                                FROM SINH_VIEN s JOIN LOP_HOC l ON l.MaLop=s.MaLop
                                WHERE s.MaSV=?""", (maSV,)).fetchone()
            kq = cur.execute("""SELECT DiemSo,DiemChu,NgayCham FROM KET_QUA
                                WHERE MaSV=? AND MaDT=?""", (maSV, maDT)).fetchone()
            release_db(conn)
            
            if not (dt and sv and kq):
                return self.send_html("<h1>404</h1><p>Không tìm thấy dữ liệu</p>", 404)
            
            # HTML phiếu điểm để in
            html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Phiếu điểm - {sv[1]}</title>
<style>
body{{font-family:'Segoe UI',sans-serif;padding:40px;background:#fff;}}
.phieu{{max-width:800px;margin:0 auto;border:2px solid #333;padding:30px;}}
h1{{text-align:center;color:#2c3e50;border-bottom:3px solid #3498db;padding-bottom:10px;}}
.info{{margin:20px 0;}}
.info table{{width:100%;border-collapse:collapse;}}
.info td{{padding:8px;border:1px solid #ddd;}}
.info td:first-child{{background:#f0f2f5;font-weight:600;width:200px;}}
.diem{{text-align:center;margin:30px 0;}}
.diem-so{{font-size:48px;font-weight:700;color:#27ae60;}}
.diem-chu{{font-size:32px;color:#2980b9;}}
.footer{{margin-top:40px;text-align:right;}}
@media print{{body{{padding:0;}} .no-print{{display:none;}}}}
</style>
</head>
<body>
<div class="no-print" style="text-align:center;margin-bottom:20px;">
  <button onclick="window.print()" class="btn">🖨️ In phiếu</button>
  <button onclick="window.close()" class="btn">✖️ Đóng</button>
</div>
<div class="phieu">
  <h1>🎓 PHIẾU ĐIỂM</h1>
  <div class="info">
    <table>
      <tr><td>Họ và tên</td><td><strong>{sv[1]}</strong></td></tr>
      <tr><td>MSSV</td><td>{sv[0]}</td></tr>
      <tr><td>Ngày sinh</td><td>{sv[2]}</td></tr>
      <tr><td>Lớp</td><td>{sv[3]}</td></tr>
      <tr><td>Môn học</td><td><strong>{dt[1]}</strong></td></tr>
      <tr><td>Học kỳ / Năm học</td><td>HK{dt[2]} – {dt[3]}</td></tr>
      <tr><td>Ngày thi</td><td>{dt[4] or 'N/A'}</td></tr>
      <tr><td>Ngày chấm</td><td>{kq[2]}</td></tr>
    </table>
  </div>
  <div class="diem">
    <div class="diem-so">{kq[0]}</div>
    <div class="diem-chu">({kq[1]})</div>
  </div>
  <div class="footer">
    <p><em>Giảng viên chấm thi</em></p>
    <p style="margin-top:60px;">({session['HoTen']})</p>
  </div>
</div>
</body></html>"""
            self.send_html(html)
            return
        if path == "/baocao":
            return self.send_html(self.page_baocao(session))
        
        # Route Excel phải đứng trước để tránh bị route chung "/baocao/export" chặn
        if path.startswith("/baocao/export-excel"):
            # Export báo cáo năm ra CSV - Phiên bản đẹp và sinh động
            from datetime import datetime
            
            qs = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(qs)
            f_nam = params.get("namHoc",[""])[0]
            if not f_nam:
                self.send_html("<h1>400 Bad Request</h1><p>Thiếu tham số namHoc</p>", 400)
                return
            
            conn = get_db(); cur = conn.cursor()
            deThis = cur.execute(
                "SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon WHERE d.MaGV=? AND d.NamHoc=?",
                (session["MaGV"], f_nam)).fetchall()
            
            # Thu thập dữ liệu chi tiết
            data_rows = []
            for dt in deThis:
                kqs = cur.execute("SELECT DiemSo,DiemChu FROM KET_QUA WHERE MaDT=?", (dt[0],)).fetchall()
                if not kqs: continue
                total = len(kqs)
                counts = {c: sum(1 for k in kqs if k[1]==c) for c in ["A","B+","B","C+","C","D+","D","F"]}
                avg = sum(k[0] for k in kqs)/total
                tl_dao = (total-counts["F"])/total*100 if total else 0
                data_rows.append({
                    "TenMon": dt[1],
                    "HocKy": dt[2],
                    "NamHoc": dt[3],
                    "TongSV": total,
                    "DiemTB": avg,
                    "counts": counts,
                    "TiLeDao": tl_dao
                })
            release_db(conn)
            
            # Tính thống kê tổng quan
            tong_sinh_vien = sum(r["TongSV"] for r in data_rows)
            diem_tb_chung = sum(r["DiemTB"] * r["TongSV"] for r in data_rows) / tong_sinh_vien if tong_sinh_vien > 0 else 0
            tong_A = sum(r["counts"]["A"] for r in data_rows)
            tong_BPlus = sum(r["counts"]["B+"] for r in data_rows)
            tong_B = sum(r["counts"]["B"] for r in data_rows)
            tong_CPlus = sum(r["counts"]["C+"] for r in data_rows)
            tong_C = sum(r["counts"]["C"] for r in data_rows)
            tong_DPlus = sum(r["counts"]["D+"] for r in data_rows)
            tong_D = sum(r["counts"]["D"] for r in data_rows)
            tong_F = sum(r["counts"]["F"] for r in data_rows)
            tong_dau = tong_sinh_vien - tong_F
            ti_le_dau_chung = (tong_dau / tong_sinh_vien * 100) if tong_sinh_vien > 0 else 0
            
            # Xây dựng CSV đẹp mắt
            csv_lines = []
            
            # Header - Tiêu đề báo cáo
            csv_lines.append("╔═══════════════════════════════════════════════════════════════════════════════╗")
            csv_lines.append("║        HỆ THỐNG QUẢN LÝ RA ĐỀ VÀ CHẤM THI - BÁO CÁO THỐNG KÊ              ║")
            csv_lines.append("╚═══════════════════════════════════════════════════════════════════════════════╝")
            csv_lines.append("")
            csv_lines.append(f"📊 Năm học: {f_nam},📅 Ngày xuất: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            csv_lines.append(f"👤 Người xuất: {session.get('TenDangNhap', 'Admin')},🏫 Đơn vị: Trường Đại học Công nghệ Thông tin")
            csv_lines.append("")
            
            # Phần thống kê tổng quan
            csv_lines.append("═══════════════════════════════════════════════════════════════════════════════")
            csv_lines.append("                           📈 THỐNG KÊ TỔNG QUAN")
            csv_lines.append("═══════════════════════════════════════════════════════════════════════════════")
            csv_lines.append(f"Tổng số sinh viên:,{tong_sinh_vien},Điểm TB chung:,{diem_tb_chung:.2f}")
            csv_lines.append(f"Tỉ lệ đậu:,{ti_le_dau_chung:.1f}%,Tỉ lệ rớt:,{(100 - ti_le_dau_chung):.1f}%")
            csv_lines.append("")
            csv_lines.append("Phân bố điểm chữ (tổng):,,,,,,,")
            csv_lines.append(f"A (≥8.5):,{tong_A},B+ (8.0-8.4):,{tong_BPlus},B (7.0-7.9):,{tong_B},C+ (6.5-6.9):,{tong_CPlus}")
            csv_lines.append(f"C (5.5-6.4):,{tong_C},D+ (5.0-5.4):,{tong_DPlus},D (4.0-4.9):,{tong_D},F (<4.0):,{tong_F}")
            csv_lines.append("")
            
            # Phần chi tiết theo môn học
            csv_lines.append("═══════════════════════════════════════════════════════════════════════════════")
            csv_lines.append("                      📚 CHI TIẾT THEO MÔN HỌC VÀ HỌC KỲ")
            csv_lines.append("═══════════════════════════════════════════════════════════════════════════════")
            csv_lines.append("")
            
            # Header bảng chính
            csv_lines.append("STT,Môn học,Học kỳ,Năm học,Tổng SV,Điểm TB,A(≥8.5),B+(8.0),B(7.0),C+(6.5),C(5.5),D+(5.0),D(4.0),F(<4.0),Tỉ lệ đỗ %,Xếp loại")
            csv_lines.append("───,────────,───────,───────,───────,───────,───────,─────,─────,─────,─────,─────,─────,──────,───────────,────────")
            
            # Sắp xếp dữ liệu
            data_rows.sort(key=lambda x: (x["NamHoc"], x["HocKy"], x["TenMon"]))
            
            stt = 1
            for row in data_rows:
                # Xếp loại chất lượng
                if row["TiLeDao"] >= 90 and row["DiemTB"] >= 7.5:
                    xep_loai = "⭐Xuất sắc"
                elif row["TiLeDao"] >= 85 and row["DiemTB"] >= 7.0:
                    xep_loai = "🏆Tốt"
                elif row["TiLeDao"] >= 75 and row["DiemTB"] >= 6.0:
                    xep_loai = "✅Khá"
                elif row["TiLeDao"] >= 60 and row["DiemTB"] >= 5.0:
                    xep_loai = "📝Trung bình"
                else:
                    xep_loai = "⚠️Cần cải thiện"
                
                csv_lines.append(
                    f"{stt},{row['TenMon']},{row['HocKy']},{row['NamHoc']},{row['TongSV']},{row['DiemTB']:.2f},"
                    f"{row['counts']['A']},{row['counts']['B+']},{row['counts']['B']},{row['counts']['C+']},"
                    f"{row['counts']['C']},{row['counts']['D+']},{row['counts']['D']},{row['counts']['F']},"
                    f"{row['TiLeDao']:.1f}%,{xep_loai}"
                )
                stt += 1
            
            # Footer
            csv_lines.append("")
            csv_lines.append("═══════════════════════════════════════════════════════════════════════════════")
            csv_lines.append("📌 CHÚ THÍCH:")
            csv_lines.append("   • A: 8.5-10 | B+: 8.0-8.4 | B: 7.0-7.9 | C+: 6.5-6.9")
            csv_lines.append("   • C: 5.5-6.4 | D+: 5.0-5.4 | D: 4.0-4.9 | F: <4.0 (Không đạt)")
            csv_lines.append("   • Xếp loại dựa trên tỉ lệ đỗ và điểm trung bình")
            csv_lines.append("")
            csv_lines.append(f"💡 Báo cáo được tạo tự động bởi Hệ thống Quản lý Ra đề và Chấm thi v1.0")
            csv_lines.append(f"🔒 Dữ liệu này chỉ dùng cho mục đích thống kê và quản lý nội bộ")
            csv_lines.append("═══════════════════════════════════════════════════════════════════════════════")
            
            # Build CSV với UTF-8 BOM
            csv_content = "\n".join(csv_lines)
            csv_bytes = csv_content.encode("utf-8-sig")  # BOM cho Excel
            
            filename = f"BaoCao_NamHoc_{f_nam}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
            self.send_header("Content-Length", str(len(csv_bytes)))
            self.end_headers()
            self.wfile.write(csv_bytes)
            return
        
        if path.startswith("/baocao/export-html"):
            # Export báo cáo năm ra HTML - Phiên bản đẹp với màu sắc và canh lề
            from datetime import datetime
            
            qs = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(qs)
            f_nam = params.get("namHoc",[""])[0]
            if not f_nam:
                self.send_html("<h1>400 Bad Request</h1><p>Thiếu tham số namHoc</p>", 400)
                return
            
            conn = get_db(); cur = conn.cursor()
            deThis = cur.execute(
                "SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon WHERE d.MaGV=? AND d.NamHoc=?",
                (session["MaGV"], f_nam)).fetchall()
            
            # Thu thập dữ liệu chi tiết
            data_rows = []
            for dt in deThis:
                kqs = cur.execute("SELECT DiemSo,DiemChu FROM KET_QUA WHERE MaDT=?", (dt[0],)).fetchall()
                if not kqs: continue
                total = len(kqs)
                counts = {c: sum(1 for k in kqs if k[1]==c) for c in ["A","B+","B","C+","C","D+","D","F"]}
                avg = sum(k[0] for k in kqs)/total
                tl_dao = (total-counts["F"])/total*100 if total else 0
                data_rows.append({
                    "TenMon": dt[1],
                    "HocKy": dt[2],
                    "NamHoc": dt[3],
                    "TongSV": total,
                    "DiemTB": avg,
                    "counts": counts,
                    "TiLeDao": tl_dao
                })
            release_db(conn)
            
            # Tính thống kê tổng quan
            tong_sinh_vien = sum(r["TongSV"] for r in data_rows)
            diem_tb_chung = sum(r["DiemTB"] * r["TongSV"] for r in data_rows) / tong_sinh_vien if tong_sinh_vien > 0 else 0
            tong_A = sum(r["counts"]["A"] for r in data_rows)
            tong_BPlus = sum(r["counts"]["B+"] for r in data_rows)
            tong_B = sum(r["counts"]["B"] for r in data_rows)
            tong_CPlus = sum(r["counts"]["C+"] for r in data_rows)
            tong_C = sum(r["counts"]["C"] for r in data_rows)
            tong_DPlus = sum(r["counts"]["D+"] for r in data_rows)
            tong_D = sum(r["counts"]["D"] for r in data_rows)
            tong_F = sum(r["counts"]["F"] for r in data_rows)
            tong_dau = tong_sinh_vien - tong_F
            ti_le_dau_chung = (tong_dau / tong_sinh_vien * 100) if tong_sinh_vien > 0 else 0
            
            # Sắp xếp dữ liệu
            data_rows.sort(key=lambda x: (x["NamHoc"], x["HocKy"], x["TenMon"]))
            
            # Xây dựng bảng chi tiết
            detail_rows = ""
            for idx, row in enumerate(data_rows, 1):
                # Xếp loại và màu sắc
                if row["TiLeDao"] >= 90 and row["DiemTB"] >= 7.5:
                    xep_loai = "⭐ Xuất sắc"
                    row_color = "#d4edda"
                elif row["TiLeDao"] >= 85 and row["DiemTB"] >= 7.0:
                    xep_loai = "🏆 Tốt"
                    row_color = "#d1ecf1"
                elif row["TiLeDao"] >= 75 and row["DiemTB"] >= 6.0:
                    xep_loai = "✅ Khá"
                    row_color = "#fff3cd"
                elif row["TiLeDao"] >= 60 and row["DiemTB"] >= 5.0:
                    xep_loai = "📝 Trung bình"
                    row_color = "#f8f9fa"
                else:
                    xep_loai = "⚠️ Cần cải thiện"
                    row_color = "#f8d7da"
                
                detail_rows += f'''
                <tr style="background-color:{row_color};">
                  <td style="text-align:center;">{idx}</td>
                  <td style="text-align:left; padding-left:15px;">{row["TenMon"]}</td>
                  <td style="text-align:center;">{row["HocKy"]}</td>
                  <td style="text-align:center;">{row["NamHoc"]}</td>
                  <td style="text-align:center; font-weight:bold;">{row["TongSV"]}</td>
                  <td style="text-align:center; font-weight:bold; color:#0066cc;">{row["DiemTB"]:.2f}</td>
                  <td style="text-align:center; background-color:#28a745; color:white; font-weight:bold;">{row["counts"]["A"]}</td>
                  <td style="text-align:center; background-color:#5cb85c; color:white;">{row["counts"]["B+"]}</td>
                  <td style="text-align:center; background-color:#7cc97c; color:white;">{row["counts"]["B"]}</td>
                  <td style="text-align:center; background-color:#ffc107; color:white;">{row["counts"]["C+"]}</td>
                  <td style="text-align:center; background-color:#fd7e14; color:white;">{row["counts"]["C"]}</td>
                  <td style="text-align:center; background-color:#ff9800; color:white;">{row["counts"]["D+"]}</td>
                  <td style="text-align:center; background-color:#e57373; color:white;">{row["counts"]["D"]}</td>
                  <td style="text-align:center; background-color:#dc3545; color:white; font-weight:bold;">{row["counts"]["F"]}</td>
                  <td style="text-align:center; font-weight:bold;">{row["TiLeDao"]:.1f}%</td>
                  <td style="text-align:center; font-weight:bold;">{xep_loai}</td>
                </tr>'''
            
            # Tạo HTML với CSS đẹp
            html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Báo cáo Năm học {f_nam}</title>
  <style>
    @media print {{
      .no-print {{ display: none; }}
    }}
    body {{
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 20px;
      background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }}
    .container {{
      max-width: 1400px;
      margin: 0 auto;
      background: white;
      padding: 30px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
      border-radius: 10px;
    }}
    .header {{
      text-align: center;
      border-bottom: 4px solid #007bff;
      padding-bottom: 20px;
      margin-bottom: 30px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 30px;
      border-radius: 8px;
    }}
    .header h1 {{
      margin: 0 0 15px 0;
      font-size: 32px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }}
    .header .meta {{
      display: flex;
      justify-content: space-around;
      margin-top: 20px;
      font-size: 14px;
    }}
    .header .meta div {{
      background: rgba(255,255,255,0.2);
      padding: 10px 20px;
      border-radius: 5px;
    }}
    .section {{
      margin: 30px 0;
      padding: 20px;
      background: #f8f9fa;
      border-left: 5px solid #007bff;
      border-radius: 5px;
    }}
    .section h2 {{
      color: #007bff;
      margin-top: 0;
      font-size: 24px;
    }}
    .stats-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 15px;
      margin: 20px 0;
    }}
    .stat-card {{
      background: white;
      padding: 20px;
      text-align: center;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
      border-top: 4px solid #007bff;
    }}
    .stat-card .label {{
      font-size: 14px;
      color: #666;
      margin-bottom: 10px;
    }}
    .stat-card .value {{
      font-size: 28px;
      font-weight: bold;
      color: #007bff;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    th {{
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 15px 8px;
      text-align: center;
      font-weight: 600;
      font-size: 13px;
      border: 1px solid #dee2e6;
    }}
    td {{
      padding: 12px 8px;
      border: 1px solid #dee2e6;
      font-size: 13px;
    }}
    tr:hover {{
      transform: scale(1.01);
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      transition: all 0.3s ease;
    }}
    .legend {{
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 15px;
      margin: 20px 0;
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      padding: 8px 15px;
      background: white;
      border-radius: 5px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    .legend-color {{
      width: 20px;
      height: 20px;
      margin-right: 8px;
      border-radius: 3px;
    }}
    .footer {{
      margin-top: 40px;
      padding-top: 20px;
      border-top: 2px solid #dee2e6;
      text-align: center;
      color: #666;
      font-size: 13px;
    }}
    .btn-print {{
      background: #28a745;
      color: white;
      padding: 12px 30px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
      margin: 20px 0;
      box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }}
    .btn-print:hover {{
      background: #218838;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>🎓 BÁO CÁO THỐNG KÊ THÀNH TÍCH HỌC TẬP</h1>
      <div style="font-size:20px; margin:10px 0;">Năm học: <strong>{f_nam}</strong></div>
      <div class="meta">
        <div>📅 <strong>Ngày xuất:</strong> {datetime.now().strftime("%d/%m/%Y %H:%M")}</div>
        <div>👤 <strong>Người xuất:</strong> {session.get("TenDangNhap", "Admin")}</div>
        <div>🏫 <strong>Đơn vị:</strong> ĐH Công nghệ Thông tin</div>
      </div>
    </div>
    
    <button class="btn-print no-print" onclick="window.print()">🖨️ In báo cáo</button>
    
    <div class="section">
      <h2>📈 THỐNG KÊ TỔNG QUAN</h2>
      <div class="stats-grid">
        <div class="stat-card">
          <div class="label">Tổng sinh viên</div>
          <div class="value">{tong_sinh_vien}</div>
        </div>
        <div class="stat-card">
          <div class="label">Điểm TB chung</div>
          <div class="value">{diem_tb_chung:.2f}</div>
        </div>
        <div class="stat-card" style="border-top-color: #28a745;">
          <div class="label">Tỉ lệ đậu</div>
          <div class="value" style="color: #28a745;">{ti_le_dau_chung:.1f}%</div>
        </div>
        <div class="stat-card" style="border-top-color: #dc3545;">
          <div class="label">Tỉ lệ rớt</div>
          <div class="value" style="color: #dc3545;">{(100 - ti_le_dau_chung):.1f}%</div>
        </div>
      </div>
      
      <h3 style="text-align:center; margin-top:30px;">Phân bố điểm chữ</h3>
      <div class="stats-grid">
        <div class="stat-card" style="border-top-color: #28a745;"><div class="label">A (≥8.5)</div><div class="value" style="color:#28a745;">{tong_A}</div></div>
        <div class="stat-card" style="border-top-color: #5cb85c;"><div class="label">B+ (8.0-8.4)</div><div class="value" style="color:#5cb85c;">{tong_BPlus}</div></div>
        <div class="stat-card" style="border-top-color: #7cc97c;"><div class="label">B (7.0-7.9)</div><div class="value" style="color:#7cc97c;">{tong_B}</div></div>
        <div class="stat-card" style="border-top-color: #ffc107;"><div class="label">C+ (6.5-6.9)</div><div class="value" style="color:#ffc107;">{tong_CPlus}</div></div>
        <div class="stat-card" style="border-top-color: #fd7e14;"><div class="label">C (5.5-6.4)</div><div class="value" style="color:#fd7e14;">{tong_C}</div></div>
        <div class="stat-card" style="border-top-color: #ff9800;"><div class="label">D+ (5.0-5.4)</div><div class="value" style="color:#ff9800;">{tong_DPlus}</div></div>
        <div class="stat-card" style="border-top-color: #e57373;"><div class="label">D (4.0-4.9)</div><div class="value" style="color:#e57373;">{tong_D}</div></div>
        <div class="stat-card" style="border-top-color: #dc3545;"><div class="label">F (&lt;4.0)</div><div class="value" style="color:#dc3545;">{tong_F}</div></div>
      </div>
    </div>
    
    <div class="section">
      <h2>📚 CHI TIẾT THEO MÔN HỌC VÀ HỌC KỲ</h2>
      <table>
        <thead>
          <tr>
            <th style="width:40px;">STT</th>
            <th style="width:200px;">Môn học</th>
            <th style="width:60px;">HK</th>
            <th style="width:80px;">Năm học</th>
            <th style="width:70px;">Tổng SV</th>
            <th style="width:70px;">Điểm TB</th>
            <th style="width:50px;">A<br>(≥8.5)</th>
            <th style="width:50px;">B+<br>(8.0)</th>
            <th style="width:50px;">B<br>(7.0)</th>
            <th style="width:50px;">C+<br>(6.5)</th>
            <th style="width:50px;">C<br>(5.5)</th>
            <th style="width:50px;">D+<br>(5.0)</th>
            <th style="width:50px;">D<br>(4.0)</th>
            <th style="width:50px;">F<br>(&lt;4.0)</th>
            <th style="width:80px;">Tỉ lệ đỗ</th>
            <th style="width:130px;">Xếp loại</th>
          </tr>
        </thead>
        <tbody>
          {detail_rows}
        </tbody>
      </table>
    </div>
    
    <div class="legend">
      <div class="legend-item"><div class="legend-color" style="background:#d4edda;"></div> ⭐ Xuất sắc</div>
      <div class="legend-item"><div class="legend-color" style="background:#d1ecf1;"></div> 🏆 Tốt</div>
      <div class="legend-item"><div class="legend-color" style="background:#fff3cd;"></div> ✅ Khá</div>
      <div class="legend-item"><div class="legend-color" style="background:#f8f9fa;"></div> 📝 Trung bình</div>
      <div class="legend-item"><div class="legend-color" style="background:#f8d7da;"></div> ⚠️ Cần cải thiện</div>
    </div>
    
    <div class="footer">
      <p>💡 <strong>Báo cáo được tạo tự động bởi Hệ thống Quản lý Ra đề và Chấm thi v1.0</strong></p>
      <p>🔒 Dữ liệu này chỉ dùng cho mục đích thống kê và quản lý nội bộ</p>
      <p style="margin-top:15px; color:#999;">© 2026 Nhóm 15 - SE104.Q23 | Trường Đại học Công nghệ Thông tin</p>
    </div>
  </div>
</body>
</html>'''
            
            filename = f"BaoCao_NamHoc_{f_nam}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            html_bytes = html_content.encode("utf-8")
            
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
            self.send_header("Content-Length", str(len(html_bytes)))
            self.end_headers()
            self.wfile.write(html_bytes)
            return
        
        if path.startswith("/baocao/export-excel"):
            # Export báo cáo dạng Excel Table - HTML format có thể mở bằng Excel
            from datetime import datetime
            
            qs = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(qs)
            f_nam = params.get("namHoc",[""])[0]
            if not f_nam:
                self.send_html("<h1>400 Bad Request</h1><p>Thiếu tham số namHoc</p>", 400)
                return
            
            conn = get_db(); cur = conn.cursor()
            deThis = cur.execute(
                "SELECT d.MaDT,m.TenMon,d.HocKy,d.NamHoc FROM DE_THI d JOIN MON_HOC m ON m.MaMon=d.MaMon WHERE d.MaGV=? AND d.NamHoc=?",
                (session["MaGV"], f_nam)).fetchall()
            
            # Thu thập dữ liệu chi tiết
            data_rows = []
            for dt in deThis:
                kqs = cur.execute("SELECT DiemSo,DiemChu FROM KET_QUA WHERE MaDT=?", (dt[0],)).fetchall()
                if not kqs: continue
                total = len(kqs)
                counts = {c: sum(1 for k in kqs if k[1]==c) for c in ["A","B+","B","C+","C","D+","D","F"]}
                avg = sum(k[0] for k in kqs)/total
                tl_dao = (total-counts["F"])/total*100 if total else 0
                data_rows.append({
                    "TenMon": dt[1],
                    "HocKy": dt[2],
                    "NamHoc": dt[3],
                    "TongSV": total,
                    "DiemTB": avg,
                    "counts": counts,
                    "TiLeDao": tl_dao
                })
            release_db(conn)
            
            # Tính thống kê tổng quan
            tong_sinh_vien = sum(r["TongSV"] for r in data_rows)
            diem_tb_chung = sum(r["DiemTB"] * r["TongSV"] for r in data_rows) / tong_sinh_vien if tong_sinh_vien > 0 else 0
            tong_A = sum(r["counts"]["A"] for r in data_rows)
            tong_BPlus = sum(r["counts"]["B+"] for r in data_rows)
            tong_B = sum(r["counts"]["B"] for r in data_rows)
            tong_CPlus = sum(r["counts"]["C+"] for r in data_rows)
            tong_C = sum(r["counts"]["C"] for r in data_rows)
            tong_DPlus = sum(r["counts"]["D+"] for r in data_rows)
            tong_D = sum(r["counts"]["D"] for r in data_rows)
            tong_F = sum(r["counts"]["F"] for r in data_rows)
            tong_dau = tong_sinh_vien - tong_F
            ti_le_dau_chung = (tong_dau / tong_sinh_vien * 100) if tong_sinh_vien > 0 else 0
            
            # Sắp xếp dữ liệu
            data_rows.sort(key=lambda x: (x["NamHoc"], x["HocKy"], x["TenMon"]))
            
            # Xây dựng bảng chi tiết cho Excel
            detail_rows = ""
            for idx, row in enumerate(data_rows, 1):
                # Xếp loại và màu sắc
                if row["TiLeDao"] >= 90 and row["DiemTB"] >= 7.5:
                    xep_loai = "Xuất sắc"
                    row_bg = "#C6EFCE"
                    row_color = "#006100"
                elif row["TiLeDao"] >= 85 and row["DiemTB"] >= 7.0:
                    xep_loai = "Tốt"
                    row_bg = "#BDD7EE"
                    row_color = "#0066CC"
                elif row["TiLeDao"] >= 75 and row["DiemTB"] >= 6.0:
                    xep_loai = "Khá"
                    row_bg = "#FFF2CC"
                    row_color = "#CC9900"
                elif row["TiLeDao"] >= 60 and row["DiemTB"] >= 5.0:
                    xep_loai = "Trung bình"
                    row_bg = "#F2F2F2"
                    row_color = "#666666"
                else:
                    xep_loai = "Cần cải thiện"
                    row_bg = "#FFC7CE"
                    row_color = "#CC0000"
                
                detail_rows += f'''
    <tr>
      <td style="border: 1px solid #000; text-align: center; background-color: {row_bg}; color: {row_color}; font-weight: bold;">{idx}</td>
      <td style="border: 1px solid #000; padding-left: 10px; background-color: {row_bg}; color: {row_color}; font-weight: bold;">{row["TenMon"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: {row_bg}; color: {row_color};">{row["HocKy"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: {row_bg}; color: {row_color};">{row["NamHoc"]}</td>
      <td style="border: 1px solid #000; text-align: center; font-weight: bold; background-color: {row_bg}; color: {row_color};">{row["TongSV"]}</td>
      <td style="border: 1px solid #000; text-align: center; font-weight: bold; background-color: {row_bg}; color: {row_color};">{row["DiemTB"]:.2f}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: #C6EFCE; color: #006100; font-weight: bold;">{row["counts"]["A"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: #C6EFCE; color: #006100;">{row["counts"]["B+"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: #D9EAD3; color: #38761D;">{row["counts"]["B"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: #FFF2CC; color: #CC9900;">{row["counts"]["C+"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: #FCE5CD; color: #E69138;">{row["counts"]["C"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: #F4CCCC; color: #CC0000;">{row["counts"]["D+"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: #EA9999; color: #990000;">{row["counts"]["D"]}</td>
      <td style="border: 1px solid #000; text-align: center; background-color: #CC0000; color: white; font-weight: bold;">{row["counts"]["F"]}</td>
      <td style="border: 1px solid #000; text-align: center; font-weight: bold; background-color: {row_bg}; color: {row_color};">{row["TiLeDao"]:.1f}%</td>
      <td style="border: 1px solid #000; text-align: center; font-weight: bold; background-color: {row_bg}; color: {row_color};">{xep_loai}</td>
    </tr>'''
            
            # Tạo HTML với format Excel-compatible
            excel_html = f'''<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="ProgId" content="Excel.Sheet">
  <meta name="Generator" content="Microsoft Excel 15">
  <!--[if gte mso 9]><xml>
   <x:ExcelWorkbook>
    <x:ExcelWorksheets>
     <x:ExcelWorksheet>
      <x:Name>Báo cáo {f_nam}</x:Name>
      <x:WorksheetOptions>
       <x:DisplayGridlines/>
       <x:Print>
        <x:ValidPrinterInfo/>
       </x:Print>
      </x:WorksheetOptions>
     </x:ExcelWorksheet>
    </x:ExcelWorksheets>
   </x:ExcelWorkbook>
  </xml><![endif]-->
  <style>
    table {{
      border-collapse: collapse;
      font-family: Calibri, Arial, sans-serif;
      font-size: 11pt;
    }}
    th {{
      border: 2px solid #000;
      background-color: #4472C4;
      color: white;
      font-weight: bold;
      text-align: center;
      padding: 8px;
      font-size: 11pt;
    }}
    td {{
      border: 1px solid #000;
      padding: 5px;
      font-size: 11pt;
    }}
    .header-cell {{
      background-color: #4472C4;
      color: white;
      font-weight: bold;
      font-size: 14pt;
      text-align: center;
      padding: 15px;
      border: 2px solid #000;
    }}
    .section-header {{
      background-color: #305496;
      color: white;
      font-weight: bold;
      font-size: 12pt;
      text-align: center;
      padding: 10px;
      border: 2px solid #000;
    }}
    .label-cell {{
      background-color: #D9E1F2;
      font-weight: bold;
      border: 1px solid #000;
      padding: 5px;
    }}
    .value-cell {{
      text-align: center;
      font-weight: bold;
      border: 1px solid #000;
      padding: 5px;
    }}
  </style>
</head>
<body>
  <table>
    <!-- HEADER -->
    <tr>
      <td colspan="16" class="header-cell">
        BÁO CÁO THỐNG KÊ THÀNH TÍCH HỌC TẬP<br>
        NĂM HỌC: {f_nam}
      </td>
    </tr>
    <tr>
      <td colspan="8" style="border: 1px solid #000; padding: 5px;"><b>Ngày xuất:</b> {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}</td>
      <td colspan="8" style="border: 1px solid #000; padding: 5px;"><b>Người xuất:</b> {session.get("TenDangNhap", "Admin")}</td>
    </tr>
    <tr><td colspan="16" style="height: 10px; border: none;"></td></tr>
    
    <!-- THỐNG KÊ TỔNG QUAN -->
    <tr>
      <td colspan="16" class="section-header">THỐNG KÊ TỔNG QUAN</td>
    </tr>
    <tr>
      <td colspan="4" class="label-cell">Tổng số sinh viên:</td>
      <td colspan="3" class="value-cell" style="background-color: #E7E6E6;">{tong_sinh_vien}</td>
      <td colspan="3" class="label-cell">Điểm TB chung:</td>
      <td colspan="3" class="value-cell" style="background-color: #E7E6E6;">{diem_tb_chung:.2f}</td>
      <td colspan="3" style="border: 1px solid #000;"></td>
    </tr>
    <tr>
      <td colspan="4" class="label-cell">Tỉ lệ đậu:</td>
      <td colspan="3" class="value-cell" style="background-color: #C6EFCE; color: #006100; font-weight: bold;">{ti_le_dau_chung:.1f}%</td>
      <td colspan="3" class="label-cell">Tỉ lệ rớt:</td>
      <td colspan="3" class="value-cell" style="background-color: #FFC7CE; color: #CC0000; font-weight: bold;">{(100 - ti_le_dau_chung):.1f}%</td>
      <td colspan="3" style="border: 1px solid #000;"></td>
    </tr>
    <tr><td colspan="16" style="height: 5px; border: none;"></td></tr>
    
    <!-- PHÂN BỐ ĐIỂM CHỮ -->
    <tr>
      <td colspan="16" class="section-header">PHÂN BỐ ĐIỂM CHỮ</td>
    </tr>
    <tr>
      <td colspan="2" class="label-cell">A (≥8.5)</td>
      <td colspan="2" class="label-cell">B+ (8.0-8.4)</td>
      <td colspan="2" class="label-cell">B (7.0-7.9)</td>
      <td colspan="2" class="label-cell">C+ (6.5-6.9)</td>
      <td colspan="2" class="label-cell">C (5.5-6.4)</td>
      <td colspan="2" class="label-cell">D+ (5.0-5.4)</td>
      <td colspan="2" class="label-cell">D (4.0-4.9)</td>
      <td colspan="2" class="label-cell">F (<4.0)</td>
    </tr>
    <tr>
      <td colspan="2" style="border: 1px solid #000; text-align: center; background-color: #C6EFCE; color: #006100; font-weight: bold; font-size: 14pt;">{tong_A}</td>
      <td colspan="2" style="border: 1px solid #000; text-align: center; background-color: #C6EFCE; color: #006100; font-weight: bold; font-size: 14pt;">{tong_BPlus}</td>
      <td colspan="2" style="border: 1px solid #000; text-align: center; background-color: #D9EAD3; color: #38761D; font-weight: bold; font-size: 14pt;">{tong_B}</td>
      <td colspan="2" style="border: 1px solid #000; text-align: center; background-color: #FFF2CC; color: #CC9900; font-weight: bold; font-size: 14pt;">{tong_CPlus}</td>
      <td colspan="2" style="border: 1px solid #000; text-align: center; background-color: #FCE5CD; color: #E69138; font-weight: bold; font-size: 14pt;">{tong_C}</td>
      <td colspan="2" style="border: 1px solid #000; text-align: center; background-color: #F4CCCC; color: #CC0000; font-weight: bold; font-size: 14pt;">{tong_DPlus}</td>
      <td colspan="2" style="border: 1px solid #000; text-align: center; background-color: #EA9999; color: #990000; font-weight: bold; font-size: 14pt;">{tong_D}</td>
      <td colspan="2" style="border: 1px solid #000; text-align: center; background-color: #CC0000; color: white; font-weight: bold; font-size: 14pt;">{tong_F}</td>
    </tr>
    <tr><td colspan="16" style="height: 10px; border: none;"></td></tr>
    
    <!-- CHI TIẾT THEO MÔN HỌC -->
    <tr>
      <td colspan="16" class="section-header">CHI TIẾT THEO MÔN HỌC VÀ HỌC KỲ</td>
    </tr>
    <tr>
      <th style="width: 40px;">STT</th>
      <th style="width: 200px;">Môn học</th>
      <th style="width: 60px;">HK</th>
      <th style="width: 90px;">Năm học</th>
      <th style="width: 70px;">Tổng SV</th>
      <th style="width: 70px;">Điểm TB</th>
      <th style="width: 60px;">A<br>(≥8.5)</th>
      <th style="width: 60px;">B+<br>(8.0)</th>
      <th style="width: 60px;">B<br>(7.0)</th>
      <th style="width: 60px;">C+<br>(6.5)</th>
      <th style="width: 60px;">C<br>(5.5)</th>
      <th style="width: 60px;">D+<br>(5.0)</th>
      <th style="width: 60px;">D<br>(4.0)</th>
      <th style="width: 60px;">F<br>(<4.0)</th>
      <th style="width: 80px;">Tỉ lệ đỗ</th>
      <th style="width: 120px;">Xếp loại</th>
    </tr>
{detail_rows}
    <tr><td colspan="16" style="height: 10px; border: none;"></td></tr>
    
    <!-- CHÚ THÍCH -->
    <tr>
      <td colspan="16" style="border: 1px solid #000; padding: 10px; background-color: #F2F2F2;">
        <b>CHÚ THÍCH:</b><br>
        • Xếp loại Xuất sắc: Tỉ lệ đỗ ≥90% và Điểm TB ≥7.5<br>
        • Xếp loại Tốt: Tỉ lệ đỗ ≥85% và Điểm TB ≥7.0<br>
        • Xếp loại Khá: Tỉ lệ đỗ ≥75% và Điểm TB ≥6.0<br>
        • Xếp loại Trung bình: Tỉ lệ đỗ ≥60% và Điểm TB ≥5.0<br>
        • Màu sắc: Xanh (tốt) → Vàng (trung bình) → Đỏ (yếu/kém)
      </td>
    </tr>
    <tr>
      <td colspan="16" style="border: 1px solid #000; text-align: center; padding: 5px; background-color: #E7E6E6; font-style: italic;">
        Báo cáo được tạo tự động bởi Hệ thống Quản lý Ra đề và Chấm thi v1.0 | © 2026 Nhóm 15 - SE104.Q23
      </td>
    </tr>
  </table>
</body>
</html>'''
            
            filename = f"BaoCao_NamHoc_{f_nam}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            
            # Thêm UTF-8 BOM để Excel nhận diện đúng
            excel_bytes = ("\ufeff" + excel_html).encode("utf-8")
            
            self.send_response(200)
            self.send_header("Content-Type", "application/vnd.ms-excel")
            self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
            self.send_header("Content-Length", str(len(excel_bytes)))
            self.end_headers()
            self.wfile.write(excel_bytes)
            return
        
        if path == "/thamso":
            return self.send_html(self.page_thamso(session))
        if path.startswith("/thamso/edit/"):
            ten = path.split("/thamso/edit/")[1]
            return self.send_html(self.page_thamso_edit(session, ten))
        if path.startswith("/api/cauhoi"):
            qs = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(qs)
            maMon = params.get("maMon",[""])[0]
            maDK  = params.get("maDoKho",[""])[0]
            conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
            sql = "SELECT c.MaCH,c.NoiDung,dk.TenDoKho,dk.MaDoKho FROM CAU_HOI c JOIN DO_KHO dk ON dk.MaDoKho=c.MaDoKho WHERE c.MaMon=?"
            args = [maMon]
            if maDK: sql += " AND c.MaDoKho=?"; args.append(maDK)
            rows = cur.execute(sql, args).fetchall()
            conn.close()
            data = [{"MaCH":r[0],"NoiDung":r[1],"TenDoKho":r[2],"MaDoKho":r[3]} for r in rows]
            body = json.dumps(data, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type","application/json; charset=utf-8")
            self.send_header("Content-Length",str(len(body)))
            self.end_headers(); self.wfile.write(body); return
        
        if path == "/test":
            # Test page để debug links
            html = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Test</title></head>
<body><h1>Test Links</h1>
<p><a href="/cauhoi?sid=test123">Test Link 1: /cauhoi?sid=test123</a></p>
<p><a href="/dethi/create?sid=test123">Test Link 2: /dethi/create?sid=test123</a></p>
<p><button onclick="location.href='/ketqua?sid=test123'">Test Button: JS redirect</button></p>
<p>Current SID: <span id="sid"></span></p>
<script>
var qs = new URLSearchParams(window.location.search);
document.getElementById('sid').textContent = qs.get('sid') || 'NONE';
</script></body></html>"""
            return self.send_html(html)

        self.send_html("<h1>404 Not Found</h1>", 404)

    def do_POST(self):
        print(f"\n{'='*60}\n[RAW POST] {self.path}\n{'='*60}", flush=True)
        path = urllib.parse.urlparse(self.path).path.rstrip("/")
        self.sid = get_sid(self)
        session = get_session(self)
        form = self.parse_body()
        # Also check sid from POST body if not in URL
        if not self.sid:
            self.sid = self.pv(form, "sid")
            if self.sid and self.sid in SESSIONS:
                session = SESSIONS[self.sid]
        
        # Debug logging
        print(f"[POST] {path} | sid={self.sid[:8] if self.sid else 'None'} | session={'OK' if session else 'NO'}", flush=True)

        if path == "/register":
            hoten = self.pv(form, "hoten").strip()
            username = self.pv(form, "username").strip().lower()
            password = self.pv(form, "password")
            password2 = self.pv(form, "password2")
            email = self.pv(form, "email").strip()
            
            # Validation
            if not hoten or not username or not password:
                return self.send_html(self.page_register("❌ Vui lòng điền đầy đủ thông tin bắt buộc!"))
            if password != password2:
                return self.send_html(self.page_register("❌ Mật khẩu xác nhận không khớp!"))
            if len(password) < 6:
                return self.send_html(self.page_register("❌ Mật khẩu phải có ít nhất 6 ký tự!"))
            if not username.isalnum():
                return self.send_html(self.page_register("❌ Tên đăng nhập chỉ được chứa chữ cái và số!"))
            
            conn = sqlite3.connect(DB_PATH)
            # Kiểm tra trùng username
            exists = conn.execute("SELECT COUNT(*) FROM GIANG_VIEN WHERE TenDangNhap=?", (username,)).fetchone()[0]
            if exists > 0:
                conn.close()
                return self.send_html(self.page_register(f"❌ Tên đăng nhập '{username}' đã tồn tại!"))
            
            # Tạo tài khoản mới
            hashed_pw = sha256(password)
            email_val = email if email else None
            conn.execute("INSERT INTO GIANG_VIEN(HoTen, TenDangNhap, MatKhau, Email) VALUES(?, ?, ?, ?)",
                        (hoten, username, hashed_pw, email_val))
            conn.commit()
            conn.close()
            
            return self.send_html(self.page_register("", f"✅ Đăng ký thành công! Bạn có thể <a href='/login'>đăng nhập</a> với tài khoản <strong>{username}</strong>"))

        if path == "/login":
            username = self.pv(form, "username")
            password = sha256(self.pv(form, "password"))
            conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
            row = cur.execute("SELECT MaGV,HoTen FROM GIANG_VIEN WHERE TenDangNhap=? AND MatKhau=?",
                              (username, password)).fetchone()
            conn.close()
            if not row:
                return self.send_html(self.page_login("❌ Tên đăng nhập hoặc mật khẩu không đúng!"))
            import secrets
            sid = secrets.token_hex(16)
            SESSIONS[sid] = {"MaGV": row[0], "HoTen": row[1]}
            self.sid = sid
            print(f"[LOGIN SUCCESS] Created session {sid[:8]}... for user {row[1]}", flush=True)
            # Set cookie via JavaScript and redirect
            html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<script>
document.cookie = "sid={sid}; path=/; max-age=86400";
console.log("Cookie set:", document.cookie);
setTimeout(function(){{ window.location.href = "/"; }}, 100);
</script>
</head><body>
<p>Đăng nhập thành công! Đang chuyển hướng...</p>
</body></html>"""
            print(f"[LOGIN SUCCESS] Sending HTML with JS cookie set for sid={sid[:8]}...", flush=True)
            return self.send_html(html)

        if not session:
            self.redirect("/login"); return

        if path == "/monhoc/create":
            ten_mon = self.pv(form, "TenMon").strip()
            ma_gv = self.pv(form, "MaGV")
            if not ten_mon:
                flash_msg = alert("❌ Vui lòng nhập tên môn học!", "danger")
                return self.send_html(self.page_monhoc_create(session, flash_msg))
            conn = sqlite3.connect(DB_PATH)
            # Kiểm tra trùng tên
            exists = conn.execute("SELECT COUNT(*) FROM MON_HOC WHERE TenMon=?", (ten_mon,)).fetchone()[0]
            if exists > 0:
                conn.close()
                flash_msg = alert(f"❌ Môn học '{ten_mon}' đã tồn tại!", "danger")
                return self.send_html(self.page_monhoc_create(session, flash_msg))
            ma_gv_val = int(ma_gv) if ma_gv and ma_gv.isdigit() else None
            conn.execute("INSERT INTO MON_HOC(TenMon, MaGV) VALUES(?, ?)", (ten_mon, ma_gv_val))
            conn.commit(); conn.close()
            self.redirect("/monhoc"); return

        if path.startswith("/monhoc/edit/"):
            ma_mon = int(path.split("/")[-1])
            ten_mon = self.pv(form, "TenMon").strip()
            ma_gv = self.pv(form, "MaGV")
            if not ten_mon:
                flash_msg = alert("❌ Vui lòng nhập tên môn học!", "danger")
                return self.send_html(self.page_monhoc_edit(session, ma_mon, flash_msg))
            conn = sqlite3.connect(DB_PATH)
            # Kiểm tra trùng tên (trừ chính nó)
            exists = conn.execute("SELECT COUNT(*) FROM MON_HOC WHERE TenMon=? AND MaMon!=?", (ten_mon, ma_mon)).fetchone()[0]
            if exists > 0:
                conn.close()
                flash_msg = alert(f"❌ Môn học '{ten_mon}' đã tồn tại!", "danger")
                return self.send_html(self.page_monhoc_edit(session, ma_mon, flash_msg))
            ma_gv_val = int(ma_gv) if ma_gv and ma_gv.isdigit() else None
            conn.execute("UPDATE MON_HOC SET TenMon=?, MaGV=? WHERE MaMon=?", (ten_mon, ma_gv_val, ma_mon))
            conn.commit(); conn.close()
            flash_msg = alert(f"✅ Đã cập nhật môn học '{ten_mon}'!", "success")
            if 'db_conn' in session:
                del session['db_conn']
            return self.send_html(self.page_monhoc(session, flash_msg))

        if path == "/sinhvien/create":
            ho_ten = self.pv(form, "HoTen").strip()
            ngay_sinh = self.pv(form, "NgaySinh")
            ma_lop = self.pv(form, "MaLop")
            if not (ho_ten and ngay_sinh and ma_lop):
                flash_msg = alert("❌ Vui lòng điền đầy đủ thông tin!", "danger")
                return self.send_html(self.page_sinhvien_create(session, flash_msg))
            conn = sqlite3.connect(DB_PATH)
            conn.execute("INSERT INTO SINH_VIEN(HoTen, NgaySinh, MaLop) VALUES(?, ?, ?)", 
                        (ho_ten, ngay_sinh, int(ma_lop)))
            conn.commit(); conn.close()
            self.redirect("/sinhvien"); return

        if path.startswith("/sinhvien/edit/"):
            ma_sv = int(path.split("/")[-1])
            ho_ten = self.pv(form, "HoTen").strip()
            ngay_sinh = self.pv(form, "NgaySinh")
            ma_lop = self.pv(form, "MaLop")
            if not (ho_ten and ngay_sinh and ma_lop):
                flash_msg = alert("❌ Vui lòng điền đầy đủ thông tin!", "danger")
                return self.send_html(self.page_sinhvien_edit(session, ma_sv, flash_msg))
            conn = sqlite3.connect(DB_PATH)
            conn.execute("UPDATE SINH_VIEN SET HoTen=?, NgaySinh=?, MaLop=? WHERE MaSV=?", 
                        (ho_ten, ngay_sinh, int(ma_lop), ma_sv))
            conn.commit(); conn.close()
            flash_msg = alert(f"✅ Đã cập nhật sinh viên '{ho_ten}'!", "success")
            if 'db_conn' in session:
                del session['db_conn']
            return self.send_html(self.page_sinhvien(session, flash_msg))

        if path == "/cauhoi/create":
            maMon = self.pv(form,"MaMon")
            maDK  = self.pv(form,"MaDoKho")
            noiDung = self.pv(form,"NoiDung").strip()
            if not (maMon and maDK and noiDung):
                return self.send_html(self.page_cauhoi_create(session,
                    alert("Vui lòng điền đầy đủ thông tin!","danger"),
                    {"mon":maMon,"dk":maDK,"nd":noiDung}))
            conn = sqlite3.connect(DB_PATH)
            conn.execute("INSERT INTO CAU_HOI(NoiDung,MaMon,MaDoKho) VALUES(?,?,?)",
                         (noiDung, maMon, maDK))
            conn.commit(); conn.close()
            self.redirect("/cauhoi"); return

        if path.startswith("/cauhoi/edit/"):
            mach = int(path.split("/")[-1])
            conn = sqlite3.connect(DB_PATH)
            conn.execute("UPDATE CAU_HOI SET NoiDung=?,MaMon=?,MaDoKho=? WHERE MaCH=?",
                         (self.pv(form,"NoiDung"), self.pv(form,"MaMon"), self.pv(form,"MaDoKho"), mach))
            conn.commit(); conn.close()
            self.redirect("/cauhoi"); return

        if path == "/dethi/create":
            maMon = self.pv(form,"MaMon"); hocKy = self.pv(form,"HocKy")
            namHoc = self.pv(form,"NamHoc"); thoiLuong = self.pv(form,"ThoiLuong")
            ngayThi = self.pv(form,"NgayThi") or None
            cauHois = form.get("CauHoi",[])
            # Validate
            tl = int(thoiLuong) if thoiLuong.isdigit() else 0
            conn = sqlite3.connect(DB_PATH); cur = conn.cursor()
            tl_min = cur.execute("SELECT GiaTri FROM THAM_SO WHERE TenThamSo='ThoiLuongToiThieu'").fetchone()[0]
            tl_max = cur.execute("SELECT GiaTri FROM THAM_SO WHERE TenThamSo='ThoiLuongToiDa'").fetchone()[0]
            so_max = cur.execute("SELECT GiaTri FROM THAM_SO WHERE TenThamSo='SoCauToiDa'").fetchone()[0]
            if not (tl_min <= tl <= tl_max):
                conn.close()
                return self.send_html(self.page_dethi_create(session,
                    alert(f"Thời lượng phải từ {tl_min} đến {tl_max} phút!","danger")))
            if len(cauHois) == 0:
                conn.close()
                return self.send_html(self.page_dethi_create(session,
                    alert("Vui lòng chọn ít nhất 1 câu hỏi!","danger")))
            if len(cauHois) > so_max:
                conn.close()
                return self.send_html(self.page_dethi_create(session,
                    alert(f"Mỗi đề thi tối đa {so_max} câu hỏi!","danger")))
            cur.execute("INSERT INTO DE_THI(MaMon,HocKy,NamHoc,ThoiLuong,NgayThi,MaGV) VALUES(?,?,?,?,?,?)",
                        (maMon, hocKy, namHoc, thoiLuong, ngayThi, session["MaGV"]))
            maDT = cur.lastrowid
            for ch in cauHois:
                cur.execute("INSERT OR IGNORE INTO CT_DETHI VALUES(?,?)", (maDT, ch))
            conn.commit(); conn.close()
            self.redirect("/dethi"); return

        if path.startswith("/ketqua/luu/"):
            maDT = int(path.split("/")[-1])
            maSVs = form.get("maSV",[])
            diems = form.get("diemSo",[])
            conn = sqlite3.connect(DB_PATH)
            for i, maSV in enumerate(maSVs):
                if i >= len(diems) or not diems[i].strip(): continue
                try: d = float(diems[i])
                except: continue
                if not 0 <= d <= 10: continue
                dc = get_diem_chu(d)
                existing = conn.execute("SELECT 1 FROM KET_QUA WHERE MaSV=? AND MaDT=?",
                                        (maSV, maDT)).fetchone()
                if existing:
                    conn.execute("UPDATE KET_QUA SET DiemSo=?,DiemChu=?,NgayCham=? WHERE MaSV=? AND MaDT=?",
                                 (d, dc, str(date.today()), maSV, maDT))
                else:
                    conn.execute("INSERT INTO KET_QUA VALUES(?,?,?,?,?)",
                                 (maSV, maDT, d, dc, str(date.today())))
            conn.commit(); conn.close()
            self.redirect(f"/ketqua/nhap/{maDT}"); return

        if path.startswith("/thamso/edit/"):
            ten = path.split("/thamso/edit/")[1]
            gia_tri = self.pv(form,"GiaTri")
            if not gia_tri or not gia_tri.isdigit():
                flash_msg = alert("❌ Giá trị phải là số nguyên!","danger")
                return self.send_html(self.page_thamso_edit(session, ten, flash_msg))
            
            conn = sqlite3.connect(DB_PATH)
            conn.execute("UPDATE THAM_SO SET GiaTri=? WHERE TenThamSo=?", (gia_tri, ten))
            conn.commit(); conn.close()
            
            # Release connection pool để reload data mới
            if 'db_conn' in session:
                del session['db_conn']
            
            # Redirect với thông báo thành công
            flash_msg = alert(f"✅ Đã cập nhật tham số '{ten}' thành {gia_tri}!","success")
            return self.send_html(self.page_thamso(session, flash_msg))

        self.send_html("Not found", 404)


if __name__ == "__main__":
    init_db()
    port = 8080
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"""
╔══════════════════════════════════════════════════════════╗
║   🎓 Quản Lý Ra Đề & Chấm Thi – Nhóm 15 SE104.Q23      ║
╠══════════════════════════════════════════════════════════╣
║   ✅ Server đang chạy tại: http://localhost:{port}          ║
║   🔑 Đăng nhập: gv01 / 123456                           ║
║   🛑 Nhấn Ctrl+C để dừng                                ║
╚══════════════════════════════════════════════════════════╝
""")
    server.serve_forever()
>>>>>>> a546afd41e823ba8c7e40278b493716982ebbd39
