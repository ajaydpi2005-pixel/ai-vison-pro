"""
AI Vision Pro - Master Launcher
Run all components simultaneously for development
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def run_in_terminal(title, command, cwd=None):
    """Run a command in a new terminal window"""
    print(f"[Launcher] Starting {title}...")
    
    if sys.platform == "win32":
        # Windows - use start command
        cmd = f'start "{title}" cmd /k "{command}"'
        subprocess.Popen(cmd, shell=True, cwd=cwd)
    elif sys.platform == "darwin":
        # macOS - use Terminal.app
        script = f'tell application "Terminal" to do script "cd {cwd or os.getcwd()} && {command}"'
        subprocess.Popen(["osascript", "-e", script])
    else:
        # Linux - try gnome-terminal or xterm
        terminals = [
            f"gnome-terminal -- bash -c '{command}; exec bash'",
            f"xterm -hold -e '{command}'",
            f"konsole --hold -e '{command}'"
        ]
        for term_cmd in terminals:
            try:
                subprocess.Popen(term_cmd, shell=True, cwd=cwd)
                break
            except:
                continue

def main():
    """Launch all components"""
    print("=" * 60)
    print("🎯 AI Vision Pro - Development Launcher")
    print("=" * 60)
    print()
    
    # Get project root
    project_root = Path(__file__).parent
    
    # Components to launch
    components = [
        ("Backend API", f"{sys.executable} backend/main.py", project_root),
        ("Desktop App", f"{sys.executable} desktop_app/main.py", project_root),
        ("Web App", f"streamlit run web_app/main.py --server.port 8501", project_root),
    ]
    
    print("[Launcher] Starting components:")
    print("  1. Backend API (http://localhost:8000)")
    print("  2. Desktop App (Tkinter window)")
    print("  3. Web App (http://localhost:8501)")
    print()
    print("[Launcher] Note: Run camera app separately after backend loads")
    print("[Launcher] Command: python camera_app/main.py")
    print()
    print("-" * 60)
    
    # Launch each component
    for title, command, cwd in components:
        run_in_terminal(title, command, str(cwd))
        time.sleep(1)  # Small delay between launches
    
    print()
    print("=" * 60)
    print("[Launcher] All components starting...")
    print("[Launcher] Press Ctrl+C in respective terminals to stop")
    print("=" * 60)
    
    # Keep script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Launcher] Exiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
