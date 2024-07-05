from Classes.Metiers.Singleton import Singleton
from Classes.Metiers.Clients import Clients
from Classes.Metiers.Employes import Employes

class PersonneFactory(metaclass=Singleton):
    '''
    Classe pour la création des personnes (clients ou employés) avec le design pattern Singleton
    '''
    def __init__(self):
        '''
        Constructeur de la classe PersonneFactory
        '''

    def create_personne(self, type, nom, prenom, telephone, email, adresse=None, commentaire=None):
        '''
        Méthode pour créer une personne (Client ou Employé)
        '''
        if type == 'client':
            new_client = Clients(nom, prenom, telephone, email, adresse, commentaire)
            return new_client
        elif type == 'employe':
            new_employe = Employes(nom, prenom, telephone, email)
            return new_employe
        else:
            raise ValueError('Type de personne inconnu')
            

