import tkinter as tk
from tkinter import ttk
import gettext
_=gettext.gettext

from Classes.Frame.Frame_Change_Devis import Frame_Change_Devis
from Classes.Frame.Frame_Change_Facture import Frame_Change_Facture

class DashBoardHistoryFactureDevis(tk.Frame):
    '''
    Classe qui crée le tableau de bord de l'historique des factures et devis
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardHistoryFactureDevis
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        
        frame = ttk.Frame(self)
        frame.pack()

        self.tree = ttk.Treeview(frame, columns=('Numero', 'Date', 'Total'), show='headings')
        self.tree.heading('Numero', text=_('Number'))
        self.tree.heading('Date', text=_('Date'))
        self.tree.heading('Total', text=_('Total'))
        self.tree.column('Numero', width=150)
        self.tree.column('Date', width=150)
        self.tree.column('Total', width=150)
        self.tree.pack(side='left', fill='both', expand=True)

        self.scrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.bind('<Double-1>', self.open_facture_devis)

    def open_facture_devis(self, event):
        '''
        Méthode qui permet d'ouvrir une facture ou un devis en double cliquant sur une ligne du tableau
        '''
        numero = self.tree.item(self.tree.selection())['values'][0]
        if numero.startswith('D'):
            Frame_Change_Devis(self.master, language_var=self.master.language_var, numero_devis=numero)
        else:
            Frame_Change_Facture(self.master, language_var=self.master.language_var, numero_facture=numero)