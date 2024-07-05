import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardCreateEmployes
from Classes.Boutons import CButtonsCreateEmployes

class Frame_Create_Employes(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour les employés pour l'application en appelant la classe DashBoardCreateEmployes et la classe ButtonsCreateEmployes
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Create_Employes
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.dash_board = CDashBoardCreateEmployes.DashBoardCreateEmployes(self)
        self.buttons = CButtonsCreateEmployes.ButtonsCreateEmployes(self, self.dash_board, self)
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
        self.dash_board.label.config(text=_('Create Employee'))
        self.dash_board.label_nom.config(text=_('Name'))
        self.dash_board.label_prenom.config(text=_('First Name'))
        self.dash_board.label_telephone.config(text=_('Phone'))
        self.dash_board.label_email.config(text=_('Email'))
        self.buttons.button1.config(text=_('Create'))
        self.buttons.button2.config(text=_('Back'))