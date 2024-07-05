import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardEmployes
from Classes.Boutons import CButtonsEmployes

class Frame_Employes(tk.Frame):
    '''
    Classe qui modifie la fenêtre principale pour les employés pour l'application en appelant la classe DashBoardEmployes et la classe ButtonsEmployes
    '''
    def __init__(self, master=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe Frame_Employes
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.pack()
        self.dash_board = CDashBoardEmployes.DashBoardEmployes(self)
        self.buttons = CButtonsEmployes.ButtonsEmployes(self, self.dash_board, is_admin, self.language_var)
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
        self.dash_board.label.config(text=_('Employes'))
        self.buttons.button1.config(text=_('Create Employee'))
        self.buttons.button2.config(text=_('Search Employee'))
        self.buttons.button3.config(text=_('Delete Employee'))
        self.buttons.button4.config(text=_('Back'))