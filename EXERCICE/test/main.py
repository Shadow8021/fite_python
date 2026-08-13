import tkinter as tk
fen=tk.Tk()

fen["bg"]="red"

menu_principal = tk.Menu(fen)
fen.config(menu=menu_principal)
menu_principal.add_cascade(label="martial")
fen.mainloop()