from tkinter.filedialog import *
import sqlite3

############################################################################################################
# Importation des dossier Classes

from Classes.Frame import Frame
from Classes.Frame import Frame_login

############################################################################################################


# Création de la base de données
with sqlite3.connect('Bdd/quit.db') as db:
    c = db.cursor() # Création d'un curseur pour exécuter des requêtes SQL

# Création des tables si elles n'existent pas
# Table entreprise
c.execute('CREATE TABLE IF NOT EXISTS entreprise (id INTEGER PRIMARY KEY, nom TEXT NOT NULL, '
          'adresse TEXT NOT NULL, email TEXT NOT NULL, telephone TEXT NOT NULL);')

# Table personne
c.execute('CREATE TABLE IF NOT EXISTS personne (id INTEGER PRIMARY KEY, nom TEXT NOT NULL, '
          'prenom TEXT NOT NULL, telephone TEXT NOT NULL, email TEXT NOT NULL);')

# Table clients
c.execute('CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, nom TEXT NOT NULL, '
          'prenom TEXT NOT NULL, telephone TEXT NOT NULL, email TEXT NOT NULL, adresse TEXT NOT NULL, '
          'commentaire TEXT NOT NULL, personne_id INTEGER, UNIQUE(nom, prenom, telephone, email, adresse), '
          'FOREIGN KEY(personne_id) REFERENCES personne(id));')

# Table employes
c.execute('CREATE TABLE IF NOT EXISTS employes (id INTEGER PRIMARY KEY, nom TEXT NOT NULL, '
          'prenom TEXT NOT NULL, telephone TEXT NOT NULL, email TEXT NOT NULL, personne_id INTEGER, '
          'UNIQUE(nom, prenom, telephone, email), FOREIGN KEY(personne_id) REFERENCES personne(id));')

# Table user
c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL, password TEXT NOT NULL, '
          'personne_id INTEGER, admin INTEGER, FOREIGN KEY(personne_id) REFERENCES personne(id));')

# Table devis
c.execute('CREATE TABLE IF NOT EXISTS devis (id INTEGER PRIMARY KEY, nom_devis TEXT NOT NULL, '
          'nom_entreprise TEXT NOT NULL, email_entreprise TEXT NOT NULL, adresse_entreprise TEXT NOT NULL, '
          'telephone_entreprise TEXT NOT NULL, nom_client TEXT NOT NULL, email_client TEXT NOT NULL, '
          'adresse_client TEXT NOT NULL, telephone_client TEXT NOT NULL, numero_devis TEXT NOT NULL UNIQUE, '
          'date TEXT NOT NULL, description TEXT NOT NULL, prix_unitaire TEXT NOT NULL, '
          'quantite TEXT NOT NULL, montant TEXT NOT NULL, sous_total TEXT NOT NULL, tva TEXT NOT NULL, '
          'total TEXT NOT NULL, id_client INTEGER, valide INTEGER DEFAULT 0, send INTEGER DEFAULT 0, '
          'FOREIGN KEY(id_client) REFERENCES clients(id), '
          'FOREIGN KEY(nom_entreprise) REFERENCES entreprise(nom));')

# Table factures
c.execute('CREATE TABLE IF NOT EXISTS factures (id INTEGER PRIMARY KEY, nom_facture TEXT NOT NULL, '
          'nom_entreprise TEXT NOT NULL, email_entreprise TEXT NOT NULL, adresse_entreprise TEXT NOT NULL, '
          'telephone_entreprise TEXT NOT NULL, nom_client TEXT NOT NULL, email_client TEXT NOT NULL, '
          'adresse_client TEXT NOT NULL, telephone_client TEXT NOT NULL, numero_facture TEXT NOT NULL UNIQUE, '
          'date TEXT NOT NULL, conditions TEXT NOT NULL, description TEXT NOT NULL, prix_unitaire TEXT NOT NULL, '
          'quantite TEXT NOT NULL, montant TEXT NOT NULL, sous_total TEXT NOT NULL, tva TEXT NOT NULL, '
          'total TEXT NOT NULL, solde_du TEXT NOT NULL, id_client INTEGER, payed INTEGER DEFAULT 0, send INTEGER DEFAULT 0, '
          'FOREIGN KEY(id_client) REFERENCES clients(id), '
          'FOREIGN KEY(nom_entreprise) REFERENCES entreprise(nom));')

# Table logo
c.execute('CREATE TABLE IF NOT EXISTS logo (id INTEGER PRIMARY KEY, logo BLOB);')
db.commit() # Enregistrement des modifications

c.execute('SELECT * FROM user')  # Requête pour sélectionner tous les utilisateurs
if not c.fetchall():    # Si la table user est vide
    # Requête pour insérer des valeurs dans une table
    c.execute('INSERT INTO personne(nom, prenom, telephone, email) VALUES("admin", "admin", "admin", "admin")')     # Insertion des valeurs dans la table personne
    db.commit()
    c.execute('INSERT INTO user(username, password, personne_id, admin) VALUES("admin", "admin", 1, 1)')    # Insertion d'un compte administrateur
    db.commit()
    c.execute('INSERT INTO personne(nom, prenom, telephone, email) VALUES("user", "user", "user", "user")')    # Insertion des valeurs dans la table personne
    db.commit()
    c.execute('INSERT INTO user(username, password, personne_id, admin) VALUES("user", "user", 2, 0)')  # Insertion d'un compte utilisateur
    db.commit()
    c.execute('INSERT INTO entreprise(nom, adresse, email, telephone) VALUES("Umbrella Corporation", "Racoon City, Colorado, USA", "A.Wesker@umbrella.com", "9698990509")') # Insertion d'une entreprise
    db.commit()

c.execute('SELECT * FROM logo')  # Requête pour sélectionner tous les logos
if not c.fetchall():    # Si la table logo est vide
    # Requête pour insérer des valeurs dans une table
    c.execute('INSERT INTO logo(logo) VALUES(NULL)')  
    db.commit()
    
db.close()  # Fermeture de la connexion à la base de données

    

############################################################################################################

if __name__ == "__main__":
    
    root = Frame.Frame()
    login = Frame_login.Frame_login(master=root)
    
    root.mainloop()