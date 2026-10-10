# TS Studio — Nhật ký phiên bản và bàn giao cho AI

Cập nhật: **10/10/2026, giờ Việt Nam**. Bản ứng dụng được đối chiếu: **TS_Studio_v1.39.py**.

Tài liệu này dùng cùng file Python hiện tại để tiếp tục phát triển. Đây là nhật ký tổng hợp từ code và lịch sử trao đổi, không phải bản diff tự động của tất cả phiên bản cũ. Chỗ chưa đủ bằng chứng được ghi rõ; không suy đoán ngày phát hành hoặc số phiên bản.

## 1. Thông tin cần đọc trước khi sửa

- Ứng dụng Python/PyQt5 cho Township, chạy chủ yếu trên Windows và giả lập Android qua ADB.
- File Python độc lập, chứa backend bắt nguồn từ `v0.4.21` trong `ENGINE_DATA` dạng Base85 + zlib. Không cần một file core bên cạnh.
- Backend được nạp vào module `township_studio_core`; lớp GUI gọi qua biến `B`.
- Bản hiện tại: `v1.39`. Bản cập nhật nhỏ tiếp theo: `v1.40`; thay đổi lớn mới lên `v2.0`, sau đó `v2.01`, `v2.02`… theo quy ước của người dùng.
- SHA-256 file Python: `73089dfb0bdf23009ec558fc6ee9007430c4b247f1fdcae95406ea397cbe9682`.
- SHA-256 backend đã giải nén: `b6bbafa3f7cfec37b47291b7e18b0b83f389583e30cc86325e645782cb53b29d`.
- Không sửa code dựa riêng vào tài liệu này nếu file Python đã có phiên bản mới hơn. Đọc lại code mới nhất trước.
- Cài đặt: `python -m pip install PyQt5 lz4 requests cryptography`. Google Drive dùng thêm `google-auth-oauthlib keyring`.
- Không đưa token tài khoản, master key, thông tin OAuth hoặc nội dung save cá nhân vào changelog.

## 2. Nhật ký thay đổi

**Cách hiểu trạng thái:** “đã triển khai” nói về code; “đã kiểm tra” nói về kiểm tra được ghi nhận; “người dùng xác nhận” chỉ áp dụng cho tình huống đã thử. Encode/decode đúng không đồng nghĩa game hoặc server sẽ chấp nhận save.

### 2.1. Giai đoạn tạo GUI và xử lý ADB/Clone

