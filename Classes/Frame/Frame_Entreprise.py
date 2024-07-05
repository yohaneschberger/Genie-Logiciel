import tkinter as tk
import gettext
import os

from Classes.DashBoard.CDashBoardEntreprise import DashBoardEntreprise
from Classes.Boutons.CButtonsEntreprise import ButtonsEntreprise

class Frame_Entreprise(tk.Frame):
    '''
    Classe qui modifie la fenêtre principale pour l'entreprise pour l'application en appelant la classe DashBoardEntreprise et la classe ButtonsEntreprise
    '''
    def __init__(self, master=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe Frame_Entreprise
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.pack()
        self.dash_board = DashBoardEntreprise(self)
        self.buttons = ButtonsEntreprise(self, self.dash_board, is_admin, self.language_var)
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
        self.dash_board.label.config(text=_('Company'))
        self.buttons.button1.config(text=_('Edit Company'))
        self.buttons.button2.config(text=_('Logo'))
        self.buttons.button3.config(text=_('Back'))
        
