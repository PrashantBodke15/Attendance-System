import cv2
import os

def capture_photos_for_student(student_id=1):
    """Capture photos for a specific student"""
    
    print(f"=== Capturing Photos for Student ID: {student_id} ===")
    
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Load face cascade
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    if face_cascade.empty():
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if face_cascade.empty():
        print("❌ Could not load face detection model")
        return False
    
    # Start camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Could not open camera")
        return False
    
    print("✅ Camera started!")
    print("Position your face in front of the camera")
    print("Photos will be captured automatically when face is detected")
    print("Press 'q' to quit early")
    
    img_id = 0
    target_photos = 50  # Capture 50 photos
    
    while img_id < target_photos:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Crop and resize face
            face_crop = frame[y:y+h, x:x+w]
            face_resize = cv2.resize(face_crop, (450, 450))
            face_gray = cv2.cvtColor(face_resize, cv2.COLOR_BGR2GRAY)
            
            # Save image
            img_id += 1
            filename = f"data/user.{student_id}.{img_id}.jpg"
            cv2.imwrite(filename, face_gray)
            
            # Show progress
            cv2.putText(frame, f"Capturing: {img_id}/{target_photos}", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            
            print(f"Captured photo {img_id}/{target_photos}")
        
        # Show frame
        cv2.imshow(f"Capturing Photos for Student {student_id} - Press Q to quit", frame)
        
        # Check for quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    if img_id >= target_photos:
        print(f"✅ Successfully captured {img_id} photos for Student ID {student_id}")
        return True
    else:
        print(f"⚠ Only captured {img_id} photos (target was {target_photos})")
        return img_id > 0

if __name__ == "__main__":
    student_id = input("Enter Student ID (default 1): ").strip()
    if not student_id:
        student_id = 1
    else:
        student_id = int(student_id)
    
    capture_photos_for_student(student_id)