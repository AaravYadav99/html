from tkinter import*
win=Tk()
win.geometry("400x400")
win.title("greeting")
def mygreet():
    name=entry1.get()
    greeting="welcome"+name
    text1.delete("1.0","end")
    text1.insert("1.0",greeting)

label=Label(text="name",fg="lightblue")
label.pack()

entry1=Entry()
entry1.pack()
button1=Button(text="greet",fg="skyblue",bg="red",command=mygreet)
button1.pack()
text1=Text(width=100,height=3,border=2)
text1.pack()
win.mainloop()