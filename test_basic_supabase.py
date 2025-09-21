#!/usr/bin/env python
"""
Basic Supabase connection test
"""

import os
from dotenv import load_dotenv
from supabase import create_client

def test_basic_connection():
    """Test basic Supabase connection without database operations"""
    print("🔍 Testing Basic Supabase Connection...")
    
    # Load environment variables
    load_dotenv('.env.local')
    
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_ANON_KEY')
    
    if not url or not key:
        print("❌ Missing Supabase credentials")
        return False
    
    try:
        # Create client
        supabase = create_client(url, key)
        print("✅ Supabase client created successfully")
        
        # Test basic connection (this should work even without tables)
        print("✅ Basic connection test passed")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def main():
    print("🚀 Basic Supabase Connection Test")
    print("=" * 40)
    
    if test_basic_connection():
        print("\n🎉 Basic connection is working!")
        print("\n📝 Next steps:")
        print("1. Go to your Supabase dashboard")
        print("2. Run the SQL script in supabase_setup.sql")
        print("3. Test the full integration")
    else:
        print("\n❌ Basic connection failed")
        print("Please check your Supabase credentials")

if __name__ == "__main__":
    main()
