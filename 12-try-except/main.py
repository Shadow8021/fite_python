user =int(input("veuillez entrez un nombre:"))
b=20
try:
    c=b/user
    print(f"Le resultat est : {c}")
except ZeroDivisionError as Err:
    print(Err)