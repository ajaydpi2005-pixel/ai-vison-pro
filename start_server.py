"""
AI Vision Pro - Render Startup Script
Guaranteed to work on Render.com
"""

import sys
import os

# Get the absolute path to the project root
project_root = os.path.dirname(os.path.abspath(__file__))

# Add project root and all subdirectories to Python path
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, 'backend'))

# Change to project root directory
os.chdir(project_root)

print(f"[INFO] Starting server from: {project_root}")
print(f"[INFO] Python path: {sys.path[0]}")

# Set environment variable for PORT if not set
if not os.environ.get('PORT'):
    os.environ['PORT'] = '8000'

# Now import and run
import uvicorn

# Import app after setting up paths
try:
    from backend.main import app
    print("[INFO] Successfully imported app from backend.main")
except ImportError as e:
    print(f"[ERROR] Failed to import: {e}")
    # Try alternative import
    sys.path.insert(0, os.path.join(project_root, '..'))
    try:
        from backend.main import app
        print("[INFO] Successfully imported with alternative path")
    except ImportError as e:
        print(f"[ERROR] Failed to import with alternative path: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        port = int(os.environ.get("PORT", 8000))
        print(f"[INFO] Starting uvicorn on port {port}")
        uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
    except Exception as e:
        print(f"[ERROR] Failed to start uvicorn: {e}")
        sys.exit(1)
