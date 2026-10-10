# TS Studio Android 2.0 Alpha 1 — source project

**Trạng thái:** Project mã nguồn Android có logic hoạt động, **chưa biên dịch APK trong môi trường tạo project**. Các bài kiểm thử Python chạy thành công trên máy xây dựng; **chưa chạy thử trên thiết bị Android / LDPlayer và chưa kiểm tra save này trong game**.

Đây là bản chuyển đổi một phần (alpha) từ `TS_Studio_v1.39.py` + `TS_Studio_CHANGELOG_AI.md` được cung cấp. Không phải toàn bộ 50+ tính năng của giao diện Windows đã được chuyển đổi. **Không cài đặt Playrix/Township**, chỉ là ứng dụng bên thứ ba làm việc với file save mà bạn có quyền truy cập.

## 1. Thành phần đã làm

- Giao diện Android mới: responsive, cảm ứng, tiếng Việt, layout tối giản, chạy trong `WebView` nhúng cục bộ (không tải trang từ internet).
- Không dùng PyQt5 trên Android. Native Java xử lý tương tác hệ điều hành; backend Python chạy qua Chaquopy.
- `township_studio_core.py`: bản backend giải nén **nguyên vẹn** từ `ENGINE_DATA` của bản v1.39, không sửa các thuật toán này. SHA-256: `b6bbafa3f7cfec37b47291b7e18b0b83f389583e30cc86325e645782cb53b29d`.
- `android_bridge.py`: giao diện API giới hạn các hàm xử lý XML trong bộ nhớ, hỗ trợ import, export, lịch sử và xác minh.
- Mở file bằng Storage Access Framework (Android picker) — không yêu cầu quyền đọc toàn bộ bộ nhớ.
- **Chỉ đọc** `mGameInfo.xml` từ thư mục game nếu giả lập đã ROOT (`su`). Không tự động ghi vào save game.
- Giải mã `0x79` → XML; xuất XML; Encode độc lập đúng công thức TSVIP v1.39; Encode bằng container gốc như backend cũ (trường hợp có template). Decode lại để xác minh dữ liệu sau Encode.
- Chỉnh mGameInfo trong phiên làm việc: Coins/Cash, Level/XP theo engine, game start month, Decorations (theo nhóm và ID), Avatar (tick trạng thái, áp dụng diff), Barn level và sản phẩm, Academy time bonus, Golden Pass Premium, Land, Museum, sửa trực tiếp `Var` có sẵn.
- Undo tối đa ba bước, Reset về bản nhập, tự lưu bản nhập làm backup nội bộ, mở lại backup, xuất lại container ban đầu.
- Khóa trần XML 32 MB / container 64 MB; XML parse/validate và xuất file bằng ghi an toàn.

**Lưu ý:** Nút đổi Level mới sửa `mGameInfo`. Phiên bản Alpha này **chưa đồng bộ LocalInfo**. KHÔNG sử dụng file Level đã sửa để ghi vào game nếu chưa triển khai đủ quy trình cặp save. Thuật toán `gui_encode_xml_standalone` của v1.39 chưa có bằng chứng được game chấp nhận trực tiếp.

## 2. Phạm vi chưa làm

- Clone V1/V3, FetchCity/Friends, New TownCity, cặp mGameInfo + LocalInfo, ghi file trực tiếp vào game/rollback, cặp identity và bảo vệ tài khoản.
- History Restore vào game, Google Drive/OAuth/cloud sync, ZIP backup và restore trực tiếp vào game.
- Skin, Stickers, Profiles, Achievements, Golden Pass Editor từng stage/chest, nhiều chế độ Academy nâng cao và các editor còn lại trong bản Windows.
- 15 themes tùy biến và 12 ngôn ngữ chưa chuyển. Bản Alpha dùng giao diện cố định tiếng Việt.
- Root chỉ hỗ trợ đọc file tại `/data/data/<package>/saves/mGameInfo.xml`. Nếu phiên bản game dùng nơi lưu khác, dùng file picker.
- Chưa kiểm tra APK thực tế trên Android, vì không có SDK/Gradle trong môi trường build của phiên này.

## 3. Yêu cầu build trên Windows

- Android Studio có Android SDK Platform 35 và Build Tools 35.
- JDK 17 (có thể dùng JetBrains Runtime trong Android Studio).
- Kết nối internet cho lần build đầu để Gradle và Chaquopy tải plugin / binary wheel.
- Gradle **8.10.2** dùng với Android Gradle Plugin **8.8.2**.
- Python có thể được dùng khi build các yêu cầu Python: chương trình mặc định `python3.11` hoặc `python` tương thích 3.11. Trên Windows bạn nên cài Python **3.11** từ python.org, và thêm vào PATH.
- Build target Android 8.0 trở lên (minSdk 26), x86_64 (LDPlayer 64-bit) hoặc arm64-v8a (điện thoại 64-bit).

**Cách 1 (tiện nhất trên Windows):**

1. Giải nén project.
2. Cài Android Studio và SDK 35, Python 3.11.
3. Chạy `build_apk_windows.bat` (double click hoặc qua CMD). Script sử dụng Gradle 8.10.2 trong thư mục riêng; nếu chưa có sẽ tải từ `services.gradle.org` bằng PowerShell, cần internet.
4. Sau khi thành công, APK nằm trong `dist/TS_Studio_Android_v2.0_alpha1-debug.apk` và `app/build/outputs/apk/debug/app-debug.apk`.
5. Cài trên LDPlayer: `adb install -r "dist\TS_Studio_Android_v2.0_alpha1-debug.apk"` (khi có nhiều thiết bị cần `adb -s <serial> install -r ...`).

