import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetchNews():
    api_key = os.environ.get("GNEWS_API_KEY")
    url = f"https://gnews.io/api/v4/top-headlines?category=general&lang=en&country=in&max=5&apikey={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        # print("API raw response:", response.json())
        
        if "articles" in data:
            articles = data["articles"]
            print("\n--- Top 5 News Headlines ---")
            titles = []
            for i, article in enumerate(articles, start=1):
                title = article["title"]
                print(f"{i}. {title}")
                titles.append(title)
            return titles
        else:
            print("GNews API error:", data)
            return []
    
    except Exception as e:
        print(f"News fetch error: {e}")
        return []