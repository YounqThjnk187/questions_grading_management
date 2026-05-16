# CHƯƠNG 3: PHÂN TÍCH YÊU CẦU

## 3.1. Danh sách Actor

**Bảng 3.1: Danh sách Actor**

| Mã Actor | Tên Actor | Mô tả | Trách nhiệm |
|----------|-----------|-------|-------------|
| A01 | Giảng viên | Người sử dụng chính của hệ thống | - Soạn và quản lý câu hỏi<br>- Tạo đề thi<br>- Chấm điểm sinh viên<br>- Tra cứu đề thi<br>- Xem báo cáo thống kê<br>- Thay đổi tham số hệ thống |

**Ghi chú:** Trong phiên bản hiện tại, hệ thống chỉ có 1 loại Actor duy nhất là **Giảng viên**. Trong tương lai có thể mở rộng thêm:
- **Admin**: Quản lý người dùng, phân quyền
- **Trưởng bộ môn**: Xem báo cáo tổng hợp của cả bộ môn
- **Sinh viên**: Xem điểm thi của bản thân

---

## 3.2. Biểu đồ Use Case tổng quát

```
┌────────────────────────────────────────────────────────────────┐
│                  HỆ THỐNG QUẢN LÝ RA ĐỀ VÀ CHẤM THI            │
│                                                                │
│                                                                │
│                ┌─────────────────────────┐                     │
│                │   UC01: Đăng nhập       │                     │
│                └──────────┬──────────────┘                     │
│                           │                                    │
│                           │ <<include>>                        │
│                           ▼                                    │
│  ┌────────────────────────────────────────────────┐            │
│  │         UC02: Soạn câu hỏi                     │            │
│  │                                                │            │
│  │  - Thêm câu hỏi                                │            │
│  │  - Sửa câu hỏi                                 │            │
│  │  - Xóa câu hỏi                                 │            │
│  │  - Xem danh sách                               │            │
│  └─────────────┬──────────────────────────────────┘            │
│                │                                               │
│                │                                               │
│  ┌─────────────▼──────────────────────────────────┐            │
│  │         UC03: Soạn đề thi                      │            │
│  │                                                │            │
│  │  - Tạo đề thi mới                              │            │
│  │  - Chọn câu hỏi                                │            │
│  │  - Gán điểm số                                 │            │
│  └────────────────────────────────────────────────┘            │
│                                                                │
│                                                                │
│  ┌────────────────────────────────────────────────┐            │
│  │         UC04: Chấm thi                         │            │
│  │                                                │            │
│  │  - Chọn đề thi + lớp                           │            │
│  │  - Nhập điểm số                                │            │
│  │  - Tự động tính điểm chữ                       │            │
│  └────────────────────────────────────────────────┘            │
│                                                                │
│                                                                │
│  ┌────────────────────────────────────────────────┐            │
│  │         UC05: Tra cứu đề thi                   │            │
│  │                                                │            │
│  │  - Tìm kiếm theo môn/HK/năm                    │            │
│  │  - Xem chi tiết đề thi                         │            │
│  └────────────────────────────────────────────────┘            │
│                                                                │
│                                                                │
│  ┌────────────────────────────────────────────────┐            │
│  │         UC06: Báo cáo năm                      │            │
│  │                                                │            │
│  │  - Thống kê theo năm                           │            │
│  │  - Xuất CSV                                    │            │
│  │  - Hiển thị biểu đồ                            │            │
│  └────────────────────────────────────────────────┘            │
│                                                                │
│                                                                │
│  ┌────────────────────────────────────────────────┐            │
│  │         UC07: Thay đổi tham số                 │            │
│  │                                                │            │
│  │  - Cập nhật số câu tối thiểu                   │            │
│  │  - Cập nhật thời gian thi                      │            │
│  └────────────────────────────────────────────────┘            │
│                                                                │
│                                                                │
│  ┌────────────────────────────────────────────────┐            │
│  │         UC08: Tra cứu nhanh                    │            │
│  │                                                │            │
│  │  - Tìm kiếm full-text                          │            │
│  │  - Highlight từ khóa                           │            │
│  └────────────────────────────────────────────────┘            │
│                                                                │
└────────────────────────────────────────────────────────────────┘

     Giảng viên ────────────────────────────────────────────────▶
     (Actor)
```

