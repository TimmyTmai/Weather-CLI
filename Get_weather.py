import json
import os
from http.client import responses

import requests

API_KEY = "be55774adbb9b0272845109b01bc4853"

def get_cordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    responese = requests.get(url)

    if responese.status_code == 200:
        data = responese.json()
        if len(data) > 0:
            lat = data[0]["lat"]
            lon = data[0]["lon"]
            return lat, lon
        else:
            print("city not found")
            return None, None
    else:
        print("Error with the request.")
        return None, None
def get_weather(lat,lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()


while True:
    city = input("Enter city name (or type 'quit' to exit): ")

    if city.lower() == "quit":
        print("Goodbye!")
        break
    lat, lon = get_cordinates(city)
    weather = get_weather(lat, lon)

    print(weather["main"], weather["weather"][0]['main'])
