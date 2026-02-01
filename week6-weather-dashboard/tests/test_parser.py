from weather_app.weather_parser import parse_current

def test_parse_current():
    sample = {
        "name": "Delhi",
        "main": {"temp": 30, "humidity": 50},
        "wind": {"speed": 3},
        "weather": [{"description": "clear sky"}]
    }
    parsed = parse_current(sample)
    assert parsed["city"] == "Delhi"
    assert parsed["temp"] == 30
    assert parsed["humidity"] == 50
    