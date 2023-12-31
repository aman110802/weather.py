import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data.")
        return None


def get_temperature(weather_data, date):
    for entry in weather_data["list"]:
        if date in entry["dt_txt"]:
            return entry["main"]["temp"]
    return None


def get_wind_speed(weather_data, date):
    for entry in weather_data["list"]:
        if date in entry["dt_txt"]:
            return entry["wind"]["speed"]
    return None


def get_pressure(weather_data, date):
    for entry in weather_data["list"]:
        if date in entry["dt_txt"]:
            return entry["main"]["pressure"]
    return None


def main():
    weather_data = get_weather_data()

    if not weather_data:
        return

    while True:
        print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(weather_data, date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature} Kelvin")
            else:
                print("No data available for the given date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("No data available for the given date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("No data available for the given date.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()