
choix=0
budget=0

while budget <=0:
    try:
        budget=int(input("Entrer votre budget: ")) 
    except ValueError:
        print("\n*****Veillez enter un budget valide****\n")
        
     
while choix != 4:
    print("-----MENU----")
    print("1-Eau 500fcs")
    print("2-Jus 1000fcs")
    print("3-Soda 500fcs")
    print("4-Quitter")
    
    try:
        choix=int(input("Faites un choix : "))
    except ValueError:
        print("\n*****Veillez enter un nombre en fonction du menu*****\n")
        
    if choix ==1:
        if budget>=500 :
            print("vous avez acheté de l'eau")
            budget-=500
        else:
            print("vous n'avez pas assez d'argent")

    elif choix ==2:
        if budget>=1000 :
            print("vous avez acheté le jus")
            budget-=500
        else:
            print("vous n'avez pas assez d'argent")

    elif choix ==3:
        if budget>=1500 :
            print("vous avez acheté du soda")
            budget-=500
        else:
            print("vous n'avez pas assez d'argent")



