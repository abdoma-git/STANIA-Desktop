# ici pour ajouter les equipes
from tkinter import *
from PIL import Image, ImageTk
from sql import inserer_match
from liste_matchs import page_table_matchs



def match():
    match_fenetre = Tk()
    match_fenetre.attributes('-fullscreen', True)
    match_fenetre.title("Ajouter match")
    match_fenetre.configure(padx=600, pady=150)


    # titre de la page
    title_label = Label(match_fenetre, text="Ajouter un nouveau match", font=("Arial", 30))
    title_label.place(x=-350, y=-140)

    # Creqtion de formulaire de creation du compte
    label_nom = Label(match_fenetre, text="Nom de l'equipe 1:")
    label_nom.grid(row=1, column=1)

    input_nom = Entry(match_fenetre)
    input_nom.grid(row=1, column=2)

    label_prenom = Label(match_fenetre, text="Nom de l'equipe 1::")
    label_prenom.grid(row=2, column=1)

    input_prenom = Entry(match_fenetre)
    input_prenom.grid(row=2, column=2, padx=10, pady=10)

    label_numero = Label(match_fenetre, text="Date du Match:")
    label_numero.grid(row=3, column=1)

    input_numero = Entry(match_fenetre)
    input_numero.grid(row=3, column=2)

    label_pays = Label(match_fenetre, text="Lieu du Match:")
    label_pays.grid(row=4, column=1, padx=10, pady=10)

    input_pays = Entry(match_fenetre)
    input_pays.grid(row=4, column=2)


    def ajouter_match():
        equipe1 = input_nom.get()
        equipe2 = input_prenom.get()
        date = input_numero.get()
        lieu = input_pays.get()

        inserer_match(equipe1, equipe2, date, lieu)


    boutton1 = Button(match_fenetre, text="Submit", command=ajouter_match)
    boutton1.grid(row=6, column=2, padx=5, pady=5)

    boutton2 = Button(match_fenetre, text="Les Matchs", command=page_table_matchs)
    boutton2.grid(row=7, column=2, padx=5, pady=5)


    boutton4 = Button(match_fenetre, text="Retour", command=exit)
    boutton4.grid(row=8, column=3, padx=5, pady=35)

    match_fenetre.mainloop()


