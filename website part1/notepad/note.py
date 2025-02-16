from tkinter import*
from tkinter.filedialog import askopenfile,asksaveasfile
def open_file():
    file=askopenfile(mode='r',filetypes=[('textfiles','*.txt')])
    if file is not NONE:
        content=file.read()
        text1.insert(END,content)
    file.close()
def save_file():
    file=asksaveasfile(mode='w',filetypes=[('textfiles','*.txt')])
    if file is not NONE:
        file.write()
    file.close
window=Tk()
window.title("text editor")
window.geometry("500x400")
text1=Text(window,width=40,height=20,borderwidth=3,relief=SUNKEN)
button1=Button(window,text="open",width=10,command=open_file)
button2=Button(window,text="save as",width=10,command=save_file)
button1.grid(row=1,column=1,padx=10)
button2.grid(row=2,column=1,padx=10)
text1.grid(row=1,column=2,padx=10,rowspan=2)
window.mainloop()