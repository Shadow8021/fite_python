import sqlite3


class DataBase:
    def _init(self):
        self.con =sqlite3.connect('../exoPOO/poo.db')
        self.cursor=self.con.cursor()