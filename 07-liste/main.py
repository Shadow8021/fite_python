#creation d'une liste
list_eleves=["Alice", "Bob", "Charlie", "David", "Eva"]
#affichage de la liste
print(list_eleves)

#afficher un élement en fonction de son index
print(list_eleves[0]) #Alice
print(list_eleves[1]) #Bob
print(list_eleves[2]) #Charlie
print(list_eleves[3]) #David
print(list_eleves[4]) #Eva

#afficher un élement en fonction de son index negatif
print(list_eleves[-5]) #Alice
print(list_eleves[-4]) #Bob
print(list_eleves[-3]) #Charlie
print(list_eleves[-2]) #David
print(list_eleves[-1]) #Eva

###methode d'une liste

print(len(list_eleves)) #len permet de compter le nombre d'element de la liste

    #slicing 
print(list_eleves[1:4]) #affiche les elements d'index 1, 2 et 3
print(list_eleves[:3]) #affiche les elements d'index 0, 1 et 2
print(list_eleves[2:5]) #affiche les elements d'index 2, 3 et 4
print(list_eleves[1:5:2]) #affiche les elements d'index 1, 3 et 5
print(list_eleves[::2]) #saut de deux en deux
print(list_eleves[::3]) #saut de trois en trois
print(list_eleves[::4]) #saut de quatre en quatre
