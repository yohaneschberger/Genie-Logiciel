import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardSearchDevis(tk.Frame):
    '''
    Classe qui crée le tableau de bord pour la recherche de devis
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardSearchDevis
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Search Quotations'))
        self.label.pack(pady=5)

        self.label_numero = tk.Label(self, text=_('Number of Quotation'))
        self.label_numero.pack(pady=5)
        self.entry_numero = tk.Entry(self)
        self.entry_numero.pack(pady=5)