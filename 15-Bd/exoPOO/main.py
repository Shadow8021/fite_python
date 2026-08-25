import sqlite3
import tkinter as tk
from tkinter import messagebox,ttk
from datetime import datetime
import os
#creation de la class database
class DataBase:
    def __init__(self):
        self.con =sqlite3.connect('./15-Bd/poo.db')
        self.cursor=self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""create table if not exists etudiants (
                    id integer primary key AUTOINCREMENT,
                    nom text not null,
                    telephone text not null,
                    sexe text,
                    classe text not null,
                    photo_path text ,
                    date_inscription text not null
        
        )""")
        self.con.commit()

    def insert_stuent(self, datas):
        self.cursor.execute("""insert into etudiants(
                nom,telephone,sexe,classe,photo_path,date_inscription
                ) values(?,?,?,?,?,?,?)""",(datas))
        self.con.commit()
        self.cursor.lastrowid


    def get_All(self):
        self.cursor.execute("select * from etudiants")
        return(self.cursor.fetchall())

    def getById(self,id):
        self.cursor.execute("select * from etudiants where id=?",(id))
        return (self.cursor.fetchone())

    def update (self,datas,id):
        requete="""update etudiants set nom=?,
                                    prenom=?,
                                    telephone=?,
                                    sexe=?,
                                    photo_path=?
                                    ,date_inscription where id=?"""
        self.cursor.execute(requete,(datas,id))
        self.con.commit()

    def Delete(self,id):
        req="delete * from etudiants where id=?"
        self.cursor.execute(req,id)
        self.con.commit()

    def ferme(self):
        self.con.close




#class Inscription

class Inscription:
    def __init__(self):
        #initial database
        self.db=DataBase()
        #data base visruelle
        self.photo_dir="student_images"
        if not os.path.exists(self.photo_dir):
            os.makedirs(self.photo_dir)
        #elements
        self.photo_path=None
        self.photo_image=None
        self.student_actuel=None
        self.tk_image=None
        #initial tkinter
        self.fen=tk.Tk()
        self.fen.title("Inscription des etudiants")
        self.fen.geometry("800x500")
        self.fen.configure(bg="grey")

        self.generation_interface()
        self.fen.mainloop()

    def generation_interface(self):
        entete=tk.Label(text="SYSTEME D'INSCRIPTION FITE",font=("liberation sans",20,"bold"),
                        fg='white',bg="green",pady=10)
        entete.pack(fill="x")

        #conteneur principal
        conteneur_principal= tk.Frame(self.fen,bg='grey')
        conteneur_principal.pack(padx=10,pady=10,fill="both",expand=True)

        #conteneur gauche
        conteneur_gauch=tk.LabelFrame(conteneur_principal, text="PERTIE INSCRIPTION",
                                 font=("liberation sans",20,"bold"),
                                 )
        conteneur_gauch.pack(side='left',fill="both",expand=True)
        tk.Label(conteneur_gauch,text="Photo :",font=("Liberation Mono",20,"bold")).grid(row=0,column=0,padx=5,pady=5)
        #conteneur image
        conteneur_photo=tk.Frame(conteneur_gauch)
        conteneur_photo.grid(row=0,column=1,padx=5,pady=5)
        self.photo_image=tk.Label(conteneur_photo,
                                  text="Cliquer pour ajouter",width=15,height=15,bd=3,bg="grey",padx=20)
        self.photo_image.pack(side='left')
        self.photo_image.bind('<Button-1>',print("hello"))

        btn_photo=tk.Frame(conteneur_photo)
        btn_photo.pack(side='left',padx=5)
        #btn
        tk.Button(btn_photo,text="Choisir la photo", bg="blue",fg="grey").pack()
        tk.Button(btn_photo,text="supprimer", bg="red", fg='white').pack()
        #formulaire
        tk.Label(conteneur_gauch,text="Nom:").grid(row=1,column=0,padx=5)
        self.nom=tk.Entry(conteneur_gauch).grid(row=1,column=1)

        tk.Label(conteneur_gauch,text="Téléphone:").grid(row=2,column=0,pady=5)
        self.prenom=tk.Entry(conteneur_gauch).grid(row=2,column=1,columnspan=2,pady=5)

        tk.Label(conteneur_gauch,text="Nom(s):").grid(row=1,column=0,padx=5)
        self.sexe=tk.Radiobutton(conteneur_gauch,text="Home").grid(row=3,column=0,pady=5)
        
app=Inscription()