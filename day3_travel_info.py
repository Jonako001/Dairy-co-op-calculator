import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    # Error type 1: Invalid key
    if response.status_code == 401:
        print("401 - Invalid API key. Check OPENWEATHER_API_KEY in .env")
        return None
    # Error type 2: City not found
    if response.status_code == 404:
        return None
    if response.status_code == 200:
        return response.json()
    print(f"Weather API Error {response.status_code}")
    return None

def get_country_info(country_code):
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                return data[0] if data else None
            return data  # it's already a dict
    except:
        pass
    return None

def run_tool():
    print("Travel Weather Tool")
    print("-------------------")
    city = input("Enter a city name: ").strip()
    if not city:
        print("No city entered. Exiting.")
        return
    print(f"\nFetching data for {city}...")
    weather_data = get_weather(city)
    if not weather_data:
        print(f"Could not find weather data for '{city}'. Check the city name and try again.")
        return
    country_code = weather_data["sys"]["country"]
    country_data = get_country_info(country_code)

    print(f"\n=== {city.title()}, {country_code} ===")
    print(f"Temperature : {weather_data['main']['temp']}C")
    print(f"Condition   : {weather_data['weather'][0]['description'].title()}")
    print(f"Humidity    : {weather_data['main']['humidity']}%")
    print(f"Wind        : {weather_data['wind']['speed']} m/s")

    if country_data:
        population = country_data.get("population", 0)
        region = country_data.get("region", "Unknown")
        currencies = ", ".join(country_data.get("currencies", {}).keys())
        print(f"\n=== Country Info ===")
        print(f"Region      : {region}")
        print(f"Population  : {population:,}")
        print(f"Currency    : {currencies}")

run_tool()