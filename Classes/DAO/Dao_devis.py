import sqlite3

class Dao_devis:
    '''
    Classe pour la gestion des devis dans la base de données
    '''
    @staticmethod
    def save(devis):
        '''
        Méthode pour enregistrer les informations du devis dans la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute("""
                INSERT INTO devis(
                    nom_devis, nom_entreprise, email_entreprise, adresse_entreprise, 
                    telephone_entreprise, nom_client, email_client, adresse_client, 
                    telephone_client, numero_devis, date, description, prix_unitaire, 
                    quantite, montant, sous_total, tva, total, id_client
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, 
            (
                devis.nom_devis, devis.nom_entreprise, devis.email_entreprise, devis.adresse_entreprise, 
                devis.telephone_entreprise, devis.nom_client, devis.email_client, devis.adresse_client, 
                devis.telephone_client, devis.numero_devis, devis.date, devis.description, devis.prix_unitaire, 
                devis.quantite, devis.montant, devis.sous_total, devis.tva, devis.total, devis.id_client
            ))
            db.commit()

    @staticmethod
    def get(numero):
        '''
        Méthode pour récupérer un devis de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM devis WHERE numero_devis = ?', (numero,))
            result = c.fetchall()
            return None if len(result) == 0 else result
        
    @staticmethod
    def get_id(nom_client, email_client):
        '''
        Méthode pour récupérer l'identifiant d'un client
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT id FROM clients WHERE nom = ? AND email = ?', (nom_client, email_client))
            result = c.fetchone()
            return None if result is None else result[0]

    @staticmethod
    def get_next_id():
        '''
        Méthode pour récupérer le prochain identifiant du devis
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT MAX(id) FROM devis')
            max_id = c.fetchone()[0]
            return 1 if max_id is None else max_id + 1
        
    @staticmethod
    def change(devis):
        '''
        Méthode pour modifier un devis dans la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute("""
                UPDATE devis SET 
                    nom_devis = ?, nom_entreprise = ?, email_entreprise = ?, adresse_entreprise = ?, 
                    telephone_entreprise = ?, nom_client = ?, email_client = ?, adresse_client = ?, 
                    telephone_client = ?, numero_devis = ?, date = ?, description = ?, prix_unitaire = ?, 
                    quantite = ?, montant = ?, sous_total = ?, tva = ?, total = ?, id_client = ?
                WHERE numero_devis = ?
            """, 
            (
                devis.nom_devis, devis.nom_entreprise, devis.email_entreprise, devis.adresse_entreprise, 
                devis.telephone_entreprise, devis.nom_client, devis.email_client, devis.adresse_client, 
                devis.telephone_client, devis.numero_devis, devis.date, devis.description, devis.prix_unitaire, 
                devis.quantite, devis.montant, devis.sous_total, devis.tva, devis.total, devis.id_client, devis.numero_devis
            ))
            db.commit()

    @staticmethod
    def all():
        '''
        Méthode pour récupérer tous les devis de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT numero_devis, date, id_client, total, valide FROM devis')
            return c.fetchall()
        
    @staticmethod
    def all_with_client(client):
        '''
        Méthode pour récupérer tous les devis d'un client
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT numero_devis, date, total FROM devis WHERE id_client = ?', (client[0],))
            return c.fetchall()
        
    @staticmethod
    def all_validated():
        '''
        Méthode pour récupérer tous les devis validés de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT numero_devis, date, id_client, total, valide FROM devis WHERE valide = 1')
            return c.fetchall()
        
    @staticmethod
    def all_unvalidated():
        '''
        Méthode pour récupérer tous les devis non validés de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT numero_devis, date, id_client, total, valide FROM devis WHERE valide = 0')
            return c.fetchall()
        
    @staticmethod
    def send(numero_devis):
        '''
        Méthode pour envoyer un devis
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('UPDATE devis SET send = 1 WHERE numero_devis = ?', (numero_devis,))
            db.commit()

    @staticmethod
    def validate(numero_devis):
        '''
        Méthode pour valider un devis
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('UPDATE devis SET valide = 1 WHERE numero_devis = ?', (numero_devis,))
            db.commit()

    @staticmethod
    def delete(id):
        '''
        Méthode pour supprimer un devis de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('DELETE FROM devis WHERE id = ?', (id,))
            db.commit()