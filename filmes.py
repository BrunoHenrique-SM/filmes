from io import BytesIO
#from filtro import *
import requests
from PIL import Image
import customtkinter as ctk

import json
import webbrowser
class Filmes:
    def __init__(self,codigo,titulo,sinopse,genero,diretor,ano,capa,trailer):
       self.codigo = codigo
       self.titulo = titulo
       self.sinopse = sinopse
       self.genero = genero
       self.diretor = diretor
       self.ano = ano
       self.capa = capa
       self.trailer = trailer
       

    def exportaFilmes(filmesLista):
        dados = []
        for filme in filmesLista:
            dados.append({
                "codigo": filme.codigo,
                "titulo": filme.titulo,
                "sinopse": filme.sinopse,
                "genero": filme.genero,
                "diretor": filme.diretor,
                "ano": filme.ano,
                "capa": filme.capa,
                "trailer": filme.trailer
            })

        with open("filmes.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

    
        
    def importaFilmes():
        filmesLista = []
        try:
            with open("filmes.json", "r", encoding="utf-8") as f:
                dados = json.load(f)

            for item in dados:
                filme = Filmes(
                    codigo=item.get("codigo"),
                    titulo=item.get("titulo"),
                    sinopse=item.get("sinopse"),
                    genero=item.get("genero"),
                    diretor=item.get("diretor"),
                    ano=item.get("ano"),
                    capa=item.get("capa"),
                    trailer=item.get("trailer")
                )
                filmesLista.append(filme)

            print(f"✅ {len(filmesLista)} filmes importados com sucesso!")
            return filmesLista

        except FileNotFoundError:
            print("⚠️ Arquivo 'filmes.json' não encontrado.")
            return []
        except json.JSONDecodeError:
            print("⚠️ Erro ao ler o arquivo 'filmes.json'. Formato inválido.")
            return []
        
    
    def importaCapa(url: str, size: tuple):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            img = Image.open(BytesIO(r.content)).convert("RGBA")
            img.thumbnail(size, Image.LANCZOS)
            return img
        except Exception as e:
            print("Erro ao carregar imagem:", e)
            return None
    def abreTrailer(url):
        webbrowser.open(url)

class Filtro:
    def __init__(self):
        pass
    def geraFiltros(lista):
        generados = []
        if lista[0]:
            generados.append("Ação")
        if lista[1]:
            generados.append("Ficção Científica")
        if lista[2]:
            generados.append("Comédia")
        if lista[3]:
            generados.append("Drama")
        if lista[4]:
            generados.append("Thriller")
        if lista[5]:
            generados.append("Animação")
        if lista[6]:
            generados.append("Fantasia")
        if lista[7]:
            generados.append("Terror")
        
        return generados
    
    def filtraFilmes(filtros):
        filtros = Filtro.geraFiltros(filtros)
        
        filmesFiltrados = []
        for i in filtros:
            print(i)
            for j in filmesLista:
                if i in j.genero:
                    
                    filmesFiltrados.append(j)
        return filmesFiltrados

filmesLista=Filmes.importaFilmes()
