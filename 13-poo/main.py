import datetime

class CompteBancaire:
    def __init__(self, titulaire, solde=0,items=[]):
        self.titulaire=titulaire
        self.solde=solde
        self.items=items

    def depose (self,montant):
        self.solde=montant+self.solde
        print(f"vous avez effectué un depot de {montant}")
        print(f"votre solde est de : {self.solde}")

        self.items.append({
            "type":"DEPOT",
            "motant": montant,
            "soldeActuel": self.solde,
            "Date":datetime.datetime.now()
        })
        
        
    def retrait (self,montant):
        if montant>=self.solde:    
            self.solde=montant-self.solde
            print(f"vous avez effectué un retrait de {montant}")
            print(f"votre solde est de : {self.solde}")
            self.items.append({
                    "type": "RETRAIT",
                    "motant": montant,
                    "soldeActuel": self.solde,
                    "Date":datetime.datetime.now()
                })
        else:
            print("fond insuffisant")
            
            
    
    def historique(self):
        print("\n***HISTORIQUE DE DEPOT***\n")
        datas=self.items
        for el in datas:
            print(el)

    def ConsulterSolde(self):
        print(f"votre solde est de {self.solde}")

       

client1=CompteBancaire(True)
client1.depose(2000)
client1.retrait(2000)
client1.depose(1000)
client1.historique()
client1.ConsulterSolde()






class Person:
    def __init__(self,nom,prenom,age,sexe,email,phone):
        self.nom=nom
        self.age=age
        self.prenom=prenom
        self.sexe=sexe
        self.phone=phone
        self.email=email

    def nom_complet(self):
        name=(f"{self.nom} {self.prenom}")
        return name

    def AfficherIdentite(self):
        print(f"Nom: {self.nom} {self.prenom}")
        print(f"Age: {self.age}")
        print(f"Sexe: {self.sexe}")
        print(f"Contacts: \n\t{self.phone}\n\t{self.email}")



#person1=Person("OYAGA","Martial",18,"M","greoyaga@gmail.com","068704756")
#person1.nom_complet()
#person1.AfficherIdentite()