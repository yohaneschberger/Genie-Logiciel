import sqlite3

def clear_db():
    '''
    Fonction pour effacer la base de données et les tables
    '''
    with sqlite3.connect('quit.db') as db:
        # Etablissement de la connexion à la base de données
        c = db.cursor()

    # Requêtes pour effacer les tables
    c.execute('DROP TABLE IF EXISTS factures')
    c.execute('DROP TABLE IF EXISTS devis')
    c.execute('DROP TABLE IF EXISTS entreprise')
    c.execute('DROP TABLE IF EXISTS user')
    c.execute('DROP TABLE IF EXISTS personne')
    c.execute('DROP TABLE IF EXISTS clients')
    c.execute('DROP TABLE IF EXISTS employes')
    db.commit()

# Appel de la fonction pour effacer la base de données
clear_db()
