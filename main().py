import json
from login import *
from interface import *
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
#tela de login
usuario,senha = Interface.telaLogin()

    
    
    
    
    
    
    
    
    
#exporta os usuários
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