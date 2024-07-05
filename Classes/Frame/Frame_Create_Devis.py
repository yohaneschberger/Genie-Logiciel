import tkinter as tk
import gettext
import os
_=gettext.gettext
from Classes.DashBoard.CDashBoardCreateDevis import DashBoardCreateDevis
from Classes.Boutons.CButtonsCreateDevis import ButtonsCreateDevis

class Frame_Create_Devis(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour la recherche et la création de devis pour l'application en appelant la classe DashBoardCreateDevis et la classe ButtonsCreateDevis
    '''
    def __init__(self, client_to_search, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Create_Devis
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.client_to_search = client_to_search
        self.dashboard = DashBoardCreateDevis(self, self.client_to_search)
        self.buttons = ButtonsCreateDevis(self, self.dashboard, self)
        self.geometry('1000x600')
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
        self.dashboard.label1.config(text=_('Company name'))
        self.dashboard.label2.config(text=_('Company email'))
        self.dashboard.label3.config(text=_('Company address'))
        self.dashboard.label4.config(text=_('Company phone'))
        self.dashboard.label5.config(text=_('Billing Address'))
        self.dashboard.label6.config(text=_('Client name'))
        self.dashboard.label7.config(text=_('Client email'))
        self.dashboard.label8.config(text=_('Client address'))
        self.dashboard.label9.config(text=_('Client phone'))
        self.dashboard.label10.config(text=_('Quotation number'))
        self.dashboard.label11.config(text=_('Date'))
        self.dashboard.label12.config(text=_('Subtotal'))
        self.dashboard.label13.config(text=_('VAT'))
        self.dashboard.label14.config(text=_('Total'))
        self.buttons.button1.config(text=_('Change'))
        self.buttons.button2.config(text=_('Quit'))