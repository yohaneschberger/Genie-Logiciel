import tkinter as tk
import gettext

_=gettext.gettext
from Classes.Frame import Frame_Welcome
from Classes.Frame import Frame_Create_Employes
from Classes.Frame import Frame_Search_Employes
from Classes.Frame import Frame_Delete_Employes

class ButtonsEmployes(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre des employés
    '''
    def __init__(self, master=None, dash_board=None, is_admin=False, language_var=None):
        '''
        Constructeur de la classe ButtonsEmployes
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.is_admin = is_admin
        self.language_var = language_var
        self.pack()
        self.button1 = tk.Button(self, text=_('Create Employee'), command=self.create_employe)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Search Employee'), command=self.search_employe)
        self.button2.pack(pady=5)
        self.button3 = tk.Button(self, text=_('Delete Employee'), command=self.delete_employe)
        self.button3.pack(pady=5)
        self.button4 = tk.Button(self, text=_('Back'), command=self.back_to_frame_wel)
        self.button4.pack(pady=5)

    def create_employe(self):
        '''
        Méthode qui permet de créer un employé
        '''
        Frame_Create_Employes.Frame_Create_Employes(self.master, language_var=self.master.language_var)

    def search_employe(self):
        '''
        Méthode qui permet de rechercher un employé
        '''
        Frame_Search_Employes.Frame_Search_Employes(self.master, language_var=self.master.language_var)

    def delete_employe(self):
        '''
        Méthode qui permet de supprimer un employé
        '''
        Frame_Delete_Employes.Frame_Delete_Employes(self.master, language_var=self.master.language_var)

    def back_to_frame_wel(self):
        '''
        Méthode qui permet de revenir à la fenêtre de bienvenue en supprimant le frame des employés et en recréant le frame de bienvenue
        '''
        self.dash_board.destroy()
        self.destroy()
        self.master.pack()
        if self.is_admin:
            Frame_Welcome.Frame_Welcome(self.master, is_admin=True, language_var=self.master.language_var)
        else:
            Frame_Welcome.Frame_Welcome(self.master, language_var=self.master.language_var)