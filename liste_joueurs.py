# lister les equipes

from tkinter import *
from sql import liste_joueur, supprimer_joueur
from tkinter import ttk


def page_table_joueurs():
    
    fnt_table_joueur = Tk()
    fnt_table_joueur.attributes('-fullscreen', True)
    fnt_table_joueur.title("Table Joueur")
    fnt_table_joueur.configure(padx=30, pady=120)

    title_label = Label(fnt_table_joueur, text="Table Joueur", font=("Arial", 30))
    title_label.place(x=40, y=-90)

    table_joueur = liste_joueur()

    # creation du tableau tkinter
    tableau_etudiant = ttk.Treeview(fnt_table_joueur)

    # definition des colones
    tableau_etudiant["columns"] = ("Id", "Nom", "Prenom", "Numero", "Pays")

    # En-tete du tableau
    tableau_etudiant.heading("Id", text="Id", anchor=CENTER)
    tableau_etudiant.heading("Nom", text="Nom", anchor=CENTER)
    tableau_etudiant.heading("Prenom", text="Prenom", anchor=CENTER)
    tableau_etudiant.heading("Numero", text="Numero", anchor=CENTER)
    tableau_etudiant.heading("Pays", text="Pays", anchor=CENTER)


    for i in table_joueur:  # id    #nom   #prenom #age
        tableau_etudiant.insert(parent="", index="end", values=(i[0], i[1], i[2], i[3], i[4]))

    tableau_etudiant.grid(row=2, column=2)

    def supprimer():
        id = tableau_etudiant.item(tableau_etudiant.selection())['values'][0]
        supprimer_joueur(id)


    button1 = Button(fnt_table_joueur, text="Supprimer joueur", command=supprimer)
    button1.grid(row=3, column=2, pady=20)


    button1 = Button(fnt_table_joueur, text="Fermer", command=exit)
    button1.grid(row=5, column=2, pady=20)


    fnt_table_joueur.mainloop()



