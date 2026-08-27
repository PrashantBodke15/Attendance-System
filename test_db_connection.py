import mysql.connector
from mysql.connector import Error

def test_connection():
    """Test MySQL connection with the correct password"""
    
    print("Testing MySQL connection...")
    
    try:
        # Test connection
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vaishnavi@18",
            database="face_recognizer"
        )
        
        if conn.is_connected():
            print("✅ MySQL connection successful!")
            
            # Test a simple query
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM student")
            count = cursor.fetchone()[0]
            print(f"✅ Database query successful! Students in database: {count}")
            
            cursor.close()
            conn.close()
            return True
            
    except Error as e:
        print(f"❌ MySQL connection failed: {e}")
        
        if e.errno == 1045:
            print("\n🔧 Troubleshooting steps:")
            print("1. Check if MySQL server is running")
            print("2. Verify the password 'vaishnavi@18' is correct")
            print("3. Try resetting MySQL root password")
            
        elif e.errno == 1049:
            print("\n🔧 Database doesn't exist. Creating it...")
            try:
                # Connect without database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="vaishnavi@18"
                )
                cursor = conn.cursor()
                cursor.execute("CREATE DATABASE face_recognizer")
                print("✅ Database 'face_recognizer' created successfully!")
                conn.close()
                return test_connection()  # Test again
            except Error as create_error:
                print(f"❌ Failed to create database: {create_error}")
        
        return False

def reset_mysql_password():
    """Instructions to reset MySQL password"""
    
    print("\n🔧 To reset MySQL root password:")
    print("1. Stop MySQL service")
    print("2. Start MySQL with --skip-grant-tables")
    print("3. Connect as root without password")
    print("4. Run: ALTER USER 'root'@'localhost' IDENTIFIED BY 'vaishnavi@18';")
    print("5. Restart MySQL service normally")

if __name__ == "__main__":
    if not test_connection():
        reset_mysql_password()