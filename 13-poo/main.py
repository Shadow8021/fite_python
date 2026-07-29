
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
            "soldeActuel": self.solde
        })
        
        
    def retrait (self,montant):
        if montant>self.solde:    
            self.solde=montant-self.solde
            print(f"vous avez effectué un retrait de {montant}")
            print(f"votre solde est de : {self.solde}")
            self.items.append({
                    "type": "RETRAIT",
                    "motant": montant,
                    "soldeActuel": self.solde
                })
        else:
            print("fond insuffisant")
            
                
    def historique(self):
        print("\n***HISTORIQUE DE DEPOT***\n")
        datas=self.items
        for el in datas:
            print(el)
       

client1=CompteBancaire(True)
client1.depose(2000)
client1.retrait(2000)


