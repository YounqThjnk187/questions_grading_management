# CHƯƠNG 7: THIẾT KẾ GIAO DIỆN

## 7.1. Nguyên tắc thiết kế giao diện

### 7.1.1. Các nguyên tắc UX/UI

Hệ thống tuân thủ các nguyên tắc thiết kế giao diện người dùng hiện đại:

**1. Đơn giản (Simplicity)**
- Mỗi màn hình chỉ tập trung vào một nhiệm vụ chính
- Loại bỏ các yếu tố không cần thiết
- Sử dụng white space hợp lý

**2. Nhất quán (Consistency)**
- Màu sắc: Gradient tím-hồng (#667eea → #764ba2) xuyên suốt
- Typography: Font Inter 15px, heading 18-24px
- Layout: Navbar cố định trên cùng, sidebar trái, content giữa
- Components: Button, card, form có style giống nhau

**3. Phản hồi nhanh (Feedback)**
- Loading indicator khi xử lý
- Toast notification cho thành công/lỗi
- Validation realtime khi nhập form
- Hover effect trên button và link

**4. Dễ học (Learnability)**
- Navigation rõ ràng với icon + text
- Tooltip giải thích chức năng
- Placeholder hướng dẫn trong input
- Error message cụ thể, không chung chung

**5. Accessibility**
- Contrast ratio ≥ 4.5:1 (WCAG AA)
- Keyboard navigation (Tab, Enter, Esc)
- Focus indicator rõ ràng
- Screen reader friendly (aria-label)

### 7.1.2. Responsive Design

Hệ thống hỗ trợ 3 breakpoint chính:

| Thiết bị | Kích thước | Layout |
|----------|-----------|--------|
| **Desktop** | ≥ 1200px | Navbar + Sidebar + Content (3 cột) |
| **Tablet** | 768px - 1199px | Navbar + Hamburger menu + Content (2 cột) |
| **Mobile** | < 768px | Navbar collapsed + Full-width content (1 cột) |

---

## 7.2. Sơ đồ điều hướng

```
┌─────────────────────────────────────────────────────────────┐
│                      ĐĂNG NHẬP                              │
│                   /login (public)                           │
└──────────────────────┬──────────────────────────────────────┘
                       │ Login thành công
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                     TRANG CHỦ                               │
│                   / (protected)                             │
│                                                             │
│  - Thống kê tổng quan (số câu hỏi, đề thi, điểm TB)        │
│  - Thông báo (cảnh báo môn < 10 câu)                       │
│  - Quick actions (Thêm câu hỏi, Soạn đề)                   │
└────┬──────────┬──────────┬──────────┬──────────┬───────────┘
     │          │          │          │          │
     ▼          ▼          ▼          ▼          ▼
┌─────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌─────────┐
│ CÂU HỎI │ │ ĐỀ THI │ │ KẾT QUẢ│ │ BÁO CÁO│ │ THAM SỐ │
└────┬────┘ └───┬────┘ └───┬────┘ └───┬────┘ └────┬────┘
     │          │          │          │          │
     │          │          │          │          │
┌────▼─────────────┐ ┌────▼──────────────┐ ┌────▼──────────┐
│ /cauhoi          │ │ /dethi            │ │ /ketqua       │
│                  │ │                   │ │               │
│ - Index (DS)     │ │ - Index (DS)      │ │ - Index       │
│ - Create         │ │ - Create          │ │ - NhapDiem    │
│ - Edit/:id       │ │ - Details/:id     │ │               │
│ - Delete/:id     │ │ - TraCuu          │ │               │
│ - Search         │ │                   │ │               │
└──────────────────┘ └───────────────────┘ └───────────────┘

┌────▼──────────────┐ ┌────▼──────────┐
│ /baocao           │ │ /thamso       │
│                   │ │               │
│ - BaoCaoNam       │ │ - Index       │
│ - ExportCSV       │ │ - Edit        │
└───────────────────┘ └───────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      ĐĂNG XUẤT                              │
│                   /logout                                   │
└─────────────────────────────────────────────────────────────┘
```

**Hình 7.1: Sơ đồ điều hướng**

---

## 7.3. Thiết kế màn hình

### 7.3.1. Màn hình Đăng nhập

**Hình 7.2: Màn hình Đăng nhập**

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│                  [Background: Gradient Purple-Pink]           │
│                                                               │
│              ┌─────────────────────────────────┐              │
│              │                                 │              │
│              │      [Logo UIT - 80x80px]       │              │
│              │                                 │              │
│              │   HỆ THỐNG QUẢN LÝ RA ĐỀ       │              │
│              │      VÀ CHẤM THI                │              │
│              │   ─────────────────────────     │              │
│              │                                 │              │
│              │   ┌─────────────────────────┐   │              │
│              │   │ 👤 Mã giảng viên       │   │              │
│              │   │ [gv01_____________]    │   │              │
│              │   └─────────────────────────┘   │              │
│              │                                 │              │
│              │   ┌─────────────────────────┐   │              │
│              │   │ 🔒 Mật khẩu            │   │              │
│              │   │ [********_________]    │   │              │
│              │   └─────────────────────────┘   │              │
│              │                                 │              │
│              │   ┌─────────────────────────┐   │              │
│              │   │    ĐĂNG NHẬP            │   │              │
│              │   └─────────────────────────┘   │              │
│              │       [Button gradient]         │              │
│              │                                 │              │
│              │   Quên mật khẩu? Liên hệ admin  │              │
│              │                                 │              │
│              └─────────────────────────────────┘              │
│                    [Card shadow, rounded]                     │
│                                                               │
│              © 2026 UIT - ĐHQG TP.HCM                         │
└───────────────────────────────────────────────────────────────┘
```

**Thành phần:**
- Background: Gradient từ #667eea (góc trái trên) đến #764ba2 (góc phải dưới)
- Card: Trắng (#fff), border-radius: 16px, box-shadow: 0 10px 40px rgba(0,0,0,0.1)
- Input: Border #ddd, focus: border gradient, height: 45px
- Button: Gradient tím-hồng, hover: transform scale(1.05), text trắng
- Font: Inter, 15px body, 24px heading

### 7.3.2. Màn hình Trang chủ

**Hình 7.3: Màn hình Trang chủ**

```
┌─────────────────────────────────────────────────────────────────────┐
│ [Navbar Fixed Top - Gradient]                                      │
│ 📚 Quản lý Đề thi  |  👤 Nguyễn Văn A  |  🔔 (2)  |  🚪 Đăng xuất  │
└─────────────────────────────────────────────────────────────────────┘
┌────────────┬────────────────────────────────────────────────────────┐
│ [Sidebar]  │                    TRANG CHỦ                           │
│            │                                                        │
│ 🏠 Trang chủ│   ┌──────────────┐ ┌──────────────┐ ┌──────────────┐│
│            │   │ 📝 Câu hỏi   │ │ 📄 Đề thi    │ │ ✅ Đã chấm   ││
│ 📝 Câu hỏi │   │              │ │              │ │              ││
│            │   │     120      │ │      15      │ │      8       ││
│ 📄 Đề thi  │   └──────────────┘ └──────────────┘ └──────────────┘│
│            │                                                        │
│ ✅ Kết quả │   ⚠️ CẢNH BÁO:                                         │
│            │   ┌────────────────────────────────────────────────┐  │
│ 📊 Báo cáo │   │ • Môn SE114 chỉ có 8 câu hỏi (cần ≥10)         │  │
│            │   │ • Có 3 đề thi chưa chấm điểm                   │  │
│ ⚙️ Tham số │   └────────────────────────────────────────────────┘  │
│            │                                                        │
│            │   THAO TÁC NHANH:                                      │
│            │   ┌──────────────┐ ┌──────────────┐                   │
│            │   │ ➕ Thêm câu  │ │ 📝 Soạn đề   │                   │
│            │   │    hỏi       │ │    thi       │                   │
│            │   └──────────────┘ └──────────────┘                   │
│            │                                                        │
│            │   ĐỀ THI GẦN ĐÂY:                                      │
│            │   ┌────────────────────────────────────────────────┐  │
│            │   │ DT001 | Đề giữa kỳ CNPM | SE104 | 01/03/2026  │  │
│            │   │ DT002 | Đề cuối kỳ TKPM | SE113 | 05/05/2026  │  │
│            │   └────────────────────────────────────────────────┘  │
└────────────┴────────────────────────────────────────────────────────┘
```

**Thành phần:**
- Navbar: Height 60px, gradient background, sticky top
- Sidebar: Width 220px, background #f8f9fa, border-right
- Cards: White background, border-radius 8px, shadow
- Icons: Font Awesome hoặc Material Icons
- Stats numbers: Font size 32px, bold, gradient color

### 7.3.3. Màn hình Quản lý câu hỏi

**Hình 7.4: Màn hình Quản lý câu hỏi**

```
┌─────────────────────────────────────────────────────────────────┐
│                     QUẢN LÝ CÂU HỎI                             │
│                                                                 │
│  [🔍 Tìm kiếm_______________________________] [➕ Thêm câu hỏi] │
│                                                                 │
│  Lọc: [Môn học ▼] [Độ khó ▼] [Áp dụng]                        │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ STT │ Nội dung câu hỏi            │ Môn │ Độ khó │ Thao tác││
│  ├─────┼─────────────────────────────┼─────┼────────┼─────────┤│
│  │  1  │ Vẽ use case diagram cho... │SE104│ Trung  │ ✏️ 🗑️  ││
│  │  2  │ Giải thích quy trình RUP... │SE104│ Dễ     │ ✏️ 🗑️  ││
│  │  3  │ Phân tích lớp đối tượng...  │SE113│ Khó    │ ✏️ 🗑️  ││
│  │ ... │ ...                         │ ... │ ...    │ ...     ││
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Hiển thị 1-10 / 120 câu hỏi    [◀️ Trước] [1] [2] [3] [Sau ▶️]│
└─────────────────────────────────────────────────────────────────┘
```

**Modal Thêm/Sửa câu hỏi:**

```
┌─────────────────────────────────────────────────────┐
│  THÊM CÂU HỎI MỚI                          [❌]     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  Nội dung câu hỏi: *                                │
│  ┌─────────────────────────────────────────────┐   │
│  │ Vẽ use case diagram cho hệ thống quản lý    │   │
│  │ thư viện với các actor: Thủ thư, Độc giả    │   │
│  │ ...                                          │   │
│  └─────────────────────────────────────────────┘   │
│  (10-500 ký tự)                                     │
│                                                     │
│  Môn học: *                                         │
│  [SE104 - Nhập môn CNPM ▼]                         │
│                                                     │
│  Độ khó: *                                          │
│  ⚪ Dễ   ⚫ Trung bình   ⚪ Khó   ⚪ Rất khó         │
│                                                     │
│  [Hủy]                               [💾 Lưu]      │
└─────────────────────────────────────────────────────┘
```

### 7.3.4. Màn hình Soạn đề thi

**Hình 7.5: Màn hình Soạn đề thi**

```
┌─────────────────────────────────────────────────────────────────┐
│                      SOẠN ĐỀ THI MỚI                            │
│                                                                 │
│  BƯỚC 1: Thông tin đề thi                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Tên đề thi: * [Đề thi giữa kỳ CNPM________________]     │   │
│  │                                                          │   │
│  │ Môn học: * [SE104 - Nhập môn CNPM ▼]                    │   │
│  │                                                          │   │
│  │ Học kỳ: * [1 ▼]  Năm: * [2026____]  Thời gian: [90] phút│   │
│  │                                                          │   │
│  │                                   [Tiếp theo →]         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  BƯỚC 2: Chọn câu hỏi (sau khi click Tiếp theo)                │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Danh sách câu hỏi môn SE104:                            │   │
│  │                                                          │   │
│  │ ☑️ Vẽ use case diagram... (Trung bình)  Điểm: [2.0]    │   │
│  │ ☑️ Giải thích quy trình RUP... (Dễ)     Điểm: [1.5]    │   │
│  │ ☐ Phân tích yêu cầu phi chức năng... (Khó) [____]      │   │
│  │ ☑️ Vẽ ERD cho hệ thống... (Trung bình) Điểm: [2.5]     │   │
│  │ ...                                                      │   │
│  │                                                          │   │
│  │ Đã chọn: 8 câu  |  Tổng điểm: 10.0 ✅                   │   │
│  │                                                          │   │
│  │ [← Quay lại]                          [💾 Lưu đề thi]  │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

**Tính năng đặc biệt:**
- Realtime tính tổng điểm khi nhập
- Validation: Tổng điểm phải = 10, số câu ≥ min
- Highlight câu hỏi đã chọn màu xanh nhạt
- Progress bar: Bước 1 / Bước 2

### 7.3.5. Màn hình Chấm thi

**Hình 7.6: Màn hình Chấm thi**

```
┌─────────────────────────────────────────────────────────────────┐
│                        CHẤM THI                                 │
│                                                                 │
│  Chọn đề thi: [DT001 - Đề giữa kỳ CNPM ▼]                      │
│  Chọn lớp học: [SE104.Q23 ▼]                    [Xem DS]       │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ STT│ MSSV     │ Họ tên              │ Điểm số │ Điểm chữ ││ │
│  ├───┼──────────┼─────────────────────┼─────────┼──────────┤│ │
│  │ 1 │ 21520001 │ Nguyễn Văn An       │ [8.5__] │ B+       ││ │
│  │ 2 │ 21520002 │ Trần Thị Bình       │ [7.0__] │ C+       ││ │
│  │ 3 │ 21520003 │ Lê Hoàng Cường      │ [9.5__] │ A        ││ │
│  │ 4 │ 21520004 │ Phạm Thị Dung       │ [6.5__] │ C        ││ │
│  │...│ ...      │ ...                 │ ...     │ ...      ││ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Điểm TB: 7.88  |  Cao nhất: 9.5  |  Thấp nhất: 6.5            │
│                                                                 │
│  [🖨️ In phiếu điểm]                          [💾 Lưu điểm]    │
└─────────────────────────────────────────────────────────────────┘
```

**Tính năng:**
- Auto-calculate điểm chữ khi nhập điểm số
- Validation: 0 ≤ điểm ≤ 10
- Tính thống kê realtime (TB, max, min)
- In phiếu điểm: Mở tab mới với layout print-friendly

### 7.3.6. Màn hình Tra cứu đề thi

**Hình 7.7: Màn hình Tra cứu đề thi**

```
┌─────────────────────────────────────────────────────────────────┐
│                      TRA CỨU ĐỀ THI                             │
│                                                                 │
│  Môn học: [Tất cả ▼]  Học kỳ: [Tất cả ▼]  Năm: [2026____]     │
│                                              [🔍 Tìm kiếm]      │
│                                                                 │
│  Kết quả: 15 đề thi                                             │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ Mã đề │ Tên đề thi      │ Môn  │ HK │ Năm │ Số câu│ Thao tác││
│  ├───────┼─────────────────┼──────┼────┼─────┼───────┼───────┤│ │
│  │ DT001 │ Đề giữa kỳ CNPM │ SE104│ 1  │2026 │   8   │ 👁️ ✏️ ││ │
│  │ DT002 │ Đề cuối kỳ CNPM │ SE104│ 1  │2026 │  10   │ 👁️ ✏️ ││ │
│  │ DT003 │ Đề giữa kỳ TKPM │ SE113│ 1  │2026 │   7   │ 👁️ ✏️ ││ │
│  │ ...   │ ...             │ ...  │... │ ... │  ...  │ ...   ││ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│  [◀️ Trước] [1] [2] [3] [Sau ▶️]                                │
└─────────────────────────────────────────────────────────────────┘
```

**Chi tiết đề thi (khi click 👁️):**

```
┌─────────────────────────────────────────────────────────────────┐
│  CHI TIẾT ĐỀ THI: DT001                               [❌]     │
├─────────────────────────────────────────────────────────────────┤
│  Tên đề: Đề thi giữa kỳ CNPM                                    │
│  Môn học: SE104 - Nhập môn Công nghệ phần mềm                   │
│  Học kỳ: 1, Năm: 2026, Thời gian: 90 phút                       │
│  Ngày tạo: 01/03/2026 10:00                                     │
│                                                                 │
│  DANH SÁCH CÂU HỎI:                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Câu 1 (2.0 điểm): Vẽ use case diagram cho hệ thống...  │   │
│  │ Câu 2 (1.5 điểm): Giải thích các bước của RUP...       │   │
│  │ Câu 3 (2.5 điểm): Vẽ ERD cho hệ thống quản lý...       │   │
│  │ ...                                                      │   │
│  │ Tổng: 10.0 điểm                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [🖨️ In đề thi]                                [Đóng]          │
└─────────────────────────────────────────────────────────────────┘
```

### 7.3.7. Màn hình Báo cáo năm

**Hình 7.8: Màn hình Báo cáo năm**

```
┌─────────────────────────────────────────────────────────────────┐
│                       BÁO CÁO NĂM                               │
│                                                                 │
│  Năm học: [2026____]                      [📊 Xem báo cáo]     │
│                                                                 │
│  THỐNG KÊ SỐ LƯỢNG ĐỀ THI THEO MÔN HỌC                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Môn học                              │ Số lượng đề thi  │   │
│  ├──────────────────────────────────────┼──────────────────┤   │
│  │ SE104 - Nhập môn CNPM                │       5          │   │
│  │ SE113 - Thiết kế phần mềm            │       3          │   │
│  │ SE114 - Kiểm thử phần mềm            │       2          │   │
│  │ SE121 - Phân tích yêu cầu            │       3          │   │
│  │ Tổng cộng                            │      13          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  BIỂU ĐỒ:                                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ SE104 ████████████ 5                                    │   │
│  │ SE113 ██████ 3                                          │   │
│  │ SE114 ████ 2                                            │   │
│  │ SE121 ██████ 3                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [📥 Xuất CSV]                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Tính năng:**
- Bar chart với gradient color
- Hover hiển thị số chính xác
- Export CSV với UTF-8 BOM (đọc được trong Excel)

### 7.3.8. Màn hình Tham số hệ thống

**Hình 7.9: Màn hình Tham số hệ thống**

```
┌─────────────────────────────────────────────────────────────────┐
│                    THAM SỐ HỆ THỐNG                             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ QUY ĐỊNH SOẠN ĐỀ THI                                    │   │
│  │                                                          │   │
│  │ Số câu hỏi tối thiểu trong một đề: [5____]              │   │
│  │ (Đề thi phải có ít nhất X câu hỏi)                      │   │
│  │                                                          │   │
│  │ Thời gian thi mặc định: [90___] phút                    │   │
│  │ (Áp dụng khi tạo đề thi mới)                            │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ QUY ĐỊNH CHẤM ĐIỂM                                       │   │
│  │                                                          │   │
│  │ Thang điểm chữ: [Xem chi tiết →]                        │   │
│  │ (A: 9.0-10.0, B+: 8.5-8.9, B: 8.0-8.4...)               │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ CẢNH BÁO                                                 │   │
│  │                                                          │   │
│  │ Số câu hỏi cảnh báo: [10___]                            │   │
│  │ (Cảnh báo khi môn học có < X câu hỏi)                   │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [Hủy]                                         [💾 Lưu thay đổi]│
└─────────────────────────────────────────────────────────────────┘
```

---

## 7.4. Design System

### 7.4.1. Color Palette

**Bảng 7.1: Bảng màu chính (Primary Colors)**

| Màu | Hex | RGB | Sử dụng |
|-----|-----|-----|---------|
| **Purple Primary** | #667eea | rgb(102, 126, 234) | Button, link, highlight |
| **Pink Secondary** | #764ba2 | rgb(118, 75, 162) | Gradient end, accent |
| **Gradient** | linear-gradient(135deg, #667eea 0%, #764ba2 100%) | - | Background, button, navbar |

**Bảng 7.2: Bảng màu phụ (Secondary Colors)**

| Màu | Hex | RGB | Sử dụng |
|-----|-----|-----|---------|
| **Success** | #28a745 | rgb(40, 167, 69) | Thông báo thành công, icon ✅ |
| **Warning** | #ffc107 | rgb(255, 193, 7) | Cảnh báo, icon ⚠️ |
| **Danger** | #dc3545 | rgb(220, 53, 69) | Lỗi, nút xóa, icon ❌ |
| **Info** | #17a2b8 | rgb(23, 162, 184) | Thông tin, tooltip |
| **Light** | #f8f9fa | rgb(248, 249, 250) | Background, card |
| **Dark** | #343a40 | rgb(52, 58, 64) | Text, border |

**Hình 7.10: Color Palette**

### 7.4.2. Typography

**Bảng 7.3: Typography Scale**

| Cấp độ | Font Size | Line Height | Font Weight | Sử dụng |
|--------|-----------|-------------|-------------|---------|
| **H1** | 32px | 40px | 700 (Bold) | Page title |
| **H2** | 24px | 32px | 600 (Semibold) | Section title |
| **H3** | 20px | 28px | 600 (Semibold) | Card title |
| **H4** | 18px | 26px | 600 (Semibold) | Subsection |
| **Body** | 15px | 24px | 400 (Regular) | Paragraph, text |
| **Small** | 13px | 20px | 400 (Regular) | Caption, note |
| **Button** | 15px | 24px | 500 (Medium) | Button text |

**Font family:** 
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 
             'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 
             'Droid Sans', 'Helvetica Neue', sans-serif;
```

**Hình 7.11: Typography System**

### 7.4.3. Components

**Button:**

```css
.btn-primary {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 12px 24px;
    border-radius: 8px;
    border: none;
    font-size: 15px;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
}

.btn-primary:active {
    transform: translateY(0);
}
```

**Card:**

```css
.card {
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    padding: 24px;
    transition: all 0.3s ease;
}

.card:hover {
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
    transform: translateY(-4px);
}
```

**Input:**

```css
.form-control {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 15px;
    transition: all 0.2s ease;
}

.form-control:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}
```

**Table:**

```css
.table {
    width: 100%;
    border-collapse: collapse;
}

.table thead {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.table th {
    padding: 12px 16px;
    font-weight: 600;
    text-align: left;
}

.table td {
    padding: 12px 16px;
    border-bottom: 1px solid #eee;
}

.table tbody tr:hover {
    background: #f8f9fa;
}
```

**Alert:**

```css
.alert-success {
    background: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 16px;
}

.alert-warning {
    background: #fff3cd;
    color: #856404;
    border: 1px solid #ffeeba;
    border-radius: 8px;
    padding: 12px 16px;
}
```

**Hình 7.12: UI Components**

---

**Kết luận chương 7**: Chương này đã thiết kế giao diện người dùng theo phong cách hiện đại, tuân thủ các nguyên tắc UX/UI, responsive 100%, và xây dựng design system đầy đủ (color palette, typography, components). Giao diện trực quan, dễ sử dụng, và nhất quán xuyên suốt hệ thống. Chương tiếp theo sẽ trình bày chi tiết về cài đặt phần mềm.

