class Filtro:
    def buscaGenero(listaFilmes,genero):
        filmes = []
        for i in listaFilmes:
            if genero in i:
                filmes.append(i)
        return filmes
    
    def buscaAno(listaFilmes,ano):
        filmes = []
        for i in listaFilmes:
            if ano in i:
                filmes.append(i)
        return filmes
    
    def buscaDiretor(listaFilmes,diretor):
        filmes = []
        for i in listaFilmes:
            if diretor in i:
                filmes.append(i)
        return filmes
    
    def reuneFilmes(listaDiretor,listaGenero,listaAno):
        filmes = listaDiretor + listaGenero + listaAno
        return filmes
        