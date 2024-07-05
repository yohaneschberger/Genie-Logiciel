import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardLogo
from Classes.Boutons import CButtonsLogo

class Frame_Logo(tk.Frame):
    '''
    Classe qui modifie la fenêtre principale pour le logo pour l'application en appelant la classe DashBoardLogo et la classe ButtonsLogo
    '''
    def __init__(self, master=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe Frame_Logo
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.pack()
        self.dash_board = CDashBoardLogo.DashBoardLogo(self)
        self.buttons = CButtonsLogo.ButtonsLogo(self, self.dash_board, is_admin)
        self.translate()

    def translate(self):
        '''
        Méthode qui permet de traduire les textes de la fenêtre
        '''
        lang = self.language_var.get()
        gettext.bindtextdomain(lang, './Langage')
        gettext.textdomain(lang)
        translation = gettext.translation(lang, localedir = os.path.join(os.path.dirname(__file__), '..', 'Langage'), languages=[lang])
        translation.install()
        _ = translation.gettext
        self.dash_board.label.config(text=_('Logo visualization'))
        self.buttons.button1.config(text=_('Confirm'))
        self.buttons.button2.config(text=_('Import'))
        self.buttons.button3.config(text=_('Cancel'))