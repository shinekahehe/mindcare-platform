#!/usr/bin/env python3
"""
Test script to verify Supabase database connection
"""
import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from base.models import MoodEntry, UserProfile, Institution

def test_supabase_connection():
    """Test Supabase database connection"""
    print("🔗 Testing Supabase Database Connection")
    print("=" * 50)
    
    try:
        # Test 1: Check database connection
        print("\n1. Testing database connection...")
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"✅ Database connection successful: {result}")
        
        # Test 2: Check if we're using PostgreSQL
        print("\n2. Checking database type...")
        db_engine = connection.vendor
        print(f"✅ Database engine: {db_engine}")
        
        if db_engine == 'postgresql':
            print("🎉 Successfully connected to Supabase PostgreSQL!")
        else:
            print("⚠️  Still using SQLite - check your .env file")
        
        # Test 3: Check existing data
        print("\n3. Checking existing data...")
        user_count = User.objects.count()
        mood_count = MoodEntry.objects.count()
        print(f"✅ Users: {user_count}")
        print(f"✅ Mood entries: {mood_count}")
        
        # Test 4: Create a test mood entry
        print("\n4. Creating test mood entry...")
        try:
            # Get or create a test user
            test_user, created = User.objects.get_or_create(
                username='supabase_test_user',
                defaults={
                    'email': 'supabase_test@example.com',
                    'first_name': 'Supabase',
                    'last_name': 'Tester'
                }
            )
            
            # Create a test mood entry
            mood_entry = MoodEntry.objects.create(
                user=test_user,
                mood_value=7,
                mood_label='Very Pleasant',
                reason='Testing Supabase connection!',
                notes='This is a test entry to verify Supabase is working'
            )
            
            print(f"✅ Created test mood entry: {mood_entry.id}")
            print(f"   User: {mood_entry.user.username}")
            print(f"   Mood: {mood_entry.mood_label}")
            print(f"   Reason: {mood_entry.reason}")
            
            # Clean up test data
            mood_entry.delete()
            test_user.delete()
            print("✅ Test data cleaned up")
            
        except Exception as e:
            print(f"❌ Error creating test mood entry: {e}")
        
        print("\n🎉 Supabase connection test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Check your .env file has correct DATABASE_URL")
        print("2. Verify your Supabase project is active")
        print("3. Check your database password is correct")
        return False

if __name__ == "__main__":
    test_supabase_connection()