**Hình 3.1: Biểu đồ Use Case tổng quát**

**Giải thích:**
- Tất cả 8 Use Case đều yêu cầu giảng viên phải **đăng nhập** trước (quan hệ `<<include>>`)
- UC02 (Soạn câu hỏi) là tiền đề cho UC03 (Soạn đề thi) - không thể soạn đề nếu chưa có câu hỏi
- UC03 (Soạn đề thi) là tiền đề cho UC04 (Chấm thi) - không thể chấm nếu chưa có đề
- UC05, UC06, UC07, UC08 là các chức năng độc lập, có thể thực hiện bất kỳ lúc nào

---

## 3.3. Đặc tả Use Case chi tiết

### 3.3.1. UC01 - Đăng nhập hệ thống

**Bảng 3.2: Đặc tả Use Case UC01 - Đăng nhập**

| **Thông tin** | **Nội dung** |
|---------------|--------------|
| **Use Case ID** | UC01 |
| **Use Case Name** | Đăng nhập hệ thống |
| **Actor** | Giảng viên |
| **Mục tiêu** | Xác thực danh tính giảng viên để truy cập hệ thống |
| **Tiền điều kiện** | - Giảng viên đã có tài khoản trong CSDL<br>- Truy cập được trang login |
| **Hậu điều kiện** | - Session được tạo<br>- Chuyển đến trang chủ |
| **Tần suất sử dụng** | Cao (mỗi khi mở trình duyệt mới) |

**Luồng sự kiện chính:**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Mở trình duyệt, truy cập http://localhost:8080/login | |
| 2 | | Hiển thị form đăng nhập với 2 trường: Mã GV, Mật khẩu |
| 3 | Nhập mã GV (VD: "gv01") và mật khẩu (VD: "123456") | |
| 4 | Click nút "Đăng nhập" | |
| 5 | | Kiểm tra mã GV có tồn tại trong bảng GIANG_VIEN không |
| 6 | | So sánh mật khẩu đã mã hóa |
| 7 | | Nếu hợp lệ: Tạo session với key = MaGV |
| 8 | | Redirect đến trang chủ (/) |
| 9 | | Hiển thị tên giảng viên trên navbar |

**Luồng sự kiện thay thế:**

**5a. Mã GV không tồn tại:**
1. Hiển thị thông báo lỗi: "Mã giảng viên không tồn tại"
2. Focus vào trường Mã GV
3. Quay lại bước 3

**6a. Mật khẩu sai:**
1. Hiển thị thông báo lỗi: "Mật khẩu không đúng"
2. Clear trường mật khẩu
3. Focus vào trường mật khẩu
4. Quay lại bước 3

**3a. Giảng viên để trống trường:**
1. Hiển thị validation message: "Vui lòng nhập đầy đủ thông tin"
2. Highlight trường bị trống
3. Quay lại bước 3

**Quy tắc nghiệp vụ:**
- BR01: Mật khẩu được mã hóa bằng SHA256 trước khi so sánh
- BR02: Session timeout sau 30 phút không hoạt động
- BR03: Không giới hạn số lần đăng nhập sai (có thể thêm captcha sau)

**Giao diện:**
- Form đăng nhập: Card centered, gradient background, logo UIT phía trên
- Button "Đăng nhập": Màu tím gradient, hover effect
- Thông báo lỗi: Alert đỏ phía trên form

---

### 3.3.2. UC02 - Soạn câu hỏi

**Bảng 3.3: Đặc tả Use Case UC02 - Soạn câu hỏi**

| **Thông tin** | **Nội dung** |
|---------------|--------------|
| **Use Case ID** | UC02 |
| **Use Case Name** | Soạn câu hỏi |
| **Actor** | Giảng viên |
| **Mục tiêu** | Quản lý ngân hàng câu hỏi (Thêm/Sửa/Xóa/Xem) |
| **Tiền điều kiện** | - Giảng viên đã đăng nhập<br>- Có ít nhất 1 môn học trong CSDL |
| **Hậu điều kiện** | - Câu hỏi được lưu vào bảng CAU_HOI<br>- Danh sách câu hỏi được cập nhật |
| **Tần suất sử dụng** | Cao (mỗi khi chuẩn bị thi) |

