from tkinter import*
from tkinter import messagebox
window=Tk()
window.title("message box")
window.geometry("300x300")
window.configure(bg="teal")
def msg():
    messagebox.showwarning("Alert","stop!! Virus found",)

button1=Button(window,text="click me",bg="grey",fg='white',command=msg)
button1.place(x=130,y=130)

window.mainloop()