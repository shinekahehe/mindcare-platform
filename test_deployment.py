#!/usr/bin/env python3
"""
Simple deployment test script
"""
import os
import sys

def test_basic_imports():
    """Test basic Python imports"""
    try:
        import django
        print(f"✅ Django {django.get_version()} imported successfully")
        
        # Set up Django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
        django.setup()
        
        from django.conf import settings
        print(f"✅ Django settings loaded")
        print(f"   DEBUG: {settings.DEBUG}")
        print(f"   ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
        
        # Test basic Django functionality
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        print("✅ WSGI application created successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        return False

def test_database():
    """Test database connection"""
    try:
        from django.db import connection
        connection.ensure_connection()
        print("✅ Database connection successful")
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def test_static_files():
    """Test static files configuration"""
    try:
        from django.conf import settings
        from django.contrib.staticfiles import finders
        
        # Test static file finders
        static_files = finders.find('admin/css/base.css')
        if static_files:
            print("✅ Static files configuration working")
        else:
            print("⚠️ Static files not found (may be normal)")
        return True
    except Exception as e:
        print(f"❌ Static files test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing deployment readiness...")
    print("=" * 50)
    
    tests = [
        ("Basic Imports", test_basic_imports),
        ("Database", test_database),
        ("Static Files", test_static_files),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🔍 Testing {test_name}...")
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {test_name}: {status}")
        if not result:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! Ready for deployment.")
    else:
        print("\n⚠️ Some tests failed. Check the errors above.")
    
    sys.exit(0 if all_passed else 1)
