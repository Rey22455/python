def chiffrerVigenere(message,cle):
    indiceCle=0
    mC=""
    for lettre in message:
        lettreAscii=ord(lettre)
        if 97<=lettreAscii<=122:
            cleAscii=ord(cle[indiceCle])
            PLC=((lettreAscii-97)+(cleAscii-97))%26
            lettreC= chr(PLC+97)
            mC+=lettreC
            indiceCle+=1
            if indiceCle==len(cle):
                indiceCle=0
        else:
            mC+=(chr(lettreAscii))
    return(mC)
print(chiffrerVigenere("j'adore ecouter la radio toute la journee","musique"))

def dechiffrerVigenere(message,cle):
    indiceCle=0
    mC=""
    for lettre in message:
        lettreAscii=ord(lettre)
        if 97<=lettreAscii<=122:
            cleAscii=ord(cle[indiceCle])
            PLC=((lettreAscii)-(cleAscii))%26
            lettreC= chr(PLC+97)
            mC+=lettreC
            indiceCle+=1
            if indiceCle==len(cle):
                indiceCle=0
        else:
            mC+=(chr(lettreAscii))
    return(mC)
print(dechiffrerVigenere("v'uvwhy ioimbul pm lslyi xaolm bu naojvuy","musique"))