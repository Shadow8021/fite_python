import tkinter as tk

fenetre=tk.Tk()
fenetre.title("mon menu")
fenetre.geometry("500x500")
#menu
menu_principal=tk.Menu(fenetre)
fenetre.config(menu=menu_principal)
menu_fichier=tk.Menu(menu_principal)
menu_principal.add_cascade(label="Fichier",menu=menu_fichier)
menu_fichier.add_command(label="Nouveau",command=lambda: print("Nouveau"))
menu_fichier.add_command(label="Ouvrir",command=lambda: print("Ouvrir"))
menu_fichier.add_command(label="Quitter")














fenetre.mainloop()
