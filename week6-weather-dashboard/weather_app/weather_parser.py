from datetime import datetime

def parse_current(data):
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"],
        "condition": data["weather"][0]["description"].title()
    }

def parse_forecast(data):
    daily = {}
    for item in data["list"]:
        date = item["dt_txt"].split(" ")[0]
        daily.setdefault(date, []).append(item["main"]["temp"])

    return {d: sum(t)/len(t) for d, t in daily.items()}
def format_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.strftime("%A, %B %d")
