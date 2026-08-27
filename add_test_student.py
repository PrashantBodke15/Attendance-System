import mysql.connector
from tkinter import messagebox

def add_test_student():
    """Add a test student to the database"""
    
    try:
        conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
        my_cursor = conn.cursor()
        
        # Check if student already exists
        my_cursor.execute("SELECT * FROM student WHERE Student_id='1'")
        existing = my_cursor.fetchone()
        
        if existing:
            print("Test student already exists!")
            conn.close()
            return True
        
        # Add test student
        my_cursor.execute("""INSERT INTO student 
                           (Dep, course, Year, Semester, Student_id, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample) 
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                         ("Computer Science", "MCA-I", "2025-26", "semester-1", "1", "Test Student", "A", "101", 
                          "Male", "01/01/2000", "test@email.com", "1234567890", "Test Address", "Test Teacher", "Yes"))
        
        conn.commit()
        conn.close()
        
        print("✅ Test student added successfully!")
        print("Student ID: 1")
        print("Name: Test Student")
        return True
        
    except Exception as e:
        print(f"❌ Error adding test student: {str(e)}")
        return False

if __name__ == "__main__":
    add_test_student()