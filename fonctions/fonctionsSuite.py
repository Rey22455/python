
def afficherCodeAscii(lettre:chr)->None:
    codeAscii = ord(lettre)
    print(codeAscii)

def afficherCodeAsciiHexa(lettre:chr)->None:
    codeAscii = ord(lettre)
    codeAsciiHexa = hex(codeAscii)
    print(codeAsciiHexa)

def afficherLettre(codeAscii : int)->None:
    lettre = chr(codeAscii)
    print(lettre)


def crypterLettre(lettre:chr,cle)->chr:
    codeAscii = ord(lettre)
    codeAsciiCrypte = codeAscii+cle
    lettreCrypte = chr(codeAsciiCrypte)
    return lettreCrypte

def decrypterLettre(lettre:chr,cle)->chr:
    codeAscii = ord(lettre)
    codeAsciideCrypte = codeAscii-cle
    lettredeCrypte = chr(codeAsciideCrypte)
    return lettredeCrypte
"""
+1
-1
myster = decrypterLettre('a')
print(myster)
"""
def crypterPhrase(phrase:str)->str:
    phraseC = ""
    for i in range(len(phrase)):
        lettre = phrase[i]
        lettreC = crypterLettre(lettre)
        phraseC+=lettreC
    return phraseC
def decrypterPhrase(phraseC:str)->str:
    phraseD = ""
    for i in range(len(phraseC)):
        lettre = phraseC[i]
        lettreD = decrypterLettre(lettre)
        phraseD+=lettreD
    return phraseD
"""
print(decrypterPhrase("Wjwfnfou!mb!qbvtf"))
"""
def crypterPhrase(phrase:str,cle:int)->str:
    phraseC = ""
    for i in range(len(phrase)):
        lettre = phrase[i]
        lettreC = crypterLettre(lettre,cle)
        phraseC+=lettreC
    return phraseC

def decrypterPhrase(phraseC:str,cle)->str:
    phraseD = ""
    for i in range(len(phraseC)):
        lettre = phraseC[i]
        lettreD = decrypterLettre(lettre,cle)
        phraseD+=lettreD
    return phraseD
mystere = crypterPhrase("phrase mystere",5)
resultat = decrypterPhrase(mystere,5)
print(resultat)