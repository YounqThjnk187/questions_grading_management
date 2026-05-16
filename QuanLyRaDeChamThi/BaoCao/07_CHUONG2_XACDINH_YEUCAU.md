# CHƯƠNG 2: XÁC ĐỊNH YÊU CẦU

## 2.1. Khảo sát hiện trạng

### 2.1.1. Đối tượng khảo sát

Nhóm đã tiến hành khảo sát tại **Trường Đại học Công nghệ Thông tin - ĐHQG TP.HCM**, với các đối tượng sau:

- **5 giảng viên bộ môn Công nghệ Phần mềm** (tuổi 30-50, kinh nghiệm giảng dạy 5-15 năm)
- **Phòng Đào tạo** (1 cán bộ phụ trách quản lý thi cử)
- **Sinh viên** (10 sinh viên năm 2-4, đã trải qua ít nhất 2 kỳ thi)

**Phương pháp khảo sát:**
- Phỏng vấn trực tiếp (1-1.5 giờ/người)
- Quan sát quy trình soạn đề thi thực tế
- Xem mẫu file Word/Excel hiện tại
- Ghi âm (có xin phép) và ghi chép lại

**Thời gian khảo sát:** Từ 05/01/2026 đến 19/01/2026 (2 tuần)

### 2.1.2. Quy trình hiện tại

#### 2.1.2.1. Quy trình soạn câu hỏi

**Bước 1: Tạo file câu hỏi**
- Giảng viên tạo file Word với tên "CauHoi_MonHoc_HocKy.docx"
- Ví dụ: "CauHoi_CNPM_HK1_2025.docx"

**Bước 2: Nhập nội dung câu hỏi**
- Nhập lần lượt: Số thứ tự - Nội dung câu - Đáp án (nếu có) - Điểm số
- Không có trường phân loại độ khó

**Bước 3: Lưu trữ**
- Lưu trên máy tính cá nhân
- Một số giảng viên upload lên Google Drive
- Không có cơ chế backup tập trung

**Vấn đề:**
- ❌ Mất nhiều thời gian tìm lại file cũ (5-10 phút)
- ❌ Dễ thất thoát dữ liệu khi thay đổi máy tính
- ❌ Không phân loại được độ khó (dễ/trung bình/khó)
- ❌ Khó tái sử dụng câu hỏi từ các học kỳ trước

#### 2.1.2.2. Quy trình soạn đề thi

**Bước 1: Mở file câu hỏi**
- Tìm file câu hỏi đã soạn (có thể nhiều file từ nhiều học kỳ)
- Mất 10-15 phút để duyệt qua hàng trăm câu hỏi

**Bước 2: Chọn câu hỏi**
- Copy-paste thủ công từ file câu hỏi sang file đề thi
- Cố gắng chọn cân đối độ khó (dựa vào kinh nghiệm)
- Thường chọn: 30% dễ, 50% trung bình, 20% khó

**Bước 3: Định dạng đề thi**
- Sắp xếp lại thứ tự câu hỏi
- Thêm header (tên trường, môn học, thời gian...)
- Kiểm tra tổng điểm = 10

**Bước 4: Lưu và in**
- Lưu file đề thi
- In ra giấy để nộp cho phòng đào tạo

**Vấn đề:**
- ❌ Mất 2-3 giờ để soạn một đề thi
- ❌ Khó đảm bảo tính ngẫu nhiên (thường chọn câu quen thuộc)
- ❌ Dễ trùng lặp câu hỏi giữa các đề
- ❌ Không có cơ chế kiểm tra ràng buộc (số câu, tổng điểm)

![Hình 2.1: Quy trình soạn đề thi hiện tại](../images/quy_trinh_cu.png)

#### 2.1.2.3. Quy trình chấm thi

**Bước 1: Nhận bài thi**
- Nhận bài thi giấy từ phòng thi
- Sắp xếp theo lớp, theo MSSV

**Bước 2: Chấm điểm**
- Chấm từng bài theo đáp án chuẩn
- Ghi điểm bằng bút đỏ
- Mất ~5-10 phút/bài (nếu 100 bài → 8-16 giờ)

**Bước 3: Nhập điểm vào Excel**
- Tạo file Excel với các cột: MSSV, Họ tên, Điểm số, Điểm chữ
- Nhập thủ công từ bài thi giấy
- Dùng công thức IF lồng nhau để tính điểm chữ

