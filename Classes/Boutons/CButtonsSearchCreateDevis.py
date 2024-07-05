import tkinter as tk
import gettext
_=gettext.gettext
from Classes.DAO import Dao_client
from Classes.Frame import Frame_Create_Devis

class ButtonsSearchCreateDevis(tk.Frame):
    '''
    Classe qui crée les boutons pour la recherche et la création de devis
    '''
    def __init__(self, master=None, dash_board=None, top_level=None):
        '''
        Constructeur de la classe ButtonsSearchCreateClients
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.pack()
        self.button1 = tk.Button(self, text=_('Search'), command=self.search)
        self.button1.pack(pady=5)
        self.button_confirm = tk.Button(self, text=_('Confirm'), command=self.confirm, state='disabled')
        self.button_confirm.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Back'), command=self.back)
        self.button2.pack(pady=5)

        self.client_label1 = tk.Label(self, text='')
        self.client_label1.pack(pady=5)

        self.client_to_search = None

        
    def search(self):
        '''
        Méthode qui permet de rechercher un client
        '''
        nom = self.dash_board.entry_nom.get()
        prenom = self.dash_board.entry_prenom.get()
        # Rechercher le client dans la base de données
        # Remplacer cette ligne par votre propre logique de recherche de client
        client = Dao_client.Dao_client.get(nom, prenom)
        if client is None:
            self.client_label1.config(text=_('Client not found'))
        else:
            self.client_to_search = client
            self.client_label1.config(text=_('Client found'))
            self.button_confirm.config(state='normal')

    def confirm(self):
        '''
        Méthode qui permet de créer une facture ou un devis
        '''
        Frame_Create_Devis.Frame_Create_Devis(self.client_to_search, self.master, self.master.language_var)
        
    def back(self):
        '''
        Méthode qui permet de retourner à la fenêtre principale
        '''
        self.top_level.destroy()