| Phiên bản | Thay đổi / mốc được ghi nhận | Trạng thái và lưu ý |
| --- | --- | --- |
| Trước v1.0 | Chuyển các chức năng console sang PyQt5; thêm tab Profile, Unlock, Tool, Premium, VIP; popup dùng danh sách/checkbox/nút; Decoration chọn từng món, cả nhóm hoặc tất cả; Send Card chia trường cấu hình thành hai cột để tăng vùng bạn bè/thẻ; một số Unlock không có cấu hình chuyển sang Apply trực tiếp. | Mốc nền tảng, chưa tách chính xác thành từng bản nhỏ. |
| v1.0 | Người dùng chốt tên `TS_Studio_v1.0.py` và quy ước tăng phiên bản. | Không khẳng định rằng hạ level đã hoạt động ổn định ở bản này. |
| v1.01 | Sửa FetchCity `HTTP 403 / old_version`: bỏ phiên bản mặc định không phù hợp, ưu tiên thông tin LocalInfo/nhập thủ công, đọc lại LocalInfo qua ADB và thử lại một lần khi có cặp phiên bản mới hợp lệ. | Kiểm tra bằng tình huống giả lập; không ghi là mọi lỗi server đã được xử lý. |
| v1.02 | Cấu hình vị trí lưu backup; áp dụng cho backup tự động, ZIP tài khoản và History. | Đường dẫn được lưu; file cũ vẫn ở thư mục cũ. |
| v1.03 | Tách thông báo, đường dẫn và các mục chi tiết thành dòng riêng; làm rõ thay đổi trước/sau. | Sau đó v1.05 tinh chỉnh vì một số chỗ xuống dòng quá nhiều. |
| v1.04 | History Restore đọc lại cặp save thiết bị, backup trước khi ghi, dùng ZIP đã chọn và hỗ trợ rollback. | Nhằm xử lý lỗi “save trên thiết bị khác file đã tải”; không bỏ kiểm tra chống ghi nhầm tài khoản. |
| v1.05 | Chỉnh cách xuống dòng log: giữ giá trị cùng nhãn, ví dụ `FetchCity thành công: CITY_ID`; danh sách chi tiết mới tách dòng. | Không cắt dòng chỉ vì gặp dấu `:`. |
| v1.06 | Cấu hình bật/tắt tự mở Township sau khi ghi vào game; gửi lệnh mở package đã cấu hình. | Đã triển khai và kiểm tra luồng bằng giả lập. |
| v1.07 | Nút ADB ban đầu đỏ; kết nối và đọc XML thành công chuyển xanh, đổi chữ “Kết nối lại ADB”; bật các chức năng theo trạng thái kết nối. | Giữ Cấu hình/Hướng dẫn khả dụng; code hiện tại cũng cho phép thao tác sao chép/xuất log khi chưa kết nối. |
| v1.08 | Sao chép bộ Level/XP từ donor, đồng bộ level giữa mGameInfo và LocalInfo, chuẩn bị ghi cặp save; log LV trước/nguồn/kết quả. | Kiểm tra encode/decode các mức thấp/cao; người dùng sau đó vẫn gặp trường hợp game trở lại LV cũ. |
| v1.09 | Trước ghi đọc lại hai save, backup bản đang ở thiết bị, kiểm tra identity tài khoản, dừng khi tài khoản đã đổi, rollback khi lỗi. | Không xử lý bằng cách bỏ mọi kiểm tra nguồn save. |
| v1.10 | Log level sau encode và sau đọc lại từ thiết bị trước khi mở game; hỗ trợ đối chiếu khi kết nối lại ADB. | Đã có log cả hai file đúng LV thấp nhưng mở game vẫn về LV cũ; bằng chứng ghi file thành công chưa chứng minh game chấp nhận. |
| v1.11 | Kiểm tra/chặn V3 khi donor có phiên bản mới hơn; lấy level backup từ mGameInfo. | Chính sách chặn phiên bản là trạng thái lịch sử, không còn là hành vi hiện tại. |
| v1.12 | Điều chỉnh xử lý thời gian V3: cập nhật `saveGlobalTime`, giữ `factoryTime`; tiếp tục đồng bộ LV cả hai file. | Không được xem đây là nguyên nhân duy nhất đã xác nhận cho lỗi quay về LV cũ. |
| v1.13 | Log đã ghi nhận kiểm tra donor/target và chặn donor `39.0.5` khi save hiện tại `39.0.2`. | Trao đổi trong giai đoạn này còn yêu cầu bảo toàn identity V3; chưa có đủ diff để gán toàn bộ sửa identity riêng vào bản này. |
| v1.14 | Khi donor mới hơn save, đọc `versionName` của game đã cài qua ADB để đối chiếu; vẫn chặn khi game thực tế cũ hơn donor. | Ví dụ `39.0.5 > 39.0.2` là log của giai đoạn đó, không phải hằng số phiên bản cần dùng về sau. |
| v1.15 | Mốc sau trao đổi về bỏ lỗi chặn phiên bản và phân tích AirScore; lịch sử cũng có hướng dẫn xem City ID trong Sender ID của Send Card. | Chưa đủ diff để khẳng định tất cả thay đổi của riêng bản này. Code hiện tại đã chuyển kiểm tra phiên bản V3 sang cảnh báo và tiếp tục, không tự đổi nhãn phiên bản XML. |

**Kết quả Clone do người dùng báo:** đã có lúc Backup/History đổi được cả từ LV thấp lên cao và từ cao xuống thấp; sau quá trình sửa, người dùng xác nhận cả V1 và V3 đã giảm được LV. Những xác nhận này không chứng minh mọi donor, mọi phiên bản game và mọi tài khoản đều hoạt động giống nhau.

### 2.2. New TownCity và bổ sung từ APK

