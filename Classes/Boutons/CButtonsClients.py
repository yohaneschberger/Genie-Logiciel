import tkinter as tk
import gettext

_=gettext.gettext
from Classes.Frame import Frame_Welcome
from Classes.Frame import Frame_Create_Clients
from Classes.Frame import Frame_Delete_Clients
from Classes.Frame import Frame_Search_Clients

class ButtonsClients(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre des clients
    '''
    def __init__(self, master=None, dash_board=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe ButtonsClients
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.is_admin = is_admin
        self.language_var = language_var
        self.pack()
        self.button1 = tk.Button(self, text=_('Create Client'), command=self.create_client)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Search Client'), command=self.search_client)
        self.button2.pack(pady=5)
        self.button3 = tk.Button(self, text=_('Delete Client'), command=self.delete_client)
        self.button3.pack(pady=5)
        self.button4 = tk.Button(self, text=_('Back'), command=self.back_to_frame_wel)
        self.button4.pack(pady=5)

    def create_client(self):
        '''
        Méthode qui permet de créer un client
        '''
        Frame_Create_Clients.Frame_Create_Clients(self.master, language_var=self.master.language_var)

    def search_client(self):
        '''
        Méthode qui permet de rechercher un client
        '''
        Frame_Search_Clients.Frame_Search_Clients(self.master, language_var=self.master.language_var)

    def delete_client(self):
        '''
        Méthode qui permet de supprimer un client
        '''
        Frame_Delete_Clients.Frame_Delete_Clients(self.master, language_var=self.master.language_var)

    def back_to_frame_wel(self):
        '''
        Méthode qui permet de revenir à la fenêtre de bienvenue en supprimant le frame des clients et en recréant le frame de bienvenue
        '''
        self.dash_board.destroy()
        self.destroy()
        self.master.pack()
        if self.is_admin:
            Frame_Welcome.Frame_Welcome(self.master, is_admin=True, language_var=self.master.language_var)
        else:
            Frame_Welcome.Frame_Welcome(self.master, language_var=self.master.language_var)