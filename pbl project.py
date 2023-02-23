import tkinter
from tkinter import *    #import all attributes of tkinter library
import pymysql           
import mysql.connector   #to connect to database, creates connection to MySQL server
from mysql.connector import Error #when program tries to import nonexisting module
from tkinter import messagebox
#db=pymysql.connect(
#    host='localhost',
#    user='root',
#    password='shadowysahil@91',
 #   database='library'
#    )

#my_cur=db.cursor()
root=tkinter.Tk()    #Tk=for creating frames/boxes, root is object of tkinter

#from tkinter import *
#from tkinter import messagebox
#import os
#import mysql.connector
#from mysql.connector import Error
py=sys.executable #path to the program that is executed

def login():   #function for LOGIN button
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
   # Canvas.destroy()
    btn1.destroy()
    btn2.destroy()
    #btn3.destroy()
   
    def check():
        conn = pymysql.connect(host='localhost',                                #connecting to database
                                         database='library',
                                         user='root',
                                         password='shadowysahil@91',
                                         cursorclass=pymysql.cursors.DictCursor)  
        cursor = conn.cursor()  #for reading from database
        root=Tk()
        root.title('ACCOUNT LOGIN')
        root.geometry('500x500')
       
       
        Label(root,text="LOGIN ID").grid(row=2,column=0)   
        Label(root,text="").grid(row=3,column=0)
        Label(root,text="PASSWORD").grid(row=4,column=0)
        Label(root,text="" ).grid(row=5,column=0)
        #Label(root,text="Issue Date" ).grid(row=6,column=0)
   
        v1 = StringVar(root)    #to read the contents of root(object)
        v2 = StringVar(root)
        #v3=StringVar()
        #v1.set("Himanshu")
        e1=Entry(root, textvariable=v1).grid(row=2,column=1)    #to take 'LOGIN ID' input
        e2=Entry(root,show='*', textvariable=v2).grid(row=4,column=1)   #to take 'Password' input
        print(v1.get())
        #Label(root,text="").grid(row=9,column=0)
       

           
        def chex():
            try:
                   
                    username = v1.get()
                    password = v2.get()
                   # query = """ SELECT * FROM `login` """
                    
                    print(username)
                    print(password)   
                    cursor.execute('select * from login')  
                    result = cursor.fetchall()      #to fetch all the data from database
                    #inputvalue = input("Input= ")
                    #print("hi")
                    print(result)
                    #temp = False
                    for x in result:
                        print(x.values())
                        print(username)
                        print(password)
                        if (username in x.values()):
                            print(password)
                            if (password in x.values()):
                                print("Password is correct")
                                messagebox.showinfo("Message","SUCCESSFULL!!")
                                conn.commit()
                                v1.set('')
                                v2.set('')
                                #Button(root,text='CONTINUE', command=entry).grid(row=8,column=1)
                            else:
                                messagebox.showinfo("Message","Wrong Password!!")
                                conn.commit()
                                v1.set('')
                                v2.set('')
                        else:
                             messagebox.showinfo("Message","Wrong Username")
                             conn.commit()
                             v1.set('')
                             v2.set('')
                                #Button(root,text='RETRY', command=close).grid(row=8,column=1)
                    #cursor.commit()    
            except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")
                   
           
                   
           
        def clear():   #function for 'RESET' button
            v1.set('')
            v2.set('')
            #v3.set('')
        def close():   #function for 'Exit' button
            root.destroy()
            #Button(root,text='LOGIN', command=entry).grid(row=8,column=0)
            #Button(root,text='RESET', command=clear).grid(row=8,column=1)
            #Button(root,text='EXIT', command=close).grid(row=8,column=2)
           
        #root.mainloop()
            #v3.set('')
       
       
        Button(root,text='LOGIN', command=chex).grid(row=8,column=0)
        Button(root,text='RESET', command=clear).grid(row=8,column=1)
        Button(root,text='EXIT', command=close).grid(row=8,column=2)
        root.mainloop()
        #chex()
    #check()
   
    c=Canvas(root,width=3000,height=3000)
    c.pack()
    #img=PhotoImage(file="C:\\Users\\kvdiat\\Desktop\\lib2.gif")
    #c.create_image(0,0, anchor=NW , image=img)
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.10)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    headingLabel = Label(headingFrame2, text="WELCOME STUDENT", fg='black',font="Times")
    headingLabel.place(relx=0.25,rely=0.10, relwidth=0.5, relheight=0.5)
    headingLabel.config(height=10,width=25)
   
    btn1 = Button(root,text="LOGIN",bg='black', fg='black',command=check)
    btn1.place(relx=0.50,rely=0.3, relwidth=0.2,relheight=0.1)
    mainloop()
    #btn2 = Button(root,text="NOTES",bg='black', fg='white',command=RETURN)
 #btn2.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)

