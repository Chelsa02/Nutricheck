@echo off
echo 🍽️ Starting NutriCheck Backend with Hugging Face AI...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo ✅ Starting server on http://localhost:5000
echo.
echo (Optional) Set Hugging Face token for unlimited requests:
echo set HF_API_TOKEN=your_token_here
echo.
echo Without token: Uses free tier with rate limiting (still works!)
echo.
python server.py
pause
