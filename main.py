import json

import requests

data_json = requests.get("https://swapi.dev/api/people/")
data = json.loads(data_json.text)
for ch in data['results']:
    home_world = ch['homeworld']
    home_world_json = requests.get(home_world)
    home_world = json.loads(home_world_json.text)
    home_world = home_world['name']
    starships = ch['starships']
    if starships:
        starships_name = []
        for el in starships:
            starships_json = requests.get(el)
            starships_data = json.loads(starships_json.text)
            starships_name.append(starships_data['name'])
        print(f"Имя: {ch['name']}\n"
              f"Рост: {ch['height']}\n"
              f"Родная планета: {home_world}\n"
              f"Космические корабли:", end=' ')
        for el in starships_name:
            if el == starships_name[starships_name.__len__() - 1]:
                print(f"{el}\n")
            else:
                print(f"{el}", end=', ')
        continue

    print(f"Имя: {ch['name']}\n"
          f"Рост: {ch['height']}\n"
          f"Родная планета: {home_world}\n")