'''def chex():
            try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='Apeksha1718@123')
                    cursor = conn.cursor()
                    username = user_text.get()
                    password = pass_text.get()
                    query = """ SELECT * FROM `login` """

                    cursor.execute(query)
                    result = cursor.fetchall()
                    #inputvalue = input("Input= ")
                    print(result)
                    temp = False
                    for x in result:
                        if username in x and password in x:
                            #temp = True
                            #if temp:
                            messagebox.showinfo("LOGGED IN SUCCESSFULLY!!")
                            Button(root,text='CONTINUE', command=entry).grid(row=8,column=1)
                        else:
                            messagebox.showinfo("LOGIN FAILED!!")
                            Button(root,text='RETRY', command=clear).grid(row=8,column=1)
                         
            except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

    def check():
        root=Tk()
        root.title('ACCOUNT LOGIN')
        root.geometry('500x500')
        Label(root,text="LOGIN ID ",font='missy').grid(row=0,columnspan=2)
        Label(root,text="").grid(row=1,column=0)
        Label(root,text="PASSWORD").grid(row=2,column=0)
        Label(root,text="").grid(row=3,column=0)
        user_text=StringVar()
        pass_text=StringVar()
        #v3=StringVar()
        e1=Entry(root, textvariable=v1).grid(row=2,column=1)
        e2=Entry(root, textvariable=v2).grid(row=4,column=1)
        def chex():
            try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='Apeksha1718@123')
                    cursor = conn.cursor()
                    username = user_text.get()
                    password = pass_text.get()
                    query = """ SELECT * FROM `login` """

                    cursor.execute(query)
                    result = cursor.fetchall()
                    #inputvalue = input("Input= ")
                    print(result)
                    temp = False
                    for x in result:
                        if username in x and password in x:
                            #temp = True
                            #if temp:
                            messagebox.showinfo("LOGGED IN SUCCESSFULLY!!")
                            Button(root,text='CONTINUE', command=entry).grid(row=8,column=1)
                        else:
                            messagebox.showinfo("LOGIN FAILED!!")
                            Button(root,text='RETRY', command=clear).grid(row=8,column=1)
                         
            except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")
                   
            v1.set('')
            v2.set('')
            v3.set('')
           
       
        def clear():
            v1.set('')
            v2.set('')
            v3.set('')
        def close():
            root.destroy()
            Button(root,text='LOGIN', command=chex).grid(row=8,column=0)
            Button(root,text='RESET', command=clear).grid(row=8,column=1)
            Button(root,text='EXIT', command=close).grid(row=8,column=2)
            root.mainloop()
           
    c=Canvas(root,width=3000,height=3000)
    c.pack()
    #img=PhotoImage(file="C:\\Users\\kvdiat\\Desktop\\lib2.gif")
    #c.create_image(0,0, anchor=NW , image=img)
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.10)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)
    headingLabel = Label(headingFrame2, text="WELCOME STUDENT", fg='black',font="Times")
    headingLabel.place(relx=0.25,rely=0.10, relwidth=0.5, relheight=0.5)
    headingLabel.config(height=10,width=25)
   
    btn1 = Button(root,text="LOGIN",bg='black', fg='white',command=check)
    btn1.place(relx=0.50,rely=0.3, relwidth=0.2,relheight=0.1)
    mainloop()
    #btn2 = Button(root,text="NOTES",bg='black', fg='white',command=RETURN)
 #btn2.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)

       
'''  
   
