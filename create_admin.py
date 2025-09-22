#!/usr/bin/env python
"""
Script to create an admin user for the MindCare platform.
Run this script to create a superuser with the credentials:
- Email: admin@example.com
- Password: admin123
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin_user():
    """Create or update admin user"""
    email = 'admin@example.com'
    username = 'admin'
    password = 'admin123'
    
    try:
        # Check if user already exists
        user = User.objects.filter(email=email).first()
        
        if user:
            print(f"✅ User with email {email} already exists!")
            print(f"   Username: {user.username}")
            print(f"   Is superuser: {user.is_superuser}")
            print(f"   Is staff: {user.is_staff}")
            
            # Update password and permissions
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            print(f"✅ Updated password and permissions for {email}")
            
        else:
            # Create new superuser
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            print(f"✅ Created new superuser: {email}")
        
        print(f"\n🔑 Login credentials:")
        print(f"   Email: {email}")
        print(f"   Password: {password}")
        print(f"   Username: {username}")
        
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")

if __name__ == "__main__":
    create_admin_user()
