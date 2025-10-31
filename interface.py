import customtkinter as ctk
import json
from login import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

#importa usuários
#importa todos os usuários
f = open("usuarios.json","r")
usuarios = json.load(f)
f.close()
for i in range(len(usuarios)):
    usuarios[i] = Login(
        i,
        usuarios[i]["nome"],
        usuarios[i]["email"],
        usuarios[i]["usuario"],
        usuarios[i]["senha"],
                
        
    )
#informações do aplicativo
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
        
        #Frame de login
        self.frameLogin = ctk.CTkFrame(self, width=350, height=380,fg_color=corPreta)
        self.frameLogin.place(x=280, y=10)
        #Colocando widgets no frame de login
        #Titulo de login
        self.tituloUsuario = ctk.CTkLabel(self.frameLogin,text='Usuário ou email:',font=fonteNormal,text_color=corBranca)
        self.tituloUsuario.grid(row=0, column=0, pady=10, padx=10)
        #entry
        self.campoUsuario = ctk.CTkEntry(self.frameLogin,placeholder_text = " Digite o nome de usuário ou email",fg_color="#ffffff",font=fonteNormal,text_color=corPreta)

        self.campoUsuario.grid(row=1, column=0, padx=10)


        #label
        self.tituloSenha = ctk.CTkLabel(self.frameLogin,text='Senha:',font=fonteNormal,text_color=corBranca)
        self.tituloSenha.grid(row=2, column=0, pady=10, padx=10)
        #entry
        self.campoSenha = ctk.CTkEntry(self.frameLogin,placeholder_text = "Senha",fg_color="#ffffff",show="*",font=fonteNormal,text_color=corPreta)
        self.campoSenha.grid(row=3, column=0, padx=10)
        #Botão de login
        self.botaoLogin = ctk.CTkButton(self.frameLogin,text='Login',command=lambda:self.confirmaLogin(self.campoUsuario,self.campoSenha,usuarios), fg_color="#db0000",hover_color=corCinza,font=fonteNormal)
        self.botaoLogin.grid(row=4, column=0, pady=10, padx=10)
        
        #Botão de cadastro
        self.botaoCadastro = ctk.CTkButton(self.frameLogin,text='Cadastro',command=self.interfaceCadastro, fg_color="#db0000",hover_color=corCinza,font=fonteNormal)
        self.botaoCadastro.grid(row=5, column=0, pady=10, padx=10)
        
        
        self.erroUsuario = ctk.CTkLabel(self.frameLogin,text='')
        self.erroUsuario.grid(row=6, column=0, pady=10, padx=10)
        self.erroSenha = ctk.CTkLabel(self.frameLogin,text='')
        self.erroSenha.grid(row=7, column=0, pady=10, padx=10)
        self.erroUsuario.configure(text="Usuário inválido",
                text_color="red")
        self.erroSenha.configure(text="Senha errada",
                text_color="red")
        self.erroUsuario.grid_remove()
        self.erroSenha.grid_remove()
        
        
    def voltarParaLogin(self):
        # Esconde quaisquer frames atuais e volta para a tela de login
        try:
            
            self.frameCadastro.place_forget()
        except Exception:
            pass
        try:
            self.frameLogin.place_forget()
        except Exception:
            pass
        
        self.botaoVoltarCadastro.place_forget() 
        self.interfaceLogin()
        
        
    def logout(self):
        # Esconde quaisquer frames atuais e volta para a tela de login
        try:
            
            self.frameCadastro.place_forget()
        except Exception:
            pass
        try:
            self.frameLogin.place_forget()
        except Exception:
            pass
        
        self.botaoLogout.place_forget() 
        self.interfaceLogin()
        
        
    def interfaceCadastro(self):
        self.frameLogin.place_forget()
        #Criando frame de cadastro
        self.frameCadastro = ctk.CTkFrame(self, width=350, height=380,fg_color=corPreta)
        self.frameCadastro.place(x=280, y=10)
        
        #Botão de voltar ao login
        self.botaoVoltarCadastro = ctk.CTkButton(
            self,
            text='← Voltar',
            command=self.voltarParaLogin,
            fg_color=corVermelha,
            hover_color=corVermelhaEscura,
            font=fonteNormal,
            width=100
        )
        self.botaoVoltarCadastro.place(x=-10, y=10)

        
        
        #campos de cadastro
        #nome
        self.campoNomeCadastro = ctk.CTkEntry(self.frameCadastro,placeholder_text ="Nome completo",fg_color=corBranca,font=fonteNormal,text_color=corPreta)
        self.campoNomeCadastro.grid(row=0,column=0,pady=10)
        
        #usuario
        self.campoUsuarioCadastro = ctk.CTkEntry(self.frameCadastro,placeholder_text = "Nome de usuário",fg_color=corBranca,font=fonteNormal,text_color=corPreta)

        self.campoUsuarioCadastro.grid(row=1, column=0, pady=10)
        
        #email
        self.campoEmail = ctk.CTkEntry(self.frameCadastro,placeholder_text = "Email",fg_color=corBranca,font=fonteNormal,text_color=corPreta)
        self.campoEmail.grid(row=2, column=0, pady=10)
        #Senha
        self.campoSenha = ctk.CTkEntry(self.frameCadastro,placeholder_text = "Senha",fg_color=corBranca,font=fonteNormal,text_color=corPreta)
        self.campoSenha.grid(row=3, column=0, pady=10)
        #Confirma senha
        self.campoConfirmaSenha = ctk.CTkEntry(self.frameCadastro,placeholder_text = "Confirma a senha",fg_color=corBranca,font=fonteNormal,text_color=corPreta)
        self.campoConfirmaSenha.grid(row=4, column=0, pady=10)
        
        #Botão de cadastrar
        self.botaoCadastrar = ctk.CTkButton(self.frameCadastro,text='Cadastrar',command=lambda:self.cadastrarUsuario(self.campoNomeCadastro,self.campoUsuarioCadastro,self.campoEmail,self.campoSenha,self.campoConfirmaSenha,usuarios), fg_color="#db0000",hover_color=corCinza,font=fonteNormal)
        self.botaoCadastrar.grid(row=5, column=0, pady=10, padx=10)
        
        
    def capturaCadastro(self,nome,usuario,email,senha,confirmaSenha):
        nome = nome.get()
        usuario = usuario.get()
        email = email.get()
        senha = senha.get()
        confirmaSenha = confirmaSenha.get()
        return nome,usuario,email,senha,confirmaSenha
        
    def cadastrarUsuario(self,nome,usuario,email,senha,confirmaSenha,usuarios):
        self.erroCadastro = ctk.CTkLabel(self.frameCadastro,text='Preencha todos os campos!',font=fonteNormal,text_color=corVermelha)        
        nome,usuario,email,senha,confirmaSenha = self.capturaCadastro(nome,usuario,email,senha,confirmaSenha)
        
        confirmaUsuario,id=Login.confirmaUsuario(usuario,usuarios)
        confirmaEmail,id = Login.confirmaEmail(email,usuarios)
        nomes = Login.separaNome(nome)
        print(nomes)
        senhaVerificada = Login.verificaSenha(senha,nomes)
        if nome =='' or usuario=='' or email=='' or senha=='' or confirmaSenha=='':
            self.erroCadastro.grid(row=6, column=0, pady=10, padx=10)
        else:
            if confirmaUsuario:
                # Apaga o conteúdo do campo atual
                self.campoUsuarioCadastro.delete(0, 'end')

                # Atualiza o placeholder e a cor para indicar o erro
                self.campoUsuarioCadastro.configure(
                    placeholder_text="Usuário já existe",
                    placeholder_text_color=corVermelha
                    )
                
            if confirmaEmail:
                self.campoEmail.delete(0, 'end')

                # Atualiza o placeholder e a cor para indicar o erro
                self.campoEmail.configure(
                    placeholder_text="Email já existe",
                    placeholder_text_color=corVermelha
                    )
            if senhaVerificada == False:
                self.campoSenha.delete(0, 'end')

                # Atualiza o placeholder e a cor para indicar o erro
                self.campoSenha.configure(
                    placeholder_text="Senha inválida",
                    placeholder_text_color=corVermelha
                    )
            else:
                if senha != confirmaSenha:
                    self.campoSenha.delete(0, 'end')
                    self.campoConfirmaSenha.delete(0, 'end')

                # Atualiza o placeholder e a cor para indicar o erro
                    self.campoSenha.configure(
                        placeholder_text="Senhas diferentes",
                        placeholder_text_color=corVermelha
                        )
                if senha == confirmaSenha and senhaVerificada==True and not confirmaEmail and not confirmaUsuario:
                    usuarios.append("")
                    usuarios[id] = Login(id,
                                         nome,
                                         email,
                                         usuario,
                                         senha)
                    print(usuarios[id].nome,usuarios[id].usuario)
                    print(usuarios[3].nome,usuarios[3].usuario)
                                         
                    self.voltarParaLogin()
                    
    def capturaLogin(self,campoUsuario,campoSenha):
        usuario = campoUsuario.get()
        senha = campoSenha.get()
        return usuario,senha
    
    def confirmaLogin(self,usuario,senha,usuarios):
        self.erroLogin = ctk.CTkLabel(self.frameLogin,text='Preencha todos os campos!',font=fonteNormal,text_color=corVermelha)        
        self.erroLogin.grid(row=6,column=0)
        self.erroLogin.grid_remove()
        
        usuario,senha = self.capturaLogin(usuario,senha)
        confirmacaoUsuario,id = Login.confirmaUsuario(usuario,usuarios)
        if usuario=="" or senha=="":
            self.erroLogin.grid()
            
            
        else:
            self.erroLogin.grid_remove()
            if confirmacaoUsuario == False:
                confirmacaoEmail,id = Login.confirmaEmail(usuario,usuarios)
            if id >= len(usuarios):
                
                self.erroUsuario.grid()
            confirmacaoSenha = Login.confirmaSenha(senha,id,usuarios)
            if confirmacaoSenha:
                #entra no programa
                #botão de logout
                self.interfaceCatalogo()
                print("Logado com sucesso")
            else:
                #repete process
                
                self.erroSenha.grid()
            
    def interfaceCatalogo(self):
        self.frameLogin.place_forget()
        self.botaoLogout = ctk.CTkButton(
        self,
        text='Logout',
        command=self.logout,
        fg_color=corVermelha,
        hover_color=corVermelhaEscura,
        font=fonteNormal,
        width=100
    )
        self.botaoLogout.place(relx=1, x=-10, y=10, anchor='ne')
        
        
        
            

        
        
        
        
        
        
        
        
        
        
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
        usuarios[i]["email"],
        usuarios[i]["usuario"],
        usuarios[i]["senha"],
                
        
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

