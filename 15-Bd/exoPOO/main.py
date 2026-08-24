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
                nom,telephone,sexe,classe,photo_path,date-inscription
                ) values(?,?,?,?,?,?,?)""",(datas))
        self.con.commit()


    def get_All(self):
        return(self.cursor.execute("select * from etudiants"))

    def getById(self,id):
        return(self.cursor.execute("select * from etudiants where id=?",(id)))