| Phiên bản | Thay đổi | Trạng thái và quyết định giữ/gỡ |
| --- | --- | --- |
| v1.16 | Tích hợp New TownCity tự động LV3: backup, reset, mở game, chờ identity mới do game tạo, ghép mẫu LV3 rồi ghi cặp save. Có chế độ tiếp tục sau reset/chờ Agree. | Người dùng xác nhận mẫu thử vào LV3 và không hiện lại tutorial. Không tự bịa City ID hoặc dùng ID của mẫu làm tài khoản mới. |
| v1.17 | Thêm sao chép log và xuất log TXT. | Giữ trong giao diện hiện tại. Không cần đọc ZIP TS Lite hoặc tự nhận diện package thay cho cấu hình package đã có. |
| v1.18 | Thử bổ sung sao chép bố cục/Zoo và kho mẫu. | Sau thảo luận, các tính năng độc lập bị coi là trùng Clone V1 và Backup/History. |
| v1.19 | Gỡ/tích hợp các chức năng trùng; đưa xem trước nguồn và chọn nội dung sao chép, gồm đảo/bảo tàng, vào Clone V1. | Không thêm lại kho mẫu hay nút sao chép Zoo riêng nếu chỉ lặp lại logic đang có. |
| v1.20 | Bổ sung chẩn đoán ADB, quyền root, cặp save; cải thiện Barn theo nhóm, sắp xếp và đếm các dòng thay đổi. | Tiếp tục dựa trên dữ liệu save và các trường đã biết. |
| v1.21 | Bổ sung tên hiển thị Sticker; thêm tab Academy chỉnh ô sản xuất nhà máy, phạm vi 2–7 ô. | Ô sản xuất khác với bonus ô kệ của Academy; không nhập hai chức năng thành một. |
| v1.22_test | Thử các Decoration chênh lệch với TWNTool. | Bản thử, không phải danh mục tất cả đã được xác nhận chạy. |
| v1.22 | Trong các ID mới thử, chỉ giữ `ExpeditionDecoration46`, `47`, `48`, `49`. | Người dùng xác nhận bốn ID này hoạt động. Các ExpeditionDecoration mới khác/biển tên thử không hoạt động; Landscape/Roads và các icon miễn phí không cần bổ sung để mở khóa. Không xóa danh mục Decoration gốc vì nhận xét này chỉ nói về các ID bổ sung. |
| v1.23 | Chuyển sang bảng màu pastel xanh tím, xanh nhạt, hồng đào/hồng/tím theo ảnh tham chiếu. | Sau đó mở rộng thành bộ theme tùy chỉnh ở v1.26–v1.27. |

### 2.3. Cloud, theme và ngôn ngữ

| Phiên bản | Thay đổi | Lưu ý kỹ thuật |
| --- | --- | --- |
| v1.24 | Backup lên Google Drive; History đọc backup cloud; cấu hình cloud trong hệ thống. | ZIP vẫn lưu trên máy trước; cloud là phần bổ sung tùy chọn. |
| v1.25 | Upload/download nhiều backup trong một đợt, chọn nhiều dòng; tiến độ, kết quả từng file, dừng và thử lại mục lỗi/chưa chạy. | Hàng đợi truyền tuần tự, không khẳng định truyền song song. |
| v1.26 | Thêm 5 theme mặc định và màu tùy chỉnh. | Màu trình bày Qt; không ảnh hưởng dữ liệu save. |
| v1.27 | Thêm 10 theme, tổng cộng 15; hỗ trợ 8 trường màu và icon phù hợp theme. | Bộ màu gồm cả sáng/tối; cần giữ khả năng đọc chữ trên nút/nền. |
| v1.28 | Cấu hình 12 ngôn ngữ: Anh, Pháp, Indonesia, Bồ Đào Nha, Tây Ban Nha, Nhật, Trung, Hàn, Nga, Thổ Nhĩ Kỳ, Việt, Ả Rập (Ai Cập). | Dịch giao diện offline; không dịch ID/khóa XML/dữ liệu người dùng. |
| v1.29 | Mở rộng bản dịch tiếng Anh cho tiêu đề, mô tả, tooltip, Settings và log; cải thiện đổi ngôn ngữ đang chạy. | Giữ nội dung log nguồn để hiển thị lại; chưa cam kết toàn bộ tên sản phẩm có tên dịch ở mọi ngôn ngữ. |

Lỗi OAuth Google `403 access_denied` khi ứng dụng ở chế độ Testing cần cấu hình Test users/phát hành phù hợp phía Google. Không ghi nhận nó là lỗi mã hóa Township hoặc một lỗi đã được sửa hoàn toàn chỉ bằng Python.