**Luồng sự kiện chính (Thêm câu hỏi):**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Click menu "Câu hỏi" trên navbar | |
| 2 | | Hiển thị trang danh sách câu hỏi |
| 3 | Click nút "Thêm câu hỏi" | |
| 4 | | Hiển thị form với 3 trường: Nội dung, Môn học (dropdown), Độ khó (dropdown) |
| 5 | Nhập nội dung câu hỏi (VD: "Vẽ use case diagram cho hệ thống quản lý thư viện") | |
| 6 | Chọn môn học (VD: "SE104 - CNPM") | |
| 7 | Chọn độ khó (VD: "DK02 - Trung bình") | |
| 8 | Click nút "Lưu" | |
| 9 | | Validate: Nội dung 10-500 ký tự |
| 10 | | Tạo mã câu hỏi mới (auto-increment) |
| 11 | | INSERT INTO CAU_HOI (MaCauHoi, NoiDung, MaMon, MaDoKho, MaGV) |
| 12 | | Hiển thị thông báo "Thêm câu hỏi thành công" |
| 13 | | Reload danh sách câu hỏi (có câu hỏi mới ở đầu) |

**Luồng sự kiện chính (Sửa câu hỏi):**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Click nút "Sửa" trên một dòng câu hỏi | |
| 2 | | Lấy dữ liệu câu hỏi theo MaCauHoi |
| 3 | | Hiển thị form với dữ liệu cũ đã điền sẵn |
| 4 | Chỉnh sửa nội dung hoặc đổi môn học/độ khó | |
| 5 | Click "Lưu" | |
| 6 | | Validate dữ liệu |
| 7 | | UPDATE CAU_HOI SET ... WHERE MaCauHoi = ? |
| 8 | | Hiển thị "Sửa câu hỏi thành công" |
| 9 | | Reload danh sách |

**Luồng sự kiện chính (Xóa câu hỏi):**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Click nút "Xóa" trên một dòng câu hỏi | |
| 2 | | Hiển thị confirm dialog "Bạn có chắc chắn muốn xóa câu hỏi này?" |
| 3 | Click "OK" | |
| 4 | | Kiểm tra: SELECT COUNT(*) FROM CT_DETHI WHERE MaCauHoi = ? |
| 5 | | Nếu = 0: DELETE FROM CAU_HOI WHERE MaCauHoi = ? |
| 6 | | Hiển thị "Xóa câu hỏi thành công" |
| 7 | | Reload danh sách (câu hỏi đã biến mất) |

**Luồng sự kiện thay thế:**

**9a. Nội dung < 10 ký tự:**
1. Hiển thị "Nội dung phải có ít nhất 10 ký tự"
2. Quay lại bước 5

**9b. Nội dung > 500 ký tự:**
1. Hiển thị "Nội dung không được vượt quá 500 ký tự"
2. Quay lại bước 5

**5a. Câu hỏi đã có trong đề thi:**
1. Hiển thị "Không thể xóa câu hỏi đã có trong đề thi. Vui lòng xóa đề thi trước."
2. Cancel thao tác xóa
3. Quay lại danh sách

**Quy tắc nghiệp vụ:**
- BR04: Mỗi giảng viên chỉ xem được câu hỏi do chính mình tạo (WHERE MaGV = session[MaGV])
- BR05: Không được xóa câu hỏi đã có trong đề thi (foreign key constraint)
- BR06: Nội dung câu hỏi: 10-500 ký tự, cho phép tiếng Việt có dấu

---

### 3.3.3. UC03 - Soạn đề thi

**Bảng 3.4: Đặc tả Use Case UC03 - Soạn đề thi**

| **Thông tin** | **Nội dung** |
|---------------|--------------|
| **Use Case ID** | UC03 |
| **Use Case Name** | Soạn đề thi |
| **Actor** | Giảng viên |
| **Mục tiêu** | Tạo đề thi mới bằng cách chọn câu hỏi từ ngân hàng |
| **Tiền điều kiện** | - Giảng viên đã đăng nhập<br>- Đã có ít nhất 5 câu hỏi cho môn học cần soạn đề |
| **Hậu điều kiện** | - Đề thi được lưu vào bảng DE_THI<br>- Chi tiết câu hỏi được lưu vào CT_DETHI |
| **Tần suất sử dụng** | Trung bình (mỗi học kỳ ~2-3 đề/môn) |

