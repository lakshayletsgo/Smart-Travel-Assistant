import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_weather_forecast(location):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={api_key}"
    
    geo_res = requests.get(geocode_url).json()
    if not geo_res:
        return {"error": "Location not found."}
    
    lat, lon = geo_res[0]["lat"], geo_res[0]["lon"]
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    forecast = requests.get(forecast_url).json()
    summary = []
    for item in forecast["list"][:5]:
        summary.append({
            "datetime": item["dt_txt"],
            "temp": item["main"]["temp"],
            "weather": item["weather"][0]["description"]
        })
    return {"forecast": summary}
