nblivre = float(input("nombre de livres : "))
prixHT = float(input("prix HT d'un livre : "))

prixTOTALHT = nblivre * prixHT

if prixTOTALHT>=1000:
    prixTOTALHT *= 0.8
if prixTOTALHT>=500 and prixTOTALHT<1000:   
    prixHT *= 0.9

prixTOTALTTC = prixTOTALHT * 1.055


print("Prix total HT : " + str(prixTOTALHT)) 
print("Prix total TTC : " + str(prixTOTALTTC)) 



