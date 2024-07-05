import tkinter as tk
from tkinter import messagebox as msg
import sqlite3
import gettext
import os

_=gettext.gettext

from Classes.Frame import Frame_Welcome

class ButtonsLog(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de login
    '''
    def __init__(self, master=None, dashboard=None):
        '''
        Constructeur de la classe ButtonsLog
        '''
        super().__init__(master)
        self.master = master
        self.dashboard = dashboard
        self.pack()
        if not hasattr(self.master, 'language_var'):
            self.master.language_var = tk.StringVar()
            self.master.language_var.set('en')
        self.radio_frame = tk.Frame(self)
        self.radio_frame.pack(side=tk.TOP, anchor=tk.NE, padx=5, pady=5)
        self.radio_fr = tk.Radiobutton(self.radio_frame, text='French', variable=self.master.language_var, value='fr', command=self.change_language)
        self.radio_fr.pack(side=tk.LEFT)
        self.radio_en = tk.Radiobutton(self.radio_frame, text='English', variable=self.master.language_var, value='en', command=self.change_language)
        self.radio_en.pack(side=tk.RIGHT)
        self.button_login = tk.Button(self, text='Login', command=self.login)
        self.button_login.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_quit = tk.Button(self, text='Quit', command=self.quit)
        self.button_quit.pack(side=tk.RIGHT, padx=5, pady=5)

    def change_language(self):
        '''
        Méthode pour changer la langue de l'application
        '''
        lang = self.master.language_var.get()   # Récupération de la langue choisie
        gettext.bindtextdomain(lang, './Langage')   # Définition du répertoire contenant les fichiers de traduction
        gettext.textdomain(lang)    # Définition du domaine de traduction
        translation = gettext.translation(lang, localedir = os.path.join(os.path.dirname(__file__), '..', 'Langage'), languages=[lang])  # Création de l'objet de traduction
        translation.install()   # Installation de l'objet de traduction
        _ = translation.gettext  # Récupération de la fonction de traduction

        # Modification des textes des widgets
        self.button_login.config(text=_('Login'))
        self.button_quit.config(text=_('Quit'))
        self.radio_fr.config(text=_('French'))
        self.radio_en.config(text=_('English'))
        self.dashboard.label_login.config(text=_('Login'))
        self.dashboard.label_password.config(text=_('Password'))
        self.dashboard.label.config(text=_('Welcome to the billing management application'))
        self.dashboard.label2.config(text=_('Please identify yourself'))
    
    def login(self):
        '''
        Méthode pour vérifier le login et le mot de passe
        '''
        username = self.dashboard.entry_login.get()
        password = self.dashboard.entry_password.get()

        conn = sqlite3.connect('Bdd/quit.db')
        conn.row_factory = sqlite3.Row  # Pour pouvoir accéder aux colonnes par leur nom
        c = conn.cursor()

        c.execute('SELECT * FROM user WHERE username = ? AND password = ?', (username, password))
        result = c.fetchone()

        if result:  # Si le login et le mot de passe sont corrects
            print(_('Login successful'))
            if result['admin'] == 1:    # Si l'utilisateur est un admin
                print(_('Admin account'))
                for widget in self.master.winfo_children():
                    widget.destroy()
                Frame_Welcome.Frame_Welcome(self.master, is_admin=True, language_var=self.master.language_var)
            else:   # Si l'utilisateur est un user
                print(_('User account'))
                for widget in self.master.winfo_children():
                    widget.destroy()
                Frame_Welcome.Frame_Welcome(self.master, language_var=self.master.language_var)
        else:    # Si le login et le mot de passe sont incorrects
            print(_('Login failed'))
            msg.showerror(_('Error'), _('Login failed'))

    def quit(self):
        '''
        Méthode pour quitter l'application
        '''
        self.master.quit()