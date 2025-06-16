from flask import Flask, request, jsonify
from agents.planner import plan_from_goal
from agents.news_agent import fetch_safety_news
from agents.weather_agent import get_weather_forecast
from agents.image_agent import fetch_images
from agents.synthesizer import synthesize_report

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/travel-plan', methods=['POST'])
def create_travel_plan():
    try:
        data = request.get_json()
        if not data or 'goal' not in data:
            return jsonify({"error": "Missing 'goal' in request body"}), 400
            
        goal = data['goal']
        location = data.get('location', 'Bali')  # Default to Bali if no location provided
        
        # Get the travel plan
        plan = plan_from_goal(goal)
        
        # Fetch all required information
        news = fetch_safety_news(location)
        weather = get_weather_forecast(location)
        images = fetch_images(location)
        
        # Generate the final report
        report = synthesize_report(location, news, weather, images)
        
        response = {
            "goal": goal,
            "location": location,
            "plan": plan,
            "report": report,
            "details": {
                "news": news,
                "weather": weather,
                "images": images
            }
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
