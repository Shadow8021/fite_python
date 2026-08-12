import tkinter as tk

fenetre=tk.Tk()
fenetre.title("mon menu")
menu_principal=tk.Menu(fenetre)
menu_fichier=tk.Menu(menu_principal,tearoff=0)
fenetre.mainloop()
