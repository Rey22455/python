from tkinter import *

Mafenetre=Tk()
Mafenetre.title("Mini-Projet")
Mafenetre.geometry("400x300+200+200")


def fenetreSuivante():
 
 Fenetre2 = Tk()
 Fenetre2.geometry("400x300+200+200")
 labelsuite = Label(Fenetre2 , text="Votre nombre genere : ",fg="black")
 labelsuite.pack()
 Buttontquit1 = Button(Fenetre2, text="QUITER", fg="white", bg="red", command=Fenetre2.destroy)
 Buttontquit1.place(x=350,y=0)
 Fenetre2.mainloop()




avant= "Generer un nombre aleatoire"
apres= "Nombre aleatoire : "

Label1 = Label(Mafenetre, text=avant, fg="black")
Label1.pack()
Label2 = Label(Mafenetre, text=apres, fg="black")
Label2.pack()
Button2 = Button(Mafenetre, text="GENERER", fg="white", bg="green", command=fenetreSuivante)
Button2.pack()
Button1 = Button(Mafenetre, text="QUITER", fg="white", bg="red", command=Mafenetre.destroy)
Button1.place(x=350,y=0)

Mafenetre.mainloop()





