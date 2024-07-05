import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardFacture(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de facture
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardFacture
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Invoice'))
        self.label.pack(pady=5)