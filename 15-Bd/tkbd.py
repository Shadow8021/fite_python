import tkinter as tk
from tkinter import ttk
fenetre=tk.Tk()
fenetre.withdraw()
splash=tk.Toplevel(fenetre)
splash.overrideredirect(True)
splash.geometry("700x400+360+160")
ttk.Label(splash,text="Bienvenue").place(x=300,y=100)


def demarrer():
    splash.destroy()
    fenetre.deiconify()
splash.after(5000, demarrer)
tk.Label(fenetre,text="mon app").place(x=300,y=100)
fenetre.mainloop()