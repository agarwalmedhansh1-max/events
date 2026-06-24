from tkinter import *

root= Tk()
root.title("Length Converter app")
root.geometry("400x400")

num = Label(text='Enter measurement in centimeter', fg='black', bg='white')
n=Entry()

def display():
    n1=n.get()

    inch=int(n1)/2.54
    textbox.insert(END, inch)

textbox=Text(height=10)

btn=Button(text='convert', command=display, height=1, bg='yellow', fg='black')

num.pack()
n.pack()
textbox.pack()
btn.pack()

root.mainloop()