#creating window
'''
class Lib(Tk):
   
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(3000, 3000)
        self.minsize(1200, 700)
        self.configure(bg="grey")
        self.title("WELCOME TO ACE IT:")
        #Button(root,text='LOGIN', command=check).grid(row=8,column=0)
        btn2 = Button(root,text="LOGIN",bg='black', fg='white',command=check)
        btn2.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)
   

        def chex():
            try:
                    conn = mysql.connector.connect(host='localhost',
                                         database='library',
                                         user='root',
                                         password='Apeksha1718@123')
                    cursor = conn.cursor()
                    username = self.user_text.get()
                    password = self.pass_text.get()
                    query = """ SELECT * FROM `login` """

                    cursor.execute(query)
                    result = cursor.fetchall()
                    #inputvalue = input("Input= ")
                    print(result)
                    temp = False
                    for x in result:
                        if username in x and password in x:
                            #temp = True
                            #if temp:
                            messagebox.showinfo("LOGGED IN SUCCESSFULLY!!")
                            Button(root,text='CONTINUE', command=entry).grid(row=8,column=1)
                        else:
                            messagebox.showinfo("LOGIN FAILED!!")
                            Button(root,text='RETRY', command=clear).grid(row=8,column=1)
                         
            except Error:
                    messagebox.showinfo('Error',"Something Goes Wrong,Try restarting")

        def check():
            self.label = Label(self, text="LOGIN", bg = 'gray' , fg = 'black', font=("courier-new", 24,'bold'))
            self.label.place(x=550, y=90)
            self.label1 = Label(self, text="User-Id" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
            self.label1.place(x=370, y=180)
            self.user_text = Entry(self, textvariable=self.a, width=45)
            self.user_text.place(x=480, y=190)
            self.label2 = Label(self, text="Password" , bg = 'gray' , fg = 'black', font=("courier-new", 18, 'bold'))
            self.label2.place(x=340, y=250)
            self.pass_text = Entry(self, show='*', textvariable=self.b, width=45)
            self.pass_text.place(x=480, y=255)
            self.butt = Button(self, text="Login",bg ='white', font=10, width=8, command=chex).place(x=580, y=300)
            self.label3 = Label(self, text="LIBRARY MANAGEMENT SYSTEM", bg='gray', fg='black', font=("courier-new", 24, 'bold'))
            self.label3.place(x=350, y=30)
#mainloop()
#mainloop()
'''
def STUDENT():
    global headingFrame1,headingFrame2,headingLabel,btn1,btn2,Canvas1
    headingFrame1.destroy()
    headingFrame2.destroy()
    headingLabel.destroy()
    #Canvas.destroy()
    #btn1.destroy()
    btn2.destroy()
    #btn3.destroy()
    #L=Lib()
    #Button(root,text="LOGIN",bg='black', fg='white',command=login)
   
   
    def RETURN():
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='shadowysahil@91',
            database='library'
            )
        my_cur=db.cursor()
        def entry():
            root=Tk()
            root.title('Student Account')
            root.geometry('250x300')
            Label(root,text="TAKE TEST",font='missy').grid(row=0,columnspan=2)  #'TAKE TEST' button
            Label(root,text="").grid(row=1,column=0)
            Label(root,text="NOTES").grid(row=2,column=0)   #'NOTES' button
            Label(root,text="").grid(row=3,column=0)
            #Label(root,text="Book Number").grid(row=4,column=0)
            #Label(root,text="" ).grid(row=5,column=0)
            #Label(root,text="Return Date" ).grid(row=6,column=0)
            v1=StringVar()
            v2=StringVar()
            #v3=StringVar()
            e1=Entry(root, textvariable=v1).grid(row=2,column=1)
            e2=Entry(root, textvariable=v2).grid(row=4,column=1)
            #e3=Entry(root, textvariable=v3).grid(row=6,column=1)
            Label(root,text="" ).grid(row=7,column=0)
            def returnbk():
                bkname=v1.get()
                bkno=v2.get()
                isdt=v3.get()
                my_cur=db.cursor()
                my_cur.execute('insert into BOOKS values(%s,%s)',(bkname,bkno))
                db.commit()
                messagebox.showinfo('successful','Thank you... Keep Reading :)')
                v1.set('')
                v2.set('')
                v3.set('')
            def clear():
                v1.set('')
                v2.set('')
                v3.set('')
            def close():
                root.destroy()
            Button(root,text='RETURN', command=returnbk).grid(row=8,column=0)
            Button(root,text='RESET', command=clear).grid(row=8,column=1)
            Button(root,text='EXIT', command=close).grid(row=8,column=2)
            root.mainloop()
        entry()
    def ISSUE():
        db=pymysql.connect(
            host='localhost',
            user='root',
            password='shadowysahil@91',
            database='library'
            )
        my_cur=db.cursor()
        def entry():
            root=Tk()
            root.title('Student Account')
            root.geometry('250x300')
            Label(root,text="Book Issue",font='missy').grid(row=0,columnspan=2)
            Label(root,text="").grid(row=1,column=0)
            Label(root,text="Book Name").grid(row=2,column=0)
            Label(root,text="").grid(row=3,column=0)
            Label(root,text="Book Number").grid(row=4,column=0)
            Label(root,text="" ).grid(row=5,column=0)
            Label(root,text="Issue Date" ).grid(row=6,column=0)
            v1=StringVar()
            v2=StringVar()
            v3=StringVar()
            e1=Entry(root, textvariable=v1).grid(row=2,column=1)
            e2=Entry(root, textvariable=v2).grid(row=4,column=1)
            e3=Entry(root, textvariable=v3).grid(row=6,column=1)
            Label(root,text="" ).grid(row=7,column=0)
            def issue():
                bkname=v1.get()
                bkno=v2.get()
                isdt=v3.get()
                my_cur=db.cursor()
                my_cur.execute('delete from BOOKS where book_no=%s',(bkno))
                db.commit()
                messagebox.showinfo('successful','you have issued the book :)')
                v1.set('')
                v2.set('')
                v3.set('')
            def clear():
                v1.set('')
                v2.set('')
                v3.set('')

            def close():
                root.destroy()
            Button(root,text='ISSUE', command=issue).grid(row=8,column=0)
            Button(root,text='RESET', command=clear).grid(row=8,column=1)
            Button(root,text='EXIT', command=close).grid(row=8,column=2)
            root.mainloop()

        entry()
    c=Canvas(root,width=3000,height=3000)
    c.pack()
    #img=PhotoImage(file="C:\\Users\\kvdiat\\Desktop\\lib2.gif")
    #c.create_image(0,0, anchor=NW , image=img)
    headingFrame1 = Frame(root,bg="#333945",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.10)

    headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
    headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

    headingLabel = Label(headingFrame2, text="WELCOME STUDENT", fg='black',font="Times")
    headingLabel.place(relx=0.25,rely=0.10, relwidth=0.5, relheight=0.5)
    headingLabel.config(height=10,width=25)
    btn1 = Button(root,text="TAKE TEST",bg='black', fg='black',command=login)
    btn1.place(relx=0.50,rely=0.3, relwidth=0.2,relheight=0.1)

    btn2 = Button(root,text="NOTES",bg='black', fg='black',command=login)
    btn2.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)
    mainloop()
           
