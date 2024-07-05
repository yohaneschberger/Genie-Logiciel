import tkinter as tk
import sqlite3
from tkinter import messagebox
import gettext
_=gettext.gettext
from Classes.Metiers.Devis import Devis
from Classes.DAO.Dao_devis import Dao_devis
from Classes.DAO.Dao_client import Dao_client

class ButtonsCreateDevis(tk.Frame):
    '''
    Classe qui crée les boutons de la fenêtre de création de devis
    '''
    def __init__(self, master=None, dash_board=None, frame=None):
        '''
        Constructeur de la classe ButtonsCreateDevis
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.frame = frame
        self.pack()
        self.button1 = tk.Button(self, text=_('Create Quotation'), command=self.create_devis)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Quit'), command=self.back)
        self.button2.pack(pady=5)

    def create_devis(self):
        '''
        Méthode qui permet de créer un devis
        '''
        # On récupère les informations du devis
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
        id_client = Dao_client.get_id(nom_client, email_client)

        # Vérifier que tous les champs nécessaires sont remplis
        if nom_devis == '' or nom_entreprise == '' or email_entreprise == '' or adresse_entreprise == '' or telephone_entreprise == '' or nom_client == '' or email_client == '' or adresse_client == '' or telephone_client == '' or numero_devis == '' or date == '':
            messagebox.showerror(_('Error'), _('Please fill all fields'))
            return
        
        # Créer un devis
        new_devis = Devis(
            nom_devis, nom_entreprise, email_entreprise, adresse_entreprise, 
            telephone_entreprise, nom_client, email_client, adresse_client, 
            telephone_client, numero_devis, date, description, prix_unitaire, 
            quantite, montant, sous_total, tva, total, id_client
        )
        try:
            Dao_devis.save(new_devis)
            messagebox.showinfo(_('Info'), _('Quote created successfully'))
            self.back()
        except sqlite3.IntegrityError:
            messagebox.showerror(_('Error'), _('Bill already exists'))
            return


    def back(self):
        '''
        Méthode qui permet de revenir à la fenêtre principale
        '''
        self.frame.destroy()
        
