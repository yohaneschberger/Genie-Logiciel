import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardCreateClients
from Classes.Boutons import CButtonsCreateClients

class Frame_Create_Clients(tk.Toplevel):
    '''
    Classe qui crée une nouvelle fenetre pour les clients pour l'application en appelant la classe DashBoardCreateClients et la classe ButtonsCreateClients
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_Create_Clients
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        self.dash_board = CDashBoardCreateClients.DashBoardCreateClients(self)
        self.buttons = CButtonsCreateClients.ButtonsCreateClients(self, self.dash_board, self)
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
        self.dash_board.label.config(text=_('Client Creation'))
        self.dash_board.label1.config(text=_('Name'))
        self.dash_board.label2.config(text=_('First Name'))
        self.dash_board.label3.config(text=_('Phone'))
        self.dash_board.label4.config(text=_('Email'))
        self.dash_board.label5.config(text=_('Address'))
        self.dash_board.label6.config(text=_('Comment (optional)'))
        self.buttons.button1.config(text=_('Create'))
        self.buttons.button2.config(text=_('Import Client'))
        self.buttons.button3.config(text=_('Cancel'))
