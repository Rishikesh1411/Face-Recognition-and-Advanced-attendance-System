from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")


        ########## VARIABLES=========
        ########## VARIABLES=========
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()



        #####FIRST IMAGE
        img1=Image.open(r"college_images\smart-attendance.jpg")  ##1ST PIC
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=200)

        ###2ND IMAGE
        img2=Image.open(r"college_images\clg.jpg")  ##2ND PIC
        img2=img2.resize((800,200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200)

        ### background img

        img3=Image.open(r"college_images\wp2551980.jpg") ##3RD PIC
        img3=img3.resize((1530,710))
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        ##### title

        title_lbl=Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM ",font=("times new roman",35,"bold"),bg="white",fg="gold")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        ##### FRAME------

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=650)

        ## LEFT SUB FRAME-----

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT ATTENDENCE DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=630)

        ## left  IMAGE
        img_left=Image.open(r"college_images\student3.jpeg") ##3RD PIC
        img_left=img_left.resize((680,100))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=20,y=0,width=680,height=100)

        #######---

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=20,y=140,width=680,height=350)



        #### LABEL AND ENTRY-----
        

        ### student id inside class student information

        Attendence_id_label=Label(left_inside_frame,text="ATTENDENCE-ID:",font=("times new roman",12,"bold"),bg="white")
        Attendence_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Attendence_id_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_id,font=("times new roman",12,"bold"))
        Attendence_id_entry.grid(row=0,column=1,pady=8,sticky=W)


        ###roll-

        roll_label=Label(left_inside_frame,text="ROLL:",font=("comicsansns",11,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_roll,font=("comicsansns",11,"bold"))
        roll_entry.grid(row=0,column=3,pady=8,sticky=W)

        ####NAME--

        name_label=Label(left_inside_frame,text="NAME:",font=("comicsansns",11,"bold"),bg="white")
        name_label.grid(row=1,column=0,pady=8,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_name,font=("comicsansns",11,"bold"))
        name_entry.grid(row=1,column=1,pady=8,sticky=W)

        #### department --

        dep_label=Label(left_inside_frame,text="DEPARTMENT:",font=("comicsansns",11,"bold"),bg="white")
        dep_label.grid(row=1,column=2)

        dep_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_department,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer Science","Mechnical","Civil","Electrical","Aeronotics")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10)

        #### time  --

        time_label=Label(left_inside_frame,text="TIME:",font=("comicsansns",11,"bold"),bg="white")
        time_label.grid(row=2,column=0,pady=8,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_time,font=("comicsansns",11,"bold"))
        time_entry.grid(row=2,column=1,pady=8,sticky=W)


        #### date--

        date_label=Label(left_inside_frame,text="DATE:",font=("comicsansns",11,"bold"),bg="white")
        date_label.grid(row=2,column=2)

        date_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_date,font=("comicsansns",11,"bold"))
        date_entry.grid(row=2,column=3,pady=8,sticky=W)

        #### ATTENDENCE STATUS--

        attendencelabel=Label(left_inside_frame,text="Attendence-status:",font=("comicsansns",11,"bold"),bg="white")
        attendencelabel.grid(row=3,column=0)

        attendence_combo=ttk.Combobox(left_inside_frame,font=("times new roman",12,"bold"),state="readonly",width=20,textvariable=self.var_attendance)
        attendence_combo["values"]=("Status","Present","Absent")
        attendence_combo.current(0)
        attendence_combo.grid(row=3,column=1,pady=8,sticky=W)

        ### BUTTONS IN LEFT FRAME--

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=260,width=630,height=70)

        # import  button
        import_btn=Button(btn_frame,text="IMPORT CSV",command=self.importcsv,width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)
        ## export button
        export_btn=Button(btn_frame,text="EXPORT CSV",command=self.exportcsv,width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1,)
        ## update
        update_btn=Button(btn_frame,text="UPDATE",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=1,column=0,)
        ## reset
        reset_btn=Button(btn_frame,text="Reset",width=35,command=self.reset_data,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=1,column=1,)
        






    


    ##RIGHT SUB FRAME----

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDENCE DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=730,height=630)
            
    

    


   
        ##RIGHT SUB FRAME----

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="ATTENDENCE DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=730,height=630)
## frame inside frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=10,width=700,height=478)
       

       #### scroll bar table 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.attendenceReport_table=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendenceReport_table.xview)
        scroll_y.config(command=self.attendenceReport_table.yview)


        self.attendenceReport_table.heading("id",text="Attendence_ID")
        self.attendenceReport_table.heading("roll",text="Roll")
        self.attendenceReport_table.heading("name",text="Name")
        self.attendenceReport_table.heading("department",text="Department")
        self.attendenceReport_table.heading("time",text="Time")
        self.attendenceReport_table.heading("date",text="Date")
        self.attendenceReport_table.heading("attendence",text="Attendence")

        self.attendenceReport_table["show"]="headings"
        
        self.attendenceReport_table.column("id",width=100)
        self.attendenceReport_table.column("roll",width=100)
        self.attendenceReport_table.column("name",width=100)
        self.attendenceReport_table.column("department",width=100)
        self.attendenceReport_table.column("time",width=100)
        self.attendenceReport_table.column("date",width=100)
        self.attendenceReport_table.column("attendence",width=100)


        self.attendenceReport_table.pack(fill=BOTH,expand=1)
        
        self.attendenceReport_table.bind("<ButtonRelease>",self.get_cursor)


    ####### fetch data =========

    def fetchdata(self,rows):
        self.attendenceReport_table.delete(*self.attendenceReport_table.get_children())
        for i in rows:
            self.attendenceReport_table.insert("",END,values=i)
    ### function for import data------
    def importcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title=" Open Csv", filetypes=(("CSV File","*csv"),("ALL File","*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=',')
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    ### export csv

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Founnd to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title=" Open Csv", filetypes=(("CSV File","*csv"),("ALL File","*.*")), parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=',')
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","your data exported to " + os.path.basename(fln)+"successfully")
        except Exception as es:
              messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    ### to get data ======

    def get_cursor(self,event=""):
        cursor_row=self.attendenceReport_table.focus()
        content=self.attendenceReport_table.item(cursor_row)
        rows=content["values"]
        self.var_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_department.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attendance.set(rows[6])

    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("")

    

      



    
        
        








if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()
