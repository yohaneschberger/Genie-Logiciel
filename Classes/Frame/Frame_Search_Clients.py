import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardSearchClients
from Classes.Boutons import CButtonsSearchClients

class Frame_Search_Clients(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour les clients pour l'application en appelant la classe DashBoardSearchClients et la classe ButtonsSearchClients
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Search_Clients
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.dash_board = CDashBoardSearchClients.DashBoardSearchClients(self)
        self.buttons = CButtonsSearchClients.ButtonsSearchClients(self, self.dash_board, self)
        self.geometry('800x600')
        self.title('Rechercher un client')
        self.translate()

    def translate(self):
        '''
        Méthode qui permet de traduire les textes de la fenêtre
        '''
        lang = self.master.language_var.get()
        gettext.bindtextdomain(lang, './Langage')
        gettext.textdomain(lang)
        translation = gettext.translation(lang, localedir = os.path.join(os.path.dirname(__file__), '..', 'Langage'), languages=[lang])
        translation.install()
        _ = translation.gettext
        self.dash_board.label.config(text=_('Search Client'))
        self.dash_board.label_nom.config(text=_('Last Name'))
        self.dash_board.label_prenom.config(text=_('First Name'))
        self.buttons.button.config(text=_('Search'))
        self.buttons.button_facture_devis.config(text=_('Invoice/Quotation'))
        self.buttons.button_export.config(text=_('Export'))
        self.buttons.button2.config(text=_('Back'))
