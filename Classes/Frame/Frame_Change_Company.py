import tkinter as tk
import gettext
import os

from Classes.DashBoard.CDashBoardChangeCompany import DashBoardChangeCompany
from Classes.Boutons.CButtonsChangeCompany import ButtonsChangeCompany

class Frame_Change_Company(tk.Toplevel):
    '''
    Classe qui modifie la fenêtre principale pour changer les informations de l'entreprise pour l'application en appelant la classe DashBoardChangeCompany et la classe ButtonsChangeCompany
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Change_Company
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.dash_board = DashBoardChangeCompany(self)
        self.buttons = ButtonsChangeCompany(self, self.dash_board, self.language_var, self)
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
        self.dash_board.label1.config(text=_('Company name'))
        self.dash_board.label2.config(text=_('Company address'))
        self.dash_board.label3.config(text=_('Company phone'))
        self.dash_board.label4.config(text=_('Company email'))
        self.buttons.button1.config(text=_('Save'))
        self.buttons.button2.config(text=_('Cancel'))
