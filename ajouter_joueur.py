# ici pour ajouter les equipes
from tkinter import *
from PIL import Image, ImageTk
from sql import inserer_joueur


def joueur():
    equipe_fenetre = Tk()
    equipe_fenetre.attributes('-fullscreen', True)
    equipe_fenetre.title("Ajouter Joueur")
    equipe_fenetre.configure(padx=600, pady=150)


    # titre de la page
    title_label = Label(equipe_fenetre, text="Ajouter un nouveau Joueur", font=("Arial", 30))
    title_label.place(x=-350, y=-140)

    # Creqtion de formulaire de creation du compte
    label_nom = Label(equipe_fenetre, text="Nom:")
    label_nom.grid(row=1, column=1)

    input_nom = Entry(equipe_fenetre)
    input_nom.grid(row=1, column=2)

    label_prenom = Label(equipe_fenetre, text="Prenom:")
    label_prenom.grid(row=2, column=1)

    input_prenom = Entry(equipe_fenetre)
    input_prenom.grid(row=2, column=2, padx=10, pady=10)

    label_numero = Label(equipe_fenetre, text="Numero:")
    label_numero.grid(row=3, column=1)

    input_numero = Entry(equipe_fenetre)
    input_numero.grid(row=3, column=2)

    label_pays = Label(equipe_fenetre, text="Pays:")
    label_pays.grid(row=4, column=1, padx=10, pady=10)

    input_pays = Entry(equipe_fenetre)
    input_pays.grid(row=4, column=2)


    def ajouter_joueur():
        nom = input_nom.get()
        prenom = input_prenom.get()
        numero = input_numero.get()
        pays = input_pays.get()

        inserer_joueur(nom, prenom, numero, pays)



    boutton1 = Button(equipe_fenetre, text="Submit", command=ajouter_joueur)
    boutton1.grid(row=6, column=2, padx=5, pady=5)


    boutton4 = Button(equipe_fenetre, text="Retour", command=exit)
    boutton4.grid(row=8, column=3, padx=5, pady=5)

    equipe_fenetre.mainloop()
