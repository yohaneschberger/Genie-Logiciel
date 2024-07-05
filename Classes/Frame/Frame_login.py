import tkinter as tk
import gettext
import os
from Classes.DashBoard import CDashBoardLog
from Classes.Boutons import CButtonsLog

class Frame_login(tk.Frame):
    '''
    Classe qui modifie la fenêtre principale pour le login pour l'application en appelant la classe DashBoardLog et la classe ButtonsLog
    '''
    def __init__(self, master=None, language_var=None):
        '''
        Constructeur de la classe Frame_login
        '''
        super().__init__(master)
        self.master = master
        self.language_var = language_var
        if self.language_var is None:
            self.language_var = tk.StringVar()
            self.language_var.set('en')
        self.pack()
        self.dash_board = CDashBoardLog.DashBoardLog(self.master)
        self.buttons = CButtonsLog.ButtonsLog(self.master, self.dash_board)
        self.translate()

    def translate(self):
        '''
        Méthode qui permet de traduire les textes de la fenêtre
        '''
        lang = self.language_var.get()
        gettext.bindtextdomain(lang, './Langage')
        gettext.textdomain(lang)
        translation = gettext.translation(lang, localedir = os.path.join(os.path.dirname(__file__), '..', 'Langage'), languages=[lang])
        translation.install()
        _ = translation.gettext
        self.dash_board.label.config(text=_('Welcome to the billing management application'))
        self.dash_board.label2.config(text=_('Please identify yourself'))
        self.dash_board.label_login.config(text=_('Login'))
        self.dash_board.label_password.config(text=_('Password'))
        self.buttons.button_login.config(text=_('Login'))
        self.buttons.button_quit.config(text=_('Quit'))
        self.buttons.radio_fr.config(text=_('French'))
        self.buttons.radio_en.config(text=_('English'))