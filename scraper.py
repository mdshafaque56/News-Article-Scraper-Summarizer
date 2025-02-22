import requests
from bs4 import BeautifulSoup

# Function to fetch news from Al Jazeera
def fetch_aljazeera_news():
    url = "https://www.aljazeera.com/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for article in soup.select(".u-clickable-card__link"):  # Adjust selector if needed
        title = article.text.strip()
        link = article["href"]
        articles.append({"title": title, "link": f"https://www.aljazeera.com{link}"})
    
    return articles[:20]  # Return top 20

# Function to fetch news from BBC
def fetch_bbc_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for article in soup.select("a.gs-c-promo-heading"):  # Adjust selector
        title = article.text.strip()
        link = article["href"]
        articles.append({"title": title, "link": f"https://www.bbc.com{link}"})
    
    return articles[:20]

# Function to fetch news from Reuters
def fetch_reuters_news():
    url = "https://www.reuters.com/news/world"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    for article in soup.select("h3.story-title > a"):
        title = article.text.strip()
        link = article["href"]
        articles.append({"title": title, "link": f"https://www.reuters.com{link}"})
    
    return articles[:20]

# Master function to fetch all sources
def fetch_all_news():
    return {
        "Al Jazeera": fetch_aljazeera_news(),
        "BBC": fetch_bbc_news(),
        "Reuters": fetch_reuters_news(),
    }

