@echo off
:: AI Vision Pro - Windows Quick Start
:: Double-click to run everything!

echo ============================================
echo     AI Vision Pro - Quick Start
echo ============================================
echo.

:: Activate virtual environment
if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    echo [OK] Virtual environment activated
) else (
    echo [INFO] Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [OK] Installing dependencies...
    pip install -r requirements_enhanced.txt
)

echo.
echo ============================================
echo Starting AI Vision Pro...
echo ============================================
echo.
echo This will open multiple windows:
echo   - Backend API (Port 8000)
echo   - Web App (Port 8501)
echo.

:: Start Backend in new window
start "Backend API" cmd /k "call venv\Scripts\activate.bat && python backend\main.py"

:: Wait for backend to start
echo [INFO] Starting backend (waiting 5 seconds)...
timeout /t 5 /nobreak > nul

:: Start Web App in new window
start "Web App" cmd /k "call venv\Scripts\activate.bat && streamlit run web_app_enhanced\main.py"

echo.
echo ============================================
echo All services started!
echo ============================================
echo.
echo Web App: http://localhost:8501
echo API Docs: http://localhost:8000/docs
echo.
echo Press any key to stop all services...
pause > nul

:: Kill all Python processes (optional cleanup)
echo Stopping services...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM pythonw.exe 2>nul

echo.
echo All services stopped.
pause
