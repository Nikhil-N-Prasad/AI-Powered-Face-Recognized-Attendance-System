from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
import cv2
from face_recognition import Face_Recognition
from attendance import Attends


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")
        self.attend_obj = Attends(root)

        # Black background image
        img=Image.open(r"C:\Users\prasa\OneDrive\Desktop\Face_recognition_system\college_images\black.jpeg")
        img=img.resize((1550,2200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=2200)

        # Title
        title_lbl=Label(f_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Segoe UI",25,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=180,y=50,width=1200,height=45)
    
        # Button - 1
        img1=Image.open(r"C:\Users\prasa\OneDrive\Desktop\Face_recognition_system\college_images\studet.jpeg")
        img1=img1.resize((220,220))
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(f_lbl,command=self.student_details,image=self.photoimg1,cursor="hand2")
        b1.place(x=200,y=170,width=220,height=220)
        b1_l=Button(f_lbl,command=self.student_details,text="Student Details",font=("Rockwell",15),bg="black",fg="white",cursor="hand2")
        b1_l.place(x=200,y=385,width=220,height=40)

        # Button - 2
        img2=Image.open(r"C:\Users\prasa\OneDrive\Desktop\Face_recognition_system\college_images\facerec.jpeg")
        img2=img2.resize((220,220))
        self.photoimg2=ImageTk.PhotoImage(img2)
        b2=Button(f_lbl,image=self.photoimg2,cursor="hand2",command=self.face_data)
        b2.place(x=600,y=170,width=220,height=220)
        b2_l=Button(f_lbl,text="Face Detector",font=("Rockwell",15),bg="black",fg="white",cursor="hand2",command=self.face_data)
        b2_l.place(x=600,y=385,width=220,height=40)

         # Button - 3
        img3=Image.open(r"C:\Users\prasa\OneDrive\Desktop\Face_recognition_system\college_images\attend.jpg")
        img3=img3.resize((220,220))
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(f_lbl,image=self.photoimg3,cursor="hand2",command=self.attend_obj.open_csv)
        b3.place(x=1000,y=170,width=220,height=220)
        b3_l=Button(f_lbl,text="Attendance",command=self.attend_obj.open_csv,font=("Rockwell",15),bg="black",fg="white",cursor="hand2")
        b3_l.place(x=1000,y=385,width=220,height=40)
        
         # Button - 4
        img4=Image.open(r"C:\Users\prasa\OneDrive\Desktop\Face_recognition_system\college_images\train.jpeg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b4=Button(f_lbl,command=self.train_data,image=self.photoimg4,cursor="hand2")
        b4.place(x=400,y=500,width=220,height=200)
        b4_l=Button(f_lbl,text="Train data",command=self.train_data,font=("Rockwell",15),bg="black",fg="white",cursor="hand2")
        b4_l.place(x=400,y=700,width=220,height=40)

         # Button - 5
        img5=Image.open(r"C:\Users\prasa\OneDrive\Desktop\Face_recognition_system\college_images\photos.jpeg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b5=Button(f_lbl,image=self.photoimg5,command=self.open_img,cursor="hand2")
        b5.place(x=800,y=500,width=220,height=200)
        b5_l=Button(f_lbl,text="Photos",command=self.open_img,font=("Rockwell",15),bg="black",fg="white",cursor="hand2")
        b5_l.place(x=800,y=700,width=220,height=40)

        
        #img6=Image.open(r"C:\Users\prasa\OneDrive\Desktop\Face_recognition_system\college_images\dev.jpeg")
        #img6=img6.resize((220,220))
        #self.photoimg6=ImageTk.PhotoImage(img6)
        #b6=Button(f_lbl,image=self.photoimg6,cursor="hand2")
        #b6.place(x=1000,y=500,width=220,height=200)
        #b6_l=Button(f_lbl,text="Developer",font=("Rockwell",15),bg="black",fg="white",cursor="hand2")
        #b6_l.place(x=1000,y=700,width=220,height=40)'''

    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()