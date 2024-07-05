import tkinter as tk
import gettext
_=gettext.gettext
from Classes.DAO.Dao_devis import Dao_devis
from Classes.DAO.Dao_client import Dao_client

class ButtonsHistoryDevis(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de l'historique des devis
    '''
    def __init__(self, master=None, dash_board=None, top_level=None):
        '''
        Constructeur de la classe ButtonsHistoryDevis
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.pack()
        self.radio_var = tk.IntVar()
        self.radio_button1 = tk.Radiobutton(self, text=_('Validated'), value=1, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button1.pack(pady=5)
        self.radio_button2 = tk.Radiobutton(self, text=_('Not validated'), value=2, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button2.pack(pady=5)
        self.radio_button3 = tk.Radiobutton(self, text=_('All'), value=3, variable=self.radio_var, command=self.fill_treeview)
        self.radio_button3.pack(pady=5)
        self.button1 = tk.Button(self, text=_('Back'), command=self.back_to_frame_wel)
        self.button1.pack(pady=5)

    def back_to_frame_wel(self):
        '''
        Méthode qui permet de revenir à la fenêtre de bienvenue en supprimant le frame de devis et en recréant le frame de bienvenue
        '''
        self.top_level.destroy()

    def fill_treeview(self):
        '''
        Méthode qui permet de remplir le tableau de bord avec les devis enregistrés dans la base de données en fonction de self.radio_var
        '''
        self.dash_board.tree.delete(*self.dash_board.tree.get_children())
        if self.radio_var.get() == 1:
            devis = Dao_devis.all_validated()
        elif self.radio_var.get() == 2:
            devis = Dao_devis.all_unvalidated()
        else:
            devis = Dao_devis.all()
        for devis in devis:
            numero_devis, date, id_client, total, valide = devis
            client = Dao_client.get_nom_prenom(id_client)
            last_name, first_name = client
            self.dash_board.tree.insert('', 'end', values=(numero_devis, date, last_name, first_name, total, valide))