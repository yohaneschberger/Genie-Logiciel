import tkinter as tk
import gettext
_=gettext.gettext
import os
from Classes.DashBoard.CDashBoardSearchDevis import DashBoardSearchDevis
from Classes.Boutons.CButtonsSearchDevis import ButtonsSearchDevis

class Frame_Search_Devis(tk.Toplevel):
    '''
    Classe qui crée la fenêtre de recherche de devis
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Search_Devis
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.dashboard = DashBoardSearchDevis(self)
        self.buttons = ButtonsSearchDevis(self, self.dashboard, self, self.language_var)
        self.title(_('Search Quote'))
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
        self.dashboard.label_numero.config(text=_('Number of Quotation'))
        self.buttons.button1.config(text=_('Search'))
        self.buttons.button_change.config(text=_('Change'))
        self.buttons.button_send.config(text=_('Send'))
        self.buttons.button_valider.config(text=_('Validate'))
        self.buttons.button_supprimer.config(text=_('Delete'))
        self.buttons.button_quitter.config(text=_('Quit'))
