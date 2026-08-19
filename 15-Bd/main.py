import sqlite3

#provider
con=sqlite3.connect("martial.db")
cursor=con.cursor()
cursor.execute("""
    create ta
""")