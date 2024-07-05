import sqlite3

class Dao_entreprise:
    '''
    Classe qui gère les accès à la base de données pour les entreprises
    '''
    @staticmethod
    def get():
        '''
        Méthode qui récupère toutes les entreprises de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM entreprise')
            return c.fetchall()
        
    @staticmethod
    def change(entreprise):
        '''
        Méthode qui modifie les informations d'une entreprise dans la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('UPDATE entreprise SET nom = ?, telephone = ?, email = ?, adresse = ?, commentaire = ? WHERE id = 1', (entreprise.nom, entreprise.telephone, entreprise.email, entreprise.adresse))
            db.commit()