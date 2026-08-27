from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #===========variable==========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_adress=StringVar()
        self.var_teacher=StringVar()
        self.var_search_by=StringVar()
        self.var_search=StringVar()


        #first image
        img=Image.open(r"D:\Downloads\attendance system\project images\Image3.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"D:\Downloads\attendance system\project images\Image3.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1= ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # #third image
        img2=Image.open(r"D:\Downloads\attendance system\project images\Image3.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2= ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #bg image
        img3=Image.open(r"D:\Downloads\attendance system\project images\Image3.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3= ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="dark green",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"D:\Downloads\attendance system\project images\Image3.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)

        #Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17)
        dep_combo["values"]=(" select Department","ZIMCA","ZIBACAR","ZCOR",)
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label = Label(current_course_frame, text="Course", font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=17)
        course_combo["values"]=("select Course","MBA-I","MBA-II","MCA-I","MCA-II")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label = Label(current_course_frame, text="Year", font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=17)
        year_combo["values"]=(" select Yerar","2025-26","2026-27","2027-28","2028-29")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester

        semester_label = Label(current_course_frame, text="Semester", font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=17)
        semester_combo["values"]=(" select semester","semester-1","semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student  Information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=250,width=720,height=300)

        #student Id
        studentId_label = Label(class_Student_frame, text="StudentID:", font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label = Label(class_Student_frame, text="StudentName:", font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #student division
        student_div_label = Label(class_Student_frame, text="StudentDivision:", font=("times new roman",13,"bold"),bg="white")
        student_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        student_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        student_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        roll_no_label = Label(class_Student_frame, text="roll no:", font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #Dob
        dob_label = Label(class_Student_frame, text="Dob:", font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone number
        phone_no_label = Label(class_Student_frame, text="Phone no:", font=("times new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Adress
        Adress_label = Label(class_Student_frame, text=" Adress", font=("times new roman",13,"bold"),bg="white")
        Adress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        Adress_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_adress,font=("times new roman",13,"bold"))
        Adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher name
        teacher_label = Label(class_Student_frame, text="Teacher", font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiobutton1.grid(row=5,column=0)

        radiobutton2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobutton2.grid(row=5,column=1)

        #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)
        
        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #kjkjkk
        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=70)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"D:\Downloads\attendance system\project images\Image3.jpg ")
        img_right=img_right.resize((720,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #======searh system=========
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="search system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label = Label(search_frame, text="search by:", font=("times new roman",15,"bold"),bg="red")
        search_label.grid(row=0,column=0,padx=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,textvariable=self.var_search_by,font=("times new roman",13,"bold"),width=15)
        search_combo["values"]=(" Select ","Roll","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


        Search_btn=Button(search_frame,text="Search",command=self.search_data,width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",command=self.fetch_data,width=12,font=("times new roman",12,"bold"),bg="blue",fg="white") 
        showAll_btn.grid(row=0,column=4,padx=4)

        #==========table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"] = "headings"
        
        self.student_table.pack(fill=BOTH, expand=1)


        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        # Create table if not exists and fetch data
        self.create_table_if_not_exists()
        self.fetch_data()


    #==========function declaration=========

    def create_table_if_not_exists(self):
        """Create the student table if it doesn't exist"""
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
            my_cursor = conn.cursor()
            
            # Create table if not exists
            my_cursor.execute("""
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
                )
            """)
            
            conn.commit()
            conn.close()
        except Exception as es:
            print(f"Error creating table: {str(es)}")

    def add_data(self):
        if self.var_dep.get()=="select department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student (Dep,course,Year,Semester,Student_id,Name,Division,Roll,Gender,Dob,Email,Phone,Address,Teacher,PhotoSample) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_adress.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ============Generate dataset or take photo samples=========
    def generate_dataset(self):
        if self.var_dep.get()=="select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_adress.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get()
                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ============Load predefined data on face frontals from opencv=========
                # Try to load cascade file from current directory first
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                # If that fails, try OpenCV's built-in cascade
                if face_classifier.empty():
                    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                
                if face_classifier.empty():
                    messagebox.showerror("Error", "Could not load face detection model", parent=self.root)
                    return

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # scaling factor=1.3
                    # Minimum Neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped_img=img[y:y+h,x:x+w]
                        return face_cropped_img
                    return None

                cap = cv2.VideoCapture(0)
                
                if not cap.isOpened():
                    messagebox.showerror("Error", "Could not open camera", parent=self.root)
                    return
                
                img_id = 0
                print(f"Starting photo capture for Student ID: {id}")
                print("Position your face in front of the camera. Press Enter to stop early.")
                
                while True:
                    ret,my_frame = cap.read()
                    if not ret:
                        break
                        
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id+=1
                        face = cv2.resize(cropped_face,(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        
                        # Show progress on the original frame
                        cv2.putText(my_frame,f"Capturing: {img_id}/100",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Capturing Photos - Press Enter to Stop",my_frame)
                        
                        # Also show the cropped face
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255),2)        
                        cv2.imshow("Cropped Face",face)
                        
                        print(f"Captured photo {img_id}/100")
                    else:
                        # Show frame even when no face is detected
                        cv2.putText(my_frame,"Position your face in camera",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                        cv2.imshow("Capturing Photos - Press Enter to Stop",my_frame)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                        
                cap.release()
                cv2.destroyAllWindows()
                
                if img_id > 0:
                    messagebox.showinfo("Result",f"Successfully captured {img_id} photos for training!",parent=self.root)
                else:
                    messagebox.showwarning("Warning","No photos were captured. Please ensure your face is visible to the camera.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    #==============Fetch data=========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vaishnavi@18",database="face_recognizer")
        my_cursor=conn.cursor()                                                                                                     
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #==============get cursor=========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_adress.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #==============update function=========
    def update_data(self):
        if self.var_dep.get()=="select department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_course.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_std_name.get(),
                                                                                                                        self.var_div.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_dob.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_adress.get(),
                                                                                                                        self.var_teacher.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_std_id.get()
                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #==============delete function=========
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #==============reset function=========
    def reset_data(self):
        self.var_dep.set("select Department")
        self.var_course.set("select Course")
        self.var_year.set("select Year")
        self.var_semester.set("select semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_adress.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #==============search function=========
    def search_data(self):
        if self.var_search_by.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Select option")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="vaishnavi@18", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_search_by.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

            

                              










if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
