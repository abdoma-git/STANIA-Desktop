# lister les equipes

from tkinter import *
from sql import liste_match, supprimer_match
from tkinter import ttk


def page_table_matchs():
    fnt_table_match = Tk()
    fnt_table_match.attributes('-fullscreen', True)
    fnt_table_match.title("Table match")
    fnt_table_match.configure(padx=30, pady=120)

    title_label = Label(fnt_table_match, text="Table match", font=("Arial", 30))
    title_label.place(x=40, y=-90)

    table_match = liste_match()

    # creation du tableau tkinter
    tableau_match = ttk.Treeview(fnt_table_match)

    # definition des colones
    tableau_match["columns"] = ("Id", "Equipe 1", "Equipe 2", "Date du match", "Lieu")

    # En-tete du tableau
    tableau_match.heading("Id", text="Id", anchor=CENTER)
    tableau_match.heading("Equipe 1", text="Equipe 1", anchor=CENTER)
    tableau_match.heading("Equipe 2", text="Equipe 2", anchor=CENTER)
    tableau_match.heading("Date du match", text="Date du match", anchor=CENTER)
    tableau_match.heading("Lieu", text="Lieu", anchor=CENTER)

    for i in table_match:  # id    #nom   #prenom #age
        tableau_match.insert(parent="", index="end", values=(i[0], i[1], i[2], i[3], i[4]))

    tableau_match.grid(row=2, column=2)

    def supprimer():
        id = tableau_match.item(tableau_match.selection())['values'][0]
        supprimer_match(id)

    button1 = Button(fnt_table_match, text="Supprimer match", command=supprimer)
    button1.grid(row=3, column=2, pady=20)

    button1 = Button(fnt_table_match, text="Fermer", command=exit)
    button1.grid(row=5, column=2, pady=20)

    fnt_table_match.mainloop()



