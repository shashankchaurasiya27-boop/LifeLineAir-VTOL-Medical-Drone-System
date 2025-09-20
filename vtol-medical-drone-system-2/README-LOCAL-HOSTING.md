# 🚁 VTOL Medical Drone System - Local Hosting Guide

This guide will help you host the VTOL Medical Drone System locally on your machine without using Streamlit.

## 🚀 Quick Start

### Option 1: Simple HTTP Server (Recommended)
```bash
# Navigate to the project directory
cd /path/to/vtol-medical-drone-system-2

# Start the server (Python 3.6+)
python start_server.py

# Or specify a custom port
python start_server.py 8080
```

### Option 2: Advanced Server with API Endpoints
```bash
# Start the advanced server with API support
python server.py

# Or specify a custom port
python server.py 8080
```

### Option 3: Built-in Python Server
```bash
# For Python 3.7+
python -m http.server 8000

# For Python 2.7 (if still using)
python -m SimpleHTTPServer 8000
```

## 🌐 Access the Application

Once the server is running, open your web browser and navigate to:

- **Main Application**: http://localhost:8000
- **Custom Port**: http://localhost:[YOUR_PORT]

## 🔐 Login Credentials

The application includes demo login credentials:

| Role | Username | Password |
|------|----------|----------|
| Administrator | admin | admin123 |
| Fleet Manager | fleet_mgr | fleet123 |
| Medical Coordinator | medical | medical123 |
| Observer | demo | demo123 |

## 📁 Project Structure

```
vtol-medical-drone-system-2/
├── index.html          # Main application HTML
├── app.js             # JavaScript application logic
├── style.css          # Application styling
├── server.py          # Advanced server with API endpoints
├── start_server.py    # Simple server startup script
├── requirements-local.txt  # Minimal dependencies
└── README-LOCAL-HOSTING.md # This file
```

## 🛠️ Features

### ✅ What Works Locally
- Complete web interface
- User authentication
- Dashboard with real-time data simulation
- Fleet management interface
- Analytics and charts
- Medical inventory tracking
- Maintenance scheduling
- Flight tracking interface
- Responsive design
- Dark/light mode support

### 🔧 API Endpoints (Advanced Server)
- `GET /api/status` - System status
- `GET /api/fleet` - Fleet data
- `GET /api/alerts` - Alert information
- `GET /api/metrics` - Performance metrics

## 🚨 Troubleshooting

### Port Already in Use
```bash
# Try a different port
python start_server.py 8080
python start_server.py 3000
```

### Permission Denied
```bash
# Make the script executable (Linux/Mac)
chmod +x start_server.py
chmod +x server.py
```

### Python Not Found
- Ensure Python 3.6+ is installed
- Try `python3` instead of `python`
- On Windows, try `py` instead of `python`

### Browser Not Opening Automatically
- Manually navigate to http://localhost:8000
- Check if your firewall is blocking the connection

## 🔄 Development Mode

For development with auto-reload:

```bash
# Install watchdog for file watching (optional)
pip install watchdog

# The server will automatically serve updated files
python start_server.py
```

## 📱 Mobile Access

The application is responsive and can be accessed from mobile devices on your local network:

1. Find your computer's IP address
2. Access from mobile: http://[YOUR_IP]:8000
3. Ensure your firewall allows connections on the port

## 🎯 Next Steps

1. **Customize Data**: Modify the data in `app.js` to reflect your specific drone fleet
2. **Add Real APIs**: Replace mock data with real API calls
3. **Database Integration**: Add a database for persistent data storage
4. **Authentication**: Implement real user authentication
5. **Real-time Updates**: Add WebSocket support for live data updates

## 📞 Support

If you encounter any issues:

1. Check that all files are present in the directory
2. Ensure Python 3.6+ is installed
3. Try different ports if the default is busy
4. Check your firewall settings

## 🎉 Enjoy Your Local VTOL Medical Drone System!

The application is now running locally and ready for use. All features are functional with simulated data, providing a complete demonstration of the VTOL Medical Drone System capabilities.
