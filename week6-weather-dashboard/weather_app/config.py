import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"
CACHE_DIR = "data/cache"
DEFAULT_UNIT = "metric"  # metric = Celsius, imperial = Fahrenheit
