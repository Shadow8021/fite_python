import sqlite3


class DataBase:
    def _init(self):
        self.con =sqlite3.connect('../exoPOO/poo.db')
        self.cursor=self.con.cursor()

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