### 2.4. Các bản chỉnh GUI gần nhất

| Phiên bản | Thay đổi | Kiểm tra / hành vi |
| --- | --- | --- |
| v1.30 | Tiếng Anh là mặc định khi chưa lưu lựa chọn; ẩn cột ID ở Avatar, Decorations, Skin, Stickers, Profiles, Achievements; sửa Current của từng Decor và hỗ trợ Quantity per Item cho mục chọn chưa sửa riêng. | Current nhập riêng được ưu tiên; 0 xóa số lượng kho; danh mục/điều kiện đặc biệt theo logic hiện có. Không xóa ID khỏi XML. |
| v1.31 | Error/traceback/HTTP lỗi tô đỏ; Warning tô vàng; thích ứng nền sáng/tối. | Dùng syntax highlighter, không chèn HTML vào nội dung sao chép/xuất log. |
| v1.32 | Checkbox ở Avatar/Skin/Stickers/Profiles/Achievements phản ánh trạng thái hiện tại; tick mở, bỏ tick khóa; Apply chỉ cập nhật khác biệt. | Không dùng checkbox đồng thời với nghĩa “chọn thao tác” rồi áp dụng mở tất cả. Bỏ tick Achievement giữ bộ đếm tiến độ. |
| v1.33 | Thanh tiêu đề tùy biến cho cửa sổ/popup, top navigation mới, icon SVG; tab tính kích thước theo chữ đậm và có cuộn ngang để tránh mất chữ. | Giữ hành vi Close/Cancel, popup cảnh báo, kéo cửa sổ, đổi kích thước. Hộp chọn file của hệ điều hành vẫn là native. |
| v1.34 | Academy Level Bonus có Industries/Trains/Islands; Max All/All/None; checkbox và bonus từng dòng. | Industries: Time/Coin/XP/Slots; Trains: Time/Coin/XP; Islands: Time/Products. Max All tác động nhóm đang xem; không sửa các dòng không chọn. |
| v1.35 | Golden Pass Editor có Free/Premium, từng Stage có Claim, chọn sản phẩm, Quantity; ST_Chest có nhiều sản phẩm, số lượng và Claim riêng. | Đọc số Stage từ save thực tế; giữ Stage không sửa. Claim chỉ sửa cờ trong save, không cộng trực tiếp sản phẩm vào kho. Đã kiểm tra GUI/XML, chưa thử trực tiếp trong game. |
| v1.36 | History rộng/cao hơn, có splitter giữa danh sách backup và thông tin, bố trí lại nút; thêm Encode và Decode ở Tool. | Lúc này Encode dùng XML và save mã hóa gốc làm template. Đã kiểm tra round-trip, giữ input và xử lý lỗi. |
| v1.37 | Điền sẵn template Encode bằng `workspace_simple/source.mGameInfo`; vẫn Browse/chỉnh đường dẫn. | Yêu cầu template thuộc giai đoạn lịch sử; đã bỏ ở v1.39. |
| v1.38 | Input mặc định ở `workspace_simple/inputxml`, Output ở `workspace_simple/output`; ghi nhớ đường dẫn/thư mục Browse bằng QSettings. | Nhớ theo từng ô/chế độ, kể cả sau khi đóng chương trình. Có tên output gợi ý, không ghi đè tên output do người dùng sửa trong popup. |
| v1.39 | Encode độc lập từ XML theo công thức TSVIP: tạo container 0x79 mới, nén LZ4, tự tính checksum/header, sinh phần ngẫu nhiên, mã hóa; bỏ ô Original encoded save. | Đối chiếu checksum với công thức Java/Smali TSVIP, round-trip compressed/plain, Unicode, dữ liệu mGameInfo/LocalInfo và GUI hai ô. Chưa thử trực tiếp trong game. Luồng Encode/Ghi qua ADB vẫn dùng backend cũ. |

## 3. Những quyết định phải giữ khi phát triển

