# TS Studio Android — Changelog cho AI

## 2.0.0-alpha1 — 10/10/2026

**Nền:** `TS_Studio_v1.39.py`, hash SHA-256 `73089dfb0bdf23009ec558fc6ee9007430c4b247f1fdcae95406ea397cbe9682`.

**Mục tiêu:** Chuyển phần đọc/chỉnh XML, codec Township và UI cơ bản sang Android/LDPlayer bằng Native Java + Chaquopy Python.

**Đã làm:**
- Trích 431789 byte backend từ `ENGINE_DATA` bằng Base85 + zlib sang `township_studio_core.py` không chỉnh sửa, hash trùng changelog nguồn.
- Viết `android_bridge.py`, gọi API XML thuần; tách UI khỏi engine; không gọi hàm Windows/ADB khi chạy Android.
- Chuyển nguyên vẹn công thức checksum/header, random content seed, nén LZ4 block và XOR delta của Encode Tool v1.39 sang adapter Android.
- Import file bằng SAF, Root read-only trên LDPlayer, export bằng SAF, backup riêng, Undo/Reset.
- GUI responsive: Trang chủ / Profile / Decoration / Avatar / Barn / Academy / Unlock / Tool / History / Log.
- Test Python: 10/10 đạt trên fixture, chưa có smoke test APK/Android thực.

**Giữ từ v1.39:** 2 codec riêng biệt; template ADB cũ không bị thay đổi; không giả định Encode thành công sẽ được game chấp nhận; preserve identity ở các luồng Clone chưa chuyển.

**Chưa làm:** Nêu trong README. Những thao tác không có nút chạy còn giữ trong backend nguyên gốc nhưng chưa tích hợp vào UI Android.

**Rủi ro / bước kiểm tra tới:** Build trên Android Studio; test màn hình x86_64; test Android picker; xác minh thư viện `lz4`, `cryptography`, `requests`; test container mGameInfo/LocalInfo thực tế offline; thiết kế một luồng ghi cặp save bảo vệ identity, backup, readback, rollback rồi mới cân nhắc thêm nút Write to game.

**Quy tắc phiên bản:** Port Android có series v2.0.x-alpha, không ghi đè changelog bản Windows v1.39.
