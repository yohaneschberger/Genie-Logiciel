import sqlite3
from Classes.DAO.Dao_personne import Dao_personne

class Dao_client:
    '''
    Classe pour la gestion des clients dans la base de données
    '''
    @staticmethod
    def get(nom, prenom):
        '''
        Méthode pour récupérer un client de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM clients WHERE nom = ? AND prenom = ?', (nom, prenom,))
            result = c.fetchall()
            return None if len(result) == 0 else result
        
    @staticmethod
    def get_nom_prenom(id):
        '''
        Méthode pour récupérer le nom et le prénom d'un client de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT nom, prenom FROM clients WHERE id = ?', (id,))
            result = c.fetchall()
            return None if len(result) == 0 else result[0]
        
    @staticmethod
    def get_id(nom, email):
        '''
        Méthode pour récupérer l'identifiant d'un client de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT id FROM clients WHERE nom = ? AND email = ?', (nom, email,))
            result = c.fetchall()
            return None if len(result) == 0 else result[0][0]

    @staticmethod
    def save(client):
        '''
        Méthode pour enregistrer les informations du client dans la base de données
        '''
        existing_client = Dao_client.get(client.nom, client.prenom)
        if existing_client:
            return
        
        Dao_personne.save(client)
        
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute("INSERT INTO clients(nom, prenom, telephone, email, adresse, commentaire) VALUES(?, ?, ?, ?, ?, ?)", (client.nom, client.prenom, client.telephone, client.email, client.adresse, client.commentaire))
            db.commit()

    @staticmethod
    def all():
        '''
        Méthode pour récupérer tous les clients de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM clients')
            return c.fetchall()

    @staticmethod
    def delete(nom, prenom):
        '''
        Méthode pour supprimer un client de la base de données
        '''
        Dao_personne.delete(nom, prenom)
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('DELETE FROM clients WHERE nom = ? AND prenom = ?', (nom, prenom,))
            db.commit()