import customtkinter as ctk
import json
from login import *
class Interface:
    #def capturaLogin():
        
        
    def capturaLogin(campoUsuario,campoSenha):
        usuario = campoUsuario.get()
        senha = campoSenha.get()
        return usuario,senha
    
    def confirmaLogin(usuario,senha,usuarios):
        usuario,senha = Interface.capturaLogin(usuario,senha)
        confirmacaoUsuario,id = Login.confirmaUsuario(usuario,usuarios)
        if confirmacaoUsuario == False:
            confirmacaoEmail,id = Login.confirmaEmail(usuario,usuarios)
        if id == -1:
            return print("Usuário inválido")
        return Login.confirmaSenha(senha,id,usuarios)
        
     

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
campoSenha = ctk.CTkEntry(app,placeholder_text = "Senha",fg_color="#ffffff")
campoSenha.pack()





botaoLogin = ctk.CTkButton(app,text='Login',command=lambda:Interface.confirmaLogin(campoUsuario,campoSenha,usuarios), fg_color="#db0000")

botaoLogin.pack(pady=50)

#button
app.mainloop()

