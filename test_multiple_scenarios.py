#!/usr/bin/env python3
"""
Test multiple chatbot scenarios
"""

import requests
import json

def test_scenario(message, expected_keywords):
    """Test a specific scenario"""
    print(f"\n🧪 Testing: '{message}'")
    
    url = "http://localhost:8000/api/gemini-chat/"
    test_data = {
        "message": message,
        "conversation_history": []
    }
    
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
        
        response = session.post(url, json=test_data, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                response_text = data.get('response', '')
                print(f"✅ Response: {response_text[:150]}...")
                
                # Check if expected keywords are in response
                for keyword in expected_keywords:
                    if keyword.lower() in response_text.lower():
                        print(f"✅ Contains expected keyword: '{keyword}'")
                    else:
                        print(f"⚠️ Missing expected keyword: '{keyword}'")
                
                return True
            else:
                print(f"❌ API Error: {data.get('error')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def main():
    """Test multiple scenarios"""
    print("🚀 Testing Multiple Chatbot Scenarios...")
    
    scenarios = [
        {
            "message": "I'm feeling really anxious about my upcoming exams",
            "expected": ["anxiety", "breathing", "techniques", "counseling"]
        },
        {
            "message": "I've been feeling really depressed lately",
            "expected": ["depression", "support", "counseling", "professional"]
        },
        {
            "message": "I'm stressed about my relationships",
            "expected": ["relationship", "communication", "support", "counseling"]
        },
        {
            "message": "I can't sleep because I'm worried",
            "expected": ["sleep", "hygiene", "relaxation", "counseling"]
        },
        {
            "message": "I don't want to live anymore",
            "expected": ["crisis", "helpline", "emergency", "911"]
        },
        {
            "message": "What's the weather like?",
            "expected": ["mental health", "support", "anxiety", "depression"]
        }
    ]
    
    passed = 0
    total = len(scenarios)
    
    for scenario in scenarios:
        if test_scenario(scenario["message"], scenario["expected"]):
            passed += 1
    
    print(f"\n📊 Results: {passed}/{total} scenarios passed")
    
    if passed == total:
        print("🎉 All scenarios working correctly!")
    else:
        print("⚠️ Some scenarios need attention")

if __name__ == "__main__":
    main()
