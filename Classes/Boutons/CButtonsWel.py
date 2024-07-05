import tkinter as tk
import gettext
_=gettext.gettext

from Classes.Frame import Frame_login
from Classes.Frame.Frame_Facture import Frame_Facture
from Classes.Frame.Frame_Devis import Frame_Devis
from Classes.Frame.Frame_Clients import Frame_Clients
from Classes.Frame.Frame_Employes import Frame_Employes
from Classes.Frame.Frame_Entreprise import Frame_Entreprise
from Classes.Frame import Frame_Welcome

class ButtonsWel(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de bienvenue
    '''
    def __init__(self, master=None, dash_board=None, is_admin=False):
        '''
        Constructeur de la classe ButtonsWel
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.is_admin = is_admin
        self.pack()

        # Barre de menu
        self.menu = tk.Menu(self.master.winfo_toplevel())
        self.menu.add_command(label='Home', command=self.go_to_frame_welcome)
        self.menu.add_command(label=_('Invoice'), command=self.go_to_frame_factures)
        self.menu.add_command(label=_('Quotation'), command=self.go_to_frame_devis)
        self.menu.add_command(label=_('Clients'), command=self.go_to_frame_clients)
        if is_admin:
            self.menu.add_command(label=_('Employes'), command=self.go_to_frame_employes)
            self.menu.add_command(label=_('Company'), command=self.go_to_frame_company)
        self.master.winfo_toplevel().config(menu=self.menu)

        self.button1 = tk.Button(self, text=_('Invoice'), command=self.go_to_frame_factures)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Quotation'), command=self.go_to_frame_devis)
        self.button2.pack(pady=5)
        self.button3 = tk.Button(self, text=_('Clients'), command=self.go_to_frame_clients)
        self.button3.pack(pady=5)
        if is_admin:
            self.button4 = tk.Button(self, text=_('Employes'), command=self.go_to_frame_employes)
            self.button4.pack(pady=5)
            self.button5 = tk.Button(self, text=_('Manage Company'), command=self.go_to_frame_company)
            self.button5.pack(pady=5)
        self.button6 = tk.Button(self, text=_('Logout'), command=self.back_to_frame_login)
        self.button6.pack(pady=5)

    def update_menu_labels(self, _):
        '''
        Méthode qui permet de traduire les textes de la fenêtre
        '''
        self.menu = tk.Menu(self.master.winfo_toplevel())
        self.master.winfo_toplevel().config(menu=self.menu)
        self.menu.add_command(label='Home', command=self.go_to_frame_welcome)
        self.menu.add_command(label=_('Invoice'), command=self.go_to_frame_factures)
        self.menu.add_command(label=_('Quotation'), command=self.go_to_frame_devis)
        self.menu.add_command(label=_('Clients'), command=self.go_to_frame_clients)
        if self.is_admin:
            self.menu.add_command(label=_('Employes'), command=self.go_to_frame_employes)
            self.menu.add_command(label=_('Company'), command=self.go_to_frame_company)
               

    def go_to_frame_welcome(self):
        '''
        Méthode qui permet d'afficher le frame de bienvenue
        '''
        for widget in self.master.winfo_children():
            widget.destroy()
        Frame_Welcome.Frame_Welcome(self.master, self.is_admin, self.master.language_var)

    def go_to_frame_factures(self):
        '''
        Méthode qui permet d'afficher le frame des factures
        '''
        for widget in self.master.winfo_children(): # On supprime tous les widgets de la fenêtre
            widget.destroy()
        Frame_Facture(self.master, self.is_admin, self.master.language_var)

    def go_to_frame_devis(self):
        '''
        Méthode qui permet d'afficher le frame des devis
        '''
        for widget in self.master.winfo_children():
            widget.destroy()
        Frame_Devis(self.master, self.is_admin, self.master.language_var)

    def go_to_frame_clients(self):
        '''
        Méthode qui permet d'afficher le frame des clients
        '''
        for widget in self.master.winfo_children():
            widget.destroy()
        Frame_Clients(self.master, self.is_admin, self.master.language_var)

    def go_to_frame_employes(self):
        '''
        Méthode qui permet d'afficher le frame des employés
        '''
        for widget in self.master.winfo_children():
            widget.destroy()
        Frame_Employes(self.master, self.is_admin, self.master.language_var)

    def go_to_frame_company(self):
        '''
        Méthode qui permet de gérer les informations de l'entreprise
        '''
        for widget in self.master.winfo_children():
            widget.destroy()
        Frame_Entreprise(self.master, self.is_admin, self.master.language_var)

    def back_to_frame_login(self):
        '''
        Méthode qui permet de revenir à la fenêtre de login en supprimant le frame d'accueil et en recréant le frame de login
        '''
        self.dash_board.destroy()
        self.menu.destroy()
        self.destroy()
        self.master.pack()
        Frame_login.Frame_login(master=self.master, language_var=self.master.language_var)
        