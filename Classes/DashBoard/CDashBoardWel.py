import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardWel(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de bienvenue après une connexion réussie
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardWel après une connexion réussie
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Successful connection'))
        self.label.pack(pady=5)