1. Tất cả editor nên dùng GUI chọn danh sách/checkbox/spinbox; tránh yêu cầu nhập theo console nếu có thể biểu diễn bằng GUI.
2. Tác vụ editor thường chỉ sửa phiên làm việc. Export/Write to game là bước lưu/ghi; New TownCity tự động và History Restore vào game có luồng ghi riêng.
3. Không thay City ID/Game ID/token/identity thiết bị của target bằng identity donor khi Clone. City ID nguồn và tài khoản đang thao tác là hai vai trò khác nhau.
4. Không kết luận “Township chắc chắn không cho giảm level” hoặc “bver/fver là nguyên nhân duy nhất”. Đã có kết quả người dùng giảm được level, nhưng từng nguồn/phiên bản cần đối chiếu riêng.
5. V3 hiện cảnh báo về phiên bản mới hơn và cho tiếp tục; không tự sửa nhãn version trong XML để giả tương thích.
6. New TownCity chờ game tạo identity mới thật; không tự sinh City ID giả. Mẫu LV3 cung cấp nội dung/tutorial, không cung cấp danh tính tài khoản mới.
7. Decorations: các ID thử chưa hoạt động không tự thêm lại; chỉ bốn ID bổ sung 46–49 đã được người dùng xác nhận. Không mở khóa các icon miễn phí chỉ để làm danh mục dài hơn.
8. Không đưa lại chức năng trùng Zoo layout/kho mẫu nếu Clone V1 và Backup/History đã đáp ứng.
9. Giữ 15 theme, tùy chỉnh màu, lựa chọn ngôn ngữ và tiếng Anh mặc định. Không dịch khóa XML, product ID, City ID, token, URL hoặc tên file.
10. Log giữ thông tin đọc được; nhãn và giá trị trên một dòng, danh sách chi tiết mới tách dòng. Màu lỗi/cảnh báo không làm thay đổi nội dung TXT.
11. Input/Output có Browse và nhớ thư mục gần nhất. Encode Tool v1.39 không được yêu cầu lại template nếu không có quyết định mới.
12. Chỉ thông báo kết quả đã kiểm tra; tách “file được ghi và đọc lại đúng” khỏi “game/server đã chấp nhận”.

## 4. Kiến trúc và điểm sửa trong code hiện tại

| Khu vực | Hàm / lớp tiêu biểu | Chú ý khi sửa |
| --- | --- | --- |
| Core | `ENGINE_DATA`, `B`, `B.SESSION` | Backend nhúng; tránh thay cả chuỗi chỉ để chỉnh GUI. |
| Menu/dispatch | `GROUPS`, `NativeWindow.open_editor`, `make_cards` | Nút mới phải có handler và tuân trạng thái kết nối/busy. |
| Worker | `Worker`, `Window.start`, `thread_finished` | Công việc dài chạy QThread; widget và hộp thoại ở UI thread. `B.print` được nối với log trong luồng Worker; test gọi action trực tiếp cần xử lý điều này. |
| XML trong phiên | `apply_result`, `run_edit`, `B.SESSION.current_xml` | Validate XML; chỉ commit khi Apply được chấp nhận. |
| Clone V1 | `CloneV1Dialog`, `gui_clone_v1`, `gui_copy_donor_level` | Chọn nội dung, kiểm tra nguồn, backup; khi copy LV/XP phải chuẩn bị LocalInfo cùng cặp. |
| Clone V3 | `gui_preserve_v3_device`, `gui_sync_local_level`, `gui_check_v3_versions` | Giữ identity target, đồng bộ LocalInfo, cảnh báo version, ghi cả hai file. |
| New TownCity | `auto_new_town`, `gui_prepare_lv3_pair`, `gui_newtown_identity`, `gui_commit_device_pair` | Backup/reset/chờ identity/ghép mẫu; có timeout và hủy; không reset lại khi chỉ tiếp tục. |
| Backup/History | `backup`, `history`, `restore_history_pair`, `write_game_action` | ZIP/cặp save; đọc lại tài khoản live, backup trước ghi, kiểm tra kết quả/rollback. |
| Drive | `GoogleDriveBackup`, `CloudBatchWorker`, `CloudBatchDialog`, `GoogleDriveHistoryDialog` | Scope `drive.file`, dữ liệu backup của ứng dụng trong My Drive, token qua keyring; không truy cập tùy ý toàn bộ Drive. |
| Theme | `THEMES`, `THEME_FIELDS`, `apply_theme`, `native_icon` | 15 theme, 8 màu; style và SVG theo theme. |
| Ngôn ngữ/log | `I18N_CATALOG`, `EN_TRANSLATIONS`, `InterfaceLanguage`, `ActivityLogHighlighter`, `append_activity` | Giữ giá trị máy ở UserRole/currentData, không lấy ID từ caption đã dịch; giữ log nguồn. |
| Unlock | `UnlockStatePicker` và các hàm patch trạng thái GUI | Checkbox là trạng thái; chỉ apply diff; giữ các trường không liên quan. |
| Decoration | Editor `decorations` và helper lượng/tình trạng kho | Sửa Current khác với bulk Quantity; giữ các dòng không chọn. |
| Academy | `AcademyUpgradePage`, `gui_set_academy_rows`, `gui_set_factory_slots` | Bonus ô kệ 0–2 khác ô sản xuất 2–7; Island Time không dùng 100 theo template hiện tại. |
| Golden Pass | `PassStagePage`, `PassProductDialog`, `PassChestDialog`, `pass_patch_stage`, `pass_apply_rows` | State riêng từng Stage/rương; giữ attributes và XML không sửa; Claim không phải cấp sản phẩm trực tiếp. |
| Train | `gui_train_groups`, `gui_train_inventory`, `gui_edit_train_wagons` | Hỗ trợ schema toa đã biết; không tự tạo toa/train không có trong save; nhiều khối phải chọn đúng. |
| Title bar | `StudioChromeMixin`, `StudioTitleBar`, `StudioTabBar`, `StudioMessageBox` | Giữ Close/Cancel và guards khi worker đang chạy; đo tab bằng font đậm. |
| Codec file | `gui_encode_xml_standalone`, `gui_tsvip_content_checksum`, `gui_convert_save_file`, `file_codec` | Encode Tool mới riêng biệt; Decode vẫn qua `B.decode_save`. |
| Đường dẫn Browse | `path_field`, `remember_browse_path` | Tham số nhớ đường dẫn chỉ mở khi caller yêu cầu; không vô tình thay hành vi mọi picker. |

