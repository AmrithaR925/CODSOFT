from tkinter import*
import random
import string

root = Tk()
root.geometry("400x200")
root.resizable(width=FALSE, height=FALSE)

pwdstr=StringVar()
pwdlen=IntVar()

def get_pwd():
    pwd_1=string.ascii_letters + string.digits + string.punctuation
    password=""
    
    for x in range(pwdlen.get()):
        password = password + random.choice(pwd_1)
        pwdstr.set(password)
Label(root, text="Password Generator", font="calibri 18 bold").pack()
Label(root, text="Enter length of the Password").pack(pady=9)
Entry(root, textvariable=pwdlen).pack(pady=2)
Button(root, text="Generate Password", command=get_pwd).pack(pady=15)
Entry(root, textvariable=pwdstr).pack(pady=2)

root.mainloop()