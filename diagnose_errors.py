import sys
import traceback
import mysql.connector
import cv2
import os
from tkinter import *
from tkinter import messagebox
import numpy as np

def diagnose_system():
    """Comprehensive system diagnosis"""
    
    print("=== System Diagnosis ===")
    
    # Check Python version
    print(f"Python Version: {sys.version}")
    
    # Check required modules
    modules_to_check = [
        'mysql.connector',
        'cv2',
        'tkinter',
        'PIL',
        'numpy'
    ]
    
    print("\n=== Module Check ===")
    for module in modules_to_check:
        try:
            if module == 'mysql.connector':
                import mysql.connector
                print(f"✅ {module}: {mysql.connector.__version__}")
            elif module == 'cv2':
                import cv2
                print(f"✅ {module}: {cv2.__version__}")
            elif module == 'tkinter':
                import tkinter
                print(f"✅ {module}: Available")
            elif module == 'PIL':
                from PIL import Image
                print(f"✅ {module}: Available")
            elif module == 'numpy':
                import numpy
                print(f"✅ {module}: {numpy.__version__}")
        except ImportError as e:
            print(f"❌ {module}: Not installed - {str(e)}")
    
    # Check files
    print("\n=== File Check ===")
    required_files = [
        'main.py',
        'prashant.py',
        'face_detector.py',
        'haarcascade_frontalface_default.xml'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}: Found")
        else:
            print(f"❌ {file}: Missing")
    
    # Check directories
    print("\n=== Directory Check ===")
    required_dirs = ['data', 'project images']
    
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name}: Found")
        else:
            print(f"❌ {dir_name}: Missing")
            try:
                os.makedirs(dir_name)
                print(f"  Created {dir_name}")
            except Exception as e:
                print(f"  Failed to create {dir_name}: {str(e)}")
    
    # Test MySQL connection
    print("\n=== MySQL Connection Test ===")
    test_mysql_connections()
    
    # Test OpenCV
    print("\n=== OpenCV Test ===")
    test_opencv()
    
    # Test camera
    print("\n=== Camera Test ===")
    test_camera()

def test_mysql_connections():
    """Test different MySQL connection scenarios"""
    
    passwords_to_try = ['vaishnavi@18', '', 'root', 'password', '123456']
    
    for password in passwords_to_try:
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password=password
            )
            print(f"✅ MySQL connection successful with password: '{password}'")
            
            # Test database creation
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS face_recognizer")
            cursor.execute("USE face_recognizer")
            
            # Test table creation
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS student (
                    Dep VARCHAR(100),
                    course VARCHAR(100),
                    Year VARCHAR(20),
                    Semester VARCHAR(20),
                    Student_id VARCHAR(50) PRIMARY KEY,
                    Name VARCHAR(100),
                    Division VARCHAR(50),
                    Roll VARCHAR(50),
                    Gender VARCHAR(20),
                    Dob VARCHAR(50),
                    Email VARCHAR(100),
                    Phone VARCHAR(20),
                    Address TEXT,
                    Teacher VARCHAR(100),
                    PhotoSample VARCHAR(10)
                )
            """)
            
            conn.commit()
            conn.close()
            
            print(f"✅ Database and table setup successful")
            
            # Update all Python files with correct password
            update_password_in_files(password)
            return True
            
        except mysql.connector.Error as err:
            print(f"❌ MySQL failed with password '{password}': {err}")
    
    print("❌ All MySQL connection attempts failed")
    return False

def update_password_in_files(correct_password):
    """Update password in all Python files"""
    
    files_to_update = ['prashant.py', 'face_detector.py', 'add_test_student.py', 'setup_face_recognition.py']
    
    for filename in files_to_update:
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as f:
                    content = f.read()
                
                # Replace password patterns
                content = content.replace('password="vaishnavi@18"', f'password="{correct_password}"')
                content = content.replace("password='vaishnavi@18'", f"password='{correct_password}'")
                content = content.replace('password="test@123"', f'password="{correct_password}"')
                content = content.replace("password='test@123'", f"password='{correct_password}'")
                
                with open(filename, 'w') as f:
                    f.write(content)
                
                print(f"✅ Updated password in {filename}")
                
            except Exception as e:
                print(f"❌ Failed to update {filename}: {str(e)}")

def test_opencv():
    """Test OpenCV functionality"""
    
    try:
        # Test cascade loading
        cascade_file = "haarcascade_frontalface_default.xml"
        if os.path.exists(cascade_file):
            face_cascade = cv2.CascadeClassifier(cascade_file)
            if face_cascade.empty():
                print("❌ Local cascade file is corrupted")
                # Try built-in cascade
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                if face_cascade.empty():
                    print("❌ Built-in cascade also failed")
                    return False
                else:
                    print("✅ Built-in cascade works")
            else:
                print("✅ Local cascade file works")
        else:
            print("❌ Cascade file not found")
            return False
        
        # Test face recognition module
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            print("✅ Face recognition module available")
        except AttributeError:
            print("❌ Face recognition module not available (need opencv-contrib-python)")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ OpenCV test failed: {str(e)}")
        return False

def test_camera():
    """Test camera functionality"""
    
    try:
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                print("✅ Camera test successful")
                cap.release()
                return True
            else:
                print("❌ Camera can't capture frames")
        else:
            print("❌ Camera not accessible")
        
        cap.release()
        return False
        
    except Exception as e:
        print(f"❌ Camera test failed: {str(e)}")
        return False

def fix_common_issues():
    """Fix common issues automatically"""
    
    print("\n=== Fixing Common Issues ===")
    
    # Create missing directories
    dirs_to_create = ['data', 'project images']
    for dir_name in dirs_to_create:
        if not os.path.exists(dir_name):
            try:
                os.makedirs(dir_name)
                print(f"✅ Created directory: {dir_name}")
            except Exception as e:
                print(f"❌ Failed to create {dir_name}: {str(e)}")
    
    # Create CSV file if missing
    if not os.path.exists('prashant.csv'):
        try:
            with open('prashant.csv', 'w') as f:
                f.write("ID,Roll,Name,Department,Time,Date,Status\n")
            print("✅ Created prashant.csv")
        except Exception as e:
            print(f"❌ Failed to create CSV: {str(e)}")
    
    # Download cascade file if missing
    if not os.path.exists('haarcascade_frontalface_default.xml'):
        print("❌ Cascade file missing - please download it manually")
        print("URL: https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml")

if __name__ == "__main__":
    try:
        diagnose_system()
        fix_common_issues()
        
        print("\n=== Summary ===")
        print("If all tests passed, your system should work correctly.")
        print("If any tests failed, please address those issues first.")
        
    except Exception as e:
        print(f"\n❌ Diagnosis failed with error: {str(e)}")
        print("Full traceback:")
        traceback.print_exc()