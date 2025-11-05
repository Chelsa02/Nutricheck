@echo off
echo 🍽️ Starting NutriCheck Backend with Hugging Face AI...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo ✅ Starting server on http://localhost:5000
echo.
echo First run will download the AI model (~350MB, takes 1-2 minutes)
echo.
python server.py
pause
