"""
Hugging Face Food Recognition Backend
Uses transformers library to identify food from images
"""
from flask import Flask, request, jsonify
from transformers import pipeline
from PIL import Image
import io
import base64
import os

app = Flask(__name__)

# Initialize the food classification model
# Using "microsoft/resnet-50" fine-tuned on Food-101 dataset
print("Loading Hugging Face model... (first run takes ~1-2 min)")
classifier = pipeline("image-classification", model="microsoft/resnet-50")

# Nutrition database mapping food names to nutrition info
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
    """Find best matching nutrition data for food label"""
    label_lower = food_label.lower()
    
    # Exact match
    if label_lower in NUTRITION_DB:
        return NUTRITION_DB[label_lower], label_lower
    
    # Partial match (prioritize longest match)
    matches = []
    for key in NUTRITION_DB:
        if key in label_lower:
            matches.append((key, len(key)))
    
    if matches:
        best_match = max(matches, key=lambda x: x[1])[0]
        return NUTRITION_DB[best_match], best_match
    
    # Default if no match
    return {'cal': 350, 'protein': 25, 'carbs': 35, 'fat': 15}, label_lower

@app.route('/api/recognize', methods=['POST'])
def recognize_food():
    """Analyze food image using Hugging Face"""
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read and process image
        image_data = file.read()
        image = Image.open(io.BytesIO(image_data))
        
        # Resize for faster processing
        image.thumbnail((512, 512))
        
        # Use Hugging Face to classify
        results = classifier(image)
        
        if not results:
            return jsonify({'error': 'Could not analyze image'}), 400
        
        # Get top result
        top_result = results[0]
        food_label = top_result['label']
        confidence = top_result['score']
        
        # Get nutrition data
        nutrition, matched_food = match_nutrition(food_label)
        
        return jsonify({
            'name': food_label.title(),
            'confidence': round(confidence * 100, 1),
            'cal': nutrition['cal'],
            'protein': nutrition['protein'],
            'carbs': nutrition['carbs'],
            'fat': nutrition['fat'],
            'matched_food': matched_food
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'model': 'Hugging Face ResNet-50'})

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