## 5. Hai cách Encode đang tồn tại — không được nhầm

### 5.1. Đọc/ghi qua ADB, Clone và cặp save

Backend `B.decode_save` đọc container; `B.encode_save(xml, template)` dùng container mẫu, giữ content seed và kích thước gốc. `B.SESSION.encode_verify()` và xử lý LocalInfo/cặp save vẫn thuộc luồng này.

**v1.39 không thay thuật toán ADB.** Nếu muốn áp dụng bộ tạo header mới vào Write to game, phải coi đó là thay đổi riêng, kiểm tra cặp save và thử trong game; không nói rằng việc này đã hoàn thành.

### 5.2. Tool → Encode độc lập ở v1.39

`gui_encode_xml_standalone` không đọc `source.mGameInfo`, không lấy seed từ template.

Quy trình hiện tại:

1. Validate XML Township, lấy nội dung đến `</root>`, thêm byte NUL như quy ước encoder đang dùng.
2. Mặc định nén LZ4 block, không dùng LZ4 frame chuẩn toàn phần. Payload là magic `04 22 4D 18`, độ dài XML 32-bit little-endian và dữ liệu nén.
3. Header seed = `(payload_length XOR 235176) + (total_length XOR 810733)`, với `total_length = payload_length + 8`. Kiểm tra giới hạn header 24 bit.
4. Checksum theo TSVIP: hai tổng cộng dồn 32 bit, **không thay bằng Adler-32 modulo 65521**.
5. Phần cao 16 bit của content seed được sinh ngẫu nhiên từ 1 đến 65535; phần thấp là checksum payload.
6. Tạo bảng 727 byte bằng helper MurmurHash2 hiện có; mã hóa payload bằng XOR và phép cộng với byte plaintext trước đó, không phải byte ciphertext trước đó.
7. Header 8 byte: `0x79`, header seed 3 byte little-endian, content seed 4 byte little-endian. Không thêm padding bằng kích thước template cũ.
8. Decode lại qua backend và so sánh canonical XML. Chỉ ghi output bằng atomic write khi khớp.

Công thức checksum được đối chiếu với `rc0.b` trong Java và Smali của TSVIP v121. API helper có nhánh không nén để kiểm tra, nhưng nút Encode mặc định nén. Hai lần Encode cùng XML có thể khác byte vì phần seed ngẫu nhiên; kiểm tra nội dung sau Decode, không yêu cầu hai file mã hóa có cùng SHA-256.

