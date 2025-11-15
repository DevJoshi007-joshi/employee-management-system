from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as c
con=c.connect(host="localhost",user="root",password="301977",database="employee_management")
cur=con.cursor()
win=Tk()
win.geometry("1500x2000")
win.title("Employee Management")
win.config(bg='cyan')
def Sign_Up():
    win1=Toplevel()
     #for Add user
    win1.geometry("1500x2000")
    win1.title("sign up")
    win1.config(bg="gold")
    Label(win1,text="User name",font=('ravie', 20),bg="white").place(x=50,y=100)
    Label(win1,text="Password",font=("ravie", 20),bg="white").place(x=50,y=150)
  
    img2=PhotoImage(file="p6.png")
    Label(win1,image=img2,height=500,width=800).place(x=400,y=250)
    def submit():
        e1=c1.get()
        e2=c2.get()
        L=[e1,e2]
        l1=['','']
        q1="select username from admin"
        cur.execute(q1)
       
        for i in cur:
            l1.append(i)

        try:
            if e1 not in l1:
                q="insert into admin values(%s,%s)"
                cur.execute(q,L)
                con.commit()
                messagebox.showinfo("saved","data stored",parent=win1)
                win1.destroy()
        except Exception:
            messagebox.showerror("error","user already exits",parent=win1)
            t1.delete(0,END)

    c1=StringVar()
    c2=StringVar()
    t1=Entry(win1,font=("consolas",20),textvariable=c1)
    t2=Entry(win1,font=("bold 20"),show="sumit",textvariable=c2)
    t1.place(x=300,y=100)
    t2.place(x=300,y=150)
    t1.insert(0,"Enter User Name")
    t2.insert(0,"Enter Password")

    def reset():
        t1.delete(0,END)
        t2.delete(0,END)
    t1.focus_set()
    Button(win1,text="Reset",font=("simsun",20),command=reset).place(x=50,y=500)
    b4=Button(win1,text="Close",font=("simsun",20),bg="red",command=win1.destroy)
    b4.place(x=350,y=500)
    Label(win1,text="sign up",font=("algerian", 40),bg="snow",fg="brown").place(x=500,y=10)
    B5=Button(win1,text="submit",font=("simsun",20),command=submit)
    B5.place(x=200,y=500)
    win1.mainloop()
