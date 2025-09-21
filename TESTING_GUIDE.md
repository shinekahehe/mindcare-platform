# 🧪 Complete Testing Guide for Supabase Integration

This guide provides multiple ways to test your Django + Supabase project, from basic setup to full functionality.

## 🚀 Quick Start Testing (No Supabase Setup Required)

### 1. **Basic Django Server Test**
```bash
# Start the server
python manage.py runserver

# Visit these URLs in your browser:
# http://localhost:8000/admin-student-portal/
# http://localhost:8000/login/
# http://localhost:8000/signup/
```

**Expected Results:**
- ✅ All pages load without errors
- ✅ Beautiful UI displays correctly
- ✅ Forms are interactive
- ✅ Navigation works

### 2. **Test Static Files and Templates**
```bash
# Check if templates are found
python manage.py check --deploy

# Test template rendering
python manage.py shell
```
```python
# In Django shell:
from django.template.loader import render_to_string
from django.http import HttpRequest

# Test template rendering
request = HttpRequest()
context = {'user': None, 'profile': None, 'institution': None}
html = render_to_string('dashboard.html', context)
print("✅ Dashboard template renders successfully")
```

## 🔧 Integration Testing (Requires Supabase Setup)

### 3. **Run Integration Tests**
```bash
# Run the comprehensive test suite
python test_supabase_integration.py
```

**What this tests:**
- ✅ Environment variables configuration
- ✅ Django models functionality
- ✅ Database connectivity
- ✅ Supabase client connection

### 4. **Manual Supabase Setup Test**

If you have Supabase credentials, create a `.env` file:
```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_ANON_KEY=your_anon_key_here
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key_here
SECRET_KEY=django-insecure-e8%q@h1rxa8tp7r)m91u(7it5wwhe3(e-8uz00!*-d1st7drl%
DEBUG=True
```

Then run:
```bash
python test_supabase_integration.py
```

## 🌐 Frontend Testing

### 5. **Browser Testing Checklist**

**Test the Admin-Student Portal:**
1. Visit: `http://localhost:8000/admin-student-portal/`
2. ✅ Page loads with beautiful gradient background
3. ✅ Institution input field is present
4. ✅ Student/Admin buttons are clickable
5. ✅ Form validation works (try submitting without institution name)

**Test the Signup Page:**
1. Click "Student" or "Admin" button
2. ✅ Redirects to signup page with role pre-selected
3. ✅ Form fields are present (username, email, password)
4. ✅ Client-side validation works
5. ✅ Form submission shows loading state

**Test the Login Page:**
1. Visit: `http://localhost:8000/login/`
2. ✅ Beautiful login interface loads
3. ✅ Email and password fields are present
4. ✅ Form validation works
5. ✅ "Create account" link works

### 6. **JavaScript Console Testing**

Open browser developer tools (F12) and check:
```javascript
// Test if Supabase client loads
console.log(typeof window.supabase); // Should be 'object'

// Test form validation
document.getElementById('username').value = 'test';
document.getElementById('email').value = 'test@example.com';
document.getElementById('password').value = 'password123';

// Check if validation classes are applied
console.log(document.getElementById('username').classList.contains('success'));
```

## 🔌 API Testing

### 7. **Test API Endpoints with curl**

**Test Signup API:**
```bash
curl -X POST http://localhost:8000/api/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com", 
    "password": "password123",
    "institution": "Test University",
    "role": "student"
  }'
```

**Test Login API:**
```bash
curl -X POST http://localhost:8000/api/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

### 8. **Test API Endpoints with Python**

Create a test script:
```python
import requests
import json

# Test signup
signup_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "password123", 
    "institution": "Test University",
    "role": "student"
}

response = requests.post('http://localhost:8000/api/signup/', 
                        json=signup_data)
print(f"Signup Response: {response.status_code}")
print(response.json())

# Test login
login_data = {
    "email": "test@example.com",
    "password": "password123"
}

response = requests.post('http://localhost:8000/api/login/',
                        json=login_data)
print(f"Login Response: {response.status_code}")
print(response.json())
```

## 🗄️ Database Testing

### 9. **Test Django Models**

```bash
python manage.py shell
```

```python
# Test model creation
from base.models import Institution, UserProfile
from django.contrib.auth.models import User

# Create test institution
institution = Institution.objects.create(name="Test University")
print(f"✅ Created institution: {institution}")

