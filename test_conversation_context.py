#!/usr/bin/env python3
"""
Test script to verify conversation context is working properly
"""

import os
import sys
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from base.views import gemini_chat_api
from django.test import RequestFactory
import json

def test_conversation_context():
    """Test that conversation context is maintained across multiple messages"""
    
    factory = RequestFactory()
    
    # Test 1: First message
    print("🧪 Test 1: First message")
    data1 = {
        'message': 'I feel anxious about my exams',
        'conversation_history': []
    }
    
    request1 = factory.post('/api/gemini-chat/', 
                          data=json.dumps(data1),
                          content_type='application/json')
    
    response1 = gemini_chat_api(request1)
    response_data1 = json.loads(response1.content.decode())
    
    print(f"✅ First response: {response_data1.get('response', 'No response')[:100]}...")
    
    # Test 2: Follow-up message with context
    print("\n🧪 Test 2: Follow-up message with context")
    conversation_history = [
        {'sender': 'user', 'content': 'I feel anxious about my exams', 'timestamp': '2025-01-21T10:00:00Z'},
        {'sender': 'ai', 'content': response_data1.get('response', ''), 'timestamp': '2025-01-21T10:00:01Z'}
    ]
    
    data2 = {
        'message': 'I keep thinking I will fail',
        'conversation_history': conversation_history
    }
    
    request2 = factory.post('/api/gemini-chat/', 
                          data=json.dumps(data2),
                          content_type='application/json')
    
    response2 = gemini_chat_api(request2)
    response_data2 = json.loads(response2.content.decode())
    
    print(f"✅ Second response: {response_data2.get('response', 'No response')[:100]}...")
    
    # Test 3: Another follow-up
    print("\n🧪 Test 3: Another follow-up message")
    conversation_history.append({
        'sender': 'user', 
        'content': 'I keep thinking I will fail', 
        'timestamp': '2025-01-21T10:00:02Z'
    })
    conversation_history.append({
        'sender': 'ai', 
        'content': response_data2.get('response', ''), 
        'timestamp': '2025-01-21T10:00:03Z'
    })
    
    data3 = {
        'message': 'What can I do to feel more confident?',
        'conversation_history': conversation_history
    }
    
    request3 = factory.post('/api/gemini-chat/', 
                          data=json.dumps(data3),
                          content_type='application/json')
    
    response3 = gemini_chat_api(request3)
    response_data3 = json.loads(response3.content.decode())
    
    print(f"✅ Third response: {response_data3.get('response', 'No response')[:100]}...")
    
    print("\n🎉 Conversation context test completed!")
    print("The AI should maintain context across all three messages.")

if __name__ == "__main__":
    test_conversation_context()
