import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardSearchCreateFacture(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de recherche des clients
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardSearchCreateClients
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Search clients'))
        self.label.pack(pady=5)

        self.label1 = tk.Label(self, text=_('Last Name'))
        self.label1.pack(pady=5)
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack(pady=5)
        self.label2 = tk.Label(self, text=_('First Name'))
        self.label2.pack(pady=5)
        self.entry_prenom = tk.Entry(self)
        self.entry_prenom.pack(pady=5)