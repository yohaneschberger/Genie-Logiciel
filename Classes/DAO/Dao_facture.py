import sqlite3

class Dao_facture:
    '''
    Classe pour la gestion des factures dans la base de données
    '''
    @staticmethod
    def save(facture):
        '''
        Méthode pour enregistrer les informations de la facture dans la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute("""
                INSERT INTO factures(
                    nom_facture, nom_entreprise, email_entreprise, adresse_entreprise, 
                    telephone_entreprise, nom_client, email_client, adresse_client, 
                    telephone_client, numero_facture, date, conditions, description, 
                    prix_unitaire, quantite, montant, sous_total, tva, total, solde_du, id_client
                ) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, 
            (
                facture.nom_facture, facture.nom_entreprise, facture.email_entreprise, facture.adresse_entreprise, 
                facture.telephone_entreprise, facture.nom_client, facture.email_client, facture.adresse_client, 
                facture.telephone_client, facture.numero_facture, facture.date, facture.conditions, facture.description, 
                facture.prix_unitaire, facture.quantite, facture.montant, facture.sous_total, facture.tva, facture.total, 
                facture.solde_du, facture.id_client              
            ))
            db.commit()
            return c.fetchall()
        
    @staticmethod
    def get(numero):
        '''
        Méthode pour récupérer une facture de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT * FROM factures WHERE numero_facture = ?', (numero,))
            result = c.fetchall()
            return None if len(result) == 0 else result
        
    @staticmethod
    def get_next_id():
        '''
        Méthode pour récupérer l'identifiant de la prochaine facture
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT MAX(id) FROM factures')
            max_id = c.fetchone()[0]
            return 1 if max_id is None else max_id + 1
        
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
    def change(facture):
        '''
        Méthode pour modifier les informations d'une facture dans la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute("""
                UPDATE factures SET 
                nom_facture = ?, nom_entreprise = ?, email_entreprise = ?, adresse_entreprise = ?, 
                telephone_entreprise = ?, nom_client = ?, email_client = ?, adresse_client = ?, 
                telephone_client = ?, numero_facture = ?, date = ?, conditions = ?, description = ?, 
                prix_unitaire = ?, quantite = ?, montant = ?, sous_total = ?, tva = ?, total = ?, 
                solde_du = ?, id_client = ? WHERE id = ?
            """, 
            (
                facture.nom_facture, facture.nom_entreprise, facture.email_entreprise, facture.adresse_entreprise, 
                facture.telephone_entreprise, facture.nom_client, facture.email_client, facture.adresse_client, 
                facture.telephone_client, facture.numero_facture, facture.date, facture.conditions, facture.description, 
                facture.prix_unitaire, facture.quantite, facture.montant, facture.sous_total, facture.tva, facture.total, 
                facture.solde_du, facture.id_client, facture.id_client
            ))
            db.commit()
            return c.fetchall()

    @staticmethod
    def all():
        '''
        Méthode pour récupérer toutes les factures de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT numero_facture, date, id_client, total, payed FROM factures')
            return c.fetchall()
        
    @staticmethod
    def all_with_client(client):
        '''
        Méthode pour récupérer toutes les factures d'un client de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT numero_facture, date, total FROM factures WHERE id_client = ?', (client[0],))
            return c.fetchall()
        
    @staticmethod
    def all_payed():
        '''
        Méthode pour récupérer toutes les factures payées de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT numero_facture, date, id_client, total, payed FROM factures WHERE payed = 1')
            return c.fetchall()
        
    @staticmethod
    def all_unpayed():
        '''
        Méthode pour récupérer toutes les factures non payées de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('SELECT numero_facture, date, id_client, total, payed FROM factures WHERE payed = 0')
            return c.fetchall()

    @staticmethod
    def delete(numero):
        '''
        Méthode pour supprimer une facture de la base de données
        '''
        with sqlite3.connect('Bdd/quit.db') as db:
            c = db.cursor()
            c.execute('DELETE FROM factures WHERE numero_facture = ?', (numero,))
            db.commit()