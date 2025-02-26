"""
dicoAmis=dict(Iliade = 'Homere' , Odyssee = 'Homere' , Eneide = 'Virgile' , Mahabharata = 'Vyasa')
dicoAmis["Ramayana"]='Valmiki' 
del dicoAmis["Eneide"] 

print(dicoAmis)
"""
import csv
def creationPaysFromCSV(nomDeFichier:str)->list:
    liste=[]
    with open(nomDeFichier, newline='',mode='r',encoding='utf-8') as fichierCsv : #ouverture
        lecture = csv.reader(fichierCsv,dialect=csv.excel_tab)
        #création d'un lecteur de fichier
        for ligne in lecture :
        #pour chaque ligne lue, on a le nom et la population du pays
            val=ligne[0]#ligne[0] correspond au nom du pays
            liste.append(val) #ajout de la valeur dans la liste
    fichierCsv.close()#fermeture du fichier même si cela n'est pas nécessaire
    return liste
def creationPopulationFromCSV(nomDeFichier:str) -> list:
    liste=[]
    with open(nomDeFichier, newline='',mode='r') as fichierCsv :
        lecture = csv.reader(fichierCsv,dialect=csv.excel_tab)
        for ligne in lecture :
            val=int(ligne[1])#ligne[1] correspond à la population du pays
            liste.append(val)
    fichierCsv.close()
    return liste

def populationDe(nom:str, d:dict):
    if nom in d:
        return d[nom]
    else:
        return "Ce pays n'est pas membre de l'UE"


def paysPopulationDe(n:int,d:dict):
    for nom,nbH in d.items():
        if nbH == n:
            return nom
    return "pas trouve"

pays=creationPaysFromCSV(nomDeFichier='population_pays_ue.csv') #la liste des noms de pays es

population=creationPopulationFromCSV(nomDeFichier='population_pays_ue.csv') #la liste de la p

dico = dict(zip(pays,population))
dico27=dico.copy()
dico27.pop("Royaume-Uni")
print(paysPopulationDe(602005,dico))
print(paysPopulationDe(10000,dico))

import PIL.Image
img = PIL.Image.open('image2.jpg')
exif_data = img._getexif() #exif-data représente le dictionnaire
img.show() 