**Luồng sự kiện chính:**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Click menu "Đề thi" → "Soạn đề mới" | |
| 2 | | Hiển thị form với các trường: Tên đề, Môn học, HK, Năm, Thời gian |
| 3 | Nhập: "Đề thi giữa kỳ CNPM", chọn "SE104", HK 1, Năm 2026, 90 phút | |
| 4 | Click "Tiếp theo" | |
| 5 | | Query: SELECT * FROM CAU_HOI WHERE MaMon='SE104' AND MaGV=? |
| 6 | | Hiển thị danh sách câu hỏi dạng bảng (Checkbox, Nội dung, Độ khó, Điểm) |
| 7 | Tick checkbox chọn 8 câu hỏi | |
| 8 | Nhập điểm cho mỗi câu: 1, 1.5, 1, 2, 1.5, 1, 1, 1 | |
| 9 | | Tính tổng điểm realtime: 1+1.5+1+2+1.5+1+1+1 = 10 ✅ |
| 10 | Click "Lưu đề thi" | |
| 11 | | Validate: Số câu ≥ SoCauToiThieu (từ THAM_SO) |
| 12 | | Validate: Tổng điểm = 10 |
| 13 | | Tạo mã đề thi mới (auto-increment, VD: "DT001") |
| 14 | | INSERT INTO DE_THI (MaDT, TenDT, MaMon, HocKy, Nam, ThoiGian, MaGV) |
| 15 | | INSERT INTO CT_DETHI (MaDT, MaCauHoi, DiemSo) cho 8 câu đã chọn |
| 16 | | Hiển thị "Soạn đề thi thành công! Mã đề: DT001" |
| 17 | | Redirect đến trang chi tiết đề thi (xem lại câu hỏi đã chọn) |

**Luồng sự kiện thay thế:**

**11a. Số câu < SoCauToiThieu:**
1. Hiển thị "Đề thi phải có ít nhất X câu (theo quy định)"
2. Highlight trường "Số câu đã chọn: Y" màu đỏ
3. Quay lại bước 7

**12a. Tổng điểm ≠ 10:**
1. Hiển thị "Tổng điểm phải bằng 10. Hiện tại: Z điểm"
2. Highlight trường "Tổng điểm" màu đỏ
3. Quay lại bước 8

**5a. Môn học chưa có câu hỏi:**
1. Hiển thị "Môn học này chưa có câu hỏi nào. Vui lòng soạn câu hỏi trước."
2. Hiển thị button "Đi đến trang soạn câu hỏi"
3. Nếu click: Redirect đến /cauhoi?create=true

**3a. Giảng viên không nhập tên đề:**
1. Hiển thị validation "Tên đề thi không được để trống"
2. Quay lại bước 3

**Quy tắc nghiệp vụ:**
- BR07: Tổng điểm các câu hỏi trong đề thi phải = 10
- BR08: Số câu hỏi ≥ SoCauToiThieu (lấy từ bảng THAM_SO, mặc định 5)
- BR09: Thời gian thi: 15-180 phút
- BR10: Có thể chọn câu hỏi bất kỳ độ khó (không bắt buộc cân đối)
- BR11: Mỗi câu hỏi chỉ xuất hiện 1 lần trong 1 đề

---

### 3.3.4. UC04 - Chấm thi

**Bảng 3.5: Đặc tả Use Case UC04 - Chấm thi**

| **Thông tin** | **Nội dung** |
|---------------|--------------|
| **Use Case ID** | UC04 |
| **Use Case Name** | Chấm thi |
| **Actor** | Giảng viên |
| **Mục tiêu** | Nhập điểm số cho sinh viên, hệ thống tự động tính điểm chữ |
| **Tiền điều kiện** | - Giảng viên đã đăng nhập<br>- Đã có ít nhất 1 đề thi<br>- Đã có ít nhất 1 lớp học với sinh viên |
| **Hậu điều kiện** | - Điểm được lưu vào bảng KET_QUA<br>- Điểm chữ được tính tự động theo BANG_DIEM_CHU |
| **Tần suất sử dụng** | Cao (mỗi kỳ thi) |

