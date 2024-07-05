import tkinter as tk
import gettext
import os

from Classes.DashBoard import CDashBoardWel
from Classes.Boutons import CButtonsWel

class Frame_Welcome(tk.Frame):
    '''
    Classe qui modifie la fenêtre principale pour la bienvenue après une connexion réussie pour l'application en appelant la classe DashBoardWel et la classe ButtonsWel
    '''
    def __init__(self, master=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe Frame_Welcome
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.pack()
        self.dash_board = CDashBoardWel.DashBoardWel(self)
        self.buttons = CButtonsWel.ButtonsWel(self, self.dash_board, is_admin)
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
        self.buttons.update_menu_labels(_)
        self.dash_board.label.config(text=_('Successful connection'))
        self.buttons.button1.config(text=_('Invoice'))
        self.buttons.button2.config(text=_('Quotation'))
        self.buttons.button3.config(text=_('Clients'))
        self.buttons.button4.config(text=_('Employes'))
        self.buttons.button5.config(text=_('Manage Company'))
        self.buttons.button6.config(text=_('Logout'))