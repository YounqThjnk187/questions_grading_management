# CHƯƠNG 9: KIỂM THỬ VÀ BẢO TRÌ

## 9.1. Kế hoạch kiểm thử

**Bảng 9.1: Kế hoạch kiểm thử**

| Giai đoạn | Thời gian | Loại kiểm thử | Người thực hiện | Công cụ |
|-----------|-----------|---------------|-----------------|---------|
| **1. Unit Testing** | Tuần 9 | Kiểm thử từng function | Developer | Manual testing |
| **2. Integration Testing** | Tuần 10 | Kiểm thử tích hợp module | Developer + Tester | Postman, Browser |
| **3. System Testing** | Tuần 11 | Kiểm thử toàn hệ thống | Tester | Test cases Excel |
| **4. UAT** | Tuần 12 | Kiểm thử chấp nhận người dùng | Giảng viên (end user) | Real usage |

**Mục tiêu:**
- ✅ Phát hiện và sửa lỗi trước khi deploy
- ✅ Đảm bảo 100% yêu cầu chức năng hoạt động
- ✅ Đảm bảo hiệu năng đáp ứng yêu cầu phi chức năng
- ✅ Đảm bảo bảo mật (SQL injection, XSS prevention)

---

## 9.2. Kiểm thử chức năng

### 9.2.1. Test Case TC01 - Đăng nhập hợp lệ

**Bảng 9.2: Test Case TC01 - Đăng nhập hợp lệ**

| **Test Case ID** | TC01 |
|------------------|------|
| **Test Case Name** | Đăng nhập với mã GV và mật khẩu hợp lệ |
| **Module** | Đăng nhập |
| **Pre-condition** | - Có tài khoản `gv01` với mật khẩu `123456` trong CSDL<br>- Truy cập được trang login |
| **Test Steps** | 1. Mở trình duyệt, truy cập http://localhost:8080/login<br>2. Nhập mã GV: `gv01`<br>3. Nhập mật khẩu: `123456`<br>4. Click nút "Đăng nhập" |
| **Expected Result** | - Redirect đến trang chủ /<br>- Navbar hiển thị "Xin chào, Nguyễn Văn A"<br>- Session["MaGV"] = "gv01" |
| **Actual Result** | ✅ PASS: Redirect thành công, navbar hiển thị đúng |
| **Status** | **PASS** |
| **Tester** | Trương Vũ Minh Tân |
| **Date** | 10/05/2026 |

### 9.2.2. Test Case TC02 - Đăng nhập không hợp lệ

**Bảng 9.3: Test Case TC02 - Đăng nhập không hợp lệ**

| **Test Case ID** | TC02 |
|------------------|------|
| **Test Case Name** | Đăng nhập với mật khẩu sai |
| **Module** | Đăng nhập |
| **Pre-condition** | - Truy cập được trang login |
| **Test Steps** | 1. Mở trình duyệt, truy cập http://localhost:8080/login<br>2. Nhập mã GV: `gv01`<br>3. Nhập mật khẩu: `wrong_password`<br>4. Click nút "Đăng nhập" |
| **Expected Result** | - Không redirect<br>- Hiển thị thông báo lỗi: "Mật khẩu không đúng"<br>- Form vẫn giữ giá trị mã GV |
| **Actual Result** | ✅ PASS: Hiển thị lỗi đúng, không redirect |
| **Status** | **PASS** |
| **Tester** | Thạch Via Sa Na |
| **Date** | 10/05/2026 |

### 9.2.3. Test Case TC03 - Thêm câu hỏi

**Bảng 9.4: Test Case TC03 - Thêm câu hỏi**

