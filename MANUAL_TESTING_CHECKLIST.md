# 🧪 Manual Testing Checklist

Your Django + Supabase project is ready for testing! Here's a step-by-step guide to test all functionality.

## 🚀 Quick Start

1. **Start the server** (if not already running):
   ```bash
   python manage.py runserver
   ```

2. **Open your browser** and visit: `http://localhost:8000/admin-student-portal/`

## ✅ Testing Checklist

### 1. **Admin-Student Portal Page**
- [ ] Page loads with beautiful gradient background
- [ ] Institution name input field is visible
- [ ] "Student" button is present and clickable
- [ ] "Admin" button is present and clickable
- [ ] Try clicking buttons without entering institution name
  - [ ] Should show alert: "Please enter your institution name first."
- [ ] Enter institution name (e.g., "Harvard University")
- [ ] Click "Student" button
  - [ ] Should redirect to signup page
  - [ ] URL should include role parameter

### 2. **Signup Page**
- [ ] Page loads with beautiful design
- [ ] Username field is present
- [ ] Email field is present  
- [ ] Password field is present
- [ ] "sign in" button is present
- [ ] Form validation works:
  - [ ] Try submitting with short username (< 3 chars)
  - [ ] Try submitting with invalid email
  - [ ] Try submitting with short password (< 6 chars)
  - [ ] Should show red borders and shake animation
- [ ] Fill valid form:
  - [ ] Username: "john_doe"
  - [ ] Email: "john@harvard.edu"
  - [ ] Password: "password123"
- [ ] Click "sign in" button
  - [ ] Should show "Creating Account..." loading state
  - [ ] Should prompt for institution name
  - [ ] Should show success notification
  - [ ] Should redirect to login page after 3 seconds

### 3. **Login Page**
- [ ] Page loads with beautiful design
- [ ] Email field is present
- [ ] Password field is present
- [ ] "login" button is present
- [ ] "create an account" link works
- [ ] "forgot password?" link is present
- [ ] Form validation works:
  - [ ] Try submitting empty form
  - [ ] Try submitting with invalid email format
  - [ ] Try submitting with short password
  - [ ] Should show appropriate error messages
- [ ] Fill valid form:
  - [ ] Email: "john@harvard.edu"
  - [ ] Password: "password123"
- [ ] Click "login" button
  - [ ] Should show loading spinner
  - [ ] Should show success notification
  - [ ] Should redirect to dashboard after 2 seconds

### 4. **Dashboard Page**
- [ ] Page loads with user information
- [ ] Header shows username and role
- [ ] Institution name is displayed
- [ ] Role-specific content is shown:
  - [ ] If Student: Shows "My Courses", "Assignments", "Grades", "Messages"
  - [ ] If Admin: Shows "Manage Courses", "Student Management", etc.
- [ ] Logout button works
- [ ] Clicking action cards shows placeholder alerts

### 5. **Navigation Testing**
- [ ] Back arrow on signup page works
- [ ] Back arrow on login page works
- [ ] "already have an account? Login here" link works
- [ ] "create an account" link works
- [ ] All redirects work correctly

### 6. **Responsive Design Testing**
- [ ] Test on different screen sizes
- [ ] Mobile view works correctly
- [ ] Tablet view works correctly
- [ ] Desktop view works correctly

### 7. **Browser Compatibility**
- [ ] Test in Chrome
- [ ] Test in Firefox
- [ ] Test in Safari (if available)
- [ ] Test in Edge

## 🔧 Testing Without Supabase

Since you haven't set up Supabase yet, the authentication will show errors. This is expected! Here's what you should see:

### Expected Behavior (Without Supabase):
- ✅ All pages load correctly
- ✅ Form validation works
- ✅ UI animations work
- ✅ Navigation works
- ❌ Signup will show error (Supabase not configured)
- ❌ Login will show error (Supabase not configured)

### To Test Full Functionality:
1. Set up Supabase project
2. Create `.env` file with credentials
3. Update HTML templates with real Supabase URLs
4. Run the full test suite

## 🎯 Success Criteria

Your project is working correctly if:

- [ ] All pages load without errors
- [ ] Beautiful UI displays correctly
- [ ] Form validation works
- [ ] Navigation flows work
- [ ] Responsive design works
- [ ] No JavaScript errors in console
- [ ] All animations and interactions work

## 🐛 Common Issues & Solutions

**Issue: Page not loading**
- Solution: Check if server is running (`python manage.py runserver`)
- Solution: Check browser console for errors

**Issue: Forms not validating**
- Solution: Check browser console for JavaScript errors
- Solution: Ensure all HTML files are properly saved

**Issue: Styling looks broken**
- Solution: Check if static files are being served
- Solution: Hard refresh browser (Ctrl+F5)

**Issue: Supabase errors**
- Solution: This is expected without Supabase setup
- Solution: Follow the setup guide to configure Supabase

## 📊 Test Results Template

```
✅ Admin-Student Portal: PASS/FAIL
✅ Signup Page: PASS/FAIL
✅ Login Page: PASS/FAIL
✅ Dashboard Page: PASS/FAIL
✅ Navigation: PASS/FAIL
✅ Form Validation: PASS/FAIL
✅ Responsive Design: PASS/FAIL
✅ Browser Compatibility: PASS/FAIL

Notes:
- [Any issues found]
- [Performance observations]
- [UI/UX feedback]
```

## 🎉 Next Steps After Testing

1. **If all tests pass**: Your Django setup is perfect!
2. **Set up Supabase**: Follow `SUPABASE_SETUP_GUIDE.md`
3. **Test full integration**: Run `python test_supabase_integration.py`
4. **Deploy**: When ready, deploy to production

Happy testing! 🚀
