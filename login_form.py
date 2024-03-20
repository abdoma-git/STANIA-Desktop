from tkinter import *
from PIL import Image, ImageTk
from sql import liste_users
from dashboard import open_dashboard


def se_connecter(fenetre):

    fenetre.destroy()

    login_fenetre = Tk()

    login_fenetre.attributes('-fullscreen', True) #plein ecran
    login_fenetre.title("Se Connecter")
    login_fenetre.configure(padx=600, pady=150)


    # titre de la page

    title_label = Label(login_fenetre, text="Se connecter Compte STANIA", font=("Arial", 30))
    title_label.place(x=-350, y=-140)

    # Creqtion de formulaire de creation du compte
    label_mail = Label(login_fenetre, text="Email:")
    label_mail.grid(row=1, column=1)

    input_mail = Entry(login_fenetre)
    input_mail.grid(row=1, column=2)

    label_mdp = Label(login_fenetre, text="Mot de passe:")
    label_mdp.grid(row=2, column=1)

    input_mdp = Entry(login_fenetre)
    input_mdp.grid(row=2, column=2, padx=10, pady=10)

    def login():
        liste = liste_users()
        mail = input_mail.get()
        mdp = input_mdp.get()

        for user in liste:
            if ( user[4] == mail and user[5] == mdp ):
                return open_dashboard(login_fenetre)
            else:
                label_info = Label(login_fenetre, text="Utilisateur n'existe pas !!")
                label_info.grid(row=5, column=2)

    boutton1 = Button(login_fenetre, text="Se Connecter", command=login)
    boutton1.grid(row=3, column=2, padx=5, pady=5)



    boutton4 = Button(login_fenetre, text="Fermer", command=exit)
    boutton4.grid(row=4, column=2, padx=5, pady=5)

    login_fenetre.mainloop()