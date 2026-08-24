import cv2

def simple_face_detection():
    """Simple face detection test"""
    
    # Try to load cascade file from current directory first
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    
    # If that fails, try OpenCV's built-in cascade
    if face_cascade.empty():
        print("Local cascade not found, trying built-in...")
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if face_cascade.empty():
        print("ERROR: Could not load face detection model")
        return False
    
    print("Face cascade loaded successfully!")
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("ERROR: Could not open camera")
        return False
    
    print("Camera opened successfully!")
    print("Face detection started. Press 'q' or Enter to exit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Draw rectangles around faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, 'Face Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Show status
        status = f"Faces: {len(faces)}"
        cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Display the frame
        cv2.imshow('Simple Face Detection - Press Q or Enter to Exit', frame)
        
        # Break on 'q' key or Enter key
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 13:  # 13 is Enter key
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Face detection test completed!")
    return True

if __name__ == "__main__":
    simple_face_detection()