#!/usr/bin/env python3
"""
GoPredict API Test Script

This script tests the main API endpoints to ensure they're working correctly.
"""

import requests
import json
import time
from datetime import datetime

API_BASE_URL = "http://localhost:8000"

def test_health():
    """Test the health endpoint"""
    print("Testing health endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/health")
        if response.status_code == 200:
            print("Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"Health check failed: {response.status_code}")
    except Exception as e:
        print(f"Health check error: {e}")

def test_status():
    """Test the status endpoint"""
    print("\nTesting status endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/status")
        if response.status_code == 200:
            print("Status check passed")
            data = response.json()
            print(f"   Models available: {data['status']['models_count']}")
            print(f"   Pipeline ready: {data['status']['pipeline_ready']}")
        else:
            print(f"Status check failed: {response.status_code}")
    except Exception as e:
        print(f"Status check error: {e}")

def test_weather():
    """Test the weather endpoint"""
    print("\nTesting weather endpoint...")
    try:
        params = {
            "latitude": 40.767937,
            "longitude": -73.982155,
            "timestamp": "2016-01-01T17:00:00"
        }
        response = requests.get(f"{API_BASE_URL}/weather", params=params)
        if response.status_code == 200:
            print("Weather API test passed")
            data = response.json()
            print(f"   Temperature: {data['data'].get('temp', 'N/A')}")
            print(f"   Humidity: {data['data'].get('humidity', 'N/A')}")
        else:
            print(f"Weather API test failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"Weather API test error: {e}")

def test_distance():
    """Test the distance calculation endpoint"""
    print("\nTesting distance calculation endpoint...")
    try:
        params = {
            "start_lat": 40.767937,
            "start_lng": -73.982155,
            "end_lat": 40.748817,
            "end_lng": -73.985428,
            "method": "both"
        }
        response = requests.post(f"{API_BASE_URL}/distance", params=params)
        if response.status_code == 200:
            print("Distance calculation test passed")
            result = response.json()
            print(f"   Manhattan distance: {result['data'].get('manhattan_distance', 'N/A')}")
            print(f"   Euclidean distance: {result['data'].get('euclidean_distance', 'N/A')}")
        else:
            print(f"Distance calculation test failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"Distance calculation test error: {e}")

def test_time_features():
    """Test the time features endpoint"""
    print("\nTesting time features endpoint...")
    try:
        params = {"datetime_str": "2016-01-01T17:00:00"}
        response = requests.post(f"{API_BASE_URL}/time-features", params=params)
        if response.status_code == 200:
            print("Time features test passed")
            result = response.json()
            print(f"   Weekday: {result['data']['weekday']}")
            print(f"   Hour: {result['data']['hour']}")
            print(f"   Holiday: {result['data']['holiday']}")
        else:
            print(f"Time features test failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"Time features test error: {e}")

def test_models():
    """Test the models endpoint"""
    print("\nTesting models endpoint...")
    try:
        response = requests.get(f"{API_BASE_URL}/models")
        if response.status_code == 200:
            print("Models endpoint test passed")
            data = response.json()
            print(f"   Available models: {data['models']}")
            print(f"   Model count: {data['count']}")
        else:
            print(f"Models endpoint test failed: {response.status_code}")
    except Exception as e:
        print(f"Models endpoint test error: {e}")

def test_prediction():
    """Test the prediction endpoint (if models are available)"""
    print("\nTesting prediction endpoint...")
    try:
        # Test with the new frontend format
        data = {
            "from": {"lat": 40.767937, "lon": -73.982155},
            "to": {"lat": 40.748817, "lon": -73.985428},
            "startTime": "2016-01-01T17:00:00",
            "city": "new_york"
        }
        response = requests.post(f"{API_BASE_URL}/predict", json=data)
        if response.status_code == 200:
            print("Prediction test passed")
            result = response.json()
            print(f"   Predicted duration: {result['minutes']:.2f} minutes")
            print(f"   Distance: {result['distance_km']:.2f} km")
            print(f"   Confidence: {result['confidence']}")
        else:
            print(f"Prediction test failed: {response.status_code}")
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"Prediction test error: {e}")

def main():
    """Run all tests"""
    print("Starting GoPredict API Tests")
    print("=" * 50)
    
    # Wait a moment for the server to be ready
    print("Waiting for API server to be ready...")
    time.sleep(2)
    
    # Run tests
    test_health()
    test_status()
    test_weather()
    test_distance()
    test_time_features()
    test_models()
    test_prediction()
    
    print("\n" + "=" * 50)
    print("API testing completed!")
    print("\nTo view the interactive API documentation, visit:")
    print("   http://localhost:8000/docs")

if __name__ == "__main__":
    main()