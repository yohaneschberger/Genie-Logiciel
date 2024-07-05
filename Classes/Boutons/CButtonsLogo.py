import sqlite3
import tkinter as tk
from PIL import Image, ImageTk # type: ignore
from tkinter.filedialog import askopenfilename
import gettext
_=gettext.gettext
from Classes.Frame import Frame_Welcome

class ButtonsLogo(tk.Frame):
    '''
    Classe qui fabrique les boutons de la fenêtre de logo
    '''
    def __init__(self, master=None, dash_board=None, is_admin=False):
        '''
        Constructeur de la classe ButtonsLogo
        '''
        super().__init__(master)
        self.master = master
        self.dash_board = dash_board
        self.is_admin = is_admin
        self.pack()
        self.button1 = tk.Button(self, text=_('Confirm'), command=self.confirmed)
        self.button1.pack(pady=5)
        self.button2 = tk.Button(self, text=_('Import'), command=self.import_png)
        self.button2.pack(pady=5)
        self.button3 = tk.Button(self, text=_('Cancel'), command=self.back_to_wel)
        self.button3.pack(pady=5)
        self.logo_filename = None

    def confirmed(self):
        '''
        Méthode qui permet de confirmer le logo importé (enregistrer dans la base de données pour l'utiliser lors de la création de facture, devis)
        '''
        if self.logo_filename:
            conn = sqlite3.connect('quit.db')
            c = conn.cursor()
            with open(self.logo_filename, 'rb') as file:
                logo = file.read()
            c.execute('INSERT OR REPLACE INTO logo (id, logo) VALUES (1, ?)', (logo,))
            conn.commit()
            conn.close()
            self.back_to_wel()

        
    def import_png(self):
        '''
        Méthode qui permet d'importer une image en format png pour le logo
        '''
        filename = askopenfilename(filetypes=[('PNG files', '*.png')])
        if filename:
            image = Image.open(filename)
            image = image.resize((200, 200), Image.BICUBIC)
            photo = ImageTk.PhotoImage(image)
            self.dash_board.label.config(image=photo)
            self.dash_board.label.image = photo
            self.logo_filename = filename


    def back_to_wel(self):
        '''
        Méthode qui permet de revenir à la fenêtre de bienvenue
        '''
        for widget in self.master.winfo_children():
            widget.destroy()
        if self.is_admin:
            Frame_Welcome.Frame_Welcome(self.master, is_admin=True, language_var=self.master.language_var)
        else:
            Frame_Welcome.Frame_Welcome(self.master, language_var=self.master.language_var)