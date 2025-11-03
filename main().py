import customtkinter as ctk
import json

from tkinter import PhotoImage
from PIL import Image, ImageTk
from sistema import *
from filmes import *
from io import BytesIO

# informações do aplicativo
corPreta = "#000000"
corVermelha = "#db0000"
corCinza = "#564d4d"
corVermelhaEscura = "#831010"
corBranca = "#ffffff"
fonteNormal = ("Century Gothic bold", 14)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.filme0 = 0
        self.filme1 = 1
        self.filme2 = 2
        self.filmesAmostra = filmesLista
        self.protocol("WM_DELETE_WINDOW", self.fechaJanela)
        self.quantidadeFilmes = len(self.filmesAmostra)
        self.configuracoesJanelaLogin()
        self.interfaceLogin()

    def alteraQuantidade(self):
        self.quantidadeFilmes = len(self.filmesAmostra)    
    def alteraAmostra(self,novaAmostra):
        self.filmesAmostra = novaAmostra
    def configuracoesJanelaLogin(self):
        # Configurações iniciais da janela principal
        self.geometry("1000x600")
        self.title("Filmes")
        self.resizable(False, False)
        self.configure(fg_color=corPreta)

    def interfaceLogin(self):

        # Frame de login
        self.frameLogin = ctk.CTkFrame(
            self,
            width=350,
            height=380,
            fg_color=corPreta
        )
        self.frameLogin.place(relx=0.5, rely=0.5, anchor="center")

        # Colocando widgets no frame de login
        # Título de usuário/email
        self.tituloUsuario = ctk.CTkLabel(
            self.frameLogin,
            text='Usuário ou email:',
            font=fonteNormal,
            text_color=corBranca
        )
        self.tituloUsuario.grid(row=0, column=0, pady=10, padx=10)

        # Campo de entrada do usuário
        self.campoUsuario = ctk.CTkEntry(
            self.frameLogin,
            placeholder_text=" Digite o nome de usuário ou email",
            fg_color="#ffffff",
            font=fonteNormal,
            text_color=corPreta
        )
        self.campoUsuario.grid(row=1, column=0, padx=10)

        # Título da senha
        self.tituloSenha = ctk.CTkLabel(
            self.frameLogin,
            text='Senha:',
            font=fonteNormal,
            text_color=corBranca
        )
        self.tituloSenha.grid(row=2, column=0, pady=10, padx=10)

        # Campo de entrada da senha
        self.campoSenha = ctk.CTkEntry(
            self.frameLogin,
            placeholder_text="Senha",
            fg_color="#ffffff",
            show="*",
            font=fonteNormal,
            text_color=corPreta
        )
        self.campoSenha.grid(row=3, column=0, padx=10)

        # Botão de login
        self.botaoLogin = ctk.CTkButton(
            self.frameLogin,
            text='Login',
            command=lambda: self.confirmaLogin(self.campoUsuario, self.campoSenha, usuarios),
            fg_color="#db0000",
            hover_color=corVermelhaEscura,
            font=fonteNormal
        )
        self.botaoLogin.grid(row=4, column=0, pady=10, padx=10)
        self.frameLogin.focus_set()
        self.campoUsuario.bind("<Return>", lambda e: self.botaoLogin.invoke())
        self.campoSenha.bind("<Return>", lambda e: self.botaoLogin.invoke())


        # Botão de cadastro
        self.botaoCadastro = ctk.CTkButton(
            self.frameLogin,
            text='Cadastro',
            command=self.interfaceCadastro,
            fg_color="#db0000",
            hover_color=corVermelhaEscura,
            font=fonteNormal
        )
        self.botaoCadastro.grid(row=5, column=0, pady=10, padx=10)

        # Labels de erro (inicialmente escondidos)
        self.erroUsuario = ctk.CTkLabel(self.frameLogin, text='')
        self.erroUsuario.grid(row=6, column=0, pady=10, padx=10)

        self.erroSenha = ctk.CTkLabel(self.frameLogin, text='')
        self.erroSenha.grid(row=7, column=0, pady=10, padx=10)

        # Configura e esconde mensagens de erro
        self.erroUsuario.configure(text="Usuário inválido", text_color="red")
        self.erroSenha.configure(text="Senha errada", text_color="red")

        self.erroCampoVazio = ctk.CTkLabel(
            self.frameLogin,
            text='Preencha todos os campos!',
            font=fonteNormal,
            text_color=corVermelha
        )
        self.erroCampoVazio.grid(row=6, column=0)
        self.erroCampoVazio.grid_remove()
        self.erroUsuario.grid_remove()
        self.erroSenha.grid_remove()
    def voltaPagina(self,pagina):
        self.limpaTela()
        pagina()
        self.botaoVoltarCadastro.place_forget()
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
        self.botaoLogout.place_forget()
        self.limpaTela()
        self.interfaceLogin()
        
        

    def interfaceCadastro(self):
        # Remove frame de login e mostra o frame de cadastro
        self.frameLogin.place_forget()

        self.frameCadastro = ctk.CTkFrame(
            self,
            width=350,
            height=380,
            fg_color=corPreta
        )
        self.frameCadastro.place(relx=0.5, rely=0.5, anchor="center")

        # Botão de voltar ao login (fora do frame de cadastro)
        self.botaoVoltarCadastro = ctk.CTkButton(
            self,
            text='← Voltar',
            command=lambda:self.voltaPagina(self.interfaceLogin),
            fg_color=corVermelha,
            hover_color=corVermelhaEscura,
            font=fonteNormal,
            width=100
        )
        self.botaoVoltarCadastro.place(x=10, y=10)

        # Campos de cadastro
        # Nome
        self.campoNomeCadastro = ctk.CTkEntry(
            self.frameCadastro,
            placeholder_text="Nome completo",
            fg_color=corBranca,
            font=fonteNormal,
            text_color=corPreta
        )
        self.campoNomeCadastro.grid(row=0, column=0, pady=10)

        # Usuário
        self.campoUsuarioCadastro = ctk.CTkEntry(
            self.frameCadastro,
            placeholder_text="Nome de usuário",
            fg_color=corBranca,
            font=fonteNormal,
            text_color=corPreta
        )
        self.campoUsuarioCadastro.grid(row=1, column=0, pady=10)

        # Email
        self.campoEmail = ctk.CTkEntry(
            self.frameCadastro,
            placeholder_text="Email",
            fg_color=corBranca,
            font=fonteNormal,
            text_color=corPreta
        )
        self.campoEmail.grid(row=2, column=0, pady=10)

        # Senha
        self.campoSenha = ctk.CTkEntry(
            self.frameCadastro,
            placeholder_text="Senha",
            fg_color=corBranca,
            font=fonteNormal,
            text_color=corPreta
        )
        self.campoSenha.grid(row=3, column=0, pady=10)

        # Confirma senha
        self.campoConfirmaSenha = ctk.CTkEntry(
            self.frameCadastro,
            placeholder_text="Confirma a senha",
            fg_color=corBranca,
            font=fonteNormal,
            text_color=corPreta
        )
        self.campoConfirmaSenha.grid(row=4, column=0, pady=10)

        # Botão de cadastrar
        self.botaoCadastrar = ctk.CTkButton(
            self.frameCadastro,
            text='Cadastrar',
            command=lambda: self.cadastrarUsuario(
                self.campoNomeCadastro,
                self.campoUsuarioCadastro,
                self.campoEmail,
                self.campoSenha,
                self.campoConfirmaSenha,
                usuarios
            ),
            fg_color="#db0000",
            hover_color=corVermelhaEscura,
            font=fonteNormal
        )
        
        for fld in (self.campoNomeCadastro,
            self.campoUsuarioCadastro,
            self.campoEmail,
            self.campoSenha,
            self.campoConfirmaSenha):
            fld.bind("<Return>", lambda e, b=self.botaoCadastrar: b.invoke())
        self.botaoCadastrar.grid(row=5, column=0, pady=10, padx=10)
        

    def capturaCadastro(self, nome, usuario, email, senha, confirmaSenha):
        nome = nome.get()
        usuario = usuario.get()
        email = email.get()
        senha = senha.get()
        confirmaSenha = confirmaSenha.get()
        return nome, usuario, email, senha, confirmaSenha

    def cadastrarUsuario(self, nome, usuario, email, senha, confirmaSenha, usuarios):
        self.erroCadastro = ctk.CTkLabel(
            self.frameCadastro,
            text='Preencha todos os campos!',
            font=fonteNormal,
            text_color=corVermelha
        )

        nome, usuario, email, senha, confirmaSenha = self.capturaCadastro(
            nome, usuario, email, senha, confirmaSenha
        )

        confirmaUsuario, id = Login.confirmaUsuario(usuario, usuarios)
        confirmaEmail, id = Login.confirmaEmail(email, usuarios)
        nomes = Login.separaNome(nome)
        
        senhaVerificada = Login.verificaSenha(senha, nomes)

        if nome == '' or usuario == '' or email == '' or senha == '' or confirmaSenha == '':
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
                if senha == confirmaSenha and senhaVerificada == True and not confirmaEmail and not confirmaUsuario:
                    usuarios.append("")
                    usuarios[id] = Login(
                        id,
                        nome,
                        email,
                        usuario,
                        senha
                    )
                    

                    self.voltaPagina(self.interfaceLogin)

    def capturaLogin(self, campoUsuario, campoSenha):
        usuario = campoUsuario.get()
        senha = campoSenha.get()
        return usuario, senha

    def confirmaLogin(self, usuario, senha, usuarios):
        usuario, senha = self.capturaLogin(usuario, senha)
        confirmacaoUsuario, id = Login.confirmaUsuario(usuario, usuarios)

        if usuario == "" or senha == "":
            self.erroSenha.grid_remove()
            self.erroCampoVazio.grid()

        else:
            self.erroCampoVazio.grid_remove()
            if confirmacaoUsuario == False:
                confirmacaoEmail, id = Login.confirmaEmail(usuario, usuarios)
            if id >= len(usuarios):
                self.erroSenha.grid_remove()
                self.erroUsuario.grid()
            else:
                confirmacaoSenha = Login.confirmaSenha(senha, id, usuarios)
                if confirmacaoSenha:
                    # entra no programa
                    # botão de logout
                    self.interfaceCatalogo()
                    print("Logado com sucesso")
                else:
                    # repete process
                    self.erroUsuario.grid_remove()
                    self.erroSenha.grid()

    def limpaTela(self):
        self.frameLogin.winfo_toplevel().focus_set()

        try:
            self.frameCadastro.place_forget()
        except Exception:
            pass
        try:
            self.frameLogin.place_forget()
        except Exception:
            pass
        try:
            self.frameCatalogo.place_forget()
        except Exception:
            pass
        try:
            self.frameFilme.place_forget()
        except Exception:
            pass
        try:
            self.botaoLogout.place_forget()  # ADICIONE ESTA LINHA
        except Exception:
            pass
        try:
            self.botaoVoltarCadastro.place_forget()  # ADICIONE ESTA LINHA
        except Exception:
            pass
    

    
    def pesquisa(self):
        self.filme0 = 0
        self.filme1 = 1
        self.filme2 = 2
        self.alteraAmostra(filmesLista)
        self.alteraQuantidade()
        self.filtrosVar.extend([
                        self.acao,
                        self.ficcao,
                        self.comedia,
                        self.drama,
                        self.thriller,
                        self.animacao,
                        self.fantasia,
                        self.terror
                        ])
        if any(var.get() for var in self.filtrosVar):    
            listaFiltros = [x.get() for x in self.filtrosVar ]
            self.alteraAmostra(Filtro.filtraFilmes(listaFiltros))
            self.alteraQuantidade()
        
        self.interfaceCatalogo()

    def interfaceCatalogo(self):
        
        self.limpaTela()

        # --- botão logout (filho de self) ---
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

        # --- frame principal do catálogo (centrado na janela) ---
        self.frameCatalogo = ctk.CTkFrame(
            self,
            width=900,
            height=500,
            fg_color="#2f2f2f"
        )
        self.frameCatalogo.place(relx=0.5, rely=0.5, anchor="center")

        # configura grid dentro do frameCatalogo: 3 linhas (filtro, amostra, controles)
        self.frameCatalogo.grid_rowconfigure(0, weight=0, minsize=70)  # filtro (pequeno)
        self.frameCatalogo.grid_rowconfigure(1, weight=1)              # amostra (maior)
        self.frameCatalogo.grid_rowconfigure(2, weight=0, minsize=60)  # controles (pequeno)
        self.frameCatalogo.grid_columnconfigure(0, weight=1)

        # --- frame Filtro (topo) ---
        self.gridFiltro = ctk.CTkFrame(
            self.frameCatalogo,
            height=60,
            fg_color="#4b4b4b"
        )
        self.filtrosVar = []
        self.acao = ctk.BooleanVar(value=False)
        self.ficcao = ctk.BooleanVar(value=False)
        self.comedia = ctk.BooleanVar(value=False)
        self.drama = ctk.BooleanVar(value=False)
        self.thriller = ctk.BooleanVar(value=False)
        self.animacao = ctk.BooleanVar(value=False)
        self.fantasia = ctk.BooleanVar(value=False)
        self.terror = ctk.BooleanVar(value=False)
        
        
        
            

            
        
        
        self.checkAcao = ctk.CTkCheckBox(self.gridFiltro,
                                         text="Ação",
                                         variable=self.acao)
        self.checkFiccao = ctk.CTkCheckBox(self.gridFiltro,
                                         text="Ficção Científica",
                                         variable=self.ficcao)
        self.checkComedia = ctk.CTkCheckBox(self.gridFiltro,
                                         text="Comédia",
                                         variable=self.comedia)
        self.checkDrama = ctk.CTkCheckBox(self.gridFiltro,
                                         text="Drama",
                                         variable=self.drama)
        self.checkThriller = ctk.CTkCheckBox(self.gridFiltro,
                                             text="Thriller",
                                             variable=self.thriller
                                            )
        self.checkAnimacao = ctk.CTkCheckBox(self.gridFiltro,
                                             text="Animação",
                                             variable=self.animacao
                                            )
        self.checkFantasia = ctk.CTkCheckBox(self.gridFiltro,
                                             text="Fantasia",
                                             variable=self.fantasia
                                            )
        self.checkTerror = ctk.CTkCheckBox(self.gridFiltro,
                                           text="Terror",
                                           variable=self.terror
                                            )
        

        self.botaoPesquisa = ctk.CTkButton(self.gridFiltro,
                                           fg_color=corVermelha,
                                           hover_color=corVermelhaEscura,
                                           text="🔍",
                                           command=self.pesquisa,
                                           height=35,
                                           width=35)
        self.checkAcao.pack(side="left", padx=3,pady=10)
        self.checkFiccao.pack(side="left",pady=10)
        self.checkComedia.pack(side="left",pady=10)
        self.checkDrama.pack(side="left",pady=10)
        self.checkThriller.pack(side="left",pady=10)
        self.checkAnimacao.pack(side="left",pady=10)
        self.checkFantasia.pack(side="left",pady=10)
        self.checkTerror.pack(side="left",pady=10)
        self.botaoPesquisa.pack(side="right", padx=10, pady=10)
        self.gridFiltro.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10,5))

        # exemplo de widget no filtro
        self.labelFiltro = ctk.CTkLabel(
            self.gridFiltro,
            text="Filtros",
            font=fonteNormal
        )
        

        # --- frame Amostra (meio, maior) ---
        # frame da amostra (já filho de self.frameCatalogo)
        self.gridAmostra = ctk.CTkFrame(
            self.frameCatalogo,
            fg_color="#353535"
        )
        self.gridAmostra.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # --- configurar tamanho/expansão da área ---
        # aumentar a altura mínima da linha 0 (onde os botões ficarão)
        self.gridAmostra.grid_rowconfigure(0, weight=1, minsize=320)  # 300px de altura mínima

        # configurar 3 colunas, cada uma cresce igualmente; minsize em px (não string)
        self.gridAmostra.grid_columnconfigure(0, weight=1, minsize=240)
        self.gridAmostra.grid_columnconfigure(1, weight=1, minsize=240)
        self.gridAmostra.grid_columnconfigure(2, weight=1, minsize=240)

        
        pil_img = Filmes.importaCapa(self.filmesAmostra[self.filme0].capa,(200,300))
        self.filme0Foto = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(200,300))
        
        self.botaoFilme0 = ctk.CTkButton(
            self.gridAmostra,
            text="",
            command=lambda: self.interfaceFilme(self.filme0),
            image=self.filme0Foto,
            fg_color= "transparent",
            text_color=corBranca,
            height=200,  # altura do botão (px)
            hover=False
        )

        pil_img = Filmes.importaCapa(self.filmesAmostra[self.filme1].capa,(200,300))
        self.filme1Foto = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(200,300))

        self.botaoFilme1 = ctk.CTkButton(
            self.gridAmostra,
            text="",
            image= self.filme1Foto,
            command=lambda: self.interfaceFilme(self.filme1),
            fg_color="transparent",
            text_color=corBranca,
            height=200,
            hover=False
        )

        pil_img = Filmes.importaCapa(self.filmesAmostra[self.filme2].capa,(200,300))
        self.filme2Foto = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(200,300))
        self.botaoFilme2 = ctk.CTkButton(
            self.gridAmostra,
            text="",
            image=self.filme2Foto,
            command=lambda: self.interfaceFilme(self.filme2),
            fg_color="transparent",
            text_color=corBranca,
            height=200,
            hover=False
        )

        # posiciona botões fazendo-os preencher a célula (nsew)
        self.botaoFilme0.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.botaoFilme1.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")
        self.botaoFilme2.grid(row=0, column=2, pady=10, padx=10, sticky="nsew")

        # --- frame Controles (embaixo) ---
        self.gridControles = ctk.CTkFrame(
            self.frameCatalogo,
            height=50,
            fg_color="#5a5a5a"
        )
        self.gridControles.grid(row=2, column=0, sticky="nsew", padx=10, pady=(5,10))

        # cria 2 colunas para os botões voltar e passar
        self.gridControles.grid_columnconfigure(0, weight=1)
        self.gridControles.grid_columnconfigure(1, weight=1)

        # botões de navegação
        self.gridControles.grid_rowconfigure(0, weight=1, minsize=60)

        self.botaoVoltar = ctk.CTkButton(
            self.gridControles,
            text="<<<",
            command=self.voltaFilmes,
            fg_color=corVermelha,
            hover_color=corVermelhaEscura,
            height=50,
            width=70
        )
        self.botaoPassar = ctk.CTkButton(
            self.gridControles,
            text=">>>",
            command=self.passaFilmes,
            fg_color=corVermelha,
            hover_color=corVermelhaEscura,
            height=50,
            width=70
        )

        self.botaoVoltar.grid(row=0, column=0, sticky="se", padx=10, pady=10)
        self.botaoPassar.grid(row=0, column=1, sticky="sw", padx=10, pady=10)

        # --- garante que o logout fique acima de todos os frames ---
        self.botaoLogout.lift()

    def avancar(self,x):
        if x == self.quantidadeFilmes -3:
            return 0
        if x == self.quantidadeFilmes -2:
            return 1
        if x == self.quantidadeFilmes -1:
            return 2
        return x+3
    def retroceder(self,x):
        if x == 0:
            return self.quantidadeFilmes - 3
        if x==1:
            return self.quantidadeFilmes -2
        if x==2:
            return self.quantidadeFilmes -1
        return x-3
    
    def voltaFilmes(self):
        self.filme0 = self.retroceder(self.filme0)
        self.filme1 = self.retroceder(self.filme1)
        self.filme2 = self.retroceder(self.filme2)
        self.limpaTela()
        self.interfaceCatalogo()
    
    def passaFilmes(self):
        self.filme0 = self.avancar(self.filme0)
        self.filme1 = self.avancar(self.filme1)
        self.filme2 = self.avancar(self.filme2)
        self.limpaTela()
        self.interfaceCatalogo()
    
    def interfaceFilme(self,filmeID):
        self.limpaTela()
        obra = self.filmesAmostra[filmeID]
        self.botaoVoltarCadastro = ctk.CTkButton(
            self,
            text='← Voltar',
            command=lambda:self.voltaPagina(self.interfaceCatalogo),
            fg_color=corVermelha,
            hover_color=corVermelhaEscura,
            font=fonteNormal,
            width=100
        )
        self.frameFilme = ctk.CTkFrame(self,
            width=900,
            height=500,
            fg_color= corCinza
            )
        self.frameCapa = ctk.CTkFrame(self.frameFilme,
                    width=300,
                    height=500,
                    fg_color=corCinza)
        
        pil_img = Filmes.importaCapa(obra.capa,(250,375))
        self.capaFilme = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(250,375))

        self.capa = ctk.CTkButton(self.frameCapa,
                    command=lambda:Filmes.abreTrailer(obra.trailer),              
                    image=self.capaFilme, 
                    text="",
                    hover=False,
                    fg_color="transparent")
        
        
       
        
        
        self.frameInformacoes= ctk.CTkFrame(self.frameFilme,
                              width=600,
                              height=500,
                              fg_color=corCinza
                              
                              )
        titulo = f"{obra.titulo} ({obra.ano})"
        self.titulo = ctk.CTkLabel(self.frameInformacoes,
                                   text=titulo,
                                   font=("Arial", 24),
                                   text_color=corBranca
                                   )
                                    
        
        self.diretor = ctk.CTkLabel(self.frameInformacoes,
                                   text=f"{obra.diretor}, {obra.genero}",
                                   font=("Arial", 17),
                                   text_color=corBranca                            
                                   )
        self.sinopse = ctk.CTkLabel(self.frameInformacoes,
                                    text=obra.sinopse,
                                    font=("Arial", 15),
                                    text_color = corBranca,
                                    wraplength=450,   
                                    justify="left")
       
        
        if hasattr(self, "botaoLogout"):
            self.botaoLogout.place(relx=1, x=-10, y=10, anchor='ne')       
        self.botaoVoltarCadastro.place(x=10, y=10)
        
        self.frameFilme.place(relx=0.5, rely=0.5, anchor="center")
        self.frameFilme.grid_columnconfigure(0, weight=1, minsize=300)
        self.frameFilme.grid_columnconfigure(1, weight=2,minsize=600)

        self.frameCapa.grid(row=0,column=0,sticky="w")
        self.capa.pack(expand=True, padx=8, pady=8)
        self.frameInformacoes.grid(row=0,column=1,sticky="n")
        self.titulo.grid(row=0,column=0,pady=(10,0),sticky="n")
        self.diretor.grid(row=1,column=0,sticky="n",pady=2)
        self.sinopse.grid(row=2,column=0,pady=(30,10),sticky="n")
    def fechaJanela(self):
        Login.exportaUsuarios()
        self.destroy()
        
        
        
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
    