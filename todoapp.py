from tkinter import *
from tkinter.font import Font

root = Tk()
root.configure(background="#F0F0F0") 
root.title('To-Do List Application')
root.geometry("700x450")
root.resizable(width=False, height=False)

font = Font(family="Helvetica", size=18, weight="bold") 

frame = Frame(root)
frame.pack(pady=10)

listbox_font = Font(family="Helvetica", size=18, weight="bold")

listbox = Listbox(frame, font=listbox_font, width=40, height=7, bg="#FFFFFF", fg="#333333", bd=0, highlightthickness=0, selectbackground="#CCCCCC", activestyle="none")
listbox.pack(side=LEFT, fill=BOTH)

entry_font = Font(family="Helvetica", size=18,)
entry = Entry(root, font=entry_font, width=26, bg='#FFFFFF') 
entry.pack(pady=20)

buttonframe = Frame(root, bg='#F0F0F0') 
buttonframe.pack(pady=20)

def delete_item():
    listbox.delete(ANCHOR)

def add_item():
    listbox.insert(END, entry.get())
    entry.delete(0, END)

def cross_off_item():
    listbox.itemconfig(listbox.curselection(), fg="#999999") 

def uncross_item():
    listbox.itemconfig(listbox.curselection(), fg="#333333") 

def delete_crossed():
    count = 0
    while count < listbox.size():
        if listbox.itemcget(count, "fg") == "#999999":
            listbox.delete(listbox.index(count))
        else:
            count += 1

def delete_list():
    listbox.delete(0, END)

deletebutton = Button(buttonframe, text="Delete Item", bg="#FF6666", fg="#FFFFFF", font=("Helvetica", 12, "bold"), command=delete_item)
addbutton = Button(buttonframe, text="Add Item", bg="#66CC66", fg="#FFFFFF", font=("Helvetica", 12, "bold"), command=add_item)
crossoffbutton = Button(buttonframe, text="Cross Off Item", bg="#FFCC66", fg="#FFFFFF", font=("Helvetica", 12, "bold"), command=cross_off_item)
uncrossbutton = Button(buttonframe, text="Uncross Item", bg="#6699FF", fg="#FFFFFF",font=("Helvetica", 12, "bold"), command=uncross_item)
deletecrossedbutton = Button(buttonframe, text="Delete Crossed", bg="#FF6666", fg="#FFFFFF", font=("Helvetica", 12, "bold"), command=delete_crossed)

deletebutton.grid(row=0, column=0)
addbutton.grid(row=0, column=1, padx=20)
crossoffbutton.grid(row=0, column=2)
uncrossbutton.grid(row=0, column=3, padx=20)
deletecrossedbutton.grid(row=0, column=4)

root.mainloop()