import sqlite3
import tkinter as tk
from tkinter import messagebox
import gettext

_=gettext.gettext
from Classes.Metiers import PersonneFactory
from Classes.DAO import Dao_employe

class ButtonsCreateEmployes(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de création d'employés
    '''
    def __init__(self, master=None, dash_board=None, top_level=None):
        '''
        Constructeur de la classe ButtonsCreateEmployes
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.top_level = top_level
        self.pack()
        self.button1 = tk.Button(self, text='Create', command=self.create_employe)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text='Cancel', command=self.cancel_employe)
        self.button2.pack(pady=5)

    def create_employe(self):
        '''
        Méthode qui crée un employé
        '''
        # On récupère les informations de l'employé
        nom = self.dash_board.entry_nom.get()
        prenom = self.dash_board.entry_prenom.get()
        telephone = self.dash_board.entry_telephone.get()
        email = self.dash_board.entry_email.get()

        # Vérifier que tous les champs nécessaires sont remplis
        if nom == '' or prenom == '' or telephone == '' or email == '':
            messagebox.showerror(_('Error'), _('Please fill all fields'))
            return
        personneFactory = PersonneFactory.PersonneFactory()

        # En vérifiant si l'emplloyé existe déjà, on évite les doublons, on utilise une contrainte d'unicité dans la base de données
        try:
            new_employe = personneFactory.create_personne('employe', nom, prenom, telephone, email)
            if new_employe is None:
                messagebox.showerror(_('Error'), _('Employee already exists'))
            else:
                Dao_employe.Dao_employe.save(new_employe)
                messagebox.showinfo(_('Information'), _('Employee created'))
                self.dash_board.destroy()
                self.top_level.destroy()
                
        # On intercepte l'erreur d'intégrité pour afficher un message d'erreur
        except sqlite3.IntegrityError:
            messagebox.showerror(_('Error'), _('Employee already exists'))

    def cancel_employe(self):
        '''
        Méthode qui annule la création d'un employé
        '''
        self.dash_board.destroy()
        self.top_level.destroy()