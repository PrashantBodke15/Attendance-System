#!/usr/bin/env python3

print("Testing imports...")

try:
    print("1. Testing face_detector import...")
    from face_detector import Face_Recognition
    print("✅ face_detector imported successfully")
except Exception as e:
    print(f"❌ face_detector import failed: {e}")

try:
    print("2. Testing main import...")
    from main import Face_Recognization_system
    print("✅ main imported successfully")
except Exception as e:
    print(f"❌ main import failed: {e}")

try:
    print("3. Testing attendance import...")
    from attendance import Attendance
    print("✅ attendance imported successfully")
except Exception as e:
    print(f"❌ attendance import failed: {e}")

try:
    print("4. Testing prashant import...")
    from prashant import Student
    print("✅ prashant imported successfully")
except Exception as e:
    print(f"❌ prashant import failed: {e}")

print("Import test completed!")