import tkinter as tk

def add_number(number):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current_text + str(number))

def clear_entry():
    entry_display.delete(0, tk.END)

def evaluate():
    expression = entry_display.get()
    try:
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

def delete():
    current_text = entry_display.get()
    new_text = current_text[:-1]
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, new_text)

app = tk.Tk()
app.title("Calculator")
app.resizable(width=False, height=False)

entry_display = tk.Entry(app, width=25, font=("Comic sans", 14, "bold"), justify="right")
entry_display.grid(row=0, column=0, columnspan=4)

buttons = [('C', 1, 0, 1, 1),('/', 1, 1, 1, 1),('%', 1, 2, 1, 1),('*', 1, 3, 1, 1), 
           ('7', 2, 0, 1, 1),('8', 2, 1, 1, 1),('9', 2, 2, 1, 1),('-', 2, 3, 1, 1),
           ('4', 3, 0, 1, 1),('5', 3, 1, 1, 1),('6', 3, 2, 1, 1),('+', 3, 3, 1, 1), 
           ('1', 4, 0, 1, 1),('2', 4, 1, 1, 1),('3', 4, 2, 1, 1),('=', 4, 3, 2, 2),
           ('0', 5, 0, 1, 1),('del',5, 1, 1, 1),('.', 5, 2, 1, 1)]

for (text, row, column, rowspan, columnspan) in buttons:
    if text == 'C':
        button = tk.Button(app, text=text, width=5, height=2, bg="#3697f5", command=clear_entry)
    elif text == '=':
        button = tk.Button(app, text=text, width=5, height=4, bg="#fe9037", command=evaluate)
    elif text == '0':
        button = tk.Button(app, text=text, width=5, height=2, bg="#e9dccd", command=lambda t=text: add_number(t))
    elif text == 'del':
        button = tk.Button(app, text=text, width=5, height=2, bg="#e9dccd", command=delete)
    else:
        button = tk.Button(app, text=text, width=5, height=2, bg="#e9dccd", command=lambda t=text: add_number(t))
    button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, pady=5)
app.mainloop()