#!/usr/bin/python
import sqlite3
import tkinter as tk
from tkinter import messagebox,ttk,filedialog
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
                    prnom text not null,
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
        entete=tk.Label(text="SYSTEME D'INSCRIPTION FITE",font=("DejaVu Sans",20,"bold"),
                        fg='white',bg="green",pady=10)
        entete.pack(fill="x")

        #conteneur principal
        conteneur_principal= tk.Frame(self.fen,bg='grey')
        conteneur_principal.pack(padx=10,pady=10,fill="both",expand=True)

        #conteneur gauche
        conteneur_gauch=tk.LabelFrame(conteneur_principal, text="PERTIE INSCRIPTION",
                                 font=("DejaVu Sans",10,"bold"),
                                 )
        conteneur_gauch.pack(side='left',fill="both")
        tk.Label(conteneur_gauch,text="Photo :",font=("DejaVu Sans",10,"bold")).grid(row=0,column=0,padx=5,pady=5)
        #conteneur image
        conteneur_photo=tk.Frame(conteneur_gauch)
        conteneur_photo.grid(row=0,column=1,padx=5,pady=5)
        self.photo_image=tk.Label(conteneur_photo,
                                  text="Cliquer pour ajouter",font=("DejaVu Sans",10,""),width=15,height=15,bd=1,bg="grey",padx=20)
        self.photo_image.pack(side='left')
        self.photo_image.bind('<Button-1>',print("hello"))

        btn_photo=tk.Frame(conteneur_photo)
        btn_photo.pack(side='left',padx=5)
        #btn
        tk.Button(btn_photo,text="Choisir la photo",font=("DejaVu Sans",10,""), bg="blue",fg="white").pack()
        tk.Button(btn_photo,text="supprimer", bg="red", fg='white',font=("DejaVu Sans",10,"")).pack()
        #formulaire
        tk.Label(conteneur_gauch,text="Nom:",font=("DejaVu Sans",10,"")).grid(row=1,column=0,padx=5)
        self.nom=tk.Entry(conteneur_gauch,width=25).grid(row=1,column=1)
        tk.Label(conteneur_gauch,text="Prenom:",font=("DejaVu Sans",10,"")).grid(row=2,column=0,padx=5)
        self.prenom=tk.Entry(conteneur_gauch,width=25).grid(row=2,column=1,pady=5)
        tk.Label(conteneur_gauch,text="Téléphone:",font=("DejaVu Sans",10,"")).grid(row=3,column=0,pady=5)
        self.phone=tk.Entry(conteneur_gauch,width=25).grid(row=3,column=1)
        #conteneur sexe
        tk.Label(conteneur_gauch,text="Sexe: ",font=("DejaVu Sans",10,"")).grid(row=4,column=0,padx=5)
        conteneur_sexe=tk.Frame(conteneur_gauch)
        conteneur_sexe.grid(row=4,column=1,padx=5,pady="5")
        self.sexe=tk.StringVar(value="")
        tk.Radiobutton(conteneur_sexe,text="Home" ,variable=self.sexe,value="Masculin").pack(side='left',padx=10)
        tk.Radiobutton(conteneur_sexe,text="Feminin",variable=self.sexe,value="Femini").pack(side="left",padx=10)
        #classe
        tk.Label(conteneur_gauch,text="Classe: ",font=("DejaVu Sans",10,"")).grid(row=5,column=0,padx=5)

        self.classe=tk.StringVar()
        self.classe_combo=ttk.Combobox(conteneur_gauch,textvariable=self.classe,values=["L1","L2","L3"],width=23)
        self.classe_combo.grid(row=5,column=1)
        self.classe_combo.current(0)
        #section btn
        conteneur_btn=tk.Frame(conteneur_gauch,pady=10)
        conteneur_btn.grid(columnspan=3)
        tk.Button(conteneur_btn,text="Ajouter",bg="green",fg="white").pack(side='left',padx=10)
        tk.Button(conteneur_btn,text="Modifier",bg="blue",fg="white").pack(side='left',padx=10)
        tk.Button(conteneur_btn,text="Supprimer",bg="red",fg="white").pack(side='left',padx=10)
        tk.Button(conteneur_btn,text="Raffraichir").pack(side='left',padx=10)


        #conteneur droit
        conteneur_droit=tk.LabelFrame(conteneur_principal, text="LISTE DES INSCRITS",font=("DejaVu Sans",10,"bold"))
        conteneur_droit.pack(side="right",padx=5,fill="both",expand=True)
        #tableaux
        colonnes=("ID","NOM","PRENOM","TELEPHONE","CLASSE")
        self.tableau=ttk.Treeview(conteneur_droit,columns=colonnes,show='headings',height=10)

        for col in colonnes:
                self.tableau.heading(col,text=col)

        self.tableau.column("ID",width=40)
        self.tableau.column("NOM",width=100)
        self.tableau.column("PRENOM",width=80)
        self.tableau.column("TELEPHONE",width=100)
        self.tableau.column("CLASSE",width=10)

        #scrolbar 
        scrollBar=ttk.Scrollbar(self.tableau,orient='vertical',command=self.tableau.yview)
        self.tableau.configure(yscrollcommand=scrollBar.set)
        scrollBar.pack(side="right",fill='y',pady=15)

        self.tableau.pack(side="left",fill="both",expand=True,pady=5)
        #section detail
        detail_conteneur=tk.LabelFrame(conteneur_droit,text="INFORMATIONS",font=("DejaVu sans",10,"bold"),width=200,height=80)
        detail_conteneur.pack(side="top",fill="x",expand=True)
        detail=tk.Frame(detail_conteneur,pady=8,padx=8,bd=8)
        detail.pack(fill="both")

        self.detail_photo=tk.Label(detail,text="IMAGE",font=("DejaVu sans",10,"bold"),width=10,height=4,bd=1)
        self.detail_photo.pack(side="right")

        self.detail_info=tk.Label(detail_conteneur,text="Details de l'etudiant")
        self.detail_info.pack(side="right",fill="both",pady=5)

        self.total_etudiant=tk.Label(conteneur_droit,text="Total Iscrits")
        self.total_etudiant.pack(pady=8)

        def choisir_image(self):
            ficher_path=filedialog.askopenfilename(
                title="choisir une image",
                filetypes=[
                    ("Image PNG","*.png"),
                    ("image GIF","*.gig")
                ],
            )
            if ficher_path:
                self.photo_path=ficher_path
                self.lire_image=(ficher_path,self.label_image)

        def lire_image(self,path,label,dimenssion=(120,100)):
            try:
                img =tk.PhotoImage(file=path)
                img_width=img.width()
                img_height=img.height()
                if img_width>dimenssion[0] or img_height>dimenssion[1]:
                    facteur_x=max(1,img_width//dimenssion[0])
                    facteur_y=max(1,img_height//dimenssion[1])
                    facteur=max(facteur_x,facteur_y)
                    img=img.subsample(facteur,facteur)
                    self.tk_image=img
                    label.config(image=img,width=0,height=0)
                    label.image=img
                    return img
            except Exception as e:
                messagebox.showerror("Erreue image",f"Impossible d'ouvrir le fichier{e}")


app=Inscription()