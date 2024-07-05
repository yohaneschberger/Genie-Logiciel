import tkinter as tk
from tkinter import messagebox
import gettext
_=gettext.gettext
from Classes.DAO.Dao_facture import Dao_facture
from Classes.Metiers.Facture import Facture


class ButtonsChangeFacture(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de changement de facture
    '''
    def __init__(self, master=None, dash_board=None, top_level=None):
        '''
        Constructeur de la classe ButtonsChangeFacture
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.pack()
        self.button_change = tk.Button(self, text=_('Change'), command=self.change)
        self.button_change.pack(pady=5)
        self.button_quitter = tk.Button(self, text=_('Quit'), command=self.quitter)
        self.button_quitter.pack(pady=5)
        self.label1 = tk.Label(self, text='')
        self.label1.pack(pady=5)
        self.facture_to_search = None

    def change(self):
        '''
        Méthode qui permet d'afficher le devis à modifier
        '''
        nom_facture = self.dash_board.entry_nom_facture.get()
        nom_entreprise = self.dash_board.entry_nom_entreprise.get()
        email_entreprise = self.dash_board.entry_email_entreprise.get()
        adresse_entreprise = self.dash_board.entry_adresse_entreprise.get()
        telephone_entreprise = self.dash_board.entry_telephone_entreprise.get()
        nom_client = self.dash_board.entry_nom_client.get()
        email_client = self.dash_board.entry_email_client.get()
        adresse_client = self.dash_board.entry_adresse_client.get()
        telephone_client = self.dash_board.entry_telephone_client.get()
        numero_facture = self.dash_board.entry_numero_facture.get()
        date = self.dash_board.entry_date.get()
        condition = self.dash_board.entry_conditions.get()
        description = self.dash_board.entry_description.get()
        prix_unitaire = self.dash_board.entry_prix_unitaire.get()
        quantite = self.dash_board.entry_quantite.get()
        montant = self.dash_board.montant.get()
        sous_total = self.dash_board.sous_total.get()
        tva = self.dash_board.tva.get()
        total = self.dash_board.total.get()
        solde_du = self.dash_board.solde_du.get()
        id_client = Dao_facture.get_id(nom_client, email_client)

        # Vérifier que tous les champs nécessaires sont remplis
        if nom_facture == '' or nom_entreprise == '' or email_entreprise == '' or adresse_entreprise == '' or telephone_entreprise == '' or nom_client == '' or email_client == '' or adresse_client == '' or telephone_client == '' or numero_facture == '' or date == '':
            messagebox.showerror(_('Error'), _('Please fill all fields'))
            return
        
        new_facture = Facture(
            nom_facture, nom_entreprise, email_entreprise, adresse_entreprise, telephone_entreprise, 
            nom_client, email_client, adresse_client, telephone_client, numero_facture, date, condition, 
            description, prix_unitaire, quantite, montant, sous_total, tva, total, solde_du, id_client
        )
        try:
            Dao_facture.change(new_facture)
            messagebox.showinfo(_('Success'), _('Quote changed successfully'))
            self.top_level.destroy()
        except Exception as e:
            messagebox.showerror(_('Error'), _('An error occurred'))
            print(e)

        

    def quitter(self):
        '''
        Méthode qui permet de quitter la fenêtre de recherche de devis
        '''
        self.top_level.destroy()