import requests
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_tavily(query):
    url = "https://api.tavily.com/search"
    headers = {"Authorization": f"Bearer {TAVILY_API_KEY}"}
    params = {
        "query": query,
        "search_depth": "deep",
        "include_answer": True,
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    results = [doc['content'] for doc in data.get("results", [])]
    return results
