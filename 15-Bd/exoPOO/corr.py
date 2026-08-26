import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import os


# ============================================================
# CLASS DATABASE
# ============================================================

class DataBase:

    def __init__(self):
        self.con = sqlite3.connect("./poo.db")
        self.cursor = self.con.cursor()
        self.create_table()

    # --------------------------------------------------------
    # Création de la table
    # --------------------------------------------------------

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS etudiants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                telephone TEXT NOT NULL,
                sexe TEXT,
                classe TEXT NOT NULL,
                photo_path TEXT,
                date_inscription TEXT NOT NULL
            )
        """)

        self.con.commit()

    # --------------------------------------------------------
    # Insérer un étudiant
    # --------------------------------------------------------

    def insert_student(self, datas):

        self.cursor.execute("""
            INSERT INTO etudiants (
                nom,
                telephone,
                sexe,
                classe,
                photo_path,
                date_inscription
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, datas)

        self.con.commit()

        return self.cursor.lastrowid

    # --------------------------------------------------------
    # Récupérer tous les étudiants
    # --------------------------------------------------------

    def get_all(self):

        self.cursor.execute("""
            SELECT * FROM etudiants
        """)

        return self.cursor.fetchall()

    # --------------------------------------------------------
    # Récupérer un étudiant par son ID
    # --------------------------------------------------------

    def get_by_id(self, student_id):

        self.cursor.execute("""
            SELECT * FROM etudiants
            WHERE id = ?
        """, (student_id,))

        return self.cursor.fetchone()

    # --------------------------------------------------------
    # Modifier un étudiant
    # --------------------------------------------------------

    def update(self, datas, student_id):

        requete = """
            UPDATE etudiants
            SET
                nom = ?,
                telephone = ?,
                sexe = ?,
                classe = ?,
                photo_path = ?,
                date_inscription = ?
            WHERE id = ?
        """

        self.cursor.execute(
            requete,
            (*datas, student_id)
        )

        self.con.commit()

    # --------------------------------------------------------
    # Supprimer un étudiant
    # --------------------------------------------------------

    def delete(self, student_id):

        requete = """
            DELETE FROM etudiants
            WHERE id = ?
        """

        self.cursor.execute(
            requete,
            (student_id,)
        )

        self.con.commit()

    # --------------------------------------------------------
    # Fermer la base de données
    # --------------------------------------------------------

    def ferme(self):

        self.con.close()


# ============================================================
# CLASS INSCRIPTION
# ============================================================