**Bước 4: Nộp điểm**
- Nộp file Excel cho phòng đào tạo
- Nộp bài thi giấy đã chấm (để lưu trữ)

**Vấn đề:**
- ❌ Chấm thủ công tốn rất nhiều thời gian
- ❌ Dễ sai sót khi nhập điểm vào Excel
- ❌ Công thức tính điểm chữ phức tạp, dễ nhầm lẫn
- ❌ Không có cơ chế kiểm tra lỗi nhập liệu (điểm âm, >10...)

#### 2.1.2.4. Quy trình báo cáo

**Bước 1: Tổng hợp dữ liệu**
- Mở tất cả file Excel của các đề thi trong năm
- Copy-paste thủ công sang file báo cáo

**Bước 2: Thống kê**
- Đếm số lượng đề thi theo môn học (thủ công)
- Tính điểm trung bình, tỷ lệ đậu/rớt
- Vẽ biểu đồ trong Excel

**Bước 3: Viết báo cáo**
- Mở Word, nhập số liệu thống kê
- Chèn biểu đồ từ Excel
- Nộp cho trưởng bộ môn

**Vấn đề:**
- ❌ Mất 1-2 ngày để tổng hợp dữ liệu cuối kỳ
- ❌ Dễ sai sót khi copy-paste
- ❌ Không có báo cáo real-time

![Hình 2.2: Quy trình chấm thi và báo cáo hiện tại](../images/quy_trinh_cham_bao_cao.png)

### 2.1.3. Đánh giá hiện trạng

#### 2.1.3.1. Ưu điểm

- ✅ Quy trình đơn giản, không cần đào tạo phức tạp
- ✅ Linh hoạt (giảng viên tự do định dạng câu hỏi)
- ✅ Không phụ thuộc vào phần mềm (chỉ cần Word/Excel)

#### 2.1.3.2. Nhược điểm

| Vấn đề | Mức độ | Ảnh hưởng |
|--------|--------|-----------|
| Tốn thời gian soạn đề | 🔴 Cao | Giảng viên mất 2-3 giờ/đề |
| Chấm điểm thủ công chậm | 🔴 Cao | 8-16 giờ cho 100 bài |
| Dễ sai sót khi nhập liệu | 🟡 Trung bình | 5-10% bài có sai điểm |
| Khó tìm kiếm câu hỏi cũ | 🟡 Trung bình | Mất 5-10 phút mỗi lần |
| Không có backup tập trung | 🔴 Cao | Mất dữ liệu khi hỏng máy |
| Báo cáo cuối kỳ tốn công | 🟡 Trung bình | 1-2 ngày để tổng hợp |
| Không kiểm soát độ khó đề | 🟢 Thấp | Đề thi thiên về dễ hoặc khó |

---

## 2.2. Đề xuất giải pháp

### 2.2.1. Phân tích nguyên nhân

Từ kết quả khảo sát, nhóm xác định nguyên nhân gốc rễ của các vấn đề:

**1. Dữ liệu phân tán:**
- Mỗi giảng viên lưu câu hỏi trên máy riêng
- Không có cơ sở dữ liệu tập trung

**2. Quy trình thủ công:**
- Soạn đề, chấm điểm, báo cáo đều thủ công
- Không có tự động hóa

**3. Thiếu kiểm soát:**
- Không có ràng buộc về số câu, tổng điểm, độ khó
- Không có cơ chế kiểm tra lỗi nhập liệu

**4. Thiếu công cụ hỗ trợ:**
- Word/Excel không được thiết kế cho bài toán này
- Cần một hệ thống chuyên dụng

### 2.2.2. Giải pháp đề xuất

Xây dựng **Hệ thống Quản lý Ra đề và Chấm thi** web-based với các tính năng:

#### 2.2.2.1. Tập trung hóa dữ liệu

- ✅ Lưu tất cả câu hỏi trên CSDL duy nhất
- ✅ Mỗi câu hỏi có phân loại: Môn học, Độ khó, Học kỳ, Năm học
- ✅ Backup tự động hàng ngày

#### 2.2.2.2. Tự động hóa quy trình

- ✅ **Soạn đề nhanh**: Chọn câu hỏi qua giao diện web, tự động tính tổng điểm
- ✅ **Chấm điểm tự động**: Nhập điểm số, hệ thống tự động tính điểm chữ
- ✅ **Báo cáo tức thời**: Click button là có báo cáo, xuất CSV

