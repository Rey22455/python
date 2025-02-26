from tkinter import *

avant = "Mario: 100 PV et Adresse: 50"
apres = "Mario: 125 PV et Adresse: 50"

Mafenetre=Tk()
Mafenetre.title("MON IHM")
Mafenetre.geometry("400x150+400+400")
Label1 = Label(Mafenetre, text=avant, fg="red", bg="black")
Label1.pack()
Label2 = Label(Mafenetre, text=apres, fg="red", bg="black")
Label2.pack()
Button1 = Button(Mafenetre, text="quiter", fg="green", bg="yellow", command=Mafenetre.destroy)
Button1.pack()




Mafenetre.mainloop()