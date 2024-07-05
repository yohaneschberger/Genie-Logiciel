import tkinter as tk
import gettext
_=gettext.gettext
from Classes.Frame import Frame_Welcome
from Classes.Frame import Frame_Search_Facture
from Classes.Frame import Frame_Search_Create_Facture
from Classes.Frame import Frame_History_Facture

class ButtonsFacture(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de facture
    '''
    def __init__(self, master=None, dash_board=None, is_admin=False):
        '''
        Constructeur de la classe ButtonsFacture
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.is_admin = is_admin
        self.pack()
        self.button1 = tk.Button(self, text=_('Search Invoice'), command=self.search_Facture)
        self.button1.pack(padx=5)
        self.button2 = tk.Button(self, text=_('Invoice History'), command=self.history_Facture)
        self.button2.pack(padx=5)
        self.button3 = tk.Button(self, text=_('Create Invoice'), command=self.create_Facture)
        self.button3.pack(padx=5)
        self.button4 = tk.Button(self, text=_('Back'), command=self.back_to_frame_wel)
        self.button4.pack(padx=5)

    def search_Facture(self):
        '''
        Méthode qui permet de rechercher une facture
        '''
        Frame_Search_Facture.Frame_Search_Facture(self.master, language_var=self.master.language_var)

    def history_Facture(self):
        '''
        Méthode qui permet de voir l'historique des factures
        '''
        Frame_History_Facture.Frame_History_Facture(self.master, language_var=self.master.language_var)

    def create_Facture(self):
        '''
        Méthode qui permet de créer une facture
        '''
        Frame_Search_Create_Facture.Frame_Search_Create_Facture(self.master, language_var=self.master.language_var)

    def back_to_frame_wel(self):
        '''
        Méthode qui permet de revenir à la fenêtre de bienvenue en supprimant le frame de facture et en recréant le frame de bienvenue
        '''
        self.dash_board.destroy()
        self.destroy()
        self.master.pack()
        if self.is_admin:
            Frame_Welcome.Frame_Welcome(self.master, is_admin=True, language_var=self.master.language_var)
        else:
            Frame_Welcome.Frame_Welcome(self.master, language_var=self.master.language_var)