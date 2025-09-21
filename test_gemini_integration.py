#!/usr/bin/env python3
"""
Test script for Gemini API integration
Run this to verify your Gemini API setup is working correctly
"""

import os
import sys
import django
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

def test_gemini_config():
    """Test Gemini configuration"""
    print("🔧 Testing Gemini Configuration...")
    
    try:
        from gemini_config import GEMINI_AVAILABLE, is_mental_health_related, get_off_topic_response
        
        if GEMINI_AVAILABLE:
            print("✅ Gemini API key found and configured")
        else:
            print("❌ Gemini API key not found. Please set GEMINI_API_KEY in your .env file")
            return False
            
        # Test mental health detection
        mental_health_messages = [
            "I'm feeling anxious about my exams",
            "I've been really depressed lately", 
            "I can't sleep because I'm stressed",
            "I'm having relationship problems"
        ]
        
        non_mental_health_messages = [
            "What's the weather like?",
            "How do I cook pasta?",
            "Tell me about history",
            "What's 2+2?"
        ]
        
        print("\n🧠 Testing Mental Health Detection...")
        for msg in mental_health_messages:
            is_related = is_mental_health_related(msg)
            status = "✅" if is_related else "❌"
            print(f"{status} '{msg}' -> Mental Health Related: {is_related}")
            
        print("\n🚫 Testing Off-Topic Detection...")
        for msg in non_mental_health_messages:
            is_related = is_mental_health_related(msg)
            status = "✅" if not is_related else "❌"
            print(f"{status} '{msg}' -> Off-Topic: {not is_related}")
            
        return True
        
    except ImportError as e:
        print(f"❌ Error importing Gemini config: {e}")
        return False
    except Exception as e:
        print(f"❌ Error testing Gemini config: {e}")
        return False

def test_gemini_api():
    """Test actual Gemini API calls"""
    print("\n🤖 Testing Gemini API Calls...")
    
    try:
        from gemini_config import generate_mental_health_response
        
        # Test mental health query
        test_message = "I'm feeling really anxious about my upcoming exams and I can't focus on studying"
        print(f"📝 Test Message: '{test_message}'")
        
        response = generate_mental_health_response(test_message)
        
        if response.get('error'):
            print(f"❌ API Error: {response['error']}")
            return False
            
        print(f"✅ API Response: {response['text'][:100]}...")
        print(f"📊 Model: {response.get('model', 'Unknown')}")
        print(f"🚨 Safety Flags: {response.get('safety_flags', [])}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing Gemini API: {e}")
        return False

def test_crisis_detection():
    """Test crisis detection functionality"""
    print("\n🚨 Testing Crisis Detection...")
    
    try:
        from gemini_config import generate_mental_health_response
        
        crisis_message = "I'm feeling hopeless and I don't want to live anymore"
        print(f"📝 Crisis Message: '{crisis_message}'")
        
        response = generate_mental_health_response(crisis_message)
        
        if 'crisis_detected' in response.get('safety_flags', []):
            print("✅ Crisis detection working correctly")
            print(f"📞 Crisis resources provided: {'CRISIS SUPPORT' in response['text']}")
        else:
            print("⚠️ Crisis detection may need adjustment")
            
        return True
        
    except Exception as e:
        print(f"❌ Error testing crisis detection: {e}")
        return False

def test_django_integration():
    """Test Django API endpoint"""
    print("\n🌐 Testing Django Integration...")
    
    try:
        from django.test import Client
        from django.urls import reverse
        import json
        
        client = Client()
        
        # Test data
        test_data = {
            'message': 'I need help with anxiety',
            'conversation_history': []
        }
        
        # Make API call
        response = client.post(
            '/api/gemini-chat/',
            data=json.dumps(test_data),
            content_type='application/json'
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                print("✅ Django API endpoint working")
                print(f"📝 Response: {data['response'][:100]}...")
                return True
            else:
                print(f"❌ API returned error: {data.get('error')}")
                return False
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Django integration: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Gemini Integration Tests...\n")
    
    tests = [
        ("Configuration", test_gemini_config),
        ("API Calls", test_gemini_api),
        ("Crisis Detection", test_crisis_detection),
        ("Django Integration", test_django_integration)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running {test_name} Test")
        print('='*50)
        
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print(f"\n{'='*50}")
    print("TEST SUMMARY")
    print('='*50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Gemini integration is working correctly.")
        print("\nNext steps:")
        print("1. Start your Django server: python manage.py runserver")
        print("2. Navigate to the AI Support page")
        print("3. Test the chatbot with mental health queries")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")
        print("\nTroubleshooting:")
        print("1. Ensure GEMINI_API_KEY is set in your .env file")
        print("2. Verify your API key is valid at https://aistudio.google.com/")
        print("3. Check your internet connection")
        print("4. Review the GEMINI_SETUP_GUIDE.md for detailed instructions")

if __name__ == "__main__":
    main()
