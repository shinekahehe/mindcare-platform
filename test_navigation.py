#!/usr/bin/env python
"""
Test navigation between pages
"""

import requests
import time

def test_navigation():
    """Test navigation between different pages"""
    base_url = "http://127.0.0.1:8000"
    
    print("🧪 Testing Page Navigation")
    print("=" * 40)
    
    # Test pages
    pages = [
        ("/admin-student-portal/", "Admin-Student Portal"),
        ("/login/", "Login Page"),
        ("/signup/", "Signup Page"),
    ]
    
    for path, name in pages:
        try:
            response = requests.get(f"{base_url}{path}", timeout=5)
            if response.status_code == 200:
                print(f"✅ {name}: OK (Status: {response.status_code})")
            else:
                print(f"⚠️  {name}: Status {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ {name}: Failed - {e}")
    
    print("\n🎯 Navigation Flow Test:")
    print("1. Visit: http://127.0.0.1:8000/admin-student-portal/")
    print("2. Click 'Student' or 'Admin' button")
    print("3. Should redirect to signup page")
    print("4. Click 'Login here' link")
    print("5. Should redirect to login page")
    print("6. Click 'create an account' link")
    print("7. Should redirect back to signup page")
    print("8. Click back arrow on any page")
    print("9. Should redirect to admin-student portal")

if __name__ == "__main__":
    test_navigation()
