import tkinter as tk

fen=tk.Tk()
fen.title("test scrollbar")
list=tk.Listbox(fen)
list.pack(side="left", fill="y")
barre=tk.Scrollbar(fen,orient='vertical',command=list.yview)
barre.pack(side="right",fill='y')
list.config(yscrollcommand=barre.set)
for i in range(80):
    list.insert(tk.END,f"Element{i} Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consectetur, ")


list2=tk.Listbox(fen)
barre2=tk.Scrollbar(fen,orient='horizontal',command=list2.yview)
barre2.pack(side="bottom",fill='y')
list2.config(yscrollcommand=barre2.set)
for i in range(50):
    list2.insert(tk.END,f"Element{i} Lorem, ipsum dolor sit amet consectetur adipisicing elit. Consectetur, ")
















fen.mainloop()