**Luồng sự kiện chính:**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Click menu "Kết quả" → "Chấm thi" | |
| 2 | | Hiển thị form: Chọn đề thi (dropdown), Chọn lớp học (dropdown) |
| 3 | Chọn đề: "DT001 - Đề thi giữa kỳ CNPM" | |
| 4 | Chọn lớp: "SE104.Q23" | |
| 5 | Click "Xem danh sách sinh viên" | |
| 6 | | Query: SELECT * FROM SINH_VIEN WHERE MaLop='SE104.Q23' |
| 7 | | Hiển thị bảng: MSSV, Họ tên, Điểm số (input), Điểm chữ (readonly) |
| 8 | | Load điểm cũ (nếu có) từ bảng KET_QUA |
| 9 | Nhập điểm: 21520001 → 8.5, 21520002 → 7.0, 21520003 → 9.5 | |
| 10 | | Sau mỗi lần nhập, tự động tính điểm chữ: |
| | | - 8.5 → B+ (theo BANG_DIEM_CHU) |
| | | - 7.0 → C+ |
| | | - 9.5 → A |
| 11 | Click "Lưu điểm" | |
| 12 | | Validate: 0 ≤ điểm ≤ 10 |
| 13 | | INSERT OR UPDATE vào KET_QUA (MaDT, MaSV, DiemSo, DiemChu) |
| 14 | | Hiển thị "Lưu điểm thành công cho 3 sinh viên" |

**Luồng sự kiện thay thế:**

**12a. Điểm < 0 hoặc > 10:**
1. Hiển thị "Điểm phải từ 0 đến 10"
2. Highlight ô input màu đỏ
3. Quay lại bước 9

**12b. Điểm không phải số:**
1. Hiển thị "Điểm phải là số"
2. Highlight ô input màu đỏ
3. Quay lại bước 9

**6a. Lớp không có sinh viên:**
1. Hiển thị "Lớp này chưa có sinh viên nào"
2. Hiển thị button "Quay lại"
3. Quay lại bước 3

**9a. Giảng viên bỏ qua sinh viên (không nhập điểm):**
1. Giữ nguyên điểm cũ (nếu có)
2. Nếu chưa có điểm cũ: Không insert vào KET_QUA (NULL)

**Quy tắc nghiệp vụ:**
- BR12: Điểm số: 0 ≤ điểm ≤ 10, bước nhảy 0.1
- BR13: Điểm chữ được tính theo bảng BANG_DIEM_CHU:
  - 9.0-10.0 → A
  - 8.5-8.9 → B+
  - 8.0-8.4 → B
  - 7.0-7.9 → C+
  - 6.5-6.9 → C
  - 5.5-6.4 → D+
  - 5.0-5.4 → D
  - <5.0 → F
- BR14: Có thể chấm lại (update điểm cũ)
- BR15: Mỗi sinh viên chỉ có 1 điểm cho 1 đề thi (unique constraint)

---

### 3.3.5. UC05 - Tra cứu đề thi

**Bảng 3.6: Đặc tả Use Case UC05 - Tra cứu đề thi**

| **Thông tin** | **Nội dung** |
|---------------|--------------|
| **Use Case ID** | UC05 |
| **Use Case Name** | Tra cứu đề thi |
| **Actor** | Giảng viên |
| **Mục tiêu** | Tìm kiếm đề thi theo môn học, học kỳ, năm học |
| **Tiền điều kiện** | - Giảng viên đã đăng nhập<br>- Đã có ít nhất 1 đề thi trong CSDL |
| **Hậu điều kiện** | - Hiển thị danh sách đề thi thỏa mãn điều kiện |
| **Tần suất sử dụng** | Trung bình (khi cần xem lại đề thi cũ) |

