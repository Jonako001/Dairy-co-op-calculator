"""
Travel Weather & Country Info Tool - Day 3

Problem it solves:
A traveler wants to know current weather AND country facts (population, region, currency) 
for any city in the world in one command.

How to run:
1. Create .env file with: OPENWEATHER_API_KEY=your_key_here
2. pip install requests python-dotenv
3. python day3_travel_info.py
4. Enter city name when prompted (e.g., Nairobi, Lagos, Mombasa)

APIs used:
- OpenWeatherMap (weather) - needs API key
- RestCountries (country info) - free, no key

Output:
- Clean readable report for non-technical user
- Saves raw responses to {city}_weather.json and {city}_country.json
"""

import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """Fetch weather from OpenWeatherMap API."""
    if not api_key:
        print("Error: OPENWEATHER_API_KEY not found in .env file")
        return None
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 401:
            print("Error 401: Invalid API key. Check your .env file")
            return None
        if response.status_code == 404:
            print(f"Error 404: City '{city}' not found")
            return None
        if response.status_code == 200:
            return response.json()
        print(f"Weather API error: {response.status_code}")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection")
        return None

def get_country_info(country_code):
    """Fetch country info from RestCountries API."""
    url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Handle API returning list or dict
            if isinstance(data, list) and data:
                return data[0]
            return data if isinstance(data, dict) else None
        return None
    except requests.exceptions.ConnectionError:
        print("Could not fetch country info - no internet")
        return None

def save_to_file(data, filename):
    """Save API response to local JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"✓ Saved to {filename}")
    except Exception as e:
        print(f"Could not save file: {e}")

def run_tool():
    """Main tool - takes user input, combines 2 APIs, displays results."""
    print("=" * 40)
    print("TRAVEL WEATHER & COUNTRY TOOL")
    print("=" * 40)
    city = input("Enter a city name: ").strip()

    if not city:
        print("No city entered. Please try again with a city name.")
        return

    print(f"\nFetching live data for {city}...")
    weather_data = get_weather(city)

    if not weather_data:
        print(f"\nCould not get data for '{city}'. Check spelling and try again.")
        print("Examples: Nairobi, Lagos, Mombasa, London, Tokyo")
        return

    country_code = weather_data["sys"]["country"]
    country_data = get_country_info(country_code)

    # --- CLEAN OUTPUT FOR NON-TECHNICAL USER ---
    print(f"\n{'='*40}")
    print(f"WEATHER IN {city.upper()}, {country_code}")
    print(f"{'='*40}")
    print(f"Temperature : {weather_data['main']['temp']}°C (feels like {weather_data['main']['feels_like']}°C)")
    print(f"Condition   : {weather_data['weather'][0]['description'].title()}")
    print(f"Humidity    : {weather_data['main']['humidity']}%")
    print(f"Wind Speed  : {weather_data['wind']['speed']} m/s")

    if country_data:
        population = country_data.get("population", 0)
        region = country_data.get("region", "Unknown")
        currencies = ", ".join(country_data.get("currencies", {}).keys()) or "Unknown"
        capital = ", ".join(country_data.get("capital", [])) or "Unknown"

        print(f"\n{'='*40}")
        print(f"COUNTRY INFO: {country_code}")
        print(f"{'='*40}")
        print(f"Capital     : {capital}")
        print(f"Region      : {region}")
        print(f"Population  : {population:,}")
        print(f"Currency    : {currencies}")
        print(f"{'='*40}")

    # --- SAVE RESPONSES ---
    save_to_file(weather_data, f"{city.lower()}_weather.json")
    if country_data:
        save_to_file(country_data, f"{city.lower()}_country.json")

    print("\nDone! Data saved for later use.")

if __name__ == "__main__":
    run_tool()