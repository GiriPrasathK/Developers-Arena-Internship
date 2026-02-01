def display_current(info, unit):
    symbol = "°C" if unit == "metric" else "°F"
    print("\n--- CURRENT WEATHER ---")
    print(f"City      : {info['city']}")
    print(f"Temp      : {info['temp']}{symbol}")
    print(f"Humidity  : {info['humidity']}%")
    print(f"Wind      : {info['wind']} m/s")
    print(f"Condition : {info['condition']}")

def display_forecast(forecast, unit):
    symbol = "°C" if unit == "metric" else "°F"
    print("\n--- 5 DAY FORECAST ---")
    for d, t in forecast.items():
        print(f"{d}: {t:.2f}{symbol}")
