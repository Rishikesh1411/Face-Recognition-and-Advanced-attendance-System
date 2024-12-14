from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from  tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
import logging
from time import strftime
from datetime import datetime



class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        ### above pic in  face recognition window
        img_top=Image.open(r"college_images\face_detector1.jpg") ##3RD PIC
        img_top=img_top.resize((650,700))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)


       
        ### bottom pic in face recognition  window
        img_bottom=Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg") ##3RD PIC
        img_bottom=img_bottom.resize((950,700))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        ## button code in face recognition window
        b1_1=Button(f_lbl,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=345,y=620,width=250,height=40)

    #####  attendence system=====
    def mark_attendance(self,i,r,n,d):
        with open("IITP.csv","r+",newline="\n") as f:
            mydatalists=f.readlines()
            name_list=[]
            for line in mydatalists:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if ((i not in name_list ) and   (r not in name_list) and (n not in name_list) and (d not in name_list)):
               now=datetime.now()
               d1=now.strftime("%d/%m/%Y")
               dstring=now.strftime("%H:%M:%S")
               f.writelines(f"\n{i},{r},{n},{d},{dstring},{d1},Present")
    

##===== Face Recognition ===========
    def face_recog(self):
        def draw_boundry(image, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_ID=" + str(id))
                n = my_cursor.fetchone()
                if n:
                    n = "+".join(n)
                else:
                    n = "Unknown"

                my_cursor.execute("select Roll from student where Student_ID=" + str(id))
                r = my_cursor.fetchone()
                if r:
                    r = "+".join(r)
                else:
                    r = "Unknown"

                my_cursor.execute("select Dep from student where Student_ID=" + str(id))
                d = my_cursor.fetchone()
                if d:
                    d = "+".join(d)
                else:
                    d = "Unknown"

                my_cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                i = my_cursor.fetchone()
                if i:
                    i = "+".join(i)
                else:
                    i = "Unknown"

                if confidence > 77:
                    cv2.putText(image, f"ID: {i}", (x, y - 90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (95, 215, 255), 3)
                    cv2.putText(image, f"Roll: {r}", (x, y - 63), cv2.FONT_HERSHEY_COMPLEX, 0.8, (95, 215, 255), 3)
                    cv2.putText(image, f"Name: {n}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (95, 215, 255), 3)
                    cv2.putText(image, f"Dep: {d}", (x, y - 8), cv2.FONT_HERSHEY_COMPLEX, 0.8, (95, 215, 255), 3)
                    self.mark_attendance(i,r,n,d)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    # cv2.putText(image, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                else:
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(image, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

                coord = [x, y, w, y]

            return coord

        def recognize(image, clf, faceCasCade):
            coord = draw_boundry(image, faceCasCade, 1.1, 10, (255, 25, 255), "Face", clf)
            return image

        faceCasCade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCasCade)
            cv2.imshow("Welcome To face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

        

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()
