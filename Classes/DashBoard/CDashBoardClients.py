import tkinter as tk
import gettext
_=gettext.gettext

class DashBoardClients(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre des clients
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardClients
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = tk.Label(self, text=_('Clients'))
        self.label.pack(pady=5)