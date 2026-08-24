from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np 


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # first image
        img_top=Image.open(r"D:\Downloads\attendance system\project images\face2.jpg" )
        img_top=img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        # second image
        img_botom=Image.open(r"D:\Downloads\attendance system\project images\facedetect.jpg" )
        img_botom=img_botom.resize((950,700),Image.LANCZOS)
        self.photoimg_botom=ImageTk.PhotoImage(img_botom)

        f_lbl=Label(self.root,image=self.photoimg_botom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        # button
        b1_1=Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="dark green",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)

    # =========attendance==========
    def mark_attendance(self,i,r,n,d):
        try:
            with open("prashant.csv","r+",newline="\n") as f:
                myDataList=f.readlines()
                name_list=[]
                for line in myDataList:
                    entry=line.split(",")
                    if len(entry) > 0:
                        name_list.append(entry[0])
                if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                    now=datetime.now()
                    d1=now.strftime("%d/%m/%Y")
                    dtstring=now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")
        except FileNotFoundError:
            # Create the file if it doesn't exist
            with open("prashant.csv","w",newline="\n") as f:
                f.write("ID,Roll,Name,Department,Time,Date,Status")
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

    #=====face recognition ==========
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                if clf is not None:
                    try:
                        # Extract face region for recognition
                        face_roi = gray_image[y:y+h,x:x+w]
                        # Resize for better recognition
                        face_roi = cv2.resize(face_roi, (200, 200))
                        
                        id,predict=clf.predict(face_roi)
                        confidence=int((100*(1-predict/300)))

                        conn=mysql.connector.connect(host="localhost",username="root",password="vaishnavi@18",database="face_recognizer")
                        my_cursor=conn.cursor() 

                        # Get all student info in one query
                        my_cursor.execute("SELECT Student_id, Name, Roll, Dep FROM student WHERE Student_id=%s",(str(id),))
                        result = my_cursor.fetchone()
                        
                        if result:
                            i = str(result[0])
                            n = result[1]
                            r = result[2]
                            d = result[3]
                        else:
                            i = n = r = d = "Unknown"

                        # Use better confidence threshold (lower is better for LBPH)
                        if predict < 100:  # Lowered threshold for better recognition
                            cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"Confidence:{confidence}%",(x,y+h+20),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2)
                            self.mark_attendance(i,r,n,d)
                        else:
                            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                            cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"Confidence:{confidence}%",(x,y+h+20),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,0,255),2)
                        
                        conn.close()
                    except Exception as e:
                        cv2.putText(img,f"Recognition Error",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                        print(f"Recognition error: {str(e)}")
                else:
                    cv2.putText(img,"Face Detected (No Model)",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                 
                coord=[x,y,w,h]
                conn.close()

            return coord
              
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        try:
            # Try to load cascade file from current directory first
            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            
            # If that fails, try OpenCV's built-in cascade
            if faceCascade.empty():
                faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            
            if faceCascade.empty():
                messagebox.showerror("Error", "Could not load face detection model", parent=self.root)
                return
            
            # Try to load the trained classifier
            clf = None
            try:
                if os.path.exists("classifier.xml"):
                    clf=cv2.face.LBPHFaceRecognizer_create()
                    clf.read("classifier.xml")
                    print("Face recognition model loaded successfully")
                else:
                    print("No trained model found. Only face detection will work.")
                    clf = None
            except (AttributeError, cv2.error, FileNotFoundError):
                messagebox.showwarning("Warning", "Face recognition model not found. Only face detection will work.", parent=self.root)
                clf = None

            video_cap=cv2.VideoCapture(0)

            if not video_cap.isOpened():
                messagebox.showerror("Error", "Could not open camera", parent=self.root)
                return

            print("Face detection started. Press Enter to exit.")
            
            while True:
                ret,img=video_cap.read()
                if not ret:
                    break
                    
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Face Recognition - Press Enter to Exit",img)

                if cv2.waitKey(1)==13:  # Press Enter to exit
                    break
            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()