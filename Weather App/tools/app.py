from tools.location import Location
from tools.user_preference import UserPreference
from tools.api_client import APIClient

class WeatherApp:
    def __init__(self,api_key) -> None:
        self.api_client = APIClient(api_key)
        self.user_preference = UserPreference()
        self.cities = [
            Location("New York", "US"),
            Location("London", "UK"),
            Location("Tokyo", "JP"),
            Location("Paris", "FR"),
            Location("Sydney", "AU")
        ]

    def run(self):
        while True:
            print("\n 1. CHeck Weather \n2. Manage Preference \n 3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                self.select_city_and_display_weather()
            elif choice == '2':
                self.manage_preference()
            elif choice == '3':
                break
            else:
                print("Invalid Option, try again")

    def select_city_and_display_weather(self):
        print("\nSelect a city to check the weather")
        for i, city in enumerate(self.cities, start=1):
            print(f"{i}, {city}")
        
        # we ask the user to select a city with the number
        citychoice = int(input("Enter a number of the City"))-1

        if citychoice <= 0 and citychoice > len(self.cities):
            print("Invalid input. Please select a valid number")
        else:
            location = self.cities[citychoice]
            self.display_weather(location)
        
    def display_weather(self, location):
        weather_data = self.api_client.fetch_weather_data(location)

        if weather_data is None:
            print(f"Falied to retrieve weather data for {location}")
            return

        print(f"Weather in {location}: \n{weather_data}")

    def manage_preference(self):
        print("Manage preference action")
        

