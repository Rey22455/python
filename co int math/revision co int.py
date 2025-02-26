from math import * 
n=1 
nbEssais=0
while n!=0 and nbEssais<5 :
    n = float(input("saisir un nombre :"))
    nbEssais+=1
    if n==0:
        print("nombre nul")
    if n>0:
        print("nombre positif")
        if (n - int(n))==0:
            res=1
            n=int(n)
            for i in range(1,n+1):
                res *= i
        else:
            res = sqrt(2*pi*n)*(n/2.73)**n
        print("resultat : "+str(res))
            
    if n<0:
        print("nombre negatif") 

if nbEssais==5:
    print("Acheter la licence")       