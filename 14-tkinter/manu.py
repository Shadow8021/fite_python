import tkinter as tk

fenetre=tk.Tk()
fenetre.title("mon menu")
fenetre.geometry("500x500")
#menu
menu_principal=tk.Menu(fenetre)
menu_fichier=tk.Menu(menu_principal,tearoff=0)
menu_principal.add_cascade(label="Fichier",menu=menu_fichier)














fenetre.mainloop()
