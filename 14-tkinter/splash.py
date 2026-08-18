import tkinter as tk
fenetre=tk.Tk()
fenetre.withdraw()
splash=tk.Toplevel(fenetre)
splash.overrideredirect(True)
splash.geometry("300x200+500+300")


fenetre.mainloop()