from .weather_api import fetch_weather, fetch_forecast
from .weather_parser import parse_current, parse_forecast
from .weather_display import display_current, display_forecast

def main():
    unit = "metric"

    while True:
        print("\n--- WEATHER DASHBOARD ---")
        print("1. Current Weather")
        print("2. 5-Day Forecast")
        print("3. Change Units")
        print("4. Exit")

        choice = input("Choice: ")

        if choice in {"1", "2"}:
            city = input("Enter city: ").strip()

            try:
                if choice == "1":
                    data = fetch_weather(city, unit)
                    display_current(parse_current(data), unit)
                else:
                    data = fetch_forecast(city, unit)
                    display_forecast(parse_forecast(data), unit)

            except RuntimeError as e:
                print("❌ Error:", e)

        elif choice == "3":
            unit = "imperial" if unit == "metric" else "metric"
            print("Units switched.")

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