#### 2.2.2.3. Kiểm soát chất lượng

- ✅ Ràng buộc số câu tối thiểu (ví dụ: ≥5 câu)
- ✅ Kiểm tra tổng điểm = 10
- ✅ Cảnh báo khi môn học có <10 câu hỏi
- ✅ Validation điểm nhập vào (0 ≤ điểm ≤ 10)

#### 2.2.2.4. Giao diện thân thiện

- ✅ Web-based: Truy cập mọi lúc, mọi nơi
- ✅ UI hiện đại: Gradient, animation, card layout
- ✅ Responsive: Hỗ trợ mobile, tablet
- ✅ Tìm kiếm nhanh: Full-text search với highlight

### 2.2.3. So sánh quy trình cũ và mới

**Bảng 2.1: So sánh quy trình cũ và mới**

| Hoạt động | Quy trình cũ | Quy trình mới | Cải thiện |
|-----------|-------------|---------------|-----------|
| **Soạn câu hỏi** | Nhập vào Word, lưu file | Nhập vào form web, lưu CSDL | Tìm kiếm nhanh hơn |
| **Tìm câu hỏi cũ** | 5-10 phút duyệt file | <5 giây tìm kiếm | **95% nhanh hơn** |
| **Soạn đề thi** | 2-3 giờ copy-paste | 15-20 phút chọn câu | **88% nhanh hơn** |
| **Kiểm tra tổng điểm** | Thủ công bằng máy tính | Tự động realtime | **100% chính xác** |
| **Chấm thi** | 8-16 giờ cho 100 bài | 1-2 giờ nhập điểm | **87% nhanh hơn** |
| **Tính điểm chữ** | Dùng công thức Excel | Tự động ngay khi nhập | **100% chính xác** |
| **Báo cáo năm** | 1-2 ngày tổng hợp | <1 phút click button | **99% nhanh hơn** |
| **Xuất báo cáo** | Copy-paste sang Word | Xuất CSV tự động | Chuẩn Excel |

---

## 2.3. Yêu cầu chức năng

Sau khi phân tích hiện trạng và đề xuất giải pháp, nhóm xác định được **8 yêu cầu chức năng** chính:

**Bảng 2.2: Bảng yêu cầu chức năng**

| Mã | Tên yêu cầu | Mô tả ngắn | Mức độ ưu tiên |
|----|-------------|------------|----------------|
| UC01 | Đăng nhập hệ thống | Giảng viên đăng nhập bằng mã GV và mật khẩu | 🔴 Cao |
| UC02 | Soạn câu hỏi | Thêm/Sửa/Xóa câu hỏi, phân loại theo môn học và độ khó | 🔴 Cao |
| UC03 | Soạn đề thi | Tạo đề thi mới, chọn câu hỏi, kiểm tra ràng buộc | 🔴 Cao |
| UC04 | Chấm thi | Nhập điểm số cho sinh viên, tự động tính điểm chữ | 🔴 Cao |
| UC05 | Tra cứu đề thi | Tìm kiếm đề thi theo môn học, học kỳ, năm học | 🟡 Trung bình |
| UC06 | Báo cáo năm | Thống kê số lượng đề thi theo môn học, xuất CSV | 🟡 Trung bình |
| UC07 | Thay đổi tham số | Cập nhật quy định số câu tối thiểu, thời gian thi | 🟢 Thấp |
| UC08 | Tra cứu nhanh | Tìm kiếm full-text câu hỏi theo từ khóa | 🟢 Thấp |

### 2.3.1. UC01 - Đăng nhập hệ thống

**Mô tả:** Giảng viên đăng nhập vào hệ thống bằng mã giảng viên và mật khẩu.

**Input:**
- Mã giảng viên (VD: "gv01")
- Mật khẩu (VD: "123456")

**Output:**
- Thành công: Chuyển đến trang chủ, hiển thị tên giảng viên
- Thất bại: Hiển thị thông báo "Mã GV hoặc mật khẩu không đúng"

**Luồng chính:**
1. Giảng viên mở trang đăng nhập
2. Nhập mã GV và mật khẩu
3. Click nút "Đăng nhập"
4. Hệ thống kiểm tra thông tin
5. Nếu hợp lệ: Tạo session, chuyển đến trang chủ
6. Nếu không hợp lệ: Hiển thị thông báo lỗi

