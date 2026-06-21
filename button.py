from tkinter import *

root=Tk()
root.title('Event Handler')
root.geometry('500x500')

def handle_keypress(event):
    print(event.char)
root.bind("<Key>", handle_keypress)

def handle_click(event):
    print('Button is clicked')

btn=Button(text='click me', bg='yellow')

btn.pack()
btn.bind("<Button-1>", handle_click)

root.mainloop()