# Create test user
user = User.objects.create_user(
    username="testuser",
    email="test@example.com",
    password="password123"
)
print(f"✅ Created user: {user}")

# Create user profile
profile = UserProfile.objects.create(
    user=user,
    institution=institution,
    role="student",
    supabase_user_id="test-supabase-id"
)
print(f"✅ Created profile: {profile}")

# Test queries
institutions = Institution.objects.all()
print(f"✅ Found {institutions.count()} institutions")

profiles = UserProfile.objects.filter(role="student")
print(f"✅ Found {profiles.count()} student profiles")
```

## 🎯 End-to-End Testing

### 10. **Complete User Flow Test**

**Scenario: New Student Registration**

1. **Start at Admin-Student Portal**
   - Visit: `http://localhost:8000/admin-student-portal/`
   - Enter institution name: "Harvard University"
   - Click "Student" button

2. **Signup Process**
   - Should redirect to signup page
   - Fill form:
     - Username: "john_doe"
     - Email: "john@harvard.edu"
     - Password: "securepass123"
   - Click "sign in" button

3. **Expected Results:**
   - ✅ Form validation passes
   - ✅ Loading state shows
   - ✅ Success notification appears
   - ✅ Redirects to login page

4. **Login Process**
   - Use same credentials
   - Click "login" button

5. **Expected Results:**
   - ✅ Login successful
   - ✅ Redirects to dashboard
   - ✅ Dashboard shows user info

### 11. **Error Handling Tests**

**Test Invalid Input:**
- Try signup with invalid email
- Try login with wrong password
- Try submitting empty forms
- Test with very short passwords

**Expected Results:**
- ✅ Appropriate error messages
- ✅ Form validation prevents submission
- ✅ UI shows error states

## 🔍 Debugging Tests

### 12. **Check Logs and Errors**

```bash
# Check Django logs
python manage.py runserver --verbosity=2

# Check for any Python errors
python -c "import django; django.setup(); from base.models import *; print('✅ All imports successful')"
```

### 13. **Browser Network Tab Testing**

1. Open Developer Tools (F12)
2. Go to Network tab
3. Try signup/login
4. Check:
   - ✅ API calls are made to correct endpoints
   - ✅ Request/response data is correct
   - ✅ No 404 or 500 errors
   - ✅ CORS headers are present

## 📊 Performance Testing

### 14. **Load Testing (Optional)**

```python
import time
import requests
import concurrent.futures

def test_signup():
    data = {
        "username": f"user{time.time()}",
        "email": f"user{time.time()}@test.com",
        "password": "password123",
        "institution": "Test University",
        "role": "student"
    }
    response = requests.post('http://localhost:8000/api/signup/', json=data)
    return response.status_code

# Test concurrent requests
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(test_signup) for _ in range(10)]
    results = [future.result() for future in futures]
    print(f"✅ Completed {len(results)} concurrent requests")
```

## 🎉 Success Criteria

Your integration is working correctly if:

- ✅ All pages load without errors
- ✅ Forms validate input correctly
- ✅ API endpoints respond appropriately
- ✅ Database operations work
- ✅ Supabase connection is established (when configured)
- ✅ User flow from signup to dashboard works
- ✅ Error handling is graceful
- ✅ UI is responsive and beautiful

## 🚨 Common Issues & Solutions

**Issue: "Invalid URL" error**
- Solution: Check your Supabase URL in .env file

**Issue: CORS errors**
- Solution: Configure CORS in Supabase dashboard

**Issue: Template not found**
- Solution: Check TEMPLATES setting in settings.py

**Issue: Static files not loading**
- Solution: Run `python manage.py collectstatic`

**Issue: Database errors**
- Solution: Run `python manage.py migrate`

## 📝 Test Report Template

After testing, document your results:

```
✅ Basic Setup: PASS/FAIL
✅ Frontend UI: PASS/FAIL  
✅ Form Validation: PASS/FAIL
✅ API Endpoints: PASS/FAIL
✅ Database Operations: PASS/FAIL
✅ Supabase Integration: PASS/FAIL
✅ End-to-End Flow: PASS/FAIL
✅ Error Handling: PASS/FAIL

Notes:
- [Any issues found]
- [Performance observations]
- [Browser compatibility notes]
```

Happy testing! 🚀
