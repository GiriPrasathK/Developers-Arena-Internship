import requests
import json
import os
import time
from .config import API_KEY, BASE_URL, CACHE_DIR

CACHE_EXPIRY = 600  # 10 minutes

def _cache_path(city, endpoint):
    return f"{CACHE_DIR}/{city.lower()}_{endpoint}.json"

def _is_cache_valid(path):
    return os.path.exists(path) and (time.time() - os.path.getmtime(path)) < CACHE_EXPIRY

def fetch_weather(city, unit="metric"):
    os.makedirs(CACHE_DIR, exist_ok=True)
    cache = _cache_path(city, "current")

    if _is_cache_valid(cache):
        with open(cache) as f:
            return json.load(f)

    try:
        res = requests.get(
            f"{BASE_URL}/weather",
            params={"q": city, "appid": API_KEY, "units": unit},
            timeout=5
        )
        res.raise_for_status()
        data = res.json()

        with open(cache, "w") as f:
            json.dump(data, f)

        return data

    except requests.RequestException as e:
        raise RuntimeError("Weather API error") from e


def fetch_forecast(city, unit="metric"):
    try:
        res = requests.get(
            f"{BASE_URL}/forecast",
            params={"q": city, "appid": API_KEY, "units": unit},
            timeout=5
        )
        res.raise_for_status()
        return res.json()
    except requests.RequestException:
        raise RuntimeError("Forecast API error")
