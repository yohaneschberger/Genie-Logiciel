import sqlite3
from Classes.Metiers.Personne import Personne

class Employes(Personne):
    '''
    Classe pour la gestion des employés
    '''
    def __init__(self, nom, prenom, telephone, email):
        '''
        Constructeur de la classe Employes
        '''
        super().__init__(nom, prenom, telephone, email)

    def __str__(self):
        '''
        Méthode pour afficher les informations de l'employé
        '''
        return f"{super().__str__()}"

    def save(self):
        '''
        Méthode pour enregistrer les informations de l'employé dans la base de données
        '''
        super().save()
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute("INSERT INTO employes(nom, prenom, telephone, email, personne_id) VALUES(?, ?, ?, ?, (SELECT MAX(id) FROM personne))", (self.nom, self.prenom, self.telephone, self.email))
            db.commit()

    @staticmethod
    def all():
        '''
        Méthode pour récupérer tous les employés de la base de données
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM employes')
            return c.fetchall()

    @staticmethod
    def get(nom, prenom):
        '''
        Méthode pour récupérer un employé de la base de données en fonction du nom et du prénom
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM employes WHERE nom = ? AND prenom = ?', (nom, prenom,))
            result = c.fetchall()
            return None if len(result) == 0 else result

    def delete(nom, prenom):
        '''
        Méthode pour supprimer un employé de la base de données
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute('DELETE FROM employes WHERE nom = ? AND prenom = ?', (nom, prenom,))
            db.commit()

    def update(self):
        '''
        Méthode pour mettre à jour les informations d'un employé dans la base de données
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute('UPDATE employes SET nom = ?, prenom = ?, telephone = ?, email = ? WHERE id = ?', (self.nom.get(), self.prenom.get(), self.telephone.get(), self.email.get(), self.id))
            db.commit()
