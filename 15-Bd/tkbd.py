import tkinter as tk
from tkinter import ttk,messagebox
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





tableau=ttk.Treeview(fenetre,columns=('id','nom','telephone'),show='headings')
tableau.heading('id',text="ID")
tableau.heading('nom',text="NOM")
tableau.heading('telephone',text="TELEPHONE")
tableau.pack()

fenetre.mainloop()