"""
listeTemp = [10,9,8,7,6,5,4,5,8,11,15,18]
listeHeure = [0,1,2,3,4,5,6,7,8,9,10,11]
print(listeTemp)
#print simplu
print(listeTemp[0])
#prima valoare
print(listeTemp[len(listeTemp)-1])
#ultima valoare mereu
heure = int(input("Saisir une heure :"))
print("A "+str(heure)+" heure, il faisait "+str(listeTemp[heure])+"°.")
"""
"""
listeTemp = [10,9,8,7,6,5,4,5,8,11,15,18]
for i in range(5,len(listeTemp)):
    print("A "+str(i)+" h, la temperature etait de "+str(listeTemp[i])+" °Celsius.")
"""
"""
listeTemp = [10,9,8,7,6,5,4,5,8,11,15,18]
Tmin=Tmax=listeTemp[0]
Hmin=Hmax=0
somme=0
for i in range(1,len(listeTemp)):
    somme=somme+listeTemp[i]
    if listeTemp[i]<Tmin:
        Tmin=listeTemp[i]
        Hmin=i

for i in range(1,len(listeTemp)):
    if listeTemp[i]>Tmax:
        Tmax=listeTemp[i]
        Hmax=i

moyenne= somme/len(listeTemp)

print("Temperature min : "+str(Tmin)+"° "+str(Hmin)+"h")
print("Temperature max : "+str(Tmax)+"° "+str(Hmax)+"h")
print("Moyenne : "+str(moyenne))
"""
"""
listeTemp = [10,9,8,7,6,5,4,5,8,11,15,18]
Tmin=Tmax=listeTemp[0]
Hmin=Hmax=0
somme=0
print(listeTemp)
print("----------------------------------------------")
listeTemp.append(20)
print(listeTemp)
listeTemp[6] = 2
print("----------------------------------------------")
print(listeTemp)
print("----------------------------------------------")
listeTemp.sorted(listeTemp)
print(listeTemp)
print("----------------------------------------------")
"""

