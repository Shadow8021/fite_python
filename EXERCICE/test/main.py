import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("700x300")

btn=tk.Button(fenetre,text="click me", padx=10, pady=50).pack(side="left",padx=40)
fenetre.mainloop()