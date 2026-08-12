import tkinter as tk


# Fenêtre
fenetre = tk.Tk()
fenetre.title("Mon menu")
fenetre.geometry("500x500")


# Menu principal
menu_principal = tk.Menu(fenetre)
fenetre.config(menu=menu_principal)


# =========================
# MENU FICHIER
# =========================

menu_fichier = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(
    label="Fichier",
    menu=menu_fichier
)

menu_fichier.add_command(
    label="Nouveau",
    command=lambda: print("Nouveau")
)

menu_fichier.add_command(
    label="Ouvrir",
    command=lambda: print("Ouvrir")
)


# =========================
# MENU EXPORTER
# =========================

menu_export = tk.Menu(menu_fichier, tearoff=0)

menu_fichier.add_cascade(
    label="Exporter",
    menu=menu_export
)


# Sous-menu PDF
menu_pdf = tk.Menu(menu_export, tearoff=0)

menu_export.add_cascade(
    label="PDF",
    menu=menu_pdf
)

menu_pdf.add_command(
    label="Bonne qualité",
    command=lambda: print("PDF - bonne qualité")
)

menu_pdf.add_command(
    label="Moyenne qualité",
    command=lambda: print("PDF - moyenne qualité")
)

menu_pdf.add_command(
    label="Faible qualité",
    command=lambda: print("PDF - faible qualité")
)


# Sous-menu SVG
menu_svg = tk.Menu(menu_export, tearoff=0)

menu_export.add_cascade(
    label="SVG",
    menu=menu_svg
)

menu_svg.add_command(
    label="Bonne qualité",
    command=lambda: print("SVG - bonne qualité")
)

menu_svg.add_command(
    label="Moyenne qualité",
    command=lambda: print("SVG - moyenne qualité")
)

menu_svg.add_command(
    label="Faible qualité",
    command=lambda: print("SVG - faible qualité")
)


# =========================
# MENU EDIT
# =========================

menu_edit = tk.Menu(menu_principal, tearoff=0)

menu_principal.add_cascade(
    label="Edit",
    menu=menu_edit
)

menu_edit.add_command(
    label="Refaire",
    command=lambda: print("Refaire")
)

menu_edit.add_command(
    label="Défaire",
    command=lambda: print("Défaire")
)

menu_edit.add_command(
    label="Couper",
    command=lambda: print("Couper")
)


# =========================
# QUITTER
# =========================

menu_fichier.add_separator()

menu_fichier.add_command(
    label="Quitter",
    command=fenetre.destroy
)


# Lancement
fenetre.mainloop()