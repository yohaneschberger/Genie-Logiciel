import tkinter as tk
from tkinter import ttk
import gettext
import os
_ = gettext.gettext
from Classes.DashBoard import CDashBoardCreateFacture
from Classes.Boutons import CButtonsCreateFacture

class Frame_Create_Facture(tk.Toplevel):
    '''
    Classe qui crée la fenêtre de création de facture
    '''
    def __init__(self, client_to_search, master=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe Frame_Create_Facture
        '''
        super().__init__(master)
        self.master = master
        self.is_admin = is_admin
        self.language_var = language_var
        print(language_var.get())
        self.client_to_search = client_to_search

        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.dashboard = CDashBoardCreateFacture.DashBoardCreateFacture(self, self.client_to_search)
        self.buttons = CButtonsCreateFacture.ButtonsCreateFacture(self, self.dashboard, self)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

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
        self.buttons.button1.config(text=_('Create Invoice'))
        self.buttons.button2.config(text=_('Quit'))