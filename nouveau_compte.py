
from tkinter import *
from PIL import Image, ImageTk
from login_form import se_connecter
from sql import inserer_user


def new_user():

    nom = input_nom.get()
    prenom = input_prenom.get()
    tel = input_tel.get()
    mail = input_mail.get()
    mdp = input_mdp.get()

    inserer_user(nom, prenom, tel, mail, mdp)




creer_compte_user = Tk()
creer_compte_user.attributes('-fullscreen', True)
creer_compte_user.title("Nouveau Compte")
creer_compte_user.configure(padx=600, pady=150)


#Image

image = Image.open("images/foot.jpeg")
photo = ImageTk.PhotoImage(image)

# Création d'un widget Label pour afficher l'image
image_label = Label(creer_compte_user, image=photo)
image_label.place(x=-300, y=0) #en html  = margin (x = margin-left et y = margin-top)
#image_label.grid(row=2, column=0)

#titre de la page

title_label = Label(creer_compte_user, text="Creer un Nouveau Compte STANIA", font=("Arial", 30))
title_label.place(x=-350, y=-140)

# Creqtion de formulaire de creation du compte
label_nom = Label(creer_compte_user,text="Nom:")
label_nom.grid(row=1, column=1)

input_nom = Entry(creer_compte_user)
input_nom.grid(row=1, column=2)


label_prenom = Label(creer_compte_user,text="Prenom:")
label_prenom.grid(row=2, column=1)

input_prenom = Entry(creer_compte_user)
input_prenom.grid(row=2, column=2, padx=10, pady=10)

label_tel = Label(creer_compte_user,text="Tel:")
label_tel.grid(row=3, column=1)

input_tel = Entry(creer_compte_user)
input_tel.grid(row=3, column=2)

label_mail = Label(creer_compte_user,text="Email:")
label_mail.grid(row=4, column=1, padx=10, pady=10)

input_mail = Entry(creer_compte_user)
input_mail.grid(row=4, column=2)

label_mdp = Label(creer_compte_user,text="Mote d passe:")
label_mdp.grid(row=5, column=1)

input_mdp = Entry(creer_compte_user)
input_mdp.grid(row=5, column=2)

boutton1 = Button(creer_compte_user, text="Submit", command=new_user)
boutton1.grid(row=6, column=2 , padx=5, pady=5 )

deja_inscrit = Label(creer_compte_user, text="Vous avez deja un compte -----------> ")
deja_inscrit.grid(row=7, column=1, padx=5, pady=5 )


def open_login():
    se_connecter(creer_compte_user)


boutton1 = Button(creer_compte_user, text="Se connecter", command=open_login)
boutton1.grid(row=7, column=2 , padx=5, pady=5)

boutton4 = Button(creer_compte_user, text="Fermer", command=exit)
boutton4.grid(row=8, column=3 , padx=5, pady=5)


creer_compte_user.mainloop()



