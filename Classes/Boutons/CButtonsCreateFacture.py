import tkinter as tk
import sqlite3
import gettext
from tkinter import messagebox
from Classes.DAO.Dao_facture import Dao_facture
from Classes.DAO.Dao_client import Dao_client
from Classes.Metiers.Facture import Facture

_=gettext.gettext

class ButtonsCreateFacture(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de création de facture
    '''
    def __init__(self, master=None, dash_board=None, top_level=None):
        '''
        Constructeur de la classe ButtonsCreateFacture
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.pack()
        self.button1 = tk.Button(self, text=_('Create Invoice'), command=self.create_Facture)
        self.button1.pack(padx=5)
        self.button2 = tk.Button(self, text=_('Back'), command=self.back_to_frame_wel)
        self.button2.pack(padx=5)

    def create_Facture(self):
        '''
        Méthode qui permet de créer une facture
        '''
        # On récupère les informations de la facture
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
        id_client = Dao_client.get_id(nom_client, email_client)

        # Vérifier que tous les champs nécessaires sont remplis
        if nom_facture == '' or nom_entreprise == '' or email_entreprise == '' or adresse_entreprise == '' or telephone_entreprise == '' or nom_client == '' or email_client == '' or adresse_client == '' or telephone_client == '' or numero_facture == '' or date == '':
            messagebox.showerror(_('Error'), _('Please fill all fields'))
            return
        
        # On vérifie si la facture existe déjà, on évite les doublons, on utilise une contrainte d'unicité dans la base de données
        new_facture = Facture(nom_facture, nom_entreprise, email_entreprise, adresse_entreprise, telephone_entreprise, nom_client, email_client, adresse_client, telephone_client, numero_facture, date, condition, description, prix_unitaire, quantite, montant, sous_total, tva, total, solde_du, id_client)
        try:
            Dao_facture.save(new_facture)
            messagebox.showinfo(_('Information'), _('Invoice created successfully'))
            self.dash_board.destroy()
            self.top_level.destroy()
        except sqlite3.IntegrityError:
            messagebox.showerror(_('Error'), _('Invoice already exists'))
            return

    def back_to_frame_wel(self):
        '''
        Méthode qui permet de revenir à la fenêtre de bienvenue en supprimant le frame de création de facture et en recréant le frame de bienvenue
        '''
        self.top_level.destroy()