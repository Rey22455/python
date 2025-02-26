"""
def saisir(): #renvoie un tuple PR(reel) PI(imaginaire)
    
    ch = input("Saisir votre nombre complexe :")
    indiceSigne = ch.rfind("+")
    if indiceSigne == -1: # PI est negative 
        indiceSigne = ch.rfind("-")
    pr = float(ch[:indiceSigne])
    pi = float(ch[indiceSigne:-1])
    return (pr,pi)

nbComplexe = saisir()
print(nbComplexe[0]) #partie reele
print(nbComplexe[1]) #partie imaginaire

def affichage(nbrComplexe):
    if nbrComplexe[1]>=0: #partie imaginaire >0
        print(str(nbrComplexe[0])+"+"+str(nbrComplexe[1])+"j")
    else:
        print(str(nbrComplexe[0])+str(nbrComplexe[1])+"j")


def addition(nbrComplexe1,nbrComplexe2):
    partieIm=nbrComplexe1[1]+nbrComplexe2[1]
    partieRe=nbrComplexe1[0]+nbrComplexe2[0]
    return partieRe,partieIm



def soustraction(nbrComplexe1,nbrComplexe2):
    partieIm=nbrComplexe1[1]-nbrComplexe2[1]
    partieRe=nbrComplexe1[0]-nbrComplexe2[0]
    return partieRe,partieIm

nb1 = saisir()
nb2 = saisir()
nbR = soustraction(nb1,nb2)
affichage(nbR)

def multiplication(nbrComplexe1,nbrComplexe2):
    (nbrComplexe1[0]*nbrComplexe2[1]-nbrComplexe1[1]*nbrComplexe2[1],
     nbrComplexe1[0]*nbrComplexe2[1]+nbrComplexe1[1]*nbrComplexe2[0])
    return 
"""
from math import sqrt,atan
def affichageTg (nc):
    module= sqrt(nc[0]**2+nc[1]**2)
    argument=atan(nc[1]/nc[0])
    print()



def mul (nc1,nc2):
    pr=nc1[0]*nc2[0]-nc1[1]*nc2[1]
    pi=nc1[0]*nc2[1]+nc1[1]*nc2[0]
    return(pr,pi)
print (mul((5,2),(3,4)))

def division (nc1,nc2):
    divisieur=nc2[0]**2+nc2[1]**2
    if divisieur!=0:
        pr=(nc1[0]*nc2[0]+nc1[1]*nc2[1])/divisieur
        pi=(nc1[1]*nc2[0]-nc1[0]*nc2[1])/divisieur
        return(pr,pi)
    else:
        return None
print (division((5,2),(3,4)))
    
    



    