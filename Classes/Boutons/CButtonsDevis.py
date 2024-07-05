import tkinter as tk
import gettext
_=gettext.gettext
from Classes.Frame import Frame_Welcome
from Classes.Frame import Frame_Search_Create_Devis
from Classes.Frame import Frame_History_Devis
from Classes.Frame import Frame_Search_Devis

class ButtonsDevis(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de devis
    '''
    def __init__(self, master=None, dash_board=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe ButtonsDevis
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.is_admin = is_admin
        self.language_var = language_var
        self.pack()
        self.button1 = tk.Button(self, text=_('Search Quotation'), command=self.search_devis)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Quotations History'), command=self.history_devis)
        self.button2.pack(pady=5)
        self.button3 = tk.Button(self, text=_('Create Quotation'), command=self.create_devis)
        self.button3.pack(pady=5)
        self.button4 = tk.Button(self, text=_('Back'), command=self.back_to_frame_wel)
        self.button4.pack(pady=5)

    def search_devis(self):
        '''
        Méthode qui permet de rechercher un devis
        '''
        Frame_Search_Devis.Frame_Search_Devis(self.master, language_var=self.master.language_var)

    def history_devis(self):
        '''
        Méthode qui permet de voir l'historique des devis
        '''
        Frame_History_Devis.Frame_History_Devis(self.master, language_var=self.master.language_var)
        

    def create_devis(self):
        '''
        Méthode qui permet de créer un devis
        '''
        Frame_Search_Create_Devis.Frame_Search_Create_Devis(self.master, language_var=self.master.language_var)

    def back_to_frame_wel(self):
        '''
        Méthode qui permet de revenir à la fenêtre de bienvenue en supprimant le frame de devis et en recréant le frame de bienvenue
        '''
        self.dash_board.destroy()
        self.destroy()
        self.master.pack()
        if self.is_admin:
            Frame_Welcome.Frame_Welcome(self.master, is_admin=True, language_var=self.master.language_var)
        else:
            Frame_Welcome.Frame_Welcome(self.master, language_var=self.master.language_var)