**Luồng sự kiện chính:**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Click menu "Đề thi" → "Tra cứu" | |
| 2 | | Hiển thị form: Môn học (dropdown, có "Tất cả"), HK (dropdown), Năm (dropdown) |
| 3 | Chọn: Môn "SE104", HK "1", Năm "2026" | |
| 4 | Click "Tìm kiếm" | |
| 5 | | Query: SELECT * FROM DE_THI WHERE MaMon='SE104' AND HocKy=1 AND Nam=2026 AND MaGV=? |
| 6 | | Hiển thị bảng kết quả: Mã đề, Tên đề, Thời gian, Số câu, Ngày tạo, Thao tác |
| 7 | Click "Xem chi tiết" trên đề "DT001" | |
| 8 | | Query: SELECT CH.* FROM CT_DETHI CT JOIN CAU_HOI CH ON CT.MaCauHoi=CH.MaCauHoi WHERE CT.MaDT='DT001' |
| 9 | | Hiển thị: Danh sách câu hỏi (STT, Nội dung, Độ khó, Điểm số) |
| 10 | | Tính tổng điểm: SUM(DiemSo) = 10 |

**Luồng sự kiện thay thế:**

**6a. Không tìm thấy đề thi:**
1. Hiển thị "Không có đề thi nào thỏa mãn điều kiện"
2. Hiển thị button "Tìm kiếm lại"
3. Quay lại bước 3

**3a. Giảng viên chọn "Tất cả" cho Môn học:**
1. Không thêm điều kiện MaMon vào WHERE
2. Hiển thị tất cả đề thi của giảng viên

**3b. Giảng viên không chọn HK và Năm:**
1. Chỉ lọc theo Môn học
2. Hiển thị tất cả đề thi của môn đó (mọi HK, mọi năm)

**Quy tắc nghiệp vụ:**
- BR16: Chỉ hiển thị đề thi do chính giảng viên đó soạn (WHERE MaGV = session[MaGV])
- BR17: Kết quả sắp xếp theo NgayTao DESC (mới nhất lên đầu)

---

### 3.3.6. UC06 - Báo cáo năm

**Bảng 3.7: Đặc tả Use Case UC06 - Báo cáo năm**

| **Thông tin** | **Nội dung** |
|---------------|--------------|
| **Use Case ID** | UC06 |
| **Use Case Name** | Báo cáo năm |
| **Actor** | Giảng viên |
| **Mục tiêu** | Thống kê số lượng đề thi theo môn học trong một năm |
| **Tiền điều kiện** | - Giảng viên đã đăng nhập<br>- Đã có ít nhất 1 đề thi |
| **Hậu điều kiện** | - Hiển thị bảng thống kê + biểu đồ<br>- File CSV được tạo (nếu xuất) |
| **Tần suất sử dụng** | Thấp (cuối năm học) |

**Luồng sự kiện chính:**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Click menu "Báo cáo" → "Báo cáo năm" | |
| 2 | | Hiển thị form: Năm học (number input, default = năm hiện tại) |
| 3 | Nhập: 2026 | |
| 4 | Click "Xem báo cáo" | |
| 5 | | Gọi stored procedure: EXEC sp_BaoCaoNam @Nam=2026 |
| 6 | | Kết quả: TenMon, SoLuongDe |
| 7 | | Hiển thị bảng: SE104 - 5 đề, SE113 - 3 đề, SE114 - 2 đề |
| 8 | | Vẽ biểu đồ cột (bar chart) với JS |
| 9 | Click "Xuất CSV" | |
| 10 | | Tạo file CSV với header: "Môn học,Số lượng đề" |
| 11 | | Ghi từng dòng: "SE104 - CNPM,5" |
| 12 | | Encoding: UTF-8 BOM (để Excel đọc được tiếng Việt) |
| 13 | | Download file: "BaoCao_Nam2026.csv" |

**Luồng sự kiện thay thế:**

**6a. Không có đề thi nào trong năm:**
1. Hiển thị "Chưa có dữ liệu cho năm này"
2. Không hiển thị biểu đồ
3. Disable nút "Xuất CSV"

**Quy tắc nghiệp vụ:**
- BR18: Chỉ thống kê đề thi của giảng viên hiện tại
- BR19: File CSV phải có UTF-8 BOM để Excel đọc đúng tiếng Việt

---

