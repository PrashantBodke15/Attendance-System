import mysql.connector

def create_users_table():
    """Create the users table with correct structure"""
    
    try:
        # Connect to database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vaishnavi@18",
            database="face_recognizer"
        )
        cursor = conn.cursor()
        
        # Drop existing table
        cursor.execute("DROP TABLE IF EXISTS users")
        print("Dropped existing users table")
        
        # Create new table with correct structure
        create_table_sql = """
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            contact VARCHAR(20),
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        
        cursor.execute(create_table_sql)
        print("✅ Created users table with correct structure")
        
        # Add test user
        cursor.execute("""
            INSERT INTO users (first_name, last_name, contact, email, password) 
            VALUES (%s, %s, %s, %s, %s)
        """, ("Admin", "User", "1234567890", "admin@test.com", "admin123"))
        
        print("✅ Added test user")
        
        # Show table structure
        cursor.execute("DESCRIBE users")
        columns = cursor.fetchall()
        print("\nTable structure:")
        for col in columns:
            print(f"  {col[0]} - {col[1]}")
        
        conn.commit()
        conn.close()
        
        print("\n✅ Database setup completed!")
        print("You can now register new users!")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    create_users_table()