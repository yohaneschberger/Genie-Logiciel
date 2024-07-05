import tkinter as tk
from tkinter import messagebox
import gettext

_=gettext.gettext
from Classes.DAO import Dao_client

class ButtonsDeleteClients(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de suppression des clients
    '''
    def __init__(self, master=None, dash_board=None, frame=None):
        '''
        Constructeur de la classe ButtonsDeleteClients
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.frame = frame
        self.pack()
        self.button1 = tk.Button(self, text=_('Search'), command=self.search_client)
        self.button1.pack(pady=5)
        self.button_delete = tk.Button(self, text=_('Delete'), command=self.delete_client, state='disabled')
        self.button_delete.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Quit'), command=self.quit)
        self.button2.pack(pady=5)

        self.client_label = tk.Label(self, text='')
        self.client_label.pack(pady=5)

        self.client_to_delete = None

    def search_client(self):
        nom = self.dash_board.entry_nom.get()
        prenom = self.dash_board.entry_prenom.get()
        # Rechercher le client dans la base de données
        # Remplacer cette ligne par votre propre logique de recherche de client
        client = Dao_client.Dao_client.search(nom, prenom)
        if client is None:
            self.client_label.config(text=_('Client not found'))
        else:
            self.client_to_delete = client
            self.client_label.config(text=_('Client found and ready to be deleted'))
            self.button_delete.config(state='normal')

    def delete_client(self):
        '''
        Méthode qui supprime un client
        '''
        if self.client_to_delete is None:
            messagebox.showerror(_("Error"), _("Client not found"))
        else:
            # Supprimer le client de la base de données
            # Remplacer cette ligne par votre propre logique de suppression de client
            nom = self.client_to_delete[0][1]
            prenom = self.client_to_delete[0][2]
            Dao_client.Dao_client.delete(nom, prenom)
            self.client_to_delete = None
            self.client_label.config(text=_('Client deleted'))
            self.button_delete.config(state='disabled')

    def quit(self):
        '''
        Méthode qui ferme la fenêtre
        '''
        self.frame.destroy()