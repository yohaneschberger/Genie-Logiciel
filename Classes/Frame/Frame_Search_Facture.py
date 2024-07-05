import tkinter as tk
import gettext
import os
from Classes.DashBoard.CDashBoardSearchFacture import CDashBoardSearchFacture
from Classes.Boutons.CButtonsSearchFacture import CButtonsSearchFacture

class Frame_Search_Facture(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour les factures pour l'application en appelant la classe DashBoardSearchFacture et la classe ButtonsSearchFacture
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Search_Facture
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.dash_board = CDashBoardSearchFacture(self)
        self.buttons = CButtonsSearchFacture(self, self.dash_board, self, self.language_var)
        self.geometry('800x600')
        self.title('Rechercher une facture')
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
        self.dash_board.label.config(text=_('Search Invoices'))
        self.dash_board.label_numero.config(text=_('Invoice Number'))
        self.buttons.button.config(text=_('Search'))
        self.buttons.button_change.config(text=_('Change'))
        self.buttons.button_supprimer.config(text=_('Delete'))
        self.buttons.button_quitter.config(text=_('Quit'))
        self.buttons.label1.config(text='')