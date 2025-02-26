"""
a = int(input("saisir a :"))
n = int(input("saisir n :"))

nb=99
nb=a*n
while nb >=1:
    print(nb)
    nb-=2  
"""
#ex 1
"""
a = int(input("saisir a :"))
n = int(input("saisir n :"))
puissance = 1 
i=1
while i!=(n+1):
    puissance *= a
    i+=1
    print(puissance)
"""
#ex 2
"""
somme = 0 
note = 0
nbNotes=0
while note != -1:
    note = int(input("saisir une note :"))
    if note != -1: 
          somme += note 
          nbNotes += 1
moyenne = somme/nbNotes
print(moyenne) 
"""
#ex 3
"""
from math import sqrt
nombre=1
while nombre != 0:
    nombre = int(input("saisir un nombre :"))
    if nombre >0: 
        resultat = sqrt(nombre)
        print(resultat)
    if nombre <0:
        print("bombre <0 interdir") 
"""
#ex 4
from random import *
nbMystere = randint (0,100)
while 
