class Etudiant:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age





class CompteBancaire:
    def __init__(self, titulaire, solde=0,items=[]):
        self.titulaire=titulaire
        self.solde=solde
        self.items=items

    def depose (self,montant):
        print(self.solde)
        print(f"vous avez effectué un depot de {montant}")
        print(f"votre solde est de : {self.solde}")

        self.items.append({
            "motant": montant,
            "soldeActuel": montant+self.solde
        })
        self.solde=montant+self.solde
        

        
    def historique(self):
        print("\n***HISTORIQUE DE DEPOT***\n")
        datas=self.items
        for el in datas:
            print(el)
       



client1=CompteBancaire(True)
client1.depose(2000)
client1.depose(2000)
client1.depose(1000)
client1.historique()

