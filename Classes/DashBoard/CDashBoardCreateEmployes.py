import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardCreateEmployes(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de création des employés ainsi que le formulaire de création de employés
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardCreateEmployes
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Create Employees'))
        self.label.pack(pady=5)
        self.label_nom = tk.Label(self, text=_('Name'))
        self.label_nom.pack(pady=5)
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack(pady=5)
        self.label_prenom = tk.Label(self, text=_('First Name'))
        self.label_prenom.pack(pady=5)
        self.entry_prenom = tk.Entry(self)
        self.entry_prenom.pack(pady=5)
        self.label_telephone = tk.Label(self, text=_('Phone'))
        self.label_telephone.pack(pady=5)
        self.entry_telephone = tk.Entry(self)
        self.entry_telephone.pack(pady=5)
        self.label_email = tk.Label(self, text='Email')
        self.label_email.pack(pady=5)
        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)