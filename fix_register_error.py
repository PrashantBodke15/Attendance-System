import mysql.connector
from mysql.connector import Error

def fix_users_table():
    """Fix the users table structure to match the registration form"""
    
    print("=== Fixing Users Table Structure ===")
    
    try:
        # Connect to database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vaishnavi@18",
            database="face_recognizer"
        )
        cursor = conn.cursor()
        
        # Drop existing users table if it exists
        cursor.execute("DROP TABLE IF EXISTS users")
        print("✅ Dropped old users table")
        
        # Create new users table with correct column names
        create_users_table = """
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
        
        cursor.execute(create_users_table)
        print("✅ Created new users table with correct structure")
        
        # Add a test user
        cursor.execute("""
            INSERT INTO users (first_name, last_name, contact, email, password) 
            VALUES (%s, %s, %s, %s, %s)
        """, ("Admin", "User", "1234567890", "admin@test.com", "admin123"))
        
        print("✅ Added test user (email: admin@test.com, password: admin123)")
        
        # Verify table structure
        cursor.execute("DESCRIBE users")
        columns = cursor.fetchall()
        print("\n✅ New table structure:")
        for col in columns:
            print(f"  - {col[0]} ({col[1]})")
        
        conn.commit()
        conn.close()
        
        return True
        
    except Error as e:
        print(f"❌ Database error: {e}")
        return False

def update_login_code():
    """Update the login.py file to use correct column names"""
    
    print("\n=== Updating Login Code ===")
    
    try:
        # Read the current login.py file
        with open('login.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace incorrect column references
        content = content.replace('fname', 'first_name')
        content = content.replace('lname', 'last_name')
        
        # Fix the INSERT statement in register_user method
        old_insert = """cursor.execute("INSERT INTO users (fname, lname, contact, email, password) VALUES (%s, %s, %s, %s, %s)","""
        new_insert = """cursor.execute("INSERT INTO users (first_name, last_name, contact, email, password) VALUES (%s, %s, %s, %s, %s)","""
        
        content = content.replace(old_insert, new_insert)
        
        # Write the updated content back
        with open('login.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Updated login.py with correct column names")
        return True
        
    except Exception as e:
        print(f"❌ Error updating login.py: {e}")
        return False

if __name__ == "__main__":
    print("=== Fixing Registration Error ===")
    
    if fix_users_table():
        print("✅ Database table fixed")
        
        if update_login_code():
            print("✅ Code updated")
            print("\n🎉 Registration should now work!")
            print("\nTest credentials:")
            print("Email: admin@test.com")
            print("Password: admin123")
        else:
            print("❌ Code update failed")
    else:
        print("❌ Database fix failed")