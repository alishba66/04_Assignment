# Weather Program

import requests

API_KEY = 'your_api_key_here'  # ← Replace with your OpenWeatherMap API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # or 'imperial' for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"\n🌍 Weather in {data['name']}, {data['sys']['country']}:")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
        print(f"📖 Description: {data['weather'][0]['description'].capitalize()}")
    else:
        print("\n❌ City not found. Please check the spelling.")

if __name__ == '__main__':
    city = input("Enter city name: ")
    get_weather(city)
