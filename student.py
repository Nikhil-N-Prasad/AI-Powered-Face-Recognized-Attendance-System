from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

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
        self.var_address=StringVar()
        self.var_teacher=StringVar()

# Black background image
        img=Image.open(r"C:\Users\prasa\OneDrive\Desktop\Face_recognition_system\college_images\black.jpeg")
        img=img.resize((1550,2200),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=2200)

# Title
        title_lbl=Label(f_lbl,text="STUDENT DETAILS",font=("Segoe UI",25,"bold"),bg="black",fg="light blue")
        title_lbl.place(x=180,y=40,width=1200,height=45)
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=20,y=90,width=1480,height=700)

#Left Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student details",font=("times new roman",16,"bold"),fg="yellow")
        Left_frame.place(x=10,y=10,width=730,height=640)
#Right Frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="black",relief=RIDGE,text="Student details",font=("times new roman",16,"bold"),fg="yellow")
        Right_frame.place(x=760,y=10,width=710,height=580)


#Left contents
#Department
        deep_label=Label(Left_frame,text="Department",font=("times new roman",16,"bold"),bg="black",fg="white")
        deep_label.place(x=20,y=15,width=110,height=30)
        dep_combo=ttk.Combobox(Left_frame,textvariable=self.var_dep,font=("times new roman",15,"bold"),state="readonly")
        dep_combo['values']=("Select Department","CSE","ISE","AIML","EEE")
        dep_combo.current(0)
        dep_combo.place(x=150,y=15,width=180,height=30)

#Course
        deep_label=Label(Left_frame,text="Course",font=("times new roman",17,"bold"),bg="black",fg="white")
        deep_label.place(x=400,y=15,width=110,height=30)
        dep_combo=ttk.Combobox(Left_frame,textvariable=self.var_course,font=("times new roman",15,"bold"),state="readonly")
        dep_combo['values']=("Select Course","BE","BCA","BBA","MBA")
        dep_combo.current(0)
        dep_combo.place(x=500,y=15,width=180,height=30)

#Year
        deep_label=Label(Left_frame,text="Year",font=("times new roman",16,"bold"),bg="black",fg="white")
        deep_label.place(x=20,y=70,width=110,height=30)
        dep_combo=ttk.Combobox(Left_frame,textvariable=self.var_year,font=("times new roman",15,"bold"),state="readonly")
        dep_combo['values']=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024")
        dep_combo.current(0)
        dep_combo.place(x=150,y=70,width=180,height=30)

#Semester
        deep_label=Label(Left_frame,text="Semester",font=("times new roman",17,"bold"),bg="black",fg="white")
        deep_label.place(x=390,y=70,width=110,height=30)
        dep_combo=ttk.Combobox(Left_frame,textvariable=self.var_semester,font=("times new roman",15,"bold"),state="readonly")
        dep_combo['values']=("Select Semester","1st Semester","2nd Semester")
        dep_combo.current(0)
        dep_combo.place(x=500,y=70,width=180,height=30)

#Student_ID
        studentID_label=Label(Left_frame,text="Student ID",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=25,y=125)
        studentID_entry=ttk.Entry(Left_frame,textvariable=self.var_std_id,width=20,font=("times new roman",15,"bold"))
        studentID_entry.place(x=150,y=125)

#Student Name
        studentID_label=Label(Left_frame,text="Student Name",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=360,y=125)
        studentID_entry=ttk.Entry(Left_frame,textvariable=self.var_std_name,width=20,font=("times new roman",15,"bold"))
        studentID_entry.place(x=500,y=125)

#Class Division
        studentID_label=Label(Left_frame,text="Class Division",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=12,y=180)
        div_combo=ttk.Combobox(Left_frame,textvariable=self.var_div,font=("times new roman",15,"bold"),state="readonly")
        div_combo['values']=("Select Division","1","2","3","4")
        div_combo.place(x=150,y=180,width=205)
        div_combo.current(0)

#Roll No.
        studentID_label=Label(Left_frame,text="Roll No.",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=410,y=180)
        studentID_entry=ttk.Entry(Left_frame,textvariable=self.var_roll,width=20,font=("times new roman",15,"bold"))
        studentID_entry.place(x=500,y=180)

#Gender
        studentID_label=Label(Left_frame,text="Gender",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=60,y=235)
        gender_combo=ttk.Combobox(Left_frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),state="readonly")
        gender_combo['values']=("Select Gender","Male","Female")
        gender_combo.place(x=150,y=235,width=205)
        gender_combo.current(0)

#DOB
        studentID_label=Label(Left_frame,text="Date Of Birth",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=365,y=235)
        studentID_entry=ttk.Entry(Left_frame,textvariable=self.var_dob,width=20,font=("times new roman",15,"bold"))
        studentID_entry.place(x=500,y=235)

