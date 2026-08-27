import cv2

def test_camera():
    """Test if camera and face detection works"""
    try:
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        # Initialize camera
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Could not open camera")
            return False
            
        print("Camera opened successfully!")
        print("Press 'q' to quit or 'Enter' to exit")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                break
                
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            # Draw rectangles around faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, 'Face Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
            
            # Display the frame
            cv2.imshow('Face Detection Test', frame)
            
            # Break on 'q' key or Enter key
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 13:  # 13 is Enter key
                break
        
        cap.release()
        cv2.destroyAllWindows()
        print("Camera test completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error during camera test: {str(e)}")
        return False

if __name__ == "__main__":
    test_camera()