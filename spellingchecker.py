import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("spelling checker")
root.geometry("700x400")
root.configure(background="#dae6f6")
def spellcheck():
    word=entertexxt.get()
    a=TextBlob(word)
    right= str(a.correct())

    cs=Label(root, text=" Correct text is :", font=("poppins", 20), bg="lightblue", fg="green")
    cs.place(x=150, y=250)
    spell.config(text=right)

heading = Label(root,text="spelling checker", font=("Trebuchet MS",30,"bold"), bg="#dae6f6", fg="#368961")
heading.pack(pady=(50,0))
entertexxt= Entry(root, justify="center", width=30, font=("poppins",20), bg="white", border=3)
entertexxt.pack(pady=10,padx=25)
entertexxt.focus_force()

button=Button(root, text="Check",font=("arial",20,"bold"),fg="lightblue",bg="red", width=10, command=spellcheck)
button.pack()
spell = Label(root,font=("poppins", 20), fg="green", bg="lightblue" )
spell.place(x=350, y=250),
root.mainloop()
