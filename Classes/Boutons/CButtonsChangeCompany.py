import tkinter as tk
from tkinter import messagebox
import gettext
_=gettext.gettext

from Classes.DAO.Dao_entreprise import Dao_entreprise

class ButtonsChangeCompany(tk.Frame):
    '''
    Classe qui fabrique les boutons pour changer les informations de l'entreprise
    '''
    def __init__(self, master=None, dash_board=None, language_var=None, top_level=None):
        '''
        Constructeur de la classe ButtonChangeCompany
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.language_var = language_var
        self.top_level = top_level
        self.pack()

        self.button1 = tk.Button(self, text=_('Save'), command=self.save)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Cancel'), command=self.cancel)
        self.button2.pack(pady=5)

    def save(self):
        '''
        Méthode qui permet de sauvegarder les informations de l'entreprise
        '''
        if self.dash_board.entry1.get() == '' or self.dash_board.entry2.get() == '' or self.dash_board.entry3.get() == '' or self.dash_board.entry4.get() == '':
            messagebox.showerror(_('Error'), _('Please fill all the fields'))
            return            
        entreprise = (self.dash_board.entry1.get(), self.dash_board.entry2.get(), self.dash_board.entry3.get(), self.dash_board.entry4.get())
        Dao_entreprise.change(entreprise)
        messagebox.showinfo(_('Information'), _('Company information has been changed'))
        self.master.destroy()

    def cancel(self):
        '''
        Méthode qui permet d'annuler les modifications
        '''
        self.top_level.destroy()