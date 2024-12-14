from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("DEVELOPER")


        title_lbl=Label(self.root,text="DEVLOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        ### above pic in train window
        img_top=Image.open(r"college_images\dev.jpg") ##3RD PIC
        img_top=img_top.resize((1530,730))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=730)


        # #### main frame---------

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=55,width=500,height=600)


        ####  image inside main frame-----

        img_top1=Image.open(r"college_images\rishikesh.jpg") ##3RD PIC
        img_top1=img_top1.resize((200,200))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)



        ##### label information of developer---

        dev_lbl=Label(main_frame,text="HELLO MY NAME IS RISHIKESH",font=("times new roman",13,"bold"),fg="darkgreen")
        dev_lbl.place(x=5,y=5)

        dev_lbl=Label(main_frame,text="I AM A FULL STACK DEVELOPER",font=("times new roman",13,"bold"),fg="darkgreen")
        dev_lbl.place(x=5,y=40)

        ######### IMAGE-----

        img_top2=Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg") ##3RD PIC
        img_top2=img_top2.resize((500,400))
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(main_frame,image=self.photoimg_top2)
        f_lbl.place(x=0,y=210,width=500,height=400)















if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()