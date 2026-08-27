import tkinter as tk
from PIL import Image,ImageTk
app=tk.Tk()
app.title("martial")

image=ImageTk.PhotoImage(Image.open("./fite.png"))
labe=tk.Label(image=image)
labe.pack()
app.mainloop()


