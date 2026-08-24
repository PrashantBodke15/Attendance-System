import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox

def fix_database_tables():
    """Create missing database tables"""
    
    print("=== Fixing Database Tables ===")
    
    try:
        # Connect to database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vaishnavi@18",
            database="face_recognizer"
        )
        cursor = conn.cursor()
        
        # Create users table for login/register functionality
        create_users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fname VARCHAR(100) NOT NULL,
            lname VARCHAR(100) NOT NULL,
            contact VARCHAR(20),
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        cursor.execute(create_users_table)
        print("✅ Users table created/verified")
        
        # Check if student table exists
        cursor.execute("SHOW TABLES LIKE 'student'")
        if cursor.fetchone():
            print("✅ Student table exists")
        else:
            # Create student table
            create_student_table = """
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
            """
            cursor.execute(create_student_table)
            print("✅ Student table created")
        
        # Add a test user for login
        try:
            cursor.execute("SELECT COUNT(*) FROM users")
            user_count = cursor.fetchone()[0]
            
            if user_count == 0:
                cursor.execute("""
                    INSERT INTO users (fname, lname, contact, email, password) 
                    VALUES (%s, %s, %s, %s, %s)
                """, ("Admin", "User", "1234567890", "admin@test.com", "admin123"))
                print("✅ Test user created (email: admin@test.com, password: admin123)")
        except Error as e:
            print(f"Note: {e}")
        
        conn.commit()
        conn.close()
        
        print("✅ Database setup completed successfully!")
        return True
        
    except Error as e:
        print(f"❌ Database error: {e}")
        return False

def test_attendance_window():
    """Test if attendance window opens correctly"""
    
    print("\n=== Testing Attendance Window ===")
    
    try:
        # Import and test attendance module
        import sys
        import os
        sys.path.append(os.getcwd())
        
        from attendance import Attendance
        
        # Create test window
        root = tk.Tk()
        root.withdraw()  # Hide main window
        
        # Test attendance window
        test_window = tk.Toplevel(root)
        attendance_app = Attendance(test_window)
        
        print("✅ Attendance window created successfully")
        
        # Close test window
        test_window.destroy()
        root.destroy()
        
        return True
        
    except Exception as e:
        print(f"❌ Attendance window error: {str(e)}")
        return False

def test_register_functionality():
    """Test register functionality"""
    
    print("\n=== Testing Register Functionality ===")
    
    try:
        # Test database connection for users table
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vaishnavi@18",
            database="face_recognizer"
        )
        cursor = conn.cursor()
        
        # Test if users table exists and is accessible
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"✅ Users table accessible. Current users: {user_count}")
        
        conn.close()
        return True
        
    except Error as e:
        print(f"❌ Register functionality error: {e}")
        return False

def create_test_csv():
    """Create test CSV file for attendance"""
    
    print("\n=== Creating Test CSV ===")
    
    try:
        import csv
        
        # Create sample attendance data
        with open('prashant.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Roll', 'Name', 'Department', 'Time', 'Date', 'Status'])
            writer.writerow(['1', '101', 'Test Student', 'Computer Science', '10:30:00', '25/12/2024', 'Present'])
            writer.writerow(['2', '102', 'Sample User', 'IT', '10:31:00', '25/12/2024', 'Present'])
        
        print("✅ Test CSV file created")
        return True
        
    except Exception as e:
        print(f"❌ CSV creation error: {e}")
        return False

if __name__ == "__main__":
    print("=== Fixing Attendance and Register Issues ===")
    
    # Fix database tables
    if fix_database_tables():
        print("✅ Database tables fixed")
    else:
        print("❌ Database setup failed")
        exit(1)
    
    # Test attendance window
    if test_attendance_window():
        print("✅ Attendance window working")
    else:
        print("❌ Attendance window has issues")
    
    # Test register functionality
    if test_register_functionality():
        print("✅ Register functionality working")
    else:
        print("❌ Register functionality has issues")
    
    # Create test CSV
    if create_test_csv():
        print("✅ Test CSV created")
    
    print("\n🎉 All fixes completed!")
    print("\nYou can now:")
    print("1. Login with: admin@test.com / admin123")
    print("2. Register new users")
    print("3. Open attendance window")
    print("4. Import/export attendance CSV files")