from tkinter import *
from random import randint

root = Tk() 
root.title("Rock Paper Scissor")
root.configure(bg= "#c3bab1")
root.resizable(width=FALSE, height=FALSE)

user_label = Label(root,font=100, text="Scissor",bg="#c3bab1",relief="solid",width=18)
comp_label = Label(root,font=100, text="Scissor",bg="#c3bab1",relief="solid",width=18)
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

playerscore= Label(root,text=0,font=100,bg="#c3bab1",fg="white")
computerscore= Label(root,text=0,font=100,bg="#c3bab1",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

user_indicator = Label(root,font=50,text="User",bg="#c3bab1",fg="white")
comp_indicator = Label(root,font=50,text="Computer",bg="#c3bab1",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

message= Label(root,font=50,bg="#c3bab1",fg="white")
message.grid(row=3,column=2)

def updatemessage(x):
    message.config(text=x)

def updateuserscore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

def updatecomputerscore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)

def checkwin(player,computer):
    if player == computer:
        updatemessage("Its a tie!")
    elif player == "Rock":
        if computer == "Paper":
            updatemessage("You lose")
            updatecomputerscore()
        else:
            updatemessage("You win")
            updateuserscore()
    elif player == "Paper":
        if computer == "Scissor":
            updatemessage("You lose")
            updatecomputerscore()
        else:
            updatemessage("You win")
            updateuserscore()
    elif player == "Scissor":
        if computer == "Rock":
            updatemessage("You lose")
            updatecomputerscore()
        else:
            updatemessage("You win")
            updateuserscore()
    else:
        pass

choices=["Rock","Paper","Scissor"]
def updatechoice(x):
    compchoice= choices[randint(0,2)]
    comp_label.config(text=compchoice)
    user_label.config(text=x)

    checkwin(x,compchoice)

rock = Button(root,width=20,height=2,text="Rock",bg="#f46049",fg="#FFFFFF",command = lambda :updatechoice("Rock"))
paper = Button(root,width=20,height=2,text="Paper",bg="#eed959",fg="#FFFFFF",command = lambda :updatechoice("Paper"))
scissor = Button(root,width=20,height=2,text="Scissor",bg="#98a9d1",fg="#FFFFFF",command = lambda :updatechoice("Scissor"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissor.grid(row=2,column=3)

root.mainloop()