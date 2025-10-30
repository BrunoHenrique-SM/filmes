import customtkinter as ctk
import json
from login import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
corPreta = "#000000"
corVermelha = "#db0000"
corCinza= "#564d4d"
corVermelhaEscura = "#831010"
corBranca = "#ffffff"
fonteNormal = ("Century Gothic bold",14)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoesJanelaLogin()
        self.interfaceLogin()
        
        
    def configuracoesJanelaLogin(self):
        self.geometry("700x400")
        self.title("Filmes")
        self.resizable(False, False)
        self.configure(fg_color= corPreta)
        
    def interfaceLogin(self):
        
        '''
        self.img = ctk.CTkImage(dark_image=Image.open("duna.jpg"),
                    size=(100, 100))
        self.labelImagem = ctk.CTkLabel(self, text=None, image=self.img)
        self.labelImagem.grid(row=1, column=0, padx=10 )
        '''
        #label
        self.tituloUsuario = ctk.CTkLabel(self,text='Usuário ou email:',font=fonteNormal)
        self.tituloUsuario.grid(row=0, column=0, pady=10, padx=300)
        #entry
        campoUsuario = ctk.CTkEntry(self,placeholder_text = " Digite o nome de usuário ou email",fg_color="#ffffff",font=fonteNormal,text_color=corPreta)

        campoUsuario.grid(row=1, column=0, pady=10, padx=300)


        #label
        tituloSenha = ctk.CTkLabel(self,text='Senha:',font=fonteNormal)
        tituloSenha.grid(row=2, column=0, pady=10, padx=300)
        #entry
        campoSenha = ctk.CTkEntry(self,placeholder_text = "Senha",fg_color="#ffffff",show="*",font=fonteNormal,text_color=corPreta)
        campoSenha.grid(row=3, column=0, pady=10, padx=300)
        #Botão de login
        botaoLogin = ctk.CTkButton(self,text='Login',command='', fg_color="#db0000",hover_color=corCinza,font=fonteNormal)
        botaoLogin.grid(row=4, column=0, pady=10, padx=300)
        
        #Botão de cadastro
        botaoCadastro = ctk.CTkButton(self,text='Cadastro',command='', fg_color="#db0000",hover_color=corCinza,font=fonteNormal)
        botaoCadastro.grid(row=5, column=0, pady=10, padx=300)
        
        
        erroUsuario = ctk.CTkLabel(self,text='')
        erroUsuario.grid(row=6, column=0, pady=10, padx=300)
        erroSenha = ctk.CTkLabel(self,text='')
        erroSenha.grid(row=7, column=0, pady=10, padx=300)
        
        
        
        
        
if __name__=="__main__":
    app = App()
    app.mainloop()
'''
class Interface:
    
        
        
    def capturaLogin(campoUsuario,campoSenha):
        usuario = campoUsuario.get()
        senha = campoSenha.get()
        return usuario,senha
    
    def confirmaLogin(app,usuario,senha,usuarios):
        
        usuario,senha = Interface.capturaLogin(usuario,senha)
        confirmacaoUsuario,id = Login.confirmaUsuario(usuario,usuarios)
        if confirmacaoUsuario == False:
            confirmacaoEmail,id = Login.confirmaEmail(usuario,usuarios)
        if id == -1:
            erroUsuario.configure(text="Usuário inválido",
            text_color="red")
        confirmacaoSenha = Login.confirmaSenha(senha,id,usuarios)
        if confirmacaoSenha:
            #entra no programa
            print("Logado com sucesso")
        else:
            #repete processo
            erroSenha.configure(text="Senha errada",
            text_color="red")
        
     

#importa todos os usuários
f = open("usuarios.json","r")
usuarios = json.load(f)
f.close()
for i in range(len(usuarios)):
    usuarios[i] = Login(
        i,
        usuarios[i]["nome"],
        usuarios[i]["usuario"],
        usuarios[i]["senha"],
        usuarios[i]["email"]        
        
    )
    
ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title("Filmes")
app.geometry('800x800')
app.configure(fg_color="#000000")
#label
tituloUsuario = ctk.CTkLabel(app,text='Usuário ou email:')
tituloUsuario.pack(pady=20)
#entry
campoUsuario = ctk.CTkEntry(app,placeholder_text = " Digite o nome de usuário ou email",fg_color="#ffffff")

campoUsuario.pack()


#label
tituloSenha = ctk.CTkLabel(app,text='Senha:')
tituloSenha.pack(pady=20)
#entry
campoSenha = ctk.CTkEntry(app,placeholder_text = "Senha",fg_color="#ffffff",show="*")
campoSenha.pack()





botaoLogin = ctk.CTkButton(app,text='Login',command=lambda:Interface.confirmaLogin(app,campoUsuario,campoSenha,usuarios), fg_color="#db0000")

botaoLogin.pack(pady=50)
erroUsuario = ctk.CTkLabel(app,text='')
erroUsuario.pack(pady = 10)
erroSenha = ctk.CTkLabel(app,text='')
erroSenha.pack(pady=10)

#button
app.mainloop()
'''

