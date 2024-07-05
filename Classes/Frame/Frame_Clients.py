import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardClients
from Classes.Boutons import CButtonsClients

class Frame_Clients(tk.Frame):
    '''
    Classe qui modifie la fenêtre principale pour les clients pour l'application en appelant la classe DashBoardClients et la classe ButtonsClients
    '''
    def __init__(self, master=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe Frame_Clients
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.pack()
        self.dash_board = CDashBoardClients.DashBoardClients(self)
        self.buttons = CButtonsClients.ButtonsClients(self, self.dash_board, is_admin, self.language_var)
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
        self.dash_board.label.config(text=_('Clients'))
        self.buttons.button1.config(text=_('Create Client'))
        self.buttons.button2.config(text=_('Search Client'))
        self.buttons.button3.config(text=_('Delete Client'))
        self.buttons.button4.config(text=_('Back'))