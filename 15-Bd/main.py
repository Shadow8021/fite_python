import sqlite3

#provider
con=sqlite3.connect("./15-Bd/martial.db")
cursor=con.cursor()
#creation de la table
cursor.execute("""
    create table if not exists produits (
        id int primary key,
        name varchar(255) not null,
        stock int 
    )
""")

cursor.execute("""create table if not exists persons(
        id int primary key,
        nom varchar(255) not null,
        prenoms varchar(255) not null
    )""")