import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("230x300")
fenetre.resizable(width=False,height=False)
a=tk.Entry(fenetre,border=3,width=36)
a.grid(column=0,row=0,columnspan=3)

def onClick():
    lab=tk.Label(fenetre, text=f"Vous avez saisie {a.get()}")
    lab.pack()

btn9=tk.Button(fenetre,text="9",padx=20,pady=16, command=onClick)
btn8=tk.Button(fenetre,text="8",padx=20,pady=16, command=onClick)
btn7=tk.Button(fenetre,text="7",padx=20,pady=16, command=onClick)
btn6=tk.Button(fenetre,text="6", padx=20,pady=16,command=onClick)
btn5=tk.Button(fenetre,text="5",padx=20,pady=16, command=onClick)
btn4=tk.Button(fenetre,text="4",padx=20,pady=16, command=onClick)
btn3=tk.Button(fenetre,text="3",padx=20,pady=16, command=onClick)
btn2=tk.Button(fenetre,text="2",padx=20,pady=16, command=onClick)
btn1=tk.Button(fenetre,text="1",padx=20,pady=16, command=onClick)
btn0=tk.Button(fenetre,text="0",padx=20,pady=16, command=onClick)


btn9.grid(column=0,row=2)
btn8.grid(column=1,row=2)
btn7.grid(column=2,row=2)

btn6.grid(column=0,row=3)
btn5.grid(column=1,row=3)
btn4.grid(column=2,row=3)

btn3.grid(column=0,row=4)
btn2.grid(column=1,row=4)
btn1.grid(column=2,row=4)


fenetre.mainloop()