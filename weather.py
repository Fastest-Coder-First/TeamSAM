import requests
import os
import sys
import urllib.error
import click
from PIL import Image
from io import BytesIO
from colorama import Fore, Back, Style
# Function that calls openweather API
def get_weather(city):

    # API Key and URL
    api_key = 'ce5672977fa34059f0b8992a98123ca2'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
        
    # API call
    response = requests.get(url)

    # Convert response to json
    data = response.json()
    st_code = data["cod"]

    # Check if API call was successful
    if st_code != 200:      
        if st_code == 404:
            print(Fore.RED + "City not found.")
        elif st_code == 401:
            print(Fore.RED + "Missing/Invalid API key.")
        else:
            print(Fore.RED + "Something went wrong.")
        return None

    # Get country and city name
    country = data["sys"]["country"]
    city_name = data["name"]

    # Get weather description
    weather_description = data["weather"][0]["description"]

    # Get temperature
    temp = data["main"]["temp"]
    temp = temp - 273.15
    temp = round(temp, 2)

    # Get humidity and windspeed
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]  

    # Get weather icon and URL and description
    weather_icon = data["weather"][0]["icon"]
    weather_icon_url = "http://openweathermap.org/img/w/{}.png".format(weather_icon)
    weather_icon_description = data["weather"][0]["main"]

    # Return weather data
    return {"Country": country, "City": city_name, 
            "Weather Description": weather_description, 
            "Temperature": temp, "Humidity": humidity, "Wind Speed": wind_speed,
            "Weather Icon URL": weather_icon_url, "Weather Icon Description": weather_icon_description}


# To view the image icon
def display_icon(icon_url):
    response = requests.get(icon_url)
    img = Image.open(BytesIO(response.content))
    img.show()


# To display the weather data
def display_weather(city):
    try:
        weather_data = get_weather(city)
        if weather_data is None:
            return

        print(Fore.BLUE+"City: {}, {}".format(weather_data["Country"],weather_data["City"]))
        print(Fore.CYAN+"Weather Description: {}".format(weather_data["Weather Description"]))
        print(Fore.WHITE+ "Temperature: {}".format(weather_data["Temperature"]))
        print(Fore.BLUE+"Humidity: {}".format(weather_data["Humidity"]))
        print(Fore.CYAN + "Wind Speed: {}".format(weather_data["Wind Speed"]))
        display_icon(weather_data["Weather Icon URL"])
        print(Fore.WHITE+"Weather Icon Description: {}".format(weather_data["Weather Icon Description"]))

    except KeyError:
        print(Fore.RED + "Error getting weather data.")
    except TypeError:
        print(Fore.RED + "Error getting weather data for given city.")
    

# Function to get IP address
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


# Function to get location
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

# Main
if __name__ == "__main__":

    # Check if city name is provided
    if len(sys.argv) < 2:
        print(Fore.RED + "Missing required <city_name> argument.")
        print(Fore.GREEN + "Enter: \n1 - To use your current location \n2 - To enter city name")

        # Get user choice
        choice = input()

        if choice == "1":
            location = get_location()
            city = location["city"]

        elif choice == "2":
            city = input()

        else:
            print(Fore.RED + "Invalid choice.")
            sys.exit(1)
    
    else:
        city = " ".join(sys.argv[1:])

    # Display weather for each city
    display_weather(city)
