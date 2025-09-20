#!/usr/bin/env python3
"""
VTOL Medical Drone System - Local Server
Simple HTTP server for hosting the web application locally
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import json
from urllib.parse import urlparse, parse_qs
import threading
import time
from datetime import datetime

class MedDroneHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler for the MedDrone application"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        # Handle API endpoints
        if parsed_path.path.startswith('/api/'):
            self.handle_api_request(parsed_path)
            return
        
        # Serve static files
        super().do_GET()
    
    def do_POST(self):
        """Handle POST requests"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path.startswith('/api/'):
            self.handle_api_request(parsed_path)
            return
        
        # Default to 404 for non-API POST requests
        self.send_error(404, "Not Found")
    
    def handle_api_request(self, parsed_path):
        """Handle API requests"""
        path = parsed_path.path
        
        if path == '/api/status':
            self.send_api_response({
                'status': 'online',
                'timestamp': datetime.now().isoformat(),
                'system': 'VTOL Medical Drone System',
                'version': '1.0.0'
            })
        
        elif path == '/api/fleet':
            self.send_api_response(self.get_fleet_data())
        
        elif path == '/api/alerts':
            self.send_api_response(self.get_alerts_data())
        
        elif path == '/api/metrics':
            self.send_api_response(self.get_metrics_data())
        
        else:
            self.send_error(404, "API endpoint not found")
    
    def send_api_response(self, data):
        """Send JSON API response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = json.dumps(data, indent=2)
        self.wfile.write(response.encode('utf-8'))
    
    def get_fleet_data(self):
        """Get fleet status data"""
        return {
            'drones': [
                {'id': 'LLA-001', 'status': 'Active', 'battery': 87, 'mission': 'Medical Delivery', 'location': 'Zone Alpha'},
                {'id': 'LLA-002', 'status': 'Charging', 'battery': 45, 'mission': 'Standby', 'location': 'Base Station'},
                {'id': 'LLA-003', 'status': 'Active', 'battery': 92, 'mission': 'Emergency Response', 'location': 'Zone Beta'},
                {'id': 'LLA-004', 'status': 'Maintenance', 'battery': 0, 'mission': 'None', 'location': 'Hangar'},
                {'id': 'LLA-005', 'status': 'Active', 'battery': 78, 'mission': 'Supply Drop', 'location': 'Zone Gamma'}
            ],
            'total_drones': 15,
            'active_missions': 8,
            'success_rate': 94.5,
            'avg_delivery_time': 12.3
        }
    
    def get_alerts_data(self):
        """Get alerts data"""
        return {
            'alerts': [
                {
                    'id': 1,
                    'title': 'Low Battery Warning',
                    'message': 'Drone LLA-002 battery at 45%',
                    'severity': 'warning',
                    'timestamp': datetime.now().isoformat(),
                    'location': 'LLA-002'
                },
                {
                    'id': 2,
                    'title': 'Critical Stock Level',
                    'message': 'Emergency Medications below threshold',
                    'severity': 'critical',
                    'timestamp': datetime.now().isoformat(),
                    'location': 'Medical Inventory'
                }
            ]
        }
    
    def get_metrics_data(self):
        """Get metrics data"""
        return {
            'kpis': {
                'total_drones': 15,
                'active_missions': 8,
                'success_rate': 94.5,
                'avg_delivery_time': 12.3
            },
            'fleet_status': {
                'active': 3,
                'charging': 1,
                'maintenance': 1,
                'standby': 10
            },
            'medical_supplies': [
                {'item': 'Blood Pack O+', 'stock': 25, 'min_threshold': 10, 'status': 'Good'},
                {'item': 'Emergency Medications', 'stock': 8, 'min_threshold': 15, 'status': 'Low'},
                {'item': 'IV Fluids', 'stock': 45, 'min_threshold': 20, 'status': 'Good'},
                {'item': 'Trauma Kits', 'stock': 12, 'min_threshold': 8, 'status': 'Good'}
            ]
        }

def start_server(port=8000):
    """Start the local server"""
    try:
        # Create the server
        with socketserver.TCPServer(("", port), MedDroneHTTPRequestHandler) as httpd:
            print(f"🚁 VTOL Medical Drone System Server")
            print(f"📡 Server running at: http://localhost:{port}")
            print(f"🌐 Open your browser and navigate to: http://localhost:{port}")
            print(f"⏹️  Press Ctrl+C to stop the server")
            print("-" * 60)
            
            # Try to open browser automatically
            try:
                webbrowser.open(f'http://localhost:{port}')
                print("🌐 Browser opened automatically")
            except:
                print("⚠️  Could not open browser automatically")
            
            print("-" * 60)
            
            # Start the server
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {port} is already in use. Trying port {port + 1}...")
            start_server(port + 1)
        else:
            print(f"❌ Error starting server: {e}")
            sys.exit(1)

def check_requirements():
    """Check if all required files are present"""
    required_files = ['index.html', 'app.js', 'style.css']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files found")
    return True

def main():
    """Main function"""
    print("🚁 VTOL Medical Drone System - Local Server Setup")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not check_requirements():
        print("❌ Please run this script from the project directory")
        sys.exit(1)
    
    # Get port from command line argument or use default
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ Invalid port number. Using default port 8000.")
    
    # Start the server
    start_server(port)

if __name__ == "__main__":
    main()
