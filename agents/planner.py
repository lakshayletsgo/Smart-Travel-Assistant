def plan_from_goal(goal):
    plan = [
        {"task": "Extract location and date", "agent": "planner"},
        {"task": "Check recent safety news", "agent": "news_agent"},
        {"task": "Get weather forecast", "agent": "weather_agent"},
        {"task": "Find image-based news summary", "agent": "image_agent"},
        {"task": "Synthesize final report", "agent": "synthesizer"}
    ]
    return plan
