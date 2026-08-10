import tkinter as tk
fn=tk.Tk()
fn.title("my super App")
fn.geometry("500x500")
fn["bg"]="red"


tk.Label(fn,text="mon texte ultime").place(x="50",y="50")


fn.mainloop()