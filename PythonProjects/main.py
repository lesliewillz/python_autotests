import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ecab0473e6e9e0ef374abdf24fa0add7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change_name = {
    "pokemon_id": "188009",
    "name": "Огонек",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)