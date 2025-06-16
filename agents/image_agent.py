import requests
import os
from dotenv import load_dotenv
load_dotenv()

def fetch_images(location):
    access_key = os.getenv("UNSPLASH_ACCESS_KEY")
    url = f"https://api.unsplash.com/search/photos?query={location}&client_id={access_key}&per_page=3"
    
    res = requests.get(url)
    data = res.json()
    
    images = []
    for result in data.get("results", []):
        images.append({
            "image_url": result["urls"]["regular"],
            "description": result["alt_description"] or "No caption"
        })
    return {"images": images}
