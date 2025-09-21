#!/usr/bin/env python3
"""
Test script for enhanced AI responses with feature recommendations
"""

import os
import sys
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from gemini_config import generate_mental_health_response, get_feature_recommendations

def test_feature_recommendations():
    """Test the feature recommendation system"""
    
    print("🧪 Testing Feature Recommendations")
    print("=" * 50)
    
    test_messages = [
        'I feel really anxious about my exams',
        'I have been feeling depressed lately', 
        'I feel lonely and isolated',
        'I need help with stress management',
        'I want to learn coping strategies',
        'I am having thoughts of self-harm'
    ]
    
    for msg in test_messages:
        print(f'\n📝 Message: "{msg}"')
        recommendations = get_feature_recommendations(msg)
        print("   Recommended Features:")
        for rec in recommendations:
            print(f"   → {rec['feature']}: {rec['description']}")
            print(f"     Benefit: {rec['benefit']}")

def test_enhanced_ai_responses():
    """Test the enhanced AI responses"""
    
    print("\n\n🤖 Testing Enhanced AI Responses")
    print("=" * 50)
    
    test_messages = [
        'I feel stressed about my upcoming exams',
        'I have been feeling sad and unmotivated',
        'I feel overwhelmed with everything'
    ]
    
    for msg in test_messages:
        print(f'\n📝 User: "{msg}"')
        try:
            response = generate_mental_health_response(msg)
            print(f"🤖 AI: {response['text'][:200]}...")
            if 'feature_recommendations' in response:
                print("   Feature Recommendations:")
                for rec in response['feature_recommendations']:
                    print(f"   → {rec['feature']}")
        except Exception as e:
            print(f"   Error: {e}")

if __name__ == "__main__":
    test_feature_recommendations()
    test_enhanced_ai_responses()
    print("\n✅ Testing completed!")
