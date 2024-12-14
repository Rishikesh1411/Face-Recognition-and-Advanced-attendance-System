from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox


class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_function)


        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()


        img_chat=Image.open(r'D:/computer_vision/face_recognition/college_images/chat.jpg')
        img_chat=img_chat.resize((200,70))
        self.photoimg=ImageTk.PhotoImage(img_chat)
        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT WITH ME',font=('arial',30,'bold'),fg='green',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)


        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',16,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',16,'bold'),width=8,bg='red',fg="white")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
  
        self.msg=''
        self.label_2=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='green',bg='white')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)


    # ========  function declaration===

    def enter_function(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete(1.0,END)
        self.entry.set('')


    def send(self):
        send='\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please Enter Some Input'
            self.label_2.config(text=self.msg,fg="red")
        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg="red")

        
        if (self.entry.get()=="Hello"):
            self.text.insert(END,'\n\n'+'Bot:Hi')

        elif (self.entry.get()=="Hi"):
            self.text.insert(END,'\n\n'+'Bot:Hello')

        elif (self.entry.get()=="How are you ?"):
            self.text.insert(END,'\n\n'+'Bot:Fine and you')

        elif (self.entry.get()=="Fantastic"):
            self.text.insert(END,'\n\n'+'Bot:Nice to Hear')
            
        elif (self.entry.get()=="Who created you ?"):
            self.text.insert(END,'\n\n'+'Bot:Rishikesh created me using Python')

        elif (self.entry.get()=="What is your  name ?"):
            self.text.insert(END,'\n\n'+'Bot:My name is advance  chatbot')


        elif (self.entry.get()=="Can you speak Marathi"):
            self.text.insert(END,"\n\n"+"Bot:I'm still learning it...... stil")
        
        elif (self.entry.get()=="What is meachine learning?"):
            self.text.insert(END,'\n\n'+'Bot:Meachine learning is the branch\nof artificial intelligence(AI) focused\non building applications that learn\nform data and improve their accuracy \nover time without being programmed\nto do so. ')

        elif (self.entry.get()=="How does face recognition work ?"):
            self.text.insert(END,'\n\n'+'Bot:Step 1:Facial recognition is a way of\nrecognizing a human face through ,\ntechnology.A facial recognition\nsystem uses')

        elif (self.entry.get()=="Bye"):
            self.text.insert(END,'\n\n'+'Bot:Thank you for chatting with me') 
        
        else:
            self.text.insert(END,'\n\n'+'Bot:Sorry I did not understand')







if __name__=='__main__':
    root=Tk()
    obj=Chatbot(root)
    root.mainloop()