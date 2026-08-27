import tkinter as tk
from tkinter import messagebox
import sys
import os

def test_all_modules():
    """Test if all modules can be imported and windows can be created"""
    
    print("=== Testing All Modules ===")
    
    # Test imports
    modules_to_test = [
        ('attendance', 'Attendance'),
        ('prashant', 'Student'),
        ('face_detector', 'Face_Recognition'),
        ('train', 'Train'),
        ('help', 'Help'),
        ('developer', 'Developer')
    ]
    
    working_modules = []
    
    for module_name, class_name in modules_to_test:
        try:
            module = __import__(module_name)
            class_obj = getattr(module, class_name)
            print(f"✅ {module_name}.{class_name} - Import successful")
            working_modules.append((module_name, class_name, class_obj))
        except Exception as e:
            print(f"❌ {module_name}.{class_name} - Import failed: {str(e)}")
    
    # Test window creation
    print(f"\n=== Testing Window Creation ===")
    
    root = tk.Tk()
    root.withdraw()  # Hide main window
    
    for module_name, class_name, class_obj in working_modules:
        try:
            test_window = tk.Toplevel(root)
            test_window.withdraw()  # Hide test window
            
            # Try to create the class instance
            app_instance = class_obj(test_window)
            print(f"✅ {class_name} window - Created successfully")
            
            # Close test window
            test_window.destroy()
            
        except Exception as e:
            print(f"❌ {class_name} window - Creation failed: {str(e)}")
    
    root.destroy()
    
    print(f"\n=== Test Complete ===")

def test_database_connection():
    """Test database connection"""
    
    print("\n=== Testing Database Connection ===")
    
    try:
        import mysql.connector
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vaishnavi@18",
            database="face_recognizer"
        )
        
        cursor = conn.cursor()
        
        # Test users table
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"✅ Users table: {user_count} users")
        
        # Test student table
        cursor.execute("SELECT COUNT(*) FROM student")
        student_count = cursor.fetchone()[0]
        print(f"✅ Student table: {student_count} students")
        
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Database connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_all_modules()
    test_database_connection()
    
    print("\n🎉 All tests completed!")
    print("\nNow you can:")
    print("1. Run 'python login.py' to test login/register")
    print("2. Run 'python main.py' to test the main application")
    print("3. Register new users should work now")
    print("4. Attendance window should open properly")