from tkinter import *
from tkinter import ttk
##installl--pip install pilllow in terminal
from PIL import Image,ImageTk
import tkinter
from student import Student  #(from file name import classof file name)
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help
from chatbot import Chatbot







class face_recognition_system:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")

        # scroll_X=ttk.Scrollbar(self.root,orient=HORIZONTAL)
        # scroll_Y=ttk.Scrollbar(self.root,orient=VERTICAL)

        # scroll_X.pack(side=BOTTOM,fill=X)
        # scroll_Y.pack(side=RIGHT,fill=Y)

        # scroll_X.config(command=self.student_table.xview)
        # scroll_Y.config(command=self.student_table.yview)

        #####FIRST IMAGE
        img1=Image.open(r"D:\computer_vision\face_recognition\college_images\images.jpg")  ##1ST PIC
        img1=img1.resize((500,130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)

        ###2ND IMAGE
        img2=Image.open(r"D:\computer_vision\face_recognition\college_images\facialrecognition.png")  ##2ND PIC
        img2=img2.resize((500,130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)

        ##3 RD IMAGE
        img3=Image.open(r"D:\computer_vision\face_recognition\college_images\employee_img2.jpg") ##3RD PIC
        img3=img3.resize((550,130))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        ##BACK GROUND IMAGE
        img4=Image.open(r"D:\computer_vision\face_recognition\college_images\bg1.jpg") ##3RD PIC
        img4=img4.resize((1530,710))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE-RECOGNITION -SYSTEM- SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        


        ###### time-------

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=("times new roman",20,"bold"),bg="white",fg="blue")
        lbl.place(x=20,y=0,width=200,height=50)
        time()
        

            


        ##student Button image
        img5=Image.open(r"D:\computer_vision\face_recognition\college_images\student.jpg") ##3RD PIC
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        ##student text   (command=self.student_deatils) by the help of which student page will open in new window)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=320,width=220,height=40)


        ##Detect face
        img6=Image.open(r"D:\computer_vision\face_recognition\college_images\face_detector1.jpg") ##3RD PIC
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        ##detect text image

        b1_1=Button(bg_img,text="Face-Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=320,width=220,height=40)


        ##attendence 
        img7=Image.open(r"D:\computer_vision\face_recognition\college_images\smart-attendance.jpg") ##3RD PIC
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        # attendence text  

        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=320,width=220,height=40)

        #help desk
        img8=Image.open(r"D:\computer_vision\face_recognition\college_images\help.jpg") ##3RD PIC
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        # help text  

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=320,width=220,height=40)
        

        ## train face
        img9=Image.open(r"D:\computer_vision\face_recognition\college_images\Train.jpg") ##3RD PIC
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        # train  face text  

        b1_1=Button(bg_img,text="Train-face",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=600,width=220,height=40)
        
        ## photo
        img10=Image.open(r"D:\computer_vision\face_recognition\college_images\photos.jpg") ##3RD PIC
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        # photo text

        b1_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=600,width=220,height=40)


        ## Developer
        img11=Image.open(r"D:\computer_vision\face_recognition\college_images\developer.jpg") ##3RD PIC
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=400,width=220,height=220)

        # developer text

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=600,width=220,height=40)
        
        ##  exit face button
        img12=Image.open(r"D:\computer_vision\face_recognition\college_images\exit.jpg") ##3RD PIC
        img12=img12.resize((220,220))
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=400,width=220,height=220)

        # exit face text text  

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=600,width=220,height=40)
       
       ## chat button======

    
        # img_chat=Image.open(r"D:\computer_vision\face_recognition\college_images\chat.jpg") ##3RD PIC
        # img_chat=img_chat.resize((220,220))
        # self.photoimg_chat=ImageTk.PhotoImage(img_chat)

        # b1=Button(bg_img,image=self.photoimg_chat,cursor="hand2",command=self.chatbot)
        # b1.place(x=1100,y=100,width=220,height=220)

        #chatbot  button======

        b1_1=Button(bg_img,text="CHATBOT",cursor="hand2",command=self.chatbot,font=("times new roman",15,"bold"),bg="darkred",fg="white")
        b1_1.place(x=650,y=50,width=220,height=40)
        
       

#####======= FUNCTION FOR OPEN IMAGES IN --PHOTOS===
    def open_img(self):
        os.startfile("data")  #@# we can write only folder name as path like data in this case

    ######exit work====

    def iExit(self):
        self.iExit= tkinter.messagebox.askyesno("Face-Recognition","Are you sure want to exit from this project",parent=self.root )
        if self.iExit > 0 :
            self.root.destroy()

        else:
            return 
    ##==========Function butttons=====
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

   ### function for train data
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    ###### function for face data

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

###### function for attendence 

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
    

    ###### function for developer 

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)



    ###### function for help_desk

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=Chatbot(self.new_window)





if __name__ =="__main__":
    root=Tk()
    obj = face_recognition_system(root)
    root.mainloop()

####window will prepare till here