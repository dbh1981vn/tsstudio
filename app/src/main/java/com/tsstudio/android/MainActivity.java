package com.tsstudio.android;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Build;
import android.webkit.JavascriptInterface;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceError;
import android.widget.Toast;
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import org.json.JSONObject;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

/**
 * TS Studio Android UI host.
 * - Private local WebView UI (no internet/navigation)
 * - Storage Access Framework for file I/O (no broad storage permission)
 * - Chaquopy adapter on one background worker (no UI freezes)
 * - Optional root read from OWN Township install on LDPlayer, read only
 */
public final class MainActivity extends Activity {
    private static final int PICK_INPUT = 11;
    private static final int PICK_OUTPUT = 12;
    private static final long MAX_SIZE = 64L * 1024L * 1024L;
    private final ExecutorService executor = Executors.newSingleThreadExecutor();
    private WebView web;
    private int pendingRequest = -1;
    private String outputPath;
    private PyObject pyAdapter;
    private String rootPackage = "com.playrix.township.vn";

    @Override public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (Build.VERSION.SDK_INT >= 29) {
            getWindow().getDecorView().setSystemUiVisibility(
                android.view.View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR
                | android.view.View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR);
        }
        web = new WebView(this);
        WebSettings config = web.getSettings();
        config.setJavaScriptEnabled(true);
        config.setDomStorageEnabled(true);
        config.setAllowFileAccess(true); // required for file:///android_asset, not arbitrary URLs.
        config.setAllowFileAccessFromFileURLs(false);
        config.setAllowUniversalAccessFromFileURLs(false);
        config.setJavaScriptCanOpenWindowsAutomatically(false);
        config.setSupportMultipleWindows(false);
        config.setMediaPlaybackRequiresUserGesture(true);
        web.setWebViewClient(new WebViewClient() {
            @Override public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                return !isLocalAsset(request.getUrl());
            }
            @SuppressWarnings("deprecation")
            @Override public boolean shouldOverrideUrlLoading(WebView view, String url) {
                return !url.startsWith("file:///android_asset/");
            }
        });
        web.addJavascriptInterface(new JsBridge(), "TSNative");
        setContentView(web);
        web.loadUrl("file:///android_asset/index.html");
    }

    private boolean isLocalAsset(Uri url) {
        return "file".equals(url.getScheme()) && url.toString().startsWith("file:///android_asset/");
    }

    private PyObject backend() {
        if (pyAdapter == null) {
            pyAdapter = Python.getInstance().getModule("android_bridge");
        }
        return pyAdapter;
    }

    private String execute(String action, JSONObject params) throws Exception {
        JSONObject request = new JSONObject();
        request.put("action", action);
        request.put("args", params);
        String raw = backend().callAttr("command", request.toString()).toString();
        JSONObject parsed = new JSONObject(raw);
        if (!parsed.optBoolean("ok", false)) {
            throw new IllegalStateException(parsed.optString("error", "Python error"));
        }
        return raw;
    }

    private void send(int id, String json) {
        // Strict JSON value interpolation; do not interpolate file names into JavaScript.
        runOnUiThread(() -> {
            if (web != null) web.evaluateJavascript("window.TSCallback(" + id + "," + json + ")", null);
        });
    }
    private void error(int id, String detail) {
        try {
            JSONObject response = new JSONObject();
            response.put("ok", false);
            response.put("error", detail == null ? "Unknown error" : detail);
            send(id, response.toString());
        } catch (Exception ignored) { }
    }

    private final class JsBridge {
        @JavascriptInterface public void invoke(int id, String action, String parameters) {
            JSONObject parsed;
            try { parsed = new JSONObject(parameters); }
            catch (Exception e) { error(id, "Dữ liệu gửi không hợp lệ"); return; }
            final JSONObject args = parsed;
            if ("selectInput".equals(action)) {
                runOnUiThread(() -> chooseInput(id));
            } else if ("exportFile".equals(action)) {
                executor.execute(() -> prepareExport(id, args));
            } else if ("importRoot".equals(action)) {
                executor.execute(() -> importRoot(id, args));
            } else if ("applyRoot".equals(action)) {
                executor.execute(() -> applyRoot(id, args));
            } else {
                executor.execute(() -> {
                    try {
                        if ("init".equals(action)) args.put("data_dir", getFilesDir().getCanonicalPath());
                        send(id, execute(action, args));
                    } catch (Exception e) { error(id, e.getMessage()); }
                });
            }
        }
    }

    private void chooseInput(int id) {
        if (pendingRequest >= 0) { error(id, "Đang có một hộp thoại chọn file"); return; }
        pendingRequest = id;
        Intent intent = new Intent(Intent.ACTION_OPEN_DOCUMENT);
        intent.setType("*/*");
        intent.addCategory(Intent.CATEGORY_OPENABLE);
        intent.addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION);
        startActivityForResult(intent, PICK_INPUT);
    }

    private void prepareExport(int id, JSONObject params) {
        try {
            JSONObject backendResult = new JSONObject(execute("export", params)).getJSONObject("result");
            File file = new File(backendResult.getString("path"));
            if (!file.isFile() || file.length() > MAX_SIZE) throw new Exception("Không tạo được file export");
            String fileName = backendResult.getString("filename");
            runOnUiThread(() -> {
                if (pendingRequest >= 0) { error(id, "Hãy đóng hộp thoại file đang mở"); return; }
                pendingRequest = id;
                outputPath = file.getAbsolutePath();
                Intent intent = new Intent(Intent.ACTION_CREATE_DOCUMENT);
                intent.setType("application/octet-stream");
                intent.addCategory(Intent.CATEGORY_OPENABLE);
                intent.putExtra(Intent.EXTRA_TITLE, fileName);
                intent.addFlags(Intent.FLAG_GRANT_WRITE_URI_PERMISSION);
                startActivityForResult(intent, PICK_OUTPUT);
            });
        } catch (Exception e) { error(id, e.getMessage()); }
    }

    @Override protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        final int id = pendingRequest;
        pendingRequest = -1;
        if (id < 0) return;
        if (resultCode != RESULT_OK || data == null || data.getData() == null) {
            error(id, "Đã hủy chọn file");
            return;
        }
        final Uri uri = data.getData();
        executor.execute(() -> {
            try {
                if (requestCode == PICK_INPUT) {
                    File target = new File(getFilesDir(), "input_from_picker.bin");
                    try (InputStream input = getContentResolver().openInputStream(uri);
                         OutputStream output = new FileOutputStream(target)) {
                        if (input == null) throw new IllegalStateException("Không thể mở file");
                        copyLimited(input, output);
                    }
                    String name = findDisplayName(uri);
                    JSONObject args = new JSONObject();
                    args.put("path", target.getCanonicalPath());
                    args.put("name", name);
                    args.put("origin", "picker");
                    send(id, execute("import", args));
                } else if (requestCode == PICK_OUTPUT) {
                    File source = new File(outputPath);
                    if (!source.isFile()) throw new IllegalStateException("Không có file đầu ra");
                    try (InputStream input = new FileInputStream(source);
                         OutputStream output = getContentResolver().openOutputStream(uri, "w")) {
                        if (output == null) throw new IllegalStateException("Không có quyền ghi đích");
                        copyLimited(input, output);
                    }
                    JSONObject result = new JSONObject();
                    result.put("ok", true);
                    result.put("result", new JSONObject().put("saved", true).put("size", source.length()));
                    send(id, result.toString());
                }
            } catch (Exception e) { error(id, e.getMessage()); }
        });
    }

    private String findDisplayName(Uri uri) {
        try (android.database.Cursor cursor = getContentResolver().query(uri, null, null, null, null)) {
            if (cursor != null && cursor.moveToFirst()) {
                int index = cursor.getColumnIndex(android.provider.OpenableColumns.DISPLAY_NAME);
                if (index >= 0) return cursor.getString(index);
            }
        } catch (Exception ignored) { }
        return "mGameInfo.xml";
    }

    private void copyLimited(InputStream in, OutputStream out) throws Exception {
        byte[] buffer = new byte[65536];
        long total = 0;
        int count;
        while ((count = in.read(buffer)) != -1) {
            total += count;
            if (total > MAX_SIZE) throw new IllegalStateException("File vượt 64 MB");
            out.write(buffer, 0, count);
        }
        out.flush();
    }

    private static String quoteShell(String str) {
        return "'" + str.replace("'", "'\\''") + "'";
    }

    /** Read-only. Never writes to another application's /data/data directory. */
    private void importRoot(int id, JSONObject params) {
        try {
            String packageId = params.optString("package", "com.playrix.township.vn");
            if (!packageId.equals("com.playrix.township.vn") && !packageId.equals("com.playrix.township")) {
                throw new SecurityException("Package không được hỗ trợ");
            }
            String path = "/data/data/" + packageId + "/saves/mGameInfo.xml";
            File dest = new File(getFilesDir(), "input_from_root.bin");
            Process root = new ProcessBuilder("su", "-c", "cat " + quoteShell(path)).start();
            // A delayed root-grant dialog must not leave the worker waiting forever.
            Thread watchdog = new Thread(() -> {
                try {
                    Thread.sleep(20000);
                    if (root.isAlive()) root.destroyForcibly();
                } catch (InterruptedException ignored) { }
            }, "root-read-watchdog");
            watchdog.setDaemon(true);
            watchdog.start();
            try (InputStream input = root.getInputStream();
                 OutputStream output = new FileOutputStream(dest)) {
                copyLimited(input, output);
            }
            if (!root.waitFor(15, TimeUnit.SECONDS)) {
                root.destroyForcibly();
                throw new IllegalStateException("ROOT hết thời gian phản hồi");
            }
            watchdog.interrupt();
            if (root.exitValue() != 0 || dest.length() == 0) {
                throw new IllegalStateException("Không thể đọc save; kiểm tra ROOT và đường dẫn trò chơi");
            }
            JSONObject args = new JSONObject();
            args.put("path", dest.getCanonicalPath());
            args.put("name", "mGameInfo.xml");
            args.put("origin", "root-read:" + packageId);
            rootPackage = packageId;
            send(id, execute("import", args));
        } catch (Exception e) { error(id, e.getMessage()); }
    }

    private static String allowedPackage(String value) {
        if (!"com.playrix.township.vn".equals(value) && !"com.playrix.township".equals(value))
            throw new SecurityException("Package Township không hợp lệ");
        return value;
    }

    private String runRoot(String command) throws Exception {
        Process process = new ProcessBuilder("su", "-c", command).redirectErrorStream(true).start();
        StringBuilder output = new StringBuilder();
        Thread reader = new Thread(() -> {
            try (InputStream stream = process.getInputStream()) {
                byte[] buf = new byte[2048]; int n;
                while ((n = stream.read(buf)) != -1 && output.length() < 16000)
                    output.append(new String(buf, 0, n, StandardCharsets.UTF_8));
            } catch (Exception ignored) {}
        });
        reader.setDaemon(true); reader.start();
        if (!process.waitFor(35, TimeUnit.SECONDS)) {
            process.destroyForcibly(); throw new IllegalStateException("ROOT không phản hồi trong 35 giây");
        }
        reader.join(1000);
        if (process.exitValue() != 0) throw new IllegalStateException("Lệnh ROOT thất bại: " + output);
        return output.toString();
    }

    /** Explicit user-confirmed apply with backup, stop, atomic replacement and verification. */
    private void applyRoot(int id, JSONObject params) {
        try {
            String pkg = allowedPackage(params.optString("package", rootPackage));
            if (!pkg.equals(rootPackage))
                throw new IllegalStateException("Package đích khác với package đã đọc. Hãy đọc lại ROOT trước.");
            JSONObject state = new JSONObject(execute("state", new JSONObject())).getJSONObject("result").getJSONObject("state");
            if (!state.optBoolean("loaded") || !state.optString("origin").equals("root-read:" + pkg))
                throw new IllegalStateException("Phải đọc save trực tiếp từ đúng package ROOT trước khi ghi");
            if (!params.optBoolean("confirmed")) throw new SecurityException("Chưa xác nhận ghi vào game");
            JSONObject export = new JSONObject(execute("export", new JSONObject().put("mode", "standalone"))).getJSONObject("result");
            File encoded = new File(export.getString("path"));
            if (!encoded.isFile() || encoded.length() == 0 || encoded.length() > MAX_SIZE)
                throw new IllegalStateException("Save mã hóa không hợp lệ");
            String path = "/data/data/" + pkg + "/saves/mGameInfo.xml";
            String staged = "/data/local/tmp/tsstudio_" + android.os.Process.myPid() + ".bin";
            String backup = "/data/data/" + pkg + "/saves/mGameInfo.xml.tsstudio.bak";
            // First check target and get original checksum, before any write.
            String original = runRoot("test -f " + quoteShell(path) + " && sha256sum " + quoteShell(path));
            String originalHash = original.trim().split("\\s+")[0];
            // Root read on import is cached: prevent overwriting a save changed since import.
            File imported = new File(getFilesDir(), "input_from_root.bin");
            if (!imported.isFile()) throw new IllegalStateException("Thiếu bản save ROOT đã đọc");
            String importedHash = sha256(imported);
            if (!originalHash.equalsIgnoreCase(importedHash))
                throw new IllegalStateException("Save trong game đã thay đổi từ lúc đọc. Hãy đọc lại ROOT trước khi Apply.");
            // Stage in app storage, root copies into same directory for atomic rename.
            String source = encoded.getCanonicalPath();
            String temp = path + ".tsstudio.tmp";
            String cmd = "set -e; am force-stop " + quoteShell(pkg)
                + "; test -f " + quoteShell(path)
                + "; test "$(sha256sum " + quoteShell(path) + " | cut -d  -f1)" = " + quoteShell(importedHash)
                + "; cp -p " + quoteShell(path) + " " + quoteShell(backup)
                + "; cp " + quoteShell(source) + " " + quoteShell(temp)
                + "; chown --reference=" + quoteShell(path) + " " + quoteShell(temp)
                + "; chmod --reference=" + quoteShell(path) + " " + quoteShell(temp)
                + "; (chcon --reference=" + quoteShell(path) + " " + quoteShell(temp) + " || restorecon " + quoteShell(temp) + ")"
                + "; mv -f " + quoteShell(temp) + " " + quoteShell(path)
                + "; test "$(sha256sum " + quoteShell(path) + " | cut -d  -f1)" = " + quoteShell(sha256(encoded));
            runRoot(cmd);
            JSONObject result = new JSONObject().put("ok", true).put("result", new JSONObject()
                .put("package", pkg).put("path", path).put("backup", backup)
                .put("bytes", encoded.length()).put("verified", true));
            send(id, result.toString());
        } catch (Exception e) { error(id, e.getMessage()); }
    }

    private static String sha256(File file) throws Exception {
        java.security.MessageDigest digest = java.security.MessageDigest.getInstance("SHA-256");
        try (InputStream in = new FileInputStream(file)) {
            byte[] buffer = new byte[65536]; int n;
            while ((n = in.read(buffer)) != -1) digest.update(buffer, 0, n);
        }
        StringBuilder result = new StringBuilder();
        for (byte b : digest.digest()) result.append(String.format(java.util.Locale.ROOT, "%02x", b & 255));
        return result.toString();
    }

    @Override protected void onDestroy() {
        if (web != null) { web.removeJavascriptInterface("TSNative"); web.destroy(); web = null; }
        executor.shutdownNow();
        super.onDestroy();
    }
}
