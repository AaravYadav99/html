from tkinter import*
window=Tk()
window.title("Login screen")

window.geometry("400x400")
window.configure(bg='grey')
frame1=Frame(window,relief='ridge',bg='blue',width=300,height=200,bd=3)
frame1.pack()
def greet():
    name=enter1.get()
    greeting="welcome"+name
    text1.delete("1.0","end")
    text1.insert("1.0",greeting)
label1=Label(frame1,text="User name",bg='blue')

label2=Label(frame1,text="Password",bg='blue')
enter1=Entry(frame1)
enter2=Entry(frame1,show="*")
button1=Button(frame1,text="login",bg="lightblue",command=greet)
label1.place(x=10,y=10)
label2.place(x=10,y=40)
enter1.place(x=100,y=10)
enter2.place(x=100,y=40)
button1.place(x=75,y=80)
text1=Text(window,relief='groove',bd=3)
text1.pack(pady=10)
window.mainloop()