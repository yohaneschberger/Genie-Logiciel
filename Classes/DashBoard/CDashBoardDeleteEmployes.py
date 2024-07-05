import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardDeleteEmployes(tk.Frame):
    '''
    Classe qui crée un tableau de bord pour la suppression des employés
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardDeleteEmployes
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Delete Employees'))
        self.label.pack(pady=5)

        self.label_nom = tk.Label(self, text=_('Last Name'))
        self.label_nom.pack(pady=5)
        self.entry_nom = tk.Entry(self)
        self.entry_nom.pack(pady=5)
        self.label_prenom = tk.Label(self, text=_('First Name'))
        self.label_prenom.pack(pady=5)
        self.entry_prenom = tk.Entry(self)
        self.entry_prenom.pack(pady=5)