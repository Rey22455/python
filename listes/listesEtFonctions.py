"""
from random import randint

def creationAleatoire(nombre:int)->list:
    liste=[]
    for i in range (nombre):
        liste.append(randint(0,20))
    return liste

def affichage(liste:list)->None:
    for i in range (len(liste)):
        print(liste[i])
    return None
listeA = creationAleatoire(20)

affichage(listeA)
"""
"""
import csv
def creationFromCSV(relevesTemp_26_4:str)->list:
    lst=[]
    fichier = open(relevesTemp_26_4,"r")
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        val=float(ligne[1])
        lst.append(val)
    fichier.close()
    return lst

liste = creationFromCSV("relevesTemp_26_4.csv")
somme=0
for i in range(len(liste)):
    print(liste[i])
    somme+=liste[i]
moyenne=somme/len(liste)
print("moyenne : "+str(moyenne))
"""
"""
import csv
def creationFromCSV(Films:str)->list:
    lst=[]
    fichier = open(Films,"r")                          #ouverture du fichier en lecture
    lecteur = csv.reader(fichier)                      #creation d'un lecteur de fichier csv
    for ligne in lecteur:                              #pour chaque ligne lue, on a l'indice et la valeur
        titre=ligne[0]                                 #ligne 0 film ligne 1 genre ligne 2 audiance
        genre=ligne[1]                                 #ajout de la valeur dans la liste
        nbEntree=int(ligne[2])                         #fermeture du fichier
        lst.append((titre,genre,nbEntree))
    fichier.close()
    return lst

def moyenne(listef:list)->list:
    somme=0
    compteurDeFilm=0
    for i in range(len(listef)):
        if listef[i][1]=="Science-Fiction":
         somme+= listef[i][2]   
         compteurDeFilm+=1                    #somme des entrees/de science fiction
    resultat = somme/compteurDeFilm                  #calcul de la moyenne
    return resultat

liste = creationFromCSV("Films.csv")
print(moyenne(liste))
"""
import csv 
from tkinter import *

def creationFromCSV(Films:str)->list:
    lst=[]
    fichier = open(Films,"r")                          #ouverture du fichier en lecture
    lecteur = csv.reader(fichier)                      #creation d'un lecteur de fichier csv
    for ligne in lecteur:                              #pour chaque ligne lue, on a l'indice et la valeur
        titre=ligne[0]                                 #ligne 0 film ligne 1 genre ligne 2 audiance
        genre=ligne[1]                                 #ajout de la valeur dans la liste
        nbEntree=ligne[2]                         #fermeture du fichier
        lst.append((titre,genre,nbEntree))
    fichier.close()
    return lst

def creationTexte(liste:list)->str:
   texte=""
   for i in range(len(liste)):
    texte+=liste[i][0]+"\t"+liste[i][1]+"\t"+liste[i][2]+"\n"
    return texte

Mafenetre=Tk()
Mafenetre.title("Films")
Mafenetre.geometry("800x600+200+50")
apres="LISTE"
Label2 = Label(Mafenetre, text=apres, fg="black",)
Label2.pack()
txt = Text(Mafenetre, height=25, width=70)
txt.insert(CURRENT, creationTexte(creationFromCSV("Films.csv")))
txt.pack(padx="15", pady="15")
Button1 = Button(Mafenetre, text="QUITER", fg="white", bg="red", command=Mafenetre.destroy)
Button1.place(x=360,y=450)

Mafenetre.mainloop()

liste = creationFromCSV("Films.csv")
