# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'username': 'root',
    'password': 'vaishnavi@18',  # Update this with your MySQL password
    'database': 'face_recognizer'
}

def get_db_connection():
    """Get database connection with error handling"""
    import mysql.connector
    from tkinter import messagebox
    
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        if err.errno == 1045:  # Access denied error
            messagebox.showerror("Database Error", 
                               f"Access denied for user '{DB_CONFIG['username']}'@'{DB_CONFIG['host']}'\n\n"
                               "Please check:\n"
                               "1. MySQL password is correct\n"
                               "2. MySQL server is running\n"
                               "3. User has proper permissions")
        elif err.errno == 1049:  # Unknown database error
            messagebox.showerror("Database Error", 
                               f"Database '{DB_CONFIG['database']}' doesn't exist\n\n"
                               "Please create the database first")
        else:
            messagebox.showerror("Database Error", f"Database connection failed: {str(err)}")
        return None

def test_db_connection():
    """Test database connection"""
    conn = get_db_connection()
    if conn:
        print("✅ Database connection successful!")
        conn.close()
        return True
    else:
        print("❌ Database connection failed!")
        return False