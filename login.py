import requests
from tkinter import *
from sistema import *
class Login:
    def __init__(self,id,nome,usuario,senha,email):
        self.id = id
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha
    '''def confirmaLogin(usuario,senha,usuarios):
        n = -1
        for i,n in enumerate usuarios:
            if usuario in i:
                id = n
        if n = -1:
            return "Usuário ou email não encontrado"
        else:'''
            
    def criaUsuario(usuarios):
        print("Nome")
        nome = Sistema.capturaNome()
        nomesLista = [x.upper() for x in nome.split()]
        for i in nomesLista:
            if len(i) <=2:
                nomesLista.remove(i)
        print(nome)
        while True:
            print("Usuário")
            nomeUsuario = Sistema.capturaNome()
            verificaUsuario = Login.confirmaUsuario(nomeUsuario,usuarios)
            if not verificaUsuario:
                break
            print("Nome de usuário já utilizado")
        while True:
            print("Email")
            email = Sistema.capturaEmail()
            verificaEmail = Login.confirmaEmail(email,usuarios)
            if not verificaEmail:
                break
            print("Email já utilizado")
                    
        while True:
            print("Senha")
            senha = Sistema.capturaSenha()
            print("Confirme a senha")
            senha2 = Sistema.capturaSenha()
            verificaSenha = Login.confirmaSenha(senha,nomesLista)
            if verificaSenha and senha == senha2:
                break
            print("Senha inválida")
            
        usuarios.append([nome,nomeUsuario,email,senha])
        
        return usuarios    
        
    
    def alteraNome(self,nome):
        self.nome = nome
        
    def alteraUsuario(self,usuario):
        self.usuario = usuario
        
    def alteraSenha(self,senha):
        self.senha = senha
        
    def mudarSenha(self):
        while True:
            senhaAntiga = input("Digite a senha antiga: ")
            if senhaAntiga == self.senha:
                break
            else:
                print("Senha incorreta")
    def confirmaUsuario(nomeUsuario,usuarios):
        for i in usuarios:
            if nomeUsuario in usuarios:
                return True
        return False
            
    def confirmaEmail(email,usuarios):
        for i in usuarios:
            if email in usuarios:
                return True
        return False
                
    def confirmaSenha(senha,nomes):
        numero = False
        letra = False
        maiusculo = False
        especial = False
        nome = True
        letras = "abcdefghijklmnopqrstuvwxyz"
        letrasMaiusculas = letras.upper()
        especiais = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~çáéíóúàèìòùãõâêîôûäëïöüÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÄËÏÖÜ"
        for i in senha:
            if i in "0123456789":
                numero = True
                
            if i in letras:
                letra = True
                
            if i in letrasMaiusculas:
                maiusculo = True
                
            if i in especiais:
                especial = True
        for i in nomes:
            if i in senha.upper():
                nome = False
                
        if numero and letra and maiusculo and especial and nome:
            return True
        else:    
            return False

        


    


                
        
    


    
