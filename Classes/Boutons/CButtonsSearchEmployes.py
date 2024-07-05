import tkinter as tk
from tkinter import messagebox
import gettext
_=gettext.gettext
from Classes.Metiers import Employes

class ButtonsSearchEmployes(tk.Frame):
    '''
    Classe qui crée les boutons de la fenêtre de recherche des employés
    '''
    def __init__(self, master=None, dash_board=None, frame=None):
        '''
        Constructeur de la classe ButtonsSearchEmployes
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.frame = frame
        self.pack()
        self.button1 = tk.Button(self, text=_('Search'), command=self.search)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Back'), command=self.retour)
        self.button2.pack(pady=5)

        self.employe_label = tk.Label(self, text='')
        self.employe_label.pack(pady=5)

        self.employe_to_search = None


    def search(self):
        '''
        Méthode qui permet de rechercher un employé
        '''
        nom = self.dash_board.entry_nom.get()
        prenom = self.dash_board.entry_prenom.get()
        # Rechercher l'employé dans la base de données
        # Remplacer cette ligne par votre propre logique de recherche d'employé
        employe = Employes.Employes.get(nom, prenom)
        if employe is None:
            messagebox.showinfo(_('Employee not found'), _('Employee not found'))
        else:
            messagebox.showinfo(_('Employee found'), _('Employee found'))

    def retour(self):
        '''
        Méthode qui permet de revenir à la fenêtre précédente
        '''
        self.frame.destroy()
        