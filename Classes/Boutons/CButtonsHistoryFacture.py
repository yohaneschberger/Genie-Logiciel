import tkinter as tk
import gettext
_=gettext.gettext
from Classes.DAO.Dao_facture import Dao_facture
from Classes.DAO.Dao_client import Dao_client

class CButtonsHistoryFacture(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de l'historique des factures
    '''
    def __init__(self, master=None, dash_board=None, top_level=None):
        '''
        Constructeur de la classe ButtonsHistoryFacture
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.pack()
        self.radio_var = tk.IntVar()
        self.radio_button1 = tk.Radiobutton(self, text=_('Payed'), value=1, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button1.pack(pady=5)
        self.radio_button2 = tk.Radiobutton(self, text=_('Not payed'), value=2, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button2.pack(pady=5)
        self.radio_button3 = tk.Radiobutton(self, text=_('All'), value=3, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button3.pack(pady=5)
        self.button_quitter = tk.Button(self, text=_('Back'), command=self.back_to_frame_wel)
        self.button_quitter.pack(padx=5)

    def back_to_frame_wel(self):
        '''
        Méthode qui permet de revenir à la fenêtre de bienvenue en supprimant le frame de l'historique des factures et en recréant le frame de bienvenue
        '''
        self.top_level.destroy()

    def fill_treeview(self):
        '''
        Méthode qui permet de remplir le tableau de bord avec les factures enregistrées dans la base de données en fonction de self.buttons.radio_var
        '''
        self.dash_board.tree.delete(*self.dash_board.tree.get_children())
        if self.radio_var.get() == 1:
            factures = Dao_facture().all_payed()
        elif self.radio_var.get() == 2:
            factures = Dao_facture().all_unpayed()
        else:
            factures = Dao_facture().all()
        for facture in factures:
            numero_facture, date, id_client, total, paye = facture
            client = Dao_client().get_nom_prenom(id_client)
            last_name, first_name = client
            self.dash_board.tree.insert('', 'end', values=(numero_facture, date, last_name, first_name, total, paye))