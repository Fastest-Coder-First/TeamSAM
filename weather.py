# Function that calls openweather API to forecast weather o city gives as input

import requests
import json
import os

from PIL import Image

from io import BytesIO

def weather(city):

    # API Key and URL
    api_key = 'ce5672977fa34059f0b8992a98123ca2'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)

    # API call
    response = requests.get(url)

    # Convert response to json
    data = response.json()

    
    # Check if the city exists
    if data["cod"] == 404:
        return "City not found."
    
    # Handle web error
    if data["cod"] != 200:
        return "Error hitting the API."
    
    # Get weather description
    weather_description = data["weather"][0]["description"]

    # Get temperature
    temp = data["main"]["temp"]
    temp = temp - 273.15
    temp = round(temp, 2)

    print(data)

    # Get humidity
    humidity = data["main"]["humidity"]

    # Get wind speed
    wind_speed = data["wind"]["speed"]

    # Get country
    country = data["sys"]["country"]
    city_name = data["name"]

    # Get sunrise and sunset
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]

    # Get timezone
    timezone = data["timezone"]

    # Get coordinates
    coordinates = data["coord"]

    # Get weather icon
    weather_icon = data["weather"][0]["icon"]

    # Get weather icon url
    weather_icon_url = "http://openweathermap.org/img/w/{}.png".format(weather_icon)

    # Get weather icon description
    weather_icon_description = data["weather"][0]["main"]

    # Return weather data
    return { "weather_description": weather_description, "temp": temp, "humidity": humidity, "wind_speed": wind_speed, "country": country, "sunrise": 
            sunrise, "sunset": sunset, "timezone": timezone, "city_name": city_name, "coordinates": coordinates, "weather_icon_url": 
            weather_icon_url, "weather_icon_description": weather_icon_description }



# To view the image icon
def imaginy(city):
    weather_data = weather(city)
    weather_icon_url = weather_data["weather_icon_url"]
    print(weather_data)
    response = requests.get(weather_icon_url)
    img = Image.open(BytesIO(response.content))
    img.show()


if len(sys.argv) < 2:
    print("Usage: python weather.py <city_name>")
    sys.exit(1)

# Get the city name from the command line argument
city_name = sys.argv[1]
imaginy(city_name)
