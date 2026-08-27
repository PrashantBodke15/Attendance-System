import cv2
import os
import numpy as np
from PIL import Image
import mysql.connector

def diagnose_face_recognition_issue():
    """Diagnose why face recognition shows Unknown"""
    
    print("=== Face Recognition Diagnosis ===")
    
    # Step 1: Check training data
    print("\n1. Checking training data...")
    data_dir = "data"
    if not os.path.exists(data_dir):
        print("❌ No 'data' directory found!")
        return False
    
    image_files = [f for f in os.listdir(data_dir) if f.endswith('.jpg')]
    print(f"Training images found: {len(image_files)}")
    
    if len(image_files) == 0:
        print("❌ No training images found!")
        print("Solution: Capture photos using 'Take Photo Sample' button")
        return False
    
    # Analyze training data structure
    student_ids = {}
    for img_file in image_files:
        parts = img_file.split('.')
        if len(parts) >= 3:
            try:
                student_id = int(parts[1])
                if student_id not in student_ids:
                    student_ids[student_id] = 0
                student_ids[student_id] += 1
            except ValueError:
                print(f"Invalid filename format: {img_file}")
    
    print("Student IDs in training data:")
    for sid, count in student_ids.items():
        print(f"  Student ID {sid}: {count} images")
    
    # Step 2: Check database students
    print("\n2. Checking database students...")
    try:
        conn = mysql.connector.connect(
            host="localhost", 
            username="root", 
            password="vaishnavi@18", 
            database="face_recognizer"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT Student_id, Name FROM student")
        db_students = cursor.fetchall()
        
        print("Students in database:")
        for student in db_students:
            print(f"  ID: {student[0]}, Name: {student[1]}")
        
        # Check for mismatches
        db_ids = [str(s[0]) for s in db_students]
        training_ids = [str(sid) for sid in student_ids.keys()]
        
        print("\n3. Checking ID matches...")
        for tid in training_ids:
            if tid in db_ids:
                print(f"✅ Student ID {tid}: Has both training data and database record")
            else:
                print(f"❌ Student ID {tid}: Has training data but NO database record")
        
        for did in db_ids:
            if did not in training_ids:
                print(f"⚠ Student ID {did}: Has database record but NO training data")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database error: {e}")
        return False
    
    # Step 3: Check classifier
    print("\n4. Checking trained model...")
    if os.path.exists("classifier.xml"):
        print("✅ Classifier file exists")
        
        # Test the classifier
        try:
            recognizer = cv2.face.LBPHFaceRecognizer_create()
            recognizer.read("classifier.xml")
            print("✅ Classifier loads successfully")
        except Exception as e:
            print(f"❌ Classifier loading error: {e}")
            return False
    else:
        print("❌ No classifier.xml found!")
        print("Solution: Run training using 'Train Data' button")
        return False
    
    return True

def retrain_model():
    """Retrain the face recognition model"""
    
    print("\n=== Retraining Face Recognition Model ===")
    
    data_dir = "data"
    if not os.path.exists(data_dir):
        print("❌ No training data directory found")
        return False
    
    image_files = [f for f in os.listdir(data_dir) if f.endswith('.jpg')]
    if len(image_files) == 0:
        print("❌ No training images found")
        return False
    
    faces = []
    ids = []
    
    print("Processing training images...")
    for image_file in image_files:
        try:
            image_path = os.path.join(data_dir, image_file)
            img = Image.open(image_path).convert('L')  # Convert to grayscale
            img_np = np.array(img, 'uint8')
            
            # Extract ID from filename (format: user.ID.number.jpg)
            parts = image_file.split('.')
            if len(parts) >= 3:
                student_id = int(parts[1])
                faces.append(img_np)
                ids.append(student_id)
                print(f"  Processed: {image_file} -> Student ID: {student_id}")
        except Exception as e:
            print(f"  Error processing {image_file}: {e}")
    
    if len(faces) == 0:
        print("❌ No valid training images processed")
        return False
    
    print(f"\nTraining model with {len(faces)} images...")
    
    try:
        # Create and train the recognizer
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, np.array(ids))
        
        # Save the trained model
        recognizer.write("classifier.xml")
        print("✅ Model trained and saved successfully!")
        
        return True
        
    except Exception as e:
        print(f"❌ Training failed: {e}")
        return False

def test_recognition():
    """Test face recognition with camera"""
    
    print("\n=== Testing Face Recognition ===")
    
    try:
        # Load models
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        if face_cascade.empty():
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        if face_cascade.empty():
            print("❌ Could not load face detection model")
            return False
        
        # Load trained recognizer
        if not os.path.exists("classifier.xml"):
            print("❌ No trained model found")
            return False
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")
        
        # Connect to database
        conn = mysql.connector.connect(
            host="localhost", 
            username="root", 
            password="vaishnavi@18", 
            database="face_recognizer"
        )
        cursor = conn.cursor()
        
        # Start camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Could not open camera")
            return False
        
        print("✅ Face recognition test started!")
        print("Press 'q' to quit")
        
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
                
                print(f"Detected ID: {id_}, Confidence: {confidence}")
                
                if confidence < 100:  # Adjust threshold as needed
                    # Get student info from database
                    cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (str(id_),))
                    result = cursor.fetchone()
                    
                    if result:
                        name, roll, dept = result
                        # Display info
                        cv2.putText(frame, f"ID: {id_}", (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        cv2.putText(frame, f"Name: {name}", (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        cv2.putText(frame, f"Roll: {roll}", (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                        cv2.putText(frame, f"Confidence: {100-confidence:.1f}%", (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                        print(f"✅ Recognized: {name} (ID: {id_})")
                    else:
                        cv2.putText(frame, f"ID {id_} not in DB", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                        print(f"❌ ID {id_} not found in database")
                else:
                    cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                    print(f"❌ Low confidence: {confidence}")
            
            cv2.imshow("Face Recognition Test - Press Q to quit", frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        conn.close()
        
        return True
        
    except Exception as e:
        print(f"❌ Test error: {e}")
        return False

if __name__ == "__main__":
    print("Face Recognition Fix Tool")
    print("=" * 50)
    
    # Step 1: Diagnose the issue
    if not diagnose_face_recognition_issue():
        print("\n❌ Issues found. Please fix them first.")
        exit(1)
    
    # Step 2: Ask if user wants to retrain
    retrain = input("\nDo you want to retrain the model? (y/n): ").lower()
    if retrain == 'y':
        if retrain_model():
            print("✅ Model retrained successfully!")
        else:
            print("❌ Retraining failed")
            exit(1)
    
    # Step 3: Test recognition
    test = input("\nDo you want to test face recognition? (y/n): ").lower()
    if test == 'y':
        test_recognition()
    
    print("\n🎉 Face recognition fix completed!")