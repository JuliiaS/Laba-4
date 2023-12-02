from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("Цветики")
root.geometry("280x173")
root.configure(bg="grey42")

def fun_butt1():
    entry.delete(0, END)
    label.configure(text = "Красный")
    entry.insert(0, "#ff0000")

butt1 = Button(text= "", bg = "red", width = 3, height = 1, command = fun_butt1)
butt1.place(x = 30, y = 130)

def fun_butt2():
    entry.delete(0, END)
    label.configure(text = "Оранжевый")
    entry.insert(0, "#ff9900")

butt2 = Button (text= "", bg = "orange", width = 3, height = 1, command = fun_butt2)    
butt2.place(x=61, y= 130)

def fun_butt3():
    entry.delete(0, END)
    label.configure(text="Желтый")
    entry.insert(0, "#ffff00")

btn3 = Button(text="", bg="yellow", width=3, height=1, command=fun_butt3)
btn3.place(x=92, y=130)

def fun_butt4():
    entry.delete(0, END)
    label.configure(text="Зеленый")
    entry.insert(0, "#00ff00")

btn4 = Button(text="", bg="green", width=3, height=1, command=fun_butt4)
btn4.place(x=123, y=130)

def fun_butt5():
    entry.delete(0, END)
    label.configure(text="Голубой")
    entry.insert(0, "#00ffff")

btn5 = Button(text="", bg="blue", width=3, height=1, command=fun_butt5)
btn5.place(x=154, y=130)

def fun_butt6():
    entry.delete(0, END)
    label.configure(text="Cиний")
    entry.insert(0, "#0000ff")

btn6 = Button(text="", bg="dark blue", width=3, height=1, command=fun_butt6)
btn6.place(x=185, y=130)

def fun_butt7():
    entry.delete(0, END)
    label.configure(text="Фиолетовый")
    entry.insert(0, "#9900ff")

btn7 = Button(text="", bg="purple", width=3, height=1, command=fun_butt7)
btn7.place(x=216, y=130)

entry = ttk.Entry(width=16)
entry.place(x=92, y= 35)


label = ttk.Label(text="", width=16, background="aquamarine", foreground="black", justify=CENTER)
label.place(x=92, y=70)


root.mainloop()