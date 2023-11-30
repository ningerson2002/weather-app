![Workflow Badge](https://img.shields.io/github/actions/workflow/status/ningerson2002/weather-app/python-app.yml
)

- [Weather App :cloud:](#weather-app-cloud)
  - [Overview](#overview)
    - [Key Features](#key-features)
    - [Dependencies](#dependencies)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Technologies Used](#technologies-used)
  - [License](#license)
  - [Disclaimer](#disclaimer)

# Weather App :cloud:

## Overview

This is a simple yet powerful weather application built in Python. It provides real-time weather information for any location, giving users access to current conditions, forecasts, and more. The app utilizes the OpenWeatherMap API to fetch accurate and up-to-date weather data.

### Key Features

- Displays temperature (in Celsius), feels like temperature, pressure, humidity, sunrise, sunset, cloudiness, and weather description.
- Provides error handling for cases where the entered city name is not found.

### Dependencies

- `tkinter`: Used for creating the graphical user interface.
- `requests`: Used for making HTTP requests to the OpenWeatherMap API.
- `json`: Used for handling JSON responses.
- `datetime`: Used for formatting time information.

## Prerequisites

Before running the program, make sure you have the following:

- Python installed on your machine.
- An API key from OpenWeatherMap. You can obtain a _free_ API key by signing up on the [OpenWeatherMap website](https://openweathermap.org/).

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/ningerson2002/weather-app.git
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `YOUR_API_KEY` in the code with your actual API key.

4. Run the app:

   ```bash
   python weather_app.py
   ```

## Usage

1. Run the app.

2. Enter desired city name in the input field.

3. Click the "Check Weather" button to retrieve and display the current weather information for the specified city.

## Technologies Used

- **Python:** The core programming language for the application.
- **Requests:** Used for making HTTP requests to the OpenWeatherMap API.
- **Tkinter:** The GUI toolkit for creating the graphical user interface.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Make sure to handle your OpenWeatherMap API key securely and avoid sharing it publicly.
