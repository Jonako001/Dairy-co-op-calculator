import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

if not api_key:
    print("ERROR: API key not found in .env")
    exit()

city = "Nairobi"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    print(f"Weather in {city}: {temp}C, {desc}, humidity {humidity}%")

elif response.status_code == 401:
    print("401 - Key invalid or not yet active. Wait 1-2 hours.")

elif response.status_code == 404:
    print(f"404 - City not found: {city}")

elif response.status_code == 429:
    print("429 - Too many requests.")

else:
    print(f"Error {response.status_code}: {response.text}")