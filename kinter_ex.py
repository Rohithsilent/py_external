from cgitb import text
import tkinter as tk
from tkinter import messagebox
from turtle import mainloop, title

def click():
    value1=entry1.get()
    value2=entry2.get()

    messagebox.showinfo("submitted",f"value1:{value1}\nvalue2:{value2}")


def reset():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)


root =tk.Tk()
root.title("form")

entry1_label=tk.Label(root,text="name")
entry1=tk.Entry(root)
entry1_label.pack()
entry1.pack()

entry2_label=tk.Label(root,text="email")
entry2=tk.Entry(root)
entry2_label.pack()
entry2.pack()

button1=tk.Button(root,text="submit",command=click)
button1.pack()

button2=tk.Button(root,text="reset",command=reset)
button2.pack()


root.mainloop()