import tkinter as tk
import gettext
_=gettext.gettext

class CDashBoardSearchFacture(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de recherche des factures
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardSearchFacture
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Search Invoices'))
        self.label.pack(pady=5)

        self.label_numero = tk.Label(self, text=_('Invoice Number'))
        self.label_numero.pack(pady=5)
        self.entry_numero = tk.Entry(self)
        self.entry_numero.pack(pady=5)
    