c=Canvas(root,width=3000,height=3000)
c.pack()
#img=PhotoImage(file="C:\\Users\\kvdiat\\Desktop\\oldlib.gif")
#c.create_image(0,0, anchor=NW , image=img)
headingFrame1 = Frame(root,bg="#333945",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.5,relheight=0.10)

headingFrame2 = Frame(headingFrame1,bg="#EAF0F1")
headingFrame2.place(relx=0.01,rely=0.05,relwidth=0.98,relheight=0.9)

headingLabel = Label(headingFrame2, text="WELCOME TO ACE IT!!", fg='black',font="Times")#heading
headingLabel.place(relx=0.25,rely=0.10, relwidth=0.5, relheight=0.5)
headingLabel.config(height=10,width=25)
#btn1 = Button(root,text="ADMIN",bg='black', fg='white',command=ADMIN)
#btn1.place(relx=0.10,rely=0.3, relwidth=0.2,relheight=0.1)

btn2 = Button(root,text="EXISTING USER",bg='black', fg='black',command=STUDENT) #'EXISTING USER' button
btn2.place(relx=0.35,rely=0.3, relwidth=0.2,relheight=0.1)

#btn3 = Button(root,text="NEW USER",bg='black', fg='white', command=LIBRARIAN)
#btn3.place(relx=0.60,rely=0.3, relwidth=0.2,relheight=0.1)
mainloop()