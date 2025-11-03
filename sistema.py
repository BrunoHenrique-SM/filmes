import json
from filmes import *            
#class Sistema:    
class Login:
    def __init__(self,id,nome,email,usuario,senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha
        self.filmes = []

    def importaUsuarios():
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
        return usuarios
    
    def exportaUsuarios():
        usuariosDicionario = [
            {
                "id": u.id,            # se você tiver um atributo id
                "nome": u.nome,
                "usuario": u.usuario,
                "senha": u.senha,
                "email": u.email
            }
            for u in usuarios
        ]   
        f = open("usuarios.json","w")
        json.dump(usuariosDicionario,f)
        f.close()
    def separaNome(nome):
        nomesLista = [x.upper() for x in nome.split()]
        for i in nomesLista:
            if len(i) <=2:
                nomesLista.remove(i)
        return nomesLista
        
        
    def confirmaUsuario(nomeUsuario,usuarios):
        for i in usuarios:
            if nomeUsuario == i.usuario:
                return True,i.id
        return False, len(usuarios)
            
    def confirmaEmail(email,usuarios):
        for i in usuarios:
            if email == i.email:
                return True,i.id
        return False,len(usuarios)
    
    def confirmaSenha(senha, id, usuarios):
        try:
            if senha == usuarios[id].senha:
                return True
            return False
        except IndexError:
            return False
    
    def verificaSenha(senha,nomes):
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
        
usuarios = Login.importaUsuarios()