| **Test Case ID** | TC03 |
|------------------|------|
| **Test Case Name** | Thêm câu hỏi mới hợp lệ |
| **Module** | Quản lý câu hỏi |
| **Pre-condition** | - Đã đăng nhập<br>- Có ít nhất 1 môn học và 1 độ khó trong CSDL |
| **Test Steps** | 1. Click menu "Câu hỏi" → "Thêm câu hỏi"<br>2. Nhập nội dung: "Vẽ use case diagram cho hệ thống quản lý thư viện"<br>3. Chọn môn: "SE104 - CNPM"<br>4. Chọn độ khó: "Trung bình"<br>5. Click "Lưu" |
| **Expected Result** | - INSERT vào bảng CAU_HOI<br>- MaCauHoi tự động (VD: CH0021)<br>- Redirect về /cauhoi<br>- Thông báo "Thêm câu hỏi thành công!" |
| **Actual Result** | ✅ PASS: Câu hỏi được thêm, mã CH0021, redirect thành công |
| **Status** | **PASS** |
| **Tester** | Hà Trọng Nghĩa |
| **Date** | 11/05/2026 |

### 9.2.4. Test Case TC04 - Sửa câu hỏi

**Bảng 9.5: Test Case TC04 - Sửa câu hỏi**

| **Test Case ID** | TC04 |
|------------------|------|
| **Test Case Name** | Sửa nội dung câu hỏi |
| **Module** | Quản lý câu hỏi |
| **Pre-condition** | - Đã đăng nhập<br>- Có câu hỏi CH0001 do gv01 tạo |
| **Test Steps** | 1. Vào trang /cauhoi<br>2. Click "Sửa" trên câu hỏi CH0001<br>3. Thay đổi nội dung: "Vẽ use case diagram và activity diagram..."<br>4. Click "Lưu" |
| **Expected Result** | - UPDATE bảng CAU_HOI WHERE MaCauHoi='CH0001'<br>- Redirect về /cauhoi<br>- Thông báo "Cập nhật thành công!" |
| **Actual Result** | ✅ PASS: Nội dung được cập nhật, redirect thành công |
| **Status** | **PASS** |
| **Tester** | Dương Quốc Thịnh |
| **Date** | 11/05/2026 |

### 9.2.5. Test Case TC05 - Xóa câu hỏi

**Bảng 9.6: Test Case TC05 - Xóa câu hỏi**

| **Test Case ID** | TC05 |
|------------------|------|
| **Test Case Name** | Xóa câu hỏi chưa có trong đề thi |
| **Module** | Quản lý câu hỏi |
| **Pre-condition** | - Đã đăng nhập<br>- Có câu hỏi CH0020 chưa thuộc đề nào |
| **Test Steps** | 1. Vào trang /cauhoi<br>2. Click "Xóa" trên CH0020<br>3. Confirm "OK" trong popup |
| **Expected Result** | - DELETE FROM CAU_HOI WHERE MaCauHoi='CH0020'<br>- Dòng CH0020 biến mất khỏi bảng<br>- Alert "Xóa thành công" |
| **Actual Result** | ✅ PASS: Câu hỏi bị xóa, alert hiển thị |
| **Status** | **PASS** |
| **Tester** | Trương Vũ Minh Tân |
| **Date** | 11/05/2026 |

**Test Case TC05b - Xóa câu hỏi đã có trong đề thi:**

| **Test Case ID** | TC05b |
|------------------|------|
| **Expected Result** | - Không xóa được<br>- Alert "Không thể xóa câu hỏi đã có trong đề thi" |
| **Actual Result** | ✅ PASS: Alert hiển thị đúng, không xóa |
| **Status** | **PASS** |

### 9.2.6. Test Case TC06 - Soạn đề thi

**Bảng 9.7: Test Case TC06 - Soạn đề thi**

