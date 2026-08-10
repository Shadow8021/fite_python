import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Formulaire")
fenetre.geometry("500x300")

formulaire = tk.Frame(fenetre)
formulaire.pack(pady=20)

tk.Label(formulaire, text="Nom :").grid(
    row=0, column=0, padx=10, pady=10
)

tk.Entry(formulaire).grid(
    row=0, column=1, padx=10, pady=10
)

tk.Label(formulaire, text="Prénoms :").grid(
    row=1, column=0, padx=10, pady=10
)

tk.Entry(formulaire).grid(
    row=1, column=1, padx=10, pady=10
)

tk.Label(formulaire, text="Ville :").grid(
    row=2, column=0, padx=10, pady=10
)

tk.Entry(formulaire).grid(
    row=2, column=1, padx=10, pady=10
)


# =====================================
# FRAME BUTTONS
# =====================================

buttons = tk.Frame(fenetre)
buttons.pack(pady=10)

tk.Button(buttons, text="Valider").pack(
    side="left", padx=5
)

tk.Button(buttons, text="Effacer").pack(
    side="left", padx=5
)

tk.Button(buttons, text="Quitter").pack(
    side="left", padx=5
)


fenetre.mainloop()