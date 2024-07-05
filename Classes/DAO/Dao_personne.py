import sqlite3
from Classes.Metiers.Personne import Personne

class Dao_personne:
    '''
    Classe pour la gestion des personnes dans la base de données
    '''
    @staticmethod
    def save(personne):
        '''
        Méthode pour enregistrer les informations de la personne dans la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute("INSERT INTO personne(nom, prenom, telephone, email) VALUES(?, ?, ?, ?)", (personne.nom, personne.prenom, personne.telephone, personne.email))
            db.commit()

    @staticmethod
    def all():
        '''
        Méthode pour récupérer toutes les personnes de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM personne')
            return c.fetchall()

    @staticmethod
    def delete(nom, prenom):
        '''
        Méthode pour supprimer une personne de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('DELETE FROM personne WHERE nom = ? AND prenom = ?', (nom, prenom,))
            db.commit()

    @staticmethod
    def delete_last_created():
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            # Supprime la derniere personne créé avec le même nom et prénom
            c.execute('DELETE FROM personne WHERE id = (SELECT MAX(id) FROM personne)')
            db.commit()