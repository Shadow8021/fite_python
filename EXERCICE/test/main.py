import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("700x300")

def onClick():
    label=tk.Label(fenetre, text="you have clicked on the button", fg='green')
    label.pack()

btn=tk.Button(fenetre,text="click me", padx=10, pady=50, command=onClick,fg="blue").pack(side="left",padx=40)
fenetre.mainloop()