Giới hạn hiện tại: XML 32 MB, container đầu vào 64 MB, header seed 24 bit. Tool không được hiểu là hỗ trợ mọi định dạng game khác hoặc mọi định dạng legacy mà TSVIP từng hỗ trợ.

## 6. Dữ liệu, cấu hình và đường dẫn

`workspace_simple` nằm cạnh file Python chạy thực tế; không ghim đường dẫn máy của người phát triển.

| Vị trí / dữ liệu | Vai trò |
| --- | --- |
| `source.mGameInfo` | Container mGameInfo đã tải; phục vụ luồng backend/template ADB. Tool Encode v1.39 không cần file này. |
| `source.LocalInfo` | Container LocalInfo đã tải. |
| `decoded.xml`, `modified.xml` | XML giải mã và bản làm việc theo backend. |
| `output.mGameInfo`, `verify.xml` | Đầu ra/kiểm tra của backend ADB; khác thư mục Tool output bên dưới. |
| `inputxml/` | Thư mục mặc định Browse input của Tool Encode/Decode. Chọn file khác vẫn được. |
| `output/` | Thư mục output của Tool; gợi ý `mGameInfo_encoded.xml` hoặc `mGameInfo_decoded.xml`, đổi tên theo input khi phù hợp. |
| `backups/` | Backup tự động; vị trí có thể đổi trong cấu hình. |
| `a_TS_Files/<tài khoản>/` | ZIP backup tài khoản và nguồn History theo cấu hình. |
| `friends/<City ID>/friend_city.xml` | Donor FetchCity đã lưu. Không nhầm thư mục donor với tài khoản đang mở. |

QSettings dùng organization/application `TownshipStudio` / `PyQt5`. Các key codec hiện tại: `codec/inputxml`, `codec/inputsave`, `codec/encode_output`, `codec/decode_output`, mỗi key có `/path` và `/browse_dir`. Key `codec/template` có thể còn từ bản cũ nhưng GUI v1.39 không sử dụng. Browse chỉ chọn file, không xử lý/ghi dữ liệu; bấm Encode/Decode mới chạy tác vụ. Chọn đường dẫn được ghi nhớ ngay, cả khi sau đó đóng popup.

## 7. Cặp save, Level, identity và AirScore

- `mGameInfo.xml` và `LocalInfo.xml` là hai file liên quan; sửa một trường `levelup` không đủ cho mọi luồng.
- V1 copy LV dùng bộ `levelup`, `experience`, `sexpx` của donor; LocalInfo đồng bộ `PushNotifDeviceInfo.lvl`. Không tính lại XP tùy ý chỉ từ level.
- V3 thay phần lớn nội dung donor nhưng giữ City ID/Game ID/token target và các trường thiết bị/tài khoản đã được code xác định. Không mang identity donor vào target.
- Khi tài khoản thiết bị đã đổi sau reset, phải đọc lại và kiểm tra identity. `SOURCE_FILE` không mặc nhiên là bản đang sống trên thiết bị.
- History Restore có thể dùng backup cũ; thao tác này khác với áp dụng kết quả clone dựa trên phiên đã tải. Không khôi phục bằng cách bỏ guard chung cho mọi trường hợp.
- V1 hiện yêu cầu chọn Stats cùng AirScore/AirInfo; V3 có checkbox giữ AirScore/AirInfo của donor. Không khẳng định AirScore đã được server chấp nhận sau mở game chỉ vì có dữ liệu trong XML.
- User từng báo `mGameInfo.levelup` và `LocalInfo...lvl` đọc lại từ thiết bị đều thấp hơn nhưng game trở về LV cũ. Log này cần được giữ như tình huống hồi quy, không dùng để suy ra một nguyên nhân duy nhất.

## 8. Kiểm thử đã ghi nhận và việc còn cần xác minh

