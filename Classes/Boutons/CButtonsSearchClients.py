import tkinter as tk
from tkinter.filedialog import *
from Classes.DAO import Dao_client
import xml.etree.ElementTree as ET
import gettext
_=gettext.gettext
from Classes.Frame.Frame_History_Facture_Devis import Frame_History_Facture_Devis

class ButtonsSearchClients(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de recherche des clients
    '''
    def __init__(self, master=None, dash_board=None, frame=None, language_var=None):
        '''
        Constructeur de la classe ButtonsSearchClients
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.frame = frame
        self.language_var = language_var
        self.pack()
        self.button = tk.Button(self, text=_('Search'), command=self.search)
        self.button.pack(pady=5)
        self.button_facture_devis = tk.Button(self, text=_('Invoice/Quotation'), command=self.facture_devis, state='disabled')
        self.button_facture_devis.pack(pady=5)
        self.button_export = tk.Button(self, text=_('Export'), command=self.export, state='disabled')
        self.button_export.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Back'), command=self.retour)
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
            self.button_facture_devis.config(state='normal')
            self.button_export.config(state='normal')

    def facture_devis(self):
        '''
        Méthode qui affiche la liste des factures et devis du client
        '''
        Frame_History_Facture_Devis(self.master, client=self.client_to_search, language_var=self.master.language_var)
        

    def export(self):
        '''
        Méthode qui permet d'exporter les informations du client dans un fichier txt ou xml
        '''
        filename = asksaveasfilename(initialdir="./Export", title="Exporter le client", filetypes=[("Fichiers texte", "*.txt"), ("Fichiers xml", "*.xml")])
        if filename:
            if filename.endswith('.txt'):
                with open(filename, 'w') as file:
                    file.write(f'Nom: {self.client_to_search[0][1]}\n')
                    file.write(f'Prénom: {self.client_to_search[0][2]}\n')
                    file.write(f'Téléphone: {self.client_to_search[0][3]}\n')
                    file.write(f'Email: {self.client_to_search[0][4]}\n')
                    file.write(f'Adresse: {self.client_to_search[0][5]}\n')
                    file.write(f'Commentaire: {self.client_to_search[0][6]}\n')
                    self.client_label1.config(text=f'Client exporté')
            elif filename.endswith('.xml'):
                root = ET.Element('client')
                nom = ET.SubElement(root, 'nom')
                nom.text = self.client_to_search[0][1]
                prenom = ET.SubElement(root, 'prenom')
                prenom.text = self.client_to_search[0][2]
                telephone = ET.SubElement(root, 'telephone')
                telephone.text = self.client_to_search[0][3]
                email = ET.SubElement(root, 'email')
                email.text = self.client_to_search[0][4]
                adresse = ET.SubElement(root, 'adresse')
                adresse.text = self.client_to_search[0][5]
                commentaire = ET.SubElement(root, 'commentaire')
                commentaire.text = self.client_to_search[0][6]
                tree = ET.ElementTree(root)
                tree.write(filename)
                self.client_label1.config(text=_('Client exported'))
        
    def retour(self):
        '''
        Méthode qui permet de retourner à la fenêtre principale
        '''
        self.frame.destroy()