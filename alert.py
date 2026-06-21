from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Alert box")
root.geometry('500x500')

def msg():
    messagebox.showwarning('Alert', 'Stop! Virus Found')

btn=Button(text='Scan for virus', command=msg)
btn.pack()

root.mainloop()