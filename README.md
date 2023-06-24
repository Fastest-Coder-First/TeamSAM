# TeamSAM
A repository for Fastest Coder First Hackathon

Problem statement : Weather Forecasting Tool - Create a command line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python. Your solution should demonstrate how GitHub Copilot can help you with API usage, data parsing, and error handling.

## Description
Given a location, the Command Line Interface displays the weather forecast for the place using the Open Weather Map API

![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/sam)


## Functionalities
1. Can forecast the weather of any city of your choice or your current location
   
2. Displays the following weather information:
   
   - City and Country
   - Weather Description (Scattered clouds, haze, etc)
   - Temperature (Celsius scale)
   - Humidity (Percentage)
   - Wind Speed (Kmph)

## Installation

- Ensure you have Python 3.x installed.
- Clone the repository - 
```git clone https://github.com/Fastest-Coder-First/TeamSAM.git```
- To install required dependencies -
```pip install -r requirements.txt```
- Head on to - https://openweathermap.org/api to get your own API-KEY.
Enter it into the file weather.py at the designated variable.

## API Key

To retrieve weather data, the application uses the OpenWeather API. You need to provide your own API key by replacing the api_key variable in the code with your API key. You can sign up and obtain an API key from the [OpenWeather website](https://openweathermap.org/).

## Demo

We have demonstrated four possibles scenarios while implementing the weather forecasting tool:

1. Passing city name
   
      ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Image1)


2. User (Current) location
   
      ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Image2)


3. City name with empty flags

      ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Image3)
  
4. Current User Location with empty flags
   
      ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Image4)
   
## Usage of GitHub CoPilot

## Acknowledgments 

- This application uses the [OpenWeather API](https://openweathermap.org/) to retrieve weather data.

- GitHub CoPilot for our code implementation

## Open to contributions
