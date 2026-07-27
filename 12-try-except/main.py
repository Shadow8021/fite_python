
b=20
try:
    user =int(input("veuillez entrez un nombre:"))
    c=b/user
    print(f"Le resultat est : {c}")
except ZeroDivisionError as Err:
    print(Err)
except ValueError as Err:
    print(Err)