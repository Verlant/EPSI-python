import requests

station_information = requests.get('https://gbfs.citibikenyc.com/gbfs/fr/station_information.json')
stations = station_information.json()["data"]["stations"]
# for station in stations:
#     print(str(station["name"]) + " : " + str(station["capacity"]))

# station_status = requests.get('https://gbfs.citibikenyc.com/gbfs/fr/station_status.json')
# stations = station_status.json()["data"]["stations"]
# stations_active = 0
# stations_HS = 0
# velos_electrique = 0
# velos_classique = 0
# for station in stations:
#     if station["is_installed"]:
#         stations_active += 1
#     else:
#         stations_HS += 1
#     velos_electrique += station["num_ebikes_available"]
#     velos_classique += station["num_bikes_available"]


# print("Nombre de stations actives : " + str(stations_active))
# print("Nombre de stations HS : " + str(stations_HS))
# print("Ratio de stations en service : " + str(stations_active / len(stations)))

# print("Nombre de vélos électriques : " + str(velos_electrique))
# print("Nombre de vélos classiques : " + str(velos_classique))
# print("Ratio de vélos électriques : " + str(velos_electrique / (velos_classique + velos_electrique)))
