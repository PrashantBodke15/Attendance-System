import cv2
import numpy as np

def test_face_detection_simple():
    """Simple face detection test without database dependencies"""
    try:
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        if face_cascade.empty():
            print("Error: Could not load haarcascade file")
            return False
        
        # Initialize camera
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Could not open camera")
            return False
            
        print("Face detection test started!")
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
                cv2.putText(frame, f'Face Detected ({len(faces)} faces)', (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            
            # Display the frame
            cv2.imshow('Face Detection Test - Press Q or Enter to Exit', frame)
            
            # Break on 'q' key or Enter key
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 13:  # 13 is Enter key
                break
        
        cap.release()
        cv2.destroyAllWindows()
        print("Face detection test completed successfully!")
        return True
        
    except Exception as e:
        print(f"Error during face detection test: {str(e)}")
        return False

if __name__ == "__main__":
    test_face_detection_simple()