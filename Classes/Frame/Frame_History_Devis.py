import tkinter as tk
import gettext
_=gettext.gettext
import os
from Classes.DashBoard.CDashBoardHistoryDevis import DashBoardHistoryDevis
from Classes.Boutons.CButtonsHistoryDevis import ButtonsHistoryDevis

class Frame_History_Devis(tk.Toplevel):
    '''
    Classe qui crée la fenêtre de l'historique des devis
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_History_Devis
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.dash_board = DashBoardHistoryDevis(self)
        self.buttons = ButtonsHistoryDevis(self, self.dash_board, self)
        self.title(_('Quote History'))
        self.geometry('800x600')
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
        self.buttons.radio_button1.config(text=_('Validated'))
        self.buttons.radio_button2.config(text=_('Not validated'))
        self.buttons.radio_button3.config(text=_('All'))
        self.buttons.button1.config(text=_('Back'))
        