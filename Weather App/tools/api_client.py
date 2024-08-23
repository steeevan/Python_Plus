import requests
from tools.weather_data import WeatherData

class APIClient:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather_data(self,location):
        params = {
            'q': f"{location.city}, {location.country}" if location.country else location.city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            print(f"Error: Unabe to fetch data. HTTP status code: {response.status_code}")
            print("Respone:", response.json())
            return None
        return self.parse_response(response.json())
    
    def parse_response(self,response):
        if 'main' not in response:
            print("Error: 'main' not found in response")
            print("Response: ",response)
            return None

        weather_data = response['main']
        wind_data = response['wind']
        weather_desc = response['weather'][0]['description']
        datetime = response['dt']

        receivedData = WeatherData( temperature=weather_data['temp'],
                                   humidity=weather_data['humidity'],
                                   pressure=weather_data['pressure'],
                                   wind_speed=wind_data['speed'],
                                   description=weather_desc,
                                   datetime=datetime
                                   )
        return receivedData