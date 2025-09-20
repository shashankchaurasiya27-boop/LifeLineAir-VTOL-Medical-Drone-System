#!/usr/bin/env python3
"""
Quick start script for VTOL Medical Drone System
This is a simplified version that just starts the server
"""

import os
import sys
import webbrowser
import http.server
import socketserver
from datetime import datetime

def main():
    """Start the local server with minimal setup"""
    
    # Check if we're in the right directory
    if not os.path.exists('index.html'):
        print("❌ Please run this script from the project directory containing index.html")
        sys.exit(1)
    
    # Get port (default 8000)
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 8000.")
    
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("🚁 VTOL Medical Drone System")
    print("=" * 50)
    print(f"📡 Starting server on port {port}...")
    print(f"🌐 URL: http://localhost:{port}")
    print("⏹️  Press Ctrl+C to stop")
    print("-" * 50)
    
    try:
        # Try to open browser
        webbrowser.open(f'http://localhost:{port}')
        print("🌐 Browser opened automatically")
    except:
        print("⚠️  Could not open browser automatically")
    
    print("-" * 50)
    
    # Start the server
    try:
        with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {port} is already in use. Try: python start_server.py {port + 1}")
        else:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
