#!/usr/bin/env python3
"""
Test mental health detection function
"""

import os
import sys
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from gemini_config import is_mental_health_related

def test_mental_health_detection():
    """Test mental health detection for various messages"""
    
    test_messages = [
        'I feel anxious about my exams',
        'I keep thinking I will fail', 
        'What can I do to feel more confident?',
        'Hello, how are you?',
        'I need help with my homework',
        'I feel depressed and hopeless',
        'Can you help me with math?'
    ]
    
    print("🧪 Testing Mental Health Detection")
    print("=" * 50)
    
    for msg in test_messages:
        result = is_mental_health_related(msg)
        status = "✅ Mental Health" if result else "❌ Off-topic"
        print(f"{status}: \"{msg}\"")

if __name__ == "__main__":
    test_mental_health_detection()
