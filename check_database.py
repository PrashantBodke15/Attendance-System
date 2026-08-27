import mysql.connector

def check_and_fix_database():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost", 
            username="root", 
            password="vaishnavi@18"
        )
        my_cursor = conn.cursor()
        
        # Create database if not exists
        my_cursor.execute("CREATE DATABASE IF NOT EXISTS face_recognizer")
        my_cursor.execute("USE face_recognizer")
        
        # Check if table exists and get its structure
        my_cursor.execute("SHOW TABLES LIKE 'student'")
        table_exists = my_cursor.fetchone()
        
        if table_exists:
            print("Table 'student' exists. Checking structure...")
            my_cursor.execute("DESCRIBE student")
            columns = my_cursor.fetchall()
            print("Current table structure:")
            for col in columns:
                print(f"  {col[0]} - {col[1]}")
            
            # Drop and recreate table with correct structure
            print("\nDropping existing table and creating new one...")
            my_cursor.execute("DROP TABLE student")
        
        # Create table with correct structure
        create_table_query = """
        CREATE TABLE student (
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
        
        my_cursor.execute(create_table_query)
        conn.commit()
        
        print("Table created successfully with correct structure!")
        
        # Verify the new structure
        my_cursor.execute("DESCRIBE student")
        columns = my_cursor.fetchall()
        print("\nNew table structure:")
        for col in columns:
            print(f"  {col[0]} - {col[1]}")
        
        conn.close()
        print("\nDatabase setup completed successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_and_fix_database()