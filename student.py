from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")

        #============  VARIABLES===========
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
        




        #####FIRST IMAGE
        img1=Image.open(r"D:\computer_vision\face_recognition\college_images\student.jpg")  ##1ST PIC
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        ###2ND IMAGE
        img2=Image.open(r"D:\computer_vision\face_recognition\college_images\student-portal_1.jpg")  ##2ND PIC
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        ##3 RD IMAGE
        img3=Image.open(r"D:\computer_vision\face_recognition\college_images\face-recognition.png") ##3RD PIC
        img3=img3.resize((550,130))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        

        ##BACK GROUND IMAGE
        img4=Image.open(r"D:\computer_vision\face_recognition\college_images\bg.jpg") ##3RD PIC
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT-MANAGEMENT-SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=650)


        ####left label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=630)
        
        ## left  IMAGE
        img_left=Image.open(r"D:\computer_vision\face_recognition\college_images\student1.jpg") ##3RD PIC
        img_left=img_left.resize((680,100))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=20,y=0,width=680,height=100)
        ########current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=20,y=110,width=680,height=110)
        
        ###deparment label

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)
         ###textvariable=self.var_Department(by the help of which student details show in hidden table)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer Science","Mechnical","Civil","Electrical","Aeronotics")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        ### course

        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","B.Tech","Bca","Bsc",)
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)
        
        ### year label

        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","1 st","2 nd","3 rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10)

        ### semester label

        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        sem_combo["values"]=("Select Semester","Sem1","Sem2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # CLASS STUDENT INFORMQATION
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student  Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=20,y=230,width=680,height=400)


        ### student id inside class student information

        student_id_label=Label(class_student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,sticky=W)

        ### student name inside class student information

        student_name_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,sticky=W)

        ### student devision inside class student information

        class_div_label=Label(class_student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)

        # class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="Read Only",width=17)
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        ### roll number inside class student information

        roll_no_label=Label(class_student_frame,text="Roll Number",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        ### gender inside class student information

        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        ## combo box for gender

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=17)
        gender_combo["values"]=("Select Gender","MALE","FEMALE","TRANS-GENDER")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        ### DOB

        dob_label=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        ### email

        email_label=Label(class_student_frame,text="EMAIL",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)

        ### PHONE NUM

        phone_label=Label(class_student_frame,text="Phone-No",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)




        ### adresss

        ad_label=Label(class_student_frame,text="ADRESS",font=("times new roman",12,"bold"),bg="white")
        ad_label.grid(row=4,column=0,padx=10,sticky=W)

        ad_entry=ttk.Entry(class_student_frame,textvariable=self.var_adress,width=20,font=("times new roman",12,"bold"))
        ad_entry.grid(row=4,column=1,padx=10,pady=10,sticky=W)


        ### TEACHER NAME

        tea_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        tea_label.grid(row=4,column=2,padx=10,sticky=W)

        tea_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        tea_entry.grid(row=4,column=3,padx=10,pady=10,sticky=W)


        ## radio butttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #### button frames

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=230,width=680,height=80)
        # save
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        ## update
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,)
        ## delete
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,)
        ## reset
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_func,width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=0,)
        #####take photo
        take_photo_btn=Button(btn_frame,text="TAKE PHOTO",command=self.generate_dataset,width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=1,)
        ###update photo
        update_photo_btn=Button(btn_frame,text="UPDATE PHOTO",width=24,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=2,)

        ###right label frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=730,height=630)
       
         
        ####RIGHT FRAME IMAGE

        img_right=Image.open(r"D:\computer_vision\face_recognition\college_images\student3.jpeg") ##3RD PIC
        img_right=img_right.resize((680,100))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg_right,bg="white")
        f_lbl.place(x=20,y=0,width=680,height=100)

        ########  search bar  ######

        # search frame
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=20,y=135,width=680,height=70)
        ###search lebel
        search_label=Label(search_frame,text=" IIT PATNA:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,sticky=W)
        ###  combobox(select option)
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select ","Roll Number","Phone-No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        

        ### search entry
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,sticky=W)



        ## search
        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        ## show all
        showall_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)
        ##======table frame========
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=20,y=210,width=710,height=330)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","adress","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Div")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("adress",text="Adress")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("adress",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    
    #================  FUNCTION DECLARATION ===========

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
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
                                                                                             self.var_adress.get(),
                                                                                             self.var_teacher.get(),
                                                                                             self.var_radio1.get()


                                                    ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
##=============    FETCH DATA ==========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student ")
        data=my_cursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

##=====  get cursor =======
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
        self.var_adress.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


#========== UPDATE FUNCTION ======

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(

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
                                                                                                                                     self.var_std_id.get(),








                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details succesfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #========= delete function =====
     
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student delete page","Do you want to delete this student data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql=" delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("delete","successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

   ##### RESET FUNCTION \========
    def reset_func(self):
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
        self.var_adress.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


######  GENERATE DATA SET AND TAKE A PHOTO SAMPLE # ######
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Adress=%s,Teacher=%s,PhotoSample=%s where Student_ID=%s",(

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
                                                                                                                                     self.var_std_id.get()==id+1


                ))

                conn.commit()
                self.fetch_data()
                self.reset_func()
                conn.close()

##### FACE DETECTION USING HARCASTADE ALGORITHM ===========
                 ### load predefined data on face frontals from opencv

                face_classifier= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    ## scalinfg factor =1.3
                    # #minimum Neighbour = 5

                    for(x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop

                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_crop(myframe) is not None:
                        img_id += 1
                        face=cv2.resize(face_crop(myframe),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id) + "."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)    
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)  
                        cv2.imshow("cropped faces",face)   

                    if cv2.waitKey(1)==13 or int(img_id)==100:  ##here 1 is num of pics in  dataset
                        break
                cap.release()  
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Genereting dataset completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                 







if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()