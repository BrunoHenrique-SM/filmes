import requests

import requests

# Substitua 'YOUR_API_KEY' pela sua chave de API do TMDb
API_KEY = 'ab071d5e175f4434c2ab6124c5090b41'
BASE_URL = 'https://api.themoviedb.org/3/discover/movie'

# Parâmetros da requisição
params = {
    'api_key': API_KEY,
    'language': 'pt-BR',  # Idioma dos resultados
    'sort_by': 'popularity.desc',  # Ordenar por popularidade decrescente
    'page': 1  # Página de resultados
}

# Realiza a requisição GET
response = requests.get(BASE_URL, params=params)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    for movie in data['results']:
        print(f"Título: {movie['title']}")
        print(f"Data de Lançamento: {movie['release_date']}")
        print(f"Descrição: {movie['overview']}")
        print('-' * 50)
else:
    print(f"Erro na requisição: {response.status_code}")