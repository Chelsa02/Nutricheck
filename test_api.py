#!/usr/bin/env python3
"""
Test script to check Hugging Face API response
"""
import json
import urllib.request
import sys

HF_API_TOKEN = ""  # Set if you have token
HF_MODEL_URL = "https://api-inference.huggingface.co/models/microsoft/resnet-50"

# Test with a simple apple image URL
test_image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/800px-Red_Apple.jpg"

try:
    print("📥 Downloading test image...")
    with urllib.request.urlopen(test_image_url) as response:
        image_bytes = response.read()
    
    print(f"✅ Image size: {len(image_bytes)} bytes")
    print("📤 Sending to Hugging Face API...")
    
    headers = {'Content-Type': 'application/octet-stream'}
    if HF_API_TOKEN:
        headers['Authorization'] = f'Bearer {HF_API_TOKEN}'
    
    req = urllib.request.Request(
        HF_MODEL_URL,
        data=image_bytes,
        headers=headers,
        method='POST'
    )
    
    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode())
    
    print("✅ API Response:")
    print(json.dumps(result, indent=2))
    
    if isinstance(result, list) and len(result) > 0:
        top_result = result[0]
        print(f"\n🍎 Top match: {top_result.get('label')} ({top_result.get('score')*100:.1f}% confident)")
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nNote: Free tier might be rate limited. If error, either:")
    print("1. Get a free Hugging Face token from https://huggingface.co/settings/tokens")
    print("2. Set HF_API_TOKEN environment variable")
    print("3. Wait a minute and try again")
