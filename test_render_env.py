#!/usr/bin/env python3
"""
Test script to check if environment variables are accessible from Render
Run this locally first, then deploy and run on Render
"""

import os
import sys
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_environment_variables():
    """Test if environment variables are accessible"""
    print("🔍 TESTING ENVIRONMENT VARIABLES")
    print("=" * 50)
    
    # Check if we're in production
    is_production = bool(os.getenv("RENDER") or os.getenv("DYNO") or os.getenv("RAILWAY_ENVIRONMENT"))
    print(f"Environment: {'PRODUCTION' if is_production else 'LOCAL DEVELOPMENT'}")
    print()
    
    # Test environment variables
    env_vars = {
        'DJANGO_SECRET_KEY': os.getenv('DJANGO_SECRET_KEY'),
        'SECRET_KEY': os.getenv('SECRET_KEY'),
        'DEBUG': os.getenv('DEBUG'),
        'ALLOWED_HOSTS': os.getenv('ALLOWED_HOSTS'),
        'DATABASE_URL': os.getenv('DATABASE_URL'),
        'SUPABASE_URL': os.getenv('SUPABASE_URL'),
        'SUPABASE_ANON_KEY': os.getenv('SUPABASE_ANON_KEY'),
        'SUPABASE_SERVICE_ROLE_KEY': os.getenv('SUPABASE_SERVICE_ROLE_KEY'),
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY'),
    }
    
    print("📋 ENVIRONMENT VARIABLES STATUS:")
    print("-" * 40)
    
    for var_name, var_value in env_vars.items():
        if var_value:
            # Mask sensitive values
            if 'KEY' in var_name or 'SECRET' in var_name:
                masked_value = var_value[:8] + "..." + var_value[-4:] if len(var_value) > 12 else "***"
                print(f"✅ {var_name}: {masked_value}")
            else:
                print(f"✅ {var_name}: {var_value}")
        else:
            print(f"❌ {var_name}: NOT SET")
    
    print()
    
    # Test Django settings
    print("🔧 DJANGO SETTINGS STATUS:")
    print("-" * 30)
    
    try:
        print(f"✅ SECRET_KEY: {'SET' if settings.SECRET_KEY else 'NOT SET'}")
        print(f"✅ DEBUG: {settings.DEBUG}")
        print(f"✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        print(f"✅ DATABASE ENGINE: {settings.DATABASES['default']['ENGINE']}")
        print(f"✅ SUPABASE_URL: {'SET' if settings.SUPABASE_URL else 'NOT SET'}")
        print(f"✅ GEMINI_API_KEY: {'SET' if settings.GEMINI_API_KEY else 'NOT SET'}")
    except Exception as e:
        print(f"❌ Error accessing Django settings: {e}")
    
    print()
    
    # Test database connection
    print("🗄️ DATABASE CONNECTION TEST:")
    print("-" * 30)
    
    try:
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ Database connection: SUCCESS")
            print(f"✅ Database engine: {settings.DATABASES['default']['ENGINE']}")
    except Exception as e:
        print(f"❌ Database connection: FAILED - {e}")
    
    print()
    
    # Test Supabase connection
    print("🔗 SUPABASE CONNECTION TEST:")
    print("-" * 30)
    
    try:
        from supabase_config import get_supabase_client
        if settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY:
            supabase = get_supabase_client()
            # Simple test query
            result = supabase.table('base_userprofile').select('id').limit(1).execute()
            print(f"✅ Supabase connection: SUCCESS")
        else:
            print(f"❌ Supabase connection: NOT CONFIGURED")
    except Exception as e:
        print(f"❌ Supabase connection: FAILED - {e}")
    
    print()
    
    # Test Gemini API
    print("🤖 GEMINI API TEST:")
    print("-" * 20)
    
    try:
        from gemini_config import GEMINI_AVAILABLE
        if GEMINI_AVAILABLE:
            print(f"✅ Gemini API: CONFIGURED")
        else:
            print(f"❌ Gemini API: NOT CONFIGURED")
    except Exception as e:
        print(f"❌ Gemini API: ERROR - {e}")
    
    print()
    print("🎯 SUMMARY:")
    print("=" * 20)
    
    # Count configured services
    configured_count = 0
    total_count = 3
    
    if settings.DATABASES['default']['ENGINE'] != 'django.db.backends.sqlite3':
        configured_count += 1
        print("✅ Database: PostgreSQL configured")
    else:
        print("⚠️ Database: Using SQLite (local development)")
    
    if settings.SUPABASE_URL:
        configured_count += 1
        print("✅ Supabase: Configured")
    else:
        print("❌ Supabase: Not configured")
    
    if settings.GEMINI_API_KEY:
        configured_count += 1
        print("✅ Gemini API: Configured")
    else:
        print("❌ Gemini API: Not configured")
    
    print(f"\n📊 Configuration Status: {configured_count}/{total_count} services configured")
    
    if is_production and configured_count < total_count:
        print("\n⚠️ WARNING: Some services not configured in production!")
        print("Please check your Render environment variables.")
    elif not is_production:
        print("\n💡 INFO: Running in local development mode.")
        print("This is expected for local testing.")

if __name__ == "__main__":
    test_environment_variables()
