#!/usr/bin/env python3
"""
GoPredict API Startup Script

This script starts the FastAPI server for the GoPredict machine learning project.
It handles environment setup and provides different run modes.
"""

import os
import sys
import uvicorn
import argparse
from pathlib import Path

def setup_environment():
    """Setup environment variables and paths"""
    # Add src to Python path
    src_path = Path(__file__).parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    # Set environment variables
    os.environ.setdefault("PYTHONPATH", str(src_path))
    
    # Debug information
    print(f"🔧 Environment Setup:")
    print(f"   Current working directory: {os.getcwd()}")
    print(f"   Script location: {Path(__file__).parent}")
    print(f"   Src path: {src_path}")
    print(f"   Src path exists: {src_path.exists()}")
    print(f"   Python path: {sys.path[:3]}...")  # Show first 3 entries

def main():
    """Main function to start the API server"""
    parser = argparse.ArgumentParser(description="GoPredict API Server")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind to")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload")
    parser.add_argument("--log-level", default="info", choices=["debug", "info", "warning", "error"])
    parser.add_argument("--workers", type=int, default=1, help="Number of worker processes")
    
    args = parser.parse_args()
    
    # Setup environment
    setup_environment()
    
    print("🚀 Starting GoPredict API Server...")
    print(f"   Host: {args.host}")
    print(f"   Port: {args.port}")
    print(f"   Reload: {args.reload}")
    print(f"   Log Level: {args.log_level}")
    print(f"   Workers: {args.workers}")
    print("=" * 50)
    
    # Test import before starting server
    try:
        print("🔍 Testing API import...")
        import api.main
        print("✅ API module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import API module: {e}")
        print("   This might indicate a path or dependency issue")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error importing API module: {e}")
        sys.exit(1)
    
    # Start the server
    uvicorn.run(
        "api.main:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level=args.log_level,
        workers=args.workers if not args.reload else 1
    )

if __name__ == "__main__":
    main()
