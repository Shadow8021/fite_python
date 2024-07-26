user =int(input("veuillez entrez un nombre:"))
b=20
if user:
    raise ValueError
print("fin")
try:
    c=b/user
    print(f"Le resultat est : {c}")
except ZeroDivisionError as Err:
    print(Err)
except ValueError as Err:
    print(Err)

