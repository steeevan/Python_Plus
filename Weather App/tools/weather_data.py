# weather_app/weather_data.py
class WeatherData:
    def __init__(self, temperature, humidity, pressure, wind_speed, description, datetime):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.wind_speed = wind_speed
        self.description = description
        self.datetime = datetime

    def __str__(self):
        return (f"Temperature: {self.temperature}°C\n"
                f"Humidity: {self.humidity}%\n"
                f"Pressure: {self.pressure} hPa\n"
                f"Wind Speed: {self.wind_speed} m/s\n"
                f"Description: {self.description}\n"
                f"Date/Time: {self.datetime}")
