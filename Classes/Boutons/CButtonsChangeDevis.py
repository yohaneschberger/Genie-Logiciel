import tkinter as tk
from tkinter import messagebox
import gettext
_=gettext.gettext
from Classes.DAO.Dao_devis import Dao_devis
from Classes.Metiers.Devis import Devis

class ButtonsChangeDevis(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de changement de devis
    '''
    def __init__(self, master=None, dash_board=None, top_level=None):
        '''
        Constructeur de la classe ButtonsChangeDevis
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
        self.devis_to_search = None

    def change(self):
        '''
        Méthode qui permet d'afficher le devis à modifier
        '''
        nom_devis = self.dash_board.entry_nom_devis.get()
        nom_entreprise = self.dash_board.entry_nom_entreprise.get()
        email_entreprise = self.dash_board.entry_email_entreprise.get()
        adresse_entreprise = self.dash_board.entry_adresse_entreprise.get()
        telephone_entreprise = self.dash_board.entry_telephone_entreprise.get()
        nom_client = self.dash_board.entry_nom_client.get()
        email_client = self.dash_board.entry_email_client.get()
        adresse_client = self.dash_board.entry_adresse_client.get()
        telephone_client = self.dash_board.entry_telephone_client.get()
        numero_devis = self.dash_board.entry_numero_devis.get()
        date = self.dash_board.entry_date.get()
        description = self.dash_board.entry_description.get()
        prix_unitaire = self.dash_board.entry_prix_unitaire.get()
        quantite = self.dash_board.entry_quantite.get()
        montant = self.dash_board.montant.get()
        sous_total = self.dash_board.sous_total.get()
        tva = self.dash_board.tva.get()
        total = self.dash_board.total.get()
        id_client = Dao_devis.get_id(nom_client, email_client)

        # Vérifier que tous les champs nécessaires sont remplis
        if nom_devis == '' or nom_entreprise == '' or email_entreprise == '' or adresse_entreprise == '' or telephone_entreprise == '' or nom_client == '' or email_client == '' or adresse_client == '' or telephone_client == '' or numero_devis == '' or date == '':
            messagebox.showerror(_('Error'), _('Please fill all fields'))
            return
        
        new_devis = Devis(
            nom_devis=nom_devis, nom_entreprise=nom_entreprise, email_entreprise=email_entreprise, 
            adresse_entreprise=adresse_entreprise, telephone_entreprise=telephone_entreprise, nom_client=nom_client, 
            email_client=email_client, adresse_client=adresse_client, telephone_client=telephone_client, 
            numero_devis=numero_devis, date=date, description=description, prix_unitaire=prix_unitaire, 
            quantite=quantite, montant=montant, sous_total=sous_total, tva=tva, total=total, id_client=id_client
        )
        try:
            Dao_devis.change(new_devis)
            messagebox.showinfo(_('Success'), _('Quote changed successfully'))
            self.top_level.destroy()
        except Exception as e:
            messagebox.showerror(_('Error'), _('An error occurred'))
            print(e)

    def quitter(self):
        '''
        Méthode qui permet de quitter la fenêtre de changement de devis
        '''
        self.top_level.destroy()