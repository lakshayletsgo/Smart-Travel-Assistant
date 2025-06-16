def synthesize_report(location, news_data, weather_data, image_data):
    report = f"📍 **Travel Report for {location}**\n\n"

    # News
    report += "📰 **Safety & News**\n"
    for news in news_data["news_headlines"]:
        report += f"- {news['title']}\n"
    
    # Weather
    report += "\n☁️ **Weather Forecast**\n"
    for item in weather_data["forecast"]:
        report += f"- {item['datetime']}: {item['temp']}°C, {item['weather']}\n"
    
    # Images
    report += "\n🖼️ **Images**\n"
    for img in image_data["images"]:
        report += f"- {img['description']}: {img['image_url']}\n"
    
    return report
