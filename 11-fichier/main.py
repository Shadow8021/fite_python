with open('11-fichier/main.txt','r') as f:
    contenu = f.readline()
    
for i in contenu:
    print(f"-> {i.strip()}")