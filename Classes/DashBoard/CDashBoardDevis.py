import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardDevis(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de devis
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardDevis
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Quotations'))
        self.label.pack(pady=5)