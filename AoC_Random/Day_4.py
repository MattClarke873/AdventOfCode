import requests
import pprint as pp


def get_weather(lat, lon):

    URL = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    # A GET request to the API
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        # Print the response
        
        latitude = round((data["latitude"]),6)
        longitude = round((data["longitude"]),6)
        temperature = (data["current_weather"]["temperature"])
        windspeed = (data["current_weather"]["windspeed"])

        print(f'Weather at ({latitude},{longitude})\nTemperature: {temperature} °C\nWind Speed: {windspeed} m/s')
    else:
        print("Error fetching data!")
        data = None


#57.1499° N, 2.0938° W

get_weather("57.1499", "-2.0938")