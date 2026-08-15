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
).grid(column=0,row=0)
label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 10, "bold italic")
).grid(column=0,row=0)


fenetre.mainloop()