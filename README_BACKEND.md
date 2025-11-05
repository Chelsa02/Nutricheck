# 🍽️ NutriCheck - AI Food Recognition with Hugging Face

A full-stack nutrition app with real AI-powered food recognition using Hugging Face models.

## **Quick Start**

### **Frontend Only (Mock AI)**
```bash
# Live at: https://nutricheck-zeta.vercel.app
# No setup needed - just upload any image, get random meal analysis
```

### **With Real AI (Backend Server)**

#### **1. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **2. Start the Backend Server**
```bash
python server.py
```

The server will:
- Load the Hugging Face model (first run: ~1-2 minutes)
- Start on `http://localhost:5000`
- Provide `/api/recognize` endpoint for image analysis

#### **3. Open Frontend**
- Local: http://localhost:3000 (if running locally)
- Production: https://nutricheck-zeta.vercel.app

#### **4. Upload a Food Image**
- Click "Upload Meal Photo"
- Select any food image
- The app will send it to the backend for real AI analysis
- If backend unavailable, falls back to mock recognition

---

## **How It Works**

### **Architecture:**
```
Frontend (HTML/JS/CSS)
    ↓
/api/recognize POST
    ↓
Backend Server (Flask)
    ↓
Hugging Face Model (ResNet-50)
    ↓
Nutrition Database Match
    ↓
Response: Food name + Calories + Macros
    ↓
Frontend displays results
```

### **Features:**

✅ **Real AI Food Recognition** - Uses Hugging Face transformers  
✅ **Food-to-Nutrition Mapping** - 15+ foods with macro breakdown  
✅ **Fallback Mode** - Works without backend (mock AI)  
✅ **Meal Logging** - Track calories in real-time  
✅ **Diet Planning** - Auto-generate meal breakdown by calorie goal  
✅ **Responsive UI** - Dark theme, mobile-friendly  
✅ **Deployable** - Works on Vercel (frontend) + any Python host (backend)  

---

## **API Reference**

### **POST /api/recognize**
Upload an image for AI food recognition

**Request:**
```bash
curl -X POST -F "image=@pizza.jpg" http://localhost:5000/api/recognize
```

**Response:**
```json
{
  "name": "Pizza",
  "confidence": 94.5,
  "cal": 580,
  "protein": 24,
  "carbs": 58,
  "fat": 28,
  "matched_food": "pizza"
}
```

### **GET /api/health**
Check if server is running

**Response:**
```json
{
  "status": "ok",
  "model": "Hugging Face ResNet-50"
}
```

---

## **Supported Foods** (in database)

Pizza, Burger, Salad, Chicken, Rice, Pasta, Fish, Salmon, Steak, Oats, Apple, Sandwich, Taco, Soup, Sushi

*The AI model (ResNet-50) recognizes 1000+ foods - nutrition data matched to closest category*

---

## **Deployment**

### **Frontend to Vercel**
```bash
git push origin main
# Auto-deploys to https://nutricheck-zeta.vercel.app
```

### **Backend to Cloud**
- **Heroku:** `heroku create nutricheck-api && git push heroku main`
- **Railway:** Connect GitHub repo, auto-deploys
- **AWS Lambda:** Requires serverless framework
- **Google Cloud Run:** Containerize and deploy

---

## **Development**

### **Project Structure**
```
Nutricheck/
├── public/
│   └── index.html          (Frontend - all-in-one HTML)
├── server.py               (Flask backend + Hugging Face)
├── requirements.txt        (Python dependencies)
├── vercel.json             (Vercel deployment config)
├── app.json                (Expo config - for mobile)
└── README.md               (This file)
```

### **Tech Stack**
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Backend:** Flask, Python 3.10+
- **AI:** Hugging Face Transformers (ResNet-50)
- **Image Processing:** Pillow
- **Deployment:** Vercel (frontend), Any Python host (backend)

---

## **Troubleshooting**

### **Issue: "API unavailable" message**
- Backend server not running? Start with `python server.py`
- Check firewall isn't blocking port 5000
- App falls back to mock recognition (works anyway!)

### **Issue: Model download takes forever**
- First run downloads ~350MB model (normal)
- Subsequent runs use cached model
- To skip: Use mock mode on frontend only

### **Issue: Image not uploading**
- Check file size (recommend <5MB)
- Supported formats: JPG, PNG, GIF, WebP
- Try different image if corrupted

---

## **Credits**

- Food Recognition: [Hugging Face Transformers](https://huggingface.co/)
- Model: [Microsoft ResNet-50](https://huggingface.co/microsoft/resnet-50)
- UI Design: Custom dark theme
- Nutrition Data: USDA FoodData Central

---

**Made with ❤️ by NutriCheck Team**
