import tkinter as tk
from tkinter import messagebox
fenetre = tk.Tk()
fenetre.title("Calculatrice")
fenetre.geometry("500x300")
formulaire = tk.Frame(fenetre)
formulaire.pack(pady=20)

def Addition():
    try:
        a=float(nbr1.get())
        b=float(nbr2.get())
        resultat.config(text=f"Resultat: {nbr1+nbr2}")
    except:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres")



def Division():
    try:
        a=float(nbr1.get())
        b=float(nbr2.get())
        resultat.config(text=f"Resultat: {nbr1/nbr2}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres")
    except ZeroDivisionError:
            messagebox.showerror("Erreur", "Impossible deviser un nombre par zero (0)")



def Multiplication():
    try:
        a=float(nbr1.get())
        b=float(nbr2.get())
        resultat.config(text=f"Resultat: {nbr1*nbr2}")
    except:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres")



def Soustraction():
    try:
        a=float(nbr1.get())
        b=float(nbr2.get())
        resultat.config(text=f"Resultat: {nbr1+nbr2}")
    except:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres")






tk.Label(formulaire, text="Nombre1:").grid(
    row=0, column=0, padx=10, pady=10
)

nbr1=tk.Entry(formulaire).grid(
    row=0, column=1, padx=10, pady=10
)


tk.Label(formulaire, text="Nombre2:").grid(
    row=1, column=0, padx=10, pady=10
)

nbr2=tk.Entry(formulaire).grid(
    row=1, column=1, padx=10, pady=10
)



result=tk.Frame(fenetre)
result.pack(pady=10)

resultat=tk.Label(fenetre,text="reponse").pack()






buttons = tk.Frame(fenetre)
buttons.pack(pady=10)

tk.Button(buttons, text="Additionner",command=Addition).pack(
    side="left", padx=5
)

tk.Button(buttons, text="Diviser",command=Division).pack(
    side="left", padx=5
)

tk.Button(buttons, text="Multiplier",command=Multiplication).pack(
    side="left", padx=5
)
tk.Button(buttons, text="Soustraire",command=Soustraction).pack(
    side="left", padx=5
)

tk.Button(buttons, text="Quitter",command=fenetre.destroy).pack(
    side="left", padx=5
)



fenetre.mainloop()