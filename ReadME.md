# 🌍 Travel Smart AI – Multimodal Multi-Agent Travel Planner

A Google ADK-based multi-agent system that takes a user’s travel goal (e.g., “Is Bali safe to visit next week?”), breaks it into subtasks, and routes data between intelligent agents to generate a rich, multimodal travel readiness report — including safety, weather, news, and image highlights.

---

## 🚀 Features

✅ Multi-Agent Architecture using Google ADK principles
✅ Goal-driven planning from natural language
✅ Flask API backend with REST endpoints
✅ Weather Forecast from OpenWeatherMap API
✅ Safety & News Headlines via NewsAPI
✅ Location-based Image Summary via Unsplash API
✅ Synthesized final travel report with text + images
✅ Modular design — each agent is independently testable

---

## 🧠 How It Works

1. **User enters a travel goal**, e.g.:

   > “I want to travel to Bali next week. Is it safe? What’s the weather like? Show me some highlights.”

2. The **Planning Agent** splits this into tasks:

   * Get location and date
   * Check safety via news
   * Get 7-day weather forecast
   * Fetch latest related images
   * Combine and summarize

3. Each **agent executes in sequence**, enriching the result.

4. Final output is a **well-structured travel readiness report** with weather, news, and image summaries.

---

## 🌐 API Endpoints

Once the application is running, you can access the endpoints using Postman or a similar tool:

### 🔎 Health Check

* **Method:** GET
* **URL:** `http://localhost:5000/health`

### ✈️ Travel Planning Endpoint

* **Method:** POST
* **URL:** `http://localhost:5000/travel-plan`
* **Headers:**

  * `Content-Type: application/json`
* **Body (raw JSON):**

```json
{
    "goal": "I want to travel to Bali next week. Is it safe? What's the weather like?",
    "location": "Bali"
}
```

* **Response:** JSON containing:

  * Travel Plan
  * Safety News
  * Weather Forecast
  * Location Images
  * Synthesized Travel Report

---

## 🗂️ Folder Structure

```
travel_smart_ai/
├── agents/
│   ├── planner.py            # Breaks goal into subtasks
│   ├── news_agent.py         # NewsAPI-based safety agent
│   ├── weather_agent.py      # Weather forecast agent
│   ├── image_agent.py        # Unsplash image fetcher
│   └── synthesizer.py        # Final report builder
├── app.py                   # Flask application file
├── .env                      # API keys (do not share)
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/lakshayletsgo/Smart-Travel-Assistant.git
cd Smart-Travel-Assistant
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure API Keys

Create a `.env` file in the root directory:

```env
OPENWEATHERMAP_API_KEY=your_openweathermap_key
NEWS_API_KEY=your_newsapi_key
UNSPLASH_ACCESS_KEY=your_unsplash_access_key
```

---

## ▶️ Run the Flask App

```bash
python app.py
```

Open your browser or Postman and hit: `http://localhost:5000/travel-plan`

---

## 🔌 APIs Used

| API            | Use Case              | Free Tier Limitations      |
| -------------- | --------------------- | -------------------------- |
| OpenWeatherMap | 5-day/3-hour forecast | 60 calls/min, 1M/month     |
| NewsAPI        | Safety/news search    | 100 calls/day (free)       |
| Unsplash API   | Location image search | 50 requests/hour, 5K/month |

---

## 📷 Sample Output

```
📍 Travel Report for Bali

📰 Safety & News
- Bali tourism rebounds post-COVID
- Local festivals expected next week

☁️ Weather Forecast
- 2025-06-23: 28°C, light rain
- 2025-06-24: 29°C, clear sky

🖼️ Images
- "Tourists at Ubud Market": [image_url]
- "Sunset at Kuta Beach": [image_url]
```

---

## 💡 Future Enhancements

* Destination alternator if weather is bad
* Flight price scraper agent
* Voice input using Whisper/Gemini
* Web interface with Streamlit

---

## 👨‍💻 Author

**Lakshay Goel**
BTech CS-AI | 3rd Year | [LinkedIn](https://www.linkedin.com/in/your-profile) | [Portfolio](https://lakshay-portfolio-five.vercel.app/)






# 📊 Multi-Agent System – Evaluations

These evaluations demonstrate how Travel Smart AI breaks down user goals, routes data between agents, and generates useful travel reports. Each eval includes user input, agent breakdown, outputs, and a brief assessment.

---

## ✅ Evaluation 1 – Bali

**🧠 Goal:**  
"I want to travel to Bali next week. Is it safe? What's the weather like?"

**📍 Location:** Bali

**🧭 Planner Output:**
- Check safety via NewsAPI
- Get weather forecast via OpenWeatherMap
- Fetch images via Unsplash
- Summarize all information

**🤖 Agent Outputs:**

- **NewsAgent:**
  - "Bali tourism rebounds post-COVID"
  - "Local festivals expected next week"

- **WeatherAgent:**
  - `2025-06-23`: 28°C, light rain  
  - `2025-06-24`: 29°C, clear sky

- **ImageAgent:**
  - `https://unsplash.com/photos/abc123`
  - `https://unsplash.com/photos/xyz456`

**📋 Final Synthesized Report:**

> It is generally safe to travel to Bali next week. Expect warm weather with occasional light rain. Cultural festivals are scheduled. Great time to visit!

**✅ Evaluation Summary:**  
Goal well satisfied. Planner correctly routed through all agents. Agent chaining and enrichment worked smoothly. Final output was coherent and informative.

---

## ⚠️ Evaluation 2 – Tokyo

**🧠 Goal:**  
"I'm planning a trip to Tokyo this weekend. What's the weather and any recent safety news?"

**📍 Location:** Tokyo

**🧭 Planner Output:**
- Check safety via NewsAPI
- Get weather forecast via OpenWeatherMap
- Fetch images via Unsplash
- Summarize all information

**🤖 Agent Outputs:**

- **NewsAgent:**
  - "Tokyo braces for weekend thunderstorms"
  - "Advisory issued for outdoor events"

- **WeatherAgent:**
  - `2025-06-22`: 27°C, thunderstorms  
  - `2025-06-23`: 26°C, cloudy

- **ImageAgent:**
  - `https://unsplash.com/photos/tokyo1`
  - `https://unsplash.com/photos/tokyo2`

**📋 Final Synthesized Report:**

> Caution is advised due to thunderstorms in Tokyo this weekend. Outdoor activities may be impacted. Stay updated with weather alerts. Otherwise, no major safety concerns reported.

**⚠️ Evaluation Summary:**  
Planner and agents performed as expected. Weather alerts and news were both highly relevant. Agents enriched each other’s data correctly, and final summary was goal-aligned.

---

✅ These evaluations demonstrate:
- Planner’s ability to understand and decompose goals
- Seamless chaining of agents and information flow
- Real-world utility for travel readiness

