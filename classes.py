import requests
class Login:
    def __init__(self,id,nome,usuario,senha):
        self.id = id
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
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
class Filmes:
    def __init__(self,codigo,nome,sinopse,genero,diretor,ano,capa,trailer):
       self.codigo = codigo
       self.titulo = titulo
       self.sinopse = sinopse
       self.genero = genero
       self.diretor = diretor
       self.ano = ano
       self.capa = capa
       self.trailer = trailer
       
       
    def alteraNome(self,titulo):
        self.titulo = titulo
        
    def alteraSinopse(self,sinopse):
        self.sinopse = sinopse
        
    def alteraGenero(self,genero):
        self.genero = genero
        
    def alteraDiretor(self,diretor):
        self.diretor = diretor
    
    def alteraAno(self,ano):
        self.ano = ano
        
    def alteraCapa(self,capa):
        self.capa = capa
        
    def alteraTrailer(self,trailer):
        self.trailer = trailer
        
    

'''class Filtro:
    
class Sistema:'''
    
