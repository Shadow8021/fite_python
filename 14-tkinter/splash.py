import tkinter as tk
from tkinter import ttk
fenetre=tk.Tk()
fenetre.withdraw()
splash=tk.Toplevel(fenetre)

splash.geometry("700x400+360+160")
ttk.Label(splash,text="Bienvenue").pack(padx=10,pady=10,fill="x")


def demarrer():
    splash.destroy()
    fenetre.deiconify()
splash.after(5000, demarrer)

fenetre.mainloop()