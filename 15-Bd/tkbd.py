import tkinter as tk
from tkinter import ttk,messagebox
import sqlite3
#connexion à la bd
conn=sqlite3.connect("../15-Bd/contact.db")
cursor=conn.cursor()

#creation des tables
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        telephone INTEGER NOT NULL

               )''')









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

form=tk.Frame(fenetre).place(x=200,y=300)
tk.Label(form,text="NOM(s):").pack()
nom=tk.Entry(form).pack()
tk.Label(form,text="TEL:").pack()
tel=tk.Entry(form).pack()

























fenetre.mainloop()