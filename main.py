from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

class login:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN System")
        self.root.geometry("1440x800+100+100")

        #Background image
        self.bg=ImageTk.PhotoImage(file="image/tokito muichiroo.jpeg")
        self.bgimage = Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #Login Frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x = 800, y =150, width = 500 , height = 500)

        # Title login
        title = Label(Frame_login , text = "LOGIN HERE", font=("Impact",35,"bold"),fg="#000000",bg="white").place(x=135,y=30)

        # subTitle login
        title = Label(Frame_login, text="Please Type in username and password", font=("Impact", 15), fg="#000000", bg="white").place(x=90, y=100)

        #username
        usertitle = Label(Frame_login, text="Username", font=("Roman", 18), fg="#000000", bg="white").place(x=135, y=150)
        self.usertitle = Entry(Frame_login, font=("Roman", 18), bg="#C0C0C0")
        self.usertitle.place(x=135, y= 180)

        #password
        userpass = Label(Frame_login, text="Password", font=("Roman", 18), fg="#000000", bg="white").place(x=135,y=220)
        self.userpass = Entry(Frame_login, font=("Roman", 18), bg="#C0C0C0")
        self.userpass.place(x=135, y=250)

        #button
        forgetbutton = Button(Frame_login, text="Forget Password?", bd = 0,cursor= "hand2",font=("Roman", 18), fg="#000000", bg="white").place(x=140, y=300)
        logbutton = Button(Frame_login, command=self.check,text="Login!", font=("Roman", 18), fg="#000000", cursor= "hand2",bg="white").place(x=200, y=350)

    def check(self):
        if self.usertitle.get() == "" or self.userpass.get() == "":
            messagebox.showerror("Error","Required",parent=self.root)
        elif self.usertitle.get() != "mrllama11" or self.userpass.get() != "ilovellama12":
            messagebox.showerror("Error, wrong username or password","Required",parent = self.root)
        else:
            messagebox.showinfo("Welcome!","Connected!")


root = Tk()
obj = login(root)
root.mainloop()