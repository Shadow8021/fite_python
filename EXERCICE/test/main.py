import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("500x300")

label = tk.Label(
    fenetre,
    text="Bonjour Tkinter",
    font=("Arial", 50, "bold")
)

label.pack(pady=50)

fenetre.mainloop()