class Inscription:

    def __init__(self):

        # Initialisation de la base de données
        self.db = DataBase()

        # Dossier contenant les photos
        self.photo_dir = "student_images"

        if not os.path.exists(self.photo_dir):
            os.makedirs(self.photo_dir)

        # Variables
        self.photo_path = None
        self.photo_image = None
        self.student_actuel = None
        self.tk_image = None

        # ----------------------------------------------------
        # Fenêtre Tkinter
        # ----------------------------------------------------

        self.fen = tk.Tk()

        self.fen.title("Inscription des étudiants")
        self.fen.geometry("800x500")
        self.fen.configure(bg="grey")

        # Génération de l'interface
        self.generation_interface()

        # Fermeture propre
        self.fen.protocol(
            "WM_DELETE_WINDOW",
            self.fermer_application
        )

        # Lancement
        self.fen.mainloop()

    # --------------------------------------------------------
    # Interface graphique
    # --------------------------------------------------------

    def generation_interface(self):

        # ----------------------------------------------------
        # ENTÊTE
        # ----------------------------------------------------

        entete = tk.Label(
            self.fen,
            text="SYSTÈME D'INSCRIPTION FITE",
            font=("Liberation Sans", 20, "bold"),
            fg="white",
            bg="green",
            pady=10
        )

        entete.pack(
            fill="x"
        )

        # ----------------------------------------------------
        # CONTENEUR PRINCIPAL
        # ----------------------------------------------------

        conteneur_principal = tk.Frame(
            self.fen,
            bg="grey"
        )

        conteneur_principal.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

        # ----------------------------------------------------
        # CONTENEUR GAUCHE
        # ----------------------------------------------------

        conteneur_gauche = tk.LabelFrame(
            conteneur_principal,
            text="PARTIE INSCRIPTION",
            font=("Liberation Sans", 14, "bold")
        )

        conteneur_gauche.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        # ----------------------------------------------------
        # CONTENEUR DROIT
        # ----------------------------------------------------

        conteneur_droit = tk.LabelFrame(
            conteneur_principal,
            text="LISTE DES ÉTUDIANTS",
            font=("Liberation Sans", 14, "bold")
        )

        conteneur_droit.pack(
            side="right",
            fill="both",
            expand=True,
            padx=5
        )

        # ----------------------------------------------------
        # FORMULAIRE
        # ----------------------------------------------------

        tk.Label(
            conteneur_gauche,
            text="Nom :"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_nom = tk.Entry(
            conteneur_gauche
        )

        self.entry_nom.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # Téléphone

        tk.Label(
            conteneur_gauche,
            text="Téléphone :"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.entry_telephone = tk.Entry(
            conteneur_gauche
        )

        self.entry_telephone.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # Sexe

        tk.Label(
            conteneur_gauche,
            text="Sexe :"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.combo_sexe = ttk.Combobox(
            conteneur_gauche,
            values=["Homme", "Femme"],
            state="readonly"
        )

        self.combo_sexe.grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        # Classe

        tk.Label(
            conteneur_gauche,
            text="Classe :"
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.combo_classe = ttk.Combobox(
            conteneur_gauche,
            values=[
                "L1",
                "L2",
                "L3",
                "M1",
                "M2"
            ],
            state="readonly"
        )

        self.combo_classe.grid(
            row=3,
            column=1,
            padx=10,
            pady=10
        )

        # ----------------------------------------------------
        # BOUTON INSCRIPTION
        # ----------------------------------------------------

        bouton_inscription = tk.Button(
            conteneur_gauche,
            text="INSCRIRE",
            bg="green",
            fg="white",
            font=("Liberation Sans", 11, "bold"),
            command=self.inscrire
        )

        bouton_inscription.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=20
        )

        # ----------------------------------------------------
        # TABLEAU
        # ----------------------------------------------------

        colonnes = (
            "id",
            "nom",
            "telephone",
            "sexe",
            "classe",
            "date"
        )

        self.table = ttk.Treeview(
            conteneur_droit,
            columns=colonnes,
            show="headings"
        )


       
        for el in colonnes:
            self.table.heading(
                        el,
                        text=el
                    )
        


        self.table.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        self.charger_etudiants()

    # --------------------------------------------------------
    # Inscription
    # --------------------------------------------------------

    def inscrire(self):

        nom = self.entry_nom.get().strip()
        telephone = self.entry_telephone.get().strip()
        sexe = self.combo_sexe.get()
        classe = self.combo_classe.get()

        # Vérification

        if not nom:
            messagebox.showwarning(
                "Attention",
                "Veuillez entrer le nom."
            )
            return

        if not telephone:
            messagebox.showwarning(
                "Attention",
                "Veuillez entrer le numéro de téléphone."
            )
            return

        if not classe:
            messagebox.showwarning(
                "Attention",
                "Veuillez sélectionner une classe."
            )
            return

        date_inscription = datetime.now().strftime(
            "%d/%m/%Y %H:%M"
        )

        datas = (
            nom,
            telephone,
            sexe,
            classe,
            self.photo_path,
            date_inscription
        )

        self.db.insert_student(datas)

        messagebox.showinfo(
            "Succès",
            "Étudiant inscrit avec succès !"
        )

        self.vider_formulaire()
        self.charger_etudiants()

    # --------------------------------------------------------
    # Charger les étudiants
    # --------------------------------------------------------

    def charger_etudiants(self):

        # Supprimer les anciennes lignes

        for item in self.table.get_children():
            self.table.delete(item)

        # Récupérer les étudiants

        etudiants = self.db.get_all()

        for etudiant in etudiants:

            id_etudiant = etudiant[0]
            nom = etudiant[1]
            telephone = etudiant[2]
            sexe = etudiant[3]
            classe = etudiant[4]
            date = etudiant[6]

            self.table.insert(
                "",
                "end",
                values=(
                    id_etudiant,
                    nom,
                    telephone,
                    sexe,
                    classe,
                    date
                )
            )

    # --------------------------------------------------------
    # Vider le formulaire
    # --------------------------------------------------------

    def vider_formulaire(self):

        self.entry_nom.delete(
            0,
            tk.END
        )

        self.entry_telephone.delete(
            0,
            tk.END
        )

        self.combo_sexe.set("")

        self.combo_classe.set("")

        self.photo_path = None

    # --------------------------------------------------------
    # Fermer l'application
    # --------------------------------------------------------

    def fermer_application(self):

        self.db.ferme()

        self.fen.destroy()


# ============================================================
# LANCEMENT
# ============================================================

if __name__ == "__main__":

    app = Inscription()