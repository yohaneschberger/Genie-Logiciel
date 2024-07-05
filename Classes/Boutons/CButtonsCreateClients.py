import sqlite3
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import xml.etree.ElementTree as ET
import gettext

_=gettext.gettext
from Classes.Metiers import PersonneFactory
from Classes.DAO import Dao_client

class ButtonsCreateClients(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de création de clients
    '''
    def __init__(self, master=None, dash_board=None, top_level=None):
        '''
        Constructeur de la classe ButtonsCreateClients
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.pack()
        self.button1 = tk.Button(self, text=_('Create'), command=self.create_client)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Import Client'), command=self.import_client)
        self.button2.pack(pady=5)
        self.button3 = tk.Button(self, text=_('Cancel'), command=self.cancel)
        self.button3.pack(pady=5)
        
    def create_client(self):
        '''
        Méthode qui crée un client, l'ajoute à la base de données (table clients) et ferme la fenêtre de création de client
        '''
        # On récupère les informations du client
        nom = self.dash_board.entry_nom.get()
        prenom = self.dash_board.entry_prenom.get()
        telephone = self.dash_board.entry_telephone.get()
        email = self.dash_board.entry_email.get()
        adresse = self.dash_board.entry_adresse.get()
        commentaire = self.dash_board.entry_commentaire.get("1.0", tk.END)

        # Vérifier que tous les champs nécessaires sont remplis
        if nom == '' or prenom == '' or telephone == '' or email == '' or adresse == '':
            messagebox.showerror(_('Error'), _('Please fill all fields'))
            return
        personneFactory = PersonneFactory.PersonneFactory()

        # En vérifiant si le client existe déjà, on évite les doublons, on utilise une contrainte d'unicité dans la base de données
        try:
            new_client = personneFactory.create_personne('client', nom, prenom, telephone, email, adresse, commentaire)
            if new_client is None:
                messagebox.showerror(_('Error'), _('Client already exists'))
            else:
                Dao_client.Dao_client.save(new_client)
                messagebox.showinfo(_('Information'), _('Client created'))
                self.dash_board.destroy()
                self.top_level.destroy()
                
        # On intercepte l'erreur d'intégrité pour afficher un message d'erreur
        except sqlite3.IntegrityError:
            messagebox.showerror(_('Error'), _('Client already exists'))

    def import_client(self):
        '''
        Méthode qui importe un client depuis un fichier txt ou xml et remplit les champs de la fenêtre de création de client
        '''
        # On ouvre une boîte de dialogue pour choisir un fichier
        filename = askopenfilename(filetypes=[("all file", "*.*"),("txt file", "*.txt"),("xml file", "*.xml")])
        
        # On vérifie si le fichier est un fichier txt ou xml
        if filename.endswith('.txt'):
            with open(filename, 'r') as file:
                data = file.read()
                data = data.split('\n')
                for i in range(len(data)):
                    if i == 0:
                        self.dash_board.entry_nom.delete(0, tk.END)
                        self.dash_board.entry_nom.insert(0, data[i])
                    if i == 1:
                        self.dash_board.entry_prenom.delete(0, tk.END)
                        self.dash_board.entry_prenom.insert(0, data[i])
                    if i == 2:
                        self.dash_board.entry_telephone.delete(0, tk.END)
                        self.dash_board.entry_telephone.insert(0, data[i])
                    if i == 3:
                        self.dash_board.entry_email.delete(0, tk.END)
                        self.dash_board.entry_email.insert(0, data[i])
                    if i == 4:
                        self.dash_board.entry_adresse.delete(0, tk.END)
                        self.dash_board.entry_adresse.insert(0, data[i])
                    if i == 5:
                        self.dash_board.entry_commentaire.delete("1.0", tk.END)
                        self.dash_board.entry_commentaire.insert("1.0", data[i])
        elif filename.endswith('.xml'):
            tree = ET.parse(filename)
            root = tree.getroot()
            for child in root:
                if child.tag == 'nom':
                    self.dash_board.entry_nom.delete(0, tk.END)
                    self.dash_board.entry_nom.insert(0, child.text)
                if child.tag == 'prenom':
                    self.dash_board.entry_prenom.delete(0, tk.END)
                    self.dash_board.entry_prenom.insert(0, child.text)
                if child.tag == 'telephone':
                    self.dash_board.entry_telephone.delete(0, tk.END)
                    self.dash_board.entry_telephone.insert(0, child.text)
                if child.tag == 'email':
                    self.dash_board.entry_email.delete(0, tk.END)
                    self.dash_board.entry_email.insert(0, child.text)
                if child.tag == 'adresse':
                    self.dash_board.entry_adresse.delete(0, tk.END)
                    self.dash_board.entry_adresse.insert(0, child.text)
                if child.tag == 'commentaire':
                    self.dash_board.entry_commentaire.delete("1.0", tk.END)
                    self.dash_board.entry_commentaire.insert("1.0", child.text)

    def cancel(self):
        '''
        Méthode qui annule la création de client et ferme la fenêtre de création de client
        '''
        self.dash_board.destroy()
        self.top_level.destroy()