import tkinter as tk
import tkinter.ttk as ttk
import gettext
_=gettext.gettext
from Classes.Frame.Frame_Change_Facture import Frame_Change_Facture

class CDashBoardHistoryFacture(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de l'historique des factures
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe DashBoardHistoryFacture
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.pack()
        self.label = tk.Label(self, text=_('Invoice History'))
        self.label.pack(pady=5)

        frame = ttk.Frame(self)
        frame.pack()

        self.tree = ttk.Treeview(frame, columns=('Numero', 'Date', 'Nom', 'Prenom', 'Total', 'Payee'), show='headings')
        self.tree.heading('Numero', text=_('Invoice Number'))
        self.tree.heading('Date', text=_('Date'))
        self.tree.heading('Nom', text=_('Last Name'))
        self.tree.heading('Prenom', text=_('First Name'))
        self.tree.heading('Total', text=_('Total'))
        self.tree.heading('Payee', text=_('Paid'))
        self.tree.column('Numero', width=150)
        self.tree.column('Date', width=150)
        self.tree.column('Nom', width=150)
        self.tree.column('Prenom', width=150)
        self.tree.column('Total', width=100)
        self.tree.column('Payee', width=80)
        self.tree.pack(side='left', fill='both', expand=True)
        
        self.scrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.bind('<Double-1>', self.open_facture)

    def open_facture(self, event):
        '''
        Méthode qui permet d'ouvrir une facture en double cliquant sur une ligne du tableau
        '''
        Frame_Change_Facture(self.master, numero_facture=self.tree.item(self.tree.selection())['values'][0], language_var=self.language_var)