from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
import cv2




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("DEVELOPER")


        title_lbl=Label(self.root,text="Help-desk",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        ### above pic in train window
        img_top=Image.open(r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg") ##3RD PIC
        img_top=img_top.resize((1530,730))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=730)

        ####label------

        help_lbl=Label(f_lbl,text="EMAIL:rishikeshr335@gmail.com",font=("times new roman",25,"bold"),fg="darkgreen")
        help_lbl.place(x=520,y=220)





if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()