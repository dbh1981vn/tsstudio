# Build APK hoàn toàn trên GitHub

1. Tạo repository **Private** trên https://github.com/new (không thêm README hay .gitignore từ GitHub).
2. Giải nén ZIP, mở thư mục `TS_Studio_Android_v2.0_alpha1` và tải **nội dung bên trong thư mục** lên gốc repository bằng Add file → Upload files. GitHub web có thể không cho tải thư mục ẩn `.github` thuận tiện; nếu thiếu, tạo file `.github/workflows/build-apk.yml` bằng Add file → Create new file và chép nội dung file từ project.
3. Vào Actions → Build TS Studio Android APK → Run workflow → Run workflow.
4. Chờ chạy xong. Vào trang lần chạy, phần Artifacts tải `TS-Studio-Android-v2.0-alpha1-debug.zip`, giải nén lấy `app-debug.apk`.
5. Kéo APK vào LDPlayer hoặc dùng `adb install -r app-debug.apk`.

**Chú ý:** Đây là build debug để thử nghiệm, chưa được xác nhận build thành công trên GitHub hay chạy trên giả lập. Nếu build báo lỗi, mở Actions → lần chạy lỗi → Build debug APK, sao chép log lỗi để sửa. Nếu tải nguyên ZIP lên GitHub như một file đơn lẻ, Actions không thể biên dịch source bên trong.
