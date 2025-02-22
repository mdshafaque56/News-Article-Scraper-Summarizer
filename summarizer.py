from transformers import pipeline
import requests
from bs4 import BeautifulSoup

# Load the AI summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    paragraphs = soup.find_all("p")
    content = " ".join([p.get_text(strip=True) for p in paragraphs])
    
    if len(content) > 1024:  # Limit for summarization model
        content = content[:1024]

    summary = summarizer(content, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]
