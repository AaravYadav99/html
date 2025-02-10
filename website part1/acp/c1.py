import tkinter
from tkinter import*
window=Tk()
window.title("Grid system")
window.geometry("200x300")
t=1
for i in range(1,4):
    window.rowconfigure(i,weight=0,minsize=100)
    for j in range(1,4):
        window.columnconfigure(j,weight=0,minsize=50)

        label1=Label(window,relief=RAISED,bg='black',fg='red',text=t,width=2)
        t+=1
        label1.grid(row=i,column=j)
window.mainloop()