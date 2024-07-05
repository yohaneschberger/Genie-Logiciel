import tkinter as tk
from tkinter import messagebox
import gettext

_=gettext.gettext
from Classes.DAO import Dao_employe

class ButtonsDeleteEmployes(tk.Frame):
    '''
    Classe qui crée les boutons pour supprimer un employé
    '''
    def __init__(self, master=None, dash_board=None, frame=None):
        '''
        Constructeur de la classe ButtonsDeleteEmployes
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.frame = frame
        self.pack()
        self.button = tk.Button(self, text=_('Search'), command=self.search_employe)
        self.button.pack(pady=5)
        self.button_delete = tk.Button(self, text=_('Delete'), command=self.delete_employe, state='disabled')
        self.button_delete.pack(pady=5)
        self.button_quit = tk.Button(self, text=_('Quit'), command=self.quit)
        self.button_quit.pack(pady=5)

        self.employe_label = tk.Label(self, text='')
        self.employe_label.pack(pady=5)

        self.employe_to_delete = None

    def search_employe(self):
        '''
        Méthode qui permet de supprimer un employé
        '''
        nom = self.dash_board.entry_nom.get()
        prenom = self.dash_board.entry_prenom.get()
        # Rechercher l'employe dans la base de données
        employe = Dao_employe.Dao_employe.get(nom, prenom)
        if employe is None:
            self.employe_label.config(text=_('Client not found'))
        else:
            self.employe_to_delete = employe
            self.employe_label.config(text=_('Client found and ready to be deleted'))
            self.button_delete.config(state='normal')
        
    def delete_employe(self):
        '''
        Méthode qui permet de supprimer un employé
        '''
        if self.employe_to_delete is None:
            messagebox.showerror(_("Error"), _("Client not found"))
        else:
            # Supprimer le client de la base de données
            # Remplacer cette ligne par votre propre logique de suppression de client
            nom = self.employe_to_delete[0][1]
            prenom = self.employe_to_delete[0][2]
            Dao_employe.Dao_employe.delete(nom, prenom)
            self.employe_to_delete = None
            self.employe_label.config(text=_('Client deleted'))
            self.button_delete.config(state='disabled')

    def quit(self):
        '''
        Méthode qui permet d'annuler la suppression d'un employé
        '''
        self.frame.destroy()