| Nhóm | Bằng chứng đang có | Chưa được khẳng định |
| --- | --- | --- |
| Clone/History hạ LV | Người dùng đã có các lần đổi LV thành công ở Backup/History và sau đó V1/V3; code có kiểm tra cặp/identity. | Độ ổn định với mọi donor, version và trạng thái server. |
| New TownCity LV3 | Người dùng xác nhận mẫu thử vào LV3, không tutorial; luồng chờ game tạo identity thật. | Hoạt động với mọi phiên bản game/mẫu/thiết bị. |
| Decoration mới | Người dùng xác nhận ExpeditionDecoration46–49. | Các ID bổ sung khác đã thất bại không được ghi là supported. |
| Theme/i18n/log/Unlock | Kiểm tra GUI, cập nhật trạng thái, giữ data/ID, màu và nội dung log. | Toàn bộ tên dịch đầy đủ ở mọi ngôn ngữ. |
| Academy | Kiểm tra bảng, bonus, giới hạn và chỉ cập nhật dòng chọn; hồi quy sau Golden Pass. | Mọi schema Upgrade phát sinh ở game tương lai. |
| Golden Pass v1.35 | Stage riêng, catalog, rương nhiều sản phẩm, Cancel, Apply, giữ XML ngoài phạm vi sửa. | Game thực sự trao/giữ phần thưởng mới đã chỉnh. |
| Codec v1.36–38 | Round-trip, file lỗi, giữ input, giao diện/đường dẫn. | Chấp nhận game của tất cả file đã sửa. |
| Codec v1.39 | Checksum tham chiếu Java và đối chiếu Smali TSVIP; header/độ dài, compressed/plain, Unicode, file mGameInfo/LocalInfo dạng fixture, lỗi không ghi output, GUI hai ô, nhớ Browse, backend không đổi. | **Chưa thử trực tiếp output v1.39 trong Township. Fixture XML không tương đương kiểm thử tài khoản thật.** |
| Drive | Code OAuth, token keyring, ZIP validation, truyền hàng đợi/kết quả từng file. | Kết quả cloud thực tế cần kiểm tra trên tài khoản/Google project đang dùng. |

Khi thử Codec mới trong game, cần ghi lại phiên bản game, input/output, thao tác áp dụng và kết quả sau khởi động. Không kết luận hoàn tất chỉ từ round-trip. Changelog này không đính kèm save thật, token hay key của người dùng.

## 9. Cách AI tiếp theo tiếp nhận và cập nhật

1. Đọc file Python mới nhất và tài liệu này; xác nhận phiên bản. Không dùng một file cũ hơn làm nền vì tình cờ còn trong thư mục tải xuống.
2. Xác định phần sửa: GUI, patch XML, network/cloud hay codec. Thay đổi phần cần thiết; kiểm tra những luồng liên quan.
3. Kiểm tra meaningful: đầu vào hợp lệ/lỗi, Apply/Cancel, không sửa dòng ngoài chọn, không làm mất thuộc tính chưa biết, không ghi đè input, giữ identity/cặp save và dữ liệu ngoài phạm vi.
4. Với GUI: kiểm tra đủ chữ khi tab active/đậm, resize, theme sáng/tối, ngôn ngữ, vùng danh sách đủ xem và nút không bị cắt.
5. Với codec: thêm test checksum/header độc lập; round-trip không kiểm tra được hết điều kiện game. Với cặp save: thử mGameInfo và LocalInfo cùng nhau.
6. Sau sửa, tăng phiên bản và ghi thêm mục changelog: vấn đề, hành vi mới, hàm/lớp đổi, kiểm tra đã chạy, giới hạn, kết quả thử trong game nếu có.
7. Đừng cập nhật các comment lịch sử bằng replace toàn bộ `v1.xx` một cách máy móc. Một số comment trong file hiện tại đã bị đổi thành số bản mới dù tính năng có từ trước; số phiên bản trong comment không đủ để xác định ngày tính năng được thêm.
8. Giữ changelog này là một tài liệu riêng cập nhật dần; không cần tăng phiên bản Python chỉ vì thêm tài liệu.

### Mẫu mục ghi cho lần sau

```text
Phiên bản: v1.40
Ngày:
Vấn đề / yêu cầu:
Thay đổi và hành vi mới:
Hàm / lớp / dữ liệu thay đổi:
Phần cần giữ tương thích:
Kiểm tra đã thực hiện:
Kết quả người dùng thử trong game:
Giới hạn / việc còn cần xác minh:
Quyết định giữ, bỏ hoặc thay thế tính năng cũ:
```

**Trạng thái kết thúc bản ghi này:** code hiện tại là v1.39; Encode Tool đã tự tạo container, chưa kiểm thử trực tiếp output mới trong game. Tài liệu không thực hiện thêm thay đổi vào Python.
