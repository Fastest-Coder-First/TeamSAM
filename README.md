# TeamSAM
A repository for Fastest Coder First Hackathon

Problem statement : Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

## Description  🌞
'mauSAM', is a simple yet elegant Python based command line tool that accepts a city's name and returns the current weather forecast. It uses OpenWeatherMap API and GitHub's CoPilot to provide a user-friendly experience.

![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/sam)


## Functionalities 🧰
1. Can forecast the weather of any city of your choice or your current location
   
2. Displays the following weather information:
   
   - City and Country
   - Weather Description (Scattered clouds, haze, etc)
   - Temperature (Celsius scale)
   - Humidity (Percentage)
   - Wind Speed (Kmph)

## Installation ✅

- Ensure you have Python 3.x installed.
- Clone the repository - 
```git clone https://github.com/Fastest-Coder-First/TeamSAM.git```
- To install required dependencies -
```pip install -r requirements.txt```
- Head on to - https://openweathermap.org/api to get your own API-KEY and
enter it into the file weather.py at the designated variable.

## API Key 🔐

To retrieve weather data, the application uses the OpenWeather API. You need to provide your own API key by replacing the api_key variable in the code with your API key.

You can sign up and obtain an API key from the [OpenWeather website](https://openweathermap.org/).

## Demo ✨

We have demonstrated four possibles scenarios while implementing the weather forecasting tool:

1. Passing city name
   
      ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Image1)


2. User (Current) location
   
      ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Image2)


3. City name with empty flags

      ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Image3)
  
4. Current User Location with empty flags
   
      ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Image4)

## Architectural Description

- Import the required modules
- Get the API Key and the city name from the user
- If specified obtain user location using their IP address
- Construct the API URL and make a request
- Check the status code of obtained data
- Parse the JSON data and extract all the relevant information
- Display the information to the user

## Usage of GitHub CoPilot 🤖

GitHub CoPilot has been used as a basis for our code implementation

- To make API calls to obtain weather parameters
- For error handling of HTTP Requests
- Aided in passing the data to obtain necessary values
- Enabled us to implement the 'click' command to handle user's choices
  
## Acknowledgments 📝

- This application uses the [OpenWeather API](https://openweathermap.org/) to retrieve weather data.

- GitHub CoPilot for our code implementation

## Contributers 🌻

   Saakshi Sanjeev

   Arati Menon

   Maalavika Srikantan
