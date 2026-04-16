import requests
import json
#1st Exercises
chuck_norris_url = "https://api.chucknorris.io/jokes/random"
chuck_norris_response = requests.get(chuck_norris_url).json()
print(chuck_norris_response['value'])
#3rd Exercises
prime_url = "http://127.0.0.1:5000/prime_number/12"
prime_response = requests.get(prime_url).json()
print(prime_response)
#2nd Exercises
city = input('Enter your city you want to see the weather: ')
url = (f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=e4c9a0ba5ee38e1433e7ddd5c60b6dea")
url_response = requests.get(url).json()
lat_city = url_response[0]['lat']
lon_city = url_response[0]['lon']
weather_url = (f"https://api.openweathermap.org/data/2.5/weather?lat={lat_city}&lon={lon_city}&appid=e4c9a0ba5ee38e1433e7ddd5c60b6dea")
weather_response = requests.get(weather_url).json()
weather_description = weather_response['weather'][0]['description']
#Celsius to Kelvin
daily_temperature = weather_response['main']['temp']
celsius = daily_temperature - 273.15
print(f'The weather description: {weather_description}, daily temperature {celsius:.2f} ℃')
#4th Exercises
airport_url = "http://127.0.0.1:5000/airport/00AK"
response = requests.get(airport_url).json()   
print(response)
