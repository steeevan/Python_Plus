from tools.app import WeatherApp

def main():
    api_key = "99834530957fe028dee79256b18d306d"
    app = WeatherApp(api_key)
    app.run()

if __name__ == "__main__":
    main()
