import cv2
import os
import numpy as np
from PIL import Image
import mysql.connector
from tkinter import messagebox
import tkinter as tk

def setup_face_recognition():
    """Complete setup for face recognition system"""
    
    print("=== Face Recognition Setup ===")
    
    # Step 1: Check if we have students in database
    try:
        conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT COUNT(*) FROM student")
        student_count = my_cursor.fetchone()[0]
        print(f"Students in database: {student_count}")
        
        if student_count == 0:
            print("❌ No students found in database!")
            print("Please add students first using the Student Details form")
            conn.close()
            return False
        
        # Get student list
        my_cursor.execute("SELECT Student_id, Name FROM student")
        students = my_cursor.fetchall()
        print("Students found:")
        for student in students:
            print(f"  ID: {student[0]}, Name: {student[1]}")
        
        conn.close()
    except Exception as e:
        print(f"❌ Database error: {str(e)}")
        return False
    
    # Step 2: Check if we have training images
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created {data_dir} directory")
    
    image_files = [f for f in os.listdir(data_dir) if f.endswith('.jpg')]
    print(f"Training images found: {len(image_files)}")
    
    if len(image_files) == 0:
        print("❌ No training images found!")
        print("Please capture photos for students first using 'Take Photo Sample'")
        return False
    
    # Step 3: Train the model
    print("\n=== Training Face Recognition Model ===")
    
    try:
        faces = []
        ids = []
        
        for image_file in image_files:
            image_path = os.path.join(data_dir, image_file)
            img = Image.open(image_path).convert('L')  # Convert to grayscale
            img_np = np.array(img, 'uint8')
            
            # Extract ID from filename (format: user.ID.number.jpg)
            parts = image_file.split('.')
            if len(parts) >= 3:
                student_id = int(parts[1])
                faces.append(img_np)
                ids.append(student_id)
        
        if len(faces) == 0:
            print("❌ No valid training images found!")
            return False
        
        print(f"Processing {len(faces)} training images...")
        
        # Create and train the recognizer
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(ids))
        
        # Save the trained model
        recognizer.write("classifier.xml")
        print("✅ Face recognition model trained and saved as 'classifier.xml'")
        
        return True
        
    except Exception as e:
        print(f"❌ Training error: {str(e)}")
        return False

def test_face_recognition():
    """Test the face recognition system"""
    
    print("\n=== Testing Face Recognition ===")
    
    try:
        # Load cascade
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        if face_cascade.empty():
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        if face_cascade.empty():
            print("❌ Could not load face detection model")
            return False
        
        # Load trained recognizer
        if not os.path.exists("classifier.xml"):
            print("❌ No trained model found. Please run training first.")
            return False
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")
        
        # Connect to database
        conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
        my_cursor = conn.cursor()
        
        # Start camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Could not open camera")
            return False
        
        print("✅ Face recognition test started!")
        print("Press 'q' to quit or Enter to exit")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            for (x, y, w, h) in faces:
                # Draw rectangle around face
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
                # Recognize face
                face_roi = gray[y:y+h, x:x+w]
                id_, confidence = recognizer.predict(face_roi)
                
                if confidence < 100:  # Confidence threshold
                    # Get student info from database
                    my_cursor.execute("SELECT Name FROM student WHERE Student_id=%s", (str(id_),))
                    result = my_cursor.fetchone()
                    name = result[0] if result else "Unknown"
                    
                    # Display info
                    cv2.putText(frame, f"ID: {id_}", (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(frame, f"Name: {name}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.putText(frame, f"Confidence: {100-confidence:.1f}%", (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            
            cv2.imshow("Face Recognition Test - Press Q to Exit", frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 13:
                break
        
        cap.release()
        cv2.destroyAllWindows()
        conn.close()
        
        print("✅ Face recognition test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Test error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Face Recognition Setup and Test")
    print("1. Setting up face recognition...")
    
    if setup_face_recognition():
        print("\n2. Testing face recognition...")
        test_face_recognition()
    else:
        print("\n❌ Setup failed. Please follow these steps:")
        print("1. Add students using Student Details form")
        print("2. Capture photos using 'Take Photo Sample'")
        print("3. Run this script again")