import tkinter as tk
import gettext
_=gettext.gettext
import os
from Classes.DashBoard.CDashBoardChangeFacture import DashBoardChangeFacture
from Classes.Boutons.CButtonsChangeFacture import ButtonsChangeFacture

class Frame_Change_Facture(tk.Toplevel):
    '''
    Classe qui crée la fenêtre de changement de facture
    '''
    def __init__(self, master=None, language_var=None, numero_facture=None):
        '''
        Constructeur de la classe Frame_Change_Facture
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.numero_facture = numero_facture
        self.dashboard = DashBoardChangeFacture(self, self.numero_facture)
        self.buttons = ButtonsChangeFacture(self, self.dashboard, self)
        self.title(_('Change Invoice'))
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
        self.dashboard.label10.config(text=_('Invoice number'))
        self.dashboard.label11.config(text=_('Date'))
        self.dashboard.label12.config(text=_('Payment Terms'))
        self.dashboard.label13.config(text=_('Subtotal'))
        self.dashboard.label14.config(text=_('TVA'))
        self.dashboard.label15.config(text=_('Total'))
        self.dashboard.label16.config(text=_('Amount due'))
        self.buttons.button_change.config(text=_('Change'))
        self.buttons.button_quitter.config(text=_('Quit'))