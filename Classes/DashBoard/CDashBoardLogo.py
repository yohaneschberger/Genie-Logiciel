import sqlite3
import tkinter as tk
from PIL import Image, ImageTk # type: ignore
import gettext
_=gettext.gettext
import io   # Importation de la bibliothèque io pour lire les données binaires

class DashBoardLogo(tk.Frame):
    '''
    Classe qui fabrique le tableau de bord de la fenêtre de logo
    '''
    def __init__(self, master=None):
        '''
        Constructeur de la classe DashBoardLogo
        '''
        super().__init__(master)
        self.master = master
        self.pack()
        conn = sqlite3.connect('Bdd/quit.db')
        c = conn.cursor()
        c.execute('SELECT logo FROM logo WHERE id = 1')
        logo = c.fetchone()
        conn.close()
        if logo is not None and logo[0] is not None:    # Si le logo existe
            logo = Image.open(io.BytesIO(logo[0]))  # On lit les données binaires du logo
            logo = logo.resize((200, 200), Image.BICUBIC)   # On redimensionne le logo
            photo = ImageTk.PhotoImage(logo)    # On convertit le logo en photo
            self.label = tk.Label(self, image=photo)    # On affiche le logo
            self.label.image = photo    # On conserve la photo
        else:   # Si le logo n'existe pas
            self.label = tk.Label(self, text=_('Logo visualization'))   # On affiche un message
        self.label.pack(pady=5)    # On affiche le label