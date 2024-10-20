import requests
import time
import json
from datetime import datetime
from weather_utils import convert_kelvin_to_celsius, send_alert

API_KEY = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
ALERT_THRESHOLD = 35  # Temperature threshold for alerts in Celsius

class WeatherMonitor:
    def __init__(self):
        self.weather_data = {city: [] for city in CITIES}

    def fetch_weather(self, city):
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            main_weather = data['weather'][0]['main']
            temp = convert_kelvin_to_celsius(data['main']['temp'])
            feels_like = convert_kelvin_to_celsius(data['main']['feels_like'])
            dt = datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
            return {'main': main_weather, 'temp': temp, 'feels_like': feels_like, 'dt': dt}
        else:
            print(f"Failed to get weather data for {city}: {response.status_code}")
            return None

    def monitor_weather(self):
        while True:
            for city in CITIES:
                weather = self.fetch_weather(city)
                if weather:
                    self.weather_data[city].append(weather)
                    print(f"Weather in {city}: {weather}")

                    # Check for alerts
                    if weather['temp'] > ALERT_THRESHOLD:
                        send_alert(city, weather['temp'])

            time.sleep(300)  # Fetch data every 5 minutes

if __name__ == "__main__":
    monitor = WeatherMonitor()
    monitor.monitor_weather()
