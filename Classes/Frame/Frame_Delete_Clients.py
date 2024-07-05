import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardDeleteClients
from Classes.Boutons import CButtonsDeleteClients

class Frame_Delete_Clients(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour les clients pour l'application en appelant la classe DashBoardDeleteClients et la classe ButtonsDeleteClients
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Delete_Clients
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.dash_board = CDashBoardDeleteClients.DashBoardDeleteClients(self)
        self.buttons = CButtonsDeleteClients.ButtonsDeleteClients(self, self.dash_board, self)
        self.geometry('800x600')
        self.title('Supprimer un client')
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
        self.dash_board.label.config(text=_('Delete Client'))
        self.dash_board.label_nom.config(text=_('Last Name'))
        self.dash_board.label_prenom.config(text=_('First Name'))
        self.buttons.button1.config(text=_('Search'))
        self.buttons.button_delete.config(text=_('Delete'))
        self.buttons.button2.config(text=_('Quit'))