### 3.3.7. UC07 - Thay đổi tham số

**Bảng 3.8: Đặc tả Use Case UC07 - Thay đổi tham số**

| **Thông tin** | **Nội dung** |
|---------------|--------------|
| **Use Case ID** | UC07 |
| **Use Case Name** | Thay đổi tham số |
| **Actor** | Giảng viên |
| **Mục tiêu** | Cập nhật quy định hệ thống (số câu tối thiểu, thời gian thi) |
| **Tiền điều kiện** | - Giảng viên đã đăng nhập |
| **Hậu điều kiện** | - Tham số được cập nhật trong bảng THAM_SO |
| **Tần suất sử dụng** | Rất thấp (1-2 lần/năm) |

**Luồng sự kiện chính:**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Click menu "Tham số" | |
| 2 | | Query: SELECT * FROM THAM_SO WHERE MaThamSo='TS01' |
| 3 | | Hiển thị form với giá trị hiện tại: SoCauToiThieu=5, ThoiGianThiMacDinh=90 |
| 4 | Chỉnh sửa: SoCauToiThieu=7, ThoiGianThiMacDinh=120 | |
| 5 | Click "Lưu" | |
| 6 | | Validate: SoCauToiThieu ≥ 1 |
| 7 | | Validate: ThoiGianThiMacDinh: 15-180 |
| 8 | | UPDATE THAM_SO SET SoCauToiThieu=7, ThoiGianThiMacDinh=120 WHERE MaThamSo='TS01' |
| 9 | | Hiển thị "Cập nhật thành công" |

**Luồng sự kiện thay thế:**

**6a. SoCauToiThieu < 1:**
1. Hiển thị "Số câu phải ≥ 1"
2. Quay lại bước 4

**7a. ThoiGianThiMacDinh < 15 hoặc > 180:**
1. Hiển thị "Thời gian phải từ 15 đến 180 phút"
2. Quay lại bước 4

**Quy tắc nghiệp vụ:**
- BR20: Số câu tối thiểu: ≥ 1
- BR21: Thời gian thi: 15-180 phút

---

### 3.3.8. UC08 - Tra cứu nhanh

**Bảng 3.9: Đặc tả Use Case UC08 - Tra cứu nhanh**

| **Thông tin** | **Nội dung** |
|---------------|--------------|
| **Use Case ID** | UC08 |
| **Use Case Name** | Tra cứu nhanh |
| **Actor** | Giảng viên |
| **Mục tiêu** | Tìm kiếm câu hỏi theo từ khóa, highlight kết quả |
| **Tiền điều kiện** | - Giảng viên đã đăng nhập<br>- Đã có ít nhất 1 câu hỏi |
| **Hậu điều kiện** | - Hiển thị danh sách câu hỏi chứa từ khóa |
| **Tần suất sử dụng** | Cao (mỗi khi cần tìm câu hỏi) |

**Luồng sự kiện chính:**

| Bước | Actor | Hệ thống |
|------|-------|----------|
| 1 | Nhập từ khóa vào ô tìm kiếm trên navbar (VD: "UML") | |
| 2 | Press Enter hoặc click icon search | |
| 3 | | Query: SELECT * FROM CAU_HOI WHERE NoiDung LIKE '%UML%' AND MaGV=? |
| 4 | | Highlight từ "UML" trong kết quả bằng thẻ `<mark>` (màu vàng) |
| 5 | | Hiển thị danh sách: "Vẽ <mark>UML</mark> use case diagram", "Giải thích <mark>UML</mark> activity diagram" |
| 6 | Click vào một câu hỏi | |
| 7 | | Redirect đến trang sửa câu hỏi |

**Luồng sự kiện thay thế:**

**3a. Không tìm thấy câu hỏi:**
1. Hiển thị "Không có câu hỏi nào chứa từ khóa 'UML'"

**1a. Từ khóa < 2 ký tự:**
1. Hiển thị "Từ khóa phải có ít nhất 2 ký tự"

**Quy tắc nghiệp vụ:**
- BR22: Tìm kiếm không phân biệt hoa thường (COLLATE NOCASE trong SQLite)
- BR23: Highlight tất cả các lần xuất hiện của từ khóa

---

