from Classes.Metiers.Personne import Personne

class Clients(Personne):
    '''
    Classe pour la gestion des clients
    '''
    def __init__(self, nom, prenom, telephone, email, adresse, commentaire=None):
        '''
        Constructeur de la classe Clients
        '''
        super().__init__(nom, prenom, telephone, email)
        self.adresse = adresse
        self.commentaire = commentaire
