import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("700x300")

label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Liberation Sans", 50, "bold italic")
)

label.pack(pady=50)

fenetre.mainloop()