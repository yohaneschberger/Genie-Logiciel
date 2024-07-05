class Singleton(type):
    '''
    Classe pour le design pattern Singleton
    '''
    _instances = {} # Dictionnaire pour stocker les instances des classes
    def __call__(cls, *args, **kwargs):
        '''
        Méthode pour appeler une instance de la classe.
        args: arguments de la classe, kwargs: arguments nommés de la classe
        '''
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
