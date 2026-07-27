import csv
with open('11-fichier/main.txt','r') as f:
    contenu = f.readline()
    
for i in contenu:
    print(f"-> {i.strip()}")


with open('11-fichier/main.csv','r') as f:
    contenu = csv.DictReader(f)
    eligible=[
        row for row in contenu if row.get("Bonus Decision")=="Eligible"
    ]

with open('11-fichier/main.csv','w', newline="") as f:
    writer = csv.DictWriter(f,fieldnames=eligible[0].keys)
    writer.writeheader()
    writer.writerows(eligible)