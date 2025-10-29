import customtkinter as ctk

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title("MDBB")
app.geometry('800x800')
#label
tituloUsuario = ctk.CTkLabel(app,text='Usuário ou email:')
tituloUsuario.pack(pady=20)
#entry
campoUsuario = ctk.CTkEntry(app,placeholder_text = " Digite o nome de usuário ou email")
campoUsuario.pack()

#label
tituloSenha = ctk.CTkLabel(app,text='Senha:')
tituloSenha.pack(pady=20)
#entry
campoSenha = ctk.CTkEntry(app,placeholder_text = "Senha")
campoSenha.pack()


ctk.CTkButto(app,text='Login',command=Login)
c

#button
app.mainloop()