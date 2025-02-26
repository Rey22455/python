"""
def volume(h,l,p)->int:
    v=h*l*p
    return v
resultat= volume(2,4,3)
print(resultat)
"""
"""
def vitesse(distance:float,temp:float)->float:
    if temp!=0:
        v=distance/temp
    else:
        v=None
    return v
v= vitesse(100,0)
print(v)
"""
"""
def facture(Nnuits:int,Nrepas:int)->float:
    montant=Nnuits*55+Nrepas*18
    return montant
m=facture(6,9)
print(m,"$")
"""

def paire(nombre:int)->bool:
    if nombre%2==0:
        return True
    else :
        return False 
