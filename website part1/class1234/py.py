from tkinter import *

root = Tk()
root.geometry('400x400')
root.configure(bg='orange')

def top():
    top = Toplevel(root)  
    top.geometry('150x150')
    
    label1 = Label(top, text='Toplevel window')  
    label1.place(x=20, y=20)  

Button1 = Button(root, text='Top level window', width=30, command=top)  
Button1.place(x=100, y=200)  

root.mainloop()