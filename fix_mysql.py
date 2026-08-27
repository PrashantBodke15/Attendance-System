import mysql.connector
from mysql.connector import Error
import getpass

def test_mysql_connection():
    """Test MySQL connection with different scenarios"""
    
    print("=== MySQL Connection Troubleshooter ===")
    
    # Test 1: Try with current password
    print("\n1. Testing with current password 'vaishnavi@18'...")
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='vaishnavi@18'
        )
        print("✅ Connection successful with 'vaishnavi@18'")
        conn.close()
        return setup_database('vaishnavi@18')
    except Error as err:
        print(f"❌ Failed: {err}")
    
    # Test 2: Try with empty password
    print("\n2. Testing with empty password...")
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        print("✅ Connection successful with empty password")
        conn.close()
        return setup_database('')
    except Error as err:
        print(f"❌ Failed: {err}")
    
    # Test 3: Ask user for password
    print("\n3. Please enter your MySQL root password:")
    password = getpass.getpass("MySQL root password: ")
    
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=password
        )
        print("✅ Connection successful with provided password")
        conn.close()
        return setup_database(password)
    except Error as err:
        print(f"❌ Failed: {err}")
        return False

def setup_database(password):
    """Setup the face_recognizer database"""
    
    try:
        print("\n=== Setting up database ===")
        
        # Connect to MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=password
        )
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS face_recognizer")
        print("✅ Database 'face_recognizer' created/verified")
        
        # Use the database
        cursor.execute("USE face_recognizer")
        
        # Create student table
        create_table_query = """
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
        cursor.execute(create_table_query)
        print("✅ Student table created/verified")
        
        conn.commit()
        conn.close()
        
        # Update config file
        update_config_file(password)
        
        print(f"\n✅ Database setup completed successfully!")
        print(f"Password to use: '{password}'")
        return True
        
    except Error as err:
        print(f"❌ Database setup failed: {err}")
        return False

def update_config_file(password):
    """Update the database configuration file"""
    
    config_content = f"""# Database configuration
DB_CONFIG = {{
    'host': 'localhost',
    'username': 'root',
    'password': '{password}',
    'database': 'face_recognizer'
}}

def get_db_connection():
    \"\"\"Get database connection with error handling\"\"\"
    import mysql.connector
    from tkinter import messagebox
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        if err.errno == 1045:  # Access denied error
            messagebox.showerror("Database Error", 
                               f"Access denied for user '{DB_CONFIG['username']}'@'{DB_CONFIG['host']}'\\n\\n"
                               "Please check:\\n"
                               "1. MySQL password is correct\\n"
                               "2. MySQL server is running\\n"
                               "3. User has proper permissions")
        elif err.errno == 1049:  # Unknown database error
            messagebox.showerror("Database Error", 
                               f"Database '{DB_CONFIG['database']}' doesn't exist\\n\\n"
                               "Please create the database first")
        else:
            messagebox.showerror("Database Error", f"Database connection failed: {str(err)}")
        return None

def test_db_connection():
    \"\"\"Test database connection\"\"\"
    conn = get_db_connection()
    if conn:
        print("✅ Database connection successful!")
        conn.close()
        return True
    else:
        print("❌ Database connection failed!")
        return False"""
    
    with open('db_config.py', 'w') as f:
        f.write(config_content)
    
    print("✅ Updated db_config.py with correct password")

if __name__ == "__main__":
    if test_mysql_connection():
        print("\n🎉 MySQL setup completed successfully!")
        print("You can now run your face recognition application.")
    else:
        print("\n❌ MySQL setup failed.")
        print("Please check:")
        print("1. MySQL server is running")
        print("2. You have the correct root password")
        print("3. MySQL is properly installed")