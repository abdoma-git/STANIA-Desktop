
import sqlite3

connection = sqlite3.connect("STANIA.db")

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT,nom VARCHAR(20),prenom VARCHAR(20), tel VARCHAR(12), mail VARCHAR(30),mdp VARCHAR(20))")
cursor.execute("CREATE TABLE IF NOT EXISTS equipes(id INTEGER PRIMARY KEY AUTOINCREMENT,nom VARCHAR(20), pays VARCHAR(20), joueur1 INTEGER, joueur2 INTEGER, joueur3 INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS joueurs(id INTEGER PRIMARY KEY AUTOINCREMENT,nom VARCHAR(20), prenom VARCHAR(20), numero INTEGER, pays VARCHAR(20))")

def inserer_user(*args):
    cursor.execute(" INSERT INTO users(nom, prenom, tel, mail, mdp) VALUES ( ?, ?, ?, ?, ?) ", args)
    connection.commit()

def inserer_equipe(*args):
    cursor.execute(" INSERT INTO equipes(nom, pays, joueur1, joueur2, joueur3) VALUES ( ?, ?, ?, ?, ?) ", args)
    connection.commit()

def inserer_joueur(*args):
    cursor.execute(" INSERT INTO joueurs(nom, prenom, numero, pays) VALUES ( ?, ?, ?, ?) ", args)
    connection.commit()

def liste_users():
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

def liste_equipe():
    cursor.execute("SELECT * FROM equipes")
    return cursor.fetchall()


def liste_joueur():
    cursor.execute("SELECT * FROM joueurs")
    return cursor.fetchall()

