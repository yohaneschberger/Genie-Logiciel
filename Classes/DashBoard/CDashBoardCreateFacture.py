import sqlite3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # type: ignore
from io import BytesIO
from Classes.DAO.Dao_entreprise import Dao_entreprise
from Classes.DAO.Dao_facture import Dao_facture

class DashBoardCreateFacture(tk.Frame):
    '''
    Classe qui crée le tableau de bord pour la création de facture
    '''
    def __init__(self, master=None, client_to_search=None):
        '''
        Constructeur de la classe DashBoardCreateFacture
        '''
        super().__init__(master)
        self.master = master
        self.client_to_search = client_to_search
        self.pack()
        self.entreprise = Dao_entreprise.get()[0]

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

        self.entry_nom_facture = tk.Entry(self, font=('Arial', 14))
        self.entry_nom_facture.insert(0, 'Facture')
        self.entry_nom_facture.grid(row=0, column=0, pady=5)
        
        self.label = tk.Label(self, text='De', font=('Arial', 14, 'bold'))
        self.label.grid(row=1, column=0, pady=5)

        self.label1 = tk.Label(self, text='Company Name')
        self.label1.grid(row=2, column=0, pady=5)
        self.entry_nom_entreprise = tk.Entry(self)
        self.entry_nom_entreprise.insert(0, self.entreprise[1])
        self.entry_nom_entreprise.grid(row=2, column=1, pady=5)

        self.label2 = tk.Label(self, text='Company Email')
        self.label2.grid(row=3, column=0, pady=5)
        self.entry_email_entreprise = tk.Entry(self)
        self.entry_email_entreprise.insert(0, self.entreprise[3])
        self.entry_email_entreprise.grid(row=3, column=1, pady=5)

        self.label3 = tk.Label(self, text='Company Address')
        self.label3.grid(row=4, column=0, pady=5)
        self.entry_adresse_entreprise = tk.Entry(self)
        self.entry_adresse_entreprise.insert(0, self.entreprise[2])
        self.entry_adresse_entreprise.grid(row=4, column=1, pady=5)

        self.label4 = tk.Label(self, text='Company Contact')
        self.label4.grid(row=5, column=0, pady=5)
        self.entry_telephone_entreprise = tk.Entry(self)
        self.entry_telephone_entreprise.insert(0, self.entreprise[4])
        self.entry_telephone_entreprise.grid(row=5, column=1, pady=5)

        self.label5 = tk.Label(self, text='Billing Address', font=('Arial', 14, 'bold'))
        self.label5.grid(row=1, column=2, pady=5)

        self.label6 = tk.Label(self, text='Client Name')
        self.label6.grid(row=2, column=2, pady=5)
        self.entry_nom_client = tk.Entry(self)
        self.entry_nom_client.insert(0, self.client_to_search[0][1])
        self.entry_nom_client.grid(row=2, column=3, pady=5)

        self.label7 = tk.Label(self, text='Client Email')
        self.label7.grid(row=3, column=2, pady=5)
        self.entry_email_client = tk.Entry(self)
        self.entry_email_client.insert(0, self.client_to_search[0][4])
        self.entry_email_client.grid(row=3, column=3, pady=5)

        self.label8 = tk.Label(self, text='Client Address')
        self.label8.grid(row=4, column=2, pady=5)
        self.entry_adresse_client = tk.Entry(self)
        self.entry_adresse_client.insert(0, self.client_to_search[0][5])
        self.entry_adresse_client.grid(row=4, column=3, pady=5)
           
        self.label9 = tk.Label(self, text='Client Phone')
        self.label9.grid(row=5, column=2, pady=5)
        self.entry_telephone_client = tk.Entry(self)
        self.entry_telephone_client.insert(0, self.client_to_search[0][3])
        self.entry_telephone_client.grid(row=5, column=3, pady=5)

        # Add a black separation line
        separator = tk.Frame(self, height=2, bg='black')
        separator.grid(row=7, columnspan=5, pady=10, sticky='we')

        self.label10 = tk.Label(self, text='Invoice Number')
        self.label10.grid(row=8, column=0, pady=5)
        self.entry_numero_facture = tk.Entry(self)
        self.entry_numero_facture.insert(0, "FAC{}".format(Dao_facture.get_next_id()))
        self.entry_numero_facture.grid(row=8, column=1, pady=5)

        self.label11 = tk.Label(self, text='Invoice Date')
        self.label11.grid(row=9, column=0, pady=5)
        self.entry_date = tk.Entry(self)
        self.entry_date.grid(row=9, column=1, pady=5)

        self.label12 = tk.Label(self, text='Payment Terms')
        self.label12.grid(row=10, column=0, pady=5)
        self.conditions_paiement_options = ['Option 1', 'Option 2', 'Option 3']  # replace with your options
        self.entry_conditions = ttk.Combobox(self, values=self.conditions_paiement_options)
        self.entry_conditions.grid(row=10, column=1, pady=5)

        separator2 = tk.Frame(self, height=2, bg='black')
        separator2.grid(row=11, columnspan=5, pady=10, sticky='we')

        self.entry_description = tk.Entry(self, font=('Arial', 14))
        self.descript_objet_options = ['V-T', 'V-G']
        self.entry_description = ttk.Combobox(self, values=self.descript_objet_options)
        self.entry_description.grid(row=12, column=0, pady=5)

        self.entry_prix_unitaire = tk.Entry(self, font=('Arial', 14))
        self.entry_prix_unitaire.insert(0, "0.00")
        self.entry_prix_unitaire.grid(row=12, column=1, pady=5)

        self.entry_quantite = tk.Entry(self, font=('Arial', 14))
        self.entry_quantite.insert(0, "1")
        self.entry_quantite.grid(row=12, column=2, pady=5)

        self.montant = tk.StringVar()
        self.montant.set("0.00 €")
        self.label_montant = tk.Label(self, textvariable=self.montant, font=('Arial', 14))
        self.label_montant.grid(row=12, column=3, pady=5)

        self.entry_prix_unitaire.bind("<KeyRelease>", self.update_montant)
        self.entry_quantite.bind("<KeyRelease>", self.update_montant)

        self.label13 = tk.Label(self, text='Subtotal')
        self.label13.grid(row=13, column=2, pady=5)
        self.sous_total = tk.StringVar()
        self.sous_total.set("0.00 €")
        self.label_sous_total = tk.Label(self, textvariable=self.sous_total, font=('Arial', 14))
        self.label_sous_total.grid(row=13, column=3, pady=5)

        self.label14 = tk.Label(self, text='VAT (20%)')
        self.label14.grid(row=14, column=2, pady=5)
        self.tva = tk.StringVar()
        self.tva.set("0.00 €")
        self.label_tva = tk.Label(self, textvariable=self.tva, font=('Arial', 14))
        self.label_tva.grid(row=14, column=3, pady=5)

        self.label15 = tk.Label(self, text='Total')
        self.label15.grid(row=15, column=2, pady=5)
        self.total = tk.StringVar()
        self.total.set("0.00 €")
        self.label_total = tk.Label(self, textvariable=self.total, font=('Arial', 14))
        self.label_total.grid(row=15, column=3, pady=5)

        self.label16 = tk.Label(self, text='Balance Due')
        self.label16.grid(row=16, column=2, pady=5)
        self.solde_du = tk.StringVar()
        self.solde_du.set("0.00 €")
        self.label_solde_du = tk.Label(self, textvariable=self.solde_du, font=('Arial', 14))
        self.label_solde_du.grid(row=16, column=3, pady=5)

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
        self.solde_du.set("{:.2f} €".format(total))

