import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardCreateClients(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de création de clients ainsi que le formulaire de création de clients
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardCreateClients
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Client Creation'))
        self.label.pack(pady=5)
        self.label1 = tk.Label(self, text=_('Name'))
        self.label1.pack(pady=5)
        self.entry_nom = tk.Entry(self, width=30)
        self.entry_nom.pack(pady=5)
        self.label2 = tk.Label(self, text=_('First Name'))
        self.label2.pack(pady=5)
        self.entry_prenom = tk.Entry(self, width=30)
        self.entry_prenom.pack(pady=5)
        self.label3 = tk.Label(self, text=_('Phone'))
        self.label3.pack(pady=5)
        self.entry_telephone = tk.Entry(self, width=30)
        self.entry_telephone.pack(pady=5)
        self.label4 = tk.Label(self, text='Email')
        self.label4.pack(pady=5)
        self.entry_email = tk.Entry(self, width=30)
        self.entry_email.pack(pady=5)
        self.label5 = tk.Label(self, text=_('Address'))
        self.label5.pack(pady=5)
        self.entry_adresse = tk.Entry(self, width=30)
        self.entry_adresse.pack(pady=5)
        self.label6 = tk.Label(self, text=_('Comment (optional)'))
        self.label6.pack(pady=5)
        self.entry_commentaire = tk.Text(self, width=50, height=5)
        self.entry_commentaire.pack(pady=5)