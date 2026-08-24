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
                if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d no