import tkinter as tk

fenetre=tk.Tk()
fenetre.title("mon menu")
fenetre.geometry("500x500")
#menu
menu_principal=tk.Menu(fenetre)
fenetre.config(menu=menu_principal)
#menu fichier

menu_fichier=tk.Menu(menu_principal)
menu_principal.add_cascade(label="Fichier",menu=menu_fichier)
menu_fichier.add_command(label="Nouveau",command=lambda: print("Nouveau"))
menu_fichier.add_command(label="Ouvrir",command=lambda: print("Ouvrir"))

#menu edit


menu_edit=tk.Menu(menu_principal)
menu_principal.add_cascade(label="Edit",menu=menu_edit)
menu_edit.add_command(label="refaire", command=lambda: print("Refaire"))
menu_edit.add_command(label="Defaire", command=lambda: print("Defaire"))
menu_edit.add_command(label="Couper", command=lambda: print("Couper"))
#menu export
menu_export=tk.Menu(menu_fichier)
menu_fichier.add_cascade(label="Exporter",menu=menu_export)
menu_export.add_command(label="pdf", command=lambda:print("exporter comme pdf"))
menu_export.add_command(label="svg", command=lambda:print("exporter comme svg"))
menu_fichier.add_command(label="Quitter")

fenetre.mainloop()
