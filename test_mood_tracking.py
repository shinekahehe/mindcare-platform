#!/usr/bin/env python3
"""
Test script for mood tracking database functionality
"""
import os
import sys
import django
import json
from pathlib import Path

# Add the project directory to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from django.contrib.auth.models import User
from base.models import MoodEntry, UserProfile, Institution

def test_mood_tracking():
    """Test mood tracking functionality"""
    print("🧪 Testing Mood Tracking Database Functionality")
    print("=" * 60)
    
    # Test 1: Create a test user
    print("\n1. Creating test user...")
    try:
        test_user, created = User.objects.get_or_create(
            username='mood_test_user',
            defaults={
                'email': 'moodtest@example.com',
                'first_name': 'Mood',
                'last_name': 'Tester'
            }
        )
        if created:
            print(f"✅ Created test user: {test_user.username}")
        else:
            print(f"✅ Using existing test user: {test_user.username}")
    except Exception as e:
        print(f"❌ Error creating test user: {e}")
        return False
    
    # Test 2: Create mood entries
    print("\n2. Creating mood entries...")
    test_moods = [
        {'value': 7, 'label': 'Very Pleasant', 'reason': 'Had a great day at work'},
        {'value': 5, 'label': 'Slightly Pleasant', 'reason': 'Nice weather today'},
        {'value': 3, 'label': 'Slightly Unpleasant', 'reason': 'Feeling stressed about exams'},
        {'value': 1, 'label': 'Very Unpleasant', 'reason': 'Having a difficult time'},
    ]
    
    created_entries = []
    for mood_data in test_moods:
        try:
            entry = MoodEntry.objects.create(
                user=test_user,
                mood_value=mood_data['value'],
                mood_label=mood_data['label'],
                reason=mood_data['reason']
            )
            created_entries.append(entry)
            print(f"✅ Created mood entry: {entry.mood_label} (Value: {entry.mood_value})")
        except Exception as e:
            print(f"❌ Error creating mood entry: {e}")
    
    # Test 3: Retrieve mood history
    print("\n3. Retrieving mood history...")
    try:
        mood_entries = MoodEntry.objects.filter(user=test_user).order_by('-created_at')
        print(f"✅ Found {mood_entries.count()} mood entries for user")
        
        for entry in mood_entries:
            print(f"   - {entry.mood_label} ({entry.mood_value}): {entry.reason}")
    except Exception as e:
        print(f"❌ Error retrieving mood history: {e}")
    
    # Test 4: Test API endpoints (simulate)
    print("\n4. Testing API endpoint simulation...")
    try:
        # Simulate save_mood_api data
        api_data = {
            'mood': {'value': 6, 'label': 'Pleasant'},
            'reasons': ['Good sleep', 'Exercise'],
            'customReason': 'Feeling motivated',
            'timestamp': '2024-01-15T10:30:00Z',
            'user_data': {'email': 'moodtest@example.com', 'username': 'Mood Tester'}
        }
        
        # Simulate the API logic
        user = User.objects.get(email=api_data['user_data']['email'])
        reason_text = ', '.join(api_data['reasons'])
        if api_data['customReason']:
            reason_text += f' | Custom: {api_data["customReason"]}'
        
        entry = MoodEntry.objects.create(
            user=user,
            mood_value=api_data['mood']['value'],
            mood_label=api_data['mood']['label'],
            reason=reason_text,
            notes=f"Timestamp: {api_data['timestamp']}"
        )
        
        print(f"✅ API simulation successful: Created entry {entry.id}")
    except Exception as e:
        print(f"❌ API simulation failed: {e}")
    
    # Test 5: Database statistics
    print("\n5. Database Statistics:")
    print(f"   Total Users: {User.objects.count()}")
    print(f"   Total Mood Entries: {MoodEntry.objects.count()}")
    print(f"   Test User Entries: {MoodEntry.objects.filter(user=test_user).count()}")
    
    # Test 6: Cleanup (optional)
    print("\n6. Cleanup test data...")
    try:
        # Delete test mood entries
        deleted_count = MoodEntry.objects.filter(user=test_user).delete()[0]
        print(f"✅ Deleted {deleted_count} test mood entries")
        
        # Delete test user
        test_user.delete()
        print("✅ Deleted test user")
    except Exception as e:
        print(f"❌ Cleanup error: {e}")
    
    print("\n🎉 Mood tracking database test completed!")
    return True

if __name__ == "__main__":
    test_mood_tracking()
