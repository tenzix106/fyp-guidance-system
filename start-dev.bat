@echo off
echo Starting FYP Guidance System Development Environment
echo.

echo Starting Flask Backend Server...
start "Flask Backend" cmd /k "cd backend && python app.py"

timeout /t 3 /nobreak > nul

echo Starting Vue.js + PrimeVue Frontend Server...
start "Vue Frontend" cmd /k "npm run dev"

echo.
echo Both servers are starting up...
echo Backend: http://localhost:5000
echo Frontend: http://localhost:8080
echo.
pause
