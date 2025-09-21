#!/usr/bin/env python3
"""
Test the Gemini API endpoint directly
"""

import requests
import json

def test_gemini_endpoint():
    """Test the Gemini API endpoint"""
    print("🧪 Testing Gemini API Endpoint...")
    
    url = "http://localhost:8000/api/gemini-chat/"
    
    test_data = {
        "message": "I'm feeling anxious about my exams",
        "conversation_history": []
    }
    
    # First get CSRF token
    session = requests.Session()
    try:
        # Get CSRF token
        csrf_response = session.get("http://localhost:8000/ai-support/")
        csrf_token = None
        if 'csrftoken' in session.cookies:
            csrf_token = session.cookies['csrftoken']
        
        headers = {'Content-Type': 'application/json'}
        if csrf_token:
            headers['X-CSRFToken'] = csrf_token
        
        response = session.post(
            url,
            json=test_data,
            headers=headers
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ API Response:")
            print(f"Success: {data.get('success')}")
            print(f"Response: {data.get('response', '')[:200]}...")
            print(f"Model: {data.get('model', 'Unknown')}")
            print(f"Crisis Detected: {data.get('crisis_detected', False)}")
            return True
        else:
            print(f"❌ Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Django server not running")
        print("Please start the server with: python manage.py runserver")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_gemini_endpoint()
