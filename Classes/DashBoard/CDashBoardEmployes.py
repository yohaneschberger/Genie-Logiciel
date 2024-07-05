import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardEmployes(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre des employés
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardEmployes
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Employees'))
        self.label.pack(pady=5)