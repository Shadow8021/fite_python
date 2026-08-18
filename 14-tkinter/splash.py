import tkinter as tk
from tkinter import ttk
fenetre=tk.Tk()
fenetre.withdraw()
splash=tk.Toplevel(fenetre)
splash.overrideredirect(True)
splash.geometry("300x200+500+300")
ttk.Label(splash,text="Bienvenue",bg="gree",fg="red").pack(padx=10,pady=10,fill="x")

fenetre.mainloop()