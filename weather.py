import requests
import os
import sys
import click
from io import BytesIO
from colorama import Fore


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
            print(Fore.RED + "City not found." + Fore.RESET)
        elif st_code == 401:
            print(Fore.RED + "Missing/Invalid API key." + Fore.RESET)
        else:
            print(Fore.RED + "Something went wrong." + Fore.RESET)
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


    # Return weather data
    return {"Country": country, "City": city_name, 
            "Weather Description": weather_description, 
            "Temperature": temp, "Humidity": humidity, "Wind Speed": wind_speed}


# To display the weather data
def display_weather(city):
    try:
        weather_data = get_weather(city)
        if weather_data is None:
            return

        print(Fore.GREEN+"City: {}, {}".format(weather_data["Country"],weather_data["City"]) + Fore.RESET)
        print(Fore.CYAN+"Weather Description: {}".format(weather_data["Weather Description"]) + Fore.RESET)
        print(Fore.WHITE+ "Temperature: {} °C".format(weather_data["Temperature"]) + Fore.RESET)
        print(Fore.BLUE+"Humidity: {} %".format(weather_data["Humidity"]) + Fore.RESET)
        print(Fore.CYAN + "Wind Speed: {} km/h".format(round(weather_data["Wind Speed"] * 18 / 5)) + Fore.RESET)

    except KeyError:
        print(Fore.RED + "Error getting weather data." + Fore.RESET)
    except TypeError:
        print(Fore.RED + "Error getting weather data for given city." + Fore.RESET)
    

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
@click.command()
@click.option("--city", help="Specify the city for which you want to get weather information.")
@click.option("--current-location", is_flag=True, help="Use your current location.")
def main(city, current_location):
    if current_location:
        location = get_location()
        city = location["city"]
    elif not city:
        print(Fore.RED + "Missing required --city argument or --current-location flag." + Fore.RESET)
        print(Fore.YELLOW + "Enter: \n1 - To use your current location \n2 - To enter city name" + Fore.RESET)

        # Get user choice
        choice = input()

        if choice == "1":
            location = get_location()
            city = location["city"]

        elif choice == "2":
            city = input()

        else:
            print(Fore.RED + "Invalid choice." + Fore.RESET)
            sys.exit(1)
        
    display_weather(city)


if __name__ == "__main__":
    main()
