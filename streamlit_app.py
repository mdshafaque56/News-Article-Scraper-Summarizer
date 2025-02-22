import streamlit as st
import json

# Load the summarized news from a JSON file
def load_news():
    try:
        with open("news_summaries.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Streamlit UI
st.set_page_config(page_title="Latest News", layout="wide")

st.title("📰 Auto-News Crawler")

news_articles = load_news()

if not news_articles:
    st.warning("No news articles available. Please wait for the next update.")
else:
    for article in news_articles:
        with st.container():
            st.markdown(f"### {article['title']}")
            st.write(article["summary"])
            st.markdown(f"[Read more]({article['link']})")
            st.markdown("---")
