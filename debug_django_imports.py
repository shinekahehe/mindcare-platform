#!/usr/bin/env python3
"""
Debug Django imports and environment
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

def test_imports():
    """Test various imports"""
    print("🔍 Testing imports in Django environment...")
    
    try:
        import google.generativeai as genai
        print("✅ google.generativeai imported successfully")
    except ImportError as e:
        print(f"❌ google.generativeai import failed: {e}")
    
    try:
        from dotenv import load_dotenv
        print("✅ python-dotenv imported successfully")
    except ImportError as e:
        print(f"❌ python-dotenv import failed: {e}")
    
    try:
        from gemini_config import generate_mental_health_response, is_mental_health_related
        print("✅ gemini_config imported successfully")
    except ImportError as e:
        print(f"❌ gemini_config import failed: {e}")
    
    try:
        from base.views import gemini_chat_api
        print("✅ gemini_chat_api imported successfully")
    except ImportError as e:
        print(f"❌ gemini_chat_api import failed: {e}")
    
    # Test the actual function
    try:
        from gemini_config import is_mental_health_related
        result = is_mental_health_related("I'm feeling anxious")
        print(f"✅ is_mental_health_related test: {result}")
    except Exception as e:
        print(f"❌ is_mental_health_related test failed: {e}")

if __name__ == "__main__":
    test_imports()
