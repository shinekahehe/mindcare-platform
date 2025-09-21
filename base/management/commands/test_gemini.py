from django.core.management.base import BaseCommand
from gemini_config import generate_mental_health_response, is_mental_health_related

class Command(BaseCommand):
    help = 'Test Gemini API integration'

    def handle(self, *args, **options):
        self.stdout.write("🧪 Testing Gemini API in Django environment...")
        
        # Test mental health detection
        test_message = "I'm feeling anxious about my exams"
        is_related = is_mental_health_related(test_message)
        self.stdout.write(f"Mental health detection: {is_related}")
        
        # Test Gemini response
        try:
            response = generate_mental_health_response(test_message)
            if response.get('error'):
                self.stdout.write(self.style.ERROR(f"Error: {response['error']}"))
            else:
                self.stdout.write(self.style.SUCCESS("✅ Gemini API working!"))
                self.stdout.write(f"Response: {response['text'][:100]}...")
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Exception: {e}"))
