#!/usr/bin/env python
"""
Test script to verify Supabase integration
Run this script to test your Supabase connection and configuration
"""

import os
import sys
import django
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from supabase_config import get_supabase_client, get_supabase_admin_client
from django.conf import settings

def test_supabase_connection():
    """Test basic Supabase connection"""
    print("🔍 Testing Supabase connection...")
    
    try:
        # Test client creation
        client = get_supabase_client()
        admin_client = get_supabase_admin_client()
        
        print("✅ Supabase clients created successfully")
        
        # Test basic query (this will fail if connection is bad)
        response = client.table('auth.users').select('*').limit(1).execute()
        print("✅ Supabase connection successful")
        
        return True
        
    except Exception as e:
        print(f"❌ Supabase connection failed: {str(e)}")
        return False

def test_environment_variables():
    """Test if all required environment variables are set"""
    print("\n🔍 Testing environment variables...")
    
    required_vars = [
        'SUPABASE_URL',
        'SUPABASE_ANON_KEY',
        'SUPABASE_SERVICE_ROLE_KEY'
    ]
    
    all_set = True
    
    for var in required_vars:
        value = getattr(settings, var, None)
        if value and value != '':
            print(f"✅ {var}: Set")
        else:
            print(f"❌ {var}: Not set or empty")
            all_set = False
    
    return all_set

def test_django_models():
    """Test Django models"""
    print("\n🔍 Testing Django models...")
    
    try:
        from base.models import Institution, UserProfile
        
        # Test model creation
        institution = Institution(name="Test Institution")
        print("✅ Institution model: OK")
        
        print("✅ Django models: OK")
        return True
        
    except Exception as e:
        print(f"❌ Django models test failed: {str(e)}")
        return False

def test_database_connection():
    """Test Django database connection"""
    print("\n🔍 Testing Django database connection...")
    
    try:
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        if result[0] == 1:
            print("✅ Django database connection: OK")
            return True
        else:
            print("❌ Django database connection: Failed")
            return False
            
    except Exception as e:
        print(f"❌ Django database connection failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Supabase Integration Tests\n")
    
    tests = [
        test_environment_variables,
        test_django_models,
        test_database_connection,
        test_supabase_connection,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your Supabase integration is ready.")
        print("\n📝 Next steps:")
        print("1. Update your HTML templates with actual Supabase credentials")
        print("2. Run: python manage.py runserver")
        print("3. Visit: http://localhost:8000/admin-student-portal/")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        print("\n🔧 Common fixes:")
        print("1. Create a .env file with your Supabase credentials")
        print("2. Run: python manage.py migrate")
        print("3. Check your Supabase project settings")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
