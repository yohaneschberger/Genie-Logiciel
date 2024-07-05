import tkinter as tk
import gettext
_=gettext.gettext

from Classes.DAO.Dao_devis import Dao_devis
from Classes.DAO.Dao_facture import Dao_facture

class ButtonsHistoryFactureDevis(tk.Frame):
    '''
    Classe qui crée les boutons de la fenêtre de l'historique des factures et devis
    '''
    def __init__(self, master=None, dash_board=None, frame=None, client=None):
        '''
        Constructeur de la classe ButtonsHistoryFactureDevis
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.frame = frame
        self.client = client
        self.pack()
        self.radio_var = tk.IntVar()
        self.radio_button1 = tk.Radiobutton(self, text=_('Invoice'), value=1, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button1.pack(pady=5)
        self.radio_button2 = tk.Radiobutton(self, text=_('Quotation'), value=2, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button2.pack(pady=5)
        self.radio_button3 = tk.Radiobutton(self, text=_('All'), value=3, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button3.pack(pady=5)
        self.button = tk.Button(self, text=_('Back'), command=self.retour)
        self.button.pack(pady=5)

    def retour(self):
        '''
        Méthode qui permet de revenir en arrière
        '''
        self.master.destroy()

    def fill_treeview(self):
        '''
        Méthode qui permet de remplir le tableau de bord avec les factures et devis enregistrés dans la base de données en fonction de self.radio_var
        '''
        self.dash_board.tree.delete(*self.dash_board.tree.get_children())
        if self.radio_var.get() == 1:
            factures = Dao_facture.all_with_client(self.client[0])
            for facture in factures:
                numero_facture, date, total = facture
                self.dash_board.tree.insert('', 'end', values=(numero_facture, date, total))
        elif self.radio_var.get() == 2:
            devis = Dao_devis.all_with_client(self.client[0])
            for devis in devis:
                numero_devis, date, total = devis
                self.dash_board.tree.insert('', 'end', values=(numero_devis, date, total))
        else:
            factures = Dao_facture.all_with_client(self.client[0])
            for facture in factures:
                numero_facture, date, total = facture
                self.dash_board.tree.insert('', 'end', values=(numero_facture, date, total))
            devis = Dao_devis.all_with_client(self.client[0])
            for devis in devis:
                numero_devis, date, total = devis
                self.dash_board.tree.insert('', 'end', values=(numero_devis, date, total))