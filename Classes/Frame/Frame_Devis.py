import tkinter as tk
import gettext
import os
_ = gettext.gettext
from Classes.DashBoard import CDashBoardDevis
from Classes.Boutons import CButtonsDevis

class Frame_Devis(tk.Frame):
    '''
    Classe qui modifie la fenêtre principale pour le devis pour l'application en appelant la classe DashBoardDevis et la classe ButtonsDevis
    '''
    def __init__(self, master=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe Frame_Devis
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.pack()
        self.dash_board = CDashBoardDevis.DashBoardDevis(self)
        self.buttons = CButtonsDevis.ButtonsDevis(self, self.dash_board, is_admin, self.language_var)
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
        self.dash_board.label.config(text=_('Quotations'))
        self.buttons.button1.config(text=_('Search Quotation'))
        self.buttons.button2.config(text=_('Quotation History'))
        self.buttons.button3.config(text=_('Create Quotation'))
        self.buttons.button4.config(text=_('Back'))

        