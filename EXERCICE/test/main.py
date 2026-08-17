import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("700x300")
a=tk.Entry(fenetre,width=100,border=3)
a.insert(0,"martial")
a.pack()

def onClick():
    lab=tk.Label(fenetre, text=f"Vous avez saisie {a.get()}")
    lab.pack()

btn=tk.Button(fenetre,text="envoyer", command=onClick).place(x=0,y=50)
fenetre.mainloop()