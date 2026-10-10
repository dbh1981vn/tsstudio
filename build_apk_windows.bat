@echo off
setlocal EnableExtensions DisableDelayedExpansion
cd /d "%~dp0"
set "ROOT=%CD%"
set "GRADLE_VERSION=8.10.2"
set "GRADLE_CACHE=%USERPROFILE%\.tsstudio-build"
set "GRADLE_DIR=%GRADLE_CACHE%\gradle-%GRADLE_VERSION%"
set "GRADLE_EXE=%GRADLE_DIR%\bin\gradle.bat"

echo.
echo === TS Studio Android 2.0 Alpha 1 : DEBUG APK ===
echo.
if not defined ANDROID_HOME if exist "%LOCALAPPDATA%\Android\Sdk" set "ANDROID_HOME=%LOCALAPPDATA%\Android\Sdk"
if not defined JAVA_HOME if exist "%ProgramFiles%\Android\Android Studio\jbr\bin\java.exe" set "JAVA_HOME=%ProgramFiles%\Android\Android Studio\jbr"
if not defined ANDROID_HOME (
    echo [ERROR] Khong tim thay Android SDK. Hay cai Android Studio + SDK Platform 35.
    pause
    exit /b 1
)
if not exist "%ANDROID_HOME%\platforms\android-35\android.jar" (
    echo [ERROR] Thieu SDK Platform 35 tai: %ANDROID_HOME%
    pause
    exit /b 1
)
if not exist "%GRADLE_EXE%" (
    echo [INFO] Tai Gradle 8.10.2 vao thu muc local. Can Internet.
    if not exist "%GRADLE_CACHE%" mkdir "%GRADLE_CACHE%"
    powershell -NoProfile -ExecutionPolicy Bypass -Command "$ErrorActionPreference='Stop'; $zip=Join-Path $env:GRADLE_CACHE 'gradle-8.10.2-bin.zip'; Invoke-WebRequest 'https://services.gradle.org/distributions/gradle-8.10.2-bin.zip' -OutFile $zip; Expand-Archive -Path $zip -DestinationPath $env:GRADLE_CACHE -Force" 
    if errorlevel 1 (
        echo [ERROR] Khong tai duoc Gradle. Kiem tra mang va chay lai.
        pause
        exit /b 1
    )
)
if not exist "%GRADLE_EXE%" (
    echo [ERROR] Gradle thieu sau khi tai.
    pause
    exit /b 1
)
echo [INFO] SDK=%ANDROID_HOME%
if defined JAVA_HOME echo [INFO] JDK=%JAVA_HOME%
echo [INFO] Can Python 3.11 trong PATH de Chaquopy xay dung pip packages.
call "%GRADLE_EXE%" --no-daemon --stacktrace assembleDebug
if errorlevel 1 (
    echo.
    echo [ERROR] Build that bai. Kiem tra JDK17 / Python3.11 / SDK35 / Internet.
    pause
    exit /b 1
)
set "OUTPUT=%ROOT%\app\build\outputs\apk\debug\app-debug.apk"
if not exist "%OUTPUT%" (
    echo [ERROR] Gradle da xong nhung khong tim thay APK.
    pause
    exit /b 1
)
if not exist "%ROOT%\dist" mkdir "%ROOT%\dist"
copy /y "%OUTPUT%" "%ROOT%\dist\TS_Studio_Android_v2.0_alpha1-debug.apk" >nul
echo.
echo [OK] Da tao APK: "%ROOT%\dist\TS_Studio_Android_v2.0_alpha1-debug.apk"
echo.
pause
