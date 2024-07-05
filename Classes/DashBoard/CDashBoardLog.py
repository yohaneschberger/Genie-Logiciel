import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardLog(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de login
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardLog
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Welcome to the billing management application'))
        self.label.pack(pady=5)
        self.label2 = tk.Label(self, text=_('Please identify yourself'))
        self.label2.pack(pady=5)
        self.label_login = tk.Label(self, text=_('Username'))
        self.label_login.pack(pady=5)
        self.entry_login = tk.Entry(self)
        self.entry_login.pack(pady=5)
        self.label_password = tk.Label(self, text=_('Password'))
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(self, show='*')
        self.entry_password.pack(pady=5)
        self.show_password_button = tk.Button(self, text=_('Visible'), command=self.toggle_password_visibility)
        self.show_password_button.pack(pady=5)

    def toggle_password_visibility(self):
        '''
        Méthode qui permet de montrer ou de cacher le mot de passe
        '''
        if self.entry_password.cget('show') == '':
            self.entry_password.config(show='*')
        else:
            self.entry_password.config(show='')
