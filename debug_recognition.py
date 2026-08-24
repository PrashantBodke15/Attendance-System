import cv2
import os
import numpy as np
from PIL import Image
import mysql.connector

def debug_face_recognition():
    """Debug face recognition issues"""
    
    print("=== Face Recognition Debug ===")
    
    # Check training data
    data_dir = "data"
    if not os.path.exists(data_dir):
        print("❌ No data directory found")
        return False
    
    image_files = [f for f in os.listdir(data_dir) if f.endswith('.jpg')]
    print(f"Training images found: {len(image_files)}")
    
    # Analyze training data
    student_ids = set()
    for img_file in image_files:
        parts = img_file.split('.')
        if len(parts) >= 3:
            try:
                student_id = int(parts[1])
                student_ids.add(student_id)
            except ValueError:
                print(f"Invalid filename format: {img_file}")
    
    print(f"Unique student IDs in training data: {sorted(student_ids)}")
    
    # Check database
    try:
        conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT Student_id, Name FROM student")
        db_students = my_cursor.fetchall()
        
        print("Students in database:")
        for student in db_students:
            print(f"  ID: {student[0]}, Name: {student[1]}")
        
        conn.close()
    except Exception as e:
        print(f"Database error: {str(e)}")
        return False
    
    # Check classifier
    if not os.path.exists("classifier.xml"):
        print("❌ No trained classifier found")
        return False
    
    print("✅ Classifier file exists")
    
    # Test recognition with improved parameters
    try:
        # Load models
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        if face_cascade.empty():
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        recognizer = cv2.face.LBPHFaceRecognizer_create()
    