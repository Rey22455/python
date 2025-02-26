"""
def cube(nombre:int)->int:
    res = nombre**3
    return res 

nb=10
resultat = cube(nb)
print(resultat)
"""
"""
def saisieNombre()->int:
    nb = int(input("saisir un nombre : "))
    return nb

def calculMaximum(nb1:int, nb2:int)->int:
    if nb1>=nb2:
        maxi = nb1
    else:
        maxi = nb2
    return maxi

def affichageMaximum(maximum:int)->None:
    print("la valeur max est "+str(maximum))
    return None

n1=saisieNombre()
n2=saisieNombre()
valeurMax=calculMaximum(n1,n2)
affichageMaximum(valeurMax)
"""
"""
def saisieResistance()->int:
    res = int(input("saisir une valeur de la resistante en Ohm "))
    return res 

def saisieChoix()->str:
    ch = input("saisir votre choix :")
    return ch 

def calculResEqui(R1:int, R2:int, choice:str):
    if choice=="serie":
        Req = R1+R2
    if choice=="parallele":
        Req = 1/R1+1/R2 
        Req = 1/Req 
    else:
        Req=-1
    return Req

def affichage(R1:int,R2:int,Req:float,choice:str)->None:
    print("La résistance équivalente de R1 ("+str(R1)+" Ohms")??????????

res1=saisieResistance()
res2=saisieResistance()
choix=saisieChoix()
resEqui=calculResEqui(res1,res2,choix)
affichage(res1,res2,resEqui,choix)
"""

