# 📤 Hướng dẫn Upload lên GitHub

## ✅ Đã hoàn thành
- ✅ Git init
- ✅ Git add .
- ✅ Git commit
- ✅ Git branch -M main
- ✅ Git remote add origin

## 🔄 Cần làm tiếp

### Phương án 1: Dùng Command Line (PowerShell)

```powershell
# Di chuyển vào thư mục project
cd "c:\Users\UDT4HC\Downloads\CNPM new\Project\QuanLyRaDeChamThi"

# Push code lên GitHub
git push -u origin main
```

**Nếu gặp lỗi authentication:**
```powershell
# Cài đặt user (thay bằng tên và email GitHub của bạn)
git config --global user.name "YounqThjnk187"
git config --global user.email "your-email@example.com"

# Push lại
git push -u origin main
```

**Nếu bị yêu cầu đăng nhập:**
- GitHub đã không còn hỗ trợ password
- Cần tạo **Personal Access Token** (PAT):
  1. Vào GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  2. Generate new token → Chọn repo
  3. Copy token
  4. Dùng token này thay cho password khi push

---

### Phương án 2: Dùng GitHub Desktop (Khuyến nghị - dễ nhất)

1. **Tải GitHub Desktop**: https://desktop.github.com/
2. **Đăng nhập** GitHub account
3. **File → Add Local Repository**
4. Chọn folder: `c:\Users\UDT4HC\Downloads\CNPM new\Project\QuanLyRaDeChamThi`
5. **Publish repository** → Chọn repo: `questions_grading_management`
6. Nhấn **Publish** → Xong!

---

### Phương án 3: Dùng VS Code

1. Mở folder project trong VS Code
2. Source Control (Ctrl+Shift+G)
3. Nhấn nút **Publish Branch**
4. Đăng nhập GitHub
5. Chọn repo `questions_grading_management`
6. Publish → Xong!

---

## 🔍 Kiểm tra đã upload thành công

Mở trình duyệt, vào:
```
https://github.com/YounqThjnk187/questions_grading_management
```

Bạn sẽ thấy:
- ✅ README.md hiển thị đẹp
- ✅ Tất cả files đã có
- ✅ 57 files changed trong commit đầu tiên

---

## 📝 Lệnh Git hữu ích

```powershell
# Xem trạng thái
git status

# Xem lịch sử commit
git log --oneline

# Xem remote
git remote -v

# Pull code mới từ GitHub về
git pull origin main

# Commit & push sau khi sửa code
git add .
git commit -m "📝 Update: mô tả thay đổi"
git push origin main
```

---

## 🎉 Sau khi upload thành công

1. **Thêm collaborators**: Settings → Collaborators → Add people
2. **Tạo branches** cho từng thành viên làm việc
3. **Sử dụng Issues** để quản lý công việc
4. **Pull Requests** để review code trước khi merge

---

**Repo URL:** https://github.com/YounqThjnk187/questions_grading_management

**Good luck! 🚀**
