import sqlite3
from Classes.DAO.Dao_personne import Dao_personne

class Dao_employe:
    '''
    Classe pour la gestion des employés dans la base de données
    '''
    @staticmethod
    def get(nom, prenom):
        '''
        Méthode pour récupérer un employé de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM employes WHERE nom = ? AND prenom = ?', (nom, prenom,))
            result = c.fetchall()
            return None if len(result) == 0 else result

    @staticmethod
    def save(employe):
        '''
        Méthode pour enregistrer les informations de l'employé dans la base de données
        '''
        Dao_personne.save(employe)
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute("INSERT INTO employes(nom, prenom, telephone, email) VALUES(?, ?, ?, ?)", (employe.nom, employe.prenom, employe.telephone, employe.email))
            db.commit()

    @staticmethod
    def all():
        '''
        Méthode pour récupérer tous les employés de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM employes')
            return c.fetchall()

    @staticmethod
    def delete(nom, prenom):
        '''
        Méthode pour supprimer un employé de la base de données
        '''
        Dao_personne.delete(nom, prenom)
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('DELETE FROM employes WHERE nom = ? AND prenom = ?', (nom, prenom,))
            db.commit()