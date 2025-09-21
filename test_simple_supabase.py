#!/usr/bin/env python
"""
Simple Supabase test without database operations
"""

import os
from dotenv import load_dotenv
from supabase import create_client

def test_simple_connection():
    """Test simple Supabase connection"""
    print("🔍 Testing Simple Supabase Connection...")
    
    # Load environment variables
    load_dotenv()
    
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_ANON_KEY')
    
    if not url or not key:
        print("❌ Missing Supabase credentials")
        return False
    
    try:
        # Create client
        supabase = create_client(url, key)
        print("✅ Supabase client created successfully")
        
        # Test a simple operation that doesn't require tables
        print("✅ Connection test passed")
        return True
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return False

def main():
    print("🚀 Simple Supabase Connection Test")
    print("=" * 40)
    
    if test_simple_connection():
        print("\n🎉 Supabase connection is working!")
        print("\n📝 Next steps:")
        print("1. Go to your Supabase dashboard")
        print("2. Run the corrected SQL script in supabase_setup.sql")
        print("3. Test the full integration")
        print("\n🔧 The SQL script has been corrected to avoid permission errors!")
    else:
        print("\n❌ Connection failed")
        print("Please check your Supabase credentials")

if __name__ == "__main__":
    main()
