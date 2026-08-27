import cv2
import os

def test_photo_capture():
    """Test photo capture functionality"""
    
    print("=== Testing Photo Capture ===")
    
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Created data directory")
    
    # Load face cascade
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    if face_cascade.empty():
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if face_cascade.empty():
        print("❌ Could not load face detection model")
        return False
    
    print("✅ Face detection model loaded")
    
    # Test camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Could not open camera")
        return False
    
    print("✅ Camera opened successfully")
    print("Position your face in front of the camera")
    print("Press 'c' to capture a test photo, 'q' to quit")
    
    photo_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Face Detected ({len(faces)})", (x, y-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Show instructions
        cv2.putText(frame, "Press 'c' to capture, 'q' to quit", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, f"Photos captured: {photo_count}", (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.imshow("Photo Capture Test", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c') and len(faces) > 0:
            # Capture photo
            for (x, y, w, h) in faces:
                face_crop = frame[y:y+h, x:x+w]
                face_resize = cv2.resize(face_crop, (450, 450))
                face_gray = cv2.cvtColor(face_resize, cv2.COLOR_BGR2GRAY)
                
                photo_count += 1
                filename = f"data/test_photo_{photo_count}.jpg"
                cv2.imwrite(filename, face_gray)
                print(f"✅ Captured photo: {filename}")
                break
    
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"Test completed. Captured {photo_count} photos.")
    return photo_count > 0

if __name__ == "__main__":
    test_photo_capture()