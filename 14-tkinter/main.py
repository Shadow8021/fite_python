import tkinter as tk
from tkinter import messagebox



def nombre_unique(value):
    return value.isdigit() or value==""

def demander_quitter():
    if messagebox.askyesno("Quitter","Voulez vous vraiment quitter?"):
        fenetre.destroy()

def valider():
    nom=nom_entry.get().strip()
    prenom=prenom_entry.get().strip()
    ville=ville_entry.get().strip()
    phone=phone_entry.get().strip()
    if not nom or not prenom or not ville or not phone:
        messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
    else:
        messagebox.showinfo("Succès", f"Bonjour {prenom} {nom}, vous habitez à {ville} et votre numéro de téléphone est {phone}.")


def effacer():
    nom_entry.delete(0, tk.END)
    prenom_entry.delete(0, tk.END)
    ville_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    nom_entry.focus()


fenetre = tk.Tk()
titre = tk.Label(fenetre, text="Bienvenu, veuillez remplir le formulaire", fg="blue", font=("Arial", 14))
titre.pack(pady=10)

cadre_formulaire = tk.Frame(fenetre)
cadre_formulaire.pack(pady=10)
nom_label = tk.Label(cadre_formulaire, text="Nom:")
nom_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
nom_entry = tk.Entry(cadre_formulaire)
nom_entry.grid(row=0, column=1, padx=10, pady=5)

prenom_label = tk.Label(cadre_formulaire, text="Prénom:")
prenom_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
prenom_entry = tk.Entry(cadre_formulaire)
prenom_entry.grid(row=1, column=1, padx=10, pady=5)

ville_label = tk.Label(cadre_formulaire, text="Ville:")
ville_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
ville_entry = tk.Entry(cadre_formulaire)
ville_entry.grid(row=2, column=1, padx=10, pady=5)

phone_label = tk.Label(cadre_formulaire, text="Téléphone:")
phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
phone_entry = tk.Entry(cadre_formulaire)
phone_entry.grid(row=3, column=1, padx=10, pady=5)

bouton_valider = tk.Button(fenetre, text="Valider", command=valider)
bouton_valider.pack(pady=10)

bouton_effacer = tk.Button(fenetre, text="Effacer", command=effacer)
bouton_effacer.pack(pady=10)

bouton_quitter = tk.Button(fenetre, text="Quitter", command=demander_quitter)
bouton_quitter.pack(pady=10)

fenetre.protocol("WM_DELETE_WINDOW", demander_quitter)
fenetre.title("Formulaire pour resident")
fenetre.geometry("400x300") 

fenetre.mainloop()