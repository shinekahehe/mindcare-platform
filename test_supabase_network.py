#!/usr/bin/env python3
"""
Test Supabase network connectivity
"""
import socket
import requests

def test_supabase_connectivity():
    """Test if we can reach Supabase"""
    print("🌐 Testing Supabase Network Connectivity")
    print("=" * 50)
    
    # Test 1: DNS Resolution
    print("\n1. Testing DNS resolution...")
    try:
        hostname = "db.rsynefzafjjxtkaqybsy.supabase.co"
        ip = socket.gethostbyname(hostname)
        print(f"✅ DNS resolved: {hostname} → {ip}")
    except socket.gaierror as e:
        print(f"❌ DNS resolution failed: {e}")
        return False
    
    # Test 2: Port connectivity
    print("\n2. Testing port connectivity...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, 5432))
        sock.close()
        
        if result == 0:
            print("✅ Port 5432 is open and reachable")
        else:
            print("❌ Port 5432 is not reachable")
            return False
    except Exception as e:
        print(f"❌ Port test failed: {e}")
        return False
    
    # Test 3: Supabase API connectivity
    print("\n3. Testing Supabase API...")
    try:
        response = requests.get("https://rsynefzafjjxtkaqybsy.supabase.co", timeout=10)
        print(f"✅ Supabase API reachable: {response.status_code}")
    except Exception as e:
        print(f"❌ Supabase API test failed: {e}")
    
    print("\n🎉 Network connectivity test completed!")
    return True

if __name__ == "__main__":
    test_supabase_connectivity()
