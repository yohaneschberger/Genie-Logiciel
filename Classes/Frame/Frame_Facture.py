import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardFacture
from Classes.Boutons import CButtonsFacture

class Frame_Facture(tk.Frame):
    '''
    Classe qui modifie la fenêtre principale pour la facture pour l'application en appelant la classe DashBoardFacture et la classe ButtonsFacture
    '''
    def __init__(self, master=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe Frame_Facture
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.pack()
        self.dash_board = CDashBoardFacture.DashBoardFacture(self)
        self.buttons = CButtonsFacture.ButtonsFacture(self, self.dash_board, is_admin)
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
        self.dash_board.label.config(text=_('Invoice'))
        self.buttons.button1.config(text=_('Search Invoice'))
        self.buttons.button2.config(text=_('Invoice History'))
        self.buttons.button3.config(text=_('Create Invoice'))
        self.buttons.button4.config(text=_('Back'))