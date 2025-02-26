choix = int(input("saisir votre choix "))
#calcul pour le carre
from math import pi 
if choix == 1:
    cote = float(input("quel est le cote du carre "))
    perimetre = 4*cote
    surface = cote * cote 
    print("le perimetre est " + str(perimetre))
    print("la surface est " + str(surface))  
elif choix == 2: 
    rayon = float(input("saisir le rayon"))
    perimetre = 2 * rayon * pi 
    surface = rayon*rayon*pi 
    print("perimetre: "+str(perimetre))
    print("surface: "+str(surface))
else:
    print("mauvais choix")
