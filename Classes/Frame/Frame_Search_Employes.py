import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardSearchEmployes
from Classes.Boutons import CButtonsSearchEmployes

class Frame_Search_Employes(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour les employés pour l'application en appelant la classe DashBoardSearchEmployes et la classe ButtonsSearchEmployes
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Search_Employes
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.dash_board = CDashBoardSearchEmployes.DashBoardSearchEmployes(self)
        self.buttons = CButtonsSearchEmployes.ButtonsSearchEmployes(self, self.dash_board, self)
        self.geometry('800x600')
        self.title('Rechercher un employé')
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
        self.dash_board.label.config(text=_('Search Employee'))
        self.dash_board.label_nom.config(text=_('Last Name'))
        self.dash_board.label_prenom.config(text=_('First Name'))
        self.buttons.button1.config(text=_('Search'))
        self.buttons.button2.config(text=_('Back'))
