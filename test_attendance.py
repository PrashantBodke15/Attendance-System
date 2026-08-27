from tkinter import *
from tkinter import messagebox
import sys
import os

def test_attendance_window():
    """Test if attendance window opens correctly"""
    
    print("Testing attendance window...")
    
    try:
        # Import the attendance module
        from attendance import Attendance
        
        # Create root window
        root = Tk()
        root.withdraw()  # Hide the root window
        
        # Try to create attendance window
        attendance_window = Toplevel(root)
        app = Attendance(attendance_window)
        
        print("✅ Attendance window created successfully!")
        
        # Show the window for 3 seconds then close
        attendance_window.after(3000, lambda: attendance_window.destroy())
        attendance_window.after(3100, lambda: root.destroy())
        
        root.mainloop()
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        return False
    except FileNotFoundError as e:
        print(f"❌ File not found: {str(e)}")
        print("Missing image files in 'project images' directory")
        return False
    except Exception as e:
        print(f"❌ Error creating attendance window: {str(e)}")
        return False

def check_required_files():
    """Check if all required files exist"""
    
    print("Checking required files...")
    
    required_files = [
        "attendance.py",
        "project images/image4.jpg",
        "project images/Image5.jpg", 
        "project images/bg.jpg",
        "project images/Image3.jpg"
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
            print(f"❌ Missing: {file_path}")
        else:
            print(f"✅ Found: {file_path}")
    
    if missing_files:
        print(f"\n⚠ {len(missing_files)} files are missing!")
        print("This might cause the attendance window to fail.")
        return False
    else:
        print("\n✅ All required files found!")
        return True

def create_dummy_images():
    """Create dummy images if they're missing"""
    
    print("Creating dummy images for missing files...")
    
    try:
        from PIL import Image
        
        # Create project images directory if it doesn't exist
        if not os.path.exists("project images"):
            os.makedirs("project images")
            print("✅ Created 'project images' directory")
        
        # Create dummy images
        dummy_files = [
            "project images/image4.jpg",
            "project images/Image5.jpg", 
            "project images/bg.jpg",
            "project images/Image3.jpg"
        ]
        
        for file_path in dummy_files:
            if not os.path.exists(file_path):
                # Create a simple colored image
                img = Image.new('RGB', (800, 200), color='lightblue')
                img.save(file_path)
                print(f"✅ Created dummy image: {file_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating dummy images: {str(e)}")
        return False

if __name__ == "__main__":
    print("=== Attendance Window Troubleshooter ===")
    
    # Check files first
    if not check_required_files():
        print("\nTrying to create missing image files...")
        if create_dummy_images():
            print("✅ Dummy images created successfully!")
        else:
            print("❌ Failed to create dummy images")
    
    # Test the attendance window
    print("\n" + "="*50)
    if test_attendance_window():
        print("\n🎉 Attendance window test passed!")
        print("The attendance window should now work in your main application.")
    else:
        print("\n❌ Attendance window test failed!")
        print("Please check the error messages above and fix the issues.")