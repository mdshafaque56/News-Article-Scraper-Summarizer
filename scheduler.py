from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import fetch_aljazeera_news
from summarizer import summarize_article
import json


scheduler = BlockingScheduler()

def job():
    print("Fetching and summarizing news...")

    # Fetch news articles
    articles = fetch_aljazeera_news()

    # Summarize articles
    summarized_articles = []
    for article in articles[:20]:  # Limit to top 20
        summary = summarize_article(article["link"])
        summarized_articles.append({
            "title": article["title"],
            "summary": summary,
            "link": article["link"]
        })

    # Save to JSON
    with open("news_summaries.json", "w", encoding="utf-8") as file:
        json.dump(summarized_articles, file, indent=4)

    print("News updated successfully!")


scheduler.add_job(job, "interval", hours=1)  # Runs every 1 hour

print("Scheduler started...")
scheduler.start()
