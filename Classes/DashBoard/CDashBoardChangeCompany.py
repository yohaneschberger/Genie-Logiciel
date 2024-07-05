import tkinter as tk
import gettext
_=gettext.gettext

from Classes.DAO.Dao_entreprise import Dao_entreprise

class DashBoardChangeCompany(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord pour changer les informations de l'entreprise
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardChangeCompany
        '''
        super().__init__(master)
        self.master = master
        self.pack()

        self.company = Dao_entreprise.get()

        self.label = tk.Label(self, text=_('Company information'))
        self.label.pack()
        self.label1 = tk.Label(self, text=_('Company name'))
        self.label1.pack()
        self.entry1 = tk.Entry(self)
        self.entry1.insert(0, self.company[0][1])
        self.entry1.pack()
        self.label2 = tk.Label(self, text=_('Company address'))
        self.label2.pack()
        self.entry2 = tk.Entry(self)
        self.entry2.insert(0, self.company[0][2])
        self.entry2.pack()
        self.label3 = tk.Label(self, text=_('Company phone'))
        self.label3.pack()
        self.entry3 = tk.Entry(self)
        self.entry3.insert(0, self.company[0][3])
        self.entry3.pack()
        self.label4 = tk.Label(self, text=_('Company email'))
        self.label4.pack()
        self.entry4 = tk.Entry(self)
        self.entry4.insert(0, self.company[0][4])
        self.entry4.pack()