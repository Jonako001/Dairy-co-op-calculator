
# import requests


"""
url = "https://restcountries.com/v3.1/name/kenya"

response = requests.get(url)

print("Status code:", response.status_code)
print("Data received:", response.json())

"""
"""
import requests


url = "https://restcountries.com/api/v1/name/kenya"

response = requests.get(url)

print("Status:", response.status_code)
print(response.text)
"""


"""
print("Hello, World!")
"""

# Variables


"""
name = "Donald"
age = 27

print(name)
print(age)
"""

"""
name = input("Enter your name: ")
print("Hello", name)
"""


"""
a = 20
b = 30


print(a + b)
print(a - b)
print(a * b)
print(a / b)
"""


"""
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
"""


# Functions
"""
def greet():
    print("Welcome to Python")

greet()

"""

"""
def greet(name):
    print("Hello", name)


greet("Etabo")


"""

# Dictionaries

"""
student = {
    "name": "Etabo", "age": 22, "Course": "Community Resource Management"
}

print(student["name"])

"""

"""
import requests


print("Hello Python!")

"""


"""
import requests

url = "https://api.restcountries.com/countries/v5/names.common/kenya"


response = requests.get(url)

print("Status code:", response.status_code)
print("Data received:", response.json())

"""




"""
import requests

url = "https://restcountries.com/v3.1/name/kenya"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    country = data[0]

    name = country["name"]["common"]
    capital = country["capital"][0]
    population = country["population"]
    currency = list(country["currencies"].keys())[0]

    print(f"Country: {name}")
    print(f"Capital: {capital}")
    print(f"Population: {population:,}")
    print(f"Currency: {currency}")
else:
    print("Request failed. Status:", response.status_code)

"""


"""
import requests

url = "https://api.restcountries.com/countries/v5/name.com/kenya"

headers = {
    "Authorization": "Bearer rc_live_demo"
}

response = requests.get(url, headers=headers, timeout=20)

print("Status Code:", response.status_code)

response.raise_for_status()

data = response.json()
print(data)

"""


"""
import requests

url = "https://restcountries.com/v3.1/name/kenya"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    country = data[0]

    name = country["name"]["common"]
    capital = country["capital"][0]
    population = country["population"]
    currency = list(country["currencies"].keys())[0]

    print(f"Country: {name}")
    print(f"Capital: {capital}")
    print(f"Population: {population:,}")
    print(f"Currency: {currency}")
else:
    print("Request failed. Status:", response.status_code)

"""

"""
import requests

url = "https://api.restcountries.com/countries/v5/names.common/Kenya"

headers = {
    "Authorization": "Bearer rc_live_demo"
}

response = requests.get(url, headers=headers, timeout=20)

print("Status Code:", response.status_code)

response.raise_for_status()

result = response.json()

# Get the list of country records
countries = result["data"]["objects"]

# Select the first country
country = countries[0]

# Extract the information
name = country["names"]["common"]
capital = country["capitals"][0]
population = country["population"]
currency = country["currencies"][0]

print("Country:", name)
print("Capital:", capital)
print("Population:", population)
print("Currency:", currency)
"""



import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

print("Status code:", response.status_code)

user = response.json()


print("\nUSER PROFILE")
print("=" * 30)
print("Name:", user["name"])
print("Username:", user["username"])
print("Email:", user["email"])
print("Phone:", user["phone"])
print("Website:", user["website"])