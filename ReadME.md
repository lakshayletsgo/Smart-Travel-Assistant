# 🌍 Travel Smart AI – Multimodal Multi-Agent Travel Planner

A Google ADK-based multi-agent system that takes a user’s travel goal (e.g., “Is Bali safe to visit next week?”), breaks it into subtasks, and routes data between intelligent agents to generate a rich, multimodal travel readiness report — including safety, weather, news, and image highlights.

---

## 🚀 Features

✅ Multi-Agent Architecture using Google ADK principles
✅ Goal-driven planning from natural language
✅ Weather Forecast from OpenWeatherMap API
✅ Safety & News Headlines via NewsAPI
✅ Location-based Image Summary via Unsplash API
✅ Synthesized final travel report with text + images
✅ Modular design — each agent is independently testable

---

## 🧠 How It Works

1. **User enters a travel goal**, e.g.:

   > “I want to travel to Bali next week. Is it safe? What’s the weather like? Show me some highlights.”
   > "Bali"

2. The **Planning Agent** splits this into tasks:

   * Get location and date
   * Check safety via news
   * Get 7-day weather forecast
   * Fetch latest related images
   * Combine and summarize

3. Each **agent executes in sequence**, enriching the result.

4. Final output is a **well-structured travel readiness report** with weather, news, and image summaries.

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
├── main.py                   # Entry point for agent orchestration
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

## ▶️ Run the App

```bash
python main.py
```

You’ll see a structured travel summary in your console.

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
BTech CS-AI | 3rd Year | [LinkedIn](https://www.linkedin.com/in/-lakshay-goel) | [Portfolio](https://lakshay-portfolio-five.vercel.app/)
