import tkinter as tk
from tkinter import messagebox
import gettext
_=gettext.gettext
from Classes.DAO.Dao_devis import Dao_devis
from Classes.Frame.Frame_Change_Devis import Frame_Change_Devis

class ButtonsSearchDevis(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de recherche de devis
    '''
    def __init__(self, master=None, dash_board=None, top_level=None, language_var=None):
        '''
        Constructeur de la classe ButtonsSearchDevis
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.language_var = language_var
        self.pack()
        self.button1 = tk.Button(self, text=_('Search'), command=self.search)
        self.button1.pack(pady=5)
        self.button_change = tk.Button(self, text=_('Change'), command=self.change, state='disabled')
        self.button_change.pack(pady=5)
        self.button_send = tk.Button(self, text=_('Send'), command=self.send, state='disabled')
        self.button_send.pack(pady=5)
        self.button_valider = tk.Button(self, text=_('Validate'), command=self.valider, state='disabled')
        self.button_valider.pack(pady=5)
        self.button_supprimer = tk.Button(self, text=_('Supprimer'), command=self.supprimer, state='disabled')
        self.button_supprimer.pack(pady=5)
        self.button_quitter = tk.Button(self, text=_('Quitter'), command=self.quitter)
        self.button_quitter.pack(pady=5)

        self.facture_to_search = None

    def search(self):
        '''
        Méthode qui permet de rechercher un devis
        '''
        numero = self.dash_board.entry_numero.get()
        # Rechercher le devis dans la base de données
        # Remplacer cette ligne par votre propre logique de recherche de devis
        devis = Dao_devis().get(numero)
        if devis is None:
            messagebox.showinfo(_('Quotation not found'), _('Quotation not found'))
        else:
            self.devis_to_search = devis
            messagebox.showinfo(_('Quotation found'), _('Quotation found'))
            self.button_change.config(state='normal')
            self.button_send.config(state='normal')
            self.button_valider.config(state='normal')
            self.button_supprimer.config(state='normal')

    def change(self):
        '''
        Méthode qui permet d'afficher le devis à modifier
        '''
        Frame_Change_Devis(self, self.language_var, self.devis_to_search[0][10])

    def send(self):
        '''
        Méthode qui permet d'envoyer le devis choisi
        '''
        if self.devis_to_search is not None:
            Dao_devis.send(self.devis_to_search[0][10])
            messagebox.showinfo(_('Quotation sent'), _('Quotation sent'))
            self.button_send.config(state='disabled')

    def valider(self):
        '''
        Méthode qui permet de valider le devis choisi
        '''
        if self.devis_to_search is not None:
            Dao_devis.validate(self.devis_to_search[0][10])

            messagebox.showinfo(_('Quotation validated'), _('Quotation validated'))
            self.button_valider.config(state='disabled')

    def supprimer(self):
        '''
        Méthode qui permet de supprimer le devis choisi
        '''
        if self.devis_to_search is not None:
            Dao_devis().delete(self.devis_to_search[0][10])
            messagebox.showinfo(_('Quotation deleted'), _('Quotation deleted'))
            self.button_change.config(state='disabled')

    def quitter(self):
        '''
        Méthode qui permet de quitter la fenêtre de recherche de devis
        '''
        self.top_level.destroy()