**Luồng thay thế:**
- 4a. Mã GV không tồn tại → Báo lỗi "Mã GV không tồn tại"
- 4b. Mật khẩu sai → Báo lỗi "Mật khẩu không đúng"
- 4c. Để trống trường → Báo lỗi "Vui lòng nhập đầy đủ thông tin"

**Ràng buộc:**
- Mã GV: Không rỗng, tối đa 10 ký tự
- Mật khẩu: Không rỗng, tối thiểu 6 ký tự

### 2.3.2. UC02 - Soạn câu hỏi

**Mô tả:** Giảng viên quản lý ngân hàng câu hỏi (thêm/sửa/xóa/xem danh sách).

**Input (Thêm câu hỏi):**
- Nội dung câu hỏi (text, 10-500 ký tự)
- Mã môn học (dropdown, VD: "SE104")
- Mã độ khó (dropdown, VD: "DK01 - Dễ")

**Output:**
- Thành công: Hiển thị thông báo "Thêm câu hỏi thành công", reload danh sách
- Thất bại: Hiển thị thông báo lỗi cụ thể

**Luồng chính (Thêm):**
1. Giảng viên click "Thêm câu hỏi"
2. Điền form: Nội dung, Môn học, Độ khó
3. Click "Lưu"
4. Hệ thống validate dữ liệu
5. Insert vào bảng CAU_HOI
6. Hiển thị thông báo thành công

**Luồng chính (Sửa):**
1. Giảng viên click "Sửa" trên một câu hỏi
2. Form hiển thị dữ liệu cũ
3. Giảng viên chỉnh sửa
4. Click "Lưu"
5. Hệ thống update bảng CAU_HOI
6. Hiển thị thông báo thành công

**Luồng chính (Xóa):**
1. Giảng viên click "Xóa" trên một câu hỏi
2. Hệ thống hiển thị confirm "Bạn có chắc chắn muốn xóa?"
3. Giảng viên click "OK"
4. Hệ thống kiểm tra ràng buộc (câu hỏi có trong đề thi nào chưa?)
5. Nếu chưa: Delete khỏi bảng CAU_HOI
6. Nếu đã có trong đề: Báo lỗi "Không thể xóa câu hỏi đã có trong đề thi"

**Ràng buộc:**
- Nội dung: 10-500 ký tự
- Môn học: Phải chọn từ danh sách có sẵn
- Độ khó: Phải chọn từ danh sách có sẵn
- Không được xóa câu hỏi đã có trong đề thi

### 2.3.3. UC03 - Soạn đề thi

**Mô tả:** Giảng viên tạo đề thi mới bằng cách chọn các câu hỏi từ ngân hàng.

**Input:**
- Tên đề thi (VD: "Đề thi giữa kỳ CNPM")
- Môn học (dropdown)
- Học kỳ (VD: 1, 2, 3)
- Năm học (VD: 2025, 2026)
- Thời gian thi (VD: 90 phút)
- Danh sách câu hỏi được chọn (checkbox)
- Điểm số cho mỗi câu (number input, 0-10)

**Output:**
- Thành công: Tạo đề thi, hiển thị mã đề (VD: "DT001")
- Thất bại: Hiển thị thông báo lỗi (VD: "Tổng điểm phải = 10")

**Luồng chính:**
1. Giảng viên click "Soạn đề thi"
2. Nhập thông tin đề thi (tên, môn, học kỳ, năm, thời gian)
3. Hệ thống hiển thị danh sách câu hỏi của môn học đó
4. Giảng viên chọn các câu hỏi (checkbox)
5. Nhập điểm số cho mỗi câu
6. Hệ thống tính tổng điểm realtime
7. Click "Lưu đề thi"
8. Hệ thống validate:
   - Số câu ≥ SoCauToiThieu (từ bảng THAM_SO)
   - Tổng điểm = 10
9. Insert vào bảng DE_THI và CT_DETHI
10. Hiển thị thông báo thành công

**Luồng thay thế:**
- 8a. Số câu < SoCauToiThieu → Báo lỗi "Đề thi phải có ít nhất X câu"
- 8b. Tổng điểm ≠ 10 → Báo lỗi "Tổng điểm phải bằng 10"
- 4a. Môn học không có câu hỏi → Báo lỗi "Môn học chưa có câu hỏi nào"

