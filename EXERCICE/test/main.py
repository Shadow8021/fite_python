import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("700x300")

label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 10, "bold italic")
).grid(column=0,row=0)

label1 = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 10, "bold italic")
).pack(side="bottom", padx=40)

label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 10, "bold italic")
).place(x=10,y=10)


fenetre.mainloop()