#!/usr/bin/env python3
"""
Simple test script to check environment variables on Render
"""

import os

def test_environment():
    print("🔍 TESTING ENVIRONMENT VARIABLES ON RENDER")
    print("=" * 50)
    
    # Check if we're on Render
    is_render = bool(os.getenv("RENDER"))
    print(f"Running on Render: {is_render}")
    print(f"RENDER env var: {os.getenv('RENDER', 'NOT SET')}")
    print()
    
    # Test environment variables
    env_vars = {
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY'),
        'SUPABASE_URL': os.getenv('SUPABASE_URL'),
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'DEBUG': os.getenv('DEBUG'),
        'ALLOWED_HOSTS': os.getenv('ALLOWED_HOSTS'),
    }
    
    print("📋 ENVIRONMENT VARIABLES:")
    print("-" * 30)
    
    for key, value in env_vars.items():
        if value:
            if 'KEY' in key or 'URL' in key:
                # Show first 10 and last 4 characters
                masked = value[:10] + "..." + value[-4:] if len(value) > 14 else "***"
                print(f"✅ {key}: {masked}")
            else:
                print(f"✅ {key}: {value}")
        else:
            print(f"❌ {key}: NOT SET")
    
    print()
    
    # Test Gemini API key specifically
    gemini_key = os.getenv('GEMINI_API_KEY')
    if gemini_key:
        print(f"✅ GEMINI_API_KEY found: {gemini_key[:10]}...{gemini_key[-4:]}")
        print(f"✅ Key length: {len(gemini_key)} characters")
        
        # Test if it starts with the expected prefix
        if gemini_key.startswith('AIzaSy'):
            print("✅ Key format looks correct (starts with AIzaSy)")
        else:
            print("⚠️ Key format might be incorrect")
    else:
        print("❌ GEMINI_API_KEY not found!")
    
    print()
    print("🎯 SUMMARY:")
    print(f"  - Render environment: {'YES' if is_render else 'NO'}")
    print(f"  - Gemini API key: {'SET' if gemini_key else 'NOT SET'}")
    print(f"  - Supabase URL: {'SET' if os.getenv('SUPABASE_URL') else 'NOT SET'}")
    print(f"  - Database URL: {'SET' if os.getenv('DATABASE_URL') else 'NOT SET'}")

if __name__ == "__main__":
    test_environment()