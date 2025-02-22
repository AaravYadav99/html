from tkinter import *

def calculate():
    global entry1, entry2, entry3, entry4  
    amount = int(entry1.get())

    n2000 = amount // 2000
    amount = amount % 2000

    n500 = amount // 500
    amount = amount % 500

    n100 = amount // 100
    amount = amount % 100

    entry2.delete(0, END)
    entry2.insert(END, str(n2000))

    entry3.delete(0, END)
    entry3.insert(END, str(n500))

    entry4.delete(0, END)
    entry4.insert(END, str(n100))

def top():
    global entry1, entry2, entry3, entry4  

    top = Toplevel()
    top.title("Denomination Calculator")
    top.geometry("400x400")
    top.configure(bg="skyblue")

    label1 = Label(top, text="Enter the amount")
    entry1 = Entry(top)

    button2 = Button(top, text="Calculate", command=calculate) 

    label2 = Label(top, text="Number of notes")
    label3 = Label(top, text="2000")
    entry2 = Entry(top)

    label4 = Label(top, text="500")
    entry3 = Entry(top)

    label5 = Label(top, text="100")
    entry4 = Entry(top)

    label1.place(x=20, y=10)
    entry1.place(x=150, y=10)

    label2.place(x=20, y=50)
    label3.place(x=20, y=80)
    entry2.place(x=100, y=80)

    label4.place(x=20, y=110)
    entry3.place(x=100, y=110)

    label5.place(x=20, y=140)
    entry4.place(x=100, y=140)

    button2.place(x=150, y=200)  

root = Tk()
root.geometry('300x400')
root.configure(bg="grey")

button1 = Button(root, text="Denomination Calculator", command=top)
button1.place(x=80, y=200)

root.mainloop()
