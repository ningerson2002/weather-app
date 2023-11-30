from tkinter import *
import requests
import json
from datetime import datetime

# Initialize window
root = Tk()
root.geometry("400x400")  # size of window (default)
root.resizable(0, 0)  # fixed window size

root.title("Weather App -- Nic Ingerson")

city_value = StringVar()


def show_weather():
    # Enter your api key, copies from OpenWeatherMap dashboard
    api_key = "YOUR_API_KEY"

    # Get city name from user
    city_name = city_value.get()

    # API url
    weather_url = (
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city_name
        + "&appid="
        + api_key
    )
    response = requests.get(weather_url)  # get response from fetched url
    weather_info = response.json()  # changing responses from json

    tfield.delete("1.0", "end")  # clear text field for new output

    if weather_info["cod"] == 200:
        kelvin = 273  # value of kelvin

        # Storing fetched values

        temp = int(weather_info["main"]["temp"] - kelvin)
        feels_like_temp = int(weather_info["main"]["feels_like"] - kelvin)
        pressure = weather_info["main"]["pressure"]
        humidity = weather_info["main"]["humidity"]
        wind_speed = weather_info["main"]["wind_speed"] * 3.6
        sunrise = weather_info["sys"]["sunrise"]
        sunset = weather_info["sys"]["sunset"]
        timezone = weather_info["timezone"]
        cloudy = weather_info["clouds"]["all"]
        description = weather_info["weather"][0]["description"]

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        # Assigning values to weather variable

        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather)