## 3.4. Biểu đồ hoạt động (Activity Diagram)

### 3.4.1. Activity Diagram - Đăng nhập

```
[Start]
  |
  v
[Hiển thị form đăng nhập]
  |
  v
<Giảng viên nhập Mã GV và Mật khẩu>
  |
  v
[Kiểm tra Mã GV có tồn tại?]
  |
  +-- (Không) --> [Hiển thị lỗi "Mã GV không tồn tại"] --> [Quay lại form]
  |
  +-- (Có) --> [So sánh mật khẩu]
               |
               +-- (Sai) --> [Hiển thị lỗi "Mật khẩu không đúng"] --> [Quay lại form]
               |
               +-- (Đúng) --> [Tạo session]
                              |
                              v
                             [Redirect đến trang chủ]
                              |
                              v
                             [Hiển thị tên GV trên navbar]
                              |
                              v
                             [End]
```

**Hình 3.2: Activity Diagram - Đăng nhập hệ thống**

### 3.4.2. Activity Diagram - Soạn câu hỏi (Thêm)

```
[Start]
  |
  v
[Click "Thêm câu hỏi"]
  |
  v
[Hiển thị form]
  |
  v
<Giảng viên nhập Nội dung, Môn học, Độ khó>
  |
  v
[Validate: 10 ≤ Nội dung ≤ 500?]
  |
  +-- (Không) --> [Hiển thị lỗi validation] --> [Quay lại form]
  |
  +-- (Có) --> [Tạo mã câu hỏi mới (auto)]
               |
               v
              [INSERT vào CAU_HOI]
               |
               v
              [Hiển thị "Thêm thành công"]
               |
               v
              [Reload danh sách]
               |
               v
              [End]
```

**Hình 3.3: Activity Diagram - Soạn câu hỏi**

### 3.4.3. Activity Diagram - Soạn đề thi

```
[Start]
  |
  v
[Nhập thông tin đề: Tên, Môn, HK, Năm, Thời gian]
  |
  v
[Load danh sách câu hỏi của môn]
  |
  v
<Giảng viên chọn câu hỏi + nhập điểm>
  |
  v
[Tính tổng điểm realtime]
  |
  v
[Kiểm tra: Số câu ≥ SoCauToiThieu?]
  |
  +-- (Không) --> [Hiển thị lỗi "Phải có ít nhất X câu"] --> [Quay lại chọn]
  |
  +-- (Có) --> [Kiểm tra: Tổng điểm = 10?]
               |
               +-- (Không) --> [Hiển thị lỗi "Tổng điểm phải = 10"] --> [Quay lại nhập điểm]
               |
               +-- (Có) --> [INSERT vào DE_THI]
                            |
                            v
                           [INSERT vào CT_DETHI (nhiều dòng)]
                            |
                            v
                           [Hiển thị "Soạn đề thành công"]
                            |
                            v
                           [End]
```

**Hình 3.4: Activity Diagram - Soạn đề thi**

### 3.4.4. Activity Diagram - Chấm thi

```
[Start]
  |
  v
[Chọn Đề thi + Lớp học]
  |
  v
[Load danh sách sinh viên]
  |
  v
[Load điểm cũ (nếu có) từ KET_QUA]
  |
  v
<Giảng viên nhập điểm số>
  |
  v
[Tự động tính điểm chữ theo BANG_DIEM_CHU]
  |
  v
[Validate: 0 ≤ điểm ≤ 10?]
  |
  +-- (Không) --> [Hiển thị lỗi] --> [Quay lại nhập]
  |
  +-- (Có) --> [INSERT/UPDATE vào KET_QUA]
               |
               v
              [Hiển thị "Lưu điểm thành công"]
               |
               v
              [End]
```

**Hình 3.5: Activity Diagram - Chấm thi**

---

**Kết luận chương 3**: Chương này đã phân tích chi tiết 8 Use Case với đầy đủ: Actor, luồng sự kiện chính/thay thế, ràng buộc, quy tắc nghiệp vụ. Activity diagram minh họa rõ ràng luồng xử lý của từng chức năng. Chương tiếp theo sẽ thiết kế kiến trúc hệ thống theo mô hình 3 lớp và MVC.