def Login():
    win2=Toplevel()
    win2.geometry("1500x2000")
    win2.config(bg="cyan")
    win2.title("Login")
    Label(win2,text="User name",font=("arial black", 20),bg="white").place(x=50,y=100)
    Label(win2,text="Password",font=("arial black", 20),bg="white").place(x=50,y=150)
    c7=StringVar()
    c8=StringVar()
    t1=Entry(win2,font=("bold 20"),textvariable=c7)
    t2=Entry(win2,font=("bold 20"),show="*",textvariable=c8)
    t1.place(x=350,y=100)
    t2.place(x=350,y=150)
    img=PhotoImage(file="op4.png")
    Label(win2,image=img,width=400).place(x=450,y=300)
    def log():
        e7=c7.get()
        e8=c8.get()
        q="select username,password from admin"
        l=[]
        c=0
        cur.execute(q) 
        for i in cur:
            l.append(i)
        if e7=='' or e8=='':
            messagebox.showerror("Error","Fill some data",parent=win2)
        else:
            for i in l:
                if i[0]==e7 and i[1]==e8:
                    c=c+1
            if c!=0:
                messagebox.showinfo("Suceed","User Found",parent=win2)
                win3=Toplevel()
                win3.geometry("1500x2000")
                win3.title("Employee Management")
                win3.config(bg='cyan')
                def AddEmployee():
                    win4=Toplevel()
                     #for Add user
                    win4.geometry("1500x2000")
                    win4.title("sign up")
                    win4.config(bg="gold")
                    Label(win4,text="Name",font=('ravie', 20),bg="white").place(x=50,y=150)
                    Label(win4,text="Employee Id",font=("ravie", 20),bg="white").place(x=50,y=200)
                    Label(win4,text="Password",font=('ravie', 20),bg="white").place(x=50,y=250)
                    Label(win4,text="DOB.",font=("ravie", 20),bg="white").place(x=50,y=300)
                    Label(win4,text="Phone No.",font=('ravie', 20),bg="white").place(x=50,y=350)
                    Label(win4,text="Email",font=('ravie', 20),bg="white").place(x=50,y=400)
                    Label(win4,text="Sign Up",font=("arial black", 50),bg='snow',fg='pink').place(x=400,y=10)
                    img=PhotoImage(file="op2.png")
                    a1=Label(win4,image=img)
                    a1.place(x=630,y=200)
                    def submit():
                        e1=c1.get()
                        e2=c2.get()
                        e3=c3.get()
                        e4=c4.get()
                        e5=c5.get()
                        e6=c6.get()
                        L=[e1,e2,e3,e4,e5,e6]
                        l1=[]
                        q1="select Employee_Id from employee"
                        cur.execute(q1)
                       
                        for i in cur:
                            l1.append(i)
                        messagebox.showinfo("data",e1)
                        try:
                            if e1 not in l1:
                                q="insert into employee values(%s,%s,%s,%s,%s,%s)"
                                cur.execute(q,L)
                                con.commit()
                                messagebox.showinfo("saved","data stored",parent=win4)
                                win4.destroy()
                        except Exception:
                                messagebox.showerror("error","user already exits",parent=win4)
                                t1.delete(0,END)


                    c2=StringVar()
                    c3=StringVar()
                    c4=StringVar()
                    c5=StringVar()
                    c6=StringVar()
                    t1=Entry(win4,font=("consolas",20),textvariable=c1)
                    Entry(win4,font=("consolas",20),show="*",textvariable=c3).place(x=300,y=250)
                    Entry(win4,font=("consolas",20),textvariable=c4).place(x=300,y=300)
                    Entry(win4,font=("consolas",20),textvariable=c5).place(x=300,y=350)
                    Entry(win4,font=("consolas",20),textvariable=c6).place(x=300,y=400)
                    t2=Entry(win4,font=("bold 20"),textvariable=c2)
                    t1.place(x=300,y=150)
                    t2.place(x=300,y=200)
                    t1.insert(0,"Enter User Name")
                    t2.insert(0,"Enter Password")

                    def reset():
                        t1.delete(0,END)
                        t2.delete(0,END)
                    t1.focus_set()
                    Button(win4,text="Reset",font=("simsun",20),command=reset).place(x=50,y=500)
                    b4=Button(win4,text="Close",font=("simsun",20),bg="red",command=win4.destroy)
                    b4.place(x=350,y=500)
                    B5=Button(win4,text="submit",font=("simsun",20),command=submit)
                    B5.place(x=200,y=500)
                    win4.mainloop()
                def employee_details():
                    win5=Toplevel()
                     #for login
                    win5.geometry("1500x2000")
                    win5.config(bg="cyan")
                    win5.title("Employee Details")
                    Label(win5,text="Employee_id",font=("arial black", 20),bg="white").place(x=50,y=100)
                    Label(win5,text="Password",font=("arial black", 20),bg="white").place(x=50,y=150)
                    c7=StringVar()
                    c8=StringVar()
                    t1=Entry(win5,font=("bold 20"),textvariable=c7)
                    t2=Entry(win5,font=("bold 20"),show="*",textvariable=c8)
                    t1.place(x=350,y=100)
                    t2.place(x=350,y=150)
                    img=PhotoImage(file="op3.png")
                    Label(win5,image=img).place(x=400,y=300)
                    def check_details():
                        e11=c7.get()
                        e12=c8.get()
                        q="select Employee_Id,password from employee"
                        l=[]
                        c=0
                        cur.execute(q) 
                        for i in cur:
                            l.append(i)
                        if e7=='' or e8=='':
                            messagebox.showerror("Error","Fill some data",parent=win5)
                        else:
                            for i in l:
                                if i[0]==e11 and i[1]==e12:
                                    c=c+1
                            if c!=0:
                                messagebox.showinfo("Suceed","User Found",parent=win5)
                                win6=Toplevel()
                                win6.geometry("1500x2000")
                                L="Welcome "+e11
                                l1=[e11]
                                Label(win6,text=L,font=("bold 40"),bg="pink",fg="brown").pack(fill='both')
                                Q5="select * from employee where Employee_Id=%s"
                                cur.execute(Q5,l1)
                                L4=[]
                                for k in cur:
                                    L4.append(k)
                                Label(win6,text="Name:",font=("algerian", 20),bg="snow",fg="brown").place(x=50,y=100)
                                Label(win6,text="Date Of Birth:",font=("algerian", 20),bg="snow",fg="brown").place(x=50,y=150)
                                Label(win6,text="Phone Number:",font=("algerian", 20),bg="snow",fg="brown").place(x=50,y=200)
                                Label(win6,text="Email Address:",font=("algerian", 20),bg="snow",fg="brown").place(x=50,y=250)
                                Label(win6,text=L4[0][0],font=("algerian", 20),bg="snow",fg="brown").place(x=400,y=100)
                                Label(win6,text=L4[0][3],font=("algerian", 20),bg="snow",fg="brown").place(x=400,y=150)
                                Label(win6,text=L4[0][4],font=("algerian", 20),bg="snow",fg="brown").place(x=400,y=200)
                                Label(win6,text=L4[0][5],font=("algerian", 20),bg="snow",fg="brown").place(x=400,y=250)
                                reset()
                                win5.destroy()
                                win6.mainloop()
                            else:
                                messagebox.showerror("Error","User Not found",parent=win5)
                                        
                    def reset():
                        t1.delete(0,END)
                        t2.delete(0,END)
                    t1.focus_set()    
                    Button(win5,text="Reset",font=("bold 20"),command=reset).place(x=50,y=200)
                    b5=Button(win5,text="Close",font=("bold 20 "),bg="red",command=win5.destroy)
                    Button(win5,text="LOGIN",font=("bold 20 "),bg="seagreen",command=check_details).place(x=200,y=200)
                    b5.place(x=400,y=200)
                    Label(win5,text="Employee details",font=("bold 40"),bg="pink",fg="brown").place(x=500,y=10)
                    win5.mainloop()
                def delete_Employee():
                    win8=Toplevel()
                    win8.geometry("1800x1800")
                    win8.config(bg="brown")
                    Label(win8,text="Employee Delete Quata",font=("bold 35"),bg='beige',fg='black').place(x=200,y=10)
                    Label(win8,text='Employee ID',font=('bold 25'),bg='beige',fg='black').place(x=70,y=300)
                    T1=StringVar()
                    S3=Entry(win8,font=('bold 20'),textvariable=T1)
                    S3.place(x=300,y=300)
                    S3.focus_set()
                    def Del():
                        V1=T1.get()
                        L1=[V1]
                        q="select employee_id from employee"
                        cur.execute(q)
                        L=[]
                        for i in cur:
                            L.append(i[0])
                        if V1 in str(L):
                            q="delete from employee where employee_id=%s"
                            cur.execute(q,L1)
                            con.commit()
                            S3.delete(0,END)
                            messagebox.showinfo("Succedd","Record Has Deleted",parent=win8)
                            win8.destroy()
                        else:
                           messagebox.showerror("EROR","Not Found",parent=win8)
                           S3.delete(0,END)
                    Button(win8,text="DELETE",font=('bold 25'),bg='beige',fg='black',command=Del).place(x=100,y=400)
                    win8.mainloop()
                  

                    
                Label(win3,text=" welcome to the application",font=("bold 40"),bg="yellow",fg="black").place(x=250,y=10)
                img=PhotoImage(file="pic7.png")
                Label(win3,image=img,width=500).place(x=400,y=200)
                b1=Button(win3,text="Add user",width=15,font=("forte", 20),bg="pink",command=AddEmployee)
                b1.place(x=50,y=100)
                b2=Button(win3,text="Employee details",width=15,font=("forte", 20),bg="pink",command=employee_details)
                b2.place(x=50,y=200)
                b4=Button(win3,text="delete employee",width=15,font=("forte", 20),bg="pink",command=delete_Employee)

                b4.place(x=50,y=300)
                b5=Button(win3,text="close",width=15,font=("forte", 20),bg="red",command=win3.destroy)
                b5.place(x=50,y=400)
                c1=StringVar()
                c2=StringVar()
                win3.mainloop()


                
                        
    def reset():
        t1.delete(0,END)
        t2.delete(0,END)
    t1.focus_set()    
    Button(win2,text="Reset",font=("bold 20"),command=reset).place(x=50,y=200)
    b5=Button(win2,text="Close",font=("bold 20 "),bg="red",command=win2.destroy)
    Button(win2,text="LOGIN",font=("bold 20 "),bg="seagreen",command=log).place(x=200,y=200)
    b5.place(x=400,y=200)
    Label(win2,text="Login",font=("bold 40"),bg="pink",fg="brown").place(x=500,y=10)
    win2.mainloop()
img1=PhotoImage(file="pic4.png")
Label(win,image=img1).place(x=0,y=0)
Label(win,text=" Admin Window",font=("bold 40"),bg="yellow",fg="black").place(x=500,y=10)
b1=Button(win,text="sign up",width=15,font=("forte", 20),command=Sign_Up)
b1.place(x=50,y=100)
b2=Button(win,text="Log In",width=15,font=("forte", 20),bg="pink",command=Login)
b2.place(x=50,y=200)
b3=Button(win,text="Close",width=15,font=("forte", 20),bg="red",command=win.destroy)
b3.place(x=50,y=300)
c1=StringVar()
c2=StringVar()
win.mainloop()