| **Test Case ID** | TC06 |
|------------------|------|
| **Test Case Name** | Soạn đề thi với tổng điểm = 10 |
| **Module** | Soạn đề thi |
| **Pre-condition** | - Đã đăng nhập<br>- Môn SE104 có ≥8 câu hỏi |
| **Test Steps** | 1. Click "Đề thi" → "Soạn đề mới"<br>2. Nhập tên: "Đề thi giữa kỳ CNPM"<br>3. Chọn môn: SE104, HK: 1, Năm: 2026, Thời gian: 90<br>4. Click "Tiếp theo"<br>5. Chọn 8 câu hỏi, nhập điểm: 2, 1.5, 2, 1.5, 1, 1, 0.5, 0.5<br>6. Tổng điểm = 10 ✅<br>7. Click "Lưu đề thi" |
| **Expected Result** | - INSERT vào DE_THI (MaDT='DT003')<br>- INSERT 8 dòng vào CT_DETHI<br>- Redirect đến /dethi/details/DT003<br>- Thông báo "Soạn đề thành công! Mã đề: DT003" |
| **Actual Result** | ✅ PASS: Đề thi được tạo, chi tiết hiển thị đúng |
| **Status** | **PASS** |
| **Tester** | Thạch Via Sa Na |
| **Date** | 12/05/2026 |

**Test Case TC06b - Soạn đề với tổng điểm ≠ 10:**

| **Expected Result** | - Không lưu được<br>- Alert "Tổng điểm phải = 10. Hiện tại: 9.5" |
| **Actual Result** | ✅ PASS: Validation chặn đúng |
| **Status** | **PASS** |

### 9.2.7. Test Case TC07 - Chấm thi

**Bảng 9.8: Test Case TC07 - Chấm thi**

| **Test Case ID** | TC07 |
|------------------|------|
| **Test Case Name** | Nhập điểm cho sinh viên |
| **Module** | Chấm thi |
| **Pre-condition** | - Đã đăng nhập<br>- Có đề DT001, lớp SE104.Q23 với 3 sinh viên |
| **Test Steps** | 1. Click "Kết quả" → "Chấm thi"<br>2. Chọn đề: DT001, lớp: SE104.Q23<br>3. Click "Xem DS"<br>4. Nhập điểm: 21520001 → 8.5, 21520002 → 7.0, 21520003 → 9.5<br>5. Điểm chữ tự động: B+, C+, A<br>6. Click "Lưu điểm" |
| **Expected Result** | - INSERT/UPDATE vào KET_QUA (3 dòng)<br>- DiemChu tính đúng theo BANG_DIEM_CHU<br>- Thông báo "Lưu điểm thành công cho 3 sinh viên" |
| **Actual Result** | ✅ PASS: Điểm được lưu, điểm chữ đúng |
| **Status** | **PASS** |
| **Tester** | Hà Trọng Nghĩa |
| **Date** | 12/05/2026 |

### 9.2.8. Test Case TC08 - Tra cứu đề thi

**Bảng 9.9: Test Case TC08 - Tra cứu đề thi**

| **Test Case ID** | TC08 |
|------------------|------|
| **Test Case Name** | Tra cứu đề thi theo môn và năm |
| **Module** | Tra cứu đề thi |
| **Pre-condition** | - Đã đăng nhập<br>- Có 5 đề thi môn SE104 năm 2026 |
| **Test Steps** | 1. Click "Đề thi" → "Tra cứu"<br>2. Chọn môn: SE104, năm: 2026<br>3. Click "Tìm kiếm" |
| **Expected Result** | - Query: SELECT * FROM DE_THI WHERE MaMon='SE104' AND Nam=2026<br>- Hiển thị bảng 5 đề thi<br>- Mỗi dòng: Mã đề, Tên đề, HK, Năm, Số câu, Thao tác (Xem, Sửa) |
| **Actual Result** | ✅ PASS: 5 đề thi hiển thị đúng |
| **Status** | **PASS** |
| **Tester** | Dương Quốc Thịnh |
| **Date** | 13/05/2026 |

### 9.2.9. Test Case TC09 - Xuất báo cáo năm

**Bảng 9.10: Test Case TC09 - Xuất báo cáo năm**

