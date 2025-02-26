#exerciec boucle
"""
n = int(input("saisir un nb : "))
for i in range(1,11):
    print(str(i)+"*"+ str(n)+" = "+str(i*n))
"""
""" 
n = int(input("saisir un nb : "))
somme=0
for i in range(1,n+1):
    somme = somme + i 
             # 0  + 1 = 1 
    # 1   =    1  + 1 = 2 
    # 2   =    2  + 1 = 3    
"""      
#saisie de a et n
a = int(input("saisir a :"))
n = int(input("saisir n :"))
puissance = 1
for i in range(0,n):#on passe n fois dans la 
    puissance = puissance*a
print(puissance)