**Ràng buộc:**
- Tên đề: Không rỗng, 5-200 ký tự
- Số câu: ≥ SoCauToiThieu (mặc định 5)
- Tổng điểm: Phải = 10
- Thời gian thi: 15-180 phút

### 2.3.4. UC04 - Chấm thi

**Mô tả:** Giảng viên nhập điểm số cho từng sinh viên, hệ thống tự động tính điểm chữ.

**Input:**
- Chọn đề thi (dropdown)
- Chọn lớp học (dropdown)
- Nhập điểm số cho từng sinh viên (number input, 0-10)

**Output:**
- Hiển thị danh sách sinh viên với điểm số và điểm chữ
- Lưu vào bảng KET_QUA

**Luồng chính:**
1. Giảng viên click "Chấm thi"
2. Chọn đề thi từ dropdown
3. Chọn lớp học từ dropdown
4. Hệ thống hiển thị danh sách sinh viên trong lớp đó
5. Giảng viên nhập điểm số vào từng ô input
6. Hệ thống tự động tính điểm chữ theo bảng BANG_DIEM_CHU
7. Click "Lưu điểm"
8. Hệ thống validate (0 ≤ điểm ≤ 10)
9. Insert/Update vào bảng KET_QUA
10. Hiển thị thông báo thành công

**Luồng thay thế:**
- 8a. Điểm < 0 hoặc > 10 → Báo lỗi "Điểm phải từ 0 đến 10"
- 8b. Điểm không phải số → Báo lỗi "Điểm phải là số"
- 4a. Lớp không có sinh viên → Báo lỗi "Lớp chưa có sinh viên nào"

**Quy tắc tính điểm chữ:**

| Điểm số | Điểm chữ |
|---------|----------|
| 9.0 - 10.0 | A |
| 8.5 - 8.9 | B+ |
| 8.0 - 8.4 | B |
| 7.0 - 7.9 | C+ |
| 6.5 - 6.9 | C |
| 5.5 - 6.4 | D+ |
| 5.0 - 5.4 | D |
| < 5.0 | F |

**Ràng buộc:**
- Điểm số: 0 ≤ điểm ≤ 10, bước nhảy 0.1
- Mỗi sinh viên chỉ có 1 điểm cho 1 đề thi
- Có thể chấm lại (update điểm cũ)

### 2.3.5. UC05 - Tra cứu đề thi

**Mô tả:** Giảng viên tìm kiếm đề thi theo môn học, học kỳ, năm học.

**Input:**
- Môn học (dropdown, có thể bỏ trống = "Tất cả")
- Học kỳ (dropdown, có thể bỏ trống)
- Năm học (dropdown, có thể bỏ trống)

**Output:**
- Danh sách đề thi thỏa mãn điều kiện
- Mỗi dòng hiển thị: Mã đề, Tên đề, Môn học, HK, Năm, Thời gian, Số câu
- Click vào mã đề → Xem chi tiết danh sách câu hỏi

**Luồng chính:**
1. Giảng viên click "Tra cứu đề thi"
2. Chọn tiêu chí tìm kiếm (môn, HK, năm)
3. Click "Tìm kiếm"
4. Hệ thống query bảng DE_THI với điều kiện WHERE
5. Hiển thị danh sách đề thi (dạng bảng)
6. Giảng viên click "Xem chi tiết" trên một đề
7. Hệ thống hiển thị danh sách câu hỏi của đề đó (join CT_DETHI + CAU_HOI)

**Luồng thay thế:**
- 5a. Không tìm thấy đề nào → Hiển thị "Không có đề thi nào"
- 2a. Không chọn tiêu chí → Hiển thị tất cả đề thi

**Ràng buộc:**
- Không có ràng buộc bắt buộc (có thể tìm kiếm tất cả)

### 2.3.6. UC06 - Báo cáo năm

**Mô tả:** Thống kê số lượng đề thi theo từng môn học trong một năm học.

**Input:**
- Năm học (number input, VD: 2025)

**Output:**
- Bảng thống kê: Tên môn học | Số lượng đề thi
- Biểu đồ cột (bar chart) hiển thị số lượng
- Nút "Xuất CSV" để download file

**Luồng chính:**
1. Giảng viên click "Báo cáo năm"
2. Nhập năm học (VD: 2025)
3. Click "Xem báo cáo"
4. Hệ thống gọi stored procedure sp_BaoCaoNam(@Nam)
5. Hiển thị bảng và biểu đồ
6. Giảng viên click "Xuất CSV"
7. Hệ thống tạo file CSV với encoding UTF-8 BOM
8. Download file "BaoCao_Nam2025.csv"

