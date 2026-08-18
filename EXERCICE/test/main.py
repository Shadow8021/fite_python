import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("230x300")
fenetre.resizable(width=False,height=False)
a=tk.Entry(fenetre,border=3,width=36)
a.grid(column=0,row=0,columnspan=3)

def onClick():
    lab=tk.Label(fenetre, text=f"Vous avez saisie {a.get()}")
    lab.pack()

btn9=tk.Button(fenetre,text="9", command=onClick)
btn8=tk.Button(fenetre,text="8", command=onClick)
btn7=tk.Button(fenetre,text="7", command=onClick)
btn6=tk.Button(fenetre,text="6", command=onClick)
btn5=tk.Button(fenetre,text="5", command=onClick)
btn4=tk.Button(fenetre,text="4", command=onClick)
btn3=tk.Button(fenetre,text="3", command=onClick)
btn2=tk.Button(fenetre,text="2", command=onClick)
btn1=tk.Button(fenetre,text="1", command=onClick)
btn0=tk.Button(fenetre,text="0", command=onClick)


btn9.grid(column=1,row=1)
btn8.grid(column=0,row=1)
btn7.grid(column=0,row=1)

btn6.grid(column=1,row=2)
btn5.grid(column=2,row=2)
btn4.grid(column=3,row=2)

btn3.grid(column=1,row=3)
btn2.grid(column=2,row=3)
btn1.grid(column=3,row=3)


fenetre.mainloop()