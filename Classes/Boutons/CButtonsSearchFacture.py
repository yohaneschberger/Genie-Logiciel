import tkinter as tk
from tkinter import messagebox
import gettext
_=gettext.gettext
from Classes.DAO.Dao_facture import Dao_facture
from Classes.Frame.Frame_Change_Facture import Frame_Change_Facture

class CButtonsSearchFacture(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de recherche de facture
    '''
    def __init__(self, master=None, dash_board=None, top_level=None, language_var=None):
        '''
        Constructeur de la classe ButtonsSearchFacture
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.language_var = language_var
        self.pack()
        self.button = tk.Button(self, text=_('Search'), command=self.search)
        self.button.pack(pady=5)
        self.button_change = tk.Button(self, text=_('Change'), command=self.change, state='disabled')
        self.button_change.pack(pady=5)
        self.button_supprimer = tk.Button(self, text=_('Delete'), command=self.supprimer, state='disabled')
        self.button_supprimer.pack(pady=5)
        self.button_quitter = tk.Button(self, text=_('Quit'), command=self.quitter)
        self.button_quitter.pack(pady=5)
        self.label1 = tk.Label(self, text='')
        self.label1.pack(pady=5)
        self.facture_to_search = None

    def search(self):
        '''
        Méthode qui permet de rechercher une facture
        '''
        numero = self.dash_board.entry_numero.get()
        # Rechercher la facture dans la base de données
        # Remplacer cette ligne par votre propre logique de recherche de facture
        facture = Dao_facture.get(numero)
        if facture is None:
            messagebox.showinfo(_('Invoice not found'), _('Invoice not found'))
        else:
            self.facture_to_search = facture
            messagebox.showinfo(_('Invoice found'), _('Invoice found'))
            self.button_change.config(state='normal')
            self.button_supprimer.config(state='normal')

    def change(self):
        '''
        Méthode qui permet d'afficher la facture à modifier
        '''
        Frame_Change_Facture(self, language_var=self.master.language_var, numero_facture=self.facture_to_search[0][10])

    def supprimer(self):
        '''
        Méthode qui permet de supprimer la facture choisie
        '''
        if self.facture_to_search is not None:
            Dao_facture.delete(self.facture_to_search[0][10])
            messagebox.showinfo(_('Invoice deleted'), _('Invoice deleted'))
            self.button_change.config(state='disabled')
            self.button_supprimer.config(state='disabled')
            self.facture_to_search = None
        else:
            messagebox.showerror(_('Error'), _('Invoice not found'))

    def quitter(self):
        '''
        Méthode qui permet de quitter la fenêtre
        '''
        self.top_level.destroy()
