import tkinter as tk
import gettext
import os
_ = gettext.gettext

from Classes.DashBoard.CDashBoardHistoryFactureDevis import DashBoardHistoryFactureDevis
from Classes.Boutons.CButtonsHistoryFactureDevis import ButtonsHistoryFactureDevis

class Frame_History_Facture_Devis(tk.Toplevel):
    '''
    Classe qui affiche la liste des factures et devis du client
    '''
    def __init__(self, master=None, client=None, language_var=None):
        '''
        Constructeur de la classe Frame_History_Facture_Devis
        '''
        super().__init__(master)
        self.master = master
        self.client = client
        self.language_var = language_var
        self.dash_board = DashBoardHistoryFactureDevis(self)
        self.buttons = ButtonsHistoryFactureDevis(self, self.dash_board, self, self.client)
        self.title(_('Bill/Quote History'))
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
        self.buttons.radio_button1.config(text=_('Invoice'))
        self.buttons.radio_button2.config(text=_('Quotation'))
        self.buttons.radio_button3.config(text=_('All'))
        self.buttons.button.config(text=_('Back'))
