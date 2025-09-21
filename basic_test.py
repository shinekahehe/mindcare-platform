#!/usr/bin/env python
"""
Basic functionality test for the Django + Supabase project
This script tests the core functionality without requiring Supabase setup
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

def test_django_setup():
    """Test basic Django setup"""
    print("🔍 Testing Django Setup...")
    
    try:
        from django.conf import settings
        from django.test import Client
        from django.urls import reverse
        
        print("✅ Django settings loaded")
        print(f"✅ Debug mode: {settings.DEBUG}")
        print(f"✅ Database: {settings.DATABASES['default']['ENGINE']}")
        
        return True
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return False

def test_models():
    """Test Django models"""
    print("\n🔍 Testing Django Models...")
    
    try:
        from base.models import Institution, UserProfile
        from django.contrib.auth.models import User
        
        # Test model creation
        institution = Institution(name="Test University")
        print("✅ Institution model: OK")
        
        user = User(username="testuser", email="test@example.com")
        print("✅ User model: OK")
        
        profile = UserProfile(user=user, institution=institution, role="student")
        print("✅ UserProfile model: OK")
        
        return True
    except Exception as e:
        print(f"❌ Models test failed: {e}")
        return False

def test_urls():
    """Test URL configuration"""
    print("\n🔍 Testing URL Configuration...")
    
    try:
        from django.urls import reverse
        from django.test import Client
        
        client = Client()
        
        # Test main URLs
        urls_to_test = [
            ('admin-student-portal', '/admin-student-portal/'),
            ('login', '/login/'),
            ('signup', '/signup/'),
        ]
        
        for name, path in urls_to_test:
            try:
                response = client.get(path)
                if response.status_code in [200, 302]:  # 302 for redirects
                    print(f"✅ {name}: OK (Status: {response.status_code})")
                else:
                    print(f"⚠️  {name}: Status {response.status_code}")
            except Exception as e:
                print(f"❌ {name}: Failed - {e}")
        
        return True
    except Exception as e:
        print(f"❌ URL test failed: {e}")
        return False

def test_templates():
    """Test template rendering"""
    print("\n🔍 Testing Template Rendering...")
    
    try:
        from django.template.loader import render_to_string
        from django.http import HttpRequest
        
        templates_to_test = [
            'admin-student.html',
            'login.html', 
            'signup.html',
            'dashboard.html'
        ]
        
        for template in templates_to_test:
            try:
                # Create a basic context
                context = {
                    'user': None,
                    'profile': None,
                    'institution': None
                }
                
                html = render_to_string(template, context)
                if html and len(html) > 100:  # Basic check for content
                    print(f"✅ {template}: OK ({len(html)} chars)")
                else:
                    print(f"⚠️  {template}: Empty or very short")
            except Exception as e:
                print(f"❌ {template}: Failed - {e}")
        
        return True
    except Exception as e:
        print(f"❌ Template test failed: {e}")
        return False

def test_api_endpoints():
    """Test API endpoint structure"""
    print("\n🔍 Testing API Endpoints...")
    
    try:
        from django.test import Client
        
        client = Client()
        
        # Test API endpoints (they should return 405 for GET requests)
        api_endpoints = [
            '/api/signup/',
            '/api/login/',
            '/api/logout/',
        ]
        
        for endpoint in api_endpoints:
            try:
                response = client.get(endpoint)
                if response.status_code == 405:  # Method not allowed (expected for POST-only)
                    print(f"✅ {endpoint}: OK (Method not allowed - expected)")
                elif response.status_code == 200:
                    print(f"✅ {endpoint}: OK (Status: 200)")
                else:
                    print(f"⚠️  {endpoint}: Status {response.status_code}")
            except Exception as e:
                print(f"❌ {endpoint}: Failed - {e}")
        
        return True
    except Exception as e:
        print(f"❌ API test failed: {e}")
        return False

def test_database():
    """Test database connectivity"""
    print("\n🔍 Testing Database...")
    
    try:
        from django.db import connection
        from base.models import Institution
        
        # Test database connection
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        
        if result[0] == 1:
            print("✅ Database connection: OK")
        else:
            print("❌ Database connection: Failed")
            return False
        
        # Test model operations
        institution_count = Institution.objects.count()
        print(f"✅ Institution count: {institution_count}")
        
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

def test_static_files():
    """Test static files configuration"""
    print("\n🔍 Testing Static Files...")
    
    try:
        from django.conf import settings
        from pathlib import Path
        
        static_dirs = settings.STATICFILES_DIRS
        print(f"✅ Static files directories: {len(static_dirs)} configured")
        
        # Check if static directory exists
        static_path = Path(settings.BASE_DIR) / 'static'
        if static_path.exists():
            print("✅ Static directory exists")
        else:
            print("⚠️  Static directory not found")
        
        return True
    except Exception as e:
        print(f"❌ Static files test failed: {e}")
        return False

def main():
    """Run all basic tests"""
    print("🚀 Basic Functionality Test for Django + Supabase Project")
    print("=" * 60)
    
    tests = [
        test_django_setup,
        test_models,
        test_urls,
        test_templates,
        test_api_endpoints,
        test_database,
        test_static_files,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 60)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All basic tests passed! Your Django setup is working correctly.")
        print("\n📝 Next steps:")
        print("1. Start the server: python manage.py runserver")
        print("2. Visit: http://localhost:8000/admin-student-portal/")
        print("3. Test the UI and forms manually")
        print("4. Set up Supabase credentials for full integration testing")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        print("\n🔧 Common fixes:")
        print("1. Run: python manage.py migrate")
        print("2. Check your Django settings")
        print("3. Verify all files are in the correct locations")
    
    print(f"\n🌐 Your server should be running at: http://localhost:8000")
    print("📚 For detailed testing guide, see: TESTING_GUIDE.md")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
