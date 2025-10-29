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