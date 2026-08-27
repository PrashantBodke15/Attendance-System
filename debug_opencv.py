import cv2
import os

def debug_opencv_cascade():
    """Debug OpenCV cascade loading issues"""
    
    print("=== OpenCV Face Detection Debug ===")
    
    # Check OpenCV version
    print(f"OpenCV Version: {cv2.__version__}")
    
    # Check if file exists
    cascade_file = "haarcascade_frontalface_default.xml"
    if os.path.exists(cascade_file):
        print(f"✓ Cascade file exists: {cascade_file}")
        print(f"File size: {os.path.getsize(cascade_file)} bytes")
    else:
        print(f"✗ Cascade file not found: {cascade_file}")
        return False
    
    # Try to load the cascade
    try:
        face_cascade = cv2.CascadeClassifier(cascade_file)
        if face_cascade.empty():
            print("✗ Failed to load cascade - file might be corrupted")
            
            # Try using OpenCV's built-in cascade
            print("Trying OpenCV's built-in cascade...")
            builtin_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            if builtin_cascade.empty():
                print("✗ Built-in cascade also failed")
                return False
            else:
                print("✓ Built-in cascade loaded successfully")
                face_cascade = builtin_cascade
        else:
            print("✓ Cascade loaded successfully")
    except Exception as e:
        print(f"✗ Error loading cascade: {str(e)}")
        return False
    
    # Test camera
    print("\nTesting camera...")
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("✗ Camera not accessible")
            return False
        
        print("✓ Camera opened successfully")
        
        # Test face detection
        print("Testing face detection (5 seconds)...")
        import time
        start_time = time.time()
        faces_detected = 0
        
        while time.time() - start_time < 5:
            ret, frame = cap.read()
            if not ret:
                continue
                
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            if len(faces) > 0:
                faces_detected += 1
                print(f"Face detected! Total detections: {faces_detected}")
            
            # Show frame for debugging
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            cv2.imshow('Debug - Face Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        
        if faces_detected > 0:
            print(f"✓ Face detection working! Detected faces {faces_detected} times")
        else:
            print("⚠ No faces detected during test (try positioning your face in front of camera)")
        
        return True
        
    except Exception as e:
        print(f"✗ Error during camera test: {str(e)}")
        return False

if __name__ == "__main__":
    debug_opencv_cascade()