"""
NutriCheck Backend - Lightweight Hugging Face Integration
Pure Python stdlib - no heavy dependencies needed!
"""
import json
import urllib.request
import sys
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

HF_API_TOKEN = os.getenv("HF_API_TOKEN", "")
HF_MODEL_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"

# Nutrition database
NUTRITION_DB = {
    'pizza': {'cal': 580, 'protein': 24, 'carbs': 58, 'fat': 28},
    'burger': {'cal': 540, 'protein': 28, 'carbs': 44, 'fat': 24},
    'salad': {'cal': 420, 'protein': 35, 'carbs': 18, 'fat': 22},
    'chicken': {'cal': 350, 'protein': 42, 'carbs': 0, 'fat': 18},
    'rice': {'cal': 380, 'protein': 8, 'carbs': 68, 'fat': 6},
    'pasta': {'cal': 520, 'protein': 18, 'carbs': 62, 'fat': 26},
    'fish': {'cal': 450, 'protein': 42, 'carbs': 24, 'fat': 16},
    'salmon': {'cal': 450, 'protein': 42, 'carbs': 24, 'fat': 16},
    'steak': {'cal': 480, 'protein': 50, 'carbs': 0, 'fat': 28},
    'oats': {'cal': 380, 'protein': 12, 'carbs': 52, 'fat': 14},
    'apple': {'cal': 95, 'protein': 0, 'carbs': 25, 'fat': 0},
    'sandwich': {'cal': 420, 'protein': 22, 'carbs': 48, 'fat': 16},
    'taco': {'cal': 520, 'protein': 24, 'carbs': 46, 'fat': 24},
    'soup': {'cal': 280, 'protein': 18, 'carbs': 32, 'fat': 8},
    'sushi': {'cal': 320, 'protein': 14, 'carbs': 42, 'fat': 8},
}

def match_nutrition(food_label):
    """Find best matching nutrition"""
    label_lower = food_label.lower()
    
    if label_lower in NUTRITION_DB:
        return NUTRITION_DB[label_lower], label_lower
    
    matches = [(k, len(k)) for k in NUTRITION_DB if k in label_lower]
    if matches:
        best_match = max(matches, key=lambda x: x[1])[0]
        return NUTRITION_DB[best_match], best_match
    
    return {'cal': 350, 'protein': 25, 'carbs': 35, 'fat': 15}, label_lower

def analyze_image(image_bytes):
    """Call Hugging Face API"""
    try:
        headers = {'Content-Type': 'application/octet-stream'}
        if HF_API_TOKEN:
            headers['Authorization'] = f'Bearer {HF_API_TOKEN}'
        
        req = urllib.request.Request(HF_MODEL_URL, data=image_bytes, headers=headers, method='POST')
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode())
        
        if isinstance(result, dict) and 'error' in result:
            return None
        
        return result[0] if isinstance(result, list) and len(result) > 0 else None
    except Exception as e:
        print(f"API Error: {e}")
        return None

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/api/recognize':
            content_length = int(self.headers.get('Content-Length', 0))
            image_data = self.rfile.read(content_length) if content_length > 0 else b''
            
            result = analyze_image(image_data)
            
            if result:
                food_label = result.get('label', 'Food')
                confidence = result.get('score', 0)
                nutrition, matched_food = match_nutrition(food_label)
                response = {
                    'name': food_label.title(),
                    'confidence': round(confidence * 100, 1),
                    'cal': nutrition['cal'],
                    'protein': nutrition['protein'],
                    'carbs': nutrition['carbs'],
                    'fat': nutrition['fat'],
                    'matched_food': matched_food,
                    'fallback': False
                }
            else:
                response = {
                    'name': 'Healthy Meal',
                    'confidence': 0,
                    'cal': 400,
                    'protein': 25,
                    'carbs': 40,
                    'fat': 15,
                    'matched_food': 'meal',
                    'fallback': True
                }
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        
        elif self.path == '/api/health':
            response = {'status': 'ok', 'model': 'ResNet-50', 'token_set': bool(HF_API_TOKEN)}
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        print(f"[{self.client_address[0]}] {format % args}")

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    print("🍽️ NutriCheck Backend Ready!")
    print(f"📍 Server: http://localhost:{port}")
    print(f"🤖 Using Hugging Face Inference API (cloud-based)")
    print(f"🔑 Token set: {bool(HF_API_TOKEN)}")
    print("Ready for image uploads!\n")
    
    server = HTTPServer(('0.0.0.0', port), RequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n✅ Server stopped")
        server.server_close()