#Email
        studentID_label=Label(Left_frame,text="E-Mail",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=60,y=290)
        studentID_entry=ttk.Entry(Left_frame,textvariable=self.var_email,width=20,font=("times new roman",15,"bold"))
        studentID_entry.place(x=150,y=290)

#Phone No.
        studentID_label=Label(Left_frame,text="Phone No.",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=390,y=290)
        studentID_entry=ttk.Entry(Left_frame,textvariable=self.var_phone,width=20,font=("times new roman",15,"bold"))
        studentID_entry.place(x=500,y=290)

#Address
        studentID_label=Label(Left_frame,text="Address",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=60,y=345)
        studentID_entry=ttk.Entry(Left_frame,textvariable=self.var_address,width=20,font=("times new roman",15,"bold"))
        studentID_entry.place(x=150,y=345)

#Teacher Name
        studentID_label=Label(Left_frame,text="Teacher Name",font=("times new roman",16,"bold"),bg="black",fg="white")
        studentID_label.place(x=360,y=345)
        studentID_entry=ttk.Entry(Left_frame,textvariable=self.var_teacher,width=20,font=("times new roman",15,"bold"))
        studentID_entry.place(x=500,y=345)

#Radio Button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Left_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.place(x=120,y=400)
        radiobtn2=ttk.Radiobutton(Left_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.place(x=470,y=400)

#Buttons
        save_btn=Button(Left_frame,text="Save",command=self.add_data,width=12,font=("times new roman",12,"bold"))
        save_btn.place(x=40,y=450)
        update_btn=Button(Left_frame,text="Update",command=self.update_data,width=12,font=("times new roman",12,"bold"))
        update_btn.place(x=210,y=450)
        delete_btn=Button(Left_frame,text="Delete",command=self.delete_data,width=12,font=("times new roman",12,"bold"))
        delete_btn.place(x=380,y=450)
        reset_btn=Button(Left_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",12,"bold"))
        reset_btn.place(x=550,y=450)
        take_photo_btn=Button(Left_frame,text="Take Photo Sample",command=self.generate_dataset,width=30,font=("times new roman",12,"bold"))
        take_photo_btn.place(x=40,y=520)
        update_photo_btn=Button(Left_frame,text="Update Photo Sample",width=30,font=("times new roman",12,"bold"))
        update_photo_btn.place(x=390,y=520)

#Search bar
        search_label=Label(Right_frame,text="Search by :",font=("times new roman",16,"bold"),bg="black",fg="white")
        search_label.place(x=10,y=30)

        search_combo=ttk.Combobox(Right_frame,font=("times new roman",15,"bold"),state="readonly")
        search_combo['values']=("Select","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.place(x=120,y=30,width=140,height=30)

        search_entry=ttk.Entry(Right_frame,width=15,font=("times new roman",15,"bold"))
        search_entry.place(x=270,y=30)

        search_btn=Button(Right_frame,text="Search",width=12,font=("times new roman",12,"bold"))
        search_btn.place(x=440,y=28)
        showall_btn=Button(Right_frame,text="Search",width=12,font=("times new roman",12,"bold"))
        showall_btn.place(x=575,y=28)

#Table Frame 
        table_frame=Frame(Right_frame,bd=2,bg="black",relief=RIDGE)
        table_frame.place(x=5,y=130,width=695,height=415)

#Scroll
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","Semester","Student ID","Name","division","roll","gender","Date Of Birth","E-Mail","Phone No.","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student ID", text="Student ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("division", text="Division")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("Date Of Birth", text="Date Of Birth")
        self.student_table.heading("E-Mail",text="E-mail")
        self.student_table.heading("Phone No.", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("Date Of Birth",width=100)
        self.student_table.column("E-Mail",width=100)
        self.student_table.column("Phone No.",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        # ~~~~~~~~Function Declaration~~~~~~~~~
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="nikhilN@27",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
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
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

#~~~~~~~~~~Fetch data from MySQL~~~~~~~~~~~~~~~~~~~~

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nikhilN@27",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#~~~~~~~~~~~~~Get cursor 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

#~~~~~~~~update button~~~~~~~~~~~

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="nikhilN@27",database="face_recogniser")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
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
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                                        ))                                                                                                              
                                      
                                                                                                                                                                                                                        
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



#~~~~~~~~~~Delete button~~~~~~~~~~~~~

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="nikhilN@27",database="face_recogniser")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


#~~~~~~~~~~~~~Reset button~~~~~~~~~~~
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

#~~~~~~~~~~Generate dataser or take photo sample~~~~~~~~~~
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="nikhilN@27",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
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
                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                    self.var_std_id.get()==id+1
                                                                                                                                                                                                                    ))
                                      
                                                                                                                                                                                                                    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #~~~~~~Loading Haarcascade frontal face detection~~~~~~~~~~~~~~

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #scaling factor=1.3, neighbour=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(600,600))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Message","Generating data set completed")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)





if __name__ == "__main__": 
    root=Tk()
    obj=Student(root)
    root.mainloop()