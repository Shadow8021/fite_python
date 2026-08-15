import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("700x300")

label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 10, "bold italic")
).grid(column=0,row=0)

label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 10, "bold italic")
).grid(column=1,row=0)
label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 10, "bold italic")
).grid(column=2,row=0)

label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 10, "bold italic")
).place(x=10,y=10)


fenetre.mainloop()