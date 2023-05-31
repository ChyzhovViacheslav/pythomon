import requests, random, json
from pockemon import Pockemon

enemy_pockemons = []


def set_enemy_pockemons():
    for _ in range(3):
        random_number = random.randint(1, 1281)
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1281&offset=0")
        data_pockemon = response.json()
        data_pockemon_url = data_pockemon["results"][random_number]["url"]
        pockemon_response = requests.get(data_pockemon_url).json()

        name = pockemon_response["name"]
        hp = pockemon_response["stats"][0]["base_stat"]
        attack = pockemon_response["stats"][1]["base_stat"]
        defense = pockemon_response["stats"][2]["base_stat"]

        enemy_pockemon = Pockemon(name, hp, attack, defense)
        enemy_pockemons.append(enemy_pockemon)


set_enemy_pockemons()
