import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry("230x300")
fenetre.resizable(width=False,height=False)
a=tk.Entry(fenetre,border=3,width=36)
a.grid(column=0,row=0,columnspan=3)
lab=tk.Label(fenetre,text="")
lab.grid(column=0,row=1)
def onClick(nbr):
    lab=tk.Label(fenetre, text=f"Vous avez saisie {a.get()}")
    lab.pack()

btn9=tk.Button(fenetre,text="9",padx=20,pady=16,  command= lambda: onClick(9))
btn8=tk.Button(fenetre,text="8",padx=20,pady=16, command= lambda: onClick(8))
btn7=tk.Button(fenetre,text="7",padx=20,pady=16, command= lambda: onClick(7))
btn6=tk.Button(fenetre,text="6", padx=20,pady=16,command= lambda: onClick(6))
btn5=tk.Button(fenetre,text="5",padx=20,pady=16, command= lambda: onClick(5))
btn4=tk.Button(fenetre,text="4",padx=20,pady=16, command= lambda: onClick(4))
btn3=tk.Button(fenetre,text="3",padx=20,pady=16, command= lambda: onClick(3))
btn2=tk.Button(fenetre,text="2",padx=20,pady=16, command= lambda: onClick(2))
btn1=tk.Button(fenetre,text="1",padx=20,pady=16, command= lambda: onClick(1))
btn0=tk.Button(fenetre,text="0",padx=20,pady=16, command= lambda: onClick(0))


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