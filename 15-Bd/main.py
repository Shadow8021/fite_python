import sqlite3



produits=[(1,"pantalon",1000,10),
          (2,"chemise",2000,20),
          (3,"chaussure",3000,30),
          (4,"t-shirt",4000,40),
          (5,"pull",5000,50),
          (6,"sac",6000,60),
          (7,"ceinture",7000,70),
          (8,"bonnet",8000,80),
          (9,"gants",9000,90),
          (10,"lunette",10000,100)
          ]
clients=[(1,"DIOP","Mamadou",776543210),
         (2,"DIOP","Moussa",776543211),
         (3,"DIOP","Mouhamed",776543212),
         (4,"DIOP","Moussa",776543213),
         (5,"DIOP","Mouhamed",776543214),
         (6,"DIOP","Moussa",776543215),
         (7,"DIOP","Mouhamed",776543216),
         (8,"DIOP","Moussa",776543217),
         (9,"DIOP","Mouhamed",776543218),
         (10,"DIOP","Moussa",776543219)
         ]

#provider
con=sqlite3.connect("./15-Bd/martial.db")
cursor=con.cursor()
#creation de la table
#creation de plusieurs tables au meme moment
cursor.executescript("""
    create table if not exists produits (
            id int primary key,
            nom varchar(255) not null,
            prix real,
            stock int );

    create table if not exists persons(
        id int primary key,
        nom varchar(255) not null,
        prenoms varchar(255) not null,
        phone integer not null
    )
""")
con.commit()
#cursor.executemany("insert into produits values(?,?,?,?)",produits)
#cursor.executemany("insert into persons values(?,?,?,?)",clients)
con.commit()
tax=0.2
#nouveau prix de chaque produit
for produit in produits:
    cursor.execute("update produits set prix=prix+(prix*?) where id=?", (tax, produit[0]))
con.commit()