import cv2
import mysql.connector
import os
import numpy as np
from datetime import datetime
from tkinter import messagebox

class ImprovedFaceRecognition:
    def __init__(self):
        self.face_cascade = None
        self.recognizer = None
        self.load_models()
    
    def load_models(self):
        """Load face detection and recognition models"""
        
        # Load face cascade
        self.face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        if self.face_cascade.empty():
            self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Load face recognizer
        if os.path.exists("classifier.xml"):
            try:
                self.recognizer = cv2.face.LBPHFaceRecognizer_create()
                self.recognizer.read("classifier.xml")
                print("✅ Face recognition model loaded")
            except Exception as e:
                print(f"❌ Error loading recognizer: {e}")
                self.recognizer = None
        else:
            print("⚠ No trained model found")
            self.recognizer = None
    
    def get_student_info(self, student_id):
        """Get student information from database"""
        
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root", 
                password="vaishnavi@18",
                database="face_recognizer"
            )
            cursor = conn.cursor()
            
            # Get all student info in one query
            cursor.execute("""
                SELECT Student_id, Name, Roll, Dep 
                FROM student 
                WHERE Student_id = %s
            """, (str(student_id),))
            
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return {
                    'id': str(result[0]),
                    'name': result[1],
                    'roll': result[2], 
                    'department': result[3]
                }
            else:
                return None
                
        except Exception as e:
            print(f"Database error: {e}")
            return None
    
    def mark_attendance(self, student_info):
        """Mark attendance in CSV file"""
        
        try:
            # Read existing attendance
            attendance_records = []
            try:
                with open("prashant.csv", "r") as f:
                    lines = f.readlines()
                    attendance_records = [line.strip().split(",") for line in lines]
            except FileNotFoundError:
                # Create new file with header
                attendance_records = [["ID", "Roll", "Name", "Department", "Time", "Date", "Status"]]
            
            # Check if already marked today
            today = datetime.now().strftime("%d/%m/%Y")
            for record in attendance_records:
                if len(record) >= 6 and record[0] == student_info['id'] and record[5] == today:
                    print(f"Attendance already marked for {student_info['name']} today")
                    return False
            
            # Add new attendance record
            now = datetime.now()
            time_str = now.strftime("%H:%M:%S")
            date_str = now.strftime("%d/%m/%Y")
            
            new_record = [
                student_info['id'],
                student_info['roll'],
                student_info['name'],
                student_info['department'],
                time_str,
                date_str,
                "Present"
            ]
            
            attendance_records.append(new_record)
            
            # Write back to file
            with open("prashant.csv", "w", newline="") as f:
                for record in attendance_records:
                    f.write(",".join(record) + "\n")
            
            print(f"✅ Attendance marked for {student_info['name']}")
            return True
            
        except Exception as e:
            print(f"Error marking attendance: {e}")
            return False
    
    def recognize_faces(self, frame):
        """Recognize faces in the frame"""
        
        if self.face_cascade is None:
            return frame
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        for (x, y, w, h) in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            if self.recognizer is not None:
                try:
                    # Extract face region
                    face_roi = gray[y:y+h, x:x+w]
                    
                    # Resize face for better recognition
                    face_roi = cv2.resize(face_roi, (200, 200))
                    
                    # Predict
                    student_id, confidence = self.recognizer.predict(face_roi)
                    
                    # Calculate confidence percentage (lower is better)
                    confidence_percent = 100 - confidence
                    
                    print(f"Detected ID: {student_id}, Confidence: {confidence_percent:.1f}%")
                    
                    # Use lower threshold for better recognition
                    if confidence < 100:  # Lowered threshold
                        student_info = self.get_student_info(student_id)
                        
                        if student_info:
                            # Display student information
                            cv2.putText(frame, f"ID: {student_info['id']}", 
                                      (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                            cv2.putText(frame, f"Name: {student_info['name']}", 
                                      (x, y-40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                            cv2.putText(frame, f"Roll: {student_info['roll']}", 
                                      (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                            cv2.putText(frame, f"Confidence: {confidence_percent:.1f}%", 
                                      (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                            
                            # Mark attendance
                            self.mark_attendance(student_info)
                        else:
                            cv2.putText(frame, f"ID {student_id} not in database", 
                                      (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    else:
                        cv2.putText(frame, "Unknown Person", 
                                  (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        cv2.putText(frame, f"Confidence: {confidence_percent:.1f}%", 
                                  (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
                except Exception as e:
                    cv2.putText(frame, "Recognition Error", 
                              (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    print(f"Recognition error: {e}")
            else:
                cv2.putText(frame, "Face Detected (No Model)", 
                          (x, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        return frame
    
    def start_recognition(self):
        """Start face recognition with camera"""
        
        print("Starting face recognition...")
        print("Press 'q' to quit or Enter to exit")
        
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Could not open camera")
            return
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Process frame
            frame = self.recognize_faces(frame)
            
            # Display frame
            cv2.imshow("Improved Face Recognition - Press Q to Exit", frame)
            
            # Check for exit
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 13:  # q or Enter
                break
        
        cap.release()
        cv2.destroyAllWindows()
        print("Face recognition stopped")

def debug_training_data():
    """Debug training data and database"""
    
    print("=== Debugging Training Data ===")
    
    # Check training images
    if os.path.exists("data"):
        image_files = [f for f in os.listdir("data") if f.endswith('.jpg')]
        print(f"Training images: {len(image_files)}")
        
        # Extract student IDs from filenames
        student_ids = set()
        for img_file in image_files:
            parts = img_file.split('.')
            if len(parts) >= 3:
                try:
                    student_id = int(parts[1])
                    student_ids.add(student_id)
                except ValueError:
                    print(f"Invalid filename: {img_file}")
        
        print(f"Student IDs in training data: {sorted(student_ids)}")
    else:
        print("❌ No training data directory found")
    
    # Check database
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="vaishnavi@18", 
            database="face_recognizer"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT Student_id, Name FROM student ORDER BY Student_id")
        students = cursor.fetchall()
        
        print("Students in database:")
        for student in students:
            print(f"  ID: {student[0]}, Name: {student[1]}")
        
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    # Debug first
    debug_training_data()
    
    # Start improved face recognition
    face_rec = ImprovedFaceRecognition()
    face_rec.start_recognition()