**Cách 2:** Mở thư mục project trong Android Studio; sử dụng JDK 17 và Gradle 8.10.2, chọn **Build > Build Bundle(s) / APK(s) > Build APK(s)**. Project không đính kèm `gradle-wrapper.jar`, nên có thể cần cấu hình Gradle distribution 8.10.2 hoặc chạy script lần đầu.

## 4. Cách dùng

1. Mở TS Studio trên LDPlayer/điện thoại.
2. Bấm **Mở file save**, chọn `mGameInfo.xml` đã trích xuất vào thư mục Android Download hoặc chọn XML thông thường.
3. Ứng dụng tự nhận loại file, decode và hiển thị thông tin Level/Coins/Cash.
4. Mở tab chỉnh sửa; chọn mục và bấm **Áp dụng**. Chức năng sửa chỉ thay XML trong phiên làm việc.
5. Bấm **Xuất save mã hóa 0x79** (Encode độc lập) hoặc **Xuất XML đã chỉnh sửa** để ghi file qua picker của Android. Không ghi đè save gốc khi không chủ ý.
6. Nếu LDPlayer ROOT, có thể chọn **Đọc từ LDPlayer ROOT**. Chọn Township VN hoặc bản quốc tế trong hộp thoại; cấp quyền root nếu giả lập hỏi. Chế độ này chỉ nhập save, tuyệt đối không tự ghi ngược vào thư mục game.
7. Tab History mở lại bản nhập đầu tiên theo thời điểm nhập; bản này lưu nội bộ và sẽ mất nếu xóa dữ liệu hoặc gỡ app. Hãy xuất bản sao ra thư mục Download trước khi xóa app.

## 5. Cấu trúc project

```
app/src/main/java/com/tsstudio/android/MainActivity.java       Android UI host, picker, ROOT read
app/src/main/assets/index.html                           Modern responsive interface
app/src/main/assets/style.css                            Design system
app/src/main/assets/app.js                                UI logic
app/src/main/python/township_studio_core.py               Engine v1.39 (unchanged)
app/src/main/python/android_bridge.py                     Safe Android-compatible Python API
app/src/main/AndroidManifest.xml                          No INTERNET/storage-wide permissions
tests/test_android_bridge.py                               PC regression tests
docs/TS_Studio_SOURCE_CHANGELOG.md                        Source history
docs/original_windows/TS_Studio_v1.39.py                 Original Windows GUI code (reference only)
docs/preview_phone.png / docs/preview_tablet.png         Android UI layout previews
docs/ANDROID_CHANGELOG.md                                 This Android port history
```

## 6. Kiểm thử

Trên máy tính cài Python (không cần SDK):

```
python -m pip install lz4 requests cryptography
python -m unittest discover -s tests -v
```

Đã kiểm tra với fixture XML, không phải save game thực tế: roundtrip 0x79 với LZ4 và không nén, checksum/header, import encrypted, export, các patch cơ bản, Undo/Reset, backup, dữ liệu hỏng và đường dẫn độc hại. Kiểm tra save thật trên game là bước bổ sung, không thể suy ra chỉ từ roundtrip.

## 7. An toàn

Ứng dụng không có quyền INTERNET trong AndroidManifest. Chưa làm đăng nhập Google, gọi server Playrix hay gửi file đi đâu. File nằm trong `getFilesDir()` app; import/export qua Android picker. Nội dung có thể bao gồm City ID/token cá nhân — không chia sẻ file save/backup công khai. Cho phép đọc ROOT phụ thuộc hệ thống; không lách sandbox Android nếu thiết bị không cấp quyền ROOT.

## 8. Ghi chú kỹ thuật

- `android_bridge.py` áp dụng thuật toán Encode độc lập từ hàm `gui_encode_xml_standalone` của GUI Windows (v1.39); backend nguồn vẫn giữ nguyên `encode_save(xml, template)` cho legacy.
- Đầu ra Encode độc lập được kiểm tra bằng `B.decode_save(result) == canonical_xml` rồi mới ghi.
- Python module có nhiều chức năng Windows/ADB cũ để bảo toàn thuật toán, nhưng app Android không gọi các hàm đó và không thể giả định ADB thực thi bên trong giả lập.
- Giao diện cần hoạt động trước khi tuyên bố tính năng hoàn thiện. Test Python chỉ xác minh nghiệp vụ phần đã chuyển.


## ROOT Apply (v2.2)
Chọn PACKAGE_NAME trên trang chủ, bấm **Đọc save ROOT**, chỉnh sửa, rồi **Apply trực tiếp vào game**. Android sẽ yêu cầu cấp quyền `su` nếu trình quản lý ROOT hỗ trợ. Chỉ hai package `com.playrix.township.vn` và `com.playrix.township` được chấp nhận. Ứng dụng kiểm tra SHA-256 để không ghi đè save đã thay đổi, dừng game, tạo `mGameInfo.xml.tsstudio.bak`, ghi file 0x79 đã encode, khôi phục owner/quyền/SELinux và xác minh SHA-256. Nếu save thay đổi sau khi đọc, phải đọc lại trước khi ghi. Cần tự backup cả LocalInfo nếu dự định sửa Level.

**Chưa được kiểm thử trực tiếp trên LDPlayer/MuMu/rooted phone.** Một số bản Android/ROM có thể từ chối `su`, `chown --reference`, `chcon --reference` hoặc đường dẫn khác `/data/data/...`. Trường hợp đó thao tác sẽ báo lỗi, không khẳng định đã ghi thành công.
