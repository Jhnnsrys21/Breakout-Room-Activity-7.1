from tkinter import *
from tkinter import messagebox

def submit():
    location=entry1.get()
    destination=entry2.get()

    if (location=="" and destination==""):
        messagebox.showinfo("","Please Input Location or Destination")


root=Tk()
root.title("Mapquest")
root.geometry("450x250")

global entry1
global entry2

Label(root,text="Location").place(x=20,y=20)
Label(root,text="Destination").place(x=20,y=60)

entry1=Entry(root,bd=1)
entry1.place(x=150,y=20)

entry2=Entry(root,bd=1)
entry2.place(x=150,y=60)

Button(root,text="Submit",command=submit,height=1,width=10,bd=5).place(x=150,y=100)

root.mainloop()
