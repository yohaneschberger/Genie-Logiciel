import tkinter as tk
import gettext
_=gettext.gettext

from Classes.Frame.Frame_Logo import Frame_Logo
from Classes.Frame import Frame_Welcome
from Classes.Frame.Frame_Change_Company import Frame_Change_Company

class ButtonsEntreprise(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de l'entreprise
    '''
    def __init__(self, master=None, dash_board=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe ButtonsEntreprise
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.is_admin = is_admin
        self.language_var = language_var
        self.pack()

        self.button1 = tk.Button(self, text=_('Edit Company'), command=self.edit_company)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Logo'), command=self.logo)
        self.button2.pack(pady=5)
        self.button3 = tk.Button(self, text=_('Back'), command=self.back_to_welcome)
        self.button3.pack(pady=5)

    def edit_company(self):
        '''
        Méthode qui permet de modifier les informations de l'entreprise
        '''
        Frame_Change_Company(self.master, language_var=self.language_var)

    def logo(self):
        '''
        Méthode qui permet de modifier le logo de l'entreprise
        '''
        for widget in self.master.winfo_children():
            widget.destroy()
        Frame_Logo(self.master, is_admin=self.is_admin, language_var=self.language_var)

    def back_to_welcome(self):
        '''
        Méthode qui permet de retourner à la fenêtre de bienvenue
        '''
        for widget in self.master.winfo_children():
            widget.destroy()
        Frame_Welcome.Frame_Welcome(self.master, is_admin=self.is_admin, language_var=self.language_var)
