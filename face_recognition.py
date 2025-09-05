'''from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        bl=Button(self.root,command=self.face_recog,text="Detect Face",font=("Rockwell",15),bg="black",fg="white",cursor="hand2")
        bl.place(x=650,y=350,width=220,height=40)

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="nikhilN@27",database="face_recogniser")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("Select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("Select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)


                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Uknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX)

                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # For Windows, avoids camera lock issues


        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()'''

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        bl = Button(self.root, command=self.face_recog, text="Detect Face", font=("Rockwell", 15),
                    bg="black", fg="white", cursor="hand2")
        bl.place(x=650, y=350, width=220, height=40)

        #~~~~~~~~~~~~~Excel Attendance~~~~~~~~~~~~~~~~
    def mark_attendance(self,i,r,n,d):
        with open ("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%I:%M:%S %p")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")






    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

                try:
                    id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                except:
                    coord.append([x, y, w, h])
                    continue

                confidence = int(100 * (1 - predict / 300))

                try:
                    conn = mysql.connector.connect(host="localhost", username="root",
                                                   password="nikhilN@27", database="face_recogniser")
                    my_cursor = conn.cursor()

                    my_cursor.execute("Select Name from student where Student_id=" + str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n) if n is not None else "Unknown"

                    my_cursor.execute("Select Roll from student where Student_id=" + str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r) if r is not None else "Unknown"

                    my_cursor.execute("Select Dep from student where Student_id=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d) if d is not None else "Unknown"

                    my_cursor.execute("Select Student_id from student where Student_id=" + str(id))
                    i = my_cursor.fetchone()
                    i = "+".join(i) if i is not None else "Unknown"

                    conn.close()
                except:
                    n, r, d = "Unknown", "Unknown", "Unknown"

                if confidence > 65:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        # Try opening camera from index 0 to 3
        video_cap = None
        for idx in range(0, 4):
            cap_try = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
            if cap_try.isOpened():
                video_cap = cap_try
                break
            else:
                cap_try.release()

        if video_cap is None or not video_cap.isOpened():
            messagebox.showerror("Camera Error", "Could not open camera. Make sure no other app is using it.")
            return

        # Camera loop
        while True:
            ret, img = video_cap.read()
            if not ret or img is None:
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 13:  # Press 'q' or Enter to exit
                break
            if cv2.getWindowProperty("Welcome To Face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