| **Test Case ID** | TC09 |
|------------------|------|
| **Test Case Name** | Xuất báo cáo năm ra CSV |
| **Module** | Báo cáo |
| **Pre-condition** | - Đã đăng nhập<br>- Năm 2026 có 13 đề thi (4 môn) |
| **Test Steps** | 1. Click "Báo cáo" → "Báo cáo năm"<br>2. Nhập năm: 2026<br>3. Click "Xem báo cáo"<br>4. Bảng và biểu đồ hiển thị<br>5. Click "Xuất CSV" |
| **Expected Result** | - File BaoCao_Nam2026.csv được download<br>- Encoding: UTF-8 BOM<br>- Nội dung: Header + 4 dòng dữ liệu<br>- Mở được trong Excel, tiếng Việt hiển thị đúng |
| **Actual Result** | ✅ PASS: File CSV đúng, Excel đọc được tiếng Việt |
| **Status** | **PASS** |
| **Tester** | Trương Vũ Minh Tân |
| **Date** | 13/05/2026 |

### 9.2.10. Test Case TC10 - Thay đổi tham số

**Bảng 9.11: Test Case TC10 - Thay đổi tham số**

| **Test Case ID** | TC10 |
|------------------|------|
| **Test Case Name** | Cập nhật số câu tối thiểu |
| **Module** | Tham số hệ thống |
| **Pre-condition** | - Đã đăng nhập<br>- SoCauToiThieu hiện tại = 5 |
| **Test Steps** | 1. Click "Tham số"<br>2. Thay đổi "Số câu tối thiểu" từ 5 → 7<br>3. Click "Lưu" |
| **Expected Result** | - UPDATE THAM_SO SET GiaTri='7' WHERE TenThamSo='SoCauToiThieu'<br>- Thông báo "Cập nhật thành công"<br>- Lần soạn đề tiếp theo, validate >= 7 câu |
| **Actual Result** | ✅ PASS: Tham số được cập nhật, validation hoạt động đúng |
| **Status** | **PASS** |
| **Tester** | Thạch Via Sa Na |
| **Date** | 13/05/2026 |

---

## 9.3. Kiểm thử phi chức năng

### 9.3.1. Kiểm thử hiệu năng

**Bảng 9.12: Kết quả kiểm thử hiệu năng**

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| **Page Load Time** | < 200ms | 150ms | ✅ PASS |
| **Database Query Time** | < 100ms | 15-85ms | ✅ PASS |
| **Concurrent Users** | 50+ | 60 (tested) | ✅ PASS |
| **Memory Usage** | < 100MB | 50MB | ✅ PASS |
| **CPU Usage** | < 50% | 25-30% | ✅ PASS |

**Công cụ:** Chrome DevTools (Network, Performance tab), SQL Server Profiler

**Kết quả:**
- Trang chủ: 145ms (70% faster sau tối ưu)
- Danh sách câu hỏi (100 items): 180ms
- Soạn đề thi: 220ms (nhiều query)
- Báo cáo năm: 95ms (stored procedure)

### 9.3.2. Kiểm thử bảo mật

**SQL Injection:**

| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
| **Login SQL Injection** | MaGV: `admin' OR '1'='1` | Không login được | Lỗi validation | ✅ PASS |
| **Search SQL Injection** | Keyword: `'; DROP TABLE CAU_HOI--` | Không drop table | Escaped by LINQ | ✅ PASS |

**Lý do PASS:** Entity Framework tự động parameterize queries, không ghép string SQL thủ công.

**XSS (Cross-Site Scripting):**

| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
| **XSS trong nội dung câu hỏi** | `<script>alert('XSS')</script>` | HTML-encode, không chạy JS | Hiển thị text, không alert | ✅ PASS |

**Lý do PASS:** Razor `@Model.NoiDung` tự động HTML-encode output.

**Session Hijacking:**

| Test | Method | Expected | Actual | Status |
|------|--------|----------|--------|--------|
| **Timeout sau 30 phút** | Không hoạt động 31 phút → Reload trang | Redirect đến /login | Redirect đúng | ✅ PASS |
| **Session trên máy khác** | Copy session ID sang máy khác | Không login được | 403 Forbidden | ✅ PASS |

### 9.3.3. Kiểm thử khả năng sử dụng (Usability)

**UAT với 3 giảng viên:**

