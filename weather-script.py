import requests

API_KEY = '72c1b3e9e22cbc7a39120dcd12cb94ee'  # Replace with your actual API key
CITY = 'Phoenix'
COUNTRY_CODE = 'US'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY_CODE}&appid={API_KEY}&units=metric'

def fetch_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {CITY}: {data['weather'][0]['description'].title()}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("Failed to fetch weather data:", response.status_code, response.text)

if __name__ == "__main__":
    fetch_weather()