import tkinter as tk
from tkinter import ttk
import gettext
import sqlite3
from PIL import Image, ImageTk # type: ignore
from io import BytesIO
_=gettext.gettext
from Classes.DAO.Dao_devis import Dao_devis

class DashBoardChangeDevis(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de changement de devis
    '''
    def __init__(self, master=None, numero_devis=None):
        '''
        Constructeur de la classe DashBoardChangeDevis
        '''
        super().__init__(master)
        self.master = master
        self.numero_devis = numero_devis
        self.pack()
        
        self.devis_to_change = Dao_devis.get(self.numero_devis)

        # Récupérer l'image du logo
        conn = sqlite3.connect('Bdd/quit.db')
        c = conn.cursor()
        c.execute("SELECT logo FROM logo LIMIT 1")
        logo_data = c.fetchone()[0]

        # Convertir les données binaires en image
        logo_image = Image.open(BytesIO(logo_data))

        logo_image = logo_image.resize((200, 200), Image.BICUBIC)

        # Convertir l'image PIL en image Tkinter
        logo_image_tk = ImageTk.PhotoImage(logo_image)

        # Créer le label avec l'image
        logo_label = tk.Label(self, image=logo_image_tk)
        logo_label.image = logo_image_tk  # Garder une référence à l'image
        logo_label.grid(row=0, column=4, rowspan=10, padx=5, sticky='NE')

        # Créer les labels et les champs de saisie

        self.entry_nom_devis = tk.Entry(self, font=('Arial', 14))
        self.entry_nom_devis.insert(0, self.devis_to_change[0][1])
        self.entry_nom_devis.config(state='readonly')
        self.entry_nom_devis.grid(row=0, column=0, pady=5)
        
        self.label = tk.Label(self, text='De', font=('Arial', 14, 'bold'))
        self.label.grid(row=1, column=0, pady=5)

        self.label1 = tk.Label(self, text='Company name')
        self.label1.grid(row=2, column=0, pady=5)
        self.entry_nom_entreprise = tk.Entry(self)
        self.entry_nom_entreprise.insert(0, self.devis_to_change[0][2])
        self.entry_nom_entreprise.grid(row=2, column=1, pady=5)

        self.label2 = tk.Label(self, text='Company Email')
        self.label2.grid(row=3, column=0, pady=5)
        self.entry_email_entreprise = tk.Entry(self)
        self.entry_email_entreprise.insert(0, self.devis_to_change[0][3])
        self.entry_email_entreprise.grid(row=3, column=1, pady=5)

        self.label3 = tk.Label(self, text='Company Address')
        self.label3.grid(row=4, column=0, pady=5)
        self.entry_adresse_entreprise = tk.Entry(self)
        self.entry_adresse_entreprise.insert(0, self.devis_to_change[0][4])
        self.entry_adresse_entreprise.grid(row=4, column=1, pady=5)

        self.label4 = tk.Label(self, text='Company phone')
        self.label4.grid(row=5, column=0, pady=5)
        self.entry_telephone_entreprise = tk.Entry(self)
        self.entry_telephone_entreprise.insert(0, self.devis_to_change[0][5])
        self.entry_telephone_entreprise.grid(row=5, column=1, pady=5)

        self.label5 = tk.Label(self, text='Billing Address', font=('Arial', 14, 'bold'))
        self.label5.grid(row=1, column=2, pady=5)

        self.label6 = tk.Label(self, text='Client Name')
        self.label6.grid(row=2, column=2, pady=5)
        self.entry_nom_client = tk.Entry(self)
        self.entry_nom_client.insert(0, self.devis_to_change[0][6])
        self.entry_nom_client.grid(row=2, column=3, pady=5)

        self.label7 = tk.Label(self, text='Client Email')
        self.label7.grid(row=3, column=2, pady=5)
        self.entry_email_client = tk.Entry(self)
        self.entry_email_client.insert(0, self.devis_to_change[0][7])
        self.entry_email_client.grid(row=3, column=3, pady=5)

        self.label8 = tk.Label(self, text='Client Address')
        self.label8.grid(row=4, column=2, pady=5)
        self.entry_adresse_client = tk.Entry(self)
        self.entry_adresse_client.insert(0, self.devis_to_change[0][8])
        self.entry_adresse_client.grid(row=4, column=3, pady=5)
           
        self.label9 = tk.Label(self, text='Client Phone')
        self.label9.grid(row=5, column=2, pady=5)
        self.entry_telephone_client = tk.Entry(self)
        self.entry_telephone_client.insert(0, self.devis_to_change[0][9])
        self.entry_telephone_client.grid(row=5, column=3, pady=5)

        # Add a black separation line
        separator = tk.Frame(self, height=2, bg='black')
        separator.grid(row=7, columnspan=5, pady=10, sticky='we')

        self.label10 = tk.Label(self, text='Devis Number')
        self.label10.grid(row=8, column=0, pady=5)
        self.entry_numero_devis = tk.Entry(self)
        self.entry_numero_devis.insert(0, self.devis_to_change[0][10])
        self.entry_numero_devis.config(state='readonly')
        self.entry_numero_devis.grid(row=8, column=1, pady=5)

        self.label11 = tk.Label(self, text='Devis Date')
        self.label11.grid(row=9, column=0, pady=5)
        self.entry_date = tk.Entry(self)
        self.entry_date.insert(0, self.devis_to_change[0][11])
        self.entry_date.grid(row=9, column=1, pady=5)

        separator2 = tk.Frame(self, height=2, bg='black')
        separator2.grid(row=11, columnspan=5, pady=10, sticky='we')

        self.entry_description = tk.Entry(self, font=('Arial', 14))
        self.entry_description.insert(0, self.devis_to_change[0][12])
        self.entry_description.grid(row=12, column=0, pady=5)

        self.entry_prix_unitaire = tk.Entry(self, font=('Arial', 14))
        self.entry_prix_unitaire.insert(0, self.devis_to_change[0][13])
        self.entry_prix_unitaire.grid(row=12, column=1, pady=5)

        self.entry_quantite = tk.Entry(self, font=('Arial', 14))
        self.entry_quantite.insert(0, self.devis_to_change[0][14])
        self.entry_quantite.grid(row=12, column=2, pady=5)

        self.montant = tk.StringVar()
        self.montant.set(self.devis_to_change[0][15])
        self.label_montant = tk.Label(self, textvariable=self.montant, font=('Arial', 14))
        self.label_montant.grid(row=12, column=3, pady=5)

        self.entry_prix_unitaire.bind("<KeyRelease>", self.update_montant)
        self.entry_quantite.bind("<KeyRelease>", self.update_montant)

        self.label12 = tk.Label(self, text='Subtotal')
        self.label12.grid(row=13, column=2, pady=5)
        self.sous_total = tk.StringVar()
        self.sous_total.set(self.devis_to_change[0][16])
        self.label_sous_total = tk.Label(self, textvariable=self.sous_total, font=('Arial', 14))
        self.label_sous_total.grid(row=13, column=3, pady=5)

        self.label13 = tk.Label(self, text='VAT (20%)')
        self.label13.grid(row=14, column=2, pady=5)
        self.tva = tk.StringVar()
        self.tva.set(self.devis_to_change[0][17])
        self.label_tva = tk.Label(self, textvariable=self.tva, font=('Arial', 14))
        self.label_tva.grid(row=14, column=3, pady=5)

        self.label14 = tk.Label(self, text='Total')
        self.label14.grid(row=15, column=2, pady=5)
        self.total = tk.StringVar()
        self.total.set(self.devis_to_change[0][18])
        self.label_total = tk.Label(self, textvariable=self.total, font=('Arial', 14))
        self.label_total.grid(row=15, column=3, pady=5)

    def update_montant(self, event):
        try:
            prix_unitaire = float(self.entry_prix_unitaire.get())
            quantite = int(self.entry_quantite.get())
        except ValueError:
            return
        
        montant = prix_unitaire * quantite
        self.montant.set("{:.2f} €".format(montant))
        self.sous_total.set("{:.2f} €".format(montant))
        tva = montant * 0.2
        self.tva.set("{:.2f} €".format(tva))
        total = montant + tva
        self.total.set("{:.2f} €".format(total))