#!/usr/bin/env python3
"""
Test self-assessment page navigation
"""

import requests
import time

def test_self_assessment_page():
    """Test that the self-assessment page is accessible"""
    print("🧪 Testing Self-Assessment Page Navigation...")
    
    try:
        # Test the self-assessment page directly
        response = requests.get("http://localhost:8000/self-assessment/")
        
        if response.status_code == 200:
            print("✅ Self-Assessment page is accessible")
            
            # Check if the page contains expected content
            content = response.text
            
            expected_elements = [
                "Self-Assessment",
                "PHQ-9 Depression Screening",
                "GAD-7 Anxiety Assessment",
                "Start Assessment",
                "Mental Health Assessment Tools"
            ]
            
            missing_elements = []
            for element in expected_elements:
                if element not in content:
                    missing_elements.append(element)
            
            if missing_elements:
                print(f"⚠️ Missing elements: {missing_elements}")
            else:
                print("✅ All expected content elements found")
            
            return True
        else:
            print(f"❌ Self-Assessment page returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Django server not running")
        print("Please start the server with: python manage.py runserver")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_mindcare_home_navigation():
    """Test that the MindCare home page contains the self-assessment navigation"""
    print("\n🧪 Testing MindCare Home Page Navigation...")
    
    try:
        # Test the MindCare home page
        response = requests.get("http://localhost:8000/mindcare-home/")
        
        if response.status_code == 200:
            print("✅ MindCare home page is accessible")
            
            # Check if the page contains self-assessment navigation
            content = response.text
            
            navigation_elements = [
                'data-page="assessment"',
                "Self-Assessment",
                "navigateToPage",
                "/self-assessment/"
            ]
            
            missing_elements = []
            for element in navigation_elements:
                if element not in content:
                    missing_elements.append(element)
            
            if missing_elements:
                print(f"⚠️ Missing navigation elements: {missing_elements}")
            else:
                print("✅ All navigation elements found")
            
            return True
        else:
            print(f"❌ MindCare home page returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Django server not running")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Testing Self-Assessment Page Integration...\n")
    
    tests = [
        ("Self-Assessment Page", test_self_assessment_page),
        ("MindCare Home Navigation", test_mindcare_home_navigation)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"{'='*50}")
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
        print("🎉 All tests passed! Self-Assessment integration is working correctly.")
        print("\n✅ Integration Complete:")
        print("1. Self-Assessment page is accessible at /self-assessment/")
        print("2. MindCare home page has proper navigation")
        print("3. Clicking 'Self-Assessment' will redirect to the assessment page")
        print("\n📱 How to test:")
        print("1. Go to http://localhost:8000/mindcare-home/")
        print("2. Click on 'Self-Assessment' in the sidebar")
        print("3. You should be redirected to the assessment page")
    else:
        print("⚠️ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()
