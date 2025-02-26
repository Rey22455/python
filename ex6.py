nb1 = float(input("saisir un nombre: "))

nb2 = float(input("saisir un nombre: "))

nb3 = float(input("saisir un nombre: "))

nb4 = float(input("saisir un nombre: "))

if nb1>=nb2 :
    maximum = nb1 
else: 
    maximum = nb2 
if nb3>maximum:
    maximum=nb3
if nb4>maximum:
    maximum=nb4
print("max: "+str(maximum))            