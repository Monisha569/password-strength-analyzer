@echo off

cd /d "%~dp0"

echo Starting Password Strength Analyzer...
echo.

start "Flask Server" cmd /k ""%~dp0venv\Scripts\python.exe" "%~dp0app.py""

timeout /t 4 /nobreak >nul

echo Opening Chrome...

start "" "http://127.0.0.1:5000"

exit