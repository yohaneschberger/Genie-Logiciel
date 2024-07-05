import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardEntreprise(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de l'entreprise
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardEntreprise
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Company'))
        self.label.pack()