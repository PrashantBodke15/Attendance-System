import mysql.connector
import os
import shutil

def fix_student_id_mismatch():
    """Fix the mismatch between training data IDs and database IDs"""
    
    print("=== Fixing Student ID Mismatch ===")
    
    # Get database students
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            username="root", 
            password="vaishnavi@18", 
            database="face_recognizer"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT Student_id, Name FROM student ORDER BY Student_id")
        db_students = cursor.fetchall()
        
        print("Current database students:")
        for i, (student_id, name) in enumerate(db_students):
            print(f"  {i+1}. ID: {student_id}, Name: {name}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False
    
    # Check training data
    data_dir = "data"
    if not os.path.exists(data_dir):
        print("❌ No training data found")
        return False
    
    image_files = [f for f in os.listdir(data_dir) if f.endswith('.jpg')]
    training_ids = set()
    
    for img_file in image_files:
        parts = img_file.split('.')
        if len(parts) >= 3:
            try:
                student_id = int(parts[1])
                training_ids.add(student_id)
            except ValueError:
                pass
    
    print(f"\nTraining data has IDs: {sorted(training_ids)}")
    print(f"Database has IDs: {[s[0] for s in db_students]}")
    
    # Solution options
    print("\n=== Solution Options ===")
    print("1. Update database IDs to match training data (2, 5, 6)")
    print("2. Rename training files to match database IDs")
    print("3. Delete old training data and capture new photos")
    
    choice = input("\nChoose option (1/2/3): ").strip()
    
    if choice == "1":
        return update_database_ids(db_students, sorted(training_ids))
    elif choice == "2":
        return rename_training_files(db_students, sorted(training_ids))
    elif choice == "3":
        return delete_old_training_data()
    else:
        print("Invalid choice")
        return False

def update_database_ids(db_students, training_ids):
    """Update database student IDs to match training data"""
    
    print("\n=== Updating Database IDs ===")
    
    if len(db_students) != len(training_ids):
        print(f"❌ Mismatch: {len(db_students)} students in DB, {len(training_ids)} training IDs")
        return False
    
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            username="root", 
            password="vaishnavi@18", 
            database="face_recognizer"
        )
        cursor = conn.cursor()
        
        # Create mapping
        id_mapping = {}
        for i, (old_id, name) in enumerate(db_students):
            new_id = training_ids[i]
            id_mapping[old_id] = new_id
            print(f"  {name}: {old_id} -> {new_id}")
        
        # Update each student
        for old_id, new_id in id_mapping.items():
            cursor.execute("UPDATE student SET Student_id = %s WHERE Student_id = %s", (str(new_id), old_id))
            print(f"✅ Updated student ID {old_id} to {new_id}")
        
        conn.commit()
        conn.close()
        
        print("✅ Database IDs updated successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Update failed: {e}")
        return False

def rename_training_files(db_students, training_ids):
    """Rename training files to match database IDs"""
    
    print("\n=== Renaming Training Files ===")
    
    if len(db_students) != len(training_ids):
        print(f"❌ Mismatch: {len(db_students)} students in DB, {len(training_ids)} training IDs")
        return False
    
    try:
        data_dir = "data"
        backup_dir = "data_backup"
        
        # Create backup
        if os.path.exists(backup_dir):
            shutil.rmtree(backup_dir)
        shutil.copytree(data_dir, backup_dir)
        print("✅ Created backup of training data")
        
        # Create mapping
        id_mapping = {}
        for i, (db_id, name) in enumerate(db_students):
            training_id = training_ids[i]
            id_mapping[training_id] = db_id
            print(f"  Training ID {training_id} -> Database ID {db_id} ({name})")
        
        # Rename files
        for old_file in os.listdir(data_dir):
            if old_file.endswith('.jpg'):
                parts = old_file.split('.')
                if len(parts) >= 3:
                    try:
                        old_training_id = int(parts[1])
                        if old_training_id in id_mapping:
                            new_db_id = id_mapping[old_training_id]
                            new_file = f"user.{new_db_id}.{parts[2]}.jpg"
                            
                            old_path = os.path.join(data_dir, old_file)
                            new_path = os.path.join(data_dir, new_file)
                            
                            os.rename(old_path, new_path)
                            print(f"  Renamed: {old_file} -> {new_file}")
                    except ValueError:
                        pass
        
        print("✅ Training files renamed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Rename failed: {e}")
        return False

def delete_old_training_data():
    """Delete old training data so user can capture new photos"""
    
    print("\n=== Deleting Old Training Data ===")
    
    confirm = input("This will delete all training images. Are you sure? (yes/no): ")
    if confirm.lower() != 'yes':
        print("Operation cancelled")
        return False
    
    try:
        data_dir = "data"
        backup_dir = "data_old"
        
        # Create backup
        if os.path.exists(backup_dir):
            shutil.rmtree(backup_dir)
        shutil.move(data_dir, backup_dir)
        os.makedirs(data_dir)
        
        print("✅ Old training data moved to 'data_old' folder")
        print("✅ New empty 'data' folder created")
        print("\nNext steps:")
        print("1. Go to Student Details")
        print("2. Select a student")
        print("3. Click 'Take Photo Sample'")
        print("4. Repeat for all students")
        print("5. Click 'Train Data'")
        
        return True
        
    except Exception as e:
        print(f"❌ Delete failed: {e}")
        return False

if __name__ == "__main__":
    fix_student_id_mismatch()