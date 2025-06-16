import requests
import os
from dotenv import load_dotenv
load_dotenv()

def fetch_safety_news(location):
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={location}&apiKey={api_key}&language=en&pageSize=5"
    
    res = requests.get(url)
    data = res.json()
    
    headlines = []
    for article in data.get("articles", []):
        headlines.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        })
    
    return {
        "location": location,
        "news_headlines": headlines
    }
