import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

api_key = os.getenv("FASTFOREX_API_KEY")

if not api_key:
    print("ERROR: FASTFOREX_API_KEY not found in .env")
    exit()

# FastForex endpoint - this is the correct format
base = "KES"
url = f"https://api.fastforex.io/fetch-all?from={base}&api_key={api_key}"

try:
    response = requests.get(url, timeout=10)
    data = response.json()

    # Error handling 1: Invalid key
    if response.status_code == 401 or "Invalid API key" in str(data):
        print("401 - Invalid API key. Did you copy from API Keys page, not Account Settings?")
        print(f"Response: {data}")
        exit()

    # Error handling 2: Rate limit / quota
    if response.status_code == 429:
        print("429 - Too many requests, quota reached")
        exit()

    # Error handling 3: Bad currency code
    if response.status_code == 400:
        print(f"400 - Bad request: {data}")
        exit()

    if response.status_code != 200:
        print(f"Error {response.status_code}: {data}")
        exit()

    # SUCCESS
    results = data.get("results", {})
    print(f"\n--- Exchange Rates: Base {base} ---")
    print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"1 {base} = {results.get('USD', 0):.6f} USD")
    print(f"1 {base} = {results.get('EUR', 0):.6f} EUR")
    print(f"1 {base} = {results.get('GBP', 0):.6f} GBP")
    print(f"1 {base} = {results.get('UGX', 0):.2f} UGX")
    print(f"1 {base} = {results.get('TZS', 0):.2f} TZS")

    # DA use-case
    usd_to_kes = 1 / results.get('USD', 1)
    print(f"\n100 USD = {usd_to_kes * 100:.2f} KES")

except requests.exceptions.Timeout:
    print("Timeout - check internet")
except requests.exceptions.ConnectionError:
    print("Connection error")
