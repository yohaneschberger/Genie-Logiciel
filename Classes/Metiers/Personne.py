import sqlite3

class Personne:
    '''
    Classe pour la gestion des personnes
    '''
    def __init__(self, nom, prenom, telephone, email):
        '''
        Constructeur de la classe Personne
        '''
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def __str__(self):
        '''
        Méthode pour afficher les informations de la personne
        '''
        return f"{self.nom} {self.prenom} {self.telephone} {self.email}"

    def save(self):
        '''
        Méthode pour enregistrer les informations de la personne dans la base de données
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute("INSERT INTO personne(nom, prenom, telephone, email) VALUES(?, ?, ?, ?)", (self.nom, self.prenom, self.telephone, self.email))
            db.commit()

    @staticmethod
    def all():
        '''
        Méthode pour récupérer toutes les personnes de la base de données
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM personne')
            return c.fetchall()

    @staticmethod
    def get(id):
        '''
        Méthode pour récupérer une personne de la base de données
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM personne WHERE id = {id}')
            return c.fetchone()

    def delete(self):
        '''
        Méthode pour supprimer une personne de la base de données
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute('DELETE FROM personne WHERE id = {self.id}')
            db.commit()

    def update(self):
        '''
        Méthode pour mettre à jour les informations d'une personne dans la base de données
        '''
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()
            c.execute('UPDATE personne SET nom = ?, prenom = ?, telephone = ?, email = ? WHERE id = ?', (self.nom, self.prenom, self.telephone, self.email, self.id))
            db.commit()
