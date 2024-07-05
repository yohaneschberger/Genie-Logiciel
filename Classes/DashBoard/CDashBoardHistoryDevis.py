import tkinter as tk
import tkinter.ttk as ttk
import gettext
_=gettext.gettext
from Classes.Frame.Frame_Change_Devis import Frame_Change_Devis

class DashBoardHistoryDevis(tk.Frame):
    '''
    Classe qui crée le tableau de bord pour l'historique des devis
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardHistoryDevis
        '''
        super().__init__(master)
        self.master = master
        self.pack()

        frame = ttk.Frame(self)
        frame.pack()
        
        self.tree = ttk.Treeview(frame, columns=('Numero', 'Date', 'Nom', 'Prenom', 'Total', 'Valide'), show='headings')
        self.tree.heading('Numero', text=_('Quotation Number'))
        self.tree.heading('Date', text=_('Date'))
        self.tree.heading('Nom', text=_('Last Name'))
        self.tree.heading('Prenom', text=_('First Name'))
        self.tree.heading('Total', text=_('Total'))
        self.tree.heading('Valide', text=_('Validated'))
        self.tree.column('Numero', width=150)
        self.tree.column('Date', width=150)
        self.tree.column('Nom', width=150)
        self.tree.column('Prenom', width=150)
        self.tree.column('Total', width=100)
        self.tree.column('Valide', width=80)
        self.tree.pack(side='left', fill='both', expand=True)

        self.scrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.bind('<Double-1>', self.open_devis)

    def open_devis(self, event):
        '''
        Méthode qui permet d'ouvrir un devis en double cliquant sur une ligne du tableau
        '''
        Frame_Change_Devis(self.master, language_var=self.master.language_var, numero_devis=self.tree.item(self.tree.selection())['values'][0])


