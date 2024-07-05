import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardSearchClients(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de recherche des clients
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardSearchClients
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Search clients'))
        self.label.pack(pady=5)

        self.label_nom = tk.Label(self, text=_('Last Name'))
        self.label_nom.pack(pady=5)
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack(pady=5)
        self.label_prenom = tk.Label(self, text=_('First Name'))
        self.label_prenom.pack(pady=5)
        self.entry_prenom = tk.Entry(self)
        self.entry_prenom.pack(pady=5)
        