**Luồng thay thế:**
- 5a. Không có đề thi nào trong năm → Hiển thị "Chưa có dữ liệu"

**Ràng buộc:**
- Năm: Số nguyên dương, 2000-2100

### 2.3.7. UC07 - Thay đổi tham số

**Mô tả:** Cập nhật các quy định hệ thống (số câu tối thiểu, thời gian thi).

**Input:**
- Số câu tối thiểu (number input, VD: 5)
- Thời gian thi mặc định (number input, VD: 90 phút)

**Output:**
- Hiển thị thông báo "Cập nhật thành công"

**Luồng chính:**
1. Giảng viên click "Tham số hệ thống"
2. Hệ thống hiển thị giá trị hiện tại (từ bảng THAM_SO)
3. Giảng viên chỉnh sửa
4. Click "Lưu"
5. Hệ thống validate (số câu ≥ 1, thời gian ≥ 15 phút)
6. Update bảng THAM_SO
7. Hiển thị thông báo thành công

**Luồng thay thế:**
- 5a. Số câu < 1 → Báo lỗi "Số câu phải ≥ 1"
- 5b. Thời gian < 15 → Báo lỗi "Thời gian phải ≥ 15 phút"

**Ràng buộc:**
- Số câu: ≥ 1
- Thời gian: 15-180 phút

### 2.3.8. UC08 - Tra cứu nhanh

**Mô tả:** Tìm kiếm câu hỏi theo từ khóa, highlight kết quả.

**Input:**
- Từ khóa (text, VD: "UML")

**Output:**
- Danh sách câu hỏi chứa từ khóa
- Từ khóa được highlight màu vàng

**Luồng chính:**
1. Giảng viên nhập từ khóa vào ô tìm kiếm
2. Click "Tìm"
3. Hệ thống query: `SELECT * FROM CAU_HOI WHERE NoiDung LIKE '%keyword%'`
4. Highlight từ khóa trong kết quả (dùng `<mark>` tag)
5. Hiển thị danh sách câu hỏi

**Luồng thay thế:**
- 4a. Không tìm thấy → Hiển thị "Không có câu hỏi nào"

**Ràng buộc:**
- Từ khóa: Không rỗng, 2-50 ký tự

---

## 2.4. Yêu cầu phi chức năng

**Bảng 2.3: Bảng yêu cầu phi chức năng**

| Loại | Yêu cầu | Mức độ |
|------|---------|--------|
| **Hiệu năng** | Thời gian tải trang < 200ms | 🔴 Cao |
| | Hỗ trợ 50+ người dùng đồng thời | 🟡 Trung bình |
| | Database query < 100ms | 🟡 Trung bình |
| **Bảo mật** | Mã hóa mật khẩu (bcrypt/SHA256) | 🔴 Cao |
| | Ngăn chặn SQL Injection | 🔴 Cao |
| | Session timeout sau 30 phút | 🟡 Trung bình |
| **Khả năng sử dụng** | Giao diện trực quan, dễ học | 🔴 Cao |
| | Responsive (desktop/tablet/mobile) | 🔴 Cao |
| | Thông báo lỗi rõ ràng | 🟡 Trung bình |
| **Độ tin cậy** | Uptime ≥ 99% | 🟡 Trung bình |
| | Backup CSDL hàng ngày | 🟡 Trung bình |
| | Recovery time < 1 giờ | 🟢 Thấp |
| **Khả năng mở rộng** | Hỗ trợ thêm môn học, độ khó dễ dàng | 🟡 Trung bình |
| | Có thể tích hợp API trong tương lai | 🟢 Thấp |
| **Tương thích** | Windows 10/11, Server 2019+ | 🔴 Cao |
| | Chrome, Edge, Firefox (phiên bản mới nhất) | 🔴 Cao |
| | SQL Server 2019+ | 🔴 Cao |

---

**Kết luận chương 2**: Chương này đã trình bày kết quả khảo sát hiện trạng, phân tích vấn đề, đề xuất giải pháp và xác định đầy đủ 8 yêu cầu chức năng cùng các yêu cầu phi chức năng. Chương tiếp theo sẽ phân tích chi tiết các Use Case bằng các biểu đồ UML.

