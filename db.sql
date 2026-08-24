-- Face Recognition System Database Schema

CREATE DATABASE IF NOT EXISTS face_recognizer;
USE face_recognizer;

-- Student table
CREATE TABLE IF NOT EXISTS student (
    Dep VARCHAR(100),
    course VARCHAR(100),
    Year VARCHAR(20),
    Semester VARCHAR(20),
    Student_id VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100),
    Division VARCHAR(50),
    Roll VARCHAR(50),
    Gender VARCHAR(20),
    Dob VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address TEXT,
    Teacher VARCHAR(100),
    PhotoSample VARCHAR(10)
);

-- Show table structure
DESCRIBE student;