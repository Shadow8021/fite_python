import sqlite3

#provider
con=sqlite3.connect("./15-Bd/martial.db")
cursor=con.cursor()
#creation de la table
#creation de plusieurs tables au meme moment
cursor.executescript("""
    create table if not exists produits (
            id int primary key,
            nom varchar(255) not null,
            prix real
            stock int );

    create table if not exists persons(
        id int primary key,
        nom varchar(255) not null,
        prenoms varchar(255) not null,
        prone integer not null
    )



""")

con.commit()