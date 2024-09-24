
import time
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from googleapiclient.discovery import build
from google.oauth2 import service_account
import mimetypes
mimetypes.add_type('application/octet-stream', '.bkp')

class NuvemMP:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Nuvem MP')
        self.root.geometry('400x500')
        self.root.resizable(False, False)
        self.frame()
        self.root.mainloop()



    def frame(self):
        self.frame_root = tk.Frame(self.root, background='white')
        self.frame_root.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.botao = tk.Button(self.frame_root, text='Escolher Arquivo', command=self.escolher_arquivo,
                               activebackground='#e9f0f2', borderwidth=0, )
        self.botao.place(relx=0.57, rely=0.16)
        self.entry = tk.Entry(self.frame_root)
        self.entry.place(relx=0.1, rely=0.1, relwidth=0.8)
        self.botao_final = tk.Button(self.frame_root, text='Mandar para a Nuvem!', command=self.nuvem,
                                     activebackground='#e9f0f2', borderwidth=0, )
        self.botao_final.place(relx=0.5, rely=0.85)
        self.imagem_load = tk.PhotoImage(file='<CAMINHO>/nuvem.png')
        self.label_imagem = tk.Label(self.frame_root, image=self.imagem_load)
        self.label_imagem.configure(background='white')
        self.label_imagem.place(relx=0.25, rely=0.38)




    def escolher_arquivo(self):
        self.label_imagem.destroy()
        self.imagem_load = tk.PhotoImage(file='<CAMINHO>/nuvem.png')
        self.label_imagem = tk.Label(self.frame_root, image=self.imagem_load)
        self.label_imagem.configure(background='white')
        self.label_imagem.place(relx=0.25, rely=0.38)
        self.escolher_arquivo = tk.filedialog.askopenfilename(title='Escolher Arquivo',
                                                              initialdir='<CAMINHO>',
                                                              filetypes=(
            ('Backup files', '*.bkp'), ('All files', '*.*'), ))
        if self.escolher_arquivo:
            self.entry.delete(0, 'end')
            self.entry.insert(0, self.escolher_arquivo)



    def nuvem(self):
        try:
            SCOPES = ['https://www.googleapis.com/auth/drive']
            SERVIVE_ACCOUNT_FILE = '<caminho>*.json'
            PARENT_FOLDER_ID = '<CAMINHO DA PASTA DRIVE>'
            creds = service_account.Credentials.from_service_account_file(SERVIVE_ACCOUNT_FILE, scopes=SCOPES)
            service = build('drive', 'v3', credentials=creds)

            nome = self.entry.get()
            indice = nome.rfind('/')


            file_metadata = {
                'name' : nome[indice+1:],
                'parents': [PARENT_FOLDER_ID]
            }

            file = service.files().create(
                body=file_metadata,
                media_body=nome

            ).execute()

            self.label_imagem.destroy()
            self.imagem_load = tk.PhotoImage(file='<CAMINHO>/nuvem2.0.png')
            self.label_imagem = tk.Label(self.frame_root, image=self.imagem_load)
            self.label_imagem.configure(background='white')
            self.label_imagem.place(relx=0.25, rely=0.38)
        except Exception:
            self.label_imagem.destroy()
            self.imagem_load = tk.PhotoImage(file='<CAMINHO>/nuvem_error.png')
            self.label_imagem = tk.Label(self.frame_root, image=self.imagem_load)
            self.label_imagem.configure(background='white')
            self.label_imagem.place(relx=0.25, rely=0.38)



NuvemMP()
