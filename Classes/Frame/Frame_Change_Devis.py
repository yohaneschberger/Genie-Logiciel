import tkinter as tk
import gettext
_=gettext.gettext
import os
from Classes.DashBoard.CDashBoardChangeDevis import DashBoardChangeDevis
from Classes.Boutons.CButtonsChangeDevis import ButtonsChangeDevis

class Frame_Change_Devis(tk.Toplevel):
    '''
    Classe qui crée la fenêtre de changement de devis
    '''
    def __init__(self, master=None, language_var=None, numero_devis=None):
        '''
        Constructeur de la classe Frame_Change_Devis
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        print(language_var.get())
        self.numero_devis = numero_devis
        self.dashboard = DashBoardChangeDevis(self, self.numero_devis)
        self.buttons = ButtonsChangeDevis(self, self.dashboard, self)
        self.title(_('Change Quote'))
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
        self.buttons.button_change.config(text=_('Create Quotation'))
        self.buttons.button_quitter.config(text=_('Quit'))