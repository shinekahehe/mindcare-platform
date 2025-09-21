#!/usr/bin/env python3
"""
Debug script to check environment variables on Render
"""

import os
import sys

def debug_environment():
    print("🔍 ENVIRONMENT VARIABLE DEBUG")
    print("=" * 50)
    
    # Check if we're in production
    is_production = bool(os.getenv("RENDER") or os.getenv("DYNO") or os.getenv("RAILWAY_ENVIRONMENT"))
    print(f"Environment: {'PRODUCTION' if is_production else 'LOCAL DEVELOPMENT'}")
    print(f"RENDER env var: {os.getenv('RENDER', 'NOT SET')}")
    print()
    
    # Check all environment variables
    env_vars = {
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY'),
        'SUPABASE_URL': os.getenv('SUPABASE_URL'),
        'SUPABASE_ANON_KEY': os.getenv('SUPABASE_ANON_KEY'),
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'DEBUG': os.getenv('DEBUG'),
        'ALLOWED_HOSTS': os.getenv('ALLOWED_HOSTS'),
    }
    
    print("📋 ENVIRONMENT VARIABLES:")
    print("-" * 30)
    
    for key, value in env_vars.items():
        if value:
            if 'KEY' in key or 'URL' in key:
                # Mask sensitive values
                masked = value[:10] + "..." + value[-4:] if len(value) > 14 else "***"
                print(f"✅ {key}: {masked}")
            else:
                print(f"✅ {key}: {value}")
        else:
            print(f"❌ {key}: NOT SET")
    
    print()
    
    # Test Django settings
    try:
        import django
        from pathlib import Path
        
        # Add project root to Python path
        project_root = Path(__file__).resolve().parent
        sys.path.insert(0, str(project_root))
        
        # Set Django settings
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
        
        # Initialize Django
        django.setup()
        
        from django.conf import settings
        
        print("🔧 DJANGO SETTINGS:")
        print("-" * 20)
        print(f"✅ GEMINI_API_KEY: {'SET' if settings.GEMINI_API_KEY else 'NOT SET'}")
        print(f"✅ SUPABASE_URL: {'SET' if settings.SUPABASE_URL else 'NOT SET'}")
        print(f"✅ DEBUG: {settings.DEBUG}")
        print(f"✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        
    except Exception as e:
        print(f"❌ Django setup failed: {e}")

if __name__ == "__main__":
    debug_environment()
