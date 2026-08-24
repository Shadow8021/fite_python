import sqlite3
import tkinter as tk
from tkinter import messagebox,ttk
from datetime import datetime
import os
#creation de la class database
class DataBase:
    def __init__(self):
        self.con =sqlite3.connect('../exoPOO/poo.db')
        self.cursor=self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""create table if not exists etudiants (
                    id integer primary key autoincrement,
                    nom text not null,
                    telephone text not null,
                    sexe text,
                    classe text not null,
                    photo_path text ,
                    date_inscription text not null,
        
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
        self.fen.configure(bd="grey")

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

