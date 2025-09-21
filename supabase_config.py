import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv('SUPABASE_URL', 'your_supabase_project_url')
SUPABASE_ANON_KEY = os.getenv('SUPABASE_ANON_KEY', 'your_supabase_anon_key')
SUPABASE_SERVICE_ROLE_KEY = os.getenv('SUPABASE_SERVICE_ROLE_KEY', 'your_supabase_service_role_key')

def get_supabase_client() -> Client:
    """Create and return a Supabase client instance"""
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

def get_supabase_admin_client() -> Client:
    """Create and return a Supabase admin client with service role key"""
    return create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)
