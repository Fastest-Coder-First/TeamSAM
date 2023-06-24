import requests
import json
import os
import sys

from PIL import Image
from io import BytesIO

# Function that calls openweather API
def get_weather(city):
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

        # Get country and city name
    country = data["sys"]["country"]
    city_name = data["name"]

    # Get weather description
    weather_description = data["weather"][0]["description"]

    # Get temperature
    temp = data["main"]["temp"]
    temp = temp - 273.15
    temp = round(temp, 2)

    # Get humidity
    humidity = data["main"]["humidity"]

    # Get wind speed
    wind_speed = data["wind"]["speed"]

    # Get sunrise and sunset
    sunrise = data["sys"]["sunrise"]
    sunset = data["sys"]["sunset"]    

    # Get weather icon
    weather_icon = data["weather"][0]["icon"]

    # Get weather icon url
    weather_icon_url = "http://openweathermap.org/img/w/{}.png".format(weather_icon)

    # Get weather icon description
    weather_icon_description = data["weather"][0]["main"]

    # Return weather data
    return {"Country": country, "City": city_name, 
            "Weather Description": weather_description, 
            "Temperature": temp, "Humidity": humidity, "Wind Speed": wind_speed, 
            "Sunrise": sunrise, "Sunset": sunset, 
            "Weather Icon URL": weather_icon_url, "Weather Icon Description": weather_icon_description}


# To view the image icon
def display_icon(icon_url):
    response = requests.get(icon_url)
    img = Image.open(BytesIO(response.content))
    img.show()


# To display the weather data
def display_weather(city):
    weather_data = get_weather(city)

    print("City: {}, {}".format(weather_data["Country"], weather_data["City"]))
    print("Weather Description: {}".format(weather_data["Weather Description"]))
    print("Temperature: {}".format(weather_data["Temperature"]))
    print("Humidity: {}".format(weather_data["Humidity"]))
    print("Wind Speed: {}".format(weather_data["Wind Speed"]))
    print("Sunrise: {}".format(weather_data["Sunrise"]))
    print("Sunset: {}".format(weather_data["Sunset"]))
    display_icon(weather_data["Weather Icon URL"])
    print("Weather Icon Description: {}".format(weather_data["Weather Icon Description"]))



#function to get ip address
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

#function to get location
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data

# Test
if __name__ == "__main__":
    display_weather("London")
    location = get_location()
    display_weather(location['city'])

'''if len(sys.argv) < 2:
    print("Usage: python weather.py <city_name>")
    sys.exit(1)

# Get the city name from the command line argument
city_name = sys.argv[1]
imaginy(city_name)'''
