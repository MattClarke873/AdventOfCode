from PIL import Image
import requests
from io import BytesIO
import pprint as pp

url = "https://opensky-network.org/api/states/all"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    states = data.get('states', [])

    # OpenSky state fields (index reference)
    fields = [
        "icao24",          # 0
        "callsign",        # 1
        "origin_country",  # 2
        "time_position",   # 3
        "last_contact",    # 4
        "longitude",       # 5
        "latitude",        # 6
        "baro_altitude",   # 7
        "on_ground",       # 8
        "velocity",        # 9
        "heading",         # 10
        "vertical_rate",   # 11
        "sensors",         # 12
        "geo_altitude",    # 13
        "squawk",          # 14
        "spi",             # 15
        "position_source"  # 16
    ]

    """
    area top right   61.158890  0.814952
    area bottom left 57.070561  -4.663027 """
icaos = []
for state in states:
    lon = state[5]
    lat = state[6]
    if lon and -4.663027 <= lon <= 0.814952:
        if lat and 57.07056 <= lat <= 61.15889:
            # Create a dict for easier readability
        #state_dict = {fields[i]: state[i] for i in range(len(fields))}
        #pp.pprint(state_dict)
            icaos.append(state[0])
            
            
for icao in icaos:
                
    url2 = f"https://hexdb.io/api/v1/aircraft/{icao}"


    response = requests.get(url2)

#    response_url.raise_for_status()  # ensure download worked
    if response.status_code == 200:
        data2 = response.json()  
        print(f'{icao} :- {data2["Registration"]} :- {data2["Manufacturer"]} :- {data2["Type"]} ')
    else:
        print(f"Request failed with status code {response.status_code}")




