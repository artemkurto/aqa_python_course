import requests
import json

url = 'https://swapi.dev/api/starships/'
response = requests.get(url)

falcon_ship = None
for ship in response.json()["results"]:
    if ship["name"] == "Millennium Falcon":
        falcon_ship = ship
        break

required_pilot_keys = ('name', 'height', 'mass', 'homeworld')
pilots = []
for pilot_url in falcon_ship['pilots']:
    pilot_data = requests.get(pilot_url).json()
    filtered_pilot_data = {key: pilot_data[key] for key in required_pilot_keys}
    pilots.append(filtered_pilot_data)


for pilot in pilots:
    homeworld_url = pilot['homeworld']
    homeworld_name = requests.get(homeworld_url).json()['name']
    pilot['homeworld_name'] = homeworld_name

required_ship_keys = ('name', 'max_atmosphering_speed', 'starship_class', 'pilots')
falcon_ship_data = {key: falcon_ship[key] for key in required_ship_keys}
falcon_ship_data['pilots'] = pilots

with open("Millennium_Falcon.json", "w") as f:
    json.dump(falcon_ship_data, f, indent=4)
