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
```
git clone https://github.com/Fastest-Coder-First/TeamSAM.git
```
- To install required dependencies -
```
pip install -r requirements.txt
```
- Head on to - https://openweathermap.org/api to get your own API-KEY and
enter it into the file weather.py at the designated variable.

## API Key 🔐

To retrieve weather data, the application uses the OpenWeather API. You need to provide your own API key by replacing the api_key variable in the code with your API key.

You can sign up and obtain an API key from the [OpenWeather website](https://openweathermap.org/).

## Usage 📖

The help manual of the tool can be called as follows to get the weather on the required city: 
```
py weather.py --help
```
![alt Help](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/help)

If no arguments have been given, you will prompted to give the name of the city as soon as the program executes.

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

## Architectural Description 🔨

- Import the required modules
- Get the API Key and the city name from the user
- If specified obtain user location using their IP address
- Construct the API URL and make a request
- Check the status code of obtained data
- Parse the JSON data and extract all the relevant information
- Display the information to the user


  ![alt Weather](https://github.com/Fastest-Coder-First/TeamSAM/blob/main/Output_Screenshots/Block_Diagram)

## Usage of GitHub CoPilot 🤖

GitHub Copilot has been used as a basis for our code implementation

- Increased productivity
- Reduced development time by filling in snippets of code
- To make API calls to obtain weather parameters
- For error handling of HTTP Requests
- Assisted in the use of libraries we were unfamiliar with
- Enabled us to implement the 'click' command to handle user's choices
  
## Acknowledgments 📝

- This application uses the [OpenWeather API](https://openweathermap.org/) to retrieve weather data.

- GitHub Copilot for our code implementation

## Open to contributions 
We welcome contributions! Please follow these steps to contribute:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <branch_name>/main`
5. Create the pull request.

Thank you for contributing!

## Contributers 🌻

   [Saakshi Sanjeev](https://github.com/Si1verKnight)

   [Arati Menon](https://github.com/menon123)

   [Maalavika Srikantan](https://github.com/MaalavikaS)
