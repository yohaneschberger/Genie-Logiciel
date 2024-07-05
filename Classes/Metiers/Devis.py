class Devis:
    '''
    Classe pour la gestion des devis
    '''
    def __init__(self, nom_devis, nom_entreprise, email_entreprise, adresse_entreprise, 
                 telephone_entreprise, nom_client, email_client, adresse_client, 
                 telephone_client, numero_devis, date, description, prix_unitaire, 
                 quantite, montant, sous_total, tva, total, id_client):
        self.nom_devis = nom_devis
        self.nom_entreprise = nom_entreprise
        self.email_entreprise = email_entreprise
        self.adresse_entreprise = adresse_entreprise
        self.telephone_entreprise = telephone_entreprise
        self.nom_client = nom_client
        self.email_client = email_client
        self.adresse_client = adresse_client
        self.telephone_client = telephone_client
        self.numero_devis = numero_devis
        self.date = date
        self.description = description
        self.prix_unitaire = prix_unitaire
        self.quantite = quantite
        self.montant = montant
        self.sous_total = sous_total
        self.tva = tva
        self.total = total
        self.id_client = id_client
        self.valide = False
        self.send = False