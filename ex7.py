note1 = float(input("saisir note1: "))

note2 = float(input("saisir note2: "))

note3 = float(input("saisir note3: "))

note4 = float(input("saisir note4: "))



if note1>=note2 :
    maximum = note1 
else: 
    maximum = note2 
if note3>maximum:
    maximum=note3
if note4>maximum:
    maximum=note4

print("max: "+str(maximum)) 


noteEXAM = float(input("saisir note EXAM: "))

moyenne = (noteEXAM+maximum)/2

print("moyenne: "+str(moyenne))
if moyenne>=10:
    print("ADMIS")
elif moyenne<8:
    print("REFUSE")
else:
    print("CONTROLE COMPLEMENTAIRE")        






