"""
AI Vision Pro - Quick Test Script
Test all components before deployment
"""

import sys
import os

print("=" * 60)
print("  AI Vision Pro - Component Test Suite")
print("=" * 60)
print()

# Test 1: Python version
print("[Test 1] Python Version")
import platform
version = platform.python_version()
if version >= "3.11":
    print(f"   ✅ Python {version} - OK")
else:
    print(f"   ⚠️  Python {version} - Recommended: 3.11+")
print()

# Test 2: Required packages
print("[Test 2] Required Packages")
packages = [
    ("fastapi", "FastAPI"),
    ("uvicorn", "Uvicorn"),
    ("streamlit", "Streamlit"),
    ("pillow", "Pillow"),
    ("requests", "Requests"),
    ("torch", "PyTorch"),
    ("transformers", "HuggingFace Transformers"),
    ("supabase", "Supabase (optional)"),
]

missing = []
for module, name in packages:
    try:
        __import__(module)
        print(f"   ✅ {name}")
    except ImportError:
        print(f"   ❌ {name} - NOT INSTALLED")
        missing.append(module)
print()

# Test 3: Configuration
print("[Test 3] Configuration")
try:
    from config.settings import check_supabase_config, check_razorpay_config
    supabase_ready = check_supabase_config()
    razorpay_ready = check_razorpay_config()
    
    print(f"   {'✅' if supabase_ready else '⚠️'}  Supabase Database")
    print(f"   {'✅' if razorpay_ready else '⚠️'}  Razorpay Payments")
    
    if not supabase_ready:
        print("   💡 Tip: Set SUPABASE_URL and SUPABASE_KEY in .env")
    if not razorpay_ready:
        print("   💡 Tip: Set RAZORPAY_KEY_ID for payments")
except Exception as e:
    print(f"   ⚠️  Error: {e}")
print()

# Test 4: AI Model
print("[Test 4] AI Model Loading")
try:
    from shared_model import get_classifier
    classifier = get_classifier()
    print("   ✅ Model wrapper loaded")
    print("   💡 Model will download on first prediction (~100MB)")
except Exception as e:
    print(f"   ❌ Error: {e}")
print()

# Test 5: Database Client
print("[Test 5] Database Client")
try:
    from database.supabase_client import db_client
    if db_client.demo_mode:
        print("   ⚠️  Running in DEMO mode (data stored in memory)")
        print("   💡 Tip: Configure Supabase for production")
    else:
        print("   ✅ Connected to Supabase")
except Exception as e:
    print(f"   ⚠️  Error: {e}")
print()

# Test 6: File Structure
print("[Test 6] File Structure")
required_files = [
    "backend/main.py",
    "web_app_enhanced/main.py",
    "shared_model/__init__.py",
    "config/settings.py",
    "database/supabase_client.py",
    ".env.example",
    "requirements_enhanced.txt",
]

for file in required_files:
    if os.path.exists(file):
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file} - MISSING")
print()

# Test 7: Quick API Test
print("[Test 7] Backend API (if running)")
try:
    import requests
    response = requests.get("http://localhost:8000/health", timeout=2)
    if response.status_code == 200:
        print("   ✅ Backend is running at http://localhost:8000")
    else:
        print(f"   ⚠️  Backend returned status {response.status_code}")
except requests.exceptions.ConnectionError:
    print("   ⚠️  Backend not running")
    print("   💡 Run: python backend/main.py")
except Exception as e:
    print(f"   ⚠️  Error: {e}")
print()

# Summary
print("=" * 60)
print("  TEST SUMMARY")
print("=" * 60)

if missing:
    print()
    print("❌ MISSING PACKAGES:")
    print(f"   Run: pip install {' '.join(missing)}")
    print()
else:
    print()
    print("✅ All core packages installed!")

print()
print("🚀 NEXT STEPS:")
print("   1. Setup Supabase (see SETUP_GUIDE.md)")
print("   2. Run: python backend/main.py")
print("   3. Run: streamlit run web_app_enhanced/main.py")
print("   4. Open: http://localhost:8501")
print()

# Offer to run setup
if __name__ == "__main__":
    import subprocess
    
    print("=" * 60)
    choice = input("Run full setup now? (y/n): ").strip().lower()
    
    if choice == 'y':
        print()
        print("Installing all packages...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements_enhanced.txt"])
        print()
        print("✅ Setup complete!")
        print()
        print("Now run:")
        print("  python backend/main.py")
        print("  streamlit run web_app_enhanced/main.py")
