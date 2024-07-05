import tkinter as tk

class Frame(tk.Tk):
    '''
    Classe qui fabrique la fenêtre principale
    '''
    def __init__(self):
        '''
        Constructeur de la classe Frame
        '''
        super().__init__()
        self.title('Application de gestion de facturation')
        self.geometry('800x600')
