@echo off
for /f  "tokens=2 delims= " %%i in ('getpid.bat') do set pid=%%i
echo %pid%
adb logcat | find  "%pid%"
pause