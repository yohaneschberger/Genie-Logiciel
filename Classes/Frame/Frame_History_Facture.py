import tkinter as tk
import gettext
import os
from Classes.DashBoard.CDashBoardHistoryFacture import CDashBoardHistoryFacture
from Classes.Boutons.CButtonsHistoryFacture import CButtonsHistoryFacture

class Frame_History_Facture(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour l'historique des factures pour l'application en appelant la classe DashBoardHistoryFacture et la classe ButtonsHistoryFacture
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_History_Facture
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.dash_board = CDashBoardHistoryFacture(self)
        self.buttons = CButtonsHistoryFacture(self, self.dash_board, self)
        self.geometry('900x400')
        self.title('Historique des factures')
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
        self.dash_board.label.config(text=_('Invoice History'))
        self.buttons.radio_button1.config(text=_('Payed'))
        self.buttons.radio_button2.config(text=_('Not payed'))
        self.buttons.radio_button3.config(text=_('All'))
        self.buttons.button_quitter.config(text=_('Back'))

        