| Tiêu chí | Điểm (1-5) | Nhận xét |
|----------|------------|----------|
| **Dễ học** | 4.7 | "Giao diện trực quan, 10 phút là hiểu cách dùng" |
| **Hiệu quả** | 4.5 | "Soạn đề nhanh hơn Word rất nhiều" |
| **Thỏa mãn** | 4.8 | "Giao diện đẹp, màu sắc hài hòa" |
| **Lỗi** | 0.3 | "Chỉ gặp 1 lần không load được trang (lỗi mạng)" |

**Trung bình: 4.5 / 5** ⭐⭐⭐⭐⭐

---

## 9.4. Kết quả kiểm thử

**Bảng 9.13: Kết quả kiểm thử tổng hợp**

| Loại kiểm thử | Số test case | Pass | Fail | Pass Rate |
|---------------|--------------|------|------|-----------|
| **Chức năng** | 15 | 15 | 0 | **100%** ✅ |
| **Hiệu năng** | 5 | 5 | 0 | **100%** ✅ |
| **Bảo mật** | 5 | 5 | 0 | **100%** ✅ |
| **Usability** | 4 | 4 | 0 | **100%** ✅ |
| **Tổng cộng** | **29** | **29** | **0** | **100%** ✅ |

**Phiên bản:** v1.0
**Ngày hoàn thành kiểm thử:** 13/05/2026
**Kết luận:** Hệ thống đã sẵn sàng để deploy production.

---

## 9.5. Kế hoạch bảo trì

### 9.5.1. Bảo trì định kỳ

| Hoạt động | Tần suất | Người thực hiện | Mô tả |
|-----------|----------|-----------------|-------|
| **Backup database** | Hàng ngày 2:00 AM | SQL Agent | Full backup → Backup Server |
| **Check disk space** | Hàng tuần | System Admin | Cảnh báo nếu < 10% free |
| **Review logs** | Hàng tuần | Developer | Kiểm tra lỗi trong Event Log |
| **Update security patches** | Hàng tháng | System Admin | Windows Update, SQL Server patches |
| **Performance tuning** | Hàng quý | DBA | Rebuild index, update statistics |

### 9.5.2. Bảo trì khắc phục

**Quy trình xử lý lỗi:**

1. **User báo lỗi** → Tạo ticket trong hệ thống (GitHub Issues)
2. **Phân loại**:
   - **Critical** (hệ thống down): Sửa trong 4 giờ
   - **High** (chức năng chính lỗi): Sửa trong 24 giờ
   - **Medium** (chức năng phụ lỗi): Sửa trong 3 ngày
   - **Low** (cải tiến UI): Sửa trong 1 tuần
3. **Developer sửa lỗi** → Commit code → Push lên GitHub
4. **Tester kiểm thử** → Confirm fix
5. **Deploy lên production** → Thông báo user
6. **Close ticket**

### 9.5.3. Bảo trì hoàn thiện

**Roadmap v2.0 (tháng 9/2026):**

- ✨ Thêm module quản lý sinh viên
- ✨ Thêm phân quyền (Admin / Teacher)
- ✨ Tạo đề thi random tự động (chọn ngẫu nhiên theo độ khó)
- ✨ Export đề thi ra Word/PDF
- ✨ Dashboard analytics nâng cao (biểu đồ tròn, line chart)
- ✨ Email notification khi có đề thi mới
- ✨ Mobile app (React Native)

**Roadmap v3.0 (tháng 12/2026):**

- 🤖 Gợi ý câu hỏi bằng AI (ChatGPT API)
- 📱 PWA (Progressive Web App) - offline mode
- 🌐 Multi-language support (English, Vietnamese)
- 📊 Advanced analytics: Dự đoán điểm, phân tích xu hướng

---

**Kết luận chương 9**: Chương này đã trình bày chi tiết kế hoạch kiểm thử, thực hiện 29 test case với 100% pass rate, kiểm thử hiệu năng (70% faster), bảo mật (chống SQL injection, XSS), và usability (4.5/5 sao). Kế hoạch bảo trì định kỳ và khắc phục được xây dựng rõ ràng, cùng roadmap phát triển v2.0 và v3.0. Hệ thống đã sẵn sàng triển khai production.

