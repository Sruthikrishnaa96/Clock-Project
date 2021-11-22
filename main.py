from tkinter import *

from tkinter import Label

from tkinter.ttk import *

from time import strftime

root = Tk()

root.title("The Time is:")


root.resizable(0,0)


def time():
    string = strftime("%H:%M:%S %p")
    Label.config(text=string)
    Label.after(500,time)


Label= Label(root, font = ("Digital-7 italic",75),background= "black",foreground= "cyan")

Label.pack